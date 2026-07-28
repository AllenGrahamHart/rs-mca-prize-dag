#!/usr/bin/env python3
"""Short heuristic search for low-energy profile-(3,6) vectors on Modal."""

from __future__ import annotations

import math
import random

import modal


app = modal.App("e1-profile-36-low-energy-search")
image = modal.Image.debian_slim()


def energy(state: dict[int, int]) -> tuple[int, tuple[int, ...]]:
    autocorrelation = [0] * 64
    support = sorted(state)
    for left_index, left in enumerate(support):
        for right in support[left_index + 1 :]:
            delta = right - left
            product = state[left] * state[right]
            if delta < 64:
                autocorrelation[delta] += product
            elif delta > 64:
                autocorrelation[128 - delta] -= product
    return sum(value * value for value in autocorrelation[1:]), tuple(autocorrelation[1:])


def random_state(rng: random.Random) -> dict[int, int]:
    while True:
        positions = rng.sample(range(128), 9)
        values = [2, 2, 2, 1, 1, 1, 1, 1, 1]
        rng.shuffle(values)
        state = {
            position: value * rng.choice((-1, 1))
            for position, value in zip(positions, values)
        }
        if mu_one(state):
            return state


def mu_one(state: dict[int, int]) -> bool:
    singleton_exponents = [position for position, value in state.items() if abs(value) == 1]
    assert len(singleton_exponents) == 6
    return sum(singleton_exponents) % 2 == 1


def mutate(state: dict[int, int], rng: random.Random) -> dict[int, int]:
    candidate = dict(state)
    move = rng.randrange(4)
    positions = list(candidate)
    if move == 0:
        position = rng.choice(positions)
        candidate[position] *= -1
    elif move == 1:
        old = rng.choice(positions)
        empty = rng.choice([position for position in range(128) if position not in candidate])
        candidate[empty] = candidate.pop(old)
    elif move == 2:
        left, right = rng.sample(positions, 2)
        left_sign = 1 if candidate[left] > 0 else -1
        right_sign = 1 if candidate[right] > 0 else -1
        candidate[left], candidate[right] = left_sign * abs(candidate[right]), right_sign * abs(candidate[left])
    else:
        old = rng.choice(positions)
        step = rng.choice((-16, -8, -4, -2, -1, 1, 2, 4, 8, 16))
        new = (old + step) % 128
        if new not in candidate:
            candidate[new] = candidate.pop(old)
    return candidate


@app.function(image=image, cpu=1, memory=512, timeout=70, max_containers=16)
def search(seed: int) -> dict[str, object]:
    rng = random.Random(seed)
    best_energy = 10**9
    best_state: dict[int, int] = {}
    best_autocorrelation: tuple[int, ...] = ()
    iterations = 0
    for restart in range(80):
        state = random_state(rng)
        current, _ = energy(state)
        temperature = 20.0
        for _ in range(25000):
            iterations += 1
            candidate = mutate(state, rng)
            if not mu_one(candidate):
                continue
            candidate_energy, candidate_autocorrelation = energy(candidate)
            delta = candidate_energy - current
            if delta <= 0 or rng.random() < math.exp(-delta / temperature):
                state = candidate
                current = candidate_energy
            temperature = max(0.05, temperature * 0.99975)
            if candidate_energy < best_energy:
                best_energy = candidate_energy
                best_state = candidate
                best_autocorrelation = candidate_autocorrelation
                if best_energy <= 6:
                    return {
                        "seed": seed,
                        "energy": best_energy,
                        "variance": 2 * best_energy,
                        "state": sorted(best_state.items()),
                        "autocorrelation": best_autocorrelation,
                        "iterations": iterations,
                    }
    return {
        "seed": seed,
        "energy": best_energy,
        "variance": 2 * best_energy,
        "state": sorted(best_state.items()),
        "autocorrelation": best_autocorrelation,
        "iterations": iterations,
    }


@app.local_entrypoint()
def main(shards: int = 16) -> None:
    rows = list(search.map(range(shards)))
    rows.sort(key=lambda row: (int(row["energy"]), int(row["seed"])))
    for row in rows:
        print(row)
    best = rows[0]
    print(
        "E1_PROFILE_36_LOW_ENERGY_SEARCH_DONE "
        f"shards={shards} best_E={best['energy']} best_V={best['variance']}"
    )
