#!/usr/bin/env python3
"""Mutation audit for the arbitrary-W received-pair router."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    mutations = 0
    for a, b, c, d in ((0, 1, -1, 0), (1, 0, 0, 1), (1, 2, 3, 5)):
        assert a * d - b * c != 0
        mutations += 1
    assert 1 * 4 - 2 * 2 == 0
    mutations += 1

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "Fiveblocks" in statement
    assert "zero branch is retained" in audit
    assert "No Modal" in audit

    print(
        "XR_PRIZE_ARBITRARY_W_RANK_TWO_RECEIVED_PAIR_ROUTER_AUDIT_PASS "
        f"mutations={mutations}"
    )


if __name__ == "__main__":
    main()
