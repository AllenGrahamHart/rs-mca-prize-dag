#!/usr/bin/env python3
"""Independent four-set replay of every minimizing-pair inequality."""

from itertools import combinations, product


def main() -> None:
    pair_indices = tuple(combinations(range(4), 2))
    checks = 0
    for family in product(range(16), repeat=4):
        union_sizes = {
            pair: (family[pair[0]] | family[pair[1]]).bit_count()
            for pair in pair_indices
        }
        a_star = min(union_sizes.values())
        for (g, h), union_size in union_sizes.items():
            if union_size != a_star:
                continue
            w_star = family[g] | family[h]
            for gamma in range(4):
                if gamma in (g, h):
                    continue
                u_gamma = family[gamma].bit_count()
                upper = (
                    2 * u_gamma
                    + family[g].bit_count()
                    + family[h].bit_count()
                    - 2 * a_star
                )
                inside = (family[gamma] & w_star).bit_count()
                outside = (family[gamma] & (15 ^ w_star)).bit_count()
                assert inside <= upper
                assert outside >= u_gamma - upper
                checks += 1

    print(
        "RATE_HALF_FR_CANONICAL_MIN_PAIR_UNION_BOUND_AUDIT_PASS "
        f"checks={checks}"
    )


if __name__ == "__main__":
    main()
