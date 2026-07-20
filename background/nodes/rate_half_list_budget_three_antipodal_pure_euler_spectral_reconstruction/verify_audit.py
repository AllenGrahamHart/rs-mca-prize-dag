#!/usr/bin/env python3
"""Audit signs, scope, and official dimensions in spectral reconstruction."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_pure_euler_spectral_reconstruction"


def official_check() -> None:
    r = (1 << 37) - 1
    d = 1 << 39
    degree = d - 4
    assert d == 4 * r + 4
    assert degree == 4 * r
    assert degree - 4 == 4 * (r - 1)
    assert d - degree == 4


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    proof = (here / "proof.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "X^4+e_4 splits" in statement
    assert "still requires the harmonic matching" in statement
    assert "dS_Phi-YS_Phi'" in proof
    assert "feasible dense official-order algorithm" in contract
    assert "never a dense length-`d`" in audit
    assert "No Modal or other remote computation was used" in audit


def main() -> None:
    official_check()
    scope_check()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_ANTIPODAL_PURE_EULER_SPECTRAL_RECONSTRUCTION_AUDIT_PASS "
        "official=1 sign=kept split_scope=kept harmonic_scope=kept"
    )


if __name__ == "__main__":
    main()
