#!/usr/bin/env python3
"""Verify the fixed-support codeword quotient and an exact F_23 chart."""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from pathlib import Path


WITNESS = (
    Path(__file__).resolve().parents[1]
    / "l1_cross_quotient_split_descent_obstruction"
    / "verify.py"
)
SPEC = spec_from_file_location("l1_nonsplit_witness", WITNESS)
assert SPEC is not None and SPEC.loader is not None
V = module_from_spec(SPEC)
SPEC.loader.exec_module(V)


def quotient_cell_audit() -> tuple[int, int]:
    p = 7
    support = (0, 1, 2)
    locator = (0, 2, 4, 1)  # X(X-1)(X-2) over F_7.
    base = (3, 1, 4, 1, 2)
    images = set()
    codewords = set()
    for coefficients in product(range(p), repeat=2):
        quotient = tuple(coefficients)
        lifted = [0] * (len(locator) + len(quotient) - 1)
        for i, x in enumerate(locator):
            for j, y in enumerate(quotient):
                lifted[i + j] = (lifted[i + j] + x * y) % p
        codeword = tuple(
            ((base[i] if i < len(base) else 0)
             + (lifted[i] if i < len(lifted) else 0)) % p
            for i in range(max(len(base), len(lifted)))
        )
        assert all(
            sum(codeword[i] * pow(point, i, p) for i in range(len(codeword))) % p
            == sum(base[i] * pow(point, i, p) for i in range(len(base))) % p
            for point in support
        )
        images.add(quotient)
        codewords.add(codeword)
    assert len(images) == len(codewords) == p**2
    return len(codewords), len(images)


def reconstructed_codeword(
    defect: tuple[int, ...], numerator: tuple[int, ...]
) -> tuple[int, ...]:
    retained = tuple(point for point in V.CORE if point not in defect)
    return V.mul(V.locator(retained), numerator)


def exact_chart_audit() -> tuple[int, int]:
    p0 = reconstructed_codeword(V.D0, V.W0)
    p1 = reconstructed_codeword(V.D1, V.W1)
    assert len(p0) - 1 <= len(V.CORE)
    assert len(p1) - 1 <= len(V.CORE)
    assert all(V.evaluate(p0, x) == V.evaluate(p1, x) for x in V.SUPPORT)

    difference = V.sub(p1, p0)
    quotient, remainder = V.divmod_poly(difference, V.locator(V.SUPPORT))
    assert remainder == (0,)
    codimension = len(V.CORE) - len(V.SUPPORT)
    assert len(quotient) - 1 <= codimension
    return codimension, len(quotient) - 1


def main() -> None:
    ambient, images = quotient_cell_audit()
    codimension, quotient_degree = exact_chart_audit()
    assert codimension == 3

    print(
        "L1_FIXED_SUPPORT_CODEWORD_QUOTIENT_PASS "
        f"ambient={ambient} images={images} codimension={codimension} "
        f"quotient_degree={quotient_degree}"
    )


if __name__ == "__main__":
    main()
