#!/usr/bin/env python3
"""Verify the terminal shortening-weighted kernel capacity cut."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "346275c29a091b24c528cbdf0f880e9585261f636c92ae041ceda9aefb5a9281"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def vector_digest(values: list[Fraction]) -> str:
    payload = json.dumps(
        [[value.numerator, value.denominator] for value in values],
        separators=(",", ":"),
    ).encode()
    return hashlib.sha256(payload).hexdigest()


def gap(kprime: int, p: dict[str, object]) -> Fraction:
    n_offset = int(p["n_offset"])
    m_offset = int(p["m_offset"])
    s_value = kprime - 10
    caps = [0, *[int(value) for value in p["complete_record_caps"]]]
    f1 = {
        d: Fraction(*p["t1_F_fractions"][str(d)])
        for d in range(4, 10)
    }
    capacity = Fraction(0)
    for d in range(1, 10):
        weighted = (
            Fraction(caps[d] * comb(s_value, d + 1))
            if d <= 3
            else f1[d] * comb(s_value - 1, d + 1)
        )
        capacity += Fraction(comb(n_offset + kprime, 10 - d), d + 2) * weighted
    demand = Fraction(
        int(p["residual_record_floor"])
        * int(p["lane_density_numerator"])
        * comb(m_offset + kprime, 11),
        int(p["lane_density_denominator"]),
    )
    return demand - capacity


def newton_coefficients(p: dict[str, object]) -> list[Fraction]:
    start = int(p["replay_minimum"])
    values = [gap(start + offset, p) for offset in range(12)]
    coefficients = []
    while values:
        coefficients.append(values[0])
        values = [values[index + 1] - values[index] for index in range(len(values) - 1)]
    return coefficients


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-shortening-weighted-capacity-cut-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_corank3_projective_capacity_cut",
        "rate_half_mca_rank11_kernel_shortening_weighted_extension_cap",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["n_offset"], p["m_offset"], p["residual_record_floor"]) == (1048576, 67472, 274980728111260126), "base parameters")
    require((p["lane_density_numerator"], p["lane_density_denominator"]) == (495405467, 1000000000), "lane density")
    require((p["previous_closed_maximum"], p["replay_minimum"], p["closed_dimension_maximum"]) == (796598, 796599, 1048576), "interval")
    require(p["polynomial_degree"] == 11, "degree")
    coefficients = newton_coefficients(p)
    require(len(coefficients) == p["positive_newton_coefficients"] == 12, "Newton count")
    require(all(value > 0 for value in coefficients), "Newton signs")
    require(vector_digest(coefficients) == p["newton_vector_sha256"], "Newton digest")
    start_gap = gap(int(p["replay_minimum"]), p)
    endpoint_gap = gap(int(p["closed_dimension_maximum"]), p)
    require([start_gap.numerator, start_gap.denominator] == p["start_gap"], "start gap")
    require([endpoint_gap.numerator, endpoint_gap.denominator] == p["endpoint_gap"], "endpoint gap")
    require("closes only the fixed-kernel branch" in str(data.get("nonclaim")), "nonclaim")
    return {"newton": len(coefficients), "start": int(p["replay_minimum"]), "end": int(p["closed_dimension_maximum"])}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("lane_density_numerator", 495405466),
        lambda item: item["parameters"].__setitem__("replay_minimum", 796600),
        lambda item: item["parameters"]["complete_record_caps"].__setitem__(0, 8147919),
        lambda item: item["parameters"]["t1_F_fractions"]["9"].__setitem__(0, 1),
        lambda item: item["parameters"].__setitem__("newton_vector_sha256", "0" * 64),
        lambda item: item["parameters"]["endpoint_gap"].__setitem__(0, 1),
        lambda item: item.__setitem__("nonclaim", "prize closure"),
    )
    caught = 0
    for mutation in mutations:
        changed = copy.deepcopy(data)
        mutation(changed)
        try:
            validate(changed)
        except (Reject, KeyError, TypeError, ValueError, ZeroDivisionError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_SHORTENING_WEIGHTED_CAPACITY_CUT_PASS "
        f"interval={result['start']}..{result['end']} newton={result['newton']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
