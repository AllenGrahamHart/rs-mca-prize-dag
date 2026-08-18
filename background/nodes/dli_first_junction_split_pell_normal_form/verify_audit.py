#!/usr/bin/env python3
"""Independent value-state enumeration of the split-Pell normal form."""

from __future__ import annotations

from itertools import product


def coefficients(values: tuple[int, ...], roots: tuple[int, ...], q: int) -> tuple[int, ...]:
    h = len(values)
    return tuple(
        pow(h, -1, q) * sum(values[i] * pow(roots[i], (-s) % h, q)
                            for i in range(h)) % q
        for s in range(h)
    )


def main() -> None:
    h, l, q, zeta = 8, 1, 17, 3
    xs = tuple(pow(zeta, i, q) for i in range(h))
    ys = tuple(x * x % q for x in xs)

    normal = nonzero_w = 0
    for labels in product(range(4), repeat=h):
        a_values = []
        w_values = []
        for i, label in enumerate(labels):
            local = (
                ((-1) % q, 0),
                (1, 0),
                (0, xs[i]),
                (0, (-xs[i]) % q),
            )[label]
            a_values.append(local[0])
            w_values.append(local[1])
        a_poly = coefficients(tuple(a_values), ys, q)
        w_poly = coefficients(tuple(w_values), ys, q)
        gaps = (
            all(a_poly[s] == 0 for s in range(h - l, h))
            and w_poly[0] == 0
            and all(w_poly[s] == 0 for s in range(h - l + 1, h))
        )
        normal += gaps
        nonzero_w += gaps and any(w_poly)

    assert (normal, nonzero_w, normal - nonzero_w) == (224, 208, 16)
    print(
        "DLI_FIRST_JUNCTION_SPLIT_PELL_AUDIT_PASS "
        "states=65536 normal=224 primitive=208 owner=16"
    )


if __name__ == "__main__":
    main()
