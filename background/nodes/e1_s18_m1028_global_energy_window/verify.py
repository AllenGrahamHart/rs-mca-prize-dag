#!/usr/bin/env python3
"""Verify the square-mass-18 cofactor-1028 global energy window."""

from __future__ import annotations

from fractions import Fraction
import json
from math import isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_s18_m1028_global_energy_window"
TARGET = "e1_official_low_square_mass_pair_budget"
COUNT = 64
MEAN = 18
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
DENOMINATOR = 2**192
EXPECTED_L32 = 13354478338703157414450712387359637585922


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
    if not 0 < low_value[0] <= low_value[1]:
        raise RuntimeError("infeasible lower chamber")
    return (
        low_value[0] ** lower_count * high_value[0] ** upper_count,
        low_value[1] ** lower_count * high_value[1] ** upper_count,
    )


def lucas(index: int) -> int:
    previous, current = 2, 18
    if index == 0:
        return previous
    for _ in range(2, index + 1):
        previous, current = current, 18 * current - previous
    return current


def main() -> None:
    if (18**64) % 2**64 or (18**64) % 2**65 == 0:
        raise RuntimeError("energy-zero valuation drift")
    value = lucas(32)
    if value != EXPECTED_L32 or value * value % 1028 != 452:
        raise RuntimeError("energy-one Lucas exclusion drift")

    target = 1028 * P_MIN
    rows = []
    for lower_count in range(1, COUNT):
        if Fraction(14 * (COUNT - lower_count), lower_count) >= MEAN**2:
            continue
        _, upper = product_interval(14, lower_count)
        if not upper < target:
            raise RuntimeError(f"energy-seven chamber survives: j={lower_count}")
        rows.append((Fraction(target, 1) / upper, lower_count))
    if len(rows) != 61 or min(rows)[1] != 63:
        raise RuntimeError("energy-seven chamber census drift")

    boundary_lower, _ = product_interval(12, 63)
    if not boundary_lower > target:
        raise RuntimeError("energy-six boundary guard drift")

    statement = (ROOT / "background/nodes" / NODE / "statement.md").read_text()
    proof = (ROOT / "background/nodes" / NODE / "proof.md").read_text()
    for text in ("{2,3,4,5,6}", "61 feasible", "energy-six"):
        if text not in statement:
            raise RuntimeError(f"statement pin missing: {text}")
    for text in ("L_32^2 mod 1028=452", "2^192", "(V,j)=(12,63)"):
        if text not in proof:
            raise RuntimeError(f"proof pin missing: {text}")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    suppliers = (
        "collision_norm_criterion",
        "e1_prize_field_floor_even_norm_exclusion",
    )
    if nodes[NODE]["status"] != "PROVED" or nodes[TARGET]["status"] != "TARGET":
        raise RuntimeError("DAG status drift")
    for supplier in suppliers:
        if nodes[supplier]["status"] != "PROVED":
            raise RuntimeError(f"supplier status drift: {supplier}")
        if (supplier, NODE, "req") not in edges:
            raise RuntimeError(f"missing supplier edge: {supplier}")
    if (NODE, TARGET, "ev") not in edges:
        raise RuntimeError("missing evidence edge")

    print(
        "E1_S18_M1028_GLOBAL_ENERGY_WINDOW_PASS "
        f"lucas_residue=452 comparisons={len(rows)} closest_j={min(rows)[1]}"
    )


if __name__ == "__main__":
    main()
