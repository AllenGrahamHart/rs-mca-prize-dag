#!/usr/bin/env python3
"""Independent audit of the exceptional quadratic-moment pin."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_quadratic_moment_pin"


def official_index_check() -> None:
    e = (1 << 38) - 1
    r = 2 * e + 1
    maxima = [2 * (r - 1) + shift for shift in range(3)]
    assert maxima == [2 * r - 2, 2 * r - 1, 2 * r]
    assert maxima[-1] == 2 * r


def symbolic_index_check() -> None:
    for r in range(2, 129):
        for shift in range(3):
            indices = [i + j + shift for i in range(r) for j in range(r)]
            assert min(indices) == shift
            assert max(indices) == 2 * (r - 1) + shift


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "contracted endpoint-syndrome weights" in statement
    assert "not a converse" in contract
    assert "generally change the" in audit
    assert "necessary, not sufficient" in audit


def main() -> None:
    official_index_check()
    symbolic_index_check()
    scope_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_QUADRATIC_MOMENT_PIN_AUDIT_PASS "
        "official=1 max_index=2r source_scope=kept"
    )


if __name__ == "__main__":
    main()
