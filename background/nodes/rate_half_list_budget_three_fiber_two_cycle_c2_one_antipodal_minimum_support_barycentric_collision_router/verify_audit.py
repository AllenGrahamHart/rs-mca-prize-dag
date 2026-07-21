#!/usr/bin/env python3
"""Mutation checks for the c2 barycentric collision router."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_verify():
    spec = importlib.util.spec_from_file_location("collision_verify", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    p = verify.PRIME
    roots = [1, 2, 33, 61]
    alpha, beta, gamma = verify.outer_coefficients(roots)
    pair_sum = (roots[1] + roots[3]) % p
    delta = (4 * gamma - alpha * alpha) % p

    # Reversing the outer-polynomial sign convention breaks the pair formula.
    assert pow(pair_sum, 3, p) != beta
    assert pow(pair_sum, 3, p) == -beta % p

    # Dropping the alpha factor breaks the eliminated collision equation.
    assert pow(delta, 3, p) != 8 * beta * beta % p
    assert pow(delta, 3, p) == 8 * pow(alpha, 3, p) * beta * beta % p

    statement = (HERE / "statement.md").read_text()
    audit = (HERE / "audit.md").read_text()
    dependency = (HERE / "dependency_subdag.md").read_text()
    assert "necessary, not sufficient" in audit
    assert "32z_t(z_t-36)^2" in statement
    assert "alpha=4c!=0" in audit
    assert "authorizes no dense" in dependency

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_BARYCENTRIC_COLLISION_ROUTER_AUDIT_PASS "
        "outer_sign=1 alpha_factor=1 necessity_scope=1 triple_exclusion=1 no_dense=1"
    )


if __name__ == "__main__":
    main()
