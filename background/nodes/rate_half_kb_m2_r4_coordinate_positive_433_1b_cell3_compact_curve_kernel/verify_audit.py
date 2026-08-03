#!/usr/bin/env python3
"""Independent audit of the cell-3 compact curve and kernel packet."""

import ast
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    structure_script = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_compact_structure_modal.py"
    profile_script = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_projection_profile_modal.py"
    kernel_script = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_compact_kernel_modal.py"
    structure = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell3_compact_structure_result.json").read_text())
    profile = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell3_projection_profile_result.json").read_text())
    kernel = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json").read_text())
    for script in (structure_script, profile_script, kernel_script):
        ast.parse(script.read_text())
    structure_text = structure_script.read_text()
    for snippet in (
        "base_rows = [*product_rows, sum_rows[1]]",
        "for index in (2, 3, 4)",
        "beta_saturation_stages",
        "ideal Jbeta=G,beta",
    ):
        require(snippet in structure_text, f"structure source {snippet}")
    require("polynomial.factor()" in profile_script.read_text() and
            "exact_reconstruction" in profile_script.read_text(),
            "profile source")
    kernel_text = kernel_script.read_text()
    for snippet in ("ab_scale", "gamma", "identically_zero", "reduce(v"):
        require(snippet in kernel_text, f"kernel source {snippet}")
    keys = {(*row["epsilon"], row["chart"]) for row in structure["rows"]}
    require(keys == set(itertools.product((-1, 1), (-1, 1), range(6))),
            "structure Cartesian cover")
    require(all(row["dimension"] == 1 and row["basis_size"] == 21 and
                row["beta_boundary_unit"] and
                row["beta_boundary_dimension"] == -1
                for row in structure["rows"]), "structure audit")
    require(len(profile["result"]["rows"]) == 4 and all(
        len(value["factorization"]["factors"]) == 1
        for row in profile["result"]["rows"]
        for value in row["projections"].values()
    ), "factor audit")
    require(len(kernel["rows"]) == 4 and all(
        row["all_rows_zero_mod_common"] and
        row["reduced_remainders"] == ["0"] * 10
        for row in kernel["rows"]
    ), "kernel audit")
    statement = (NODE / "statement.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    # Forced pin correction (wave-43 audit): the original pin required "FLINT"
    # in frontier.md, but the quotient-child commit legitimately rewrote the
    # frontier around the quadratic pair algebra. Pin the current route marker.
    require("does not exclude" in statement and
            "Do not scale" in frontier and
            "quadratic pair algebra" in frontier,
            "retained frontier")
    print("audit=ok charts=24 signs=4 beta_boundary=unit kernels=4")


if __name__ == "__main__":
    main()
