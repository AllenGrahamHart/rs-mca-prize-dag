#!/usr/bin/env python3
"""Verify the order-32 common-support cancellation adapter."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "a7560d26144727a5ccbbda52922e20281b3ddcf92e4907016a39dad53eefa36a"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def trim(poly: list[int], p: int) -> list[int]:
    out = [value % p for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    return trim(
        [
            (left[i] if i < len(left) else 0)
            + (right[i] if i < len(right) else 0)
            for i in range(size)
        ],
        p,
    )


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([scalar * value for value in poly], p)


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return trim(out, p)


def evaluate(poly: list[int], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def validate_toy(toy: object) -> int:
    require(isinstance(toy, dict), "toy")
    p = toy.get("field")
    domain = toy.get("domain")
    dimension = toy.get("K")
    agreement = toy.get("m")
    common = toy.get("common_support")
    slope = toy.get("slope")
    require(
        (p, domain, dimension, agreement, common, slope)
        == (17, list(range(11)), 6, 8, [0, 1], 7),
        "toy constants",
    )
    A = toy.get("A_coefficients")
    B = toy.get("B_coefficients")
    q = toy.get("residual_explanation_coefficients")
    require((A, B, q) == ([3, 2], [5, 1], [4, 0, 3, 1]), "toy polynomials")
    locator = [0, -1, 1]
    explanation = add(add(A, scale(B, slope, p), p), multiply(locator, q, p), p)
    require(len(explanation) - 1 < dimension, "toy lifted degree")
    residual_dimension = dimension - len(common)
    residual_support = set(range(2, 8))
    original_support = set(common) | residual_support
    r0: dict[int, int] = {}
    r1: dict[int, int] = {}
    for x in common:
        r0[x] = evaluate(A, x, p)
        r1[x] = evaluate(B, x, p)
    for x in set(domain) - set(common):
        locator_value = evaluate(locator, x, p)
        q_value = evaluate(q, x, p)
        if x in residual_support:
            residual_r1 = pow(x, residual_dimension, p)
            residual_r0 = (q_value - slope * residual_r1) % p
        else:
            residual_r1 = 0
            residual_r0 = (q_value + 1) % p
        r0[x] = (evaluate(A, x, p) + locator_value * residual_r0) % p
        r1[x] = (evaluate(B, x, p) + locator_value * residual_r1) % p
    agreements = {
        x
        for x in domain
        if (r0[x] + slope * r1[x] - evaluate(explanation, x, p)) % p == 0
    }
    require(agreements == original_support and len(agreements) == agreement, "toy exact support")
    require(len(residual_support) == agreement - len(common), "toy residual support")
    require(residual_dimension < len(residual_support), "toy uniqueness range")
    # The residual direction is X^K' on more than K' points, so no
    # degree-below-K' direction codeword agrees there.
    require(residual_dimension == 4 and len(residual_support) == 6, "toy badness guard")
    return len(residual_support)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-order32-common-support-cancellation-v1",
        "schema",
    )
    require(
        data.get("dependency")
        == "rate_half_mca_rank11_heavy_pair_order32_seed_compiler",
        "dependency",
    )
    row = data.get("official")
    require(isinstance(row, dict), "official")
    n, dimension, agreement = (row.get(key) for key in ("n", "K", "m"))
    require((n, dimension, agreement) == (2097152, 1048576, 1116048), "row")
    redundancy = n - dimension
    excess = agreement - dimension
    c_max = row.get("common_support_size_maximum")
    residual_min = dimension - c_max
    critical_numerator = 2 * redundancy
    critical_floor = critical_numerator // excess
    critical_order = critical_floor + 1
    degree_floor_min = (32 * (residual_min + excess) + redundancy + residual_min - 1) // (
        redundancy + residual_min
    )
    degree_floor_deployed = (32 * agreement + n - 1) // n
    degree18_min = (17 * redundancy - 32 * excess) // 15 + 1
    degree18_core_max = dimension - degree18_min
    require(
        (
            redundancy,
            excess,
            row.get("seed_size"),
            c_max,
            residual_min,
            row.get("residual_dimension_maximum"),
            critical_numerator,
            critical_floor,
            critical_order,
        )
        == tuple(
            row.get(key)
            for key in (
                "redundancy",
                "agreement_excess",
                "seed_size",
                "common_support_size_maximum",
                "residual_dimension_minimum",
                "residual_dimension_maximum",
                "critical_order_numerator",
                "critical_order_floor",
                "critical_order",
            )
        )
        == (1048576, 67472, 32, 1043653, 4923, 1048576, 2097152, 31, 32),
        "parameter ledger",
    )
    require(
        (
            degree_floor_min,
            degree_floor_deployed,
            degree18_min,
            degree18_core_max,
        )
        == tuple(
            row.get(key)
            for key in (
                "slope_degree_floor_at_residual_minimum",
                "slope_degree_floor_at_deployed_dimension",
                "residual_dimension_for_degree18_minimum",
                "common_support_for_degree18_maximum",
            )
        )
        == (3, 18, 1044446, 4130),
        "slope-degree route boundary",
    )
    output = data.get("output")
    require(isinstance(output, dict), "output")
    require(output.get("code_family") == "RS[F,D_without_C,K_minus_c]", "code family")
    require(output.get("common_support") == "empty", "common support")
    preserved = output.get("preserved")
    require(isinstance(preserved, list) and "support-wise MCA badness" in preserved, "badness")
    require("critical order 32" in preserved, "critical order preservation")
    require("degree-18 floor" in str(output.get("nonclaim")), "nonclaim")
    toy_support = validate_toy(data.get("toy"))
    return {"critical_order": critical_order, "residual_min": residual_min, "toy_support": toy_support}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["official"].__setitem__("common_support_size_maximum", 1043654),
        lambda item: item["official"].__setitem__("residual_dimension_minimum", 4922),
        lambda item: item["official"].__setitem__("critical_order", 31),
        lambda item: item["official"].__setitem__("residual_dimension_for_degree18_minimum", 1044445),
        lambda item: item["output"].__setitem__("common_support", "unknown"),
        lambda item: item["toy"].__setitem__("slope", 6),
        lambda item: item.__setitem__("dependency", "rate_half_band_crossing_location"),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_ORDER32_COMMON_SUPPORT_CANCELLATION_PASS "
        f"Kmin={result['residual_min']} order={result['critical_order']} "
        f"toy={result['toy_support']} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
