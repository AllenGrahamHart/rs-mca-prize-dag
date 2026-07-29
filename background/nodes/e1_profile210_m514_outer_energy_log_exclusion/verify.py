#!/usr/bin/env python3
"""Verify the profile-(2,10), cofactor-514 outer-energy exclusion."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile210_m514_outer_energy_log_exclusion"
TARGET = "e1_official_low_square_mass_pair_budget"
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
P_MAX = (B_PRIZE + 1) * 2**128 - 1
COFACTOR = 514


def atanh_upper(parameter: Fraction, terms: int) -> Fraction:
    head = 2 * sum(
        (parameter ** (2 * index + 1) / (2 * index + 1)
         for index in range(terms)),
        Fraction(),
    )
    first_tail_index = terms
    denominator = 2 * first_tail_index + 1
    tail = (
        2
        * parameter ** denominator
        / denominator
        / (1 - parameter**2)
    )
    return head + tail


def main() -> None:
    low_series = atanh_upper(Fraction(2, 7), 2)
    low_threshold = Fraction(4, 9) + Fraction(32, 223)
    if low_series != Fraction(45364, 77175):
        raise RuntimeError("low atanh upper drift")
    if low_threshold != Fraction(1180, 2007):
        raise RuntimeError("low endpoint threshold drift")
    low_margin = low_threshold - low_series
    if low_margin != Fraction(776, 5736675) or low_margin <= 0:
        raise RuntimeError("low endpoint separation failed")

    low_exponential_upper = Fraction(223, 159) ** 4
    low_required_ratio = Fraction(18**64, COFACTOR * P_MAX)
    if not low_exponential_upper < low_required_ratio:
        raise RuntimeError("low-energy field-ceiling separation failed")

    high_series = atanh_upper(Fraction(7, 16), 2)
    high_threshold = Fraction(14, 9) - Fraction(784, 1275)
    if high_series != Fraction(994931, 1059840):
        raise RuntimeError("high atanh upper drift")
    if high_threshold != Fraction(3598, 3825):
        raise RuntimeError("high endpoint threshold drift")
    high_margin = high_threshold - high_series
    if high_margin != Fraction(56987, 30028800) or high_margin <= 0:
        raise RuntimeError("high endpoint separation failed")

    exponent = Fraction(1792, 1275)
    exponential_lower = sum(
        (exponent**degree / __import__("math").factorial(degree)
         for degree in range(5)),
        Fraction(),
    )
    high_required_ratio = Fraction(18**64, COFACTOR * P_MIN)
    if not exponential_lower > high_required_ratio:
        raise RuntimeError("high-energy field-floor separation failed")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    suppliers = (
        "e1_profile210_split_prime_ideal_router",
        "e1_prize_n256_s18_variance_cofactor_windows",
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
        "E1_PROFILE210_M514_OUTER_ENERGY_LOG_EXCLUSION_PASS "
        f"low_margin={low_margin} high_margin={high_margin} "
        "remaining_energies=5-13"
    )


if __name__ == "__main__":
    main()
