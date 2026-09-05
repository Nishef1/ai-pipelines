"""Behavioral regression checks for outcome reporting, not prompt wording."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('harness_eval', Path(__file__).resolve().parents[1] / 'scripts/harness_eval.py')
eval_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eval_module)


def record(**updates):
    row = dict(task_id='task', variant='baseline', success=True,
               false_completion=False, user_corrections=0, unnecessary_files=0,
               unnecessary_tests=0, residue_items=0)
    return row | updates


class OutcomeReportingTests(unittest.TestCase):
    def summarize(self, data):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'runs.json'
            path.write_text(json.dumps(data))
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = eval_module.outcome_summary(path)
            return result, output.getvalue()

    def test_example_cannot_be_reported_as_real_outcomes(self):
        with self.assertRaises(eval_module.EvalError):
            self.summarize({'example_only': True, 'runs': [record()]})

    def test_invalid_metrics_are_rejected_without_crashing(self):
        for changes in ({'cost': float('nan')}, {'latency_seconds': float('inf')},
                        {'ui_preference': []}, {'task_id': ' '}, {'cost': True}):
            with self.subTest(changes=changes):
                self.assertTrue(eval_module.validate_outcome_record(record(**changes), 0))

    def test_repeated_tasks_may_have_different_preferences(self):
        # Different runs/judges can prefer different versions; this is variance.
        rows = [record(ui_preference='baseline'),
                record(variant='candidate', ui_preference='candidate')]
        result, output = self.summarize(rows)
        self.assertEqual(result, 0)
        self.assertIn('mixed=1', output)

    def test_single_or_unpaired_runs_are_not_comparative_proof(self):
        _, output = self.summarize([record()])
        self.assertIn('descriptive only', output)
        _, output = self.summarize([record(), record(variant='candidate')])
        self.assertIn('repeated runs in both variants: 0/1', output)


if __name__ == '__main__':
    unittest.main()
