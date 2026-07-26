#!/usr/bin/env python3
"""Independent audit of the E1 clean-anchor class and loss arithmetic."""

from __future__ import annotations

import itertools
from collections import Counter


EXPECTED = (
    (256, 65, 1 << 122,
     1146852336572689151906730465296195854216377730651578907904,
     1146852336572689151901413553313056190724762502410457529599,
     382284112190896383970682459093111839235997652964233428737),
    (256, 33, 1 << 122,
     38001322036274275320505631960233903602944,
     37996005124291135657014016731992782224639,
     12668879649419138327999082396158341660417),
    (512, 33, 1 << 122,
     3413962861332812601133559951042096138635313539480064,
     3413962861332807284221576811378604523407072418101759,
     1137987620444272639348514363568529251287851553619457),
    (256, 65, 317494674775468773183020924238786383963,
     1146852336572689151906730465296195854216377730651578907904,
     1146852336572689151589235790520727081033356806412792523940,
     382284112190896384074741713357221542466466218296788430623),
    (256, 33, 317494674775468773183020924238786383963,
     38001322036274275320505631960233903602944,
     37683827361498806547322611035995117218980,
     12772938903683248031229550961490896662303),
    (512, 33, 317494674775468773183020924238786383963,
     3413962861332812601133559951042096138635313539480064,
     3413962861332495106458784482268913117711074753096100,
     1137987620444376698602778473271759719853184108621343),
)


def class_count_from_ternary_profiles(half: int, ell: int) -> int:
    count = 0
    for word in itertools.product((-1, 0, 1), repeat=half):
        singleton_count = sum(value != 0 for value in word)
        remainder = ell - singleton_count
        if remainder >= 0 and remainder % 2 == 0:
            full_pairs = remainder // 2
            if full_pairs <= half - singleton_count:
                count += 1
    return count


def recurrence_count(half: int, ell: int) -> int:
    # Sum feasible signed supports via Pascal recurrence, independently of comb().
    binomial_row = [1]
    for _ in range(half):
        binomial_row = [1] + [
            binomial_row[index - 1] + binomial_row[index]
            for index in range(1, len(binomial_row))
        ] + [1]
    total = 0
    for singleton_count, choose_count in enumerate(binomial_row):
        remainder = ell - singleton_count
        if remainder >= 0 and remainder % 2 == 0 and remainder // 2 <= half - singleton_count:
            total += choose_count << singleton_count
    return total


def main() -> None:
    ternary_checks = 0
    for half in range(1, 9):
        for ell in range(2 * half + 1):
            assert class_count_from_ternary_profiles(half, ell) == recurrence_count(half, ell)
            ternary_checks += 1
    assert recurrence_count(8, 9) == 3280

    for order, ell, budget, expected_count, expected_allowance, expected_b_min in EXPECTED:
        got = recurrence_count(order // 2, ell)
        assert got == expected_count
        assert got - budget - 1 == expected_allowance
        assert expected_b_min == (got + budget + 3) // 3

    # Brute-force every labeled map for K<=7; fibers are reconstructed from maps.
    map_checks = 0
    for class_count in range(1, 8):
        for codomain_size in range(1, class_count + 1):
            observed_min = None
            for image in itertools.product(range(codomain_size), repeat=class_count):
                fibers = Counter(image).values()
                distinct = len(set(image))
                pair_count = sum(size * (size - 1) // 2 for size in fibers)
                assert class_count - distinct <= pair_count
                observed_min = pair_count if observed_min is None else min(observed_min, pair_count)
                map_checks += 1
            quotient, remainder = divmod(class_count, codomain_size)
            expected_min = (
                codomain_size * quotient * (quotient - 1) // 2
                + remainder * quotient
            )
            assert observed_min == expected_min

    print(
        "E1_CLEAN_ANCHOR_EXACT_COLLISION_ALLOWANCE_AUDIT_PASS "
        f"rows={len(EXPECTED)} ternary_checks={ternary_checks} map_checks={map_checks}"
    )


if __name__ == "__main__":
    main()
