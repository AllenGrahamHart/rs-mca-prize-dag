#!/usr/bin/env python3
"""Mutation audit for the common root-sign symmetry quotient."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CHECKER = ROOT / (
    "experiments/prize_resolution/"
    "check_rate_half_kb_positive_433_1a_common_root_sign_symmetry.py"
)
SPEC = importlib.util.spec_from_file_location("symmetry_checker", CHECKER)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def main():
    MODULE.check_loop_paired_actions()
    MODULE.check_cell0_actions()
    MODULE.check_cell12_actions()
    orbits = MODULE.orbit_census()
    MODULE.require(len(orbits) == 10, "orbit count")
    MODULE.require(sum(len(orbit) for orbit in orbits) == 60, "orbit cover")
    MODULE.require(len({state for orbit in orbits for state in orbit}) == 60,
                   "orbit disjointness")
    print("positive 433-1a common sign symmetry audit verified states=60")


if __name__ == "__main__":
    main()
