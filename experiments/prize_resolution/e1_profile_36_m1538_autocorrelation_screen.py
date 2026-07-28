#!/usr/bin/env python3
"""Screen the low-variance m=1538 chambers modulo 769."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, product


P = 769
TARGET = -18 % P


def primitive_root() -> int:
    for generator in range(2, P):
        if pow(generator, (P - 1) // 2, P) != 1 and pow(generator, (P - 1) // 3, P) != 1:
            return generator
    raise AssertionError("no primitive root")


def signed_terms(weights: list[int], size: int) -> list[tuple[int, int, tuple[tuple[int, int], ...]]]:
    rows = []
    for lags in combinations(range(1, 64), size):
        mask = sum(1 << lag for lag in lags)
        for signs in product((-1, 1), repeat=size):
            value = sum(sign * weights[lag] for lag, sign in zip(lags, signs)) % P
            rows.append((value, mask, tuple(zip(lags, signs))))
    return rows


def exact_mu_one(lags: tuple[int, ...]) -> bool:
    # For C=sum_d (X^d+X^-d), the coefficient of (X+1)^2 is the
    # parity of the number of odd d. Exact multiplicity two means it is odd.
    return sum(lag % 2 for lag in lags) % 2 == 1


def find_disjoint(
    left: list[tuple[int, int, tuple[tuple[int, int], ...]]],
    right_by_sum: dict[int, list[tuple[int, tuple[tuple[int, int], ...]]]],
    target: int,
    forbidden_mask: int = 0,
) -> tuple[tuple[int, int], ...] | None:
    for value, mask, terms in left:
        if mask & forbidden_mask:
            continue
        for other_mask, other_terms in right_by_sum.get((target - value) % P, ()):
            if (mask & other_mask) or (other_mask & forbidden_mask):
                continue
            witness = terms + other_terms
            if exact_mu_one(tuple(lag for lag, _ in witness)):
                return witness
    return None


def main() -> None:
    generator = primitive_root()
    root = pow(generator, 3, P)
    assert pow(root, 256, P) == 1 and pow(root, 128, P) == P - 1
    weights = [0] + [(pow(root, lag, P) + pow(root, -lag, P)) % P for lag in range(1, 64)]

    singles = signed_terms(weights, 1)
    pairs = signed_terms(weights, 2)
    triples = signed_terms(weights, 3)
    by_size = {1: singles, 2: pairs, 3: triples}
    grouped = {}
    for size, rows in by_size.items():
        table: dict[int, list[tuple[int, tuple[tuple[int, int], ...]]]] = defaultdict(list)
        for value, mask, terms in rows:
            table[value].append((mask, terms))
        grouped[size] = table

    def unit_witness(
        size: int, target: int, forbidden_mask: int = 0
    ) -> tuple[tuple[int, int], ...] | None:
        if size == 0:
            return None
        if size <= 3:
            for value, mask, terms in by_size[size]:
                if mask & forbidden_mask:
                    continue
                if value == target and exact_mu_one(tuple(lag for lag, _ in terms)):
                    return terms
            return None
        left_size = size // 2
        right_size = size - left_size
        return find_disjoint(
            by_size[left_size], grouped[right_size], target, forbidden_mask
        )

    profiles = {
        4: [(0, 2)],
        6: [(0, 3)],
        8: [(0, 4), (1, 0)],
        10: [(0, 5), (1, 1)],
        12: [(0, 6), (1, 2)],
    }
    results = {}
    for variance, shapes in profiles.items():
        witnesses = []
        for double_count, unit_count in shapes:
            shape = (double_count, unit_count)
            if double_count == 0:
                witness = unit_witness(unit_count, TARGET)
                witnesses.append((shape, witness))
                continue

            witness = None
            for lag in range(1, 64):
                for sign in (-1, 1):
                    adjusted = (TARGET - 2 * sign * weights[lag]) % P
                    units = unit_witness(unit_count, adjusted, 1 << lag)
                    if units is None:
                        continue
                    if exact_mu_one(tuple(unit_lag for unit_lag, _ in units)):
                        witness = ((lag, 2 * sign),) + units
                        break
                if witness is not None:
                    break
            witnesses.append((shape, witness))
        results[variance] = witnesses

    print(f"generator={generator} root={root} pair_rows={len(pairs)} triple_rows={len(triples)}")
    for variance, witnesses in results.items():
        for shape, witness in witnesses:
            print(f"V={variance} shape={shape} witness={witness}")

    assert all(any(witness is not None for _, witness in witnesses) for witnesses in results.values())
    print("E1_PROFILE_36_M1538_AUTOCORRELATION_SCREEN_PASS all_chambers_survive_relaxation")


if __name__ == "__main__":
    main()
