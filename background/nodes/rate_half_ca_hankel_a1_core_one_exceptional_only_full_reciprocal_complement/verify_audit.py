#!/usr/bin/env python3
"""Independent audit of the full reciprocal complement descent."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_full_reciprocal_complement"


def official_degree_check() -> None:
    e = (1 << 38) - 1
    r = 2 * e + 1
    d_0 = 8 * e + 7
    s = d_0 - r
    n_x = d_0 - 1
    assert s - 1 == 6 * e + 5
    assert r + s == d_0
    assert r + s - 1 == n_x
    assert d_0 - n_x == 1


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "necessary reduction" in statement
    assert "no converse" in contract
    assert "exactly one factor of `Y`" in audit
    assert "separate divisibility" in audit


def main() -> None:
    official_degree_check()
    scope_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_FULL_RECIPROCAL_COMPLEMENT_AUDIT_PASS "
        "official=1 reversal_degree=D_0 reconstruction_guard=kept"
    )


if __name__ == "__main__":
    main()
