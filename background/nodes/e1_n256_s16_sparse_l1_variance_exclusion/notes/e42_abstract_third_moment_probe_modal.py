#!/usr/bin/env python3
"""Maximize M3 over abstract integer autocorrelations with E=42, L=24."""

from __future__ import annotations

import modal


app = modal.App("e1-n256-e42-abstract-third-moment-probe")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=1.0, memory=256, timeout=30)
def search(task: int) -> dict[str, object]:
    import math
    import random
    import time

    profiles = []
    for count_4 in range(5):
        for count_3 in range(7):
            for count_2 in range(10):
                count_1 = 24 - 4 * count_4 - 3 * count_3 - 2 * count_2
                if count_1 < 0:
                    continue
                if (
                    16 * count_4
                    + 9 * count_3
                    + 4 * count_2
                    + count_1
                    == 42
                ):
                    profiles.append((count_4, count_3, count_2, count_1))
    profiles.sort()
    profile_index = task % len(profiles)
    replica = task // len(profiles)
    profile = profiles[profile_index]
    magnitudes = []
    for value, count in zip((4, 3, 2, 1), profile):
        magnitudes.extend([value] * count)

    rng = random.Random(0xE142A00 + task)
    started = time.monotonic()
    deadline = 10.0

    def third_moment(half: dict[int, int]) -> int:
        full = dict(half)
        full.update({128 - index: -value for index, value in half.items()})
        square: dict[int, int] = {}
        for left_index, left_value in full.items():
            for right_index, right_value in full.items():
                quotient, residue = divmod(left_index + right_index, 128)
                term = (-1 if quotient % 2 else 1) * left_value * right_value
                square[residue] = square.get(residue, 0) + term
        total = 0
        for left_index, left_value in square.items():
            for right_index, right_value in full.items():
                quotient, residue = divmod(left_index + right_index, 128)
                if residue == 0:
                    total += (-1 if quotient % 2 else 1) * left_value * right_value
        return total

    def absolute_correlation_gaps(half: dict[int, int]) -> dict[str, object]:
        absolute = {index: abs(value) for index, value in half.items()}
        absolute.update({128 - index: abs(value) for index, value in half.items()})
        energy = sum(value * value for value in absolute.values())
        rows = []
        for index, value in sorted(absolute.items()):
            correlation = sum(
                other_value * absolute.get((-index - other_index) % 128, 0)
                for other_index, other_value in absolute.items()
            )
            rows.append(
                {
                    "index": index,
                    "value": value,
                    "gap": energy - correlation,
                    "gap_beyond_forced": energy - correlation - value * value,
                }
            )
        return {
            "energy": energy,
            "minimum_gap_beyond_forced": min(
                row["gap_beyond_forced"] for row in rows
            ),
            "weighted_gap": sum(
                row["value"] * row["gap"] for row in rows
            ),
            "rows": rows,
        }

    positions = rng.sample(range(1, 64), len(magnitudes))
    values = [value * rng.choice((-1, 1)) for value in magnitudes]
    rng.shuffle(values)
    current = dict(zip(positions, values))
    current_moment = third_moment(current)
    best = dict(current)
    best_moment = current_moment
    iterations = 0

    while time.monotonic() - started < deadline:
        proposal = dict(current)
        mutation = rng.randrange(3)
        support = list(proposal)
        if mutation == 0:
            source = rng.choice(support)
            target = rng.randrange(1, 64)
            if target in proposal:
                continue
            proposal[target] = proposal.pop(source)
        elif mutation == 1:
            source = rng.choice(support)
            proposal[source] = -proposal[source]
        else:
            left, right = rng.sample(support, 2)
            proposal[left], proposal[right] = proposal[right], proposal[left]
        proposal_moment = third_moment(proposal)
        temperature = max(1.0, 80.0 * (1.0 - (time.monotonic() - started) / deadline))
        gain = proposal_moment - current_moment
        if gain >= 0 or rng.random() < math.exp(gain / temperature):
            current = proposal
            current_moment = proposal_moment
        if proposal_moment > best_moment:
            best = proposal
            best_moment = proposal_moment
        iterations += 1

    return {
        "complete": True,
        "task": task,
        "profile_index": profile_index,
        "replica": replica,
        "profile_n4_n3_n2_n1": profile,
        "iterations": iterations,
        "best_third_moment": best_moment,
        "best_half_autocorrelation": sorted(best.items()),
        "best_absolute_correlation_gaps": absolute_correlation_gaps(best),
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }


@app.local_entrypoint()
def main(replicas: int = 2) -> None:
    profile_count = 6
    results = list(search.map(range(profile_count * replicas)))
    print(
        "E1_N256_E42_ABSTRACT_THIRD_MOMENT_PROBE "
        + repr(
            {
                "profiles": profile_count,
                "replicas": replicas,
                "best": max(results, key=lambda result: result["best_third_moment"]),
                "results": results,
            }
        )
    )
