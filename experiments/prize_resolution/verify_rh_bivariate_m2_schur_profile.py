#!/usr/bin/env python3
"""Verify the bounded m=2 Schur-profile Modal aggregate."""

import json
from collections import Counter, defaultdict
from pathlib import Path


RESULT = Path(__file__).with_name("rh_bivariate_m2_schur_profile_result.json")

EXPECTED_TOTALS = {
    "all_blocks_full_saturated": 105574,
    "any_pair_full_deficient": 19761,
    "any_pair_full_saturated": 105574,
    "any_single_full_deficient": 19761,
    "any_single_full_saturated": 105574,
    "attempted": 88867,
    "bad_pairs": 125335,
    "deficient_w": 19761,
    "full_matrix_rank": 125335,
    "j0_full_deficient": 15435,
    "j0_full_saturated": 82247,
    "j1_full_deficient": 19761,
    "j1_full_saturated": 105574,
    "j2_full_deficient": 19761,
    "j2_full_saturated": 105574,
    "regular_incidence": 58644,
    "saturated_w": 105574,
}

EXPECTED_HISTOGRAMS = {
    "deficient_block_ranks": {
        "0,2,2": 1803,
        "0,3,3": 2523,
        "2,2,2": 6455,
        "3,3,3": 8980,
    },
    "deficient_full_schur_block_ranks": {
        "0,3,3": 1803,
        "0,4,4": 2523,
        "3,3,3": 6455,
        "4,4,4": 8980,
    },
    "deficient_pair_full_sets": {"01,02,12": 19761},
    "saturated_block_ranks": {
        "0,2,2": 10993,
        "0,3,3": 12334,
        "2,2,2": 38366,
        "3,3,3": 43881,
    },
    "saturated_full_schur_block_ranks": {
        "0,2,2": 10993,
        "0,3,3": 12334,
        "2,2,2": 38366,
        "3,3,3": 43881,
    },
    "saturated_pair_full_sets": {"01,02,12": 105574},
}


def main() -> None:
    payload = json.loads(RESULT.read_text())
    assert payload["schema"] == "rate-half-bivariate-m2-schur-profile-v1"
    assert payload["complete"] is True
    assert payload["error"] is None
    assert payload["exceptions"] == []
    assert payload["completed_tasks"] == 16
    assert payload["parameters"] == {
        "field": 97,
        "m": 2,
        "pivot_rule": "first 9 sorted support points",
        "seconds_per_task": 30.0,
        "tasks": 16,
        "trial_cap_per_task": 100000,
    }

    rows = payload["rows"]
    assert len(rows) == 16
    assert [row["seed"] for row in rows] == list(range(16))

    totals = Counter()
    histograms: dict[str, Counter] = defaultdict(Counter)
    for row in rows:
        assert row["exceptions"] == []
        counters = row["counters"]
        totals.update(counters)
        for name, histogram in row["histograms"].items():
            histograms[name].update(histogram)

        assert counters["bad_pairs"] == (
            counters["saturated_w"] + counters["deficient_w"]
        )
        assert counters["full_matrix_rank"] == counters["bad_pairs"]
        for branch in ("saturated", "deficient"):
            branch_total = counters[f"{branch}_w"]
            assert counters[f"j1_full_{branch}"] == branch_total
            assert counters[f"j2_full_{branch}"] == branch_total
            assert counters[f"any_single_full_{branch}"] == branch_total
            assert counters[f"any_pair_full_{branch}"] == branch_total
        assert counters["all_blocks_full_saturated"] == counters["saturated_w"]

    assert dict(totals) == EXPECTED_TOTALS
    assert payload["totals"] == EXPECTED_TOTALS
    computed_histograms = {
        name: dict(histogram) for name, histogram in histograms.items()
    }
    assert computed_histograms == EXPECTED_HISTOGRAMS
    assert payload["histograms"] == EXPECTED_HISTOGRAMS

    print(
        "RH_BIVARIATE_M2_SCHUR_PROFILE_PASS "
        "tasks=16 bad_pairs=125335 rank_deficient=0 "
        "j1_j2_failures=0"
    )


if __name__ == "__main__":
    main()
