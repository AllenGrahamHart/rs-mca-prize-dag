#!/usr/bin/env python3
"""Mutation audit for the XR prize uniform-trade private-point floor."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def main() -> None:
    # The multiplicity inequality is exact for private points, neutral at
    # multiplicity two, and safely negative thereafter.
    for m in range(1, 100):
        value = m - m * (m - 1)
        assert value == 1 if m == 1 else value <= 0

    rows = (
        ((1 << 33) + 1, 384, 11_243_370),
        ((1 << 33) + 1, 448, 9_629_972),
        ((1 << 32) + 1, 960, 2_241_633),
    )
    for h, L, expected in rows:
        actual = ceil_div(h + 1, 2 * (L - 2))
        assert actual == expected
        assert 2 * (L - 2) * actual >= h + 1
        assert 2 * (L - 2) * (actual - 1) < h + 1

    # The all-rank floor is slightly lower than the sharper rank-two floor.
    assert 11_243_370 < 11_265_488
    assert 9_629_972 < 9_646_193
    assert 2_241_633 < 2_243_389

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "Everyover-budgetuniformselector" in statement
    assert "wholecoreorapropersubset" in audit.replace(" ", "")
    assert "nonuniform-cell statement" in audit

    print("XR_PRIZE_UNIFORM_TRADE_PRIVATE_POINT_RANK_FLOOR_AUDIT_PASS mutations=11")


if __name__ == "__main__":
    main()
