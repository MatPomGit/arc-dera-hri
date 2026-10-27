"""Tests for v3 review form and reproducible CVR/CVI summaries."""
import csv
import tempfile
import unittest
from pathlib import Path

from tools.content_validity import exact_p, load_bank, load_ratings, summarize

ROOT = Path(__file__).resolve().parents[1]
FORM = ROOT / "instruments" / "dera_hri_v3_expert_form.csv"


class ContentValidityTests(unittest.TestCase):
    def test_form_matches_canonical_bank(self):
        bank = load_bank()
        with FORM.open(encoding="utf-8", newline="") as handle:
            form = list(csv.DictReader(handle))
        self.assertEqual(len(form), 49)
        self.assertEqual([row["item_id"] for row in form], list(bank))
        for row in form:
            base = bank[row["item_id"]]
            self.assertEqual(row["text_en"], base["text_en"])
            self.assertEqual(row["scale"], base["scale"])
            self.assertEqual(row["condition"], base["condition"])
            self.assertEqual(row["scope"], (
                "core" if row["item_id"].isdecimal() else "supplementary"
            ))
            self.assertTrue(all(
                not row[name] for name in (
                    "essentiality", "relevance", "clarity", "simplicity",
                    "assigned_domain", "comment",
                )
            ))

    def test_cognitive_log_matches_v3(self):
        path = ROOT / "instruments" / "dera_hri_v3_cognitive_log.csv"
        bank = load_bank()
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 49)
        self.assertEqual([row["item_id"] for row in rows], list(bank))
        empty = (
            "session_code", "applicable", "answer_1_7", "problem_codes",
            "severity_0_3", "participant_paraphrase",
            "interviewer_observation", "proposed_revision",
        )
        for row in rows:
            source = bank[row["item_id"]]
            self.assertEqual(row["text_en"], source["text_en"])
            self.assertEqual(row["scale"], source["scale"])
            self.assertEqual(row["condition"], source["condition"])
            self.assertEqual(
                row["scope"],
                "core" if row["item_id"].isdecimal() else "supplementary",
            )
            self.assertTrue(all(not row[field] for field in empty))

    def test_domain_coverage_form(self):
        path = ROOT / "instruments" / "dera_hri_v3_domain_review.csv"
        with path.open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(
            [r["scale"] for r in rows],
            ["EAR-D", "SEI-D", "SAP-D", "MP-D", "RAR-D"],
        )
        self.assertTrue(all(row["definition_en"] for row in rows))
        self.assertTrue(all(
            all(not row[field] for field in (
                "coverage_1_4", "missing_facets", "overlap_with_other_scale",
                "context_or_channel_issues", "comment",
            ))
            for row in rows
        ))

    def test_exact_binomial_critical_counts(self):
        for n, cutoff in [(12, 10), (13, 10), (14, 11), (15, 12)]:
            with self.subTest(n=n):
                self.assertLessEqual(exact_p(cutoff, n), 0.05)
                self.assertGreater(exact_p(cutoff - 1, n), 0.05)
        self.assertAlmostEqual(exact_p(1, 2), 0.75)

    def test_minimal_private_example_and_missingness(self):
        bank = load_bank()
        with FORM.open(encoding="utf-8", newline="") as handle:
            template = list(csv.DictReader(handle))
            fields = list(template[0])
        with tempfile.TemporaryDirectory() as directory:
            paths = []
            for idx, (ess, rel, clear, simple) in enumerate([
                ("essential", "4", "3", "3"),
                ("useful", "2", "4", "1"),
            ]):
                path = Path(directory) / f"E0{idx + 1}.csv"
                with path.open("w", encoding="utf-8", newline="") as stream:
                    writer = csv.DictWriter(stream, fieldnames=fields)
                    writer.writeheader()
                    for item in template:
                        row = dict(item)
                        if row["item_id"] == "1":
                            row.update(
                                essentiality=ess, relevance=rel,
                                clarity=clear, simplicity=simple,
                            )
                        writer.writerow(row)
                paths.append(path)
            results = summarize(bank, load_ratings(paths, bank))
        first, second = results[0], results[1]
        self.assertEqual(first["n_essentiality"], 2)
        self.assertEqual(first["cvr"], 0)
        self.assertAlmostEqual(first["i_cvi_relevance"], 0.5)
        self.assertAlmostEqual(first["i_cvi_clarity"], 1.0)
        self.assertAlmostEqual(first["i_cvi_simplicity"], 0.5)
        self.assertEqual(second["n_essentiality"], 0)
        self.assertEqual(second["cvr"], "")
        self.assertEqual(second["i_cvi_relevance"], "")


if __name__ == "__main__":
    unittest.main()
