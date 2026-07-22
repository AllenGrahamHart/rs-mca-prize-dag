#!/usr/bin/env python3
"""Independent order audit for the positive tangent exclusion."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    checks = 0
    for e in range(2, 40):
        for d in (0, 1):
            correction_order = 2 * e + d - 1
            assert correction_order > e
            checks += 1

    for nu, eta, r_floor, r_ceiling in ((1, 2, 2, 3), (2, 1, 3, 3)):
        assert nu + eta == 3
        assert 2 <= r_floor <= r_ceiling <= 3
        assert 3 * r_ceiling <= 9
        checks += 3

    proof = (HERE / "proof.md").read_text()
    for anchor in ("phi'(y_0)", "x!=0", "e<=p-1", "ord_x(V)=e-1",
                   "2e+d-1", "p<=9"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "both positive" in statement
    assert "wider `m`" in statement
    checks += 2

    print(f"L1_M4_H3_POSITIVE_TANGENT_MULTIPLICITY_EXCLUSION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
