#!/usr/bin/env python3
"""Independent audit for the heavy-plane Segre ruling router."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
d = json.loads((HERE / "source_contract.json").read_text())


def choose(n: int, k: int) -> int:
    value = 1
    for i in range(1, k + 1):
        value = value * (n - k + i) // i
    return value


def product(values: range) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def alternate_support_cap(k: int, rank: int) -> int:
    n = d["redundancy"] + k
    m = d["agreement_gap"] + k
    theta = d["margin"]
    if rank == 0:
        return n // theta
    first = Fraction(
        product(range(n - rank, n + 1)),
        m * theta * product(range(d["agreement_gap"] + 1, d["agreement_gap"] + rank)),
    )
    second = Fraction(
        product(range(d["redundancy"], d["redundancy"] + rank + 1)),
        theta
        * product(
            range(d["agreement_gap"] + 1, d["agreement_gap"] + rank + 1)
        ),
    )
    return max(
        first.numerator // first.denominator,
        second.numerator // second.denominator,
    )


endpoints = (d["shortened_k_min"], d["shortened_k_max"])
independent_caps = [
    max(alternate_support_cap(k, rank) for k in endpoints) for rank in range(5)
]
assert independent_caps == d["high_caps_by_rank"]


q4 = choose(d["redundancy"] + 4, 4) // choose(
    d["agreement_gap"] - d["margin"] + 5, 4
)
q2 = choose(d["redundancy"] + 2, 2) // choose(
    d["agreement_gap"] - d["margin"] + 3, 2
)
assert q4 == 58361 == d["rank_four_pair_types"]
assert q2 == 241 == d["rank_two_pair_types"]

high = max(independent_caps)
low = d["mass"] - high
ruling = low - 2 * q4
assert high == d["high_cap"]
assert low == d["low_mass"]
assert ruling == d["ruling_mass"]

outside = d["redundancy"] - d["agreement_gap"] + d["margin"] - 1
per_plane = outside * q2
assert outside == 981115 == d["fixed_pair_multiplicity"]
assert per_plane == 236448715 == d["fixed_ruling_cap"]
assert 2 * per_plane < ruling <= 3 * per_plane

zero = q4 - 1 + outside
nonzero = ruling - zero
assert zero == d["zero_correction_cap"]
assert nonzero == d["nonzero_ruling_mass"]
assert Fraction(nonzero, 2) <= d["orientation_mass"]
assert d["orientation_mass"] > per_plane

# Independent 2 x 2 determinant coefficient checks for both ruling types.
def determinant_coefficients(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, int, int]:
    a00, a01, a10, a11 = a
    b00, b01, b10, b11 = b
    return (
        a00 * a11 - a01 * a10,
        a00 * b11 + b00 * a11 - a01 * b10 - b01 * a10,
        b00 * b11 - b01 * b10,
    )


# Common left factor e_0 and common right factor e_0.
assert determinant_coefficients((1, 0, 0, 0), (0, 1, 0, 0)) == (0, 0, 0)
assert determinant_coefficients((1, 0, 0, 0), (0, 0, 1, 0)) == (0, 0, 0)
# Opposite corners give a genuinely quadratic intersection.
assert determinant_coefficients((1, 0, 0, 0), (0, 0, 0, 1)) == (0, 1, 0)

proof = (HERE / "proof.md").read_text().lower()
assert "det(a+zb)" in proof
assert "common left factor" in proof
assert "first-owned" in (HERE / "claim_contract.md").read_text().lower()

print(
    "RANK11_SEGRE_RULING_AUDIT_PASS "
    f"q4={q4} q2={q2} ruling={ruling} nonzero={nonzero}"
)
