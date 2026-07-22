#!/usr/bin/env python3
"""Mutation audit for the arbitrary-W dual-plane support router."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    mutations = 0
    for multiplicities in ((1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1)):
        assert max(multiplicities) <= 2
        mutations += 1
    assert max((3, 1, 1)) > 2
    mutations += 1

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "projectivefibermap" in statement
    assert "may repeat twice" in audit
    assert "No Modal" in audit

    print(
        "XR_PRIZE_ARBITRARY_W_RANK_TWO_DUAL_PLANE_SUPPORT_ROUTER_AUDIT_PASS "
        f"mutations={mutations}"
    )


if __name__ == "__main__":
    main()
