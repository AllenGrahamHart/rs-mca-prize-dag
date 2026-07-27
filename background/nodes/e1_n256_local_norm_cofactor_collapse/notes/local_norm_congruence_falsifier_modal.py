#!/usr/bin/env python3
"""Falsify the predicted unit-norm congruence on deterministic sparse samples."""

from __future__ import annotations

import modal


app = modal.App("e1-n256-local-norm-congruence-falsifier")
image = modal.Image.debian_slim().pip_install("python-flint")


@app.function(image=image, cpu=1.0, memory=512, timeout=60)
def falsify() -> dict[str, object]:
    import random
    import time

    from flint import fmpz, fmpz_poly

    started = time.monotonic()
    deadline = 52.0
    rng = random.Random(0xE1256)
    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    checked = 0
    first_failure = None

    explicit = {
        0: 2,
        16: -2,
        32: -1,
        48: 1,
        65: 1,
        80: -1,
        96: -2,
    }

    def negacyclic_product(left: list[int], right: list[int]) -> list[int]:
        result = [0] * 128
        for left_index, left_value in enumerate(left):
            if not left_value:
                continue
            for right_index, right_value in enumerate(right):
                if not right_value:
                    continue
                quotient, residue = divmod(left_index + right_index, 128)
                result[residue] += (
                    -1 if quotient % 2 else 1
                ) * left_value * right_value
        return result

    def explicit_moments(coefficients: dict[int, int]) -> dict[str, object]:
        import cmath
        import math

        autocorrelation = [0] * 128
        for left, left_value in coefficients.items():
            for right, right_value in coefficients.items():
                quotient, residue = divmod(left - right, 128)
                autocorrelation[residue] += (
                    -1 if quotient % 2 else 1
                ) * left_value * right_value
        square_mass = sum(value * value for value in coefficients.values())
        autocorrelation[0] -= square_mass
        powers = {}
        current = [1] + [0] * 127
        for degree in range(1, 7):
            current = negacyclic_product(current, autocorrelation)
            if degree >= 2:
                powers[str(degree)] = current[0]

        conjugate_squares = []
        for unit in range(1, 256, 2):
            zeta = cmath.exp(2j * math.pi * unit / 256)
            value = sum(
                coefficient * zeta**exponent
                for exponent, coefficient in coefficients.items()
            )
            conjugate_squares.append(abs(value) ** 2)
        return {
            "central_moments": powers,
            "minimum_y": min(conjugate_squares),
            "maximum_y": max(conjugate_squares),
        }

    def check(coefficients: dict[int, int], profile: str) -> dict[str, object]:
        nonlocal checked, first_failure
        dense = [0] * (max(coefficients) + 1)
        for index, value in coefficients.items():
            dense[index] = value
        norm = abs(int(cyclotomic.resultant(fmpz_poly(dense))))
        valuation = (norm & -norm).bit_length() - 1
        odd_part_mod_256 = (norm >> valuation) % 256
        checked += 1
        if odd_part_mod_256 != 1 and first_failure is None:
            first_failure = {
                "profile": profile,
                "coefficients": sorted(coefficients.items()),
                "valuation": valuation,
                "odd_part_mod_256": odd_part_mod_256,
            }
        return {
            "norm_bits": norm.bit_length(),
            "valuation": valuation,
            "odd_part_bits": (norm >> valuation).bit_length(),
            "odd_part_mod_256": odd_part_mod_256,
            "odd_part_is_prime": bool(fmpz(norm >> valuation).is_prime()),
            "odd_part": norm >> valuation,
        }

    explicit_record = {
        **check(explicit, "3,4,0-explicit"),
        **explicit_moments(explicit),
    }
    for profile, heavy_count, singleton_count in (
        ("3,4,0", 3, 4),
        ("4,2,0", 4, 2),
    ):
        for _ in range(256):
            if time.monotonic() - started > deadline:
                return {
                    "complete": False,
                    "checked": checked,
                    "first_failure": first_failure,
                    "explicit_record": explicit_record,
                }
            support = rng.sample(range(128), heavy_count + singleton_count)
            coefficients = {}
            for position, index in enumerate(support):
                magnitude = 2 if position < heavy_count else 1
                coefficients[index] = magnitude * rng.choice((-1, 1))
            check(coefficients, profile)

    return {
        "complete": True,
        "checked": checked,
        "first_failure": first_failure,
        "explicit_record": explicit_record,
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }


@app.local_entrypoint()
def main() -> None:
    result = falsify.remote()
    print("E1_N256_LOCAL_NORM_CONGRUENCE_FALSIFIER " + repr(result))
