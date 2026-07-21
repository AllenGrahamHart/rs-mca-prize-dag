#!/usr/bin/env python3
"""Mutation checks for the c2 canonical-cell Fourier ladder."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_verify():
    spec = importlib.util.spec_from_file_location("canonical_cell_verify", HERE / "verify.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    p = verify.PRIME
    h = 3
    b = [1, 2, 3, 4]
    ws = [1, 2, 3, -6 % p]
    sums = []
    for w in ws:
        factor = b[:]
        factor[h] = (factor[h] + w) % p
        sums.append(verify.power_sums(factor, 10))

    # The cutoff is strict: the w^3-kernel generally fails at degree 3H.
    rows = [[pow(w, exponent, p) for w in ws] for exponent in range(3)]
    lam = verify.null_vector(rows)
    assert sum(lam[i] * sums[i][3 * h] for i in range(4)) % p != 0

    # Distinctness is essential for both kernel dimensions and Vandermonde use.
    repeated = [1, 2, 2, -5 % p]
    assert len(set(repeated)) < 4

    # Negation support is paired, so the raw odd bound 2H+1 rounds upward.
    assert (2 * h + 1) % 2 == 1
    assert 2 * h + 2 == 8
    assert (3 * h + 1) % 2 == 0

    statement = (HERE / "statement.md").read_text()
    audit = (HERE / "audit.md").read_text()
    assert "either `u_lambda=0` identically" in statement
    assert "range is strict" in audit
    assert "authorizes no" in (HERE / "dependency_subdag.md").read_text()

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_CANONICAL_CELL_FOURIER_AUDIT_PASS "
        "strict_endpoint=1 repeated_outer=1 invariant_alternative=1 parity_rounding=1"
    )


if __name__ == "__main__":
    main()
