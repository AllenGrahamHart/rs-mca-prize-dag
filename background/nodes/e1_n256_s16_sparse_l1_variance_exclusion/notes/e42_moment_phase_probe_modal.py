#!/usr/bin/env python3
"""Probe third-moment and phase maxima on the geometric E=42, L=24 locus."""

from __future__ import annotations

import modal


app = modal.App("e1-n256-e42-moment-phase-probe")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=1.0, memory=256, timeout=30)
def search(seed: int) -> dict[str, object]:
    import cmath
    import math
    import random
    import time
    from collections import defaultdict

    started = time.monotonic()
    deadline = 15.0
    rng = random.Random(0xE142300 + seed)
    mode = "third_moment" if seed % 2 == 0 else "maximum_y"

    def ledger(coefficients: dict[int, int]) -> tuple[int, int, list[int]]:
        groups: dict[int, list[int]] = defaultdict(list)
        support = sorted(coefficients)
        for left_index, left in enumerate(support):
            for right in support[left_index + 1 :]:
                difference = right - left
                product = coefficients[left] * coefficients[right]
                if difference == 64:
                    continue
                if difference < 64:
                    groups[difference].append(product)
                else:
                    groups[128 - difference].append(-product)
        half = [0] * 64
        for difference, values in groups.items():
            half[difference] = sum(values)
        return (
            sum(value * value for value in half),
            sum(abs(value) for value in half),
            half,
        )

    def negacyclic_product(left: list[int], right: list[int]) -> list[int]:
        result = [0] * 128
        left_support = [(index, value) for index, value in enumerate(left) if value]
        right_support = [(index, value) for index, value in enumerate(right) if value]
        for left_index, left_value in left_support:
            for right_index, right_value in right_support:
                quotient, residue = divmod(left_index + right_index, 128)
                result[residue] += (
                    -1 if quotient % 2 else 1
                ) * left_value * right_value
        return result

    def endpoint_metrics(
        coefficients: dict[int, int], half: list[int]
    ) -> tuple[int, float]:
        autocorrelation = [0] * 128
        for difference in range(1, 64):
            autocorrelation[difference] = half[difference]
            autocorrelation[128 - difference] = -half[difference]
        square = negacyclic_product(autocorrelation, autocorrelation)
        cube = negacyclic_product(square, autocorrelation)
        maximum_y = 0.0
        for unit in range(1, 256, 2):
            zeta = cmath.exp(2j * math.pi * unit / 256)
            value = sum(
                coefficient * zeta**exponent
                for exponent, coefficient in coefficients.items()
            )
            maximum_y = max(maximum_y, abs(value) ** 2)
        return cube[0], maximum_y

    def base_score(coefficients: dict[int, int]) -> tuple[int, int, list[int]]:
        energy, l1_norm, half = ledger(coefficients)
        return abs(energy - 42) + 2 * abs(l1_norm - 24), energy, half

    best: dict[str, object] | None = None
    target_visits = 0
    iterations = 0
    current: dict[int, int] | None = None
    current_scalar = float("inf")

    while time.monotonic() - started < deadline:
        if current is None or rng.random() < 0.002:
            positions = rng.sample(range(128), 7)
            values = [2, 2, 2, 1, 1, 1, 1]
            rng.shuffle(values)
            current = {
                position: value * rng.choice((-1, 1))
                for position, value in zip(positions, values)
            }
            penalty, _, half = base_score(current)
            objective = 0.0
            if penalty == 0:
                third_moment, maximum_y = endpoint_metrics(current, half)
                objective = (
                    float(third_moment)
                    if mode == "third_moment"
                    else 100.0 * maximum_y
                )
            current_scalar = 10000.0 * penalty - objective

        proposal = dict(current)
        mutation = rng.randrange(3)
        support = list(proposal)
        if mutation == 0:
            source = rng.choice(support)
            target = rng.randrange(128)
            if target in proposal:
                continue
            proposal[target] = proposal.pop(source)
        elif mutation == 1:
            source = rng.choice(support)
            proposal[source] = -proposal[source]
        else:
            left, right = rng.sample(support, 2)
            proposal[left], proposal[right] = proposal[right], proposal[left]

        penalty, energy, half = base_score(proposal)
        objective = 0.0
        third_moment = None
        maximum_y = None
        if penalty == 0:
            target_visits += 1
            third_moment, maximum_y = endpoint_metrics(proposal, half)
            objective = (
                float(third_moment)
                if mode == "third_moment"
                else 100.0 * maximum_y
            )
            candidate = {
                "coefficients": sorted(proposal.items()),
                "energy": energy,
                "l1_norm": 24,
                "third_moment": third_moment,
                "maximum_y": maximum_y,
            }
            key = third_moment if mode == "third_moment" else maximum_y
            best_key = None if best is None else best[mode]
            if best_key is None or key > best_key:
                candidate[mode] = key
                best = candidate
        proposal_scalar = 10000.0 * penalty - objective
        temperature = 4.0
        if proposal_scalar <= current_scalar or rng.random() < math.exp(
            min(0.0, (current_scalar - proposal_scalar) / temperature)
        ):
            current = proposal
            current_scalar = proposal_scalar
        iterations += 1

    return {
        "complete": True,
        "seed": seed,
        "mode": mode,
        "iterations": iterations,
        "target_visits": target_visits,
        "best": best,
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }


@app.local_entrypoint()
def main(workers: int = 8) -> None:
    results = list(search.map(range(workers)))
    print("E1_N256_E42_MOMENT_PHASE_PROBE " + repr(results))
