#!/usr/bin/env python3
"""Mutation audit for the polarized petal-entropy ledger."""

import itertools


def main() -> None:
    ell = 9
    petals = 4

    # Mutation 1: total deficit misprices a sparse petal.
    sizes = (1, ell, ell, ell)
    polar = sum(min(a, ell - a) for a in sizes)
    deficit = sum(ell - a for a in sizes)
    assert polar == 1 < deficit

    # Mutation 2: dropping the orientation factor misses all full/empty words.
    zero_cost = [
        sizes
        for sizes in itertools.product((0, ell), repeat=petals)
        if sum(min(a, ell - a) for a in sizes) == 0
    ]
    assert len(zero_cost) == 2**petals
    assert len(zero_cost) > 1

    # Mutation 3: using only touched petals loses the identity of full petals.
    full_sets = {
        tuple(i for i, a in enumerate(sizes) if a == ell)
        for sizes in zero_cost
    }
    assert len(full_sets) == 2**petals

    print("L1_POLARIZED_PETAL_ENTROPY_AUDIT_PASS mutations=3")


if __name__ == "__main__":
    main()
