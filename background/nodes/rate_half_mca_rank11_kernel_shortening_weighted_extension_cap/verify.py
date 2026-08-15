#!/usr/bin/env python3
"""Verify the shortening-weighted kernel record/extension cap."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "7e8c30e32fed0c67ff8d4526f89e8a6314d3548ee1e8af4b032b831832918ce0"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def f_value(r_value: int, w_value: int, d: int, t: int) -> Fraction:
    return Fraction(
        falling(r_value + d + t, d + 1),
        (w_value + d + t) * rising(w_value + 1, d - 1),
    )


def weighted_ratio(r_value: int, w_value: int, s_value: int, d: int, t: int) -> Fraction:
    q = d + 1
    return Fraction(
        (r_value + d + t + 1) * (w_value + d + t) * (s_value - t - q),
        (r_value + t) * (w_value + d + t + 1) * (s_value - t),
    )


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-shortening-weighted-extension-cap-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_multibasis_decoration_compression",
        "rate_half_mca_rank11_kernel_projective_paving_integer_gap_fence",
        "rate_half_mca_rank11_kernel_corank1_projective_pair_cap",
        "rate_half_mca_rank11_kernel_corank2_uniform_projective_basis_cap",
        "rate_half_mca_rank11_kernel_corank3_uniform_projective_basis_cap",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    r_value, w_value = int(p["R"]), int(p["w"])
    k_min, k_max = int(p["K_prime_minimum"]), int(p["K_prime_maximum"])
    require((r_value, w_value, k_min, k_max) == (1048576, 67472, 796599, 1048576), "range")
    caps = p["complete_record_caps"]
    require(caps == [8147918, 84416263, 983902549, 12232092309, 158406193634, 2109949210211, 28689347099870, 396280526311830, 5542092977392141], "complete caps")
    require(p["uniform_coranks"] == [1, 2, 3] and p["noncomplete_coranks"] == [4, 5, 6, 7, 8, 9], "corank split")
    require(p["noncomplete_weighted_maximizer"] == 1 and p["decorations"] == "d+2", "weighted structure")

    s_min, s_max = k_min - 10, k_max - 10
    dominance_checks = 0
    ratio_checks = 0
    for d in range(4, 10):
        q = d + 1
        f1 = f_value(r_value, w_value, d, 1)
        require(p["t1_F_fractions"][str(d)] == [f1.numerator, f1.denominator], f"F1 d={d}")
        require(f1 * comb(s_min - 1, q) > caps[d - 1] * comb(s_min, q), f"t1 dominance d={d}")
        dominance_checks += 1
        for s_value in (s_min, (s_min + s_max) // 2, s_max):
            for t in (1, max(1, (s_value - q) // 2), s_value - q - 1):
                if t < s_value - q:
                    ratio = weighted_ratio(r_value, w_value, s_value, d, t)
                    require(0 < ratio < 1, f"weighted ratio d={d}")
                    ratio_checks += 1
    require(dominance_checks == p["dominance_checks"] == 6, "dominance count")
    require(ratio_checks == p["ratio_checks"] == 54, "ratio count")
    require("does not promote" in str(data.get("nonclaim")), "nonclaim")
    return {"dominance": dominance_checks, "ratios": ratio_checks}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("K_prime_minimum", 796598),
        lambda item: item["parameters"]["complete_record_caps"].__setitem__(3, 12232092308),
        lambda item: item["parameters"].__setitem__("uniform_coranks", [1, 2, 3, 4]),
        lambda item: item["parameters"].__setitem__("noncomplete_weighted_maximizer", 0),
        lambda item: item["parameters"]["t1_F_fractions"]["4"].__setitem__(0, 1),
        lambda item: item.__setitem__("nonclaim", "uniform promotion"),
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
        "RATE_HALF_MCA_RANK11_KERNEL_SHORTENING_WEIGHTED_EXTENSION_CAP_PASS "
        f"dominance={result['dominance']} ratios={result['ratios']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
