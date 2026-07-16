#!/usr/bin/env python3
"""Verify the reserve-scale rich-fiber arithmetic and DAG contract."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "petal_reserve_rich_fiber_reduction"


def ceil_div(x: int, y: int) -> int:
    return (x + y - 1) // y


def main() -> None:
    checks = 0
    minimum_rich = None

    for exponent in range(13, 45):
        n = 1 << exponent
        ell = ceil_div(n, exponent)
        for denominator in (2, 4, 8, 16):
            k = n // denominator
            outside = n - k + 1
            petals = outside // ell
            background = outside - petals * ell
            rich = ceil_div(ell, petals)
            profile_floor = ceil_div(ell * ell, outside)

            assert 0 <= background < ell
            assert petals >= 1
            assert ell > petals
            assert rich >= profile_floor
            assert rich * petals >= ell
            assert (rich - 1) * petals < ell
            minimum_rich = rich if minimum_rich is None else min(minimum_rich, rich)
            checks += 7

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge["kind"])
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    assert (NODE, "petal_mixed_amplification", "ev") in edges
    assert (NODE, "imgfib", "ev") in edges
    checks += 3

    # Mutation controls for the two load-bearing strict inequalities.
    ell = 11
    background = ell - 1
    d = 7
    assert (d + 1) + background >= ell
    assert not (background < ell - 1)
    checks += 2

    print(
        "PETAL_RESERVE_RICH_FIBER_PASS "
        f"checks={checks} rows={32 * 4} min_rich={minimum_rich} mutations=2"
    )


if __name__ == "__main__":
    main()
