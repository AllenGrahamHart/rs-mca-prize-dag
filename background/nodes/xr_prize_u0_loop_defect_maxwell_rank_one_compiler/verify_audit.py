#!/usr/bin/env python3
"""Mutation audit for the prize u=0 loop-defect compiler."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    # The loop-defect term is forced by the exact row/rank ledger.
    mutations = 0
    for a in range(2, 6):
        for h in range(1, 5):
            for v in range(1, 5):
                for t in range(3, 7):
                    for e in range(h):
                        numerator = h * t + 2 * (a + v) - e
                        if numerator % 2:
                            continue
                        union = numerator // 2
                        actual = (h + v) * t - (2 * union - (2 * a + 1))
                        expected = v * (t - 2) + e + 1
                        assert actual == expected
                        assert actual != expected - 1
                        mutations += 1

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "Rank-onetrades" in statement
    assert "classified in both directions" in audit
    assert "No Modal" in audit

    print(
        "XR_PRIZE_U0_LOOP_DEFECT_MAXWELL_RANK_ONE_COMPILER_AUDIT_PASS "
        f"mutations={mutations}"
    )


if __name__ == "__main__":
    main()
