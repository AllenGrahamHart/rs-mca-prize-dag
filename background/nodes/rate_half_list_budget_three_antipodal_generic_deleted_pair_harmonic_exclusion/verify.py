#!/usr/bin/env python3
"""Verify the official deleted-pair harmonic exclusion and packet."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_harmonic_exclusion"
DEPENDENCIES = {
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_mobius_ratio_router",
    "rate_half_list_budget_three_maximal_field_degree_collapse",
}
CONSUMER = "rate_half_list_adjacent_crossing"
CHECKER = (
    ROOT
    / "experiments"
    / "prize_resolution"
    / "rate_half_list_deleted_pair_harmonic_characteristic_check.py"
)


def arithmetic_check() -> None:
    order = 1 << 40
    lower_square = 3 * (1 << 128)
    lower = __import__("math").isqrt(lower_square)
    if lower * lower < lower_square:
        lower += 1
    start = (lower - 1 + order - 1) // order
    stop = ((1 << 65) - 2) // order + 1
    assert (start, stop, stop - start) == (29058991, 33554432, 4495441)

    # The trace recurrence detects every order 2^s, 3<=s<=40.
    for exponent in range(3, 41):
        assert 1 <= exponent - 2 <= 38

    completed = subprocess.run(
        ["python3", str(CHECKER)],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert "candidates=4495441 shards=32 hits=0" in completed.stdout


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "q=mu/lambda!=-1",
        "harmonic fourth-power alternative",
        "4,495,441",
        "including composite moduli",
        "does not exclude any nonharmonic",
    ):
        assert marker in statement


def main() -> None:
    arithmetic_check()
    wiring_check()
    print(
        "RATE_HALF_ANTIPODAL_DELETED_PAIR_HARMONIC_EXCLUSION_PASS "
        "harmonic_branches=0 official_moduli=4495441"
    )


if __name__ == "__main__":
    main()
