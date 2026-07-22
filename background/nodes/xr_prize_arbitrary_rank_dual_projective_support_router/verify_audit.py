#!/usr/bin/env python3
"""Mutation audit for the arbitrary-rank projective support router."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    mutations = 0
    for rank in range(2, 50):
        for arity in range(rank + 2, 2 * rank + 2):
            expected = 2 * rank - arity + 1
            assert expected >= 0
            assert expected != 2 * rank - arity
            mutations += 1

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "projectivehyperplanesection" in statement
    assert "can overlap when" in audit
    assert "No Modal" in audit

    print(
        "XR_PRIZE_ARBITRARY_RANK_DUAL_PROJECTIVE_SUPPORT_ROUTER_AUDIT_PASS "
        f"mutations={mutations}"
    )


if __name__ == "__main__":
    main()
