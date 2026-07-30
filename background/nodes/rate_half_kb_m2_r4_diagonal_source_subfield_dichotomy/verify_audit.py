#!/usr/bin/env python3
"""Independent arithmetic audit for the source-subfield router."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def main() -> None:
    contract = (NODE / "claim_contract.md").read_text()
    audit = (NODE / "audit.md").read_text()
    assert "source-line lift" in contract
    assert "not the ambient `V4`" in audit

    # Reciprocal inversion pairs 15 bidegree-(2,4) coefficients.
    involution = {
        (i, j): (2 - i, 4 - j)
        for i in range(3)
        for j in range(5)
    }
    assert all(involution[involution[p]] == p for p in involution)
    traces = sum(involution[p] == p for p in involution)
    assert traces == 1
    assert ((15 + traces) // 2, (15 - traces) // 2) == (8, 7)

    # Two rational quadratic quotients inside a tame V4 cover.
    rows = []
    for genus in (0, 1):
        fixed_rational = 2 * genus + 2
        fixed_third = 2 * genus + 6 - 2 * fixed_rational
        branch_orbits = (
            fixed_rational // 2,
            fixed_rational // 2,
            fixed_third // 2,
        )
        rows.append((genus, fixed_third, branch_orbits))
    assert rows == [(0, 2, (1, 1, 1)), (1, 0, (2, 2, 0))]
    print("RATE_HALF_KB_M2_R4_DIAGONAL_SOURCE_SUBFIELD_DICHOTOMY_AUDIT_PASS")


if __name__ == "__main__":
    main()
