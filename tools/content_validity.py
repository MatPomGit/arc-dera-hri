"""Summarize expert CVR/CVI ratings. No individual responses leave the local machine.

Usage: python tools/content_validity.py data/E01.csv data/E02.csv > data/summary.csv
One filled copy of instruments/dera_hri_v3_expert_form.csv per expert.
"""
import argparse
import csv
import math
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "instruments" / "dera_hri_v3.csv"
COLUMNS = ("essentiality", "relevance", "clarity", "simplicity")
SCALE = ("EAR-D", "SEI-D", "SAP-D", "MP-D", "RAR-D")


def load_bank():
    with BANK.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    return {row["item_id"]: row for row in rows}


def exact_p(ne, n):
    """Pr(X >= ne | Binomial(n, 0.5)); not an estimate of content validity."""
    if not 0 <= ne <= n or n < 1:
        raise ValueError("Invalid counts for exact binomial test")
    return math.fsum(math.comb(n, k) for k in range(ne, n + 1)) / 2**n


def load_ratings(paths, bank):
    """Require complete, untampered item inventories; allow unanswered ratings."""
    values = defaultdict(list)
    for path in paths:
        with Path(path).open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            expected = {
                "item_id", "scale", "scope", "condition", "text_en",
                "essentiality", "relevance", "clarity", "simplicity",
                "assigned_domain", "comment",
            }
            if not reader.fieldnames or not expected.issubset(reader.fieldnames):
                raise ValueError(f"{path}: incomplete form headers")
            rows = list(reader)
        ids = [row["item_id"] for row in rows]
        if len(rows) != len(bank) or set(ids) != set(bank) or len(set(ids)) != len(ids):
            raise ValueError(f"{path}: item list differs from canonical v3")
        for row in rows:
            item = bank[row["item_id"]]
            if (
                row["scale"] != item["scale"]
                or row["condition"] != item["condition"]
                or row["text_en"] != item["text_en"]
                or row["scope"] != (
                    "core" if row["item_id"].isdecimal() else "supplementary"
                )
            ):
                raise ValueError(f"{path}: changed item {row['item_id']}")
            essentiality = row["essentiality"].strip().lower()
            if essentiality not in {"", "essential", "useful", "not_necessary"}:
                raise ValueError(f"{path}: invalid essentiality at {row['item_id']}")
            scores = {}
            for key in COLUMNS[1:]:
                value = row[key].strip()
                if value and value not in {"1", "2", "3", "4"}:
                    raise ValueError(f"{path}: invalid {key} at {row['item_id']}")
                scores[key] = int(value) if value else None
            values[row["item_id"]].append((essentiality, scores))
    return values


def summarize(bank, responses):
    """No scores for unanswered items; no automatic item keep/delete decision."""
    output = []
    for item_id, row in bank.items():
        assessments = responses.get(item_id, [])
        essential = [v[0] for v in assessments if v[0]]
        n = len(essential)
        ne = sum(v == "essential" for v in essential)
        result = {
            "item_id": item_id,
            "scale": row["scale"],
            "scope": "core" if item_id.isdecimal() else "supplementary",
            "n_essentiality": n,
            "n_essential": ne if n else "",
            "cvr": round(2 * ne / n - 1, 6) if n else "",
            "p_exact": round(exact_p(ne, n), 6) if n else "",
        }
        for dimension in COLUMNS[1:]:
            scores = [v[1][dimension] for v in assessments if v[1][dimension] is not None]
            count = len(scores)
            result[f"n_{dimension}"] = count
            result[f"i_cvi_{dimension}"] = (
                round(sum(value >= 3 for value in scores) / count, 6)
                if count else ""
            )
        output.append(result)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ratings", nargs="+", help="One private CSV file per expert")
    args = parser.parse_args()
    bank = load_bank()
    try:
        ratings = load_ratings(args.ratings, bank)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    results = summarize(bank, ratings)
    columns = list(results[0])
    writer = csv.DictWriter(sys.stdout, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    writer.writerows(results)

    for scale in SCALE:
        rows = [r for r in results if r["scale"] == scale]
        for dimension in COLUMNS[1:]:
            values = [r[f"i_cvi_{dimension}"] for r in rows
                      if r[f"i_cvi_{dimension}"] != ""]
            if values:
                mean = math.fsum(values) / len(values)
                print(
                    f"S-CVI/Ave {scale} {dimension}: {mean:.3f} "
                    f"({len(values)}/{len(rows)} rated items)",
                    file=sys.stderr,
                )
    print(
        f"Experts supplied: {len(args.ratings)}. "
        "CVR p_exact uses one-sided Binomial(n, 0.5); "
        "no automatic acceptance decision.",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
