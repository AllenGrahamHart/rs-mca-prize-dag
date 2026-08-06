#!/usr/bin/env python3
"""Replay the h=3 three-to-one direct-floor reduction."""

from __future__ import annotations

from collections import Counter

from f3_h3_shifted_energy_direct_floor import primitive_root, subgroup


EXPECTED = {
    (97, 32): (9_692, 10_315, 4_742, 4_950),
    (4_289, 64): (3_639, 10_755, 981, 2_658),
    (7_937, 64): (5_765, 13_191, 1_571, 4_194),
}

OFFICIAL_N = 8_192
OFFICIAL_THREE_TO_ONE = 66_933_997


def verify_row(p: int, n: int) -> tuple[int, int, int, int]:
    roots = subgroup(p, n, primitive_root(p))
    root_set = set(roots)
    shifted = tuple((1 - value) % p for value in roots if value != 1)

    product = Counter(left * right % p for left in shifted for right in shifted)
    quotient = Counter(
        left * pow(right, -1, p) % p for left in shifted for right in shifted
    )
    three_to_one = sum(product[value] * quotient[value] for value in product)
    energy = sum(multiplicity * multiplicity for multiplicity in product.values())

    forced_output = 0
    signed_collisions = 0
    collision_free = 0
    for left in roots:
        if left == 1:
            continue
        for middle in roots:
            if middle == 1:
                continue
            partial = (1 - left) * (1 - middle) % p
            for right in roots:
                if right == 1:
                    continue
                output = (1 - partial * (1 - right)) % p
                if output in root_set:
                    forced_output += 1
                    signed_roots = (
                        left * middle % p,
                        left * right % p,
                        middle * right % p,
                        output,
                        -left % p,
                        -middle % p,
                        -right % p,
                        -left * middle * right % p,
                    )
                    if len(set(signed_roots)) < 8:
                        signed_collisions += 1
                    else:
                        collision_free += 1

    if forced_output != three_to_one:
        raise AssertionError(("TO2", p, n, forced_output, three_to_one))
    if three_to_one > energy:
        raise AssertionError(("TO1", p, n, three_to_one, energy))
    if signed_collisions + collision_free != three_to_one:
        raise AssertionError(
            ("collision split", p, n, signed_collisions, collision_free)
        )
    return three_to_one, energy, signed_collisions, collision_free


def main() -> None:
    for row, expected in EXPECTED.items():
        actual = verify_row(*row)
        if actual != expected:
            raise AssertionError((row, actual, expected))
    residual = (
        36 * OFFICIAL_N * OFFICIAL_N
        - OFFICIAL_THREE_TO_ONE
        - OFFICIAL_N // 2
    )
    if residual <= 0 or residual**3 <= 512 * OFFICIAL_N**4:
        raise AssertionError(("TO3 pinned row", residual))
    print(
        "H3_THREE_TO_ONE_DIRECT_FLOOR_PASS "
        f"rows={len(EXPECTED)} "
        f"collision_free={sum(expected[3] for expected in EXPECTED.values())}"
    )


if __name__ == "__main__":
    main()
