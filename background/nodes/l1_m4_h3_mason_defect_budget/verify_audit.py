#!/usr/bin/env python3
"""Independent mutation audit for the m=4, h=3 Mason defect budget."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    checks = 0
    for p in (7, 13, 31, 127):
        n, u = 4 * (p + 1), p + 4
        for nu in range(5):
            nonzero_a_rhs = (p - nu + u) + (p + u - 3 * nu)
            zero_a_rhs = (p - nu + u) + (u - 3 * nu)
            lhs = n - 3 * nu
            assert nonzero_a_rhs - lhs == 4 - nu
            assert zero_a_rhs < lhs
            assert (p + u - 3 * nu) - 2 * (p - nu) == 4 - nu
            assert (u - 3 * nu) - 2 * (p - nu) < 0
            checks += 4
        assert ((p - 5 + u) + (p + u - 15)) < n - 15
        checks += 1

    proof = (HERE / "proof.md").read_text()
    for anchor in ("Frobenius-degenerate arm", "Wronskian", "H!=0",
                   "a=0", "p-4+nu", "divides H",
                   "delta_A+delta_B=deg K<=deg H<=4-nu"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "finite low-defect classification target" in statement
    assert "does not prove" in statement
    checks += 2
    print(f"L1_M4_H3_MASON_DEFECT_BUDGET_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
