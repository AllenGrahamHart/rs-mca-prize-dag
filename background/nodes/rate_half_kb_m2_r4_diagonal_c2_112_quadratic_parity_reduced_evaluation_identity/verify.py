#!/usr/bin/env python3
"""Check the parity-reduced evaluation identity on formal basis terms."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


Monomial = tuple[int, int, int]
Polynomial = dict[Monomial, int]


def add(*values: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for value in values:
        for monomial, coefficient in value.items():
            result[monomial] = result.get(monomial, 0) + coefficient
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def scale(value: Polynomial, coefficient: int) -> Polynomial:
    return {monomial: coefficient * current for monomial, current in value.items() if coefficient * current}


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for (ul, vl, zl), cl in left.items():
        for (ur, vr, zr), cr in right.items():
            monomial = (ul + ur, vl + vr, zl + zr)
            result[monomial] = result.get(monomial, 0) + cl * cr
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def term(u: int, v: int, z: int, coefficient: int = 1) -> Polynomial:
    return {} if coefficient == 0 else {(u, v, z): coefficient}


R = add(term(2, 0, 0), term(0, 1, 1, -1))
HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / (
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_"
    "degree12_leading_branch_decomposition/modal_degree12_parity_metrics_output.json"
)
OUTPUT_SHA256 = "37e33746c9268cb70ff68d6e08806fb817d0c2f79c3672dcdaf87ea3304b8c46"


def quotient_term(degree: int, index: int, odd_sign: int = -1) -> Polynomial:
    half = index // 2
    if half == 0:
        return {}
    geometric = add(*(
        term(2 * (half - 1 - power), power, power)
        for power in range(half)
    ))
    if index % 2 == 0:
        return multiply(term(0, degree - index, 0), geometric)
    return scale(
        multiply(term(1, degree - index, 0), geometric),
        odd_sign,
    )


def identity_holds(degree: int, index: int, odd_sign: int = -1) -> bool:
    direct_sign = -1 if index % 2 else 1
    direct = term(index, degree - index, 0, direct_sign)
    half = index // 2
    if index % 2 == 0:
        reduced = term(0, degree - half, half)
    else:
        reduced = term(1, degree - half - 1, half, odd_sign)
    difference = add(direct, scale(reduced, -1))
    return difference == multiply(R, quotient_term(degree, index, odd_sign))


def main() -> None:
    cases = [(degree, index) for degree in range(13) for index in range(degree + 1)]
    assert all(identity_holds(degree, index) for degree, index in cases)
    assert any(not identity_holds(degree, index, 1) for degree, index in cases if index % 2)
    raw = OUTPUT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == OUTPUT_SHA256
    payload = json.loads(raw)
    assert payload["counts"] == {"FAIL": 0, "PASS": 1, "REMOTE_ERROR": 0, "TIMEOUT": 0}
    row = payload["results"][0]
    assert row["status"] == "PASS" and row["cell"] == "F04-R02"
    compiled = next(record for record in row["records"] if record["phase"] == "PARITY_COMPILED")
    direct = [(value["degree"], value["terms"], value["sha256"]) for value in compiled["direct"]]
    parity = [(value["degree"], value["terms"], value["sha256"]) for value in compiled["parity"]]
    assert direct == [
        (99, 52336, "2cdede128b75fc902dc70843f51f7dcfe34c0d4ef045ae42f131e41cfafd0efa"),
        (99, 49949, "76181dfa17c9e16d1905e34399bb517afbfc3b5b646ec263a702cd298b794da3"),
    ]
    assert parity == [
        (98, 52257, "d0c3bfb298538275593184cbd2afee494014bf2417f0a3e0bbae884f57b0e22d"),
        (97, 49848, "3fd6a65e18b4ad8a53576a0b0b3f280d190d73330825376888e1fba0ea62dffa"),
    ]
    terminal = next(record for record in row["records"] if record["phase"] == "DONE")
    assert terminal["terminal"] == "DEGREE12_PARITY_REPRESENTATIVES_COMPILED"
    print(f"KB_C2_112_PARITY_REDUCED_EVALUATION_PASS cases={len(cases)} literal_metrics=1 mutations=1/1")


if __name__ == "__main__":
    main()
