#!/usr/bin/env python3
"""Multiplicity checks for the sharp endpoint resultant profiles."""


def profile_exponents(e, swapped):
    ordinary = 4 * e
    base = (e - 1) // 2
    exponents = [base] * ordinary
    if swapped:
        exponents[0] += 1
        exponents[1] -= 1
    return exponents


def check_profiles():
    for e in (3, 5, 9):
        endpoint = 3 * (e + 1) // 2 - 1
        r = 2 * e + 1
        for swapped in (False, True):
            exponents = profile_exponents(e, swapped)
            assert len(exponents) == 4 * e
            assert sum(exponents) == 2 * e * (e - 1)
            assert 2 * e + sum(exponents) == 2 * e * e
            complements = [r - exponent for exponent in exponents]
            assert sum(complements) == 4 * e * 3 * (e + 1) // 2
            if swapped:
                assert complements[0] == endpoint
                assert complements[1] == endpoint + 2
                assert all(value == endpoint + 1 for value in complements[2:])
            else:
                assert all(value == endpoint + 1 for value in complements)

    # Official arithmetic is checked without allocating 4e entries.
    e = 2**38 - 1
    base = (e - 1) // 2
    endpoint = 3 * (e + 1) // 2 - 1
    r = 2 * e + 1
    assert 4 * e * base == 2 * e * (e - 1)
    assert 2 * e + 4 * e * base == 2 * e * e
    assert r - base == endpoint + 1
    assert r - (base + 1) == endpoint
    assert r - (base - 1) == endpoint + 2
    complement_base = r - base
    assert complement_base == 3 * (e + 1) // 2
    assert (r - 1) - 2 * e == 0


def check_mutation_caught():
    e = 5
    correct = profile_exponents(e, True)
    mutated = correct[:]
    mutated[1] += 1
    assert sum(correct) == 2 * e * (e - 1)
    assert sum(mutated) != 2 * e * (e - 1)


def main():
    check_profiles()
    check_mutation_caught()
    print("PASS exceptional quotient endpoint resultant profile")


if __name__ == "__main__":
    main()
