#!/usr/bin/env python3
"""Run the 32 exact h=7 two-pair norm gcds on Modal.

The local entrypoint writes after every returned packet, so an interrupted
map retains all completed rows. Do not launch while the workspace spend
limit is active.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TypeAlias

import modal


HERE = Path(__file__).resolve().parent
RESULT = HERE / "modal_gcd_result.json"
PRIMES = (8191, 131071, 524287, 2147483647)
F_COEFFICIENTS = (4860, -44172, 8199, -15516, 2862, 672, -180, 10, 5)

Element: TypeAlias = tuple[int, int]
Polynomial: TypeAlias = list[Element]

app = modal.App("l1-h7-order-one-quadratic-two-pair-gcd")


def ff_add(left: Element, right: Element, p: int) -> Element:
    return ((left[0] + right[0]) % p, (left[1] + right[1]) % p)


def ff_sub(left: Element, right: Element, p: int) -> Element:
    return ((left[0] - right[0]) % p, (left[1] - right[1]) % p)


def ff_mul(left: Element, right: Element, p: int) -> Element:
    return (
        (left[0] * right[0] - left[1] * right[1]) % p,
        (left[0] * right[1] + left[1] * right[0]) % p,
    )


def ff_inv(value: Element, p: int) -> Element:
    norm = (value[0] * value[0] + value[1] * value[1]) % p
    if norm == 0:
        raise ZeroDivisionError("zero in F_(p^2)")
    inverse = pow(norm, p - 2, p)
    return (value[0] * inverse % p, -value[1] * inverse % p)


def ff_pow(value: Element, exponent: int, p: int) -> Element:
    out = (1, 0)
    base = value
    while exponent:
        if exponent & 1:
            out = ff_mul(out, base, p)
        base = ff_mul(base, base, p)
        exponent >>= 1
    return out


def trim(poly: Polynomial) -> Polynomial:
    while len(poly) > 1 and poly[-1] == (0, 0):
        poly.pop()
    return poly


def poly_sub(left: Polynomial, right: Polynomial, p: int) -> Polynomial:
    out = [(0, 0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] = ff_add(out[index], value, p)
    for index, value in enumerate(right):
        out[index] = ff_sub(out[index], value, p)
    return trim(out)


def poly_mul(left: Polynomial, right: Polynomial, p: int) -> Polynomial:
    out = [(0, 0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = ff_add(out[i + j], ff_mul(a, b, p), p)
    return trim(out)


def poly_divmod(dividend: Polynomial, divisor: Polynomial, p: int) -> tuple[Polynomial, Polynomial]:
    dividend = trim(dividend[:])
    divisor = trim(divisor[:])
    if divisor == [(0, 0)]:
        raise ZeroDivisionError("zero polynomial")
    quotient = [(0, 0)] * max(1, len(dividend) - len(divisor) + 1)
    divisor_lead_inverse = ff_inv(divisor[-1], p)
    while len(dividend) >= len(divisor) and dividend != [(0, 0)]:
        offset = len(dividend) - len(divisor)
        scalar = ff_mul(dividend[-1], divisor_lead_inverse, p)
        quotient[offset] = scalar
        shifted = [(0, 0)] * offset + [ff_mul(scalar, value, p) for value in divisor]
        dividend = poly_sub(dividend, shifted, p)
    return trim(quotient), trim(dividend)


def poly_monic(poly: Polynomial, p: int) -> Polynomial:
    poly = trim(poly[:])
    inverse = ff_inv(poly[-1], p)
    return [ff_mul(value, inverse, p) for value in poly]


def poly_mod(poly: Polynomial, modulus: Polynomial, p: int) -> Polynomial:
    return poly_divmod(poly, modulus, p)[1]


def poly_pow_x(exponent: int, modulus: Polynomial, p: int) -> Polynomial:
    out = [(1, 0)]
    base = [(0, 0), (1, 0)]
    while exponent:
        if exponent & 1:
            out = poly_mod(poly_mul(out, base, p), modulus, p)
        base = poly_mod(poly_mul(base, base, p), modulus, p)
        exponent >>= 1
    return out


def poly_gcd(left: Polynomial, right: Polynomial, p: int) -> Polynomial:
    left = trim(left[:])
    right = trim(right[:])
    while right != [(0, 0)]:
        left, right = right, poly_mod(left, right, p)
    return poly_monic(left, p)


def poly_exact_div(dividend: Polynomial, divisor: Polynomial, p: int) -> Polynomial:
    quotient, remainder = poly_divmod(dividend, divisor, p)
    if remainder != [(0, 0)]:
        raise ArithmeticError("nonexact polynomial division")
    return quotient


def saturate(poly: Polynomial, saturation: Polynomial, p: int) -> Polynomial:
    out = poly_monic(poly, p)
    while len(out) > 1:
        common = poly_gcd(out, saturation, p)
        if len(common) == 1:
            break
        out = poly_monic(poly_exact_div(out, common, p), p)
    return out


def serialize(poly: Polynomial) -> list[list[int]]:
    return [[real, imag] for real, imag in poly]


@app.function(cpu=0.25, memory=128, timeout=60)
def compute_packet(p: int, zeta_exponent: int) -> dict[str, object]:
    assert p % 8 == 7
    inverse_two = pow(2, p - 2, p)
    root_inverse_two = pow(inverse_two, (p + 1) // 4, p)
    assert root_inverse_two * root_inverse_two % p == inverse_two
    omega = (root_inverse_two, root_inverse_two)
    assert ff_pow(omega, 4, p) == (p - 1, 0)
    assert ff_pow(omega, 8, p) == (1, 0)
    zeta = ff_pow(omega, zeta_exponent, p)

    polynomial = poly_monic([((value % p), 0) for value in F_COEFFICIENTS], p)
    norm_remainder = poly_pow_x(p + 1, polynomial, p)
    norm_remainder[0] = ff_sub(norm_remainder[0], zeta, p)
    raw_gcd = poly_gcd(polynomial, norm_remainder, p)

    x_poly = [(0, 0), (1, 0)]
    x_plus_one = [(1, 0), (1, 0)]
    denominator = [((18 % p), 0), (1, 0), ((-1) % p, 0)]
    saturation = poly_mul(poly_mul(x_poly, x_plus_one, p), denominator, p)
    live_gcd = saturate(raw_gcd, saturation, p)

    assert poly_mod(polynomial, raw_gcd, p) == [(0, 0)]
    assert poly_mod(norm_remainder, raw_gcd, p) == [(0, 0)]
    return {
        "p": p,
        "zeta_exponent": zeta_exponent,
        "zeta": list(zeta),
        "raw_degree": len(raw_gcd) - 1,
        "raw_gcd": serialize(raw_gcd),
        "live_degree": len(live_gcd) - 1,
        "live_gcd": serialize(live_gcd),
    }


def write_partial(rows: list[dict[str, object]]) -> None:
    rows.sort(key=lambda row: (int(row["p"]), int(row["zeta_exponent"])))
    packet = {
        "schema": "l1-h7-order-one-quadratic-two-pair-gcd-v1",
        "complete": len(rows) == 32,
        "all_live_unit": len(rows) == 32 and all(int(row["live_degree"]) == 0 for row in rows),
        "completed_packets": len(rows),
        "expected_packets": 32,
        "rows": rows,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main() -> None:
    rows: list[dict[str, object]] = []
    if RESULT.exists():
        previous = json.loads(RESULT.read_text())
        rows = list(previous.get("rows", []))
    completed = {(int(row["p"]), int(row["zeta_exponent"])) for row in rows}
    tasks = [(p, exponent) for p in PRIMES for exponent in range(8) if (p, exponent) not in completed]
    if tasks:
        primes = [task[0] for task in tasks]
        exponents = [task[1] for task in tasks]
        for row in compute_packet.map(primes, exponents):
            rows.append(row)
            write_partial(rows)
            print("L1_H7_Q2_PAIR_PARTIAL " + json.dumps(row, sort_keys=True))
    write_partial(rows)
    print(f"L1_H7_Q2_PAIR_DONE completed={len(rows)} result={RESULT}")
