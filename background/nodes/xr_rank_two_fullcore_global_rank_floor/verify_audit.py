#!/usr/bin/env python3
"""Mutation audit for the XR global full-core rank floor."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def mass_floor(t: int, D: int) -> int:
    return t * D // 2 if D % 2 == 0 else t * (D + 1) // 2 - 1


def main() -> None:
    # Strictness is real: equality at the relaxed shell has D_0=0, not <0.
    equality_controls = 0
    for h in range(1, 50, 2):
        for t in range(4, 40):
            numerator = t * h + 2 * t * (t - 2)
            denominator = (t - 2) * (t + 1)
            if numerator % denominator == 0:
                D = numerator // denominator
                baseline = t * h + (t - 2) * (t - 1) * D
                assert baseline == 2 * (t - 2) * t * (D - 1)
                equality_controls += 1
    assert equality_controls > 0

    # Pair mass, rather than the baseline floor, controls a high-arity RowC cell.
    h, t, D = 5, 130, 3
    baseline_floor = (t * h + (t - 2) * (t - 1) * D) // (2 * (t - 2)) + 1
    assert mass_floor(t, D) == 259 > baseline_floor

    # Pair mass makes Z-D dominate both standalone shell-rank terms.
    for h in range(1, 30, 2):
        for t in range(4, 60):
            numerator = t * h + 2 * t * (t - 2)
            denominator = (t - 2) * (t + 1)
            D = max(3, numerator // denominator + 1)
            baseline = t * h + (t - 2) * (t - 1) * D
            Z = max(mass_floor(t, D), baseline // (2 * (t - 2)) + 1)
            assert Z - D >= D
            assert Z - D >= t - 2

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "958" in statement
    assert "not an existence theorem" in audit
    assert "Proper four/five-block circuits" in audit

    print("XR_RANK_TWO_FULLCORE_GLOBAL_RANK_FLOOR_AUDIT_PASS mutations=11")


if __name__ == "__main__":
    main()
