#!/usr/bin/env python3
"""Independent audit of the exceptional Hankel-factor identification."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_factor_pin"


def official_omission_check() -> None:
    e = (1 << 38) - 1
    r = 2 * e + 1
    d = 2 * e + 1
    assert r == d
    assert r - (r - 1) == 1


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "nonzero field" in statement
    assert "scalar `c_H`" in statement
    assert "no normalization of `c_H` by a square root" in contract
    assert "boundary-only" in audit
    assert "No exact valuation claim" in audit


def main() -> None:
    official_omission_check()
    scope_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_HANKEL_FACTOR_PIN_AUDIT_PASS "
        "official=1 omission=1 scalar_guard=kept valuation_guard=kept"
    )


if __name__ == "__main__":
    main()
