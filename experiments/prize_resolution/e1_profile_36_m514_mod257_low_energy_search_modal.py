#!/usr/bin/env python3
"""Adversarially search the cofactor-514 congruence chamber."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import random
import time

import modal


app = modal.App("e1-profile-36-m514-mod257-low-energy-search")
image = modal.Image.debian_slim()

MODULUS = 257
GENERATOR = 3
TARGET_MU = 1
MAX_ENERGY = 17
HERE = Path(__file__).resolve()
ROOT = (
    Path("/repo")
    if Path("/repo").is_dir()
    else HERE.parents[2] if len(HERE.parents) > 2
    else Path("/")
)


def power_table() -> tuple[list[int], dict[int, tuple[int, int]]]:
    powers = [pow(GENERATOR, exponent, MODULUS) for exponent in range(128)]
    oriented: dict[int, tuple[int, int]] = {}
    for exponent, value in enumerate(powers):
        oriented[value] = (exponent, 1)
        oriented[-value % MODULUS] = (exponent, -1)
    assert len(oriented) == MODULUS - 1
    return powers, oriented


POWERS, ORIENTED_SINGLETON = power_table()


def root_multiplicity(state: dict[int, int]) -> int:
    singleton_exponents = [
        position for position, value in state.items() if abs(value) == 1
    ]
    assert len(singleton_exponents) == 6
    for derivative in range(16):
        parity = sum(
            (derivative & ~exponent) == 0 for exponent in singleton_exponents
        ) % 2
        if parity:
            return derivative
    return 16


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
    return sum(value * value for value in autocorrelation[1:]), tuple(
        autocorrelation[1:]
    )


def complete_state(
    free_singletons: dict[int, int], heavies: dict[int, int]
) -> dict[int, int] | None:
    occupied = set(free_singletons) | set(heavies)
    residue = sum(
        coefficient * POWERS[position]
        for position, coefficient in free_singletons.items()
    )
    residue += sum(
        coefficient * POWERS[position] for position, coefficient in heavies.items()
    )
    target = -residue % MODULUS
    if target == 0:
        return None
    position, sign = ORIENTED_SINGLETON[target]
    if position in occupied:
        return None
    state = dict(free_singletons)
    state[position] = sign
    state.update(heavies)
    assert sum(
        coefficient * POWERS[position] for position, coefficient in state.items()
    ) % MODULUS == 0
    return state


def random_parameterization(
    rng: random.Random,
) -> tuple[dict[int, int], dict[int, int], dict[int, int]]:
    while True:
        positions = rng.sample(range(128), 8)
        free_singletons = {
            position: rng.choice((-1, 1)) for position in positions[:5]
        }
        heavies = {position: rng.choice((-2, 2)) for position in positions[5:]}
        state = complete_state(free_singletons, heavies)
        if state is not None and root_multiplicity(state) == TARGET_MU:
            return free_singletons, heavies, state


def reparameterize(
    state: dict[int, int], rng: random.Random
) -> tuple[dict[int, int], dict[int, int]]:
    singletons = [
        (position, value) for position, value in state.items() if abs(value) == 1
    ]
    omitted = rng.randrange(len(singletons))
    free_singletons = {
        position: value
        for index, (position, value) in enumerate(singletons)
        if index != omitted
    }
    heavies = {
        position: value for position, value in state.items() if abs(value) == 2
    }
    return free_singletons, heavies


def mutate(
    free_singletons: dict[int, int],
    heavies: dict[int, int],
    rng: random.Random,
) -> tuple[dict[int, int], dict[int, int]]:
    candidate_singletons = dict(free_singletons)
    candidate_heavies = dict(heavies)
    selected = (
        candidate_heavies if rng.random() < 3 / 8 else candidate_singletons
    )
    old = rng.choice(list(selected))
    coefficient = selected.pop(old)
    if rng.random() < 0.35:
        coefficient *= -1
    step = rng.choice((-32, -16, -8, -4, -2, -1, 1, 2, 4, 8, 16, 32))
    new = (old + step) % 128
    occupied = set(candidate_singletons) | set(candidate_heavies)
    if new in occupied:
        choices = [position for position in range(128) if position not in occupied]
        new = rng.choice(choices)
    selected[new] = coefficient
    return candidate_singletons, candidate_heavies


@app.function(image=image, cpu=1.0, memory=256, timeout=75, max_containers=64)
def search(seed: int, seconds: float) -> dict[str, object]:
    rng = random.Random(seed)
    deadline = time.monotonic() + seconds
    best_energy = 10**9
    best_state: dict[int, int] = {}
    best_autocorrelation: tuple[int, ...] = ()
    iterations = 0
    valid_mutations = 0
    restarts = 0

    while time.monotonic() < deadline:
        restarts += 1
        free_singletons, heavies, state = random_parameterization(rng)
        current_energy, _ = energy(state)
        temperature = 24.0
        for _ in range(20000):
            if time.monotonic() >= deadline:
                break
            iterations += 1
            candidate_singletons, candidate_heavies = mutate(
                free_singletons, heavies, rng
            )
            candidate = complete_state(candidate_singletons, candidate_heavies)
            if candidate is None or root_multiplicity(candidate) != TARGET_MU:
                continue
            valid_mutations += 1
            candidate_energy, candidate_autocorrelation = energy(candidate)
            delta = candidate_energy - current_energy
            if delta <= 0 or rng.random() < math.exp(-delta / temperature):
                free_singletons = candidate_singletons
                heavies = candidate_heavies
                state = candidate
                current_energy = candidate_energy
                if rng.random() < 0.08:
                    free_singletons, heavies = reparameterize(state, rng)
            temperature = max(0.08, temperature * 0.99965)
            if candidate_energy < best_energy:
                best_energy = candidate_energy
                best_state = candidate
                best_autocorrelation = candidate_autocorrelation
                if best_energy <= MAX_ENERGY:
                    return {
                        "seed": seed,
                        "found": True,
                        "energy": best_energy,
                        "variance": 2 * best_energy,
                        "state": sorted(best_state.items()),
                        "autocorrelation": best_autocorrelation,
                        "iterations": iterations,
                        "valid_mutations": valid_mutations,
                        "restarts": restarts,
                    }
    return {
        "seed": seed,
        "found": False,
        "energy": best_energy,
        "variance": 2 * best_energy,
        "state": sorted(best_state.items()),
        "autocorrelation": best_autocorrelation,
        "iterations": iterations,
        "valid_mutations": valid_mutations,
        "restarts": restarts,
    }


@app.local_entrypoint()
def main(
    shards: int = 16,
    seconds: float = 60.0,
    output: str = (
        "experiments/prize_resolution/"
        "e1_profile_36_m514_mod257_low_energy_search_result.json"
    ),
) -> None:
    rows = list(search.starmap((seed, seconds) for seed in range(shards)))
    rows.sort(key=lambda row: (int(row["energy"]), int(row["seed"])))
    payload = {
        "schema": "e1-profile-36-m514-mod257-low-energy-search-v1",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "shards": shards,
        "seconds": seconds,
        "rows": rows,
    }
    output_path = ROOT / output
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    for row in rows:
        print(row)
    found = sum(bool(row["found"]) for row in rows)
    total_iterations = sum(int(row["iterations"]) for row in rows)
    print(
        "E1_PROFILE_36_M514_MOD257_LOW_ENERGY_SEARCH_DONE "
        f"shards={shards} seconds={seconds} found={found} "
        f"best_E={rows[0]['energy']} iterations={total_iterations} output={output_path}"
    )
