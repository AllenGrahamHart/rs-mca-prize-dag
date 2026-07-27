#!/usr/bin/env python3
"""Search actual E=38,L=22 seven-term vectors for large third moment."""

from __future__ import annotations

import modal


app = modal.App("e1-n256-e38-geometric-moment-probe")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=1.0, memory=256, timeout=30)
def search(seed: int) -> dict[str, object]:
    import math
    import random
    import time
    from collections import defaultdict

    started = time.monotonic()
    deadline = 15.0
    generator = random.Random(0xE138220 + seed)

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
                result[residue] += (-1 if quotient % 2 else 1) * left_value * right_value
        return result

    def metrics(coefficients: dict[int, int]) -> tuple[int, int, int]:
        energy, l1_norm, half = ledger(coefficients)
        autocorrelation = [0] * 128
        for difference in range(1, 64):
            autocorrelation[difference] = half[difference]
            autocorrelation[128 - difference] = -half[difference]
        square = negacyclic_product(autocorrelation, autocorrelation)
        cube = negacyclic_product(square, autocorrelation)
        return energy, l1_norm, cube[0]

    best: dict[str, object] | None = None
    target_visits = 0
    iterations = 0
    current: dict[int, int] | None = None
    current_scalar = float("inf")

    while time.monotonic() - started < deadline:
        if current is None or generator.random() < 0.002:
            positions = generator.sample(range(128), 7)
            values = [2, 2, 2, 1, 1, 1, 1]
            generator.shuffle(values)
            current = {
                position: value * generator.choice((-1, 1))
                for position, value in zip(positions, values)
            }
            energy, l1_norm, third_moment = metrics(current)
            penalty = abs(energy - 38) + 2 * abs(l1_norm - 22)
            current_scalar = 10000.0 * penalty - float(third_moment)

        proposal = dict(current)
        mutation = generator.randrange(3)
        support = list(proposal)
        if mutation == 0:
            source = generator.choice(support)
            target = generator.randrange(128)
            if target in proposal:
                continue
            proposal[target] = proposal.pop(source)
        elif mutation == 1:
            source = generator.choice(support)
            proposal[source] = -proposal[source]
        else:
            left, right = generator.sample(support, 2)
            proposal[left], proposal[right] = proposal[right], proposal[left]

        energy, l1_norm, third_moment = metrics(proposal)
        penalty = abs(energy - 38) + 2 * abs(l1_norm - 22)
        if penalty == 0:
            target_visits += 1
            candidate = {
                "coefficients": sorted(proposal.items()),
                "third_moment": third_moment,
            }
            if best is None or third_moment > best["third_moment"]:
                best = candidate
        proposal_scalar = 10000.0 * penalty - float(third_moment)
        if proposal_scalar <= current_scalar or generator.random() < math.exp(
            min(0.0, (current_scalar - proposal_scalar) / 4.0)
        ):
            current = proposal
            current_scalar = proposal_scalar
        iterations += 1

    return {
        "complete": True,
        "seed": seed,
        "iterations": iterations,
        "target_visits": target_visits,
        "best": best,
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }


@app.local_entrypoint()
def main(workers: int = 8) -> None:
    print("E1_N256_E38_GEOMETRIC_MOMENT_PROBE " + repr(list(search.map(range(workers)))))
