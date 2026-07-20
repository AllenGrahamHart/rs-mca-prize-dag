#!/usr/bin/env python3
"""Exact v13.2 discrete subfield-census normalization replay."""

import json
from math import comb, log2
from pathlib import Path

N = 2**21
K = 2**20
KB_P = 2**31 - 2**24 + 1
M31_P = 2**31 - 1
KB_M = 1_116_046
M31_M = 1_116_022


def ceil_div(a, b):
    return (a + b - 1) // b


def log2_int(value):
    bits = value.bit_length()
    if bits <= 64:
        return log2(value)
    top = value >> (bits - 64)
    return bits - 64 + log2(top)


def retreat_binomial(value, upper, start, target):
    r = start
    while r > target:
        value = value * r // (upper - r + 1)
        r -= 1
    return value


def offset_rows(m, base_binomial, p):
    big = base_binomial
    spray = 1
    rows = []
    for offset in range(4):
        w_prime = m - K
        d1 = w_prime + 1 + offset
        mp = K - 1 + d1
        assert K <= m
        assert 2 * w_prime <= N - K
        assert w_prime + 1 <= d1 <= (N - K + 1) // 2
        assert mp + d1 <= N
        exponent = m - K + offset
        denominator = p**exponent
        prefix_floor = ceil_div(big, denominator)
        discrete = spray * prefix_floor
        wrong_order = ceil_div(spray * big, denominator)
        rows.append((prefix_floor, discrete, wrong_order, big, denominator, spray))
        assert mp == m + offset
        big = big * (N - mp) // (mp + 1)
        spray = spray * (mp + 1) // (offset + 1)
    return rows


kb_base = comb(N, KB_M)
m31_base = retreat_binomial(kb_base, N, KB_M, M31_M)

kb = offset_rows(KB_M, kb_base, KB_P)
m31 = offset_rows(M31_M, m31_base, M31_P)

assert [row[0] for row in kb] == [
    157_702_518_233_425_975_347,
    65_065_153_468,
    27,
    1,
]
assert [row[0] for row in m31] == [
    4_870_025_984_688_527,
    1_993_678,
    1,
    1,
]

assert [round(log2_int(row[1]), 4) for row in kb] == [
    67.0958,
    56.0111,
    43.9348,
    57.6849,
]
assert [round(log2_int(row[1]), 4) for row in m31] == [
    52.1129,
    41.0169,
    39.1799,
    57.6848,
]

for row in kb + m31:
    _, discrete, _, numerator, denominator, spray = row
    assert discrete * denominator <= spray * (numerator + denominator)

# These cells detect the v13 raw ceiling-after-product mutation.
for rows, offsets in ((kb, (3,)), (m31, (2, 3))):
    for offset in offsets:
        prefix_floor, discrete, wrong_order, numerator, denominator, spray = rows[offset]
        assert numerator < denominator
        assert prefix_floor == 1
        assert discrete == spray
        assert wrong_order != discrete

root = Path(__file__).resolve().parents[3]
statement = (root / "background/nodes/v13_2_discrete_subfield_census_guard/statement.md").read_text()
correspondence = (root / "notes/correspondence/MB_VS_F1_LEDGER.md").read_text()
dag = json.loads((root / "dag.json").read_text())
f1_tower = next(node for node in dag["nodes"] if node["id"] == "f1_case_tower")
assert "C(m',m) ceil(A_B(d1))" in statement
assert "depth one in practice\" conclusion is retracted" in correspondence
assert "31.3" in correspondence and "superseded" in correspondence
assert "active unsafe list agreement `1116046`" in correspondence
assert "next rung `1116047`" in correspondence
assert "not thereby certified safe" in correspondence
assert f1_tower["status"] == "PROVED"
assert "V13.2 CENSUS CORRECTION" in f1_tower["statement"]
assert "ONE level deep in practice" not in f1_tower["statement"]

print("V13_2_DISCRETE_SUBFIELD_CENSUS_GUARD_PASS")
