"""Sprawdzenie integralności banku v2, bez zewnętrznych zależności."""

import csv
import unittest
from collections import Counter
from pathlib import Path

BANK = Path(__file__).resolve().parents[1] / "instruments" / "dera_hri_v2.csv"
EXPECTED_REVERSED = {12, 17, 23, 31, 34, 36, 41, 42, 43}


class ItemBankTest(unittest.TestCase):
    def test_v2_structure(self):
        with BANK.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))

        self.assertEqual(len(rows), 48)
        self.assertEqual([int(row["id"]) for row in rows], list(range(1, 49)))
        self.assertEqual(
            dict(Counter(row["scale"] for row in rows)),
            {"EAR-D": 12, "SAP-D": 12, "SEI-D": 12, "RAR-D": 12},
        )
        self.assertEqual(
            {int(row["id"]) for row in rows if row["reverse"] == "true"},
            EXPECTED_REVERSED,
        )
        self.assertTrue(all(row["text_pl"].strip() and row["domain"].strip() for row in rows))
        self.assertTrue(all(row["reverse"] in {"true", "false"} for row in rows))


if __name__ == "__main__":
    unittest.main()
