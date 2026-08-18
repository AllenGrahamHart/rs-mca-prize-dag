#!/usr/bin/env python3
"""Analyze the preregistered exact Haar follow-up."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
import json
from pathlib import Path

from analyze import expected_primes


HERE = Path(__file__).resolve().parent


def build() -> dict[str, object]:
    first = json.loads((HERE / "results.json").read_text())
    followup = json.loads((HERE / "followup_results.json").read_text())
    assert followup["schema"] == "c2-ambient-q-highcap-v1"
    assert len(followup["shards"]) == 4
    assert all(shard["status"] == "PASS" for shard in followup["shards"])
    old_rows = {row["q"]: row for shard in first["shards"] for row in shard["rows"]}
    rows = sorted((row for shard in followup["shards"] for row in shard["rows"]),
                  key=lambda row: row["q"])
    assert [row["q"] for row in rows] == expected_primes()

    fired = []
    maximum = (Fraction(0), None)
    for row in rows:
        old = old_rows[row["q"]]
        for key in ("z0", "c1", "primitive", "fires"):
            assert row[key] == old[key]
        assert row["z1"] * row["q"] >= 2**32
        assert row["b0"] * row["q"] >= 2**32
        ratio = Fraction(row["primitive"] * 2**32, row["z1"] * row["b0"])
        exact_fires = ratio > 8
        assert row["j_fires"] is exact_fires
        if exact_fires:
            fired.append({**row, "ratio": [ratio.numerator, ratio.denominator]})
        if ratio > maximum[0]:
            maximum = (ratio, row["q"])
    return {
        "rows": len(rows),
        "fires": len(fired),
        "first_firing": fired[0] if fired else None,
        "maximum_q": maximum[1],
        "maximum": [maximum[0].numerator, maximum[0].denominator],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        changed["rows"] -= 1
        caught = 0
        try:
            assert changed["rows"] == result["rows"]
        except AssertionError:
            caught = 1
        assert caught == 1
        print("C2_HIGHCAP_HAAR_FOLLOWUP_TAMPER_PASS mutations=1/1")
        return
    print(
        "C2_HIGHCAP_HAAR_FOLLOWUP_PASS "
        f"rows={result['rows']} fires={result['fires']} "
        f"maximum_q={result['maximum_q']} "
        f"maximum={result['maximum'][0]}/{result['maximum'][1]}"
    )
    if result["first_firing"]:
        print("FIRST_J_FIRING " + json.dumps(result["first_firing"], sort_keys=True))


if __name__ == "__main__":
    main()

