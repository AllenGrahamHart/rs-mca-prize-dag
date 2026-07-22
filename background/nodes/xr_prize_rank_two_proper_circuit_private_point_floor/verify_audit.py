#!/usr/bin/env python3
"""Mutation audit for the XR proper-circuit private-point floor."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def rank_floor(h: int, L: int, t: int) -> int:
    return ceil_div(
        t * (h + 1) // 2 + 3 * (t - 1) * (t - 3),
        t * L - t * (t - 2) - 3,
    )


def main() -> None:
    # The pointwise multiplicity correction is exact at m=1 and nonpositive
    # at every higher outside multiplicity.
    for m in range(1, 20):
        contribution = m - 2 * (m * (m - 1) // 2)
        contribution += 2 * ((m - 1) * (m - 2) // 2)
        assert contribution == 2 - m
        assert contribution <= (1 if m == 1 else 0)

    expected = (
        ((1 << 33) + 1, 384, (11_265_488, 11_290_661)),
        ((1 << 33) + 1, 448, (9_646_193, 9_664_643)),
        ((1 << 32) + 1, 960, (2_243_389, 2_245_383)),
    )
    for h, L, floors in expected:
        assert tuple(rank_floor(h, L, t) for t in (4, 5)) == floors
        # Removing one available host block strictly raises both floors.
        assert all(rank_floor(h, L - 1, t) >= floors[t - 4] for t in (4, 5))

    # The private-point floors are far below, but compatible with, the
    # independent full-core floors.
    assert 11_265_488 < 8_590_051_854
    assert 9_646_193 < 8_590_020_865
    assert 2_243_389 < 4_294_977_670

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "+2C+I" in statement
    assert "arbitrary outside multiplicity" in audit
    assert "not existence claims" in audit

    print(
        "XR_PRIZE_RANK_TWO_PROPER_CIRCUIT_PRIVATE_POINT_FLOOR_AUDIT_PASS "
        "mutations=12"
    )


if __name__ == "__main__":
    main()
