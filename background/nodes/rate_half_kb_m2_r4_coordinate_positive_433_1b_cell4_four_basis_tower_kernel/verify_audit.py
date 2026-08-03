#!/usr/bin/env python3
"""Independent audit of the cell-4 four-basis tower and kernel packet."""

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
    structure_script = EXPERIMENTS / (
        "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_modal.py"
    )
    kernel_script = EXPERIMENTS / (
        "rate_half_kb_positive_433_1b_cell4_compact_kernel_modal.py"
    )
    structure = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_result.json"
    ).read_text())
    kernel = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell4_compact_kernel_result.json"
    ).read_text())
    for script in (structure_script, kernel_script):
        ast.parse(script.read_text())

    structure_text = structure_script.read_text()
    for snippet in (
        "base_rows = [*product_rows, sum_rows[pivot]]",
        "ideal Jpivot=G,pivot_scale",
        "ideal Q=K[1],K[2],K[6]",
        "quotient_saturation_stages",
        "quotient_remainders == [\"0\"] * 9",
    ):
        require(snippet in structure_text, f"structure source {snippet}")
    kernel_text = kernel_script.read_text()
    for snippet in (
        "pivot_scale", "gamma", "identically_zero_rows", "reduce(v",
    ):
        require(snippet in kernel_text, f"kernel source {snippet}")

    expected = set(itertools.product((-1, 1), (-1, 1), range(6)))
    actual = {(*row["epsilon"], row["chart"]) for row in structure["rows"]}
    require(actual == expected and len(structure["rows"]) == 24,
            "structure Cartesian cover")
    require(all(
        row["cell"] == 4 and row["pivot"] == 1 and
        row["status"] == "COMPLETE" and row["dimension"] == 1 and
        row["basis_size"] == 16 and row["pivot_boundary_unit"] and
        row["quotient_exact"] and row["quotient_remainders"] == ["0"] * 9
        for row in structure["rows"]
    ), "structure audit")
    for signs in itertools.product((-1, 1), repeat=2):
        rows = [row for row in structure["rows"]
                if tuple(row["epsilon"]) == signs]
        require(len(rows) == 6 and len({
            tuple(value["sha256"] for value in row["lex_basis"])
            for row in rows
        }) == 1, f"chart invariance {signs}")

    require(len(kernel["rows"]) == 4 and all(
        row["status"] == "COMPLETE" and
        row["all_rows_zero_mod_common"] and
        row["reduced_remainders"] == ["0"] * 10
        for row in kernel["rows"]
    ), "kernel audit")
    require(len({
        tuple(value["sha256"] for value in row["kernel"])
        for row in kernel["rows"]
    }) == 1, "kernel sign invariance")

    statement = (NODE / "statement.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("Irreducibility of the second quadratic is not claimed" in statement,
            "irreducibility fence")
    require("Dimension one is not emptiness evidence" in audit and
            "Do not retry" in frontier and "four-basis" in frontier,
            "retained frontier")
    print("audit=ok charts=24 signs=4 quotient_rows=216 kernel_rows=40")


if __name__ == "__main__":
    main()
