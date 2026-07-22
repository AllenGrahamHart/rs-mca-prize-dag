#!/usr/bin/env python3
"""Verify the HGE4 ambient-order norm level cap packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_ambient_order_norm_level_cap"
DEPENDENCIES = {
    "f3_hge4_exact_ratio_tower_orbit_compiler",
    "f3_hge4_cyclotomic_norm_quarter_width_exclusion",
}
CONSUMER = "f3_hge4_norm_gate_count"


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def ambient_cap(ambient_exponent: int, level_exponent: int) -> int:
    order = 1 << level_exponent
    c_value = ceil_div(order * level_exponent, 8 * ambient_exponent)
    return min(order // 4 - 1, 2 * c_value - 1)


def sharp_deleted(ambient_exponent: int, level_exponent: int, defect: int) -> bool:
    order = 1 << level_exponent
    level_gap = ambient_exponent - level_exponent
    left = 4 * (25 * ambient_exponent - 36) * defect
    if defect % 2:
        left += 100 * ambient_exponent
    return left <= 25 * level_gap * order


def parity_count(limit: int, parity: int, maximum: int) -> int:
    limit = min(limit, maximum)
    first = 2 if parity == 0 else 1
    if limit < first:
        return 0
    return (limit - first) // 2 + 1


def sharp_removed_count(ambient_exponent: int, level_exponent: int) -> int:
    order = 1 << level_exponent
    level_gap = ambient_exponent - level_exponent
    denominator = 4 * (25 * ambient_exponent - 36)
    maximum = order // 4 - 4
    even_limit = 25 * level_gap * order // denominator
    odd_numerator = 25 * level_gap * order - 100 * ambient_exponent
    odd_limit = odd_numerator // denominator if odd_numerator >= 0 else -1
    return (
        parity_count(even_limit, 0, maximum)
        + parity_count(odd_limit, 1, maximum)
    )


def first_sharp_live_defect(ambient_exponent: int, level_exponent: int) -> int:
    order = 1 << level_exponent
    level_gap = ambient_exponent - level_exponent
    denominator = 4 * (25 * ambient_exponent - 36)
    even_limit = 25 * level_gap * order // denominator
    odd_numerator = 25 * level_gap * order - 100 * ambient_exponent
    odd_limit = odd_numerator // denominator if odd_numerator >= 0 else -1

    next_even = even_limit + 1
    if next_even % 2:
        next_even += 1
    next_odd = odd_limit + 1
    if next_odd % 2 == 0:
        next_odd += 1
    return min(next_even, next_odd)


def width_ledger() -> tuple[int, dict[str, int]]:
    removed_at_top_ambient = 0
    sharp_removed_at_top_ambient = 0
    first_live: dict[int, int] = {}
    for ambient_exponent in range(13, 42):
        for level_exponent in range(4, ambient_exponent + 1):
            order = 1 << level_exponent
            cap = ambient_cap(ambient_exponent, level_exponent)
            old_count = max(0, order // 4 - 4)
            new_count = max(0, cap - 3)
            assert new_count <= old_count
            if new_count and ambient_exponent not in first_live:
                first_live[ambient_exponent] = level_exponent

            # Every width above the cap triggers the integer exponent
            # contradiction 8*s*floor(h/2) >= m*a.
            if order <= 4096:
                for width in range(max(4, cap + 1), order // 4):
                    assert (
                        8 * ambient_exponent * (width // 2)
                        >= order * level_exponent
                    )
            if ambient_exponent == 41:
                removed_at_top_ambient += old_count - new_count
                sharp_removed_at_top_ambient += sharp_removed_count(
                    ambient_exponent, level_exponent
                )

        top_order = 1 << ambient_exponent
        assert ambient_cap(ambient_exponent, ambient_exponent) == top_order // 4 - 1

    expected_first_live = {
        13: 6,
        20: 6,
        30: 7,
        41: 7,
    }
    for exponent, level in expected_first_live.items():
        assert first_live[exponent] == level

    stats = {
        "top_ambient_removed": removed_at_top_ambient,
        "top_ambient_sharp_removed": sharp_removed_at_top_ambient,
        "top_proper_cap": ambient_cap(41, 40),
        "top_proper_first_live_defect": (1 << 38) - ambient_cap(41, 40),
        "top_proper_sharp_first_live_defect": first_sharp_live_defect(41, 40),
        "quarter_vandermonde_cap_at_m_2_40": 1_373_333_614,
    }
    assert stats == {
        "top_ambient_removed": 26_817_356_728,
        "top_ambient_sharp_removed": 27_793_519_353,
        "top_proper_cap": 268_173_567_751,
        "top_proper_first_live_defect": 6_704_339_193,
        "top_proper_sharp_first_live_defect": 6_948_379_851,
        "quarter_vandermonde_cap_at_m_2_40": 1_373_333_614,
    }
    return sum(first_live.values()), stats


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "n^(2 floor(h/2)) < (4h)^(m/4)",
        "C(m,n)=ceil(ma/(8s))",
        "268173567751",
        "6704339193",
        "4(25s-36)d+100s",
        "6948379851",
        "not an estimate",
    ):
        assert marker in text


def main() -> None:
    first_live_checksum, stats = width_ledger()
    packet_check()
    print(
        "F3_HGE4_AMBIENT_ORDER_NORM_LEVEL_CAP_PASS "
        f"first_live_checksum={first_live_checksum} "
        f"removed={stats['top_ambient_sharp_removed']} "
        f"top_proper_cap={stats['top_proper_cap']}"
    )


if __name__ == "__main__":
    main()
