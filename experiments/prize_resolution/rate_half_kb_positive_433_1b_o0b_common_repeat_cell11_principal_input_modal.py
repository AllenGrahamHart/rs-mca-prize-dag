#!/usr/bin/env python3
"""Compile reusable cell-11 repeated-BC principal-curve inputs."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
COMMON = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_vieta_compiler.py"
)
PRODUCT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_product_rank_compiler.py"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_principal_input_result.json"
)
REMOTE_COMMON = "/root/common.py"
REMOTE_PRODUCT = "/root/product.py"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-o0b-cell11-repeat-principal-input")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=240, max_containers=8)
def compile_common(case):
    import runpy
    import sympy as sp

    started = time.perf_counter()
    epsilon_1, epsilon_2, bc_sign = case
    compiler = runpy.run_path(REMOTE_COMMON)
    variables, equations, metadata = compiler["compile_cell"](
        11, epsilon_1, epsilon_2, bc_sign, strip_fast=True
    )
    t, r, c, b = variables
    labels = metadata["labels"]
    guards = [
        labels[left] - labels[right]
        for left in range(5) for right in range(left + 1, 5)
    ]
    guards.extend((
        r, t, b, c, b - 1, b + 1, c - 1, c + 1, b - c, b + c,
    ))

    def normalized(expression):
        return str(sp.Poly(
            expression, *variables, modulus=PRIME
        ).monic().as_expr())

    equation_text = [normalized(value) for value in equations]
    guard = sp.Poly(sp.prod(guards), *variables, modulus=PRIME).monic()
    return {
        "epsilon": [epsilon_1, epsilon_2], "bc_sign": bc_sign,
        "status": "COMPLETE",
        "equations": equation_text,
        "equation_sha256": [
            hashlib.sha256(value.encode()).hexdigest()
            for value in equation_text
        ],
        "guard": str(guard.as_expr()),
        "guard_sha256": hashlib.sha256(
            str(guard.as_expr()).encode()
        ).hexdigest(),
        "seconds": time.perf_counter() - started,
    }


@app.function(image=image, cpu=1.0, memory=2048, timeout=240, max_containers=2)
def compile_product(bc_sign):
    import runpy

    started = time.perf_counter()
    compiler = runpy.run_path(REMOTE_PRODUCT)
    output = compiler["compile_cell"](11, bc_sign, dump=True)
    candidates = [
        (row["degree"], row["terms"], index, expression)
        for index, (row, expression) in enumerate(zip(
            output["stripped"], output["stripped_expressions"]
        ))
        if row["terms"]
    ]
    degree, terms, column, expression = min(candidates)
    return {
        "bc_sign": bc_sign, "status": "COMPLETE",
        "rank_minor_column": column,
        "rank_minor_degree": degree,
        "rank_minor_terms": terms,
        "rank_minor": expression,
        "rank_minor_sha256": hashlib.sha256(expression.encode()).hexdigest(),
        "seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main():
    common_cases = tuple(itertools.product((-1, 1), (-1, 1), (-1, 1)))
    common_raw = list(compile_common.map(
        common_cases, order_outputs=True, return_exceptions=True
    ))
    product_raw = list(compile_product.map(
        (-1, 1), order_outputs=True, return_exceptions=True
    ))
    common_rows = []
    for case, row in zip(common_cases, common_raw):
        if isinstance(row, BaseException):
            common_rows.append({
                "epsilon": list(case[:2]), "bc_sign": case[2],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            common_rows.append(row)
    product_rows = []
    for bc_sign, row in zip((-1, 1), product_raw):
        if isinstance(row, BaseException):
            product_rows.append({
                "bc_sign": bc_sign, "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            product_rows.append(row)
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-o0b-common-repeat-"
            "cell11-principal-input-v1"
        ),
        "scope": (
            "Exact stripped common equations, source/target guard, and "
            "selected product-rank cofactor for all cell-11 sign rows."
        ),
        "common_compiler_sha256": hashlib.sha256(COMMON.read_bytes()).hexdigest(),
        "product_compiler_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "status_counts": dict(sorted(Counter(
            row["status"] for row in [*common_rows, *product_rows]
        ).items())),
        "common_rows": common_rows,
        "product_rows": product_rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT), "status_counts": output["status_counts"],
        "common_rows": [{
            "epsilon": row["epsilon"], "bc_sign": row["bc_sign"],
            "status": row["status"], "seconds": row.get("seconds"),
        } for row in common_rows],
        "product_rows": [{
            "bc_sign": row["bc_sign"], "status": row["status"],
            "rank_minor": [row.get("rank_minor_column"),
                           row.get("rank_minor_degree"),
                           row.get("rank_minor_terms")],
            "seconds": row.get("seconds"),
        } for row in product_rows],
    }, sort_keys=True))
