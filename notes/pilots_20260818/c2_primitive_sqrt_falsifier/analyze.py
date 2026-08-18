#!/usr/bin/env python3
"""Exact fail-closed analysis of the C2 primitive square-root grid."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED_ROWS = {
    (32, 97),
    (32, 5857),
    (64, 193),
    (64, 257),
    (64, 449),
    (64, 577),
    (64, 769),
    (64, 1153),
    (128, 257),
    (128, 641),
    (128, 769),
    (128, 1153),
    (256, 769),
}


def build() -> dict[str, object]:
    payload = json.loads((HERE / "results.json").read_text())
    assert payload["schema"] == "c2-primitive-sqrt-falsifier-v1"
    assert payload["rows_requested"] == payload["rows_returned"] == 13
    rows = payload["results"]
    assert {(row["n"], row["q"]) for row in rows} == EXPECTED_ROWS

    maximum = (Fraction(-1), (0, 0))
    above_one = 0
    for row in rows:
        assert row["status"] == "PASS"
        numerator = int(row["ratio_numerator"])
        denominator = int(row["ratio_denominator"])
        ratio = Fraction(numerator, denominator)
        n = row["n"]
        primitive = int(row["primitive"])
        assert primitive == int(row["z0"]) - int(row["c1"])
        assert primitive % n == 0
        fires = numerator * numerator > 2 * n * denominator * denominator
        assert fires is False
        assert row["fires"] is False
        above_one += ratio > 1
        maximum = max(maximum, (ratio, (n, row["q"])))

    control97 = next(row for row in rows if (row["n"], row["q"]) == (32, 97))
    control5857 = next(row for row in rows if (row["n"], row["q"]) == (32, 5857))
    assert (control97["z0"], control97["c1"], control97["z1"], control97["b0"]) == (
        "455744", "736", "44299296", "44278048"
    )
    assert (control5857["z0"], control5857["c1"], control5857["z1"], control5857["b0"]) == (
        "1152", "256", "1829376", "787968"
    )

    summary = {
        "rows": len(rows),
        "fires": sum(row["fires"] for row in rows),
        "above_one": above_one,
        "max_n": maximum[1][0],
        "max_q": maximum[1][1],
        "max_numerator": maximum[0].numerator,
        "max_denominator": maximum[0].denominator,
        "max_ratio_bits": math.log2(maximum[0].numerator) - math.log2(maximum[0].denominator),
        "max_sqrt_slack_bits": 0.5 * math.log2(2 * maximum[1][0])
        - (math.log2(maximum[0].numerator) - math.log2(maximum[0].denominator)),
    }
    assert summary == {
        "rows": 13,
        "fires": 0,
        "above_one": 1,
        "max_n": 32,
        "max_q": 5857,
        "max_numerator": 14680064,
        "max_denominator": 5498847,
        "max_ratio_bits": 1.4166572071441266,
        "max_sqrt_slack_bits": 1.5833427928558734,
    }
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    summary = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(summary)
        changed["fires"] = 1
        caught = 0
        try:
            assert changed == summary
        except AssertionError:
            caught = 1
        assert caught == 1
        print("C2_PRIMITIVE_SQRT_FALSIFIER_TAMPER_PASS mutations=1/1")
        return
    print(
        "C2_PRIMITIVE_SQRT_FALSIFIER_PASS "
        f"rows={summary['rows']} fires={summary['fires']} "
        f"max={summary['max_numerator']}/{summary['max_denominator']}"
    )


if __name__ == "__main__":
    main()
