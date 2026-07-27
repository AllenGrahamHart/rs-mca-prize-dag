#!/usr/bin/env python3
"""Search for geometric realizations of the relaxed E=42, L=24 endpoint."""

from __future__ import annotations

import modal


app = modal.App("e1-n256-e42-geometry-falsifier")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=1.0, memory=256, timeout=60)
def search(seed: int) -> dict[str, object]:
    import math
    import random
    import time
    from collections import defaultdict

    started = time.monotonic()
    deadline = 52.0
    rng = random.Random(0xE142000 + seed)

    def ledger(coefficients: dict[int, int]) -> tuple[int, int, int, int]:
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
        return energy, l1_norm, diameter_square_mass, cross_sum

    def score(coefficients: dict[int, int]) -> tuple[int, int, int]:
        energy, l1_norm, _, _ = ledger(coefficients)
        return (
            abs(energy - 42) + 2 * abs(l1_norm - 24),
            abs(energy - 42),
            abs(l1_norm - 24),
        )

    seed_geometry = {
        0: 2,
        16: -2,
        32: -1,
        48: 1,
        65: 1,
        80: -1,
        96: -2,
    }
    best = seed_geometry
    best_score = score(best)
    iterations = 0
    restarts = 0

    while time.monotonic() - started < deadline:
        if restarts % 3 == 0:
            current = dict(seed_geometry)
        else:
            positions = rng.sample(range(128), 7)
            values = [2, 2, 2, 1, 1, 1, 1]
            rng.shuffle(values)
            current = {
                position: value * rng.choice((-1, 1))
                for position, value in zip(positions, values)
            }
        current_score = score(current)

        for step in range(5000):
            if time.monotonic() - started >= deadline:
                break
            proposal = dict(current)
            mutation = rng.randrange(4)
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
            elif mutation == 2:
                left, right = rng.sample(support, 2)
                proposal[left], proposal[right] = proposal[right], proposal[left]
            else:
                shift = rng.randrange(1, 128)
                proposal = {
                    (position + shift) % 128: value
                    for position, value in proposal.items()
                }
                if len(proposal) != 7:
                    continue

            proposal_score = score(proposal)
            temperature = max(0.12, 4.0 * (1.0 - step / 5000))
            improvement = current_score[0] - proposal_score[0]
            if improvement >= 0 or rng.random() < math.exp(improvement / temperature):
                current = proposal
                current_score = proposal_score
            if proposal_score < best_score:
                best = proposal
                best_score = proposal_score
            iterations += 1
            if proposal_score == (0, 0, 0):
                energy, l1_norm, diameter, cross_sum = ledger(proposal)
                ordered_support = sorted(proposal)
                conductor_gcd = math.gcd(
                    256,
                    *(position - ordered_support[0] for position in ordered_support),
                )
                return {
                    "complete": True,
                    "found": True,
                    "seed": seed,
                    "iterations": iterations,
                    "coefficients": sorted(proposal.items()),
                    "energy": energy,
                    "variance": 2 * energy,
                    "l1_norm": l1_norm,
                    "diameter_square_mass": diameter,
                    "cross_sum": cross_sum,
                    "conductor_gcd": conductor_gcd,
                    "elapsed_seconds": round(time.monotonic() - started, 3),
                }
        restarts += 1

    energy, l1_norm, diameter, cross_sum = ledger(best)
    return {
        "complete": True,
        "found": False,
        "seed": seed,
        "iterations": iterations,
        "best_score": best_score,
        "best_coefficients": sorted(best.items()),
        "best_energy": energy,
        "best_l1_norm": l1_norm,
        "best_diameter_square_mass": diameter,
        "best_cross_sum": cross_sum,
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }


@app.local_entrypoint()
def main(workers: int = 16) -> None:
    results = list(search.map(range(workers)))
    hits = [result for result in results if result["found"]]
    print(
        "E1_N256_E42_GEOMETRY_FALSIFIER "
        + repr(
            {
                "workers": workers,
                "hit_count": len(hits),
                "hits": hits,
                "best": min(
                    results,
                    key=lambda result: tuple(result.get("best_score", (0, 0, 0))),
                ),
            }
        )
    )
