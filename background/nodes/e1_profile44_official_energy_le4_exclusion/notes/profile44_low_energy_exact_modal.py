#!/usr/bin/env python3
"""Target energy one and compute the exact norm of an energy-two witness."""

from __future__ import annotations

import argparse
from itertools import combinations
import json
import math
import random
import time

import sympy as sp


ENERGY_TWO = (
    (48, 1),
    (49, -2),
    (50, -2),
    (51, -1),
    (111, -1),
    (112, 2),
    (113, -2),
    (114, -1),
)


def correlations(state: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    values = [0] * 64
    for index, (left, left_value) in enumerate(state):
        for right, right_value in state[index + 1 :]:
            delta = right - left
            if delta < 64:
                values[delta] += left_value * right_value
            elif delta > 64:
                values[128 - delta] -= left_value * right_value
    return tuple(values)


def parity_weight(support: tuple[int, ...]) -> int:
    mask = 0
    for left, right in combinations(support, 2):
        delta = (right - left) % 128
        if delta != 64:
            mask ^= 1 << min(delta, 128 - delta)
    return mask.bit_count()


def q1_supports() -> list[tuple[int, ...]]:
    return [
        (0,) + tail
        for tail in combinations(range(1, 128), 3)
        if parity_weight((0,) + tail) == 1
    ]


def random_q1_state(
    supports: list[tuple[int, ...]], rng: random.Random
) -> tuple[tuple[int, int], ...]:
    singles = list(rng.choice(supports))
    occupied = set(singles)
    doubles = []
    while len(doubles) < 4:
        position = rng.randrange(128)
        if position not in occupied:
            occupied.add(position)
            doubles.append(position)
    rows = [(position, rng.choice((-1, 1))) for position in singles]
    rows += [(position, rng.choice((-2, 2))) for position in doubles]
    return tuple(sorted(rows))


def mutate_doubles_and_signs(
    state: tuple[tuple[int, int], ...], rng: random.Random
) -> tuple[tuple[int, int], ...]:
    rows = list(state)
    if rng.randrange(3):
        choices = [index for index, (_, value) in enumerate(rows) if abs(value) == 2]
        index = rng.choice(choices)
        occupied = {position for position, _ in rows}
        while (position := rng.randrange(128)) in occupied:
            pass
        rows[index] = (position, rows[index][1])
    else:
        index = rng.randrange(8)
        rows[index] = (rows[index][0], -rows[index][1])
    return tuple(sorted(rows))


def targeted_search(seconds: float, seed: int) -> dict:
    rng = random.Random(seed)
    supports = q1_supports()
    started = time.monotonic()
    deadline = started + seconds
    best = 10**9
    best_state = None
    trials = 0
    restarts = 0
    while time.monotonic() < deadline:
        state = random_q1_state(supports, rng)
        value = sum(item * item for item in correlations(state))
        restarts += 1
        for step in range(1200):
            if (trials & 8191) == 0 and time.monotonic() >= deadline:
                break
            candidate = mutate_doubles_and_signs(state, rng)
            candidate_value = sum(item * item for item in correlations(candidate))
            temperature = max(0.2, 8.0 * (1.0 - step / 1200.0))
            delta = candidate_value - value
            if delta <= 0 or rng.random() < math.exp(-delta / temperature):
                state, value = candidate, candidate_value
            trials += 1
            if value < best:
                best, best_state = value, state
                print(
                    json.dumps(
                        {"event": "best", "energy": best, "state": state, "trials": trials},
                        separators=(",", ":"),
                    ),
                    flush=True,
                )
                if best == 1:
                    return {
                        "q1_supports": len(supports),
                        "trials": trials,
                        "restarts": restarts,
                        "best_energy": best,
                        "best_state": best_state,
                    }
    return {
        "q1_supports": len(supports),
        "trials": trials,
        "restarts": restarts,
        "best_energy": best,
        "best_state": best_state,
    }


def exact_energy_two() -> dict:
    x = sp.symbols("x")
    polynomial = sum(value * x**position for position, value in ENERGY_TWO)
    norm = abs(int(sp.resultant(x**128 + 1, polynomial, x)))
    corr = correlations(ENERGY_TWO)
    return {
        "state": ENERGY_TWO,
        "correlations": [(index, value) for index, value in enumerate(corr) if value],
        "energy": sum(value * value for value in corr),
        "factorization": str(sp.factor(polynomial)),
        "norm": str(norm),
        "norm_bits": norm.bit_length(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=55.0)
    parser.add_argument("--seed", type=int, default=440021)
    args = parser.parse_args()
    print(json.dumps({"event": "exact", **exact_energy_two()}, separators=(",", ":")), flush=True)
    print(
        json.dumps(
            {"event": "search_summary", **targeted_search(args.seconds, args.seed)},
            separators=(",", ":"),
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
