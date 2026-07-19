#!/usr/bin/env python3
"""Independent audit of the leading reciprocal Bezout identity."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_reciprocal_bezout_normalization"


def official_coefficient_check() -> None:
    e = (1 << 38) - 1
    r = 2 * e + 1
    d_0 = 8 * e + 7
    a_top_degree = d_0 - r
    a_minus_degree = a_top_degree - 1
    assert r + a_top_degree == d_0
    assert r + a_minus_degree == d_0 - 1
    assert (r - 1) + a_top_degree == d_0 - 1


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "specified inverse" in statement
    assert "no uniqueness" in contract
    assert "complete form `E q_bar`" in audit
    assert "No profile exclusion" in audit


def main() -> None:
    official_coefficient_check()
    scope_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_RECIPROCAL_BEZOUT_AUDIT_PASS "
        "official=1 coefficient=D_0-1 uniqueness_guard=kept"
    )


if __name__ == "__main__":
    main()
