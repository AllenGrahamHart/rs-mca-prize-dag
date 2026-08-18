#!/usr/bin/env python3
"""Independent audit for rank-two-triple shortening/transversality."""

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


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def alternate_cap(rank: int, theta: int) -> int:
    n, k, m = d["n_short"], d["k_short"], d["m_short"]
    w = m - k
    num1 = product(range(n - rank, n + 1))
    den1 = m * theta * product(range(w + 1, w + rank))
    num2 = product(range(n - k, n - k + rank + 1))
    den2 = theta * product(range(w + 1, w + rank + 1))
    return max(floor_fraction(Fraction(num1, den1)), floor_fraction(Fraction(num2, den2)))


assert d["rank_four_cap"] == 63397365764 < d["mass"]
assert d["residual_roots_before"] - 3 == d["residual_roots_after"]
for rank, last, first, last_cap, first_cap in (
    (
        5,
        d["rank_five_last_margin"],
        d["rank_five_first_paying_margin"],
        d["rank_five_last_cap"],
        d["rank_five_first_paying_cap"],
    ),
    (
        6,
        d["rank_six_last_margin"],
        d["rank_six_first_paying_margin"],
        d["rank_six_last_cap"],
        d["rank_six_first_paying_cap"],
    ),
):
    assert first == last + 1
    assert alternate_cap(rank, last) == last_cap >= d["mass"]
    assert alternate_cap(rank, first) == first_cap < d["mass"]

proof = (HERE / "proof.md").read_text().lower()
assert "strictly below retained" not in proof
assert "first-owned" in proof
audit = (HERE / "audit.md").read_text().lower()
assert "recomputed" in audit
assert "equality would not suffice" in audit

print(
    "RANK11_RANK2_SHORT_AUDIT_PASS "
    f"rank5={d['rank_five_last_margin']} rank6={d['rank_six_last_margin']}"
)
