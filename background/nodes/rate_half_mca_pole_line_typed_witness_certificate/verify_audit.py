#!/usr/bin/env python3
"""Independent audit of the typed deployed pole-line witness."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "9423f8ab7c0444205ba7eb9a78fdf16a818d58d1dc0e17c6a81c74a78eb2edc4"


class Reject(ValueError):
    pass


def poly_trim(poly: list[int], p: int) -> list[int]:
    out = [value % p for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return poly_trim(out, p)


def poly_rem(left: list[int], modulus: list[int], p: int) -> list[int]:
    out = poly_trim(left, p)
    inverse = pow(modulus[-1], -1, p)
    while out != [0] and len(out) >= len(modulus):
        coefficient = out[-1] * inverse % p
        shift = len(out) - len(modulus)
        for i, value in enumerate(modulus):
            out[i + shift] = (out[i + shift] - coefficient * value) % p
        out = poly_trim(out, p)
    return out


def frobenius(poly: list[int], modulus: list[int], p: int) -> list[int]:
    result = [1]
    base = poly[:]
    exponent = p
    while exponent:
        if exponent & 1:
            result = poly_rem(poly_mul(result, base, p), modulus, p)
        base = poly_rem(poly_mul(base, base, p), modulus, p)
        exponent >>= 1
    return result


def poly_gcd(left: list[int], right: list[int], modulus_p: int) -> list[int]:
    a, b = poly_trim(left, modulus_p), poly_trim(right, modulus_p)
    while b != [0]:
        remainder = poly_rem(a, b, modulus_p)
        a, b = b, remainder
    inverse = pow(a[-1], -1, modulus_p)
    return poly_trim([inverse * value for value in a], modulus_p)


def check(data: object) -> None:
    if not isinstance(data, dict):
        raise Reject("object")
    field, row, record = data.get("field"), data.get("row"), data.get("record")
    if not all(isinstance(value, dict) for value in (field, row, record)):
        raise Reject("records")
    p = field.get("p")
    modulus = field.get("extension_modulus_low_to_high")
    if p != 2130706433 or modulus != [6, 1, 0, 0, 0, 0, 1]:
        raise Reject("field")

    # Independent Frobenius-chain Rabin test.
    x = [0, 1]
    powers = {0: x}
    current = x
    for index in range(1, 7):
        current = frobenius(current, modulus, p)
        powers[index] = current
    if powers[6] != x:
        raise Reject("degree-six closure")
    for index in (2, 3):
        delta = powers[index][:]
        if len(delta) < 2:
            delta += [0] * (2 - len(delta))
        delta[1] = (delta[1] - 1) % p
        if poly_gcd(modulus, delta, p) != [1]:
            raise Reject("proper factor")

    fixed_row = (2097152, 1048576, 1048577, 1116048, 981104, 1213133211)
    if tuple(row.get(key) for key in ("n", "k", "effective_k", "m", "omega", "zeta")) != fixed_row:
        raise Reject("fixed row")
    n, k, effective_k, m, omega, zeta = fixed_row
    e = record.get("error_prefix_size")
    end = record.get("support_end_exclusive")
    if (
        e != 67473
        or record.get("support_start") != e
        or end != e + m
        or end >= n
        or omega != n - m
        or effective_k != k + 1
        or pow(zeta, n, p) != 1
        or pow(zeta, n // 2, p) != p - 1
        or not m > k + 1
        or n - e <= k + e - 1
        or record.get("guarded_quotient_degree") != -1
        or record.get("d1_code_shift") != e
        or record.get("d1_effective_shift") != e
        or record.get("frozen_owner") != "UNASSIGNED"
    ):
        raise Reject("witness ledger")


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != SHA256:
        raise Reject("contract hash")
    data = json.loads(CONTRACT.read_text())
    check(data)
    controls = []
    for section, key, value in (
        ("row", "m", 1048577),
        ("record", "d1_code_shift", 67472),
        ("record", "frozen_owner", "Q"),
    ):
        altered = copy.deepcopy(data)
        altered[section][key] = value
        try:
            check(altered)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_POLE_LINE_TYPED_WITNESS_CERTIFICATE_AUDIT_PASS "
        f"checks=irreducibility,subgroup,support,root-margins,guard,owner controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
