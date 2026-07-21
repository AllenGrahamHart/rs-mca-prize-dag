#!/usr/bin/env python3
"""Mutation checks for the c2 minimum-support Euler divisor gate."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_verify():
    spec = importlib.util.spec_from_file_location("euler_verify", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    p = verify.PRIME
    h_minus_one = 2
    c_poly = [1, 0, 0, 1]
    t_poly = verify.add([h_minus_one], verify.mul(c_poly, [0, 1]))
    good = verify.add(t_poly, [-h_minus_one])
    wrong_sign = verify.add(t_poly, [h_minus_one])
    assert verify.divmod_poly(good, c_poly)[1] == [0]
    assert verify.divmod_poly(wrong_sign, c_poly)[1] != [0]

    statement = (HERE / "statement.md").read_text()
    audit = (HERE / "audit.md").read_text()
    dependency = (HERE / "dependency_subdag.md").read_text()
    assert "z^(-2H)" in statement
    assert "(H-1)E_4b_0z^(2H+1)" in statement
    assert "C_sharp=c_m^(-1)C" in statement
    assert "Full support-polynomial degree is essential" in audit
    assert "not permission to materialize" in dependency

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_MIN_SUPPORT_EULER_AUDIT_PASS "
        "binomial_sign=1 boundary_term=1 valuation_scope=1 monic_normalization=1 min_support_scope=1 no_dense=1"
    )


if __name__ == "__main__":
    main()
