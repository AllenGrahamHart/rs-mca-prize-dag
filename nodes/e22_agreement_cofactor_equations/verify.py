#!/usr/bin/env python3
"""Check the E22 cofactor agreement identity on the local n=16 profiles."""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

CORE = Path(__file__).resolve().parents[1] / "worst_word_challenger_pricing" / "notes"
sys.path.insert(0, str(CORE))

from e22_core import (  # noqa: E402
    P,
    classify_pattern,
    locator,
    pattern,
    poly_eval,
    polynomial_through,
    sunflower_word,
)


def trim(poly: list[int]) -> tuple[int, ...]:
    while poly and poly[-1] % P == 0:
        poly.pop()
    return tuple(x % P for x in poly)


def div_exact(poly: tuple[int, ...], divisor: tuple[int, ...]) -> tuple[int, ...]:
    rem = list(poly)
    den = list(divisor)
    if not den:
        raise ZeroDivisionError
    out = [0] * max(1, (len(rem) - len(den) + 1))
    inv_lead = pow(den[-1], -1, P)
    while len(rem) >= len(den) and rem:
        coeff = rem[-1] * inv_lead % P
        shift = len(rem) - len(den)
        out[shift] = coeff
        for i, d in enumerate(den):
            rem[shift + i] = (rem[shift + i] - coeff * d) % P
        while rem and rem[-1] == 0:
            rem.pop()
    assert not rem, rem
    return trim(out)


def listed_polys(word: dict) -> dict[tuple[int, ...], dict]:
    found = {}
    for indices in itertools.combinations(range(word["n"]), word["s"]):
        poly = polynomial_through(list(indices), word["domain"], word["values"], word["k"])
        if poly is None:
            continue
        rec = pattern(poly, word)
        if rec["agreement"] >= word["s"]:
            found[poly] = rec
    return found


def check_cell(n: int, k: int, sigma: int) -> int:
    word = sunflower_word(n, k, sigma, "cyclic_step_1", "linear")
    core = set(word["core"])
    zero_zone = set(word["core"]) | set(word["background"])
    checks = 0
    for poly, rec in listed_polys(word).items():
        cls = classify_pattern(rec, word["ell"])
        if cls not in {"mixed_petal", "full_petal"}:
            continue
        Z = sorted(idx for idx in zero_zone if poly_eval(poly, word["domain"][idx], P) == 0)
        LZ = locator([word["domain"][idx] for idx in Z], P)
        U = div_exact(poly, LZ)
        Z_not_C = sorted(idx for idx in Z if idx not in core)
        C_not_Z = sorted(idx for idx in word["core"] if idx not in set(Z))
        L_z_not_c = locator([word["domain"][idx] for idx in Z_not_C], P)
        L_c_not_z = locator([word["domain"][idx] for idx in C_not_Z], P)
        for scalar, petal in zip(word["scalars"], word["petals"]):
            for idx in petal:
                x = word["domain"][idx]
                if poly_eval(poly, x, P) != word["values"][idx]:
                    continue
                left = poly_eval(U, x, P) * poly_eval(L_z_not_c, x, P) % P
                right = scalar * poly_eval(L_c_not_z, x, P) % P
                assert left == right, (n, k, sigma, poly, idx, left, right)
                checks += 1
    return checks


def main() -> None:
    total = 0
    for k in (2, 4, 8):
        total += check_cell(16, k, 1)
    print(f"E22 cofactor equations verified on n=16 structured agreements: {total}")


if __name__ == "__main__":
    main()
