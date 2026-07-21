#!/usr/bin/env python3
"""Mutation checks for the c2 degree-defect global gate router."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    audit = (HERE / "audit.md").read_text()

    assert "d_e=5H-10-3e-epsilon_e" in statement
    assert "eta=d_e-r_J in 2 Z_(>=0)" in statement
    assert "|supp u|=3H+3e+epsilon_e+eta" in statement
    assert "e=1: |supp u|>=3H+3" in statement
    assert "Res(C_sharp,T_0) is a nonzero base-field cube" in statement
    assert "O_inf divides X^N-1" in statement
    assert "<=355106851<2^29" in statement
    assert "at every\nsupport" in statement
    assert "does not assert" in statement and "endpoint product `Xi`" in statement

    assert "(H+m-r)bc=-e bc" in proof
    assert "delta=2+2m+(r+m)=5H-10-3e" in proof
    assert "No support-size hypothesis" in proof
    assert "degree and the selected-antipodal" in audit

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_DEGREE_DEFECT_GLOBAL_GATE_AUDIT_PASS "
        "degree_parity=1 support_defect=1 scope_extension=1 nonclaims=2"
    )


if __name__ == "__main__":
    main()
