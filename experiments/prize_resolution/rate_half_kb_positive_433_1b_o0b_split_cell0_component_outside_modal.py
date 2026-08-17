#!/usr/bin/env python3
"""Exact O0b outside ideals for canonical split cell-0 component cases."""

import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMPONENTS = DIRECTORY / "rate_half_kb_positive_433_1b_cell0_principal_component_compiler_result.json"
REPRESENTATIVES = (
    DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_representatives.json"
)
CORE = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cell0_outside_core.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cell0_component_outside_result.json"
REMOTE_COMPONENTS = "/root/components.json"
PRIME = 2130706433
IOTA = 16711679
FULL_REPRESENTATIVES_SHA256 = (
    "23d7e403e420307b5466ffaf6d2af59d0cf9a4a93766b4d0bcf68231aba1a741"
)
REPRESENTATIVES_FILE_SHA256 = (
    "658ae5f1f3c0667df2cece818e0c89a752ce9cdf7c4f6f421fc4a721134b8fa4"
)
PILOT_REPRESENTATIVES_SHA256 = (
    "47ef7c3a9a92ac2bcb08462377195c0576c2495b0ff1f7c0948103d10e02bc27"
)

app = modal.App("rs-mca-positive-433-1b-o0b-split-cell0-outside")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMPONENTS, REMOTE_COMPONENTS)
)

core_spec = importlib.util.spec_from_file_location("cell0_outside_core", CORE)
core_module = importlib.util.module_from_spec(core_spec)
core_spec.loader.exec_module(core_module)
EDGE_SPECS = core_module.EDGE_SPECS


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, values[index]),) + tail


def representative_cases(scope):
    if hashlib.sha256(REPRESENTATIVES.read_bytes()).hexdigest() != REPRESENTATIVES_FILE_SHA256:
        raise RuntimeError("representative manifest custody")
    manifest = json.loads(REPRESENTATIVES.read_text())
    if manifest["representatives_sha256"] != FULL_REPRESENTATIVES_SHA256:
        raise RuntimeError("representative router custody")
    if manifest["representative_count"] != 708 or len(manifest["representatives"]) != 708:
        raise RuntimeError("representative manifest census")
    representatives = tuple(tuple(row) for row in manifest["representatives"])
    if scope == "all":
        return representatives
    if scope != "pilot":
        raise RuntimeError("scope must be pilot or all")
    cases = tuple(tuple(row) for row in manifest["pilot_representatives"])
    encoded = json.dumps(cases, separators=(",", ":"))
    if (manifest["pilot_stratum_count"] != 56 or len(cases) != 24 or
            hashlib.sha256(encoded.encode()).hexdigest() !=
            PILOT_REPRESENTATIVES_SHA256):
        raise RuntimeError("pilot representative census")
    return cases


def case_key(case):
    component, lane, sigma_o, source_sign, xi_index, pairing_index = case
    return {
        "component": component,
        "lane": lane,
        "sigma_o": sigma_o,
        "source_sign": source_sign,
        "xi_index": xi_index,
        "pairing_index": pairing_index,
    }


