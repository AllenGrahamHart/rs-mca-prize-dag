#!/usr/bin/env python3
"""Verify the XR global quotient-core collision router."""

from __future__ import annotations

from math import comb, gcd
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_quotient_global_core_collision_router"
DEPENDENCIES = {
    "xr_quotient_max_agreement_first_match_owner",
    "xr_target_budget_audit",
}
CONSUMERS = {
    "xr_tangent_support_mismatch_bridge",
    "xr_highcore_collision_count",
}
PRIZE_BSTAR = 317494674775468773183020924238786383963
ROWS = (
    ("RowC-1/4", 1 << 10, 1 << 8, 261, 1 << 122),
    ("RowC-1/8", 1 << 10, 1 << 7, 133, 1 << 122),
    ("RowC-1/16", 1 << 10, 1 << 6, 67, 1 << 122),
    ("prize-1/4", 1 << 41, 1 << 39, 558345748481, PRIZE_BSTAR),
    ("prize-1/8", 1 << 41, 1 << 38, 283467841537, PRIZE_BSTAR),
    ("prize-1/16", 1 << 41, 1 << 37, 141733920769, PRIZE_BSTAR),
)


def powers_of_two(limit: int) -> tuple[int, ...]:
    values = []
    value = 1
    while value <= limit:
        values.append(value)
        value *= 2
    return tuple(values)


def quotient_envelope(n: int, k: int, agreement: int) -> int:
    reserve = agreement - k
    total = 0
    quotient_length = 2
    while quotient_length <= n and quotient_length * reserve <= n:
        selected = (n - agreement) * quotient_length // n
        if 1 <= selected < quotient_length:
            total += comb(quotient_length, selected)
        quotient_length *= 2
    return total


def arithmetic_check() -> tuple[int, int]:
    rows = 0
    scales = 0
    for _, n, k, agreement, budget in ROWS:
        reserve = agreement - k
        active = tuple(
            scale
            for scale in powers_of_two(gcd(n, k))
            if scale > reserve
        )
        core_sum = 0
        for scale in active:
            quotient_length = n // scale
            core_size = k // scale
            assert scale * core_size == k
            assert 2 * core_size + 1 <= quotient_length
            assert (n - agreement) // scale == quotient_length - core_size - 1
            assert comb(quotient_length, core_size) <= comb(
                quotient_length, core_size + 1
            )
            core_sum += comb(quotient_length, core_size)
            scales += 1

        envelope = quotient_envelope(n, k, agreement)
        assert core_sum <= envelope
        assert core_sum + (n - agreement + 1) + 16 * n**3 <= budget
        rows += 1
    return rows, scales


def global_grouping_check() -> None:
    records = (
        (2, "K0", 3, "z0"),
        (2, "K1", 3, "z1"),
        (2, "K0", 4, "z2"),
        (4, "K2", 5, "z3"),
    )
    groups: dict[tuple[int, str], list[str]] = {}
    for scale, core, _agreement, slope in records:
        groups.setdefault((scale, core), []).append(slope)
    singleton = {slopes[0] for slopes in groups.values() if len(slopes) == 1}
    collision = {
        slope for slopes in groups.values() if len(slopes) >= 2 for slope in slopes
    }
    assert singleton == {"z1", "z3"}
    assert collision == {"z0", "z2"}
    assert singleton.isdisjoint(collision)
    assert singleton | collision == {record[3] for record in records}


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "|K_z|=k",
        "|Z_single|",
        "<=B_quot_ub(A_0)",
        "xr_highcore_collision_count",
        "doesnotprovetheP-Abound",
    ):
        assert marker in statement


def main() -> None:
    rows, scales = arithmetic_check()
    global_grouping_check()
    packet_check()
    print(
        "XR_QUOTIENT_GLOBAL_CORE_COLLISION_ROUTER_PASS "
        f"rows={rows} active_scales={scales} groups=3"
    )


if __name__ == "__main__":
    main()
