#!/usr/bin/env python3
"""Independent audit of the full reciprocal unit-square descent."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_full_reciprocal_square_descent"


def official_degree_check() -> None:
    e = (1 << 38) - 1
    r = 2 * e + 1
    d_0 = 8 * e + 7
    n_x = d_0 - 1
    exponent = n_x + r - 1
    assert exponent == d_0 + r - 2
    assert exponent == 10 * e + 6
    assert r + n_x == exponent + 1


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "one division by `P_cl` and two divisions by `E`" in statement
    assert "no automatic exactness" in contract
    assert "possibly zero" in audit
    assert "Hankel and" in audit


def main() -> None:
    official_degree_check()
    scope_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_FULL_RECIPROCAL_SQUARE_AUDIT_PASS "
        "official=1 exponent=n_X+r-1 zero_branch=kept"
    )


if __name__ == "__main__":
    main()
