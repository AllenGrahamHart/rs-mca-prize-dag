#!/usr/bin/env python3
"""Verify the bounded m=2 bad-overlap Modal campaign packet."""

import json
from pathlib import Path


RESULT = Path(__file__).with_name("rh_bivariate_m2_badpattern_result.json")
EXPECTED = {
    "attempted": 1276996,
    "regular_incidence": 841449,
    "open_pair": 1795113,
    "bad_overlap": 1795113,
    "rank_deficient": 0,
    "blockwise_kernel": 0,
    "degree_extension": 0,
    "full_witness": 0,
}


def main() -> None:
    packet = json.loads(RESULT.read_text())
    assert packet["schema"] == "rate-half-bivariate-m2-badpattern-v1"
    assert packet["complete"] and packet["error"] is None
    assert packet["completed_tasks"] == packet["parameters"]["tasks"] == 32
    assert packet["parameters"]["field"] == 97
    assert packet["parameters"]["m"] == 2
    assert [row["seed"] for row in packet["rows"]] == list(range(32))
    assert all(not row["witnesses"] for row in packet["rows"])

    totals = {
        key: sum(int(row["counters"][key]) for row in packet["rows"])
        for key in EXPECTED
    }
    assert totals == packet["totals"] == EXPECTED
    assert totals["bad_overlap"] == totals["open_pair"]
    assert totals["rank_deficient"] == 0
    print(
        "RATE_HALF_BIVARIATE_M2_BADPATTERN_RESULT_PASS "
        f"trials={totals['attempted']} bad_pairs={totals['bad_overlap']} "
        "rank_deficient=0"
    )


if __name__ == "__main__":
    main()
