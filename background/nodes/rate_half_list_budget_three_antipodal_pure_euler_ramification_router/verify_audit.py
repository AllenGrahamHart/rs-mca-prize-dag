#!/usr/bin/env python3
"""Independent audit of the pure Euler ramification router."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_pure_euler_ramification_router"


def official_degree_check() -> None:
    r = (1 << 37) - 1
    d = 4 * r + 4
    degree_v = r - 1
    degree_t = r
    degree_c = r + 3
    degree_phi = degree_t + 3 * r
    degree_w = degree_t + r - 1
    assert d == 1 << 39
    assert degree_phi == d - 4
    assert degree_w == 2 * r - 1
    assert degree_w - 2 * degree_v == 1
    assert 3 * degree_v + degree_c == degree_phi


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "Conversely" in statement
    assert "one-point defect localization" in contract
    assert "not an emptiness theorem" in contract
    assert "low-critical-value polynomials exist" in audit


def main() -> None:
    official_degree_check()
    scope_check()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_ANTIPODAL_PURE_EULER_RAMIFICATION_ROUTER_AUDIT_PASS "
        "official=1 degree_linear=1 converse_scope=kept"
    )


if __name__ == "__main__":
    main()
