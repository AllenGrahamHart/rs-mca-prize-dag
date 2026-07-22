#!/usr/bin/env python3
"""Mutation audit for the XR quotient safe-sum fence."""

from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PRIZE_BSTAR = 317494674775468773183020924238786383963
ROWS = (
    ("RowC-1/4", 1 << 10, 1 << 8, 261, 1 << 3, 261, 1 << 122),
    ("RowC-1/8", 1 << 10, 1 << 7, 133, 1 << 3, 135, 1 << 122),
    ("RowC-1/16", 1 << 10, 1 << 6, 67, 1 << 4, 79, 1 << 122),
    (
        "prize-1/4",
        1 << 41,
        1 << 39,
        558345748481,
        1 << 34,
        558345748481,
        PRIZE_BSTAR,
    ),
    (
        "prize-1/8",
        1 << 41,
        1 << 38,
        283467841537,
        1 << 34,
        283467841537,
        PRIZE_BSTAR,
    ),
    (
        "prize-1/16",
        1 << 41,
        1 << 37,
        141733920769,
        1 << 33,
        141733920769,
        PRIZE_BSTAR,
    ),
)


def main() -> None:
    rowc = ROWS[:3]
    exact = []
    for _, n, _, _, fiber, support, threshold in rowc:
        profile, remainder = divmod(support, fiber)
        value = comb(n // fiber, profile) * comb(
            n - fiber * profile, remainder
        )
        exact.append(value)
        assert value > threshold

    no_remainder_choice = [
        comb(n // fiber, support // fiber)
        for _, n, _, _, fiber, support, _ in ROWS
    ]
    assert not all(
        value > row[-1] for value, row in zip(no_remainder_choice, ROWS)
    )

    old_midpoint = [n // 2 + 1 for _, n, *_ in ROWS]
    assert all(
        midpoint - k >= fiber
        for midpoint, (_, _, k, _, fiber, _, _) in zip(old_midpoint, ROWS)
    )

    assert all(
        support - k >= fiber // 2
        for _, _, k, _, fiber, support, _ in ROWS
    )

    prize_ambients = [n - k for _, n, k, *_ in ROWS[3:]]
    assert all(comb(ambient, 3) <= PRIZE_BSTAR for ambient in prize_ambients)
    assert all(comb(ambient, 4) > PRIZE_BSTAR for ambient in prize_ambients)

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "activeonlywhen`c>B-k`" in statement
    assert "`(c,B)=(8,261),(8,135),(16,79)`" in statement
    assert "doesnotassertthattheactualquotientslopeunion" in statement
    assert "upper bound larger than the budget" in audit
    assert "midpoint cell `B=n/2+1` is inactive" in audit
    assert "no large official-row support integer is materialized" in audit

    print("XR_AGREEMENT_RAISE_QUOTIENT_SAFE_SUM_FENCE_AUDIT_PASS mutations=8")


if __name__ == "__main__":
    main()
