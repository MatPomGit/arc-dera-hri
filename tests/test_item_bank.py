"""Kontrola struktury źródłowych banków DERA-HRI (bez walidacji psychometrycznej)."""

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
    def test_historical_banks(self):
        for version, (filename, reverses) in VERSIONS.items():
            with self.subTest(version=version):
                with (ROOT / filename).open(encoding="utf-8", newline="") as handle:
                    items = list(csv.DictReader(handle))
                self.assertEqual([int(row["id"]) for row in items], list(range(1, 49)))
                self.assertEqual(
                    dict(Counter(row["scale"] for row in items)),
                    {"EAR-D": 12, "SAP-D": 12, "SEI-D": 12, "RAR-D": 12},
                )
                self.assertEqual(
                    {int(row["id"]) for row in items if row["reverse"] == "true"},
                    reverses,
                )
                self.assertTrue(all(row["text_pl"].strip() for row in items))

    def test_v3_pl_translation(self):
        with (ROOT / "dera_hri_v3.csv").open(
            encoding="utf-8", newline=""
        ) as source:
            english = list(csv.DictReader(source))
        with (ROOT / "dera_hri_v3_pl.csv").open(
            encoding="utf-8", newline=""
        ) as source:
            polish = list(csv.DictReader(source))

        self.assertEqual(len(polish), 49)
        self.assertEqual(
            [row["item_id"] for row in polish],
            [row["item_id"] for row in english],
        )
        for original, translation in zip(english, polish):
            with self.subTest(item=original["item_id"]):
                self.assertEqual(translation["scale"], original["scale"])
                self.assertEqual(
                    translation["condition"], original["condition"]
                )
                self.assertTrue(translation["text_pl"].strip())
                self.assertNotEqual(
                    translation["text_pl"], original["text_en"]
                )

    def test_v3_bank(self):
        with (ROOT / "dera_hri_v3.csv").open(encoding="utf-8", newline="") as handle:
            items = list(csv.DictReader(handle))

        core = [row for row in items if row["item_id"].isdecimal()]
        extra = [row for row in items if not row["item_id"].isdecimal()]
        self.assertEqual([int(row["item_id"]) for row in core], list(range(1, 46)))
        self.assertEqual(
            dict(Counter(row["scale"] for row in core)),
            {"EAR-D": 11, "SEI-D": 12, "SAP-D": 10, "MP-D": 4, "RAR-D": 8},
        )
        self.assertEqual([row["item_id"] for row in extra], ["M1", "M2", "M3", "F1"])
        self.assertEqual(
            {row["item_id"]: row["condition"] for row in core if row["condition"] != "always"},
            {
                "12": "movement",
                "13": "voice",
                "14": "gestures",
                "15": "facial_expressions",
                "16": "multichannel_review",
            },
        )
        self.assertTrue(all(row["source_reverse"] == "false" for row in items))
        self.assertTrue(all(row["text_en"].strip() for row in items))


if __name__ == "__main__":
    unittest.main()
