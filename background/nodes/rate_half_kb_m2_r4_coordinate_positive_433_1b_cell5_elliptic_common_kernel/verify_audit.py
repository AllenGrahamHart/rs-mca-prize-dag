#!/usr/bin/env python3
"""Independent algebra audit for the cell-5 common kernel."""

import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
COMMON = EXP / "rate_half_kb_positive_433_1b_common_vieta_compiler.py"
STRUCTURE = EXP / "rate_half_kb_positive_433_1b_cell5_complete_pivot_scout_result.json"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell5_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
P = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_common():
    spec = importlib.util.spec_from_file_location("cell5_common", COMMON)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    structure = json.loads(STRUCTURE.read_text())
    require(len(structure["rows"]) == 24, "structure count")
    for signs in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        rows = [row for row in structure["rows"] if row["epsilon"] == list(signs)]
        require(len(rows) == 6
                and len({tuple(item["sha256"] for item in row["lex_basis"])
                         for row in rows}) == 1,
                "chart signature")

    tower = json.loads(TOWER.read_text())
    for row in tower["rows"]:
        if row["c_row_index"] != 6:
            continue
        t, r = sp.symbols("t r")
        base = sp.Poly(sp.sympify(row["base"]["expression"]), t, r, modulus=P)
        direct = sp.Poly(sp.discriminant(base.as_expr(), t), r, modulus=P)
        require(hashlib.sha256(str(direct.as_expr()).encode()).hexdigest()
                == row["base_discriminant"]["sha256"],
                "direct discriminant digest")
        factors = [sp.Poly(sp.sympify(item["expression"]), r, modulus=P)
                   for item in row["base_discriminant_factors"]["factors"]]
        quartic = next(value for value in factors if value.degree() == 4)
        require(sp.gcd(quartic, quartic.diff()).degree() == 0
                and row["b_boundary_unit"] and row["c_boundary_unit"],
                "boundary-free square-free tower")

    common = load_common()
    kernel_payload = json.loads(KERNEL.read_text())
    mutated_failure = False
    for row in kernel_payload["rows"]:
        signs = tuple(row["epsilon"])
        variables, _, metadata = common.compile_cell(5, *signs)
        values = [sp.sympify(item["expression"]) for item in row["kernel"]]
        product_rows = [
            [-product, -product * label, -product * label**2,
             1, label, label**2, 0, 0]
            for label, product in zip(metadata["labels"], metadata["products"])
        ]
        sum_rows = [
            [q_value, q_value * label, q_value * label**2,
             0, 0, 0, label, label**2]
            for label, q_value in zip(metadata["labels"], metadata["q_values"])
        ]
        identities = []
        for source_row in [*product_rows, *sum_rows]:
            dot = sum(left * right for left, right in zip(source_row, values))
            identities.append(sp.Poly(dot, *variables, modulus=P).is_zero)
        require(identities == [True] * 7 + [False] * 3,
                "formal identity reconstruction")
        if signs == (-1, -1):
            changed = list(values)
            changed[0] += 1
            dot = sum(left * right for left, right in zip(product_rows[0], changed))
            mutated_failure = not sp.Poly(dot, *variables, modulus=P).is_zero
    require(mutated_failure, "kernel mutation test")
    print("PASS cell-5 common-kernel audit: charts=24 formal=28 mutation=1/1")


if __name__ == "__main__":
    main()
