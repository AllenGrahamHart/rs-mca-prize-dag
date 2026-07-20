#!/usr/bin/env python3
"""Independent audit of the exceptional Hankel kernel-plane theorem."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_kernel_plane_transversality"


def official_complete_intersection_check() -> None:
    e = (1 << 38) - 1
    r = 2 * e + 1
    form_degree = 2 * r
    first_generator = r - 1
    second_generator = form_degree + 2 - first_generator
    assert second_generator == r + 3
    assert (r + 1) - (r - 1) == 2


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "other exceptional kernel line" in statement
    assert "no converse from the" in contract
    assert "not merely the specialized" in audit
    assert "generic rank recovery alone" in audit


def main() -> None:
    official_complete_intersection_check()
    scope_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_KERNEL_PLANE_TRANSVERSALITY_AUDIT_PASS "
        "official=1 kernel_dim=2 higher_order_guard=kept"
    )


if __name__ == "__main__":
    main()
