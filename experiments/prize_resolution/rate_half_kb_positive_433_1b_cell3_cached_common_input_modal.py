#!/usr/bin/env python3
"""Compile four reusable cell-3 common polynomial packets on Modal."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
PRODUCT = DIRECTORY / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
STRUCTURE = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_compact_structure_result.json"
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
REMOTE_PRODUCT = "/root/product.json"
REMOTE_STRUCTURE = "/root/structure.json"
REMOTE_KERNEL = "/root/kernel.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-cell3-cached-common-input")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("sympy==1.14.0")
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=1.0, memory=3072, timeout=180, max_containers=4)
def compile_packet(signs):
    import functools

    import sympy as sp

    epsilon_1, epsilon_2 = signs
    t, r, c, b = sp.symbols("t r c b")
    variables = (t, r, c, b)
    roots = (1, t, epsilon_1 * IOTA, r, epsilon_2 * IOTA * r)
    labels = tuple(sp.expand(root * root) for root in roots)
    products = (-1, b, c, b * c, -b * c)
    sums = (0, 1 + b, 1 + c, b + c, b - c)
    q_values = tuple(
        sp.expand(root * edge_sum) for root, edge_sum in zip(roots, sums)
    )
    product_rows = [
        [-product, -product * label, -product * label**2,
         1, label, label**2, 0]
        for label, product in zip(labels, products)
    ]
    sum_rows = [
        [q_value, q_value * label, q_value * label**2,
         0, 0, 0, -label * (1 - label)]
        for label, q_value in zip(labels, q_values)
    ]
    base_rows = [*product_rows, sum_rows[1]]
    equations = [
        sp.expand(
            sp.Matrix([*base_rows, sum_rows[index]]).det(method="domain-ge")
        )
        for index in (2, 3, 4)
    ]
    route_guards = [
        b, c, r, t,
        b - 1, b + 1, c - 1, c + 1, b - c, b + c,
        r * r - 1, r * r + 1, t * t - 1, t * t + 1,
        t * t - r * r, t * t + r * r,
    ]

    def strip_factors(expression):
        value = sp.Poly(expression, *variables, modulus=PRIME)
        for factor in route_guards:
            divisor = sp.Poly(factor, *variables, modulus=PRIME)
            while True:
                quotient, remainder = sp.div(value, divisor)
                if not remainder.is_zero:
                    break
                value = quotient
        return value.monic().as_expr()

    equations = tuple(strip_factors(value) for value in equations)
    product_payload = json.loads(Path(REMOTE_PRODUCT).read_text())
    product_row = next(
        row for row in product_payload["rows"] if row["cell"] == 3
    )
    raw_cofactors = tuple(
        sp.Poly(sp.sympify(value), *variables, modulus=PRIME)
        for value in product_row["kernel_cofactor_expressions"]
    )
    common_gcd = functools.reduce(sp.gcd, raw_cofactors)
    for value in raw_cofactors:
        _, remainder = sp.div(value, common_gcd)
        if not remainder.is_zero:
            raise RuntimeError("nonexact product-kernel gcd division")
    rank_cofactors = tuple(
        sp.Poly(sp.sympify(value), *variables, modulus=PRIME).monic().as_expr()
        for value in product_row["stripped_expressions"]
    )
    if len({str(value) for value in rank_cofactors}) != 6:
        raise RuntimeError("six distinct product-rank charts")

    kernel_payload = json.loads(Path(REMOTE_KERNEL).read_text())
    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    if kernel_row["status"] != "COMPLETE" or len(kernel_row["kernel"]) != 8:
        raise RuntimeError("kernel-row custody")
    kernel = tuple(
        sp.Poly(sp.sympify(value["expression"]), *variables, modulus=PRIME).as_expr()
        for value in kernel_row["kernel"]
    )
    structure_payload = json.loads(Path(REMOTE_STRUCTURE).read_text())
    structure_row = next(
        row for row in structure_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2] and row["chart"] == 0
    )
    equation_hashes = tuple(
        hashlib.sha256(str(value).encode()).hexdigest() for value in equations
    )
    expected_equation_hashes = tuple(
        value["sha256"] for value in structure_row["equation_summaries"]
    )
    kernel_hashes = tuple(
        hashlib.sha256(str(value).encode()).hexdigest() for value in kernel
    )
    expected_kernel_hashes = tuple(
        value["sha256"] for value in kernel_row["kernel"]
    )
    if equation_hashes != expected_equation_hashes:
        raise RuntimeError("compact-equation hash mismatch")
    if kernel_hashes != expected_kernel_hashes:
        raise RuntimeError("coefficient-kernel hash mismatch")

    def singular(expression):
        return str(
            sp.Poly(expression, *variables, modulus=PRIME).as_expr()
        ).replace("**", "^")

    packet = {
        "variables": ["t", "r", "c", "b"],
        "common_equations": [singular(value) for value in equations],
        "kernel": [singular(value) for value in kernel],
        "route_guards": [singular(value) for value in route_guards],
        "rank_cofactors": [singular(value) for value in rank_cofactors],
    }
    encoded = json.dumps(packet, separators=(",", ":"), sort_keys=True)
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "status": "COMPLETE",
        "packet_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "equation_hashes": list(equation_hashes),
        "kernel_hashes": list(kernel_hashes),
        "packet": packet,
    }


def write_checkpoint(rows, complete):
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell3-cached-common-input-v1",
        "field": PRIME,
        "complete": complete,
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "source_structure_sha256": hashlib.sha256(STRUCTURE.read_bytes()).hexdigest(),
        "source_kernel_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "expected_row_count": 4,
        "processed_row_count": len(rows),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    cases = tuple(
        (epsilon_1, epsilon_2)
        for epsilon_1 in (-1, 1) for epsilon_2 in (-1, 1)
    )
    rows = []
    write_checkpoint(rows, complete=False)
    remote_rows = compile_packet.map(cases, order_outputs=True, return_exceptions=True)
    for case, row in zip(cases, remote_rows):
        rows.append({
            "epsilon": list(case),
            "status": "REMOTE_ERROR",
            "error": repr(row),
        } if isinstance(row, BaseException) else row)
        write_checkpoint(rows, complete=False)
    complete = len(rows) == 4 and all(row["status"] == "COMPLETE" for row in rows)
    write_checkpoint(rows, complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "complete": complete,
        "processed": len(rows),
        "statuses": [row["status"] for row in rows],
        "packet_hashes": [row.get("packet_sha256") for row in rows],
    }, sort_keys=True))
