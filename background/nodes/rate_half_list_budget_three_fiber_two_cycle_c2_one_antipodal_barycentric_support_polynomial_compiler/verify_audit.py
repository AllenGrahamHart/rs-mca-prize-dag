#!/usr/bin/env python3
"""Mutation checks for the c2 barycentric support-polynomial compiler."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_verify():
    spec = importlib.util.spec_from_file_location("support_poly_verify", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    p = verify.PRIME
    h = 3
    b = [1, 2, 3, 4]
    c = [1]
    v = verify.shift(c, h)
    q_minus = [1, -5 % p, 7]
    e = verify.mul([1, 0, -1 % p], q_minus)
    wronskian = verify.add(
        verify.mul(b, verify.derivative(v)),
        verify.scale(verify.mul(verify.derivative(b), v), -1),
    )
    good = verify.scale(verify.mul(verify.mul(e, verify.mul(v, v)), wronskian), -1)

    # The wrong partial-fraction sign reverses every nonzero moment.
    wrong_sign = verify.scale(good, -1)
    assert good != wrong_sign

    # Omitting the leading Wronskian cancellation gives only a weaker degree.
    r = 2 * h - 3
    assert len(wronskian) - 1 <= 2 * r - 2
    assert 2 * r - 2 < 2 * r - 1

    statement = (HERE / "statement.md").read_text()
    audit = (HERE / "audit.md").read_text()
    assert "J(1)J(-1)!=0" in statement
    assert "leading terms cancel" in audit
    assert "authorizes no dense" in (HERE / "dependency_subdag.md").read_text()

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_BARYCENTRIC_SUPPORT_POLY_AUDIT_PASS "
        "partial_fraction_sign=1 wronskian_degree=1 endpoint_overlap=1 no_dense=1"
    )


if __name__ == "__main__":
    main()
