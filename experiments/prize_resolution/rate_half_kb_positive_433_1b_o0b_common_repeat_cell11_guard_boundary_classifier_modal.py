#!/usr/bin/env python3
"""Classify every registered cell-11 function-field guard boundary."""

from collections import Counter
import ast
import hashlib
import json
from pathlib import Path
import sys

import modal


DIRECTORY = Path(__file__).parent
PREFIX = "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_"
CORE = DIRECTORY / f"{PREFIX}function_field_core.py"
TOWER = DIRECTORY / f"{PREFIX}symmetric_tower_result.json"
INPUT = DIRECTORY / f"{PREFIX}principal_input_result.json"
PLUS = DIRECTORY / f"{PREFIX}uncolored_generic_rank_bcplus_result.json"
MINUS = DIRECTORY / f"{PREFIX}uncolored_generic_rank_bcminus_result.json"
OUTPUT = DIRECTORY / f"{PREFIX}guard_boundary_classifier_result.json"
REMOTE_CORE = "/root/cell11_core.py"
REMOTE_INPUT = "/root/input.json"

app = modal.App("rs-mca-positive-433-1b-o0b-cell11-guard-boundary")
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
        json.dumps(polynomial_coefficients(value), separators=(",", ":")).encode()
    ).hexdigest()


@app.function(image=image, cpu=1.0, memory=1024, timeout=120, max_containers=8)
def classify(case):
    tower_row, guard_atlas = case
    sys.path.insert(0, "/root")
    import cell11_core as core

    context = core.FunctionFieldContext(tower_row)
    tower_chart_guards = tuple(context.guards)
    input_payload = json.loads(Path(REMOTE_INPUT).read_text())
    input_common = next(
        row for row in input_payload["common_rows"]
        if row["epsilon"] == tower_row["epsilon"]
        and row["bc_sign"] == tower_row["bc_sign"]
    )
    epsilon_1, epsilon_2 = tower_row["epsilon"]

    def evaluate(polynomial, value):
        if polynomial.is_zero():
            return 0
        output = 0
        for degree in range(int(polynomial.degree()), -1, -1):
            output = (output * value + int(polynomial[degree])) % core.PRIME
        return output

    def normalize(polynomial):
        if polynomial.is_zero():
            raise ValueError("zero guard polynomial")
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
            raise ZeroDivisionError("tower rational denominator")
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
                left = visit(node.left)
                if isinstance(node.op, ast.Add):
                    return (left + visit(node.right)) % core.PRIME
                if isinstance(node.op, ast.Sub):
                    return (left - visit(node.right)) % core.PRIME
                if isinstance(node.op, ast.Mult):
                    return left * visit(node.right) % core.PRIME
                if (
                    isinstance(node.op, ast.Pow)
                    and isinstance(node.right, ast.Constant)
                    and isinstance(node.right.value, int)
                    and node.right.value >= 0
                ):
                    return pow(left, node.right.value, core.PRIME)
            raise ValueError(f"unsupported expression: {ast.dump(node)}")

        return visit(tree)

    guards = {}
    factors = {}
    root_to_guards = {}
    for digest, encoded in guard_atlas.items():
        coefficients = [int(value) for value in encoded.split(",")]
        polynomial = normalize(context.polynomial_context(coefficients))
        if polynomial_sha256(polynomial) != digest:
            raise ValueError("guard digest mismatch")
        guards[digest] = polynomial
        _, factorization = polynomial.factor()
        factor_rows = []
        for factor, multiplicity in factorization:
            factor = normalize(factor)
            factor_digest = polynomial_sha256(factor)
            roots = [
                int(root) % core.PRIME for root, _ in factor.roots()
            ]
            factor_rows.append({
                "degree": int(factor.degree()),
                "multiplicity": int(multiplicity),
                "sha256": factor_digest,
                "base_field_roots": sorted(roots),
            })
            factors[factor_digest] = factor_rows[-1]
            for root in roots:
                root_to_guards.setdefault(root, set()).add(digest)

    root_rows = []
    guarded_points = []
    for x_value in sorted(root_to_guards):
        zero_tower_guards = [
            polynomial_sha256(guard) for guard in tower_chart_guards
            if evaluate(guard, x_value) == 0
        ]
        root_row = {
            "x": x_value,
            "vanishing_guard_sha256": sorted(root_to_guards[x_value]),
            "zero_tower_guard_sha256": sorted(zero_tower_guards),
            "source_candidate_count": 0,
            "guarded_source_point_count": 0,
            "source_points": [],
        }
        if zero_tower_guards:
            root_row["status"] = "PROVED_TOWER_CHART_BOUNDARY"
            root_rows.append(root_row)
            continue

        y_coefficients = [
            -rational_at(value, x_value) % core.PRIME
            for value in context.y_relation
        ] + [1]
        y_roots = [
            int(value) % core.PRIME
            for value, _ in context.polynomial_context(y_coefficients).roots()
        ]
        root_row["y_root_count"] = len(y_roots)
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
                r_value = int(r_root) % core.PRIME
                root_row["source_candidate_count"] += 1
                b_value = element_at(context.b, x_value, y_value, r_value)
                c_value = element_at(context.c, x_value, y_value, r_value)
                t_value = epsilon_1 * epsilon_2 * r_value * r_value % core.PRIME
                values = {
                    "b": b_value,
                    "c": c_value,
                    "r": r_value,
                    "t": t_value,
                }
                equation_values = [
                    expression_at(text, values)
                    for text in input_common["equations"]
                ]
                guard_value = expression_at(input_common["guard"], values)
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
                }
                point["guarded"] = (
                    point["bc_matches_x"]
                    and point["common_equations_zero"]
                    and point["common_guard_nonzero"]
                )
                root_row["source_points"].append(point)
                if point["guarded"]:
                    guarded_points.append(point)
                    root_row["guarded_source_point_count"] += 1
        root_row["status"] = (
            "GUARDED_SOURCE_BOUNDARY_PRESENT"
            if root_row["guarded_source_point_count"]
            else "NO_GUARDED_SOURCE_BOUNDARY_POINT"
        )
        root_rows.append(root_row)

    return {
        "bc_sign": tower_row["bc_sign"],
        "epsilon": tower_row["epsilon"],
        "tower_valid": all(context.validate_tower()),
        "guard_count": len(guards),
        "factor_count": len(factors),
        "base_field_root_count": len(root_to_guards),
        "tower_boundary_root_count": sum(
            row["status"] == "PROVED_TOWER_CHART_BOUNDARY" for row in root_rows
        ),
        "guarded_source_point_count": len(guarded_points),
        "guard_factorizations": {
            digest: [
                row for row in (
                    {
                        "degree": int(normalize(factor).degree()),
                        "multiplicity": int(multiplicity),
                        "sha256": polynomial_sha256(normalize(factor)),
                        "base_field_roots": sorted(
                            int(root) % core.PRIME
                            for root, _ in normalize(factor).roots()
                        ),
                    }
                    for factor, multiplicity in polynomial.factor()[1]
                )
            ]
            for digest, polynomial in sorted(guards.items())
        },
        "root_rows": root_rows,
        "status": (
            "GUARDED_GUARD_BOUNDARY_PRESENT"
            if guarded_points
            else "NO_GUARDED_GUARD_BOUNDARY_POINT"
        ),
    }


