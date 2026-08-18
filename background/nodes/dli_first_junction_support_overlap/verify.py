#!/usr/bin/env python3
"""Exhaustive small-field replay of the first-junction overlap identity."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
from itertools import product


FIXTURES = ((8, 2, 17), (8, 4, 17), (16, 2, 17), (16, 4, 17))
EXPECTED = {
    "fixtures": 4,
    "positive": 1,
    "rows": {
        "8|2|17": {"z0": 4, "c1": 4, "primitive": 0, "z1": 36,
                    "b0": 16, "ratio_num": 0, "ratio_den": 1},
        "8|4|17": {"z0": 2, "c1": 2, "primitive": 0, "z1": 18,
                    "b0": 16, "ratio_num": 0, "ratio_den": 1},
        "16|2|17": {"z0": 224, "c1": 16, "primitive": 208, "z1": 3856,
                     "b0": 3856, "ratio_num": 53248, "ratio_den": 58081},
        "16|4|17": {"z0": 4, "c1": 4, "primitive": 0, "z1": 388,
                     "b0": 320, "ratio_num": 0, "ratio_den": 1},
    },
}


def factors(value: int) -> list[int]:
    out: list[int] = []
    p = 2
    while p * p <= value:
        if value % p == 0:
            out.append(p)
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        out.append(value)
    return out


def primitive_root(q: int) -> int:
    for g in range(2, q):
        if all(pow(g, (q - 1) // p, q) != 1 for p in factors(q - 1)):
            return g
    raise AssertionError("primitive root missing")


def null(values: tuple[int, ...], columns: list[tuple[int, ...]], q: int) -> bool:
    return all(sum(a * column[r] for a, column in zip(values, columns)) % q == 0
               for r in range(len(columns[0])))


def fixture(n: int, t: int, q: int) -> dict[str, int]:
    h, L = n // 2, t // 2
    zeta = pow(primitive_root(q), (q - 1) // n, q)
    assert pow(zeta, h, q) == q - 1
    x = [pow(zeta, i, q) for i in range(h)]
    y = [value * value % q for value in x]
    even_columns = [tuple(pow(value, r, q) for r in range(1, L + 1)) for value in y]
    odd_columns = [tuple(x[i] * pow(y[i], r, q) % q for r in range(L))
                   for i in range(h)]

    E: dict[int, int] = {}
    O: dict[int, int] = {}
    for mask in range(1 << h):
        support = [i for i in range(h) if mask >> i & 1]
        complement = [i for i in range(h) if not (mask >> i & 1)]

        even_count = 0
        signed_complement = 0
        for choices in product((0, 1), repeat=len(complement)):
            e = [1 if i in support else 0 for i in range(h)]
            epsilon = [0] * h
            for i, bit in zip(complement, choices):
                e[i] = 2 * bit
                epsilon[i] = 1 if bit else -1
            even_count += null(tuple(e), even_columns, q)
            signed_complement += null(tuple(epsilon), even_columns, q)
        assert even_count == signed_complement
        E[mask] = even_count

        odd_count = 0
        for signs in product((-1, 1), repeat=len(support)):
            o = [0] * h
            for i, sign in zip(support, signs):
                o[i] = sign
            odd_count += null(tuple(o), odd_columns, q)
        O[mask] = odd_count

        if 1 <= len(support) <= L:
            assert O[mask] == 0
        if 1 <= len(complement) <= L:
            assert E[mask] == 0

    z0_support = sum(E[mask] * O[mask] for mask in E)
    c1 = E[0]
    z1_support = sum((1 << mask.bit_count()) * E[mask] for mask in E)
    b0_support = sum((1 << (h - mask.bit_count())) * O[mask] for mask in O)

    roots = [pow(zeta, i, q) for i in range(n)]
    level0_columns = [tuple(pow(root, r, q) for r in range(1, t + 1))
                      for root in roots]
    z0_direct = sum(null(bits, level0_columns, q)
                    for bits in product((0, 1), repeat=n))
    primitive_direct = sum(
        null(bits, level0_columns, q)
        and any(bits[i] != bits[i + h] for i in range(h))
        for bits in product((0, 1), repeat=n)
    )
    z1_direct = sum(
        (1 << sum(value == 1 for value in values))
        for values in product((0, 1, 2), repeat=h)
        if null(values, even_columns, q)
    )
    b0_direct = sum(
        (1 << sum(value == 0 for value in values))
        for values in product((-1, 0, 1), repeat=h)
        if null(values, odd_columns, q)
    )

    assert z0_support == z0_direct
    assert z0_support - c1 == primitive_direct
    assert z1_support == z1_direct
    assert b0_support == b0_direct

    overlap = sum(
        Fraction((1 << mask.bit_count()) * E[mask], z1_support)
        * Fraction((1 << (h - mask.bit_count())) * O[mask], b0_support)
        for mask in E if mask
    )
    ratio = Fraction((z0_support - c1) << n, z1_support * b0_support)
    assert ratio == (1 << h) * overlap
    return {
        "z0": z0_support,
        "c1": c1,
        "primitive": primitive_direct,
        "z1": z1_support,
        "b0": b0_support,
        "ratio_num": ratio.numerator,
        "ratio_den": ratio.denominator,
    }


def build() -> dict[str, object]:
    rows = {f"{n}|{t}|{q}": fixture(n, t, q) for n, t, q in FIXTURES}
    summary = {
        "fixtures": len(rows),
        "positive": sum(row["primitive"] > 0 for row in rows.values()),
        "rows": rows,
    }
    assert summary == EXPECTED
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        first = next(iter(changed["rows"].values()))
        first["z0"] += 1
        caught = 0
        try:
            assert changed == result
        except AssertionError:
            caught = 1
        assert caught == 1
        print("DLI_FIRST_JUNCTION_SUPPORT_OVERLAP_TAMPER_PASS mutations=1/1")
        return
    print(
        "DLI_FIRST_JUNCTION_SUPPORT_OVERLAP_PASS "
        f"fixtures={result['fixtures']} positive={result['positive']}"
    )


if __name__ == "__main__":
    main()
