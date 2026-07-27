#!/usr/bin/env python3
"""Measure one exact full-conductor E=50, L=28 geometric witness."""

from __future__ import annotations

import modal


app = modal.App("e1-n256-e50-witness-norm")
image = modal.Image.debian_slim().pip_install("python-flint")


@app.function(image=image, cpu=1.0, memory=512, timeout=60)
def measure() -> dict[str, object]:
    import cmath
    import math
    from collections import defaultdict

    from flint import fmpz, fmpz_poly

    coefficients = {
        48: -2,
        51: -2,
        67: -1,
        81: 2,
        83: 1,
        84: -1,
        111: 1,
    }

    groups: dict[int, list[int]] = defaultdict(list)
    diameter_square_mass = 0
    support = sorted(coefficients)
    for left_index, left in enumerate(support):
        for right in support[left_index + 1 :]:
            difference = right - left
            product = coefficients[left] * coefficients[right]
            if difference == 64:
                diameter_square_mass += product * product
            elif difference < 64:
                groups[difference].append(product)
            else:
                groups[128 - difference].append(-product)
    energy = sum(sum(values) ** 2 for values in groups.values())
    l1_norm = sum(abs(sum(values)) for values in groups.values())
    cross_sum = sum(
        sum(
            values[left] * values[right]
            for left in range(len(values))
            for right in range(left + 1, len(values))
        )
        for values in groups.values()
    )

    dense = [0] * 128
    for exponent, coefficient in coefficients.items():
        dense[exponent] = coefficient
    norm = abs(int(fmpz_poly([1] + [0] * 127 + [1]).resultant(fmpz_poly(dense))))
    valuation = (norm & -norm).bit_length() - 1
    odd_part = norm >> valuation

    autocorrelation = [0] * 128
    for left, left_value in coefficients.items():
        for right, right_value in coefficients.items():
            quotient, residue = divmod(left - right, 128)
            autocorrelation[residue] += (
                -1 if quotient % 2 else 1
            ) * left_value * right_value
    autocorrelation[0] -= 16

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

    moments = {}
    power = [1] + [0] * 127
    for degree in range(1, 7):
        power = negacyclic_product(power, autocorrelation)
        if degree >= 2:
            moments[str(degree)] = power[0]

    conjugate_squares = []
    for unit in range(1, 256, 2):
        zeta = cmath.exp(2j * math.pi * unit / 256)
        value = sum(
            coefficient * zeta**exponent
            for exponent, coefficient in coefficients.items()
        )
        conjugate_squares.append(abs(value) ** 2)

    return {
        "coefficients": sorted(coefficients.items()),
        "conductor_gcd": math.gcd(
            256, *(position - support[0] for position in support)
        ),
        "energy": energy,
        "variance": 2 * energy,
        "l1_norm": l1_norm,
        "diameter_square_mass": diameter_square_mass,
        "cross_sum": cross_sum,
        "central_moments": moments,
        "minimum_y": min(conjugate_squares),
        "maximum_y": max(conjugate_squares),
        "norm_bits": norm.bit_length(),
        "norm_below_2_250": norm < 2**250,
        "valuation": valuation,
        "odd_part_bits": odd_part.bit_length(),
        "odd_part_mod_256": odd_part % 256,
        "odd_part_is_prime": bool(fmpz(odd_part).is_prime()),
        "norm": norm,
    }


@app.local_entrypoint()
def main() -> None:
    print("E1_N256_E50_WITNESS_NORM " + repr(measure.remote()))
