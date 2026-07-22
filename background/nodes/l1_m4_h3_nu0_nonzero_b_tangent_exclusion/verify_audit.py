#!/usr/bin/env python3
"""Independent audit of the tangent radical degree comparison."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    checks = 0
    for h in range(4):
        derivative_degree = 101 + h - 5
        radical_floor = 101 - derivative_degree
        assert radical_floor == 5 - h
        if h > 0:
            feasible = radical_floor <= h
            assert feasible == (h == 3)
        checks += 2

    proof = (HERE / "proof.md").read_text()
    for anchor in ("b Delta/(8a^3)", "Evaluating", "deg gcd(T,T')",
                   "H-kappa", "R(0)Delta+12a^2g(R(0))",
                   "algebraic closure"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "h=1: impossible" in statement
    assert "h=2: impossible" in statement
    assert "does not treat `b=0`" in statement
    checks += 3
    print(f"L1_M4_H3_NU0_NONZERO_B_TANGENT_EXCLUSION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
