#!/usr/bin/env python3
"""Verify the profile-(2,10), cofactor-514 middle-shape router."""

from __future__ import annotations

from fractions import Fraction
from math import factorial
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile210_m514_middle_shape_log_router"
TARGET = "e1_official_low_square_mass_pair_budget"
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
P_MAX = (B_PRIZE + 1) * 2**128 - 1
COFACTOR = 514
SURVIVORS = {
    (5, 5, 0, 0),
    (6, 6, 0, 0), (6, 2, 1, 0),
    (7, 7, 0, 0), (7, 3, 1, 0),
    (8, 8, 0, 0), (8, 4, 1, 0), (8, 0, 2, 0),
    (9, 9, 0, 0), (9, 5, 1, 0), (9, 1, 2, 0),
    (10, 10, 0, 0), (10, 6, 1, 0),
    (11, 11, 0, 0), (11, 7, 1, 0),
    (12, 12, 0, 0),
    (13, 13, 0, 0),
}
BOUNDARIES = {
    (9, 3): Fraction(253, 100800),
    (10, 6): Fraction(11, 36000),
    (11, 7): Fraction(931, 95040),
    (12, 10): Fraction(607, 229824),
    (13, 11): Fraction(321013, 16286400),
}


def atanh_upper(parameter: Fraction, terms: int) -> Fraction:
    head = 2 * sum(
        (parameter ** (2 * index + 1) / (2 * index + 1)
         for index in range(terms)),
        Fraction(),
    )
    denominator = 2 * terms + 1
    tail = (
        2
        * parameter**denominator
        / denominator
        / (1 - parameter**2)
    )
    return head + tail


def profiles() -> set[tuple[int, int, int, int]]:
    rows = set()
    for energy in range(5, 14):
        for threes in range(energy // 9 + 1):
            for twos in range((energy - 9 * threes) // 4 + 1):
                ones = energy - 9 * threes - 4 * twos
                rows.add((energy, ones, twos, threes))
    return rows


def main() -> None:
    low_upper = atanh_upper(Fraction(1, 5), 1)
    low_threshold = Fraction(1, 3) + Fraction(36 * 13, 6400)
    if low_upper != Fraction(73, 180):
        raise RuntimeError("energy-five atanh bound drift")
    if low_threshold - low_upper != Fraction(13, 14400):
        raise RuntimeError("energy-five endpoint margin drift")
    low_exponential_upper = Fraction(160, 147) ** 16
    if not low_exponential_upper < Fraction(18**64, COFACTOR * P_MAX):
        raise RuntimeError("energy-five ceiling separation failed")

    deficit = Fraction(69, 50)
    for (energy, l1_mass), expected_margin in BOUNDARIES.items():
        coefficient = deficit / (128 * energy)
        radius = 2 * l1_mass
        parameter = Fraction(l1_mass, 18 + l1_mass)
        endpoint_threshold = (
            Fraction(l1_mass, 9) - coefficient * radius**2
        )
        margin = endpoint_threshold - atanh_upper(parameter, 1)
        if margin != expected_margin or margin <= 0:
            raise RuntimeError(f"upper endpoint drift: {(energy, l1_mass)}")
        if not Fraction(1, 36 * (18 + radius)) < coefficient < Fraction(1, 648):
            raise RuntimeError(f"upper derivative interval drift: {(energy, l1_mass)}")

    exponential_lower = sum(
        (deficit**degree / factorial(degree) for degree in range(5)),
        Fraction(),
    )
    if not exponential_lower > Fraction(18**64, COFACTOR * P_MIN):
        raise RuntimeError("high-middle floor separation failed")

    all_profiles = profiles()
    if len(all_profiles) != 32:
        raise RuntimeError("square-partition census drift")
    excluded = {(5, 1, 1, 0)}
    l1_boundaries = {energy: l1_mass for energy, l1_mass in BOUNDARIES}
    for row in all_profiles:
        energy, ones, twos, threes = row
        l1_mass = ones + 2 * twos + 3 * threes
        boundary = l1_boundaries.get(energy)
        if boundary is not None and l1_mass <= boundary:
            excluded.add(row)
    if all_profiles - excluded != SURVIVORS or len(excluded) != 15:
        raise RuntimeError("middle-shape survivor ledger drift")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    suppliers = (
        "e1_profile210_m514_outer_energy_log_exclusion",
        "e1_profile210_split_prime_ideal_router",
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
        "E1_PROFILE210_M514_MIDDLE_SHAPE_LOG_ROUTER_PASS "
        f"profiles={len(all_profiles)} excluded={len(excluded)} "
        f"survivors={len(SURVIVORS)}"
    )


if __name__ == "__main__":
    main()
