#!/usr/bin/env python3
"""Mutation checks for the c2 barycentric negation syndrome."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_verify():
    spec = importlib.util.spec_from_file_location("barycentric_verify", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    p = verify.PRIME
    roots = [value % p for value in (1, -1, 2, -2, 3, -3, 4, -4, 5, -5)]
    h = 3
    good = {
        root: (-2 * h) * pow(verify.derivative_at_roots(roots, root), -1, p) % p
        for root in roots
    }

    # Dropping the negation factor two gives the wrong first syndrome.
    half = {
        root: (-h) * pow(verify.derivative_at_roots(roots, root), -1, p) % p
        for root in roots
    }
    endpoint = lambda weights: sum(
        weights[root] * pow(root, 3 * h, p) for root in roots
    ) % p
    assert endpoint(good) == -2 * h % p
    assert endpoint(half) == -h % p
    assert endpoint(half) != endpoint(good)

    # Removing one support point destroys the full zero prefix.
    shortened = roots[:-1]
    short_weights = {
        root: (-2 * h) * pow(verify.derivative_at_roots(shortened, root), -1, p) % p
        for root in shortened
    }
    assert sum(short_weights[root] * pow(root, len(shortened) - 1, p) for root in shortened) % p == -2 * h % p

    statement = (HERE / "statement.md").read_text()
    audit = (HERE / "audit.md").read_text()
    assert "=-2H!=0" in statement
    assert "equality-case classification only" in audit
    assert "authorizes no computation" in (HERE / "dependency_subdag.md").read_text()

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_BARYCENTRIC_SYNDROME_AUDIT_PASS "
        "factor_two=1 shortened_support=1 equality_scope=1 no_compute=1"
    )


if __name__ == "__main__":
    main()
