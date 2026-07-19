#!/usr/bin/env python3
"""Replay the exact h=3 shifted-product splitting reduction."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from f3_h3_dilation_lift_bound import (
    activated_pairs,
    canonical,
    root_table,
    signatures,
)


def split_count(p: int, n: int, roots: list[int]) -> int:
    count = 0
    for triple in combinations(roots, 3):
        left, middle, right = triple
        e1 = (left + middle + right) % p
        e2 = (left * middle + left * right + middle * right) % p
        e3 = left * middle % p * right % p
        residual_roots = [
            value
            for value in roots
            if (
                e3 * value * value
                + (e3 - e2) * value
                + e1
                - e2
                + e3
            )
            % p
            == 0
        ]
        if len(residual_roots) != 2 or 1 in residual_roots:
            continue
        p_side = {pow(value, -1, p) for value in triple}
        q_side = {1, *residual_roots}
        if len(p_side) != 3 or len(q_side) != 3 or p_side & q_side:
            continue
        if sum(p_side) % p == 0:
            continue
        count += 6
    return count


def shifted_envelope(p: int, roots: list[int]) -> tuple[int, int]:
    shifted = [(1 - value) % p for value in roots if value != 1]
    inverse = {value: pow(value, -1, p) for value in shifted}
    products = Counter(left * right % p for left in shifted for right in shifted)
    quotients = Counter(
        left * inverse[right] % p for left in shifted for right in shifted
    )
    three_to_one = sum(
        multiplicity * quotients[value]
        for value, multiplicity in products.items()
    )
    energy = sum(multiplicity * multiplicity for multiplicity in products.values())
    if three_to_one > energy:
        raise AssertionError((p, three_to_one, energy))
    return three_to_one, energy


def verify_row(p: int, n: int) -> dict[str, int]:
    roots = root_table(p, n)
    normalized = {canonical(pair, n) for pair in activated_pairs(p, n)}
    nonzero_orbits = sum(
        signatures(pair[0], roots, p)[0] != 0 for pair in normalized
    )
    split = split_count(p, n, roots)
    if split != 36 * nonzero_orbits:
        raise AssertionError((p, n, split, nonzero_orbits))
    three_to_one, energy = shifted_envelope(p, roots)
    if split > three_to_one:
        raise AssertionError((p, n, split, three_to_one))
    return {
        "nonzero_orbits": nonzero_orbits,
        "split": split,
        "three_to_one": three_to_one,
        "energy": energy,
    }


def main() -> None:
    rows = ((97, 16), (97, 32), (193, 64))
    for p, n in rows:
        result = verify_row(p, n)
        print(
            f"p={p} n={n} A3_nz={result['nonzero_orbits']} "
            f"split={result['split']} N_3to1={result['three_to_one']} "
            f"energy={result['energy']}"
        )
    print(f"H3_SHIFTED_PRODUCT_SPLITTING_REDUCTION_PASS rows={len(rows)}")


if __name__ == "__main__":
    main()
