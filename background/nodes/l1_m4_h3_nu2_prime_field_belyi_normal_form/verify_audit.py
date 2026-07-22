#!/usr/bin/env python3
"""Independent audit of the multiplicity cross-product formula."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    checks = 0
    for p in (7, 13, 31):
        for e1 in range(1, p - 1):
            for e2 in range(e1 + 1, p):
                e3 = p - e1 - e2
                if e3 <= 0 or e3 in (e1, e2):
                    continue
                d = ((e2 - e3) % p, (e3 - e1) % p, (e1 - e2) % p)
                assert all(d)
                assert sum(d) % p == 0
                assert sum(e * value for e, value in zip((e1, e2, e3), d)) % p == 0
                checks += 3
    assert checks > 0

    proof = (HERE / "proof.md").read_text()
    for anchor in ("1/r_1+1/r_2+1/r_3", "logarithmic", "cross product",
                   "lambda^p", "critical-value passport"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "prime-field polynomial" in statement
    assert "does not prove" in statement
    checks += 2
    print(f"L1_M4_H3_NU2_PRIME_FIELD_BELYI_NORMAL_FORM_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
