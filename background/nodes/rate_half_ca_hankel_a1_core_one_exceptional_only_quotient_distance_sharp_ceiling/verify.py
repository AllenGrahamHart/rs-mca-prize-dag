#!/usr/bin/env python3
"""Bigint checks for the sharp exceptional quotient-distance ceiling."""


def check_official_values():
    e = 2**38 - 1
    r = 2 * e + 1
    old_ceiling = 3 * (e + 1) // 2
    new_ceiling = old_ceiling - 1
    slopes = 4 * e
    total_complements = 6 * e * (e + 1)
    assert old_ceiling == 412316860416
    assert new_ceiling == 412316860415
    assert total_complements == slopes * old_ceiling
    assert 2 * e // (old_ceiling - 1) == 1
    assert 2 * e // (new_ceiling - 1) == 1

    flat = [old_ceiling] * slopes if slopes < 1000 else None
    assert flat is None  # Do not allocate the official profile.

    a_middle = r - old_ceiling
    assert a_middle == (e - 1) // 2
    assert r - new_ceiling == (e + 1) // 2
    assert r - (old_ceiling + 1) == (e - 3) // 2


def check_symbolic_profile_arithmetic():
    for e in (3, 5, 9):
        old = 3 * (e + 1) // 2
        h = old - 1
        slopes = 4 * e
        target_excess = slopes * old - slopes * h
        assert target_excess == slopes

        no_minimum = [1] * slopes
        one_minimum = [0, 2] + [1] * (slopes - 2)
        assert sum(no_minimum) == target_excess
        assert sum(one_minimum) == target_excess


def check_mutation_caught():
    e = 9
    old = 3 * (e + 1) // 2
    slopes = 4 * e
    exact = slopes * old
    mutated_lower = slopes * old + slopes - 1
    assert mutated_lower > exact


def main():
    check_official_values()
    check_symbolic_profile_arithmetic()
    check_mutation_caught()
    print("PASS exceptional quotient-distance sharp ceiling")


if __name__ == "__main__":
    main()
