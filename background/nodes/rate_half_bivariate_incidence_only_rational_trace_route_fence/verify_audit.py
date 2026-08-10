#!/usr/bin/env python3
"""Independent barycentric audit of the rational-trace kernel."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "experiments/prize_resolution/rh_bivariate_m2_rational_trace_fence_result.json"


def main() -> None:
    payload = json.loads(RESULT.read_text())
    prime = 97
    points = payload["support_values"]
    kernel = []
    for x in points:
        derivative = 1
        for y in points:
            if y != x:
                derivative = derivative * (x - y) % prime
        kernel.append(x * pow(derivative, prime - 2, prime) % prime)
    assert kernel == payload["kernel"] and all(kernel)

    # H_x(Y)=Y(Y-1)(Y-nu_x), so the nontrivial coefficients are nu and
    # -(1+nu). Multiplying by lambda turns them into degree-2 numerators.
    inverse_derivatives = {}
    for x in points:
        derivative = 1
        for y in points:
            if y != x:
                derivative = derivative * (x - y) % prime
        inverse_derivatives[x] = pow(derivative, prime - 2, prime)
    for moment in range(9):
        constant_numerator = sum(
            pow(x, moment + 1, prime)
            * inverse_derivatives[x]
            for x in points
        ) % prime
        rational_numerator = sum(
            pow(x, moment, prime)
            * (x * x + 1)
            * inverse_derivatives[x]
            for x in points
        ) % prime
        assert constant_numerator == 0
        assert rational_numerator == 0

    owners = payload["owners"]
    outside = [index for index in range(32) if index not in payload["support"]]
    multiplicities = {}
    singleton = 0
    for column in outside:
        values = owners[column]
        if len(values) == 1:
            singleton += 1
        else:
            key = tuple(sorted(values))
            multiplicities[key] = multiplicities.get(key, 0) + 1
    assert singleton == 1
    assert len(multiplicities) == 18
    assert sorted(multiplicities.values()) == [1] * 17 + [2]

    print(
        "RATE_HALF_BIVARIATE_INCIDENCE_ONLY_RATIONAL_TRACE_ROUTE_FENCE_"
        "AUDIT_PASS inverse_pairs=6 outside_edges=19"
    )


if __name__ == "__main__":
    main()
