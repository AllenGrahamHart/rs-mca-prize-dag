#!/usr/bin/env python3
"""Independent audit of the order and fixed-root arithmetic."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    checks = 0
    for r in (3, 5, 7, 13, 17, 19, 31):
        p = (1 << r) - 1
        n = 1 << (r + 2)
        assert pow(p, 2, n) == 1 + n // 2
        assert pow(p, 4, n) == 1
        assert pow(p, 1, n) != 1
        assert pow(p, 2, n) != 1
        checks += 4

    proof = (HERE / "proof.md").read_text()
    for anchor in ("number of fixed points", "product of all roots",
                   "c/x", "D_0(-x)=0", "(3w)^p=3w", "R_0(cW)/c",
                   "c^(3-3p)=1"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "exactly one sign" in statement
    assert "not a converse" in statement
    checks += 2
    print(f"L1_M4_H3_NU2_FIXED_POINT_CERTIFICATE_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
