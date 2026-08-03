#!/usr/bin/env python3
"""Independent root and boundary audit for cell-4 xi0/pairing0."""

import ast
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi0_pairing0_four_basis_norm_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi0_pairing0_four_basis_norm_result.json"
)
PRIME = 2130706433
r = sp.symbols("r")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def trim(value):
    value = [item % PRIME for item in value]
    while len(value) > 1 and value[-1] == 0:
        value.pop()
    return value or [0]


def remainder(left, right):
    left = trim(left[:])
    right = trim(right[:])
    inverse = pow(right[-1], -1, PRIME)
    while len(left) >= len(right) and left != [0]:
        shift = len(left) - len(right)
        quotient = left[-1] * inverse % PRIME
        if quotient:
            for index, value in enumerate(right):
                left[index + shift] = (
                    left[index + shift] - quotient * value
                ) % PRIME
        left = trim(left)
    return left


def multiply_mod(left, right, modulus):
    output = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        if left_value:
            for j, right_value in enumerate(right):
                output[i + j] = (
                    output[i + j] + left_value * right_value
                ) % PRIME
    return remainder(output, modulus)


def power_mod(base, exponent, modulus):
    output = [1]
    while exponent:
        if exponent & 1:
            output = multiply_mod(output, base, modulus)
        base = multiply_mod(base, base, modulus)
        exponent //= 2
    return output


def gcd(left, right):
    left = trim(left)
    right = trim(right)
    while right != [0]:
        left, right = right, remainder(left, right)
    inverse = pow(left[-1], -1, PRIME)
    return [(value * inverse) % PRIME for value in left]


def coefficients(profile):
    polynomial = sp.Poly(
        sp.sympify(profile["expression"]), r, modulus=PRIME
    )
    output = [0] * (polynomial.degree() + 1)
    for (degree,), value in polynomial.terms():
        output[degree] = int(value) % PRIME
    return trim(output)


def evaluate(polynomial, point):
    output = 0
    for value in reversed(polynomial):
        output = (output * point + value) % PRIME
    return output


def multiply(left, right):
    output = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            output[i + j] = (
                output[i + j] + left_value * right_value
            ) % PRIME
    return trim(output)


def field_root_part(polynomial):
    if polynomial == [0]:
        return None
    if len(polynomial) == 1:
        return [1]
    x_to_p = power_mod([0, 1], PRIME, polynomial)
    if len(x_to_p) < 2:
        x_to_p.extend([0] * (2 - len(x_to_p)))
    x_to_p[1] = (x_to_p[1] - 1) % PRIME
    return gcd(polynomial, trim(x_to_p))


def audit_profile(profile, candidates):
    polynomial = coefficients(profile)
    root_part = field_root_part(polynomial)
    require(root_part is not None, "identically zero root polynomial")
    found = sorted(point for point in candidates if evaluate(polynomial, point) == 0)
    reconstructed = [1]
    for point in found:
        reconstructed = multiply(reconstructed, [(-point) % PRIME, 1])
    require(root_part == reconstructed, "incomplete finite-field root list")
    return found


def main():
    ast.parse(SCRIPT.read_text())
    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 4, "four result rows")
    audited_polynomials = 0
    for row in payload["rows"]:
        candidates = row["candidate_roots"]
        target = audit_profile(row["target_norm"]["numerator"], candidates)
        audited_polynomials += 1
        require(target == row["target_roots"], "target root replay")
        union = set(target)
        for value in [*row["inverse_guards"], row["target_norm"]]:
            for side in ("numerator", "denominator"):
                union.update(audit_profile(value[side], candidates))
                audited_polynomials += 1
        require(sorted(union) == candidates, "candidate root union")
        require({value["r"] for value in row["boundary_rows"]} == set(union),
                "boundary payment")
        require(not row["finite_rows"] and not row["unresolved"] and
                not row["witnesses"], "terminal ledgers")
    statement = (NODE / "statement.md").read_text()
    audit = (NODE / "audit.md").read_text()
    require("16" in statement and "sound direction" in audit and
            "one of `7*15=105`" in audit, "scope fences")
    print(f"audit=ok rows=4 polynomials={audited_polynomials} candidates=28")


if __name__ == "__main__":
    main()
