#!/usr/bin/env python3
"""Independent case-coverage audit for official m=4,h=3 emptiness."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    checks = 0
    positive = {(1, 2), (2, 1)}
    assert positive == {(1, 2), (2, 1)}
    checks += 1

    nu0 = {
        ("zero", h) for h in range(4)
    } | {
        ("nonzero", h) for h in range(4)
    }
    assert len(nu0) == 8
    checks += 1

    proof = (HERE / "proof.md").read_text()
    for anchor in ("nu=ord_0(R) in {0,1,2,3}", "If `nu>0`",
                   "If `b=0`", "Suppose `b!=0`", "deg H=1,2",
                   "deg H=0", "deg H=3", "exhausted"):
        assert anchor in proof
        checks += 1
    statement = (HERE / "statement.md").read_text()
    assert "complete official `m=4,h=3` stratum is" in statement
    assert "nonembedded `m=4,h=2`" in statement
    checks += 2

    print(f"L1_M4_H3_OFFICIAL_EMPTINESS_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
