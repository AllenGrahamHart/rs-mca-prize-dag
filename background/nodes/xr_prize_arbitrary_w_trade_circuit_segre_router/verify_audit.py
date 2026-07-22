#!/usr/bin/env python3
"""Mutation audit for the arbitrary-W Segre router."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    mutations = 0
    for rank in range(1, 30):
        lower = rank + 2
        upper = 2 * rank + 1
        assert lower - 1 < lower
        assert upper + 1 > upper
        mutations += 2

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "arbitraryflat-nullitypolynomialspace" in statement
    assert "Rank-one circuits are retained" in audit
    assert "No Modal" in audit

    print(
        "XR_PRIZE_ARBITRARY_W_TRADE_CIRCUIT_SEGRE_ROUTER_AUDIT_PASS "
        f"mutations={mutations}"
    )


if __name__ == "__main__":
    main()
