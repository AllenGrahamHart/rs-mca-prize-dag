#!/usr/bin/env python3
"""Independent audit of the two-sided resultant exponents."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_two_sided_resultant_saturation"


def official_arithmetic() -> None:
    m = 1 << 37
    e = 2 * m - 1
    t = 4 * e + 1
    d_0 = 16 * m - 1
    n_x = d_0 - 1
    r = 2 * e + 1
    assert t * r - 1 == e * n_x
    assert (t - 1) * r + (r - 1) == e * n_x
    assert (t - 1) * (n_x - r) + (n_x - r + 1) == (t - e) * n_x

    # Mutation: forgetting the exceptional decrement overcounts by one.
    assert t * r != e * n_x


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "r-1" in statement and "n_X-r+1" in statement
    assert "no sufficiency" in contract
    assert "not treated as" in audit


def main() -> None:
    official_arithmetic()
    scope_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_RESULTANT_SATURATION_AUDIT_PASS "
        "official=1 mutation=exceptional_plus_one scope=guarded"
    )


if __name__ == "__main__":
    main()
