#!/usr/bin/env python3
"""Replay the cell-11 selected product-rank cofactor boundary."""

from collections import Counter
import ast
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
INPUT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_principal_input_result.json"
)
OUTPUT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_selected_cofactor_boundary_result.json"
)
REMOTE_CORE = "/root/cell11_core.py"
REMOTE_INPUT = "/root/input.json"

app = modal.App("rs-mca-positive-433-1b-o0b-cell11-selected-boundary")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(CORE, REMOTE_CORE)
    .add_local_file(INPUT, REMOTE_INPUT)
)


def polynomial_coefficients(value):
    if value.is_zero():
        return []
    return [int(value[index]) for index in range(int(value.degree()) + 1)]


def polynomial_sha256(value):
    return hashlib.sha256(
        json.dumps(
            polynomial_coefficients(value), separators=(",", ":")
        ).encode()
    ).hexdigest()


@app.function(image=image, cpu=1.0, memory=1024, timeout=120, max_containers=8)
def profile(tower_row):
    sys.path.insert(0, "/root")
    import cell11_core as core

    context = core.FunctionFieldContext(tower_row)
    pre_cofactor_guards = tuple(context.guards)
    epsilon_1, epsilon_2 = tower_row["epsilon"]
    input_payload = json.loads(Path(REMOTE_INPUT).read_text())
    input_common = next(
        row for row in input_payload["common_rows"]
        if row["epsilon"] == tower_row["epsilon"]
        and row["bc_sign"] == tower_row["bc_sign"]
    )
    input_product = next(
        row for row in input_payload["product_rows"]
        if row["bc_sign"] == tower_row["bc_sign"]
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
        scale = pow(
            int(polynomial[polynomial.degree()]) % core.PRIME,
            -1,
            core.PRIME,
        )
        return polynomial * scale

    def rational_at(value, x_value):
        numerator = evaluate(value.numer, x_value)
        denominator = evaluate(value.denom, x_value)
        if denominator == 0:
            raise ZeroDivisionError("specialized rational denominator")
        return numerator * pow(denominator, -1, core.PRIME) % core.PRIME

    def element_at(value, x_value, y_value, r_value):
        output = 0
        for index, coefficient in enumerate(value.values):
            r_degree, y_degree = divmod(index, context.y_degree)
            output = (
                output
                + rational_at(coefficient, x_value)
                * pow(r_value, r_degree, core.PRIME)
                * pow(y_value, y_degree, core.PRIME)
            ) % core.PRIME
        return output

    def expression_at(text, values):
        tree = ast.parse(text, mode="eval")

        def visit(node):
            if isinstance(node, ast.Expression):
                return visit(node.body)
            if isinstance(node, ast.Constant) and isinstance(node.value, int):
                return node.value % core.PRIME
            if isinstance(node, ast.Name) and node.id in values:
                return values[node.id]
            if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
                return -visit(node.operand) % core.PRIME
            if isinstance(node, ast.BinOp):
                left, right = visit(node.left), visit(node.right)
                if isinstance(node.op, ast.Add):
                    return (left + right) % core.PRIME
                if isinstance(node.op, ast.Sub):
                    return (left - right) % core.PRIME
                if isinstance(node.op, ast.Mult):
                    return left * right % core.PRIME
                if isinstance(node.op, ast.Pow):
                    return pow(left, right, core.PRIME)
            raise ValueError(f"unsupported expression node: {ast.dump(node)}")

        return visit(tree)

    def expression_in_algebra(text):
        tree = ast.parse(text, mode="eval")
        values = {
            "b": context.b,
            "c": context.c,
            "r": context.r,
            "t": epsilon_1 * epsilon_2 * context.r**2,
        }

        def visit(node):
            if isinstance(node, ast.Expression):
                return visit(node.body)
            if isinstance(node, ast.Constant) and isinstance(node.value, int):
                return context.constant(node.value)
            if isinstance(node, ast.Name) and node.id in values:
                return values[node.id]
            if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
                return -visit(node.operand)
            if isinstance(node, ast.BinOp):
                left = visit(node.left)
                if isinstance(node.op, ast.Add):
                    return left + visit(node.right)
                if isinstance(node.op, ast.Sub):
                    return left - visit(node.right)
                if isinstance(node.op, ast.Mult):
                    return left * visit(node.right)
                if (
                    isinstance(node.op, ast.Pow)
                    and isinstance(node.right, ast.Constant)
                    and isinstance(node.right.value, int)
                    and node.right.value >= 0
                ):
                    return left**node.right.value
            raise ValueError(f"unsupported algebra node: {ast.dump(node)}")

        return visit(tree)

    selected_cofactor = expression_in_algebra(input_product["rank_minor"])
    norm = determinant(selected_cofactor.multiplication_matrix())
    if norm.is_zero():
        raise ValueError("selected cofactor norm is zero")
    numerator = normalize(norm.numer)
    denominator = normalize(norm.denom)
    roots = []
    for root_value, multiplicity in numerator.roots():
        root = int(root_value) % core.PRIME
        zero_guard_indices = [
            index for index, guard in enumerate(pre_cofactor_guards)
            if evaluate(guard, root) == 0
        ]
        roots.append({
            "x": root,
            "multiplicity": int(multiplicity),
            "zero_guard_indices": zero_guard_indices,
            "pre_cofactor_guards_nonzero": not zero_guard_indices,
        })
    _, factors = numerator.factor()
    factorization = [{
        "degree": int(factor.degree()),
        "multiplicity": int(multiplicity),
        "sha256": polynomial_sha256(factor),
    } for factor, multiplicity in factors]
    off_chart_roots = [
        row for row in roots if not row["pre_cofactor_guards_nonzero"]
    ]
    deployed_boundary_roots = [
        row for row in roots if row["pre_cofactor_guards_nonzero"]
    ]
    boundary_points = []
    root_fiber_census = []
    for root in deployed_boundary_roots:
        x_value = root["x"]
        y_coefficients = [
            -rational_at(value, x_value) % core.PRIME
            for value in context.y_relation
        ] + [1]
        y_roots = [
            int(value) % core.PRIME
            for value, _ in context.polynomial_context(y_coefficients).roots()
        ]
        source_candidates = 0
        boundary_candidates = 0
        for y_value in y_roots:
            r_linear = sum(
                rational_at(value, x_value) * pow(y_value, degree, core.PRIME)
                for degree, value in enumerate(context.r_linear)
            ) % core.PRIME
            r_constant = sum(
                rational_at(value, x_value) * pow(y_value, degree, core.PRIME)
                for degree, value in enumerate(context.r_constant)
            ) % core.PRIME
            r_polynomial = context.polynomial_context([
                -r_constant % core.PRIME, -r_linear % core.PRIME, 1
            ])
            for r_root, _ in r_polynomial.roots():
                source_candidates += 1
                r_value = int(r_root) % core.PRIME
                if element_at(
                    selected_cofactor, x_value, y_value, r_value
                ) != 0:
                    continue
                boundary_candidates += 1
                b_value = element_at(context.b, x_value, y_value, r_value)
                c_value = element_at(context.c, x_value, y_value, r_value)
                t_value = (
                    epsilon_1 * epsilon_2 * r_value * r_value
                ) % core.PRIME
                values = {
                    "b": b_value, "c": c_value, "r": r_value,
                    "t": t_value,
                }
                equation_values = [
                    expression_at(text, values)
                    for text in input_common["equations"]
                ]
                guard_value = expression_at(input_common["guard"], values)
                rank_minor_value = expression_at(
                    input_product["rank_minor"], values
                )
                point = {
                    "x": x_value,
                    "y": y_value,
                    "r": r_value,
                    "t": t_value,
                    "b": b_value,
                    "c": c_value,
                    "bc_matches_x": b_value * c_value % core.PRIME == x_value,
                    "common_equations_zero": all(value == 0 for value in equation_values),
                    "common_guard_nonzero": guard_value != 0,
                    "selected_rank_minor_zero": rank_minor_value == 0,
                }
                point["deployed"] = (
                    point["bc_matches_x"]
                    and point["common_equations_zero"]
                    and point["common_guard_nonzero"]
                    and point["selected_rank_minor_zero"]
                )
                boundary_points.append(point)
        root_fiber_census.append({
            "x": x_value,
            "y_root_count": len(y_roots),
            "source_candidate_count": source_candidates,
            "boundary_candidate_count": boundary_candidates,
        })
    return {
        "bc_sign": tower_row["bc_sign"],
        "epsilon": tower_row["epsilon"],
        "algebra_dimension": context.dimension,
        "tower_program_sha256": tower_row["program_sha256"],
        "tower_valid": all(context.validate_tower()),
        "pre_cofactor_guard_count": len(pre_cofactor_guards),
        "pre_cofactor_guard_sha256": [
            polynomial_sha256(guard) for guard in pre_cofactor_guards
        ],
        "selected_rank_minor_sha256": input_product["rank_minor_sha256"],
        "norm_numerator_degree": int(numerator.degree()),
        "norm_denominator_degree": int(denominator.degree()),
        "norm_numerator_sha256": polynomial_sha256(numerator),
        "norm_denominator_sha256": polynomial_sha256(denominator),
        "norm_numerator_factorization": factorization,
        "base_field_roots": roots,
        "off_chart_roots": off_chart_roots,
        "deployed_boundary_roots": deployed_boundary_roots,
        "root_fiber_census": root_fiber_census,
        "boundary_points": boundary_points,
        "field_boundary_point_count": sum(
            point["deployed"] for point in boundary_points
        ),
        "status": (
            "DEPLOYED_FIELD_BOUNDARY_PRESENT"
            if any(point["deployed"] for point in boundary_points)
            else "NO_DEPLOYED_FIELD_BOUNDARY_POINT"
        ),
    }


@app.local_entrypoint()
def main():
    tower = json.loads(TOWER.read_text())
    rows = list(profile.map(tower["rows"], order_outputs=True))
    statuses = Counter(row["status"] for row in rows)
    deployed_roots = [
        root["x"] for row in rows for root in row["deployed_boundary_roots"]
    ]
    boundary_points = [
        point for row in rows for point in row["boundary_points"]
        if point["deployed"]
    ]
    output = {
        "schema": "kb-positive-433-1b-o0b-cell11-selected-boundary-v1",
        "statement": (
            "Exact source-algebra norm roots of the selected product-rank "
            "cofactor, lifted and replayed against the original common "
            "equations and guard."
        ),
        "case_count": len(rows),
        "status_counts": dict(sorted(statuses.items())),
        "deployed_boundary_root_occurrences": len(deployed_roots),
        "distinct_deployed_boundary_root_count": len(set(deployed_roots)),
        "field_boundary_point_count": len(boundary_points),
        "rows": rows,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "output": str(OUTPUT),
        "case_count": output["case_count"],
        "status_counts": output["status_counts"],
        "deployed_boundary_root_occurrences": (
            output["deployed_boundary_root_occurrences"]
        ),
        "distinct_deployed_boundary_root_count": (
            output["distinct_deployed_boundary_root_count"]
        ),
        "field_boundary_point_count": output["field_boundary_point_count"],
    }, sort_keys=True))
