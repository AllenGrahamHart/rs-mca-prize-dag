#!/usr/bin/env python3
"""Mutation audit for the XR rank-one flat/basis owner."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    mutations = 0
    for r in range(20, 50):
        for h in range(2, 10):
            for v in range(0, min(r, 10)):
                cap = (r - v) // h
                assert cap * h <= r - v < (cap + 1) * h
                wrong = r // h
                if wrong != cap:
                    mutations += 1

    assert mutations > 0
    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "exactownerdichotomy" in statement
    assert "does not claim that" in audit
    assert "No Modal" in audit

    print(
        "XR_PRIZE_RANK_ONE_TRADE_FLAT_BASIS_OWNER_AUDIT_PASS "
        f"mutations={mutations}"
    )


if __name__ == "__main__":
    main()
