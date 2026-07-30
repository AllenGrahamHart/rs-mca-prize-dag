#!/usr/bin/env python3
"""Verify the profile-(2,10), cofactor-514 parity and trace cap."""

from __future__ import annotations

from fractions import Fraction
from math import factorial
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile210_m514_parity_trace_cap"
TARGET = "e1_official_low_square_mass_pair_budget"
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
COFACTOR = 514


def arctangent_sum(value: Fraction, last_index: int) -> Fraction:
    return sum(
        (
            (-1) ** index
            * value ** (2 * index + 1)
            / (2 * index + 1)
            for index in range(last_index + 1)
        ),
        Fraction(),
    )


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


def main() -> None:
    atan_fifth_lower = arctangent_sum(Fraction(1, 5), 5)
    atan_fifth_upper = arctangent_sum(Fraction(1, 5), 6)
    atan_239_lower = arctangent_sum(Fraction(1, 239), 1)
    atan_239_upper = arctangent_sum(Fraction(1, 239), 2)
    pi_lower = 16 * atan_fifth_lower - 4 * atan_239_upper
    pi_upper = 16 * atan_fifth_upper - 4 * atan_239_lower
    if not Fraction(333, 106) < pi_lower < pi_upper < Fraction(355, 113):
        raise RuntimeError("Machin pi interval failed")

    square_sum = sum(index**2 for index in range(1, 14))
    fourth_sum = sum(index**4 for index in range(1, 14))
    trace_upper = 2 * (
        Fraction(13)
        - Fraction(333, 106) ** 2 * square_sum / (2 * 128**2)
        + Fraction(355, 113) ** 4 * fourth_sum / (24 * 128**4)
    )
    trace_margin = Fraction(2551, 100) - trace_upper
    if trace_margin != Fraction(
        7795466688479683619, 12294344879326520934400
    ) or trace_margin <= 0:
        raise RuntimeError("distinct-trace cap failed")

    radius = Fraction(2551, 100)
    deficit = Fraction(683, 500)
    coefficient = deficit / (128 * 13)
    parameter = radius / (36 + radius)
    endpoint_threshold = radius / 18 - coefficient * radius**2
    endpoint_margin = endpoint_threshold - atanh_upper(parameter, 2)
    if endpoint_margin != Fraction(
        1589177092552089193351, 25273817512265112960000000
    ) or endpoint_margin <= 0:
        raise RuntimeError("trace logarithm endpoint failed")
    if not Fraction(1, 36 * (18 + radius)) < coefficient < Fraction(1, 648):
        raise RuntimeError("trace logarithm derivative interval failed")

    exponential_lower = sum(
        (deficit**degree / factorial(degree) for degree in range(7)),
        Fraction(),
    )
    if not exponential_lower > Fraction(18**64, COFACTOR * P_MIN):
        raise RuntimeError("energy-thirteen field-floor separation failed")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    suppliers = (
        "e1_profile210_m514_middle_shape_log_router",
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
        "E1_PROFILE210_M514_PARITY_TRACE_CAP_PASS "
        f"trace_margin={trace_margin} endpoint_margin={endpoint_margin} "
        "remaining_profiles=15"
    )


if __name__ == "__main__":
    main()
