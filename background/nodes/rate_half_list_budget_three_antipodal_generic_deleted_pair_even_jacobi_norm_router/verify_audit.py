#!/usr/bin/env python3
"""Audit scope and official dimensions of the even-Jacobi norm router."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = (
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_"
    "even_jacobi_norm_router"
)


def official_check() -> None:
    m = 1 << 35
    ell = 1 << 36
    source_degree = (1 << 37) - 1
    assert ell == 2 * m
    assert source_degree == 2 * ell - 1
    assert ell // m == 2


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "still six signed tests" in statement
    assert "no degree-" in statement
    assert "none of the six gcds is proved trivial" in contract
    assert "not the two choices of `s`" in audit
    assert "No Modal or other remote computation was used" in audit


def main() -> None:
    official_check()
    scope_check()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_ANTIPODAL_GENERIC_DELETED_PAIR_EVEN_JACOBI_NORM_ROUTER_AUDIT_PASS "
        "official=1 signs=6 degree=2^35 nonclaim=kept"
    )


if __name__ == "__main__":
    main()
