#!/usr/bin/env python3
"""Exhaust the canonical FR identity for three sets on five points."""

from itertools import product


def size(mask: int) -> int:
    return mask.bit_count()


def main() -> None:
    masks = range(1 << 5)
    checks = 0
    pairs = ((0, 1, 2), (0, 2, 1), (1, 2, 0))
    for family in product(masks, repeat=3):
        unions = [size(family[i] | family[j]) for i, j, _ in pairs]
        a_star = min(unions)
        for (g, h, gamma), union_size in zip(pairs, unions):
            if union_size != a_star:
                continue
            s_gamma = family[gamma]
            w_star = family[g] | family[h]
            lhs = size(s_gamma & w_star)
            rhs = (
                2 * size(s_gamma)
                + size(family[g])
                + size(family[h])
                - 2 * a_star
            )
            assert lhs <= rhs
            assert size(s_gamma & ~w_star) >= size(s_gamma) - rhs
            checks += 1

    for m in (1, 2, 3, 4, 8, 64, 1 << 20, 1 << 37):
        rho = 4 * m - 1
        a_star = 7 * m - 1
        assert 4 * rho - 2 * a_star == 2 * m - 2
        assert 2 * a_star - 3 * rho == 2 * m + 1

    print(f"RATE_HALF_FR_CANONICAL_MIN_PAIR_UNION_BOUND_PASS checks={checks}")


if __name__ == "__main__":
    main()
