#!/usr/bin/env python3
"""Independent audit of the positive 433-1b cell-14 curve structure."""

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
    structure_script = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell14_kernel_structure_modal.py"
    curve_script = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell14_curve_kernel_modal.py"
    structure = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_kernel_structure_result.json").read_text())
    curve = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_curve_kernel_result.json").read_text())
    ast.parse(structure_script.read_text())
    ast.parse(curve_script.read_text())
    for snippet in ("base_rows = [*product_rows, sum_rows[1]]",
                    "for index in (2, 3, 4)",
                    "ideal Jt=G,dt", "ideal Jc=G,dc"):
        require(snippet in structure_script.read_text(), f"structure source {snippet}")
    for snippet in ("a_coefficients = interpolate", "b_coefficients = interpolate",
                    "row_checks", "relation_over_field"):
        require(snippet in curve_script.read_text(), f"kernel source {snippet}")
    keys = {(*row["epsilon"], row["chart"]) for row in structure["rows"]}
    require(keys == set(itertools.product((-1, 1), (-1, 1), range(6))),
            "structure Cartesian product")
    require(all(row["dimension"] == 1 and not row["unit"] and
                row["t_denominator_unit"] and
                row["c_exception_dimension"] == 0
                for row in structure["rows"]), "structure audit")
    require(len(curve["rows"]) == 4 and
            all(row["all_rows_zero"] and len(row["row_checks"]) == 10
                for row in curve["rows"]), "kernel audit")
    statement = (NODE / "statement.md").read_text()
    require("does not exclude" in statement and "zero-dimensional" in statement,
            "frontier retained")
    print("audit=ok charts=24 signs=4 dense_kernels=4 finite_exception=retained")


if __name__ == "__main__":
    main()
