#!/usr/bin/env python3
"""Independent ledger checks for the normalized c=2 small-order census."""

from __future__ import annotations

from hashlib import sha256
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RESULT = HERE / "rate_half_list_fiber_two_cycle_c2_normalized_small_order_census_result.json"


def main() -> None:
    payload = json.loads(RESULT.read_text())
    script = ROOT / payload["script"]
    assert sha256(script.read_bytes()).hexdigest() == payload["script_sha256"]

    rows = payload["rows"]
    expected_rows = {
        (prime, height)
        for prime in (2017, 12097)
        for height in (3, 4, 7, 8, 10)
    }
    expected_rows.update({(97, 7), (113, 8), (257, 9), (641, 9)})
    assert {(row["p"], row["H"]) for row in rows} == expected_rows

    for row in rows:
        assert row["N"] == 8 * row["H"] - 8
        assert (row["p"] - 1) % (2 * row["N"]) == 0
        assert row["sets"] == comb(row["N"] - 1, 3)
        assert row["sets"] == sum(
            row[key]
            for key in (
                "primary_fail",
                "secondary_fail",
                "span_fail",
                "canonical_pass",
            )
        )
        witness = row["stage_witness"]
        if witness is None:
            assert row["primary_fail"] == row["sets"]
            continue
        assert len(set(witness)) == 4 and 1 in witness
        pure = False
        if row["p"] - 1 in witness:
            nonreal = [
                value for value in witness if value not in (1, row["p"] - 1)
            ]
            pure = (
                len(nonreal) == 2
                and (nonreal[0] + nonreal[1]) % row["p"] == 0
                and nonreal[0] * nonreal[0] % row["p"] == row["p"] - 1
            )
        assert pure == row.get("witness_pure", True)

    totals = payload["totals"]
    assert totals["normalized_quartets"] == sum(row["sets"] for row in rows)
    assert totals["primary_fail"] == sum(row["primary_fail"] for row in rows)
    assert totals["primary_pass"] == totals["normalized_quartets"] - totals["primary_fail"]
    assert totals["secondary_fail"] == sum(row["secondary_fail"] for row in rows)
    assert totals["span_fail"] == sum(row["span_fail"] for row in rows)
    assert totals["nonpure_primary_pass"] == 12
    assert totals["secondary_nonpure_pass"] == 0
    assert totals["canonical_pass"] == 0
    assert totals["coupled_pair_pass"] == 0

    print(
        "RATE_HALF_LIST_C2_NORMALIZED_SMALL_ORDER_CENSUS_CHECK_PASS "
        f"rows={len(rows)} quartets={totals['normalized_quartets']} "
        f"primary_survivors={totals['primary_pass']} canonical_survivors=0"
    )


if __name__ == "__main__":
    main()
