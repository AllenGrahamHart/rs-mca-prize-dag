#!/usr/bin/env python3
"""Affine/Galois symmetry of the h=3 activation predicate."""

from __future__ import annotations

import json
import math
import random
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
SUMMARY_PATH = HERE / "f3_h3_all_core_census_summary.json"
N = 96
UNITS = tuple(u for u in range(N) if math.gcd(u, N) == 1)


def elementary(values: list[int], degree: int, p: int) -> int:
    total = 0
    for combo in combinations(values, degree):
        prod = 1
        for value in combo:
            prod = (prod * value) % p
        total = (total + prod) % p
    return total


def primitive_root_of_order(p: int, n: int) -> int:
    if (p - 1) % n:
        raise ValueError((p, n))
    for cand in range(2, p):
        root = pow(cand, (p - 1) // n, p)
        if root == 1:
            continue
        if pow(root, n, p) == 1 and all(pow(root, d, p) != 1 for d in range(1, n)):
            return root
    raise AssertionError((p, n))


def signature(exps: tuple[int, int, int], root: int, p: int) -> tuple[int, int, int]:
    values = [pow(root, exp, p) for exp in exps]
    return tuple(elementary(values, degree, p) for degree in (1, 2, 3))


def active(flat: tuple[int, ...], root: int, p: int) -> bool:
    left = tuple(sorted(flat[:3]))
    right = tuple(sorted(flat[3:]))
    left_sig = signature(left, root, p)
    right_sig = signature(right, root, p)
    return left_sig[:2] == right_sig[:2] and left_sig[2] != right_sig[2]


def active_root(flat: tuple[int, ...], base_root: int, p: int) -> int | None:
    for unit in UNITS:
        root = pow(base_root, unit, p)
        if active(flat, root, p):
            return root
    return None


def transform(flat: tuple[int, ...], unit: int, shift: int, swap: bool = False) -> tuple[int, ...]:
    left = tuple(sorted((unit * exp + shift) % N for exp in flat[:3]))
    right = tuple(sorted((unit * exp + shift) % N for exp in flat[3:]))
    return (right + left) if swap else (left + right)


def finite_field_checks() -> None:
    rng = random.Random(20260708)
    for p in (97, 193, 577, 769):
        root = primitive_root_of_order(p, N)
        for _ in range(200):
            exps = rng.sample(range(N), 6)
            flat = tuple(sorted(exps[:3]) + sorted(exps[3:]))
            unit = rng.choice(UNITS)
            shift = rng.randrange(N)
            transformed = transform(flat, unit, shift, bool(rng.randrange(2)))
            inv_unit = pow(unit, -1, N)
            transformed_root = pow(root, inv_unit, p)
            if active(flat, root, p) != active(transformed, transformed_root, p):
                raise AssertionError((p, flat, unit, shift, transformed))


def banked_activation_checks() -> None:
    data = json.loads(SUMMARY_PATH.read_text())
    activations = data["activation_exceptions"]
    if len(activations) != 720:
        raise AssertionError(len(activations))
    root_cache: dict[int, int] = {}
    for record in activations:
        flat = tuple(record["shape"])
        primes = record["activation_primes"]
        if len(primes) != 1:
            raise AssertionError(record)
        p = int(primes[0])
        base_root = root_cache.setdefault(p, primitive_root_of_order(p, N))
        root = active_root(flat, base_root, p)
        if root is None:
            raise AssertionError(("banked activation inactive", flat, p))
        for unit, shift, swap in (
            (1, 0, True),
            (5, 13, False),
            (7, 29, False),
            (11, 41, True),
        ):
            transformed = transform(flat, unit, shift, swap)
            transformed_root = pow(root, pow(unit, -1, N), p)
            if not active(transformed, transformed_root, p):
                raise AssertionError(("symmetry image inactive", flat, p, transformed))


def main() -> None:
    finite_field_checks()
    banked_activation_checks()
    print("h=3 activation symmetry")
    print("finite-field predicate checks: n=96, p in {97,193,577,769}, 200 samples each")
    print("banked activation transformed-embedding checks: 720 records")
    print("H3_ACTIVATION_SYMMETRY_PASS")


if __name__ == "__main__":
    main()
