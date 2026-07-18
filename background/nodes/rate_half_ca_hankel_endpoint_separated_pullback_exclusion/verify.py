#!/usr/bin/env python3
"""Tiny integer checks for the strict-endpoint separated-pullback exclusion."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def lower_bound(m: int, e: int) -> tuple[int, int, int, int]:
    n = 16 * m
    slopes = 4 * m + 1
    r = 4 * e - 1
    q, s = divmod(slopes, e)
    leftover = n - q * r
    assert q in (4, 5)
    assert 0 < leftover <= r
    return q, s, leftover, leftover * (e - s)


def check_power(power: int) -> int:
    m = 1 << power
    assert m % 20 == 12
    minimum_e = (3 * m + 4) // 4
    checked = 0
    for e in range(minimum_e, m + 1):
        q, s, leftover, defect = lower_bound(m, e)
        assert defect > m
        if q == 4:
            b = m - e
            assert s == 4 * b + 1
            assert leftover == 16 * b + 4
            assert e - s == m - 5 * b - 1
        else:
            b = m - e
            assert s == 5 * b - m + 1
            assert leftover == 20 * b - 4 * m + 5
            assert leftover >= 17
            assert e - s >= m // 2 + 5
        checked += 1
    return checked


def check_official() -> int:
    m = 1 << 37
    assert m % 5 == 2
    minimum_e = 3 * (1 << 35) + 1

    q, _, leftover, defect = lower_bound(m, m)
    assert q == 4 and leftover == 4 and defect == 4 * (m - 1)

    boundary_e = (4 * m - 3) // 5
    q, _, leftover, defect = lower_bound(m, boundary_e)
    assert q == 5 and leftover == 17 and defect > m

    q, _, _, defect = lower_bound(m, minimum_e)
    assert q == 5 and defect > m
    return m


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    node_id = "rate_half_ca_hankel_endpoint_separated_pullback_exclusion"
    assert nodes[node_id]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "rate_half_ca_hankel_endpoint_component_defect_localization",
        node_id,
        "req",
    ) in edges
    assert (node_id, "rate_half_band_closure", "ev") in edges


def main() -> None:
    checked = sum(check_power(power) for power in range(5, 18, 4))
    official = check_official()
    check_dag()
    print(
        "RATE_HALF_CA_HANKEL_ENDPOINT_SEPARATED_PULLBACK_PASS "
        f"degrees={checked} official_m={official}"
    )


if __name__ == "__main__":
    main()
