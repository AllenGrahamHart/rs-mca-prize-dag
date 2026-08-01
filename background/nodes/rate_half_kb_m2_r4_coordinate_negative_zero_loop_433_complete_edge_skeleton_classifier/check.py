#!/usr/bin/env python3
"""Independent direct checks for the zero-loop 433 skeleton census."""

import importlib.util
import itertools
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_zero_loop_433_outside_skeleton_census.py"
)


def main():
    specification = importlib.util.spec_from_file_location("census", SCRIPT)
    census = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(census)
    solutions, orbits = census.verify()
    for colored, loops, multiplicities in solutions:
        de, df, ef = multiplicities
        degrees = (
            2 * loops[0] + de + df,
            2 * loops[1] + de + ef,
            2 * loops[2] + df + ef,
        )
        if sum(colored) != 2 or sum(loops) > 2:
            raise RuntimeError("budget")
        if sum(loops) + sum(multiplicities) != 5:
            raise RuntimeError("internal count")
        if degrees != tuple(4 - value for value in colored):
            raise RuntimeError("degree")
    covered = set()
    for representative, size in orbits:
        orbit = {
            census.permute(representative, permutation)
            for permutation in itertools.permutations(range(3))
        }
        if len(orbit) != size or covered & orbit:
            raise RuntimeError("orbit partition")
        covered |= orbit
    if covered != set(solutions):
        raise RuntimeError("coverage")
    print("RATE_HALF_KB_ZERO_LOOP_433_OUTSIDE_SKELETON_CHECK_PASS cells=21")


if __name__ == "__main__":
    main()
