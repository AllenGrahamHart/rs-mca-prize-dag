#!/usr/bin/env python3
"""Search the joint all-singleton, low-energy, mod-257 gate on Modal."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import random
import time

import modal


app = modal.App("e1-profile018-m514-low-energy-root-search")
image = modal.Image.debian_slim()

MODULUS = 257
GENERATOR = 3
TERMS = 18
FREE_TERMS = TERMS - 1
MAX_ENERGY = 12
MAX_HITS = 64
EXCLUDED_MAGNITUDE_PROFILES = {(9, 1, 2, 0), (11, 7, 1, 0)}
HERE = Path(__file__).resolve()
ROOT = Path("/repo") if Path("/repo").is_dir() else HERE.parents[2]


def oriented_table() -> tuple[list[int], dict[int, tuple[int, int]]]:
    powers = [pow(GENERATOR, exponent, MODULUS) for exponent in range(128)]
    oriented: dict[int, tuple[int, int]] = {}
    for exponent, value in enumerate(powers):
        for sign in (-1, 1):
            residue = sign * value % MODULUS
            if residue in oriented:
                raise RuntimeError("oriented singleton table collision")
            oriented[residue] = (exponent, sign)
    if set(oriented) != set(range(1, MODULUS)):
        raise RuntimeError("oriented singleton table is not bijective")
    return powers, oriented


POWERS, ORIENTED = oriented_table()


def complete_state(free: dict[int, int]) -> dict[int, int] | None:
    if len(free) != FREE_TERMS:
        raise RuntimeError("free-state arity drift")
    residual = -sum(sign * POWERS[position] for position, sign in free.items()) % MODULUS
    if residual == 0:
        return None
    position, sign = ORIENTED[residual]
    if position in free:
        return None
    state = dict(free)
    state[position] = sign
    return state


def local_multiplicity_one(state: dict[int, int]) -> bool:
    return len(state) == TERMS and sum(state) % 2 == 1


def autocorrelation(state: dict[int, int]) -> tuple[int, ...]:
    values = [0] * 64
    support = sorted(state)
    for left_index, left in enumerate(support):
        for right in support[left_index + 1 :]:
            difference = right - left
            product = state[left] * state[right]
            if difference < 64:
                values[difference] += product
            elif difference > 64:
                values[128 - difference] -= product
    return tuple(values[1:])


def energy(state: dict[int, int]) -> tuple[int, tuple[int, ...]]:
    correlation = autocorrelation(state)
    return sum(value * value for value in correlation), correlation


def magnitude_profile(correlation: tuple[int, ...]) -> tuple[int, int, int, int]:
    energy_value = sum(value * value for value in correlation)
    return (
        energy_value,
        sum(abs(value) == 1 for value in correlation),
        sum(abs(value) == 2 for value in correlation),
        sum(abs(value) == 3 for value in correlation),
    )


def canonical(state: dict[int, int]) -> tuple[tuple[int, int], ...]:
    rows = []
    support = tuple(state)
    for origin in support:
        for unit in range(1, 256, 2):
            row = []
            for position, coefficient in state.items():
                image = unit * (position - origin) % 256
                sign = coefficient if image < 128 else -coefficient
                row.append((image % 128, sign))
            row.sort()
            packed = tuple(row)
            rows.append(packed)
            rows.append(tuple((position, -sign) for position, sign in packed))
    return min(rows)


def random_free(rng: random.Random) -> dict[int, int]:
    return {
        position: rng.choice((-1, 1))
        for position in rng.sample(range(128), FREE_TERMS)
    }


def initialize(rng: random.Random) -> tuple[dict[int, int], dict[int, int]]:
    while True:
        free = random_free(rng)
        state = complete_state(free)
        if state is not None and local_multiplicity_one(state):
            return free, state


def reparameterize(state: dict[int, int], rng: random.Random) -> dict[int, int]:
    omitted = rng.choice(tuple(state))
    return {position: sign for position, sign in state.items() if position != omitted}


def mutate(free: dict[int, int], rng: random.Random) -> dict[int, int]:
    candidate = dict(free)
    old_position = rng.choice(tuple(candidate))
    sign = candidate.pop(old_position)
    if rng.random() < 0.3:
        sign = -sign
    if rng.random() < 0.8:
        step = rng.choice((-32, -16, -8, -4, -2, -1, 1, 2, 4, 8, 16, 32))
        position = (old_position + step) % 128
    else:
        position = rng.randrange(128)
    if position in candidate:
        available = [value for value in range(128) if value not in candidate]
        position = rng.choice(available)
    candidate[position] = sign
    return candidate


@app.function(image=image, cpu=1.0, memory=256, timeout=70, max_containers=16)
def search(seed: int, seconds: float) -> dict[str, object]:
    rng = random.Random(seed)
    deadline = time.monotonic() + seconds
    free, state = initialize(rng)
    current_energy, current_correlation = energy(state)
    best_energy = current_energy
    best_state = state
    best_correlation = current_correlation
    hits: dict[tuple[tuple[int, int], ...], dict[str, object]] = {}
    iterations = 0
    valid = 0
    restarts = 0
    temperature = 48.0

    while time.monotonic() < deadline:
        iterations += 1
        candidate_free = mutate(free, rng)
        candidate = complete_state(candidate_free)
        if candidate is None or not local_multiplicity_one(candidate):
            continue
        valid += 1
        candidate_energy, candidate_correlation = energy(candidate)
        delta = candidate_energy - current_energy
        if delta <= 0 or rng.random() < math.exp(-delta / temperature):
            free = candidate_free
            state = candidate
            current_energy = candidate_energy
            current_correlation = candidate_correlation
            if rng.random() < 0.05:
                free = reparameterize(state, rng)
        temperature = max(0.05, temperature * 0.99985)

        if candidate_energy < best_energy:
            best_energy = candidate_energy
            best_state = candidate
            best_correlation = candidate_correlation
        if (
            candidate_energy <= MAX_ENERGY
            and magnitude_profile(candidate_correlation)
            not in EXCLUDED_MAGNITUDE_PROFILES
        ):
            key = canonical(candidate)
            hits.setdefault(
                key,
                {
                    "energy": candidate_energy,
                    "state": sorted(candidate.items()),
                    "autocorrelation": candidate_correlation,
                },
            )
            if len(hits) >= MAX_HITS:
                break
        if iterations % 25000 == 0 and temperature <= 0.051:
            restarts += 1
            free, state = initialize(rng)
            current_energy, current_correlation = energy(state)
            temperature = 48.0

    return {
        "seed": seed,
        "seconds": seconds,
        "iterations": iterations,
        "valid_mutations": valid,
        "restarts": restarts,
        "best_energy": best_energy,
        "best_state": sorted(best_state.items()),
        "best_autocorrelation": best_correlation,
        "hits": sorted(hits.values(), key=lambda row: (int(row["energy"]), row["state"])),
        "complete": time.monotonic() < deadline,
    }


@app.local_entrypoint()
def main(
    shards: int = 16,
    seconds: float = 55.0,
    output: str = (
        "experiments/prize_resolution/"
        "e1_profile018_m514_low_energy_root_search_result.json"
    ),
) -> None:
    rows = list(search.starmap((seed, seconds) for seed in range(shards)))
    canonical_hits: dict[tuple[tuple[int, int], ...], dict[str, object]] = {}
    for row in rows:
        for hit in row["hits"]:
            state = {int(position): int(sign) for position, sign in hit["state"]}
            canonical_hits.setdefault(canonical(state), hit)
    payload = {
        "schema": "e1-profile018-m514-low-energy-root-search-v1",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "excluded_magnitude_profiles": sorted(EXCLUDED_MAGNITUDE_PROFILES),
        "shards": shards,
        "seconds": seconds,
        "rows": rows,
        "canonical_hits": sorted(
            canonical_hits.values(),
            key=lambda row: (int(row["energy"]), row["state"]),
        ),
    }
    output_path = ROOT / output
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE018_M514_LOW_ENERGY_ROOT_SEARCH_DONE "
        f"shards={shards} seconds={seconds} "
        f"best_E={min(int(row['best_energy']) for row in rows)} "
        f"canonical_hits={len(canonical_hits)} output={output_path}"
    )
