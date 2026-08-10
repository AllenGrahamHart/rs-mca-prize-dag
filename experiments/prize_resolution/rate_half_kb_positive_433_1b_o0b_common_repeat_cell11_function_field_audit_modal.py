#!/usr/bin/env python3
"""Audit quotient-algebra arithmetic and the cell-11 common kernel."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import time

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
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_function_field_audit_result.json"
)
REMOTE_CORE = "/root/cell11_core.py"
REMOTE_TOWER = "/root/tower.json"

app = modal.App("rs-mca-positive-433-1b-o0b-cell11-function-field-audit")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(CORE, REMOTE_CORE)
    .add_local_file(TOWER, REMOTE_TOWER)
)


def polynomial_coefficients(value):
    if value.is_zero():
        return []
    return [int(value[index]) for index in range(int(value.degree()) + 1)]


def element_digest(element):
    payload = [
        {
            "numer": polynomial_coefficients(value.numer),
            "denom": polynomial_coefficients(value.denom),
        }
        for value in element.values
    ]
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":")).encode()
    ).hexdigest()


def element_degrees(element):
    return {
        "numerator": max(
            (int(value.numer.degree()) for value in element.values
             if not value.numer.is_zero()), default=-1,
        ),
        "denominator": max(
            (int(value.denom.degree()) for value in element.values), default=-1,
        ),
    }


def element_payload(element):
    return [
        {
            "numer": polynomial_coefficients(value.numer),
            "denom": polynomial_coefficients(value.denom),
        }
        for value in element.values
    ]


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=8)
def audit(row):
    started = time.perf_counter()
    sys.path.insert(0, "/root")
    import cell11_core as core

    context = core.FunctionFieldContext(row)
    epsilon_1, epsilon_2 = row["epsilon"]
    data = core.cell11_common_data(
        context, epsilon_1, epsilon_2, row["bc_sign"]
    )
    tower_residuals = [
        context.evaluate_compact(value)
        for value in context.tower_polynomials
    ]
    lift_residual = context.evaluate_compact(
        context.lift_polynomial, "bryx", {"b": context.b}
    )
    tower_residuals.extend((
        lift_residual, context.b + context.c - context.y,
        context.b * context.c - context.x,
    ))
    tower_checks = tuple(value.is_zero() for value in tower_residuals)
    encoded_quadratic = context.r**2
    encoded_quadratic = encoded_quadratic - sum(
        (context.constant(value) * context.y**index * context.r
         for index, value in enumerate(context.r_linear)),
        context.zero(),
    )
    encoded_quadratic = encoded_quadratic - sum(
        (context.constant(value) * context.y**index
         for index, value in enumerate(context.r_constant)),
        context.zero(),
    )
    product_checks = tuple(value.is_zero() for value in data["product_checks"])
    sum_checks = tuple(value.is_zero() for value in data["sum_checks"])
    kernel_nonzero = tuple(
        not value.is_zero()
        for value in (*data["a_values"], *data["b_values"])
    )
    valid = (
        all(tower_checks) and all(product_checks) and all(sum_checks)
        and any(kernel_nonzero) and not data["missing_product"].is_zero()
    )
    unique_guards = {}
    for guard in context.guards:
        coefficients = polynomial_coefficients(guard)
        digest = hashlib.sha256(
            json.dumps(coefficients, separators=(",", ":")).encode()
        ).hexdigest()
        unique_guards[digest] = coefficients
    return {
        "epsilon": row["epsilon"], "bc_sign": row["bc_sign"],
        "status": "COMPLETE" if valid else "ERROR",
        "extension_degree": context.dimension,
        "tower_checks": list(tower_checks),
        "encoded_quadratic_zero": encoded_quadratic.is_zero(),
        "tower_residual_payloads": [
            None if value.is_zero() else element_payload(value)
            for value in tower_residuals
        ],
        "product_kernel_checks": list(product_checks),
        "sum_kernel_checks": list(sum_checks),
        "kernel_nonzero": list(kernel_nonzero),
        "b_sha256": element_digest(context.b),
        "c_sha256": element_digest(context.c),
        "missing_product_sha256": element_digest(data["missing_product"]),
        "missing_product_degrees": element_degrees(data["missing_product"]),
        "missing_sum_squared_sha256": element_digest(data["missing_sum_squared"]),
        "missing_sum_squared_degrees": element_degrees(data["missing_sum_squared"]),
        "construction_guards": {
            digest: ",".join(map(str, coefficients))
            for digest, coefficients in sorted(unique_guards.items())
        },
        "seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main():
    payload = json.loads(TOWER.read_text())
    cases = tuple(payload["rows"])
    raw = list(audit.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": case["epsilon"], "bc_sign": case["bc_sign"],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-o0b-common-repeat-"
            "cell11-function-field-audit-v1"
        ),
        "scope": (
            "Exact quotient-algebra replay of the symmetric towers, ordered "
            "b/c lift, product kernel, and all five common sum constraints."
        ),
        "core_sha256": hashlib.sha256(CORE.read_bytes()).hexdigest(),
        "tower_sha256": hashlib.sha256(TOWER.read_bytes()).hexdigest(),
        "status_counts": dict(sorted(Counter(
            row["status"] for row in rows
        ).items())),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT), "status_counts": output["status_counts"],
        "rows": [{
            "epsilon": row["epsilon"], "bc_sign": row["bc_sign"],
            "status": row["status"], "degree": row.get("extension_degree"),
            "tower": row.get("tower_checks"),
            "product": row.get("product_kernel_checks"),
            "sums": row.get("sum_kernel_checks"),
            "kernel_nonzero": row.get("kernel_nonzero"),
            "guards": len(row.get("construction_guards", {})),
            "missing_product_degrees": row.get("missing_product_degrees"),
            "missing_sum_squared_degrees": row.get("missing_sum_squared_degrees"),
            "seconds": row.get("seconds"),
        } for row in rows],
    }, sort_keys=True))
