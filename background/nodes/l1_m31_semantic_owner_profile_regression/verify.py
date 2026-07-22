#!/usr/bin/env python3
"""Replay the M31 profile arithmetic and the F_241 semantic owner fixture."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m31_semantic_owner_profile_regression"
CONSUMER = "l1_mixed_petal_amplification"
P = 241
DOMAIN = [
    1, 235, 36, 25, 91, 177, 143, 106, 87, 201,
    240, 6, 205, 216, 150, 64, 98, 135, 154, 40,
]
U0 = [108, 150, 68, 65, 34, 129, 22, 52, 33, 226, 174] + [0] * 9
U1 = [5, 28, 224, 117, 204, 112, 224, 189, 230, 72, 55] + [0] * 9
SUPPORTS = [
    [0, 1, 2, 4, 6, 7, 12, 15, 17, 19],
    [0, 1, 3, 4, 6, 8, 13, 15, 18, 19],
    [0, 1, 3, 5, 8, 10, 13, 15, 16, 18],
    [0, 1, 4, 5, 9, 10, 14, 15, 16, 19],
    [0, 1, 4, 7, 8, 9, 11, 17, 18, 19],
    [0, 2, 3, 4, 5, 6, 12, 13, 15, 16],
    [0, 2, 4, 5, 7, 9, 11, 12, 16, 17],
    [0, 3, 4, 5, 8, 9, 11, 13, 16, 18],
    [1, 2, 3, 7, 8, 12, 13, 16, 17, 18],
    [1, 2, 4, 7, 9, 12, 14, 16, 17, 19],
    [2, 5, 6, 10, 11, 13, 14, 17, 18, 19],
]
COEFFICIENTS = [
    [171, 176, 191, 210, 94, 14, 115, 194],
    [140, 201, 133, 161, 175, 152, 122, 208],
    [37, 130, 27, 158, 108, 217, 147, 117],
    [41, 230, 170, 54, 57, 142, 7, 72],
    [102, 124, 184, 203, 150, 123, 162, 210],
    [22, 120, 143, 5, 219, 42, 154, 126],
    [175, 213, 233, 115, 82, 137, 119, 127],
    [1, 64, 94, 180, 21, 62, 176, 45],
    [120, 53, 101, 117, 179, 171, 101, 131],
    [86, 93, 79, 56, 134, 84, 102, 221],
    [113, 237, 177, 78, 216, 69, 11, 189],
]
SCALES = [194, 208, 117, 72, 210, 126, 127, 45, 131, 221, 189]
RAYS = [
    [22, 227, 119, 175, 239, 92, 136, 1],
    [98, 213, 69, 185, 2, 10, 230, 1],
    [196, 135, 130, 127, 38, 179, 199, 1],
    [24, 117, 76, 61, 51, 89, 57, 1],
    [90, 237, 134, 9, 104, 66, 228, 1],
    [4, 219, 26, 220, 237, 161, 28, 1],
    [64, 144, 110, 166, 198, 225, 111, 1],
    [75, 221, 61, 4, 129, 71, 186, 1],
    [218, 28, 67, 80, 40, 154, 67, 1],
    [68, 152, 225, 190, 162, 44, 19, 1],
    [21, 204, 131, 119, 70, 96, 162, 1],
]
SLOPES = [115, 44, 22, 133, 230, 0, 74, 107, 56, 9, 193]
PARITIES = [
    [126, 49, 25, 199, 4, 139, 174, 112, 71, 65],
    [124, 197, 153, 180, 21, 201, 21, 137, 2, 169],
    [193, 29, 219, 11, 62, 60, 200, 218, 212, 1],
    [68, 128, 109, 125, 229, 156, 82, 133, 113, 62],
    [42, 33, 206, 62, 191, 9, 165, 62, 89, 105],
    [9, 157, 93, 72, 154, 230, 219, 224, 206, 82],
    [108, 29, 227, 182, 71, 40, 4, 150, 14, 139],
    [3, 197, 60, 72, 7, 104, 21, 42, 194, 23],
    [50, 108, 60, 85, 50, 116, 68, 191, 173, 63],
    [229, 85, 41, 145, 179, 127, 22, 12, 125, 240],
    [138, 46, 205, 127, 37, 196, 121, 2, 178, 155],
]
LOCATOR_A = [25, 68, 25, 95, 0, 89, 90, 46, 135, 149, 1]
LOCATOR_B = [201, 179, 205, 0, 146, 154, 35, 0, 135, 149, 1]
COMMON_CORE = [0, 1, 15]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def evaluate(coefficients: list[int], value: int) -> int:
    out = 0
    for coefficient in reversed(coefficients):
        out = (coefficient + value * out) % P
    return out


def prefix(support: list[int]) -> tuple[int, int]:
    values = [DOMAIN[index] for index in support]
    first = sum(values) % P
    second = sum(
        values[i] * values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    ) % P
    return first, second


def weighted_sum(weights: list[int], support: list[int], values: list[int]) -> int:
    require(len(weights) == len(support), "weight/support length")
    return sum(weight * values[index] for weight, index in zip(weights, support)) % P


def exchange_distance(left: list[int], right: list[int]) -> int:
    return len(left) - len(set(left) & set(right))


def root_indices(coefficients: list[int]) -> list[int]:
    return [
        index for index, value in enumerate(DOMAIN)
        if evaluate(coefficients, value) == 0
    ]


def main() -> None:
    m31_p = 2**31 - 1
    m31_n = 2**21
    m31_a = 1_116_023
    omega = 981_129
    average_ceil = 1_993_678
    require(m31_n - m31_a == omega, "M31 complement")
    require(m31_n // omega == 2, "M31 one-pencil cap")
    require(1 + average_ceil == 1_993_679, "M31 natural numerator")
    require(1 <= m31_p and 2 <= m31_p, "M31 slope budgets")
    require(1 <= 1_993_679 and 2 <= 1_993_679, "M31 natural budgets")

    require(DOMAIN == [pow(235, index, P) for index in range(20)], "domain powers")
    require(len(set(DOMAIN)) == 20 and pow(235, 20, P) == 1, "domain order")
    require(all(pow(235, exponent, P) != 1 for exponent in range(1, 20)),
            "generator exact order")
    require(len(SUPPORTS) == len(COEFFICIENTS) == len(SCALES) == 11,
            "record count")
    require(len(set(SLOPES)) == 11, "duplicate slopes")
    require(len({tuple(ray) for ray in RAYS}) == 11, "duplicate rays")
    require(len({tuple(support) for support in SUPPORTS}) == 11,
            "duplicate supports")

    for record in range(11):
        support = SUPPORTS[record]
        coefficients = COEFFICIENTS[record]
        parity = PARITIES[record]
        require(len(support) == len(set(support)) == 10, f"support {record}")
        require(all(0 <= index < 20 for index in support), f"domain {record}")
        require(prefix(support) == (92, 135), f"prefix {record}")
        for index in support:
            expected = (U0[index] + SLOPES[record] * U1[index]) % P
            require(evaluate(coefficients, DOMAIN[index]) == expected,
                    f"agreement {record}:{index}")
        for degree in range(8):
            monomial = [pow(value, degree, P) for value in DOMAIN]
            require(weighted_sum(parity, support, monomial) == 0,
                    f"parity moment {record}:{degree}")
        require(weighted_sum(parity, support, U1) != 0,
                f"parity direction {record}")
        require(SCALES[record] != 0 and RAYS[record][-1] == 1,
                f"ray normalization {record}")
        require(
            [(SCALES[record] * value) % P for value in RAYS[record]]
            == coefficients,
            f"ray scaling {record}",
        )

    require(root_indices(LOCATOR_A) == SUPPORTS[0], "locator A roots")
    require(root_indices(LOCATOR_B) == SUPPORTS[2], "locator B roots")
    require(sorted(set(SUPPORTS[0]) & set(SUPPORTS[2])) == COMMON_CORE,
            "common core")
    outside = [index for index in range(20) if index not in COMMON_CORE]
    split_parameters = []
    for parameter in range(P + 1):
        coefficients = LOCATOR_B if parameter == P else [
            (left + parameter * right) % P
            for left, right in zip(LOCATOR_A, LOCATOR_B)
        ]
        moving_roots = sum(
            evaluate(coefficients, DOMAIN[index]) == 0 for index in outside
        )
        if moving_roots >= 7:
            split_parameters.append(parameter)
    require(split_parameters == [0, 241], "split pencil parameters")
    require([SLOPES[0], SLOPES[2]] == [115, 22], "owner slopes")

    anchor = SUPPORTS[10]
    require(all(exchange_distance(anchor, support) == 6 for support in SUPPORTS[:10]),
            "distance-six shell")
    residual = [index for index in range(10) if index not in {0, 2}]
    require(residual == [1, 3, 4, 5, 6, 7, 8, 9], "residual filter")
    denominator = P**2
    ambient = comb(10, 6) ** 2
    left = denominator * (len(residual) - 3)
    right = 7 * ambient
    require((denominator, ambient, left, right, right - left)
            == (58_081, 44_100, 290_405, 308_700, 18_295),
            "3+7 arithmetic")

    dag = json.loads((ROOT / "dag.json").read_text(encoding="utf-8"))
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    require(nodes[NODE]["status"] == "PROVED", "DAG status")
    require((NODE, CONSUMER, "ev") in edges, "DAG evidence edge")
    require(not any(edge[0] == NODE and edge[2] != "ev" for edge in edges),
            "unexpected required consumer")

    print(
        "L1_M31_SEMANTIC_OWNER_PROFILE_REGRESSION_PASS "
        "m31_caps=1,2 semantic_states=11 owner_slopes=2 residual=8 margin=18295"
    )


if __name__ == "__main__":
    main()
