#!/usr/bin/env python3
"""Test the missing-BE/CF endpoint-sum consistency over each cell-11 tower."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

import modal


DIRECTORY = Path(__file__).parent
CORE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_function_field_core.py"
)
TOWER = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_symmetric_tower_result.json"
)
OUTPUT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_colored_consistency_result.json"
)
REMOTE_CORE = "/root/cell11_core.py"

app = modal.App("rs-mca-positive-433-1b-o0b-cell11-colored-consistency")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(CORE, REMOTE_CORE)
)


def polynomial_coefficients(value):
    if value.is_zero():
        return []
    return [int(value[index]) for index in range(int(value.degree()) + 1)]


@app.function(image=image, cpu=1.0, memory=1024, timeout=120, max_containers=8)
def profile(tower_row):
    sys.path.insert(0, "/root")
    import cell11_core as core

    context = core.FunctionFieldContext(tower_row)
    epsilon_1, epsilon_2 = tower_row["epsilon"]
    common = core.cell11_common_data(
        context, epsilon_1, epsilon_2, tower_row["bc_sign"]
    )

    def determinant(matrix):
        size = len(matrix)
        states = {0: context._rf_one()}
        for row in range(size):
            updated = {}
            for mask, value in states.items():
                for column in range(size):
                    bit = 1 << column
                    if mask & bit:
                        continue
                    term = value * matrix[row][column]
                    if (mask >> (column + 1)).bit_count() % 2:
                        term = -term
                    target = mask | bit
                    updated[target] = (
                        updated.get(target, context._rf_zero()) + term
                    )
            states = updated
        return states[(1 << size) - 1]

    def evaluate(polynomial, x_value):
        if polynomial.is_zero():
            return 0
        output = 0
        for degree in range(int(polynomial.degree()), -1, -1):
            output = (
                output * x_value + int(polynomial[degree])
            ) % core.PRIME
        return output

    def normalize(polynomial):
        if polynomial.is_zero():
            return polynomial
        scale = pow(
            int(polynomial[polynomial.degree()]) % core.PRIME,
            -1,
            core.PRIME,
        )
        return polynomial * scale

    rows = []
    for missing_record, base in (("BE", context.b), ("CF", context.c)):
        endpoint = common["missing_product"] / base
        consistency = (
            (base + endpoint) ** 2 - common["missing_sum_squared"]
        )
        determinant_value = determinant(consistency.multiplication_matrix())
        numerator = determinant_value.numer
        denominator = determinant_value.denom
        witness_x = next(
            (
                x_value
                for x_value in range(2, 130)
                if evaluate(denominator, x_value) != 0
                and evaluate(numerator, x_value) != 0
            ),
            None,
        )
        normalized_numerator = normalize(numerator)
        normalized = polynomial_coefficients(normalized_numerator)
        roots = []
        if not normalized_numerator.is_zero():
            for root_value, multiplicity in normalized_numerator.roots():
                root = int(root_value) % core.PRIME
                roots.append({
                    "x": root,
                    "multiplicity": int(multiplicity),
                    "construction_guards_nonzero": all(
                        evaluate(guard, root) != 0 for guard in context.guards
                    ),
                })
        non_guard_roots = [
            row for row in roots if row["construction_guards_nonzero"]
        ]
        rows.append({
            "missing_record": missing_record,
            "algebra_dimension": context.dimension,
            "consistency_identity": consistency.is_zero(),
            "determinant_zero": determinant_value.is_zero(),
            "determinant_numerator_degree": (
                -1 if numerator.is_zero() else int(numerator.degree())
            ),
            "determinant_denominator_degree": int(denominator.degree()),
            "determinant_numerator_sha256": hashlib.sha256(
                json.dumps(normalized, separators=(",", ":")).encode()
            ).hexdigest(),
            "base_field_roots": roots,
            "non_guard_base_field_roots": non_guard_roots,
            "witness_x": witness_x,
            "witness_value": (
                None if witness_x is None else (
                    evaluate(numerator, witness_x)
                    * pow(evaluate(denominator, witness_x), -1, core.PRIME)
                    % core.PRIME
                )
            ),
            "status": (
                "DEPLOYED_POINTWISE_BOUNDARY"
                if non_guard_roots
                else "DEPLOYED_OFF_GUARD_UNIT"
                if witness_x is not None
                else "UNRESOLVED"
            ),
        })
    return {
        "bc_sign": tower_row["bc_sign"],
        "epsilon": tower_row["epsilon"],
        "tower_program_sha256": tower_row["program_sha256"],
        "tower_valid": all(context.validate_tower()),
        "rows": rows,
    }


@app.local_entrypoint()
def main():
    tower = json.loads(TOWER.read_text())
    rows = list(profile.map(tower["rows"], order_outputs=True))
    statuses = Counter(
        row["status"] for tower_row in rows for row in tower_row["rows"]
    )
    non_guard_roots = [
        root["x"]
        for tower_row in rows
        for row in tower_row["rows"]
        for root in row["non_guard_base_field_roots"]
    ]
    output = {
        "schema": "kb-positive-433-1b-o0b-cell11-colored-consistency-v1",
        "statement": (
            "Exact generic unit test for the necessary missing-BE/CF "
            "endpoint product/squared-sum consistency identities."
        ),
        "source_tower_count": len(rows),
        "case_count": sum(len(row["rows"]) for row in rows),
        "status_counts": dict(sorted(statuses.items())),
        "non_guard_root_occurrences": len(non_guard_roots),
        "distinct_non_guard_root_count": len(set(non_guard_roots)),
        "rows": rows,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "output": str(OUTPUT),
        "source_tower_count": output["source_tower_count"],
        "case_count": output["case_count"],
        "status_counts": output["status_counts"],
        "non_guard_root_occurrences": output["non_guard_root_occurrences"],
        "distinct_non_guard_root_count": output["distinct_non_guard_root_count"],
    }, sort_keys=True))
