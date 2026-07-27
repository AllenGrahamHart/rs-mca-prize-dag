#!/usr/bin/env python3
"""Check the m=16 reciprocal-elimination result and its small radical."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m16_order_zero_reciprocal_elimination"
DEPS = (
    "l1_mersenne_next_to_maximal_hypergeometric_normal_form",
    "l1_mersenne_hnf_frobenius_reciprocal_gate",
)
CONSUMER = "l1_mixed_petal_amplification"
P = 8191
EXPECTED_HASHES = {
    "R12": "4d85a002b1a6859f596728ccb6a47946da5540bf2950ac5030e9aff9aa08f23d",
    "R13": "e9e428a171b0e4d421c2486eee0b7d2ad4fb2dc16eaabdf49ca126b52176a076",
    "gcd": "567ee9bf42f7ff97267c8a4b288bc4c4662688d17a1a65450df994ad120bfd94",
    "radical": "42c76c6b52be5c2a1ced34377e1e469fd3b0114ed2d0156f2e443baf0e640a5e",
}


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % P == 0:
        poly.pop()
    return [value % P for value in poly]


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    return trim(out)


def divide(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    remainder = trim(dividend[:])
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, P)
    while remainder != [0] and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1] * inverse % P
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            remainder[index + shift] = (remainder[index + shift] - coefficient * value) % P
        trim(remainder)
    return trim(quotient), remainder


def gcd(left: list[int], right: list[int]) -> list[int]:
    while right != [0]:
        _, remainder = divide(left, right)
        left, right = right, remainder
    inverse = pow(left[-1], -1, P)
    return trim([value * inverse for value in left])


def derivative(poly: list[int]) -> list[int]:
    return trim([index * poly[index] for index in range(1, len(poly))] or [0])


def remainder_multiply(left: list[int], right: list[int], modulus: list[int]) -> list[int]:
    _, remainder = divide(multiply(left, right), modulus)
    return remainder


def power_mod(base: list[int], exponent: int, modulus: list[int]) -> list[int]:
    out = [1]
    while exponent:
        if exponent & 1:
            out = remainder_multiply(out, base, modulus)
        base = remainder_multiply(base, base, modulus)
        exponent >>= 1
    return out


def singular_text(poly: list[int]) -> str:
    terms: list[str] = []
    for exponent in range(len(poly) - 1, -1, -1):
        coefficient = poly[exponent] % P
        if coefficient == 0:
            continue
        signed = coefficient if coefficient <= P // 2 else coefficient - P
        sign = "-" if signed < 0 else "+"
        magnitude = abs(signed)
        if exponent == 0:
            body = str(magnitude)
        else:
            scalar = "" if magnitude == 1 else str(magnitude)
            body = scalar + "s" + (str(exponent) if exponent != 1 else "")
        if not terms:
            terms.append(("-" if signed < 0 else "") + body)
        else:
            terms.append(sign + body)
    return "".join(terms) or "0"


def main() -> None:
    radical = [1]
    for root in (0, 1, *range(-1, -16, -1)):
        radical = multiply(radical, [-root, 1])
    assert len(radical) - 1 == 17
    assert gcd(radical, derivative(radical)) == [1]
    assert power_mod([0, 1], P, radical) == [0, 1]

    radical_text = singular_text(radical)
    assert hashlib.sha256(radical_text.encode()).hexdigest() == EXPECTED_HASHES["radical"]

    primary = json.loads(
        (ROOT / "experiments/prize_resolution/l1_mersenne_m16_reciprocal_gcd_result.json").read_text()
    )
    audit = json.loads(
        (ROOT / "experiments/prize_resolution/l1_mersenne_m16_reciprocal_companion_audit_result.json").read_text()
    )
    assert primary["status"] == audit["status"] == "COMPLETE"
    assert (primary["p"], primary["m"], primary["h"]) == (P, 16, 15)
    assert primary["sha256"] == EXPECTED_HASHES
    assert audit["sha256"] == EXPECTED_HASHES
    assert audit["uses_primary_Q_resultant"] is False
    assert audit["all_hashes_match_primary"] is True
    assert primary["radical_text"] == radical_text
    assert primary["radical_squarefree"] is True
    assert primary["radical_divides_s_to_p_minus_s"] is True
    assert primary["degrees"] == {
        "R12": 11472,
        "R13": 15296,
        "gcd": 9912,
        "gcd_derivative_gcd": 9895,
        "radical": 17,
        "radical_derivative_gcd": 0,
        "field_polynomial_remainder": -1,
    }

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    for dependency in DEPS:
        assert statuses[dependency] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_MERSENNE_HNF_M16_ORDER_ZERO_RECIPROCAL_ELIMINATION_PASS "
        "row=1 eliminants=2 degrees=11472,15296 gcd=9912 radical=17 audits=2"
    )


if __name__ == "__main__":
    main()
