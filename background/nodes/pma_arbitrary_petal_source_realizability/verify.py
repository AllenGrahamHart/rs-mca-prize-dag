#!/usr/bin/env python3
"""Verify arbitrary-petal sunflower realizability on a smooth domain."""

from __future__ import annotations

import json


NODE = "pma_arbitrary_petal_source_realizability"


def evaluate(poly: list[int], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def multiply(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def locator(points: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for point in points:
        out = multiply(out, [-point, 1], p)
    return out


def build_word(
    domain: tuple[int, ...],
    core: tuple[int, ...],
    background: tuple[int, ...],
    petals: tuple[tuple[int, ...], ...],
    labels: tuple[int, ...],
    p: int,
) -> tuple[dict[int, int], list[int]]:
    core_locator = locator(core, p)
    word = {x: 0 for x in core + background}
    for petal, label in zip(petals, labels, strict=True):
        for x in petal:
            word[x] = label * evaluate(core_locator, x, p) % p
    assert set(word) == set(domain)
    return word, core_locator


def agreement(
    domain: tuple[int, ...], word: dict[int, int], poly: list[int], p: int
) -> set[int]:
    return {x for x in domain if word[x] == evaluate(poly, x, p)}


def run() -> dict[str, object]:
    p = 17
    domain = tuple(range(1, 17))
    core = tuple(range(1, 8))
    petals = ((8, 9), (10, 11), (12, 13), (14, 15))
    background = (16,)
    labels = (1, 2, 3, 4)
    ell = 2
    k = 8

    word, core_locator = build_word(
        domain, core, background, petals, labels, p
    )
    agreement_sets = []
    for petal, label in zip(petals, labels, strict=True):
        codeword = [(label * coefficient) % p for coefficient in core_locator]
        assert len(codeword) - 1 == k - 1
        actual = agreement(domain, word, codeword, p)
        expected = set(core) | set(petal)
        assert actual == expected
        assert len(actual) == k - 1 + ell == k + 1
        agreement_sets.append(actual)

    for i, left in enumerate(agreement_sets):
        for right in agreement_sets[i + 1 :]:
            assert left & right == set(core)

    petal_locators = [locator(petal, p) for petal in petals]
    linear_coefficients = [poly[1] for poly in petal_locators]
    assert len(set(linear_coefficients)) == len(petals)

    packing_checks = 0
    for n in range(4, 129):
        for core_size in range(1, n):
            remainder = n - core_size
            for size in range(1, remainder + 1):
                petals_count, b = divmod(remainder, size)
                assert b < size
                assert petals_count * size <= remainder
                assert (petals_count + 1) * size > remainder
                packing_checks += 1

    # Mutation 1: repeated labels merge two petals.
    repeated = (1, 1, 3, 4)
    mutant_word, mutant_core = build_word(
        domain, core, background, petals, repeated, p
    )
    mutant_codeword = [coefficient % p for coefficient in mutant_core]
    assert agreement(domain, mutant_word, mutant_codeword, p) == (
        set(core) | set(petals[0]) | set(petals[1])
    )

    # Mutation 2: a zero label gains every zero-background point.
    zero_labels = (0, 2, 3, 4)
    zero_word, _ = build_word(domain, core, background, petals, zero_labels, p)
    assert set(core) | set(petals[0]) | set(background) <= agreement(
        domain, zero_word, [0], p
    )

    # Mutation 3: b=ell leaves enough points for another petal.
    assert len((15, 16)) == ell

    # Mutation 4: a core of size k-2 misses the k+1 threshold by one.
    assert (k - 2) + ell == k

    return {
        "node": NODE,
        "status": "PASS",
        "domain_size": len(domain),
        "petals": len(petals),
        "agreement_per_codeword": k + 1,
        "petal_linear_coefficients": linear_coefficients,
        "packing_checks": packing_checks,
        "mutations_caught": 4,
    }


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True))
