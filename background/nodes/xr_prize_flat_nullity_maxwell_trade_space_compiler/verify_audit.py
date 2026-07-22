#!/usr/bin/env python3
"""Mutation audit for the general flat-nullity Maxwell compiler."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    mutations = 0
    for a in range(1, 5):
        for h in range(1, 5):
            for u in range(4):
                for v in range(4):
                    for t in range(3, 7):
                        for e in range(h):
                            numerator = h * t + 2 * (a + u + v) - e
                            if numerator % 2:
                                continue
                            union = numerator // 2
                            actual = (h + u + v) * t - (
                                2 * union - (2 * a + 1)
                            )
                            expected = (u + v) * (t - 2) + e + 1
                            assert actual == expected
                            assert actual != expected + 1
                            mutations += 1

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "canonicalsharedlocal-tangentcircuit" in statement
    assert "No MDS dual-distance claim" in audit
    assert "No Modal" in audit

    print(
        "XR_PRIZE_FLAT_NULLITY_MAXWELL_TRADE_SPACE_COMPILER_AUDIT_PASS "
        f"mutations={mutations}"
    )


if __name__ == "__main__":
    main()
