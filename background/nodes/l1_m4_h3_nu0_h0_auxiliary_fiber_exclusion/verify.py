#!/usr/bin/env python3
"""Verify the auxiliary-fiber exceptional-packet exclusion."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_nu0_h0_auxiliary_fiber_exclusion"
SUPPLIER = "l1_m4_h3_nu0_h0_universal_packet_exclusion"
CONSUMER = "l1_mixed_petal_amplification"
P = 2147483647
A = 844833809
B = 2002167159
EXPECTED_POLY = [573306971, 664831389, 1800058023, 1]
EXPECTED_REMAINDER = [876663072]


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % P == 0:
        poly.pop()
    return [value % P for value in poly]


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % P
    return trim(out)


def remainder(dividend: list[int], divisor: list[int]) -> list[int]:
    dividend = trim(dividend[:])
    inverse_leader = pow(divisor[-1], -1, P)
    while len(dividend) >= len(divisor):
        scale = dividend[-1] * inverse_leader % P
        offset = len(dividend) - len(divisor)
        for index, value in enumerate(divisor):
            dividend[offset + index] = \
                (dividend[offset + index] - scale * value) % P
        trim(dividend)
    return dividend


def power_x(exponent: int, modulus: list[int]) -> list[int]:
    out, base = [1], [0, 1]
    while exponent:
        if exponent & 1:
            out = remainder(multiply(out, base), modulus)
        base = remainder(multiply(base, base), modulus)
        exponent >>= 1
    return out


def main() -> None:
    assert (9 * B - 4 * A * A - 6 * A) % P == 0
    sigma = 2 * A * pow(3, -1, P) % P
    scale = (sigma - 1) % P
    constant = (1 + A + B) % P
    poly = [
        constant * pow(scale, -3, P) % P,
        (A + 3) * pow(scale, -2, P) % P,
        3 * pow(scale, -1, P) % P,
        1,
    ]
    assert poly == EXPECTED_POLY
    observed = power_x(4 * (P + 1), poly)
    observed[0] = (observed[0] - 1) % P
    assert trim(observed) == EXPECTED_REMAINDER
    checks = 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (SUPPLIER, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    checks += 5

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(AFE2)", "(AFE3)", "(AFE4)", "876663072",
                   "entire `nu=0,b!=0,deg H=0` endpoint", "does not"):
        assert anchor in statement
        checks += 1
    print(f"L1_M4_H3_NU0_H0_AUXILIARY_FIBER_EXCLUSION_PASS checks={checks}")


if __name__ == "__main__":
    main()
