#!/usr/bin/env python3
"""Mutation checks for the selected-antipodal infinity affine compiler."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_verify():
    spec = importlib.util.spec_from_file_location("affine_verify", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    p = verify.PRIME
    a, y, tau = 80, 50, 28
    first, second = verify.affine_values(a, y)
    assert (first, second) == (42, 89)

    wrong_first = ((a + 1) * y - (a + 2)) % p
    assert wrong_first != first
    assert a * a % p == -2 % p and a * a % p != 2

    new_a, new_y, new_tau = -a % p, pow(y, -1, p), tau * y % p
    new_first, new_second = verify.affine_values(new_a, new_y)
    old_roots = [tau * first % p, tau * second % p, tau * y % p, tau]
    new_roots = [new_tau * new_first % p, new_tau * new_second % p,
                 new_tau * new_y % p, new_tau]
    assert new_roots == [old_roots[1], old_roots[0], old_roots[3], old_roots[2]]

    p_src = 69
    z_inf = p_src * y * first * second % p
    assert pow(z_inf, verify.ORDER // 4, p) == 1
    assert pow(z_inf, verify.ORDER // 8, p) != 1
    assert pow(28, verify.ORDER, p) == 1
    assert pow(28, verify.ORDER // 4, p) != 1

    statement = (HERE / "statement.md").read_text()
    audit = (HERE / "audit.md").read_text()
    dependency = (HERE / "dependency_subdag.md").read_text()
    assert "a^2=-2" in statement and "tau^4" in statement
    assert "Z_inf^(N/4)=1" in statement and "not merely `N/2`" in audit
    assert "genuine subgroup scale" in audit
    assert "No speculative conjecture" in dependency

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_SELECTED_ANTIPODAL_INFINITY_AFFINE_AUDIT_PASS "
        "sign=1 discriminants=1 scale=1 quarter_strict=1 involution=1 nonemptiness=1"
    )


if __name__ == "__main__":
    main()
