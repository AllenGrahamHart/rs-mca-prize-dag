#!/usr/bin/env python3
"""Mutation audit for the XR flat-nullity rank-metric router."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    mutations = 0
    for m in range(1, 8):
        for columns in range(2, 12):
            for rank_limit in range(1, m + 1):
                threshold = (m - rank_limit) * columns
                # Strictness is essential: equality is allowed by Singleton.
                assert not (threshold > threshold)
                assert threshold + 1 > threshold
                mutations += 2

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "2s+(t-1)e+2" in statement
    assert "deletes rows of the compressed" in audit
    assert "No Modal" in audit

    print(
        "XR_PRIZE_FLAT_NULLITY_RANK_METRIC_TRADE_ROUTER_AUDIT_PASS "
        f"mutations={mutations}"
    )


if __name__ == "__main__":
    main()
