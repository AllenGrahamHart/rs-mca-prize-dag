#!/usr/bin/env python3
"""Exact finite audit of the shared Haar norm-product gate."""

from fractions import Fraction
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
    assert n_total & (n_total - 1) == 0
    e = sum(value == 1 for value in c)
    assert e == sum(value == -1 for value in c)

    levels = n_total.bit_length() - 1
    energies = []
    for j in range(levels):
        beta = ROUTER.fold(c, j)
        energies.append(sum(value * value for value in beta))

    identity = sum(
        (Fraction(energy, 1 << (j + 1)) for j, energy in enumerate(energies)),
        Fraction(0),
    )
    assert identity == 2 * e

    active = [
        j for j, energy in enumerate(energies[:-1]) if energy > 0
    ]
    subset_checks = 0
    for size in range(1, len(active) + 1):
        for selected in combinations(active, size):
            exponents = [n_total // (1 << (j + 2)) for j in selected]
            a_sum = sum(exponents)
            energy_product = 1
            norm_product = 1
            for j, exponent in zip(selected, exponents):
                beta = ROUTER.fold(c, j)
                norm = ROUTER.cyclotomic_norm(beta)
                assert norm > 0
                energy_product *= energies[j] ** exponent
                norm_product *= norm
            assert norm_product <= energy_product
            assert energy_product * (a_sum**a_sum) <= (e * n_total) ** a_sum
            subset_checks += 1
    return subset_checks


def exhaustive(n_total, widths):
    universe = set(range(n_total))
    vectors = 0
    subset_checks = 0
    for e in widths:
        for p_tuple in combinations(range(n_total), e):
            p_set = set(p_tuple)
            for q_tuple in combinations(sorted(universe - p_set), e):
                q_set = set(q_tuple)
                c = [
                    int(index in p_set) - int(index in q_set)
                    for index in range(n_total)
                ]
                subset_checks += check_vector(c)
                vectors += 1
    return vectors, subset_checks


def main():
    n8 = exhaustive(8, (1, 2, 3, 4))
    n16 = exhaustive(16, (1, 2))
    assert n8[0] == 1106
    assert n16[0] == 11160
    print(
        "X4_PRIMITIVE_SHIFTPAIR_HAAR_NORM_PRODUCT_GATE_PASS "
        f"n8={n8} n16={n16}"
    )


if __name__ == "__main__":
    main()
