#!/usr/bin/env python3
"""Time-bounded falsifier for low-energy profile-(4,4) coefficient vectors."""

from __future__ import annotations

import argparse
import json
import math
import random
import time


LENGTH = 128


def energy(state: tuple[tuple[int, int], ...]) -> int:
    correlations = [0] * 64
    for index, (left, left_value) in enumerate(state):
        for right, right_value in state[index + 1 :]:
            delta = right - left
            if delta < 64:
                correlations[delta] += left_value * right_value
            elif delta > 64:
                correlations[128 - delta] -= left_value * right_value
    return sum(value * value for value in correlations)


def canonical_state(positions: list[int], values: list[int]) -> tuple[tuple[int, int], ...]:
    return tuple(sorted(zip(positions, values)))


def random_state(rng: random.Random) -> tuple[tuple[int, int], ...]:
    positions = rng.sample(range(LENGTH), 8)
    values = [2] * 4 + [1] * 4
    rng.shuffle(values)
    values = [value if rng.randrange(2) else -value for value in values]
    return canonical_state(positions, values)


def mutate(
    state: tuple[tuple[int, int], ...], rng: random.Random
) -> tuple[tuple[int, int], ...]:
    positions = [position for position, _ in state]
    values = [value for _, value in state]
    mutation = rng.randrange(4)
    if mutation == 0:
        index = rng.randrange(8)
        occupied = set(positions)
        occupied.remove(positions[index])
        while (candidate := rng.randrange(LENGTH)) in occupied:
            pass
        positions[index] = candidate
    elif mutation == 1:
        values[rng.randrange(8)] *= -1
    elif mutation == 2:
        left, right = rng.sample(range(8), 2)
        if abs(values[left]) != abs(values[right]):
            values[left], values[right] = values[right], values[left]
        else:
            values[left] *= -1
    else:
        shift = rng.randrange(1, LENGTH)
        moved = []
        for position, value in zip(positions, values):
            target = position + shift
            moved.append((target % LENGTH, value if target < LENGTH else -value))
        return tuple(sorted(moved))
    return canonical_state(positions, values)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=55.0)
    parser.add_argument("--seed", type=int, default=440020)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    started = time.monotonic()
    deadline = started + args.seconds
    best_energy = 10**9
    best_states: set[tuple[tuple[int, int], ...]] = set()
    trials = 0
    restarts = 0

    while time.monotonic() < deadline:
        current = random_state(rng)
        current_energy = energy(current)
        restarts += 1
        for step in range(1800):
            if (trials & 8191) == 0 and time.monotonic() >= deadline:
                break
            candidate = mutate(current, rng)
            candidate_energy = energy(candidate)
            temperature = max(0.35, 10.0 * (1.0 - step / 1800.0))
            delta = candidate_energy - current_energy
            if delta <= 0 or rng.random() < math.exp(-delta / temperature):
                current = candidate
                current_energy = candidate_energy
            trials += 1
            if current_energy < best_energy:
                best_energy = current_energy
                best_states = {current}
                print(
                    json.dumps(
                        {
                            "event": "best",
                            "energy": best_energy,
                            "state": current,
                            "trials": trials,
                            "seconds": round(time.monotonic() - started, 3),
                        },
                        separators=(",", ":"),
                    ),
                    flush=True,
                )
            elif current_energy == best_energy and len(best_states) < 32:
                best_states.add(current)

    print(
        json.dumps(
            {
                "event": "summary",
                "seed": args.seed,
                "seconds_requested": args.seconds,
                "seconds_used": round(time.monotonic() - started, 3),
                "trials": trials,
                "restarts": restarts,
                "best_energy": best_energy,
                "best_states": sorted(best_states),
            },
            separators=(",", ":"),
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
