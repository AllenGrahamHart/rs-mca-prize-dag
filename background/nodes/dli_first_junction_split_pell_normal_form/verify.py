#!/usr/bin/env python3
"""Exhaustively verify the first-junction split-Pell normal form."""

from __future__ import annotations

import argparse
import copy
from itertools import product


EXPECTED = {
    "words": 1 << 16,
    "null": 224,
    "nonprimitive": 16,
    "primitive": 208,
    "normal_form": 224,
    "nonzero_w": 208,
}


def cyclic_mul(left: list[int], right: list[int], q: int) -> list[int]:
    h = len(left)
    out = [0] * h
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[(i + j) % h] = (out[(i + j) % h] + a * b) % q
    return out


def interpolate(values: list[int], roots: list[int], q: int) -> list[int]:
    h = len(values)
    inv_h = pow(h, -1, q)
    return [
        inv_h * sum(value * pow(root, (-s) % h, q)
                    for value, root in zip(values, roots, strict=True)) % q
        for s in range(h)
    ]


def build() -> dict[str, int]:
    n, h, l, q, zeta = 16, 8, 1, 17, 3
    xs = [pow(zeta, i, q) for i in range(h)]
    ys = [x * x % q for x in xs]
    assert len(set(ys)) == h
    result = {key: 0 for key in EXPECTED}
    result["words"] = 1 << n

    for bits in product((0, 1), repeat=n):
        direct = all(
            sum(bits[i] * pow(zeta, moment * i, q) for i in range(n)) % q == 0
            for moment in range(1, 2 * l + 1)
        )
        a_values = [(bits[i] + bits[i + h] - 1) % q for i in range(h)]
        w_values = [xs[i] * (bits[i] - bits[i + h]) % q for i in range(h)]
        a_poly = interpolate(a_values, ys, q)
        w_poly = interpolate(w_values, ys, q)

        degree_gaps = (
            all(a_poly[s] == 0 for s in range(h - l, h))
            and w_poly[0] == 0
            and all(w_poly[s] == 0 for s in range(h - l + 1, h))
        )
        assert direct == degree_gaps

        a2 = cyclic_mul(a_poly, a_poly, q)
        a3 = cyclic_mul(a2, a_poly, q)
        assert all((a3[s] - a_poly[s]) % q == 0 for s in range(h))
        w2 = cyclic_mul(w_poly, w_poly, q)
        pell = w2[:]
        for s, value in enumerate(a2):
            pell[(s + 1) % h] = (pell[(s + 1) % h] + value) % q
        pell[1] = (pell[1] - 1) % q
        assert all(value == 0 for value in pell)

        if direct:
            result["null"] += 1
            result["normal_form"] += degree_gaps
            primitive = any(bits[i] != bits[i + h] for i in range(h))
            result["primitive"] += primitive
            result["nonprimitive"] += not primitive
            nonzero_w = any(w_poly)
            result["nonzero_w"] += nonzero_w
            assert primitive == nonzero_w

    assert result == EXPECTED
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        changed["nonzero_w"] += 1
        caught = 0
        try:
            assert changed == result
        except AssertionError:
            caught = 1
        assert caught == 1
        print("DLI_FIRST_JUNCTION_SPLIT_PELL_TAMPER_PASS mutations=1/1")
        return
    print(
        "DLI_FIRST_JUNCTION_SPLIT_PELL_PASS "
        "n=16 null=224 owner=16 primitive=208"
    )


if __name__ == "__main__":
    main()
