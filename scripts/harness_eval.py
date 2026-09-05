#!/usr/bin/env python3
"""Small stdlib-only checks for ai-pipelines Harness v2.

This script deliberately does not call a model. It validates the repository's
routing fixtures, checks release/version consistency, summarizes repeated real
baseline-vs-candidate outcome records, and can detect reviewed-provider drift.
Real task runs must be produced by the harness/model environment being evaluated.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import statistics
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"
PROVIDERS = ROOT / "skills" / "design-pipeline" / "references" / "providers.json"
VERSION_FILE = ROOT / "VERSION"
SKILLS = ("task-execution", "design-pipeline")


class EvalError(RuntimeError):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise EvalError(f"{path}: {exc}") from exc


def frontmatter_version(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    in_frontmatter = False
    for line in text.splitlines():
        if line.strip() == "---":
            if not in_frontmatter:
                in_frontmatter = True
                continue
            break
        if in_frontmatter and line.strip().startswith("version:"):
            return line.split(":", 1)[1].strip()
    raise EvalError(f"{path}: metadata.version not found")


def check_versions() -> list[str]:
    errors: list[str] = []
    expected = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not expected:
        return ["VERSION is empty"]
    for skill in SKILLS:
        path = ROOT / "skills" / skill / "SKILL.md"
        try:
            actual = frontmatter_version(path)
        except (OSError, EvalError) as exc:
            errors.append(str(exc))
            continue
        if actual != expected:
            errors.append(f"{path}: version {actual!r} != VERSION {expected!r}")
    return errors


def check_fixture_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = load_json(path)
    except EvalError as exc:
        return [str(exc)]

    if not isinstance(data, dict):
        return [f"{path}: root must be an object"]
    if not isinstance(data.get("schema_version"), int):
        errors.append(f"{path}: schema_version must be an integer")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append(f"{path}: cases must be a non-empty array")
        return errors

    seen: set[str] = set()
    for index, case in enumerate(cases):
        where = f"{path}: cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{where}: must be an object")
            continue
        case_id = case.get("id")
        prompt = case.get("prompt")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{where}: missing non-empty id")
        elif case_id in seen:
            errors.append(f"{where}: duplicate id {case_id!r}")
        else:
            seen.add(case_id)
        if not isinstance(prompt, str) or not prompt.strip():
            errors.append(f"{where}: missing non-empty prompt")

        if "expect_host" in case and case["expect_host"] not in (None, "task-execution"):
            errors.append(f"{where}: unsupported expect_host {case['expect_host']!r}")
        if case.get("expect_domain") == "design-pipeline" and case.get("expect_host") not in (None, "task-execution"):
            errors.append(f"{where}: design-pipeline cannot replace the HOST")
        if case.get("max_primary_craft_providers_per_build_pass") not in (None, 1):
            errors.append(f"{where}: primary craft provider limit must be 1")

    return errors


def check_fixtures() -> list[str]:
    errors: list[str] = []
    files = sorted(EVALS.glob("**/*-cases.json"))
    if not files:
        return ["no eval JSON fixtures found"]
    for path in files:
        errors.extend(check_fixture_file(path))
    return errors


OUTCOME_REQUIRED = {
    "task_id": str,
    "variant": str,
    "success": bool,
    "false_completion": bool,
    "user_corrections": int,
    "unnecessary_files": int,
    "unnecessary_tests": int,
    "residue_items": int,
}


def validate_outcome_record(record: Any, index: int) -> list[str]:
    errors: list[str] = []
    where = f"record[{index}]"
    if not isinstance(record, dict):
        return [f"{where}: must be an object"]
    for key, typ in OUTCOME_REQUIRED.items():
        value = record.get(key)
        if type(value) is not typ:
            errors.append(f"{where}: {key} must be {typ.__name__}")
    if isinstance(record.get("variant"), str) and record["variant"] not in {"baseline", "candidate"}:
        errors.append(f"{where}: variant must be baseline or candidate")
    if isinstance(record.get("task_id"), str) and not record["task_id"].strip():
        errors.append(f"{where}: task_id must be non-empty")
    for key in ("user_corrections", "unnecessary_files", "unnecessary_tests", "residue_items"):
        if isinstance(record.get(key), int) and record[key] < 0:
            errors.append(f"{where}: {key} cannot be negative")
    for key in ("latency_seconds", "cost"):
        value = record.get(key)
        if value is not None and (
            not isinstance(value, (int, float))
            or isinstance(value, bool)
            or value < 0
            or (isinstance(value, float) and not math.isfinite(value))
        ):
            errors.append(f"{where}: {key} must be a finite non-negative number when present")
    pref = record.get("ui_preference")
    if pref is not None and (not isinstance(pref, str) or pref not in {"baseline", "candidate", "tie", "not_applicable"}):
        errors.append(f"{where}: invalid ui_preference {pref!r}")
    return errors


def mean(rows: list[dict[str, Any]], key: str) -> float | None:
    values = [float(row[key]) for row in rows if row.get(key) is not None]
    return statistics.fmean(values) if values else None


def outcome_summary(path: Path) -> int:
    data = load_json(path)
    if isinstance(data, dict) and data.get("example_only"):
        raise EvalError("example-only input is not real outcome evidence; supply observed runs")
    records = data.get("runs") if isinstance(data, dict) else data
    if not isinstance(records, list) or not records:
        raise EvalError("outcome input must be a non-empty array or {\"runs\": [...]} object")

    errors: list[str] = []
    for index, record in enumerate(records):
        errors.extend(validate_outcome_record(record, index))
    if errors:
        raise EvalError("\n".join(errors))

    by_variant: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_task: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for record in records:
        by_variant[record["variant"]].append(record)
        by_task[record["task_id"]][record["variant"]].append(record)

    print("Harness outcome summary — descriptive only; input evidence is not independently verified")
    print("======================")
    for variant in ("baseline", "candidate"):
        rows = by_variant.get(variant, [])
        if not rows:
            print(f"{variant}: no runs")
            continue
        successes = sum(1 for row in rows if row["success"])
        false_completion = sum(1 for row in rows if row["false_completion"])
        print(
            f"{variant}: n={len(rows)} success={successes/len(rows):.1%} "
            f"false_completion={false_completion/len(rows):.1%} "
            f"corrections={mean(rows, 'user_corrections'):.2f} "
            f"unnecessary_files={mean(rows, 'unnecessary_files'):.2f} "
            f"unnecessary_tests={mean(rows, 'unnecessary_tests'):.2f} "
            f"residue={mean(rows, 'residue_items'):.2f}"
        )
        latency = mean(rows, "latency_seconds")
        cost = mean(rows, "cost")
        if latency is not None or cost is not None:
            print(f"  mean latency={latency if latency is not None else 'n/a'}; cost={cost if cost is not None else 'n/a'}")

    paired = [task_id for task_id, variants in by_task.items() if variants.get("baseline") and variants.get("candidate")]
    print(f"paired tasks: {len(paired)}/{len(by_task)}")
    repeated = sum(all(len(by_task[task_id][v]) >= 2 for v in ("baseline", "candidate")) for task_id in paired)
    print(f"paired tasks with repeated runs in both variants: {repeated}/{len(paired)}")
    print("Pooled means may reflect different task mixes or run counts; they do not establish improvement.")
    if not paired:
        return 0

    candidate_wins = baseline_wins = ties = mixed = 0
    for task_id in paired:
        prefs = {
            r.get("ui_preference")
            for v in ("baseline", "candidate")
            for r in by_task[task_id][v]
            if r.get("ui_preference") in {"baseline", "candidate", "tie"}
        }
        if len(prefs) > 1:
            mixed += 1
            continue
        if prefs:
            pref = next(iter(prefs))
            candidate_wins += pref == "candidate"
            baseline_wins += pref == "baseline"
            ties += pref == "tie"
    if candidate_wins or baseline_wins or ties or mixed:
        print(f"UI preference by paired task (not votes): candidate={candidate_wins} baseline={baseline_wins} tie={ties} mixed={mixed}")

    print("Interpret dimensions separately; do not collapse these numbers into one universal quality score.")
    return 0


def github_repo_from_source(source: str) -> tuple[str, str] | None:
    prefix = "https://github.com/"
    if not source.startswith(prefix):
        return None
    parts = source[len(prefix):].strip("/").split("/")
    if len(parts) < 2:
        return None
    return parts[0], parts[1]


def github_default_head(owner: str, repo: str) -> tuple[str, str]:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "ai-pipelines-harness-eval"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    repo_req = urllib.request.Request(f"https://api.github.com/repos/{owner}/{repo}", headers=headers)
    with urllib.request.urlopen(repo_req, timeout=15) as response:
        meta = json.load(response)
    branch = meta["default_branch"]

    commit_req = urllib.request.Request(f"https://api.github.com/repos/{owner}/{repo}/commits/{branch}", headers=headers)
    with urllib.request.urlopen(commit_req, timeout=15) as response:
        commit = json.load(response)
    return branch, commit["sha"]


def provider_drift() -> int:
    data = load_json(PROVIDERS)
    providers = data.get("providers", {})
    if not isinstance(providers, dict):
        raise EvalError("providers.json: providers must be an object")

    drifted = 0
    checked = 0
    for name, provider in providers.items():
        if not isinstance(provider, dict):
            continue
        source = provider.get("source")
        reviewed_ref = provider.get("reviewed_ref")
        if not isinstance(source, str) or not isinstance(reviewed_ref, str):
            continue
        repo = github_repo_from_source(source)
        if not repo:
            continue
        checked += 1
        try:
            branch, head = github_default_head(*repo)
        except (urllib.error.URLError, urllib.error.HTTPError, KeyError, TimeoutError) as exc:
            print(f"{name}: ERROR checking upstream: {exc}", file=sys.stderr)
            return 3
        if head == reviewed_ref:
            print(f"{name}: current ({branch} {head[:12]})")
        else:
            drifted += 1
            print(f"{name}: DRIFTED reviewed={reviewed_ref[:12]} upstream={head[:12]} branch={branch}")
    print(f"checked={checked} drifted={drifted}")
    return 2 if drifted else 0


def static_check() -> int:
    errors = check_versions() + check_fixtures()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    fixture_count = len(list(EVALS.glob("**/*-cases.json")))
    print("Structural validation only: no model behavior or outcome quality was evaluated.")
    print(f"OK: version={VERSION_FILE.read_text(encoding='utf-8').strip()} fixtures={fixture_count}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("check", help="validate VERSION/skill metadata and all eval fixture files")
    outcomes = sub.add_parser("outcomes", help="summarize repeated real baseline/candidate run records")
    outcomes.add_argument("path", type=Path)
    sub.add_parser("provider-drift", help="compare reviewed GitHub provider refs with current default-branch HEADs")

    args = parser.parse_args()
    try:
        if args.command == "check":
            return static_check()
        if args.command == "outcomes":
            return outcome_summary(args.path)
        if args.command == "provider-drift":
            return provider_drift()
    except (EvalError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
