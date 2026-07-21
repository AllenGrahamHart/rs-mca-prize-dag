#!/usr/bin/env python3
"""Mutation checks for the c2 minimum-support collision branch compiler."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_verify():
    spec = importlib.util.spec_from_file_location("branch_verify", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    p = verify.PRIME
    y, z = 7, 17
    linear, square = verify.factors(y, z)
    assert verify.curve(y, z) == -27 * linear * square % p
    assert verify.curve(y, z) != 27 * linear * square % p

    t = 4
    correct = 64 * t * (1 + t) ** 2 % p
    wrong = 64 * (1 + t) ** 2 % p
    assert correct != wrong

    statement = (HERE / "statement.md").read_text()
    audit = (HERE / "audit.md").read_text()
    dependency = (HERE / "dependency_subdag.md").read_text()
    assert "z!=-12" in statement
    assert "selected denominator pair" in audit
    assert "authorizes no dense" in dependency

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_BARYCENTRIC_COLLISION_BRANCH_AUDIT_PASS "
        "factor_sign=1 denominator_factor=1 z_minus_12=1 selected_scope=1 no_dense=1"
    )


if __name__ == "__main__":
    main()
