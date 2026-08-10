#!/usr/bin/env python3
"""Check the compact certificate for the preregistered FPC5 route probe."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RESULT = ROOT / "experiments/prize_resolution/fpc5_hankel_guard_probe_result.json"
EXPECTED_CONFIGS = {
    "t4e2": 64,
    "t4e3": 64,
    "t4e4": 32,
    "t5e2": 48,
    "t5e3": 48,
    "t5e4": 24,
}
EXPECTED_CHARTS = {
    "t4e2": 64,
    "t4e3": 128,
    "t4e4": 96,
    "t5e2": 48,
    "t5e3": 96,
    "t5e4": 72,
}


def classify(payload: dict) -> tuple[bool, bool]:
    cells = payload["cells"]
    ratios = {}
    for cell_id, cell in cells.items():
        actual = cell["max_primitive"]
        random = cell["max_random_primitive"]
        ratios[cell_id] = float("inf") if random == 0 and actual else (
            actual / random if random else 0.0
        )

    excess_cells = sum(value > 16.0 for value in ratios.values())
    monotone_growth = False
    for t in (4, 5):
        lane = [ratios[f"t{t}e{ell}"] for ell in (2, 3, 4)]
        if lane[0] and all(a <= b for a, b in zip(lane, lane[1:])):
            monotone_growth |= lane[-1] > 4.0 * lane[0]
    rational_excess = excess_cells >= 2 or monotone_growth

    suppressed = sum(
        cell["median_guard_fraction"] < 0.25
        for cell in cells.values()
    )
    return rational_excess, suppressed >= 2


def check(payload: dict) -> None:
    assert payload["schema"] == "fpc5-hankel-guard-probe-summary-v1"
    assert payload["preregistration_commit"] == "468f04f1d"
    assert payload["full_payload_bytes"] == 78469
    assert payload["full_payload_sha256"] == (
        "bc9ec288a00a35790dd157dc44fb2c078751e3cb1b85d7867107b34089aba05d"
    )
    assert set(payload["cells"]) == set(EXPECTED_CONFIGS)
    assert payload["completed_configurations"] == sum(EXPECTED_CONFIGS.values())
    assert payload["completed_fixed_charts"] == sum(EXPECTED_CHARTS.values())
    for cell_id, expected in EXPECTED_CONFIGS.items():
        cell = payload["cells"][cell_id]
        assert cell["completed"] == expected
        assert cell["fixed_charts"] == EXPECTED_CHARTS[cell_id]
        assert cell["max_guarded"] <= cell["max_primitive"]
        assert cell["mean_guarded"] <= cell["mean_primitive"]
        assert 0.0 <= cell["median_guard_fraction"] <= 1.0

    rational_excess, guard_suppression = classify(payload)
    decision = payload["decision"]
    assert decision["rational_excess_alarm"] is rational_excess
    assert decision["guard_suppression_signal"] is guard_suppression
    expected_class = (
        "ALARM" if rational_excess else
        "GUARD_SUPPRESSION" if guard_suppression else
        "NO_SEPARATION"
    )
    assert decision["classification"] == expected_class


def tamper_selftest(payload: dict) -> int:
    rejected = 0
    mutations = []

    bad = copy.deepcopy(payload)
    bad["completed_configurations"] += 1
    mutations.append(bad)

    bad = copy.deepcopy(payload)
    bad["cells"]["t4e2"]["max_primitive"] = 400
    bad["cells"]["t5e2"]["max_primitive"] = 400
    mutations.append(bad)

    bad = copy.deepcopy(payload)
    bad["cells"]["t4e2"]["median_guard_fraction"] = 0.0
    bad["cells"]["t5e2"]["median_guard_fraction"] = 0.0
    mutations.append(bad)

    for mutation in mutations:
        try:
            check(mutation)
        except AssertionError:
            rejected += 1
    assert rejected == len(mutations)
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(RESULT.read_text())
    check(payload)
    rejected = tamper_selftest(payload) if args.tamper_selftest else 0
    print(
        "FPC5_HANKEL_GUARD_CERT_PASS "
        f"configs={payload['completed_configurations']} "
        f"charts={payload['completed_fixed_charts']} "
        f"tamper_rejected={rejected}"
    )


if __name__ == "__main__":
    main()
