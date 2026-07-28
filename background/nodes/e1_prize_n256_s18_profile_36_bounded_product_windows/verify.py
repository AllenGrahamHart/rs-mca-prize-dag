#!/usr/bin/env python3
"""Verify the bounded sharp product windows for profile (3,6)."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_profile_36_bounded_product_windows"
PARENT = "e1_prize_n256_s18_profile_36_cofactor_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
COUNT = 64
MEAN = Fraction(18)
CAP = Fraction(144)
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
DENOMINATOR = 2**192
WINDOWS = {
    2: (286, 350, 2651), 4: (268, 314, 2072), 8: (256, 278, 1112),
    16: (218, 244, 516), 32: (172, 208, 757), 64: (132, 174, 946),
    256: (62, 104, 1111), 512: (36, 68, 929), 514: (36, 68, 929),
}
EXPECTED_CLOSEST = {
    2: (286, 1, 62), 4: (268, 1, 62), 8: (256, 1, 62),
    16: (218, 0, 63), 32: (172, 0, 63), 64: (132, 0, 63),
    256: (62, 0, 63), 512: (36, 0, 63), 514: (36, 0, 63),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sqrt_interval(value: Fraction) -> tuple[Fraction, Fraction]:
    scaled = value.numerator * DENOMINATOR**2 // value.denominator
    floor = isqrt(scaled)
    lower = Fraction(floor, DENOMINATOR)
    if floor * floor * value.denominator == value.numerator * DENOMINATOR**2:
        return lower, lower
    return lower, Fraction(floor + 1, DENOMINATOR)


def products(variance: int) -> list[tuple[int, int, Fraction, Fraction]]:
    rows = []
    for capped in range(8):
        residual_count = COUNT - capped
        residual_mean = (COUNT * MEAN - capped * CAP) / residual_count
        residual_square = (
            COUNT * variance
            - capped * (CAP - MEAN) ** 2
            - residual_count * (residual_mean - MEAN) ** 2
        )
        if residual_square < 0:
            continue
        residual_variance = residual_square / residual_count
        if residual_variance == 0:
            value = CAP**capped * residual_mean**residual_count
            rows.append((capped, residual_count, value, value))
            continue
        for lower_count in range(1, residual_count):
            upper_count = residual_count - lower_count
            low_square = residual_variance * upper_count / lower_count
            high_square = residual_variance * lower_count / upper_count
            if low_square >= residual_mean**2:
                continue
            if high_square > (CAP - residual_mean) ** 2:
                continue
            low_sqrt = sqrt_interval(low_square)
            high_sqrt = sqrt_interval(high_square)
            low_value = (residual_mean - low_sqrt[1], residual_mean - low_sqrt[0])
            high_value = (residual_mean + high_sqrt[0], residual_mean + high_sqrt[1])
            rows.append((
                capped, lower_count,
                CAP**capped * low_value[0]**lower_count * high_value[0]**upper_count,
                CAP**capped * low_value[1]**lower_count * high_value[1]**upper_count,
            ))
    assert rows
    return rows


def main() -> None:
    node_dir = ROOT / "background/nodes" / NODE
    pin = json.loads((node_dir / "source_pin.json").read_text())
    for key in ("parent_statement", "parent_proof", "certificate"):
        assert sha256(ROOT / pin[f"{key}_file"]) == pin[f"{key}_sha256"]

    total = 0
    for cofactor, (onset, old_upper, expected_count) in WINDOWS.items():
        target = cofactor * P_MIN
        closest = None
        comparisons = 0
        for variance in range(onset, old_upper + 1, 2):
            for capped, lower_count, _, upper in products(variance):
                assert upper < target
                row = (Fraction(target, 1) / upper, variance, capped, lower_count)
                if closest is None or row < closest:
                    closest = row
                comparisons += 1
        assert comparisons == expected_count
        assert closest is not None and closest[1:] == EXPECTED_CLOSEST[cofactor]
        assert any(lower > target for _, _, lower, _ in products(onset - 2))
        total += comparisons
    assert total == 11023

    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("4<=V<=284", "4<=V<=34", "nine residual"):
        assert text in statement
    for text in ("11023", "2^192", "(k,j)=(1,62)"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target_node, "ev") in edges for target_node in TARGETS)

    print(
        "E1_PRIZE_N256_S18_PROFILE_36_BOUNDED_PRODUCT_WINDOWS_PASS "
        f"cofactors={len(WINDOWS)} comparisons={total}"
    )


if __name__ == "__main__":
    main()
