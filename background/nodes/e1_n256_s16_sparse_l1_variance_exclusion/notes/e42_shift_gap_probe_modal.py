#!/usr/bin/env python3
"""Minimize supported-shift autocorrelation gaps at E=42, L=24."""

from __future__ import annotations

import modal


app = modal.App("e1-n256-e42-shift-gap-probe")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=1.0, memory=256, timeout=20)
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
    profile_index, valuation = divmod(task, 6)
    profile = profiles[profile_index]
    shift = 1 << valuation
    magnitudes = []
    for value, count in zip((4, 3, 2, 1), profile):
        magnitudes.extend([value] * count)

    rng = random.Random(0xE142600 + task)
    started = time.monotonic()
    deadline = 5.0

    def gap(half: dict[int, int]) -> int:
        full = dict(half)
        full.update({128 - index: value for index, value in half.items()})
        correlation = sum(
            value * full.get((index + shift) % 128, 0)
            for index, value in full.items()
        )
        return 84 - correlation

    marked_value = rng.choice(magnitudes)
    remaining = list(magnitudes)
    remaining.remove(marked_value)
    positions = rng.sample([index for index in range(1, 64) if index != shift], len(remaining))
    rng.shuffle(remaining)
    current = {shift: marked_value, **dict(zip(positions, remaining))}
    current_gap = gap(current)
    best = dict(current)
    best_gap = current_gap
    iterations = 0

    while time.monotonic() - started < deadline:
        proposal = dict(current)
        mutation = rng.randrange(2)
        support = list(proposal)
        if mutation == 0:
            movable = [index for index in support if index != shift]
            source = rng.choice(movable)
            target = rng.randrange(1, 64)
            if target in proposal or target == shift:
                continue
            proposal[target] = proposal.pop(source)
        else:
            other = rng.choice([index for index in support if index != shift])
            proposal[shift], proposal[other] = proposal[other], proposal[shift]
        proposal_gap = gap(proposal)
        temperature = max(0.1, 8.0 * (1.0 - (time.monotonic() - started) / deadline))
        improvement = current_gap - proposal_gap
        if improvement >= 0 or rng.random() < math.exp(improvement / temperature):
            current = proposal
            current_gap = proposal_gap
        if proposal_gap < best_gap:
            best = proposal
            best_gap = proposal_gap
        iterations += 1

    return {
        "complete": True,
        "task": task,
        "profile_index": profile_index,
        "profile_n4_n3_n2_n1": profile,
        "shift": shift,
        "valuation": valuation,
        "iterations": iterations,
        "best_gap": best_gap,
        "marked_value": best[shift],
        "gap_beyond_forced_square": best_gap - best[shift] ** 2,
        "best_half_magnitudes": sorted(best.items()),
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }


@app.local_entrypoint()
def main() -> None:
    results = list(search.map(range(36)))
    print(
        "E1_N256_E42_SHIFT_GAP_PROBE "
        + repr(
            {
                "minimum": min(results, key=lambda result: result["best_gap"]),
                "minimum_beyond_forced": min(
                    results,
                    key=lambda result: result["gap_beyond_forced_square"],
                ),
                "results": results,
            }
        )
    )
