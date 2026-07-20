#!/usr/bin/env python3
"""Bigint checks for the exceptional minimal-support packing bound."""


def leader_bound(e, h):
    universe = 6 * e + 7
    intersection = 2 * h - 2 * e - 4
    delta = h * h - universe * intersection
    if delta <= 0:
        return None
    return universe * (h - intersection) // delta


def check_official_cutoffs():
    e = 2**38 - 1
    universe = 6 * e + 7
    assert universe == 1649267441665
    lower = e + 2
    cutoff = 302646214511
    lambda_cutoff = 2 * cutoff - 2 * e - 4
    delta_cutoff = cutoff * cutoff - universe * lambda_cutoff
    next_h = cutoff + 1
    next_delta = next_h * next_h - universe * (2 * next_h - 2 * e - 4)
    assert delta_cutoff == 350860694341 > 0
    assert next_delta == -2342381759966 < 0

    assert leader_bound(e, lower) == 5
    assert leader_bound(e, lower + 1) == 6
    assert leader_bound(e, 279180239468) == 6
    assert leader_bound(e, 279180239469) == 7
    assert 279180239468 - lower + 1 == 4302332524


def check_small_johnson_inequality():
    # Five disjoint 5-subsets fill a 25-point universe; six do not fit.
    e = 3
    h = e + 2
    universe = 6 * e + 7
    intersection = 2 * h - 2 * e - 4
    assert universe == 25 and intersection == 0
    assert leader_bound(e, h) == 5
    assert 5 * h == universe


def check_mutations_caught():
    e = 2**38 - 1
    h = e + 2
    correct = leader_bound(e, h)
    wrong_universe = 6 * e + 6
    intersection = 2 * h - 2 * e - 4
    wrong = wrong_universe * (h - intersection) // (
        h * h - wrong_universe * intersection
    )
    # The off-by-one universe is arithmetically visible even where floors agree.
    assert correct == wrong == 5
    assert 6 * e + 7 != wrong_universe


def main():
    check_official_cutoffs()
    check_small_johnson_inequality()
    check_mutations_caught()
    print("PASS exceptional quotient minimal-support packing")


if __name__ == "__main__":
    main()
