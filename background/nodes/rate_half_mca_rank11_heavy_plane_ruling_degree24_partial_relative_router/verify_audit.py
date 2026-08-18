#!/usr/bin/env python3
"""Independent audit of the degree-24 partial-relative composition."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "aebdf3c851ac2dbdfe437b569beaeb37a5374abbd7eb658e2ee305bcc6cb4547"


def convolution(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for total in range(len(out)):
        out[total] = sum(
            left[i] * right[total - i]
            for i in range(len(left))
            if 0 <= total - i < len(right)
        ) % p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def value(poly: list[int], x: int, p: int) -> int:
    return sum(coefficient * pow(x, degree, p) for degree, coefficient in enumerate(poly)) % p


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256
    data = json.loads(CONTRACT.read_text())
    row, toy = data["official"], data["toy"]
    dimension, agreement = row["K"], row["m"]
    excess = agreement - dimension
    threshold = 3 * agreement - dimension + 3
    assert (excess, threshold) == (67472, 2299571)
    assert row["common_support_maximum"] == dimension - 3
    assert row["residual_dimension_minimum"] == 3
    for c in (0, 1, 4130, 1045975, dimension - 3):
        kp, mp = dimension - c, agreement - c
        unknowns = excess + 1 + 2 * (mp + 1)
        assert kp >= 3
        assert unknowns == 3 * mp - kp + 3
        assert unknowns + 2 * c == threshold

    p = toy["field"]
    LC, Q = toy["common_locator"], toy["denominator_Q"]
    AC, BC = toy["common_A"], toy["common_B"]
    u, v = toy["residual_u"], toy["residual_v"]
    LR = [1]
    for root in toy["residual_locator_roots"]:
        LR = convolution(LR, [(-root) % p, 1], p)
    c0, c1 = toy["scalar_c0"], toy["scalar_c1"]
    Qu, Qv = convolution(Q, u, p), convolution(Q, v, p)
    size = max(len(Qu), len(LR))
    A1 = [
        ((Qu[i] if i < len(Qu) else 0) + c0 * (LR[i] if i < len(LR) else 0)) % p
        for i in range(size)
    ]
    size = max(len(Qv), len(LR))
    B1 = [
        ((Qv[i] if i < len(Qv) else 0) + c1 * (LR[i] if i < len(LR) else 0)) % p
        for i in range(size)
    ]
    QA, QB = convolution(Q, AC, p), convolution(Q, BC, p)
    LCA, LCB = convolution(LC, A1, p), convolution(LC, B1, p)
    size = max(len(QA), len(LCA))
    A = [
        ((QA[i] if i < len(QA) else 0) + (LCA[i] if i < len(LCA) else 0)) % p
        for i in range(size)
    ]
    size = max(len(QB), len(LCB))
    B = [
        ((QB[i] if i < len(QB) else 0) + (LCB[i] if i < len(LCB) else 0)) % p
        for i in range(size)
    ]
    L = convolution(LC, LR, p)
    for gamma in toy["slopes"]:
        scalar = (c0 + c1 * gamma) % p
        for x in range(p):
            h1 = (value(u, x, p) + gamma * value(v, x, p)) % p
            h = (
                value(AC, x, p)
                + gamma * value(BC, x, p)
                + value(LC, x, p) * h1
            ) % p
            assert (value(Q, x, p) * h + scalar * value(L, x, p)) % p == (
                value(A, x, p) + gamma * value(B, x, p)
            ) % p
    assert len(L) - 1 == toy["m"] and L[-1] == 1
    assert max(len(A), len(B)) - 1 <= toy["m"]
    assert row["slope_degree_minimum"] == row["anchor_records_minimum"] == 24
    proof = Path(__file__).with_name("proof.md").read_text().lower()
    assert "never divide pointwise by `q`" in proof
    assert "first-owned slope labels" in proof
    print(
        "RANK11_RULING_DEG24_PARTIAL_AUDIT_PASS "
        f"chi={threshold} endpoint={dimension - 3} "
        f"toy_profile_degree={max(len(A), len(B)) - 1}"
    )


if __name__ == "__main__":
    main()
