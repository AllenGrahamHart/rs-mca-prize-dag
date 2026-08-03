#!/usr/bin/env python3
"""Independent audit for the cell-14 fixed-a rank-one chain exclusion."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_module(name, path):
    specification = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def main():
    compiler = (EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_flint_profile_modal.py").read_text()
    for snippet in (
        "u_exponent-v_exponent",
        "f_exponent+2*v_exponent",
        "constant*cutter_linear-linear*cutter_constant",
        "pow(parameter, PRIME, outer_polynomial)",
        "direct_outer_fiber",
        '"CLEARING_BOUNDARY"',
    ):
        require(snippet in compiler, f"compiler construction: {snippet}")

    process = subprocess.run(
        [sys.executable, str(EXPERIMENTS /
         "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_census.py")],
        cwd=ROOT, text=True, capture_output=True, check=True,
    )
    require('"status": "PASS"' in process.stdout, "census replay")

    payload = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_census_result.json").read_text())
    primary = load_module("primary", NODE / "verify.py")
    primary.verify_payload(payload)
    for field, value in (
        ("case_count", 431),
        ("root_count", 9455),
        ("direct_fiber_count", 8735),
        ("remaining_allmixed_case_count", 143),
    ):
        mutant = copy.deepcopy(payload)
        mutant[field] = value
        try:
            primary.verify_payload(mutant)
        except RuntimeError:
            pass
        else:
            raise RuntimeError(f"mutation survived: {field}")
    print("audit=ok cases=432 roots=9456 direct=8736 mutations=4")


if __name__ == "__main__":
    main()
