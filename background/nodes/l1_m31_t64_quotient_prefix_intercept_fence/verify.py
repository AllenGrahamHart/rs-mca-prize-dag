#!/usr/bin/env python3
"""Exact replay of the M31 T64 quotient-prefix intercept fence."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m31_t64_quotient_prefix_intercept_fence"
CONSUMER = "l1_mixed_petal_amplification"
P = 2**31 - 1
SCALE = pow(2, -2047, P)
GENERATOR = (1717986917, 1288490189)
ACTIVE_ROOTS = (
    434373082, 614288294, 1713110565, 1533195353,
    1984437538, 380812851, 163046109, 1766670796,
)
PARTIAL_27 = (
    27, 37, 91, 101, 155, 165, 219, 229, 283, 293, 347, 357,
    411, 421, 475, 485, 539, 549, 603, 613, 667, 677, 731, 741,
    795, 805, 859, 869, 923, 933, 987,
)
MOVING = {"A": 5, "B1": 7, "B2": 9, "B3": 11,
          "B4": 13, "B5": 29, "B6": 31}
EXPECTED_TAU = (
    26164677, 1580223790, 280947147, 456695729,
    579625837, 1013961365, 194696271, 505542828,
    1641940819, 1952787376, 1133522282, 1567857810,
    1690787918, 1866536500, 567259857, 2121318970,
)
ETA = (
    2144970186, 693846040, 254084710, 1501952290,
    1904231690, 558873387, 1400618348, 1749425225,
    2110682204, 1763030673, 102589073, 1770388691,
    971529856, 948975681, 774218929, 1490251835,
    2095038705, 838625156, 774891784, 644995098,
    888552471, 1685238706, 1330006363, 1053276022,
    1544945819, 100722017, 1420529349, 1803184017,
    1196844108, 324775767, 591689729, 1982980281,
)
EXPECTED_H64 = int(
    "586374616784432967317447344396311850952251481404090129066339701269086144611744331859382537679275957595113162682732279972248681107329260801825759429939073953027297000"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def mul_pair(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    a, b = left
    c, d = right
    return ((a * c - b * d) % P, (a * d + b * c) % P)


def pow_pair(base: tuple[int, int], exponent: int) -> tuple[int, int]:
    out = (1, 0)
    while exponent:
        if exponent & 1:
            out = mul_pair(out, base)
        base = mul_pair(base, base)
        exponent >>= 1
    return out


def chebyshev_power_two(value: int, log_exponent: int) -> int:
    out = value % P
    for _ in range(log_exponent):
        out = (2 * out * out - 1) % P
    return out


def labels() -> dict[int, int]:
    return {
        r: SCALE * pow_pair(GENERATOR, r * 2**19)[0] % P
        for r in range(1, 2048, 2)
    }


def block(a: int) -> tuple[int, ...]:
    return tuple(
        r for r in range(1, 2048, 2) if r % 64 in {a, 64 - a}
    )


def multiply_linear(poly: list[int], root: int) -> list[int]:
    out = [0] * (len(poly) + 1)
    for index, coefficient in enumerate(poly):
        out[index] = (out[index] - root * coefficient) % P
        out[index + 1] = (out[index + 1] + coefficient) % P
    return out


def prefix(reps: tuple[int, ...], quotient_labels: dict[int, int], depth: int) -> tuple[int, ...]:
    poly = [1]
    for rep in reps:
        poly = multiply_linear(poly, quotient_labels[rep])
    require(poly[-1] == 1, "locator is not monic")
    return tuple(reversed(poly[:-1]))[:depth]


def main() -> None:
    conjugate = (GENERATOR[0], -GENERATOR[1] % P)
    require(mul_pair(GENERATOR, conjugate) == (1, 0), "generator norm")
    require(pow_pair(GENERATOR, 2**30) == (P - 1, 0), "generator half order")
    require(pow_pair(GENERATOR, 2**31) == (1, 0), "generator full order")

    quotient_labels = labels()
    require(len(quotient_labels) == 1024, "label count")
    require(len(set(quotient_labels.values())) == 1024, "duplicate label")

    require(all(chebyshev_power_two(x, 21) == 0 for x in ACTIVE_ROOTS),
            "active roots")
    active_labels = tuple(
        SCALE * chebyshev_power_two(x, 11) % P for x in ACTIVE_ROOTS
    )
    require(active_labels == (quotient_labels[1],) * 4 + (quotient_labels[3],) * 4,
            "active punctures")

    taus = []
    for a in range(1, 32, 2):
        reps = block(a)
        values = tuple(quotient_labels[r] for r in reps)
        tau = chebyshev_power_two(2 * quotient_labels[a], 6)
        require(len(reps) == len(set(values)) == 64, f"block {a} size")
        require(all(chebyshev_power_two(2 * value, 6) == tau for value in values),
                f"block {a} is not a T64 fiber")
        taus.append(tau)
    require(tuple(taus) == EXPECTED_TAU, "T64 values")

    allowed = set(range(1, 2048, 2)) - {1, 3}
    common = set(PARTIAL_27)
    for a in (15, 17, 19, 21, 23, 25):
        common.update(block(a))
    require(len(common) == 415 and common <= allowed, "common core")

    supports: dict[str, tuple[int, ...]] = {}
    prefixes = set()
    for name, moving_class in MOVING.items():
        reps = tuple(sorted(common | set(block(moving_class))))
        require(len(reps) == 479 and set(reps) <= allowed, f"support {name}")
        pref = prefix(reps, quotient_labels, 63)
        require(pref[:32] == ETA, f"target mismatch for {name}")
        prefixes.add(pref)
        supports[name] = reps
    require(len(prefixes) == 1, "first 63 coefficients differ")
    require(len({supports[name] for name in supports}) == 7, "duplicate support")

    anchor = set(supports["A"])
    for index in range(1, 7):
        neighbor = set(supports[f"B{index}"])
        require(len(anchor - neighbor) == len(neighbor - anchor) == 64,
                f"wrong deficiency B{index}")
        require(len(anchor & neighbor) == 415, f"wrong core B{index}")

    h64 = comb(479, 64) * comb(543, 64)
    require(h64 == EXPECTED_H64, "H64 mismatch")
    q32 = P**32
    require(4 * h64 < q32, "shell floor is not zero")
    for intercept in (3, 4, 5):
        require(q32 * (6 - intercept) > 4 * h64,
                f"intercept {intercept} not refuted")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    require(nodes[NODE]["status"] == "PROVED", "DAG status")
    require((NODE, CONSUMER, "ev") in edges, "DAG evidence edge")

    print(
        "L1_M31_T64_QUOTIENT_PREFIX_INTERCEPT_FENCE_PASS "
        "labels=1024 punctured=1022 supports=7 deficiency=64 "
        "matching_prefix=63 rooted_degree>=6 floor4H_over_p32=0"
    )


if __name__ == "__main__":
    main()
