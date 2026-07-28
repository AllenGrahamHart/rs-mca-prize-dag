#!/usr/bin/env python3
"""Verify the profile-(3,6) sharp product-window certificate."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_profile_36_sharp_product_window"
PARENT = "e1_prize_n256_s18_profile_36_cofactor_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
COUNT = 64
MEAN = 18
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
DENOMINATOR = 2**192


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sqrt_interval(value: Fraction) -> tuple[Fraction, Fraction]:
    scaled_square = value.numerator * DENOMINATOR**2 // value.denominator
    floor = isqrt(scaled_square)
    lower = Fraction(floor, DENOMINATOR)
    if floor * floor * value.denominator == value.numerator * DENOMINATOR**2:
        return lower, lower
    return lower, Fraction(floor + 1, DENOMINATOR)


def product_interval(variance: int, lower_count: int) -> tuple[Fraction, Fraction]:
    upper_count = COUNT - lower_count
    low_sqrt = sqrt_interval(Fraction(variance * upper_count, lower_count))
    high_sqrt = sqrt_interval(Fraction(variance * lower_count, upper_count))
    low_value = (Fraction(MEAN) - low_sqrt[1], Fraction(MEAN) - low_sqrt[0])
    high_value = (Fraction(MEAN) + high_sqrt[0], Fraction(MEAN) + high_sqrt[1])
    assert 0 < low_value[0] <= low_value[1]
    return (
        low_value[0] ** lower_count * high_value[0] ** upper_count,
        low_value[1] ** lower_count * high_value[1] ** upper_count,
    )


def main() -> None:
    node_dir = ROOT / "background/nodes" / NODE
    pin = json.loads((node_dir / "source_pin.json").read_text())
    for key in ("parent_statement", "parent_proof", "certificate"):
        assert sha256(ROOT / pin[f"{key}_file"]) == pin[f"{key}_sha256"]

    target = 1024 * P_MIN
    comparisons = 0
    closest: tuple[Fraction, int, int] | None = None
    for variance in range(14, 36, 2):
        for lower_count in range(1, COUNT):
            if Fraction(variance * (COUNT - lower_count), lower_count) >= MEAN**2:
                continue
            _, product_upper = product_interval(variance, lower_count)
            assert product_upper < target
            margin = Fraction(target, 1) / product_upper
            if closest is None or margin < closest[0]:
                closest = (margin, variance, lower_count)
            comparisons += 1
    assert comparisons == 649
    assert closest is not None and closest[1:] == (14, 63)

    boundary_lower, _ = product_interval(12, 63)
    assert boundary_lower > target

    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("{1024,1028}", "{4,6,8,10,12}", "V=12"):
        assert text in statement
    for text in ("649", "2^192", "(V,j)=(14,63)"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (PARENT, NODE, "req") in edges
    assert all((NODE, target_node, "ev") in edges for target_node in TARGETS)

    print(
        "E1_PRIZE_N256_S18_PROFILE_36_SHARP_PRODUCT_WINDOW_PASS "
        f"comparisons={comparisons} closest=V{closest[1]}_j{closest[2]}"
    )


if __name__ == "__main__":
    main()
