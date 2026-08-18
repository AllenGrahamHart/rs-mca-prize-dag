#!/usr/bin/env python3
"""Independent audit for heavy-plane Segre shortening/transversality."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
d = json.loads((HERE / "source_contract.json").read_text())


def product(values: range) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def alternate_cap(s: int, theta: int) -> int:
    r, gap, redundancy = 4, d["agreement_gap"], d["redundancy"]
    n, m = redundancy + s, gap + s
    first = Fraction(
        product(range(n - r, n + 1)),
        m * theta * product(range(gap + 1, gap + r)),
    )
    second = Fraction(
        product(range(redundancy, redundancy + r + 1)),
        theta * product(range(gap + 1, gap + r + 1)),
    )
    return max(first.numerator // first.denominator, second.numerator // second.denominator)


assert d["locator_min"] == 37733
assert d["locator_max"] == 1048569
assert d["shortened_k_min"] == 4
assert d["shortened_k_max"] == 1010840
assert 40 * d["rank_two_cap"] == 9945763960 < d["mass"]
assert 41 * d["rank_two_cap"] >= d["mass"]

turn = d["turning_dimension"]
sign = lambda s: 4 * s + 5 * d["agreement_gap"] - d["redundancy"] + 4
assert sign(turn) == 0
assert sign(turn - 1) < 0 < sign(turn + 1)

for theta, expected in (
    (d["last_margin"], d["last_margin_uniform_cap"]),
    (d["first_paying_margin"], d["first_paying_uniform_cap"]),
):
    endpoint_caps = [
        alternate_cap(d["shortened_k_min"], theta),
        alternate_cap(d["shortened_k_max"], theta),
    ]
    assert max(endpoint_caps) == expected

assert d["last_margin_uniform_cap"] >= d["mass"]
assert d["first_paying_uniform_cap"] < d["mass"]
proof = (HERE / "proof.md").read_text().lower()
assert "tensor product" in proof
assert "first-match" in proof
audit = (HERE / "audit.md").read_text().lower()
assert "deployed evaluation field" in audit
assert "not monotone" in audit

print(
    "RANK11_HEAVY_SEGRE_AUDIT_PASS "
    f"turn={turn} used={d['minimum_used_factors']} exceptions={d['last_margin']}"
)
