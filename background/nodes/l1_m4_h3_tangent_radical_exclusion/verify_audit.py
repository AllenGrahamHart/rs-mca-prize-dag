#!/usr/bin/env python3
"""Independent audit of the tangent radical degree comparison."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    checks = 0
    expected = {
        (1, 0): False, (1, 1): False, (1, 2): True,
        (2, 0): False, (2, 1): True,
        (3, 0): False,
    }
    for p in (7, 13, 31, 127):
        for (nu, eta), possible in expected.items():
            radical_upper = nu + eta
            derivative_factor = p + eta - 4
            radical_lower = p - derivative_factor
            assert (radical_lower <= radical_upper) is possible
            assert possible is (nu + 2 * eta >= 4)
            checks += 2

    proof = (HERE / "proof.md").read_text()
    for anchor in ("bD(0)=-alpha", "g'(y_0)", "P(x)=0",
                   "p-deg rad(T)", "nu+2eta>=4"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "clean `nu=3` case is empty" in statement
    assert "separate treatment" in statement
    checks += 2
    print(f"L1_M4_H3_TANGENT_RADICAL_EXCLUSION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
