#!/usr/bin/env python3
"""Verify the projective-paving integer-gap envelope."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "f62c32a69299fa026812eebb2490dbf74ffe00676e3a0e32d314fcd0f89d310c"
ROOT = Path(__file__).resolve().parents[3]


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def complete(p: dict[str, object], dimension: int) -> Fraction:
    r, w = int(p["R"]), int(p["w"])
    return Fraction(
        falling(r + dimension, dimension + 1),
        (dimension + 1) * falling(w + dimension - 1, dimension),
    )


def pointwise(p: dict[str, object], dimension: int, t: int) -> Fraction:
    r, w = int(p["R"]), int(p["w"])
    return Fraction(
        falling(r + dimension + t, dimension + 1),
        (w + dimension + t) * rising(w + 1, dimension - 1),
    )


def envelope(p: dict[str, object], kprime: int, dimension: int) -> int:
    return int(max(
        complete(p, dimension),
        pointwise(p, dimension, 1),
        pointwise(p, dimension, kprime - int(p["correction_dimension"])),
    ))


def validate(data: object) -> tuple[int, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-kernel-projective-paving-integer-gap-fence-v1",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_projective_paving_record_caps",
        "rate_half_mca_support_local_transversality_compiler",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(
        (p["R"], p["w"], p["correction_dimension"])
        == (1048576, 67472, 10),
        "base parameters",
    )
    require(
        (p["official_K_prime_minimum"], p["official_K_prime_maximum"])
        == (10, 1048576),
        "official range",
    )
    maximum_t = int(p["official_K_prime_maximum"]) - 10
    r, w = int(p["R"]), int(p["w"])
    g0 = Fraction((r + 1) * r, 2 * w)
    gmax = Fraction(
        (r + maximum_t + 1) * (r + maximum_t),
        2 * (w + maximum_t),
    )
    require(g0 > gmax, "corank-one endpoint dominance")
    require(int(g0) == p["corank1_uniform_cap"], "corank-one cap")
    for dimension in range(2, 10):
        sign0 = (dimension + 1) * (w + dimension) - r
        sign1 = dimension * maximum_t + sign0
        require(sign0 < sign1, "one-turn sign")
    kprime = int(p["audit_K_prime"])
    cap2, cap3 = envelope(p, kprime, 2), envelope(p, kprime, 3)
    require(cap2 == p["audit_corank2_cap"], "corank-two audit cap")
    require(cap3 == p["audit_corank3_cap"], "corank-three audit cap")
    require(cap2 > int(complete(p, 2)), "corank-two gap")
    require(cap3 > int(complete(p, 3)), "corank-three gap")
    evidence = data.get("evidence")
    require(isinstance(evidence, dict), "evidence")
    require(evidence.get("status") == "heuristic_only", "evidence status")
    script = ROOT / str(evidence["script"])
    result_path = ROOT / str(evidence["result"])
    require(
        hashlib.sha256(script.read_bytes()).hexdigest()
        == evidence["script_sha256"],
        "probe script hash",
    )
    require(
        hashlib.sha256(result_path.read_bytes()).hexdigest()
        == evidence["result_sha256"],
        "probe result hash",
    )
    result = json.loads(result_path.read_text())
    require(result.get("complete") is True, "probe completion")
    require(
        [row["kprime"] for row in result["frontier"]]
        == evidence["observed_frontier"],
        "probe frontier",
    )
    require("not claimed sharp" in str(data.get("nonclaim")), "nonclaim")
    return cap2, cap3


def main() -> None:
    require(
        hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256,
        "contract hash",
    )
    data = json.loads(CONTRACT.read_text())
    cap2, cap3 = validate(data)
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("correction_dimension", 11),
        lambda item: item["parameters"].__setitem__("official_K_prime_maximum", 2000000),
        lambda item: item["parameters"].__setitem__("corank1_uniform_cap", 8147917),
        lambda item: item["parameters"].__setitem__("audit_corank2_cap", 84416263),
        lambda item: item["parameters"].__setitem__("audit_corank3_cap", 983902549),
        lambda item: item["evidence"].__setitem__("status", "proved"),
        lambda item: item.__setitem__("nonclaim", "sharp"),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError, ZeroDivisionError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_PROJECTIVE_PAVING_INTEGER_GAP_FENCE_PASS "
        f"M2={cap2} M3={cap3} controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