@app.local_entrypoint()
def main():
    tower = json.loads(TOWER.read_text())
    payloads = {
        1: json.loads(PLUS.read_text()),
        -1: json.loads(MINUS.read_text()),
    }
    for sign, payload in payloads.items():
        if payload["bc_sign_filter"] != sign or not payload["complete_atlas"]:
            raise ValueError("generic-rank atlas scope mismatch")
    cases = tuple(
        (row, payloads[row["bc_sign"]]["guard_atlas"])
        for row in tower["rows"]
    )
    raw = list(classify.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            tower_row, _ = case
            rows.append({
                "bc_sign": tower_row["bc_sign"],
                "epsilon": tower_row["epsilon"],
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    statuses = Counter(row["status"] for row in rows)
    output = {
        "schema": "kb-positive-433-1b-o0b-cell11-guard-boundary-classifier-v1",
        "statement": (
            "Factor every registered function-field guard, lift every "
            "deployed root outside the proved tower boundary, and replay "
            "the original common equations and source guard."
        ),
        "case_count": len(rows),
        "status_counts": dict(sorted(statuses.items())),
        "guarded_source_point_count": sum(
            row.get("guarded_source_point_count", 0) for row in rows
        ),
        "rows": rows,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "output": str(OUTPUT),
        "case_count": output["case_count"],
        "status_counts": output["status_counts"],
        "guarded_source_point_count": output["guarded_source_point_count"],
        "row_summaries": [{
            "bc_sign": row["bc_sign"],
            "epsilon": row["epsilon"],
            "status": row["status"],
            "guard_count": row.get("guard_count"),
            "factor_count": row.get("factor_count"),
            "base_field_root_count": row.get("base_field_root_count"),
            "tower_boundary_root_count": row.get("tower_boundary_root_count"),
            "guarded_source_point_count": row.get("guarded_source_point_count"),
        } for row in rows],
    }, sort_keys=True))
