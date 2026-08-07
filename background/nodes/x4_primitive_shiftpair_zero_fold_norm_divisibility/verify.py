#!/usr/bin/env python3
"""Finite exact audit of zero-fold dyadic norm divisibility."""

from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path


def load_router():
    path = (
        Path(__file__).resolve().parents[1]
        / "x4_primitive_shiftpair_dyadic_norm_router"
        / "verify.py"
    )
    spec = spec_from_file_location("x4_dyadic_router_verify", path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ROUTER = load_router()


def check_vector(c):
    n_total = len(c)
    e = sum(value == 1 for value in c)
    assert e == sum(value == -1 for value in c)
    supplied = list(range(n_total.bit_length() - 2))
    active = [j for j in supplied if any(ROUTER.fold(c, j))]
    zero = [j for j in supplied if j not in active]
    if not active:
        return 0

    norm_product = 1
    energy_product = 1
    a_sum = 0
    for j in active:
        beta = ROUTER.fold(c, j)
        energy = sum(value * value for value in beta)
        exponent = n_total // (1 << (j + 2))
        norm_product *= ROUTER.cyclotomic_norm(beta)
        energy_product *= energy**exponent
        a_sum += exponent

    t_two = sum(
        min(n_total >> j, n_total >> a) // 2
        for j in active
        for a in zero
    )
    two_divisor = 1 << (len(active) + t_two)
    assert norm_product % two_divisor == 0
    assert norm_product <= energy_product
    assert two_divisor * (a_sum**a_sum) <= (e * n_total) ** a_sum
    return 1


def exhaustive(n_total, widths):
    universe = set(range(n_total))
    total = 0
    checked = 0
    patterns = set()
    for e in widths:
        for p_tuple in combinations(range(n_total), e):
            p_set = set(p_tuple)
            for q_tuple in combinations(sorted(universe - p_set), e):
                q_set = set(q_tuple)
                c = [
                    int(index in p_set) - int(index in q_set)
                    for index in range(n_total)
                ]
                total += 1
                checked += check_vector(c)
                supplied = range(n_total.bit_length() - 2)
                patterns.add(tuple(bool(any(ROUTER.fold(c, j))) for j in supplied))
    return total, checked, len(patterns)


def main():
    n8 = exhaustive(8, (1, 2, 3, 4))
    n16 = exhaustive(16, (1, 2))
    assert n8[0] == 1106 and n16[0] == 11160
    assert n8[1] > 0 and n16[1] > 0
    print(
        "X4_PRIMITIVE_SHIFTPAIR_ZERO_FOLD_NORM_DIVISIBILITY_PASS "
        f"n8={n8} n16={n16}"
    )


if __name__ == "__main__":
    main()
