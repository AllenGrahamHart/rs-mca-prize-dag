#!/usr/bin/env python3
"""Independent audit of common-support cancellation."""

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


def polynomial_value(coefficients: list[int], x: int, p: int) -> int:
    return sum(value * pow(x, i, p) for i, value in enumerate(coefficients)) % p


def audit(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "object")
    row = data.get("official")
    toy = data.get("toy")
    require(isinstance(row, dict) and isinstance(toy, dict), "records")
    n, dimension, agreement = row.get("n"), row.get("K"), row.get("m")
    redundancy = n - dimension
    excess = agreement - dimension
    require(redundancy == row.get("redundancy") == 1048576, "redundancy")
    require(excess == row.get("agreement_excess") == 67472, "excess")
    require(2 * redundancy // excess == row.get("critical_order_floor") == 31, "floor")
    require(row.get("critical_order") == 32, "order")
    require(
        dimension - row.get("common_support_size_maximum")
        == row.get("residual_dimension_minimum")
        == 4923,
        "residual minimum",
    )
    residual_min = row.get("residual_dimension_minimum")
    ceil_ratio = lambda numerator, denominator: (numerator + denominator - 1) // denominator
    require(
        ceil_ratio(32 * (residual_min + excess), residual_min + redundancy)
        == row.get("slope_degree_floor_at_residual_minimum")
        == 3,
        "minimum slope degree",
    )
    degree18_min = (17 * redundancy - 32 * excess) // 15 + 1
    require(
        degree18_min == row.get("residual_dimension_for_degree18_minimum") == 1044446,
        "degree-18 threshold",
    )
    require(
        dimension - degree18_min
        == row.get("common_support_for_degree18_maximum")
        == 4130,
        "degree-18 core",
    )

    p = toy.get("field")
    domain = toy.get("domain")
    common = set(toy.get("common_support"))
    slope = toy.get("slope")
    A = toy.get("A_coefficients")
    B = toy.get("B_coefficients")
    q = toy.get("residual_explanation_coefficients")
    require((p, domain, common, slope) == (17, list(range(11)), {0, 1}, 7), "toy base")
    residual_dimension = toy.get("K") - len(common)
    support = set(range(2, 8))
    agreements = set(common)
    for x in set(domain) - common:
        locator = x * (x - 1) % p
        qx = polynomial_value(q, x, p)
        if x in support:
            y = pow(x, residual_dimension, p)
            residual_slope = (qx - slope * y + slope * y) % p
        else:
            residual_slope = (qx + 1) % p
        lifted_slope = (
            polynomial_value(A, x, p)
            + slope * polynomial_value(B, x, p)
            + locator * residual_slope
        ) % p
        lifted_explanation = (
            polynomial_value(A, x, p)
            + slope * polynomial_value(B, x, p)
            + locator * qx
        ) % p
        if lifted_slope == lifted_explanation:
            agreements.add(x)
    require(agreements == common | support and len(agreements) == toy.get("m"), "toy support")
    require(len(support) > residual_dimension, "toy badness uniqueness")
    output = data.get("output")
    require(isinstance(output, dict) and output.get("common_support") == "empty", "output")
    return {"residual_min": row.get("residual_dimension_minimum"), "toy": len(support)}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = audit(data)
    controls = []
    for section, key, value in (
        ("official", "critical_order_floor", 30),
        ("official", "residual_dimension_minimum", 4922),
        ("official", "common_support_for_degree18_maximum", 4131),
        ("toy", "m", 7),
        ("output", "common_support", "nonempty"),
    ):
        altered = copy.deepcopy(data)
        altered[section][key] = value
        try:
            audit(altered)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "audit controls")
    print(
        "RATE_HALF_MCA_RANK11_ORDER32_COMMON_SUPPORT_CANCELLATION_AUDIT_PASS "
        f"Kmin={result['residual_min']} toy={result['toy']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
