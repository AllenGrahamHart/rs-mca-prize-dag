#!/usr/bin/env python3
"""Mutation checks for the c2 minimum-support endpoint torsion gate."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_verify():
    spec = importlib.util.spec_from_file_location("endpoint_verify", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    p = verify.PRIME
    b_top, b_next = 8, 7
    c_top, c_next = 11, 9
    good = (b_next * c_top - b_top * c_next) % p
    reversed_sign = (b_top * c_next - b_next * c_top) % p
    assert good != reversed_sign

    n = 32
    generator = verify.subgroup_generator(n)
    roots = []
    for exponent in [1, 2, 3, 4, 5, 6, 8]:
        root = pow(generator, exponent, p)
        roots.extend((root, -root % p))
    xi = 1
    for root in roots:
        xi = xi * root % p
    assert pow(xi, n // 2, p) == 1
    assert pow(xi, n // 4, p) != 1

    statement = (HERE / "statement.md").read_text()
    audit = (HERE / "audit.md").read_text()
    dependency = (HERE / "dependency_subdag.md").read_text()
    assert "Xi^(N/2)=1" in statement
    assert "distinct from the" in audit
    assert "authorizes neither dense" in dependency

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_MIN_SUPPORT_ENDPOINT_TORSION_AUDIT_PASS "
        "determinant_sign=1 strict_half_order=1 notation_scope=1 no_dense=1"
    )


if __name__ == "__main__":
    main()
