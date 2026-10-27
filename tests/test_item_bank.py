"""Kontrola integralności roboczych banków DERA-HRI bez zależności."""

import csv
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "instruments"
VERSIONS = {
    "v2": ("dera_hri_v2.csv", {12, 17, 23, 31, 34, 36, 41, 42, 43}),
    "v2.1": ("dera_hri_v2_1.csv", {6, 12, 17, 23, 31, 32, 34, 36, 41, 42, 43}),
}


class ItemBankTest(unittest.TestCase):
    def test_source_structure(self):
        for version, (filename, source_reverse) in VERSIONS.items():
            with self.subTest(version=version):
                with (ROOT / filename).open(encoding="utf-8", newline="") as file:
                    rows = list(csv.DictReader(file))

                self.assertEqual(len(rows), 48)
                self.assertEqual([int(row["id"]) for row in rows], list(range(1, 49)))
                self.assertEqual(
                    dict(Counter(row["scale"] for row in rows)),
                    {"EAR-D": 12, "SAP-D": 12, "SEI-D": 12, "RAR-D": 12},
                )
                self.assertEqual(
                    {int(row["id"]) for row in rows if row["reverse"] == "true"},
                    source_reverse,
                )
                self.assertTrue(
                    all(
                        row["text_pl"].strip()
                        and row["domain"].strip()
                        and row["reverse"] in {"true", "false"}
                        for row in rows
                    )
                )


if __name__ == "__main__":
    unittest.main()
