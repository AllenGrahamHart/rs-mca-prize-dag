#!/usr/bin/env python3
"""Verify the exact residual-budget prime-field collapse."""

from __future__ import annotations

from math import gcd
from pathlib import Path


N = 2**41
BUDGETS = (2**39, 2**39 + 1)
ROOTS = {
    2: (1, N // 2 - 1, N // 2 + 1, N - 1),
    3: (1,),
    4: tuple(sorted({(sign + j * 2**39) % N for sign in (1, -1) for j in range(4)})),
}


def ceil_nth_root(value: int, degree: int) -> int:
    low = 0
    high = 1 << ((value.bit_length() + degree - 1) // degree + 1)
    while low + 1 < high:
        middle = (low + high) // 2
        if middle**degree < value:
            low = middle
        else:
            high = middle
    assert (high - 1) ** degree < value <= high**degree
    return high


def candidates(budget: int, degree: int) -> tuple[int, ...]:
    lower = budget * 2**128
    upper = (budget + 1) * 2**128
    first = ceil_nth_root(lower, degree)
    stop = ceil_nth_root(upper, degree)
    out = []
    for residue in ROOTS[degree]:
        value = residue + ((first - residue + N - 1) // N) * N
        while value < stop:
            assert lower <= value**degree < upper
            assert pow(value, degree, N) == 1
            out.append(value)
            value += N
    return tuple(sorted(out))


def load_factor_ledger() -> dict[tuple[int, int, int], int]:
    path = Path(__file__).with_name("quadratic_candidate_factors.tsv")
    lines = path.read_text(encoding="ascii").splitlines()
    assert lines[0] == "budget\tdegree\tcandidate_p\tfactor"
    ledger = {}
    for line in lines[1:]:
        budget, degree, candidate, factor = map(int, line.split("\t"))
        key = (budget, degree, candidate)
        assert key not in ledger
        assert 1 < factor < candidate
        assert candidate % factor == 0
        ledger[key] = factor
    return ledger


def main() -> None:
    assert 3**105 < 2**168 < 3**106

    # Exact replay of the LTE lower-bound degree sieve.
    survivors = []
    for degree in range(1, 106):
        if degree % 2:
            lower_p = 2**41 + 1
        else:
            two_adic = (degree & -degree).bit_length() - 1
            lower_p = 2 ** (41 - two_adic) - 1
        if lower_p**degree < 2**168:
            survivors.append(degree)
    assert survivors == [1, 2, 3, 4]

    # The listed roots are complete by C_2 x C_(2^39), and all are replayed.
    for degree, roots in ROOTS.items():
        expected_count = gcd(degree, 2) * gcd(degree, 2**39)
        assert len(roots) == expected_count
        assert len(set(roots)) == expected_count
        assert all(pow(root, degree, N) == 1 for root in roots)

    ledger = load_factor_ledger()
    seen = set()
    counts = {}
    for budget in BUDGETS:
        for degree in (2, 3, 4):
            values = candidates(budget, degree)
            counts[(budget, degree)] = len(values)
            if degree in (3, 4):
                assert values == ()
            for value in values:
                key = (budget, degree, value)
                assert key in ledger
                seen.add(key)

    assert counts == {
        (2**39, 2): 24,
        (2**39, 3): 0,
        (2**39, 4): 0,
        (2**39 + 1, 2): 22,
        (2**39 + 1, 3): 0,
        (2**39 + 1, 4): 0,
    }
    assert seen == set(ledger)
    assert len(ledger) == 46

    print(
        "RATE_HALF_RESIDUAL_PRIME_FIELD_COLLAPSE_PASS "
        "degrees=1,2,3,4 quadratic_candidates=46 "
        "cubic_candidates=0 quartic_candidates=0 composite=46"
    )


if __name__ == "__main__":
    main()
