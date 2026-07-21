#!/usr/bin/env python3
"""Mutation checks for the c2 minimum-support infinity-cell torsion gate."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_verify():
    spec = importlib.util.spec_from_file_location("infinity_verify", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    p = verify.PRIME

    good = verify.polynomial_from_roots([1, 28, 27, 33])
    remainder = [0, 1]
    for _ in range(5):
        remainder = verify.square_remainder(remainder, good)
    assert remainder == [1]

    bad = verify.polynomial_from_roots([1, 28, 27, 2])
    remainder = [0, 1]
    for _ in range(5):
        remainder = verify.square_remainder(remainder, bad)
    assert remainder != [1]

    roots = [1, 28, 27, 33]
    derivatives = verify.derivative_values(roots)
    classes = sorted((derivatives.count(value) for value in set(derivatives)), reverse=True)
    assert classes == [2, 1, 1]

    statement = (HERE / "statement.md").read_text()
    audit = (HERE / "audit.md").read_text()
    dependency = (HERE / "dependency_subdag.md").read_text()
    assert "R_40=1" in statement and "R_40=X" in audit
    assert "explicit non-antipodal" in audit
    assert "not introduced as a speculative child" in dependency
    assert pow(2, 32, p) != 1

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_MIN_SUPPORT_INFINITY_TORSION_AUDIT_PASS "
        "endpoint=1 off_subgroup=1 collision_pattern=1 nonclassification=1 no_dense=1"
    )


if __name__ == "__main__":
    main()
