#!/usr/bin/env python3
"""Case-split interface for the normalized loose affine-line target."""

from __future__ import annotations

import sympy as sp

from f3_h3_repeat_loose_collision_branch_parametrization import BRANCHES, D
from f3_h3_repeat_loose_collision_orbit_compiler import EXPECTED_ORBITS
from f3_h3_repeat_loose_lambda_slope_collisions import NONTRIVIAL_LAMBDA_COORDINATE


def check_case_split() -> None:
    orbit_union = frozenset().union(*EXPECTED_ORBITS)
    if orbit_union != NONTRIVIAL_LAMBDA_COORDINATE:
        raise AssertionError((orbit_union, NONTRIVIAL_LAMBDA_COORDINATE))
    if sorted(len(orbit) for orbit in EXPECTED_ORBITS) != [3, 6]:
        raise AssertionError(EXPECTED_ORBITS)
    branch_representatives = {data["representative"] for data in BRANCHES.values()}
    if not all(any(rep in orbit for orbit in EXPECTED_ORBITS) for rep in branch_representatives):
        raise AssertionError((branch_representatives, EXPECTED_ORBITS))


def main() -> None:
    print("h=3 repeat loose case-split interface")
    check_case_split()
    print("generic target: no lambda-coordinate divisor, hence nine distinct slopes")
    print("collision targets after S3 quotient:")
    for label, data in BRANCHES.items():
        representative = data["representative"]
        formula = sp.factor(data["b_formula"])
        print(f"  branch_{label}: representative={representative} b={formula}")
    print(f"shared denominator D={sp.factor(D)}")
    print("secondary subcells are the one-variable pullbacks inside branch_A and branch_B")
    print("H3_REPEAT_LOOSE_CASE_SPLIT_INTERFACE_PASS")


if __name__ == "__main__":
    main()
