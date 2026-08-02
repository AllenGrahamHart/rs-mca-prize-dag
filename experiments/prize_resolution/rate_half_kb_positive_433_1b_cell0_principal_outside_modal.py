#!/usr/bin/env python3
"""Exact outside ledgers for parameterized cell-0 principal components."""

import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMPONENTS = DIRECTORY / "rate_half_kb_positive_433_1b_cell0_principal_component_compiler_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell0_principal_outside_result.json"
REMOTE_COMPONENTS = "/root/components.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-cell0-principal-outside")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMPONENTS, REMOTE_COMPONENTS)
)


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


@app.function(image=image, cpu=1.0, memory=2048, timeout=210, max_containers=100)
def decide_case(case):
    import sympy as sp

    component, source_sign, sigma_c, sigma_o, xi_index, pairing_index = case
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

    a2_missing = evaluate((d0, d1, d2), missing_label)
    a0_missing = evaluate((e0, e1, e2), missing_label)
    b1_missing = sp.cancel(beta0 + beta1*missing_label)
    records = (
        d*e, d*e, -d*e, d*f, sigma_o*e*f,
        b*f, sigma_c*c*f,
    )
    squared_sums = (
        d*d + e*e + 2*d*e,
        d*d + e*e + 2*d*e,
        d*d + e*e - 2*d*e,
        d*d + f*f + 2*d*f,
        e*e + f*f + 2*sigma_o*e*f,
        b*b + f*f + 2*b*f,
        c*c + f*f + 2*sigma_c*c*f,
    )

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
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=180,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "component": component, "sigma": [sigma_c, sigma_o],
            "source_sign": source_sign,
            "xi_index": xi_index, "pairing_index": pairing_index,
            "status": "TIMEOUT", "partial_stdout": (error.stdout or "")[-1000:],
            "partial_stderr": (error.stderr or "")[-500:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout
    dimensions = re.findall(r"DIM=(-?\d+)", stdout)
    basis_sizes = re.findall(r"SIZE=(\d+)", stdout)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    unit = "UNIT=1" in stdout
    return {
        "component": component,
        "source_sign": source_sign,
        "sigma": [sigma_c, sigma_o],
        "xi_index": xi_index,
        "pairing_index": pairing_index,
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


@app.local_entrypoint()
def main(
    components: str = "A,B",
    source_signs: str = "-1,1",
    lanes: str = "-1:-1,-1:1,1:-1,1:1",
    xi_indices: str = "0,1,2,3,4,5,6",
    pairing_indices: str = ",".join(str(index) for index in range(15)),
):
    selected_components = tuple(value for value in components.split(",") if value)
    selected_source_signs = tuple(
        int(value) for value in source_signs.split(",") if value
    )
    selected_lanes = tuple(
        tuple(int(sign) for sign in value.split(":"))
        for value in lanes.split(",") if value
    )
    selected_xi_indices = tuple(
        int(value) for value in xi_indices.split(",") if value
    )
    selected_pairing_indices = tuple(
        int(value) for value in pairing_indices.split(",") if value
    )
    cases = tuple(
        (component, source_sign, sigma_c, sigma_o, xi_index, pairing_index)
        for component in selected_components
        for source_sign in selected_source_signs
        for sigma_c, sigma_o in selected_lanes
        for xi_index in selected_xi_indices
        for pairing_index in selected_pairing_indices
    )
    raw = list(decide_case.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "component": case[0], "source_sign": case[1],
                "sigma": list(case[2:4]),
                "xi_index": case[4], "pairing_index": case[5],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell0-principal-outside-v2",
        "app": "rs-mca-positive-433-1b-cell0-principal-outside",
        "scope": "Exact equal-sign cell-0 principal-component outside exclusions.",
        "field": PRIME,
        "source_components_sha256": hashlib.sha256(COMPONENTS.read_bytes()).hexdigest(),
        "component_count": len(selected_components),
        "source_sign_count": len(selected_source_signs),
        "lane_count": (
            len(selected_components)*len(selected_source_signs)*len(selected_lanes)
        ),
        "case_count": len(rows),
        "status_counts": {
            status: sum(row["status"] == status for row in rows)
            for status in sorted({row["status"] for row in rows})
        },
        "unit_count": sum(row.get("unit", False) for row in rows),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status_counts": {
            status: sum(row["status"] == status for row in rows)
            for status in sorted({row["status"] for row in rows})
        },
        "unit": sum(row.get("unit", False) for row in rows),
        "nonunit": sum(row["status"] == "COMPLETE" and not row.get("unit", False)
                       for row in rows),
        "nonunit_rows": [
            [row["xi_index"], row["pairing_index"],
             row.get("dimension"), row.get("basis_size")]
            for row in rows if row["status"] == "COMPLETE" and not row.get("unit", False)
        ],
    }, sort_keys=True))
