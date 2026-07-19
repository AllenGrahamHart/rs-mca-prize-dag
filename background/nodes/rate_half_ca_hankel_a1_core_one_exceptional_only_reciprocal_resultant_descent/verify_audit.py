#!/usr/bin/env python3
"""Independent audit of reciprocal signs and theorem scope."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_reciprocal_resultant_descent"


def official_sign_and_exponent() -> None:
    e = (1 << 38) - 1
    r = 2 * e + 1
    d_0 = 8 * e + 7
    assert r % 2 == d_0 % 2 == 1
    reversal_sign = (-1) ** (r * d_0)
    linear_resultant_sign = (-1) ** r
    assert reversal_sign == linear_resultant_sign == -1
    assert reversal_sign // linear_resultant_sign == 1
    assert r - 1 == 2 * e


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "proved fixed degrees" in statement
    assert "no profile exclusion" in contract
    assert "does not assume" in audit
    assert "not promoted" in audit


def main() -> None:
    official_sign_and_exponent()
    scope_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_RECIPROCAL_DESCENT_AUDIT_PASS "
        "official=1 reversal_sign=-1 linear_sign=-1 scope=kept"
    )


if __name__ == "__main__":
    main()
