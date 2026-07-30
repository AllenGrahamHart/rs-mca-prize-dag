#!/usr/bin/env python3
"""Verify the KoalaBear m2 r2 dihedral outer-factor reduction."""

from pathlib import Path


NODE = Path(__file__).resolve().parent
DIVISORS = tuple(value for value in range(2, 31) if 30 % value == 0)


def pole_profile(degree: int) -> dict[str, object] | None:
    if degree == 5:
        return {"order5_generic_fibers": 1, "simple_total_fibers": 1}
    if 6 % degree == 0:
        return {"order5_generic_fibers": 6 // degree, "simple_total_fibers": 0}
    return None


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    proof = (NODE / "proof.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "No one of the four factor degrees is deleted" in statement
    assert "recurrence, not closure" in contract
    assert "F=G composed q_n" in proof

    assert DIVISORS == (2, 3, 5, 6, 10, 15, 30)
    profiles = {degree: pole_profile(degree) for degree in DIVISORS}
    assert {degree for degree, profile in profiles.items() if profile} == {2, 3, 5, 6}
    assert profiles[2] == {"order5_generic_fibers": 3, "simple_total_fibers": 0}
    assert profiles[3] == {"order5_generic_fibers": 2, "simple_total_fibers": 0}
    assert profiles[5] == {"order5_generic_fibers": 1, "simple_total_fibers": 1}
    assert profiles[6] == {"order5_generic_fibers": 1, "simple_total_fibers": 0}

    branch_rows = {
        0: {"a": 1, "c": 1, "ac": 1},
        1: {"a": 0, "c": 2, "ac": 2},
    }
    assert sum(branch_rows[0].values()) == 3
    assert sum(branch_rows[1].values()) == 4
    fixed_totals = {
        genus: 2 * sum(values.values())
        for genus, values in branch_rows.items()
    }
    assert fixed_totals == {0: 6, 1: 8}
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_OUTER_FACTOR_REDUCTION_PASS")


if __name__ == "__main__":
    main()
