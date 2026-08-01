#!/usr/bin/env python3
"""Brute-force small-modulus audit of the Smith congruence solver."""

import importlib.util
import itertools
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_zero_loop_433_cell2_product_probe.py"
)


def brute(rows, values, modulus):
    return {
        point
        for point in itertools.product(range(modulus), repeat=3)
        if all(
            sum(row[index] * point[index] for index in range(3)) % modulus
            == value % modulus
            for row, value in zip(rows, values)
        )
    }


def main():
    specification = importlib.util.spec_from_file_location("router", SCRIPT)
    router = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(router)
    matrices = (
        ((0, 0, 1), (2, 1, 1), (1, 2, 1), (1, 1, 2)),
        ((2, 0, 0), (0, 2, 0), (0, 0, 2), (1, 1, 1)),
        ((1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 2, 2)),
        ((0, 2, 0), (1, 1, 2), (2, 0, 1), (1, 3, 1)),
    )
    checks = 0
    for modulus in (15, 16):
        for index, rows in enumerate(matrices):
            seed = tuple((index + 2 * coordinate + 1) % modulus for coordinate in range(3))
            values = tuple(
                sum(row[coordinate] * seed[coordinate] for coordinate in range(3))
                % modulus
                for row in rows
            )
            rank, solutions, family = router.solve_congruences(
                rows, values, modulus=modulus, family_sample_size=modulus
            )
            if family:
                expected = brute(rows, values, modulus)
                if set(solutions) != expected:
                    raise RuntimeError(f"family brute mismatch {modulus}/{index}")
            else:
                if set(solutions) != brute(rows, values, modulus):
                    raise RuntimeError(f"isolated brute mismatch {modulus}/{index}")
            if rank > 3 or any(
                sum(rows[row][column] * point[column] for column in range(3))
                % modulus != values[row]
                for point in solutions
                for row in range(4)
            ):
                raise RuntimeError("replay")
            checks += 1

    if router.GENERATOR != 3 or math.gcd(router.GENERATOR, router.P) != 1:
        raise RuntimeError("base generator")
    if pow(router.GENERATOR, router.BASE_ORDER, router.P) != 1:
        raise RuntimeError("base order")
    for prime in (2, 127):
        if pow(router.GENERATOR, router.BASE_ORDER // prime, router.P) == 1:
            raise RuntimeError(f"base primitive root {prime}")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_PRODUCT_ROUTER_AUDIT_PASS "
        f"smith_bruteforce={checks} moduli=15,16"
    )


if __name__ == "__main__":
    main()
