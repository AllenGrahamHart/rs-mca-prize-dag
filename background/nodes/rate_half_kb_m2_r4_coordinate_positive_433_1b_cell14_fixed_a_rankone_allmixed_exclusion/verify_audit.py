#!/usr/bin/env python3
"""Independent audit for the cell-14 all-mixed exclusion."""

import copy
import importlib.util
import json
from pathlib import Path


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
        "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_modal.py").read_text()
    for snippet in (
        "u_exponent-v_exponent",
        "f_exponent+2*v_exponent",
        "value/common_factor",
        "weighted_substitute",
        "polynomial_field_roots(common_f)",
        '"GUARDED_COUNTEREXAMPLE"',
    ):
        require(snippet in compiler, f"compiler construction: {snippet}")

    payload = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_census_result.json").read_text())
    primary = load_module("primary", NODE / "verify.py")
    primary.verify_payload(payload)
    for field, value in (
        ("case_count", 143),
        ("root_count", 2991),
        ("common_factor_root_count", 959),
        ("factor_weight_branch_count", 959),
        ("residual_outer_root_count", 1),
    ):
        mutant = copy.deepcopy(payload)
        mutant[field] = value
        try:
            primary.verify_payload(mutant)
        except RuntimeError:
            pass
        else:
            raise RuntimeError(f"mutation survived: {field}")
    print("audit=ok cases=144 roots=2992 factors=960 mutations=5")


if __name__ == "__main__":
    main()
