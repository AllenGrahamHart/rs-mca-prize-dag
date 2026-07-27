#!/usr/bin/env python3
"""Census one-odd reflected vectors with vanishing odd autocorrelations."""

from __future__ import annotations

import modal


app = modal.App("e1-e38-one-odd-reflection-census")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=1.0, memory=256, timeout=60)
def census() -> dict[str, object]:
    from collections import Counter, defaultdict
    from itertools import combinations, product

    def half_autocorrelation(coefficients: dict[int, int]) -> list[int]:
        groups: dict[int, int] = defaultdict(int)
        support = sorted(coefficients)
        for left_index, left in enumerate(support):
            for right in support[left_index + 1 :]:
                difference = right - left
                value = coefficients[left] * coefficients[right]
                if difference < 64:
                    groups[difference] += value
                elif difference > 64:
                    groups[128 - difference] -= value
        return [groups[difference] for difference in range(64)]

    # Translate the unique odd support point to 1. Cancellation of its six
    # odd chords pairs the even points at radii +/-r, for odd 1<=r<=63.
    # Negacyclic wrap signs are handled by the autocorrelation routine itself.
    radii = range(1, 64, 2)
    target_count = 0
    vanishing_count = 0
    energy_histogram: Counter[int] = Counter()
    smallest_odd_energy: tuple[int, list[tuple[int, int]], int, int] | None = None
    e38_witness: dict[str, object] | None = None

    for chosen_radii in combinations(radii, 3):
        pairs = [((1 - radius) % 128, (1 + radius) % 128) for radius in chosen_radii]
        for heavy_pair in range(3):
            magnitudes = [2 if index == heavy_pair else 1 for index in range(3)]
            for signs in product((-1, 1), repeat=6):
                coefficients = {1: 2}
                sign_index = 0
                for pair, magnitude in zip(pairs, magnitudes):
                    for position in pair:
                        coefficients[position] = magnitude * signs[sign_index]
                        sign_index += 1
                if len(coefficients) != 7:
                    continue

                half = half_autocorrelation(coefficients)
                odd_energy = sum(half[difference] ** 2 for difference in range(1, 64, 2))
                energy = sum(value * value for value in half)
                l1_norm = sum(abs(value) for value in half)
                target_count += energy == 38 and l1_norm == 22
                if smallest_odd_energy is None or odd_energy < smallest_odd_energy[0]:
                    smallest_odd_energy = (
                        odd_energy,
                        sorted(coefficients.items()),
                        energy,
                        l1_norm,
                    )
                if odd_energy:
                    continue

                vanishing_count += 1
                energy_histogram[energy] += 1
                if energy == 38 and l1_norm == 22:
                    e38_witness = {
                        "coefficients": sorted(coefficients.items()),
                        "half_autocorrelation": [
                            (difference, half[difference])
                            for difference in range(1, 64)
                            if half[difference]
                        ],
                    }
                    return {
                        "complete": True,
                        "e38_witness": e38_witness,
                        "tested_target_vectors": target_count,
                        "vanishing_count_before_witness": vanishing_count,
                    }

    return {
        "complete": True,
        "e38_witness": e38_witness,
        "tested_target_vectors": target_count,
        "vanishing_count": vanishing_count,
        "vanishing_energy_histogram": sorted(energy_histogram.items()),
        "smallest_odd_energy": smallest_odd_energy,
    }


@app.local_entrypoint()
def main() -> None:
    print("E1_E38_ONE_ODD_REFLECTION_CENSUS " + repr(census.remote()))
