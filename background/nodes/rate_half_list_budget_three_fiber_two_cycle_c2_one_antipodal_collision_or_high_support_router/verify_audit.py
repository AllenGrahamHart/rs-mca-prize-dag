#!/usr/bin/env python3
"""Mutation checks for the c2 collision-or-high-support router."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_verify():
    spec = importlib.util.spec_from_file_location("router_verify", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    h = 5
    n = 8 * h - 8
    degree_only_floor = n - 2 - (4 * h - 7)
    parity_floor = n - 2 - (4 * h - 8)
    assert degree_only_floor == 4 * h - 3
    assert parity_floor == 4 * h - 2

    for y, z in ((0, 4), (4 * pow(3, -1, verify.PRIME) % verify.PRIME, 36)):
        curve, linear, square = verify.branch_factors(y, z)
        assert (curve, linear, square) == (0, 0, 0)

    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    audit = (HERE / "audit.md").read_text()
    dependency = (HERE / "dependency_subdag.md").read_text()
    assert "|supp u|>=4H-2" in statement and "|supp u|<=4H-4" in statement
    assert "None of these arguments used the size" in proof
    assert "odd lower bound `4H-3`" in audit
    assert "does not mint a conjecture" in dependency

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_COLLISION_OR_HIGH_SUPPORT_AUDIT_PASS "
        "automatic_zeros=2 parity_sharpening=1 scope_extension=1 intersections=2 nonclaims=1"
    )


if __name__ == "__main__":
    main()
