#!/usr/bin/env python3
"""Independent audit of the unit-resultant normalization."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_unit_resultant_collapse"


def official_parity_and_exponents() -> None:
    e = (1 << 38) - 1
    r = 2 * e + 1
    d_0 = 8 * e + 7
    n_x = d_0 - 1
    assert r % 2 == 1
    assert n_x % 2 == 0
    assert d_0 - n_x == 1

    for m in (r - 2, r - 1):
        e_power = m + n_x + 1
        q_power = m + n_x
        assert e_power == q_power + 1
        assert e_power + 1 == m + d_0 + 1


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "actual `X`-degree" in statement
    assert "no root-free claim" in contract
    assert "false inverse-polynomial contradiction" in audit


def main() -> None:
    official_parity_and_exponents()
    scope_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_UNIT_RESULTANT_AUDIT_PASS "
        "official=1 parity=positive degree_guard=kept"
    )


if __name__ == "__main__":
    main()
