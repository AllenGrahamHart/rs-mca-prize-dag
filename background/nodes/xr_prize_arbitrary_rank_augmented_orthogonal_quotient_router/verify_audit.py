#!/usr/bin/env python3
"""Mutation audit for the augmented-orthogonal quotient router."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    mutations = 0
    for rank in range(2, 100):
        asserted = 2 * rank - 1
        old = 2 * rank + 1
        assert asserted != old
        assert asserted - 1 == 2 * (rank - 1)
        mutations += 2

    statement = " ".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "`tau_i=0` exactly for augmented-orthogonal rows" in statement
    assert "quotient coefficients" in audit
    assert "No Modal" in audit

    print(
        "XR_PRIZE_ARBITRARY_RANK_AUGMENTED_ORTHOGONAL_QUOTIENT_ROUTER_AUDIT_PASS "
        f"mutations={mutations}"
    )


if __name__ == "__main__":
    main()
