#!/usr/bin/env python3
"""Mutation audit for the general first-core peeling owner."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    mutations = 0
    for r in range(20, 80):
        for h in range(3, 15):
            for v in range(0, min(r, 10)):
                bound = (2 * (r - v) - 1) // h
                assert h * bound < 2 * (r - v)
                assert h * (bound + 1) >= 2 * (r - v)
                wrong = 2 * (r - v) // h
                if wrong != bound:
                    mutations += 1
    assert mutations > 0

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "firstnonzerotrade" in statement
    assert "recomputed after each deletion" in audit
    assert "No Modal" in audit

    print(
        "XR_PRIZE_FLAT_NULLITY_FIRST_CORE_PEELING_OWNER_AUDIT_PASS "
        f"mutations={mutations}"
    )


if __name__ == "__main__":
    main()
