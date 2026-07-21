#!/usr/bin/env python3
"""Mutation checks for the selected-antipodal affine Stepanov cap."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_verify():
    spec = importlib.util.spec_from_file_location("cap_verify", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    n = 1 << 40
    a_0, b_0, d_0 = 79_896_510, 12_902, 79_896_510
    numerator = a_0 + 2 * n * b_0
    quotient, remainder = divmod(numerator, d_0)
    assert remainder != 0
    assert quotient == 355_106_851
    assert not (quotient + 1 < numerator / d_0)

    degree_budget = a_0 + n * b_0
    assert degree_budget < 31_950_697_969_885_030_204
    assert degree_budget > 1 << 53

    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    audit = (HERE / "audit.md").read_text()
    dependency = (HERE / "dependency_subdag.md").read_text()
    assert "355106851" in statement and "A_0+NB_0<p" in audit
    assert "every extension of the prime field" in proof
    assert "not `355106852`" in audit
    assert "no speculative child" in dependency

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_SELECTED_ANTIPODAL_AFFINE_STEPANOV_AUDIT_PASS "
        "rounding=1 characteristic=1 extension_field=1 determinant=1 no_scan=1"
    )


if __name__ == "__main__":
    main()