@app.function(image=image, cpu=1.0, memory=2048, timeout=210, max_containers=64)
def decide_case(case):
    import sympy as sp

    component, lane, sigma_o, source_sign, xi_index, pairing_index = case
    payload = json.loads(Path(REMOTE_COMPONENTS).read_text())
    source = next(
        row for row in payload["rows"]
        if row["component"] == component and row["source_sign"] == source_sign
    )
    b, d, e, f, t, x = sp.symbols("b d e f t x")
    relation = sp.sympify(source["relation"]["expression"])
    relation_poly = sp.Poly(relation, t)
    relation_x = sp.expand(
        relation_poly.coeff_monomial(1)
        + relation_poly.coeff_monomial(t**2)*x
    )
    t_square = x
    kernel = [sp.sympify(row["expression"]) for row in source["kernel"]]
    d0, d1, d2, e0, e1, e2, beta0, beta1 = kernel
    c = (
        source_sign*IOTA if component == "A" else -source_sign*IOTA
    ) * b
    r = 1/b if component == "A" else b
    missing_label = -t_square

    def evaluate(coefficients, value):
        return sp.cancel(
            coefficients[0] + coefficients[1]*value + coefficients[2]*value**2
        )

    def edge(left, right, sign):
        return sign*left*right, left*left + right*right + 2*sign*left*right

    a2_missing = evaluate((d0, d1, d2), missing_label)
    a0_missing = evaluate((e0, e1, e2), missing_label)
    b1_missing = sp.cancel(beta0 + beta1*missing_label)
    if lane not in EDGE_SPECS:
        raise RuntimeError("unknown O0b lane")
    outside_values = (b, c, d, e, f)
    signed_edges = tuple(
        edge(outside_values[left], outside_values[right],
             sigma_o if sign == 0 else sign)
        for left, right, sign in EDGE_SPECS[lane]
    )
    records = tuple(row[0] for row in signed_edges)
    squared_sums = tuple(row[1] for row in signed_edges)

    y, z = sp.symbols("y z")
    p0, p1, p2 = e0-y*d0, e1-y*d1, e2-y*d2
    q0, q1, q2 = e0-z*d0, -e1+z*d1, e2-z*d2
    paired = sp.expand(
        (p2*q0-p0*q2)**2 - (p2*q1-p1*q2)*(p1*q0-p0*q1)
    )
    residual = tuple(index for index in range(7) if index != xi_index)
    matching = tuple(pairings(range(6)))[pairing_index]
    rational_equations = [
        relation_x,
        records[xi_index]*a2_missing-a0_missing,
    ]
    rational_equations.extend(
        paired.subs({y: records[residual[left]], z: records[residual[right]]})
        for left, right in matching
    )
    rational_equations.append(
        missing_label*b1_missing*b1_missing
        - squared_sums[xi_index]*a2_missing*a2_missing
    )

    target_values = (1, b, c, d, e, f)
    guard_factors = [
        b, d, e, f, r, t_square,
        r*r-1, r*r+1,
        t_square-1, t_square+1,
        t_square-r*r, t_square+r*r,
    ]
    guard_factors.extend(
        target_values[left]**2 - target_values[right]**2
        for left in range(6) for right in range(left + 1, 6)
    )
    common_labels = (t_square, 1, -1, r*r, -r*r)
    guard_factors.extend(
        evaluate((d0, d1, d2), label) for label in common_labels
    )
    guard_factors.append(a2_missing)

    polynomial_variables = (b, x, d, e, f)
    denominators = []

    def numerator(expression):
        top, bottom = sp.fraction(sp.cancel(expression))
        denominators.append(bottom)
        return sp.Poly(top, *polynomial_variables, modulus=PRIME).as_expr()

    equations = [numerator(value) for value in rational_equations]
    guards = [numerator(value) for value in guard_factors]
    source_denominators = tuple(denominators)

    def polynomial_numerator(expression):
        top, _ = sp.fraction(sp.cancel(expression))
        return sp.Poly(top, *polynomial_variables, modulus=PRIME).as_expr()

    guards.extend(polynomial_numerator(value) for value in source_denominators)
    unique_guards = []
    seen_guards = set()
    for factor in guards:
        factor_poly = sp.Poly(factor, *polynomial_variables, modulus=PRIME)
        if factor_poly.total_degree() == 0:
            continue
        normalized = factor_poly.monic().as_expr()
        key = str(normalized)
        if key not in seen_guards:
            seen_guards.add(key)
            unique_guards.append(normalized)

    def singular(expression):
        return str(sp.Poly(expression, *polynomial_variables,
                           modulus=PRIME).as_expr()).replace("**", "^")

    definitions = "\n".join(
        f"poly q{index}={singular(value)};"
        for index, value in enumerate(equations)
    )
    guard_definitions = "\n".join(
        f"poly h{index}={singular(value)};"
        for index, value in enumerate(unique_guards)
    )
    saturation_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G); "
        f'print("SAT={index},DIM="+string(dim(G))+",SIZE="+string(size(G)));'
        for index in range(len(unique_guards))
    )
    ring_variables = ",".join(str(value) for value in polynomial_variables)
    equation_generators = ",".join(
        f"q{index}" for index in range(len(equations))
    )
    program = f"""
LIB "elim.lib";
ring R={PRIME},({ring_variables}),dp;
option(redSB);
{definitions}
{guard_definitions}
ideal I={equation_generators};
ideal G=slimgb(I);
{saturation_stages}
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); }}
print("END");
quit;
"""
    key = case_key(case)
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=180,
        )
    except subprocess.TimeoutExpired as error:
        return {
            **key,
            "status": "TIMEOUT",
            "partial_stdout": (error.stdout or "")[-1000:],
            "partial_stderr": (error.stderr or "")[-500:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout
    dimensions = re.findall(r"DIM=(-?\d+)", stdout)
    basis_sizes = re.findall(r"SIZE=(\d+)", stdout)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    unit = "UNIT=1" in stdout
    return {
        **key,
        "status": "COMPLETE" if valid else "ERROR",
        "unit": unit,
        "dimension": int(dimensions[-1]) if dimensions else None,
        "basis_size": int(basis_sizes[-1]) if basis_sizes else None,
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-500:],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "input_polynomials": [] if unit else [singular(value) for value in equations],
        "guard_factors": [] if unit else [singular(value) for value in unique_guards],
    }


def write_checkpoint(scope, cases, rows, complete):
    encoded_cases = json.dumps(cases, separators=(",", ":"))
    statuses = sorted({row["status"] for row in rows})
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-split-cell0-outside-v1",
        "app": "rs-mca-positive-433-1b-o0b-split-cell0-outside",
        "scope": scope,
        "complete": complete,
        "field": PRIME,
        "source_components_sha256": hashlib.sha256(COMPONENTS.read_bytes()).hexdigest(),
        "source_representatives_sha256": hashlib.sha256(REPRESENTATIVES.read_bytes()).hexdigest(),
        "source_outside_core_sha256": hashlib.sha256(CORE.read_bytes()).hexdigest(),
        "full_representatives_sha256": FULL_REPRESENTATIVES_SHA256,
        "selected_cases_sha256": hashlib.sha256(encoded_cases.encode()).hexdigest(),
        "expected_case_count": len(cases),
        "processed_case_count": len(rows),
        "status_counts": {
            status: sum(row["status"] == status for row in rows)
            for status in statuses
        },
        "unit_count": sum(row.get("unit", False) for row in rows),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main(scope: str = "pilot"):
    cases = representative_cases(scope)
    rows = []
    write_checkpoint(scope, cases, rows, complete=False)
    remote_rows = decide_case.map(cases, order_outputs=True, return_exceptions=True)
    for case, row in zip(cases, remote_rows):
        if isinstance(row, BaseException):
            rows.append({
                **case_key(case),
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
        write_checkpoint(scope, cases, rows, complete=False)
    complete = len(rows) == len(cases) and all(
        row["status"] == "COMPLETE" for row in rows
    )
    write_checkpoint(scope, cases, rows, complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "scope": scope,
        "complete": complete,
        "expected": len(cases),
        "processed": len(rows),
        "status_counts": {
            status: sum(row["status"] == status for row in rows)
            for status in sorted({row["status"] for row in rows})
        },
        "unit": sum(row.get("unit", False) for row in rows),
        "nonunit": sum(row["status"] == "COMPLETE" and not row.get("unit", False)
                       for row in rows),
    }, sort_keys=True))
