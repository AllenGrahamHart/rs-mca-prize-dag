#!/usr/bin/env python3
"""Replay the official shape-A subgroup-point genus floor."""

import argparse
from math import gcd


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def ceil_div(a, b):
    return (a + b - 1) // b


def replay(mutation=None):
    mutation = mutation or {}
    N = mutation.get("N", 2**41)
    e = mutation.get("e", (2**39 + 1) // 3)
    m = mutation.get("m", e - 2)
    n = mutation.get("n", (3 * e - 7) // 2)
    R = mutation.get("R", (9 * e - 7) // 2)
    coefficient = mutation.get("coefficient", 54)
    characteristic_floor = mutation.get("characteristic_floor", 2**167)

    P = R * m
    denominator = coefficient * N**2 * m * n
    chi_floor = ceil_div(P**3, denominator)
    genus_floor = ceil_div(chi_floor - 2 * (m + n) + 2, 2)
    genus_ceiling = (m - 1) * (n - 1)

    require(e == 183251937963, "official e")
    require(m == 183251937961, "official parameter degree")
    require(n == 274877906941, "official row degree")
    require(R == 824633720830, "classified-row count")
    require(N == 2199023255552, "official subgroup order")
    require(coefficient == 54, "Corvaja--Zannier cube coefficient")
    require(gcd(n, N) == 1 and n > 1, "translated-subtorus exclusion")
    require(P == 151115727450087753427630, "subgroup point floor")
    require(12 * N**2 * m * n < characteristic_floor, "characteristic branch")
    require((chi_floor - 1) * denominator < P**3, "chi lower strictness")
    require(chi_floor * denominator >= P**3, "chi ceiling")
    require(chi_floor == 262353693488940318721, "Euler characteristic floor")
    require(genus_floor == 131176846286340314460, "genus floor")
    require(genus_ceiling == 50371909149143533442400, "bidegree genus ceiling")
    require(genus_floor * 384 < genus_ceiling, "factor-384 endpoint")
    require(genus_floor * 385 > genus_ceiling, "factor-385 gap")

    return P, chi_floor, genus_floor, genus_ceiling


def tamper_selftest():
    mutations = [
        {"N": 2**41 + 1},
        {"e": (2**39 + 1) // 3 + 1},
        {"m": 183251937962},
        {"n": 274877906943},
        {"R": 824633720829},
        {"coefficient": 53},
        {"characteristic_floor": 2**160},
    ]
    rejected = 0
    for mutation in mutations:
        try:
            replay(mutation)
        except AssertionError:
            rejected += 1
    require(rejected == len(mutations), "hostile mutation rejection")
    return rejected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()

    P, chi_floor, genus_floor, genus_ceiling = replay()
    suffix = ""
    if args.tamper_selftest:
        suffix = f" mutations={tamper_selftest()}/7"
    print(
        "RATE_HALF_SHAPE_A_GENUS_FLOOR_PASS "
        f"points={P} chi={chi_floor} genus={genus_floor} "
        f"ceiling={genus_ceiling}{suffix}"
    )


if __name__ == "__main__":
    main()
