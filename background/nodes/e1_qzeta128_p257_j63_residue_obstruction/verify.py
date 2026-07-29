#!/usr/bin/env python3
"""Verify the auxiliary-prime residue obstruction for J_63."""

from __future__ import annotations

import json
from math import isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_qzeta128_p257_j63_residue_obstruction"
UNIT_NODE = "e1_conductor128_full_unit_circular_basis"
RELATION_NODE = "e1_qzeta128_p257_j63_stickelberger_relation"
CONSUMER = "e1_qzeta128_p257_j63_fixed_field_nonprincipality_certificate"
Q = 128
P = 257
ELL = 21121
R = 5406977
G = 3
COEFFICIENTS = [
    21121, -24549, -26280, -22490, -16564, -12336, -20492, -20254,
    -28314, -25086, -29901, -20529, -12414, -5602, -8856, -7172,
    2231, 7193, 0, 3708, 10233, 17881, 9371, 20529, 14851, 21121,
    15861, 21263, 29977, 42499, 39176, 46066,
]
PAIRS = [(32, 32)] + [(1, index - 1) for index in range(2, 33)]


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def character_logs() -> dict[int, int]:
    logs = {}
    value = 1
    for exponent in range(P - 1):
        assert value not in logs
        logs[value] = exponent
        value = value * 3 % P
    assert value == 1 and len(logs) == P - 1
    return logs


def jacobi_value(a: int, b: int, root: int, logs: dict[int, int]) -> int:
    value = 0
    for x in range(2, P):
        exponent = (a * logs[x] + b * logs[(1 - x) % P]) % Q
        value -= pow(root, exponent, R)
    return value % R


def psi(values: list[int]) -> int:
    result = 1
    for value in values:
        assert value
        result = result * pow(value, 256, R) % R
    return result


def main() -> None:
    assert R == 256 * ELL + 1
    assert is_prime(ELL) and is_prime(R)
    assert pow(G, R - 1, R) == 1
    assert pow(G, (R - 1) // 2, R) != 1
    assert pow(G, (R - 1) // ELL, R) != 1

    root = pow(G, (R - 1) // Q, R)
    omega = pow(G, (R - 1) // ELL, R)
    assert root == 3758939 and omega == 2166434
    assert pow(root, Q, R) == 1 and pow(root, Q // 2, R) == R - 1
    assert pow(omega, ELL, R) == 1 and omega != 1

    exponents = list(range(1, 64, 2))
    roots = [pow(root, s, R) for s in exponents]
    assert len(set(roots)) == 32

    for a in range(3, 64, 2):
        reductions = []
        for zeta in roots:
            eta = (
                pow(zeta, (1 - a) // 2, R)
                * (1 - pow(zeta, a, R))
                * pow(1 - zeta, -1, R)
            ) % R
            reductions.append(eta)
        assert psi(reductions) == 1

    logs = character_logs()
    alpha_reductions = []
    for zeta in roots:
        conjugate = pow(zeta, -1, R)
        alpha = 1
        for coefficient, (a, b) in zip(COEFFICIENTS, PAIRS):
            numerator = jacobi_value(a, b, zeta, logs)
            denominator = jacobi_value(a, b, conjugate, logs)
            assert numerator and denominator
            ratio = numerator * pow(denominator, -1, R) % R
            alpha = alpha * pow(ratio, coefficient % (R - 1), R) % R
        alpha_reductions.append(alpha)

    psi_alpha = psi(alpha_reductions)
    assert pow(omega, 20582, R) == 500235
    assert psi_alpha == 500235 != 1

    node_dir = ROOT / "background/nodes" / NODE
    proof = (node_dir / "proof.md").read_text()
    for text in ("Psi(eta_a)=1", "Psi(alpha)=500235", "I=J_63/bar(J_63)"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for node in (NODE, UNIT_NODE, RELATION_NODE, CONSUMER):
        assert nodes[node]["status"] == "PROVED"
    assert (UNIT_NODE, NODE, "req") in edges
    assert (RELATION_NODE, NODE, "req") in edges
    assert (NODE, CONSUMER, "req") in edges

    print(
        "E1_QZETA128_P257_J63_RESIDUE_OBSTRUCTION_PASS "
        f"r={R} units=31 jacobi_sums=32 embeddings=32 psi_alpha={psi_alpha}"
    )


if __name__ == "__main__":
    main()
