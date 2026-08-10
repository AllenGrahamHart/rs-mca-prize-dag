#!/usr/bin/env python3
"""Compact common kernels for repeated-BC 433-1b/O0b cells 3 and 6."""

import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMMON = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_vieta_compiler.py"
)
PRODUCT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_product_rank_compiler_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cells3_6_compact_kernel_result.json"
)
REMOTE_COMMON = "/root/repeat_common.py"
REMOTE_PRODUCT = "/root/repeat_product.json"
PRIME = 2130706433
CELLS = (3, 6)
SUM_PIVOT = 1
PRODUCT_GUARD_COLUMN = 1

app = modal.App("rs-mca-positive-433-1b-o0b-repeat-cells3-6-kernel")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=240, max_containers=16)
def compile_kernel(case):
    import functools
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from repeat_common import compile_cell

    cell, epsilon_1, epsilon_2, bc_sign = case
    variables, _, metadata = compile_cell(
        cell, epsilon_1, epsilon_2, bc_sign
    )
    t, r, c, b = variables
    labels = metadata["labels"]
    products = metadata["products"]
    q_values = metadata["q_values"]

    product_payload = json.loads(Path(REMOTE_PRODUCT).read_text())
    product_row = next(
        row for row in product_payload["rows"]
        if row["cell"] == cell and row["bc_sign"] == bc_sign
    )
    if PRODUCT_GUARD_COLUMN not in product_row["guard_only_minor_columns"]:
        raise RuntimeError("selected product cofactor is not guard-only")
    raw_cofactors = tuple(
        sp.Poly(sp.sympify(value), *variables, modulus=PRIME)
        for value in product_row["kernel_cofactor_expressions"]
    )
    common_gcd = functools.reduce(sp.gcd, raw_cofactors)
    cofactors = []
    for value in raw_cofactors:
        quotient, remainder = sp.div(value, common_gcd)
        if not remainder.is_zero:
            raise RuntimeError("nonexact product-kernel gcd division")
        cofactors.append(quotient.as_expr())

    loop_label = labels[0]
    pivot_label = labels[SUM_PIVOT]
    scale = sp.expand(pivot_label * (loop_label - pivot_label))
    a_at_pivot = sp.expand(sum(
        cofactors[index] * pivot_label**index for index in range(3)
    ))
    gamma = sp.expand(q_values[SUM_PIVOT] * a_at_pivot)
    kernel = [
        *(sp.expand(scale * value) for value in cofactors),
        sp.expand(-loop_label * gamma),
        gamma,
    ]
    kernel_polynomials = [
        sp.Poly(value, *variables, modulus=PRIME) for value in kernel
    ]
    kernel_gcd = functools.reduce(sp.gcd, kernel_polynomials)
    primitive_kernel = []
    for value in kernel_polynomials:
        quotient, remainder = sp.div(value, kernel_gcd)
        if not remainder.is_zero:
            raise RuntimeError("nonexact final-kernel gcd division")
        primitive_kernel.append(quotient.as_expr())
    first = next(sp.Poly(value, *variables, modulus=PRIME)
                 for value in primitive_kernel if value != 0)
    inverse = pow(int(first.LC()) % PRIME, -1, PRIME)
    primitive_kernel = [
        sp.Poly(inverse * value, *variables, modulus=PRIME).as_expr()
        for value in primitive_kernel
    ]

    product_rows = [
        [-product, -product * label, -product * label**2,
         1, label, label**2, 0, 0]
        for label, product in zip(labels, products)
    ]
    sum_rows = [
        [q_value, q_value * label, q_value * label**2,
         0, 0, 0, label, label**2]
        for label, q_value in zip(labels, q_values)
    ]
    rows = [*product_rows, *sum_rows]
    row_dots = [
        sp.expand(sum(left * right for left, right in zip(row, primitive_kernel)))
        for row in rows
    ]
    identically_zero = [
        sp.Poly(value, *variables, modulus=PRIME).is_zero for value in row_dots
    ]
    if identically_zero[:7] != [True] * 7:
        raise RuntimeError("product/loop/pivot kernel identity")

    source_guards = [
        labels[left] - labels[right]
        for left in range(5) for right in range(left + 1, 5)
    ]
    target_guards = [
        r, t, b, c, b - 1, b + 1, c - 1, c + 1, b - c, b + c,
    ]
    guards = [*source_guards, *target_guards]

    def strip_factors(expression):
        value = sp.Poly(expression, *variables, modulus=PRIME)
        for factor in guards:
            divisor = sp.Poly(factor, *variables, modulus=PRIME)
            if divisor.total_degree() == 0:
                continue
            while True:
                quotient, remainder = sp.div(value, divisor)
                if not remainder.is_zero:
                    break
                value = quotient
        return value.monic().as_expr()

    compact_equations = [strip_factors(row_dots[5 + index])
                         for index in (2, 3, 4)]
    guard_product = sp.prod(guards)

    def singular(expression):
        return str(
            sp.Poly(expression, *variables, modulus=PRIME).as_expr()
        ).replace("**", "^")

    equation_definitions = "\n".join(
        f"poly q{index}={singular(value)};"
        for index, value in enumerate(compact_equations)
    )
    row_definitions = "\n".join(
        f"poly v{index}={singular(value)};"
        for index, value in enumerate(row_dots)
    )
    reductions = "\n".join(
        f'print("ROW={index},BEGIN"); print(reduce(v{index},G)); '
        f'print("ROW={index},END");'
        for index in range(len(row_dots))
    )
    program = f"""
ring R={PRIME},(z,t,r,c,b),(dp(1),dp(4));
option(redSB);
{equation_definitions}
poly guard={singular(guard_product)};
ideal I=q0,q1,q2,z*guard-1;
ideal G=std(I);
{row_definitions}
print("BEGIN");
print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
{reductions}
print("BASIS_BEGIN"); print(G); print("BASIS_END");
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=210,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "cell": cell, "epsilon": [epsilon_1, epsilon_2],
            "bc_sign": bc_sign, "status": "TIMEOUT",
            "partial_stdout": (error.stdout or "")[-8000:],
            "partial_stderr": (error.stderr or "")[-2000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout
    remainders = []
    for index in range(len(row_dots)):
        match = re.search(
            rf"ROW={index},BEGIN\n(.*?)\nROW={index},END",
            stdout, re.DOTALL,
        )
        remainders.append("".join(match.group(1).split()) if match else None)
    basis_match = re.search(r"BASIS_BEGIN\n(.*?)\nBASIS_END", stdout, re.DOTALL)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout

    def summary(expression, include_expression=False):
        polynomial = sp.Poly(expression, *variables, modulus=PRIME)
        text = str(polynomial.as_expr())
        output = {
            "degree": polynomial.total_degree(),
            "terms": len(polynomial.terms()),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
        }
        if include_expression:
            output["expression"] = text
        return output

    return {
        "cell": cell,
        "epsilon": [epsilon_1, epsilon_2],
        "bc_sign": bc_sign,
        "status": "COMPLETE" if valid else "ERROR",
        "loop_label": str(loop_label),
        "sum_pivot": SUM_PIVOT,
        "pivot_label": str(pivot_label),
        "product_guard_column": PRODUCT_GUARD_COLUMN,
        "product_kernel_removed_gcd": summary(common_gcd.as_expr()),
        "final_kernel_removed_gcd": summary(kernel_gcd.as_expr()),
        "kernel": [summary(value, include_expression=True)
                   for value in primitive_kernel],
        "identically_zero_rows": identically_zero,
        "compact_equations": [summary(value, include_expression=True)
                              for value in compact_equations],
        "reduced_remainders": remainders,
        "all_rows_zero_mod_common": all(value == "0" for value in remainders),
        "common_dimension": int(re.search(r"DIM=(-?\d+)", stdout).group(1)),
        "common_basis_size": int(re.search(r"SIZE=(\d+)", stdout).group(1)),
        "common_basis": basis_match.group(1).strip() if basis_match else None,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-2000:],
    }


@app.local_entrypoint()
def main():
    cases = tuple(itertools.product(CELLS, (-1, 1), (-1, 1), (-1, 1)))
    raw = list(compile_kernel.map(
        cases, order_outputs=True, return_exceptions=True
    ))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "cell": case[0], "epsilon": list(case[1:3]),
                "bc_sign": case[3], "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-repeat-cells3-6-kernel-v1",
        "field": PRIME,
        "scope": (
            "Exact polynomial coefficient kernels and guarded common ideals "
            "for repeated-BC survivor cells 3 and 6; no outside or route claim."
        ),
        "source_common_sha256": hashlib.sha256(COMMON.read_bytes()).hexdigest(),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                "cell": row.get("cell"), "epsilon": row.get("epsilon"),
                "bc_sign": row.get("bc_sign"), "status": row.get("status"),
                "dimension": row.get("common_dimension"),
                "basis_size": row.get("common_basis_size"),
                "all_rows_zero": row.get("all_rows_zero_mod_common"),
                "kernel_shapes": [
                    [item["degree"], item["terms"]]
                    for item in row.get("kernel", [])
                ],
            }
            for row in rows
        ],
    }, sort_keys=True))

