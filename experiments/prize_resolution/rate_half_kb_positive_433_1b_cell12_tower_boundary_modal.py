#!/usr/bin/env python3
"""Classify deployed leading-coefficient boundaries of the cell-12 tower."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
STRUCTURE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_complete_pivot_scout_result.json"
)
TOWER = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_tower_boundary_result.json"
)
REMOTE_STRUCTURE = "/root/structure.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell12-tower-boundary")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=3)
def classify(case):
    import sympy as sp

    epsilon_1, epsilon_2, boundary, r_value = case
    c, b, t, r = sp.symbols("c b t r")
    symbols = {"c": c, "b": b, "t": t, "r": r}

    def parse_singular(text):
        expression = 0
        for term in re.findall(r"[+-]?[^+-]+", text):
            sign = -1 if term.startswith("-") else 1
            unsigned = term.lstrip("+-")
            digits = re.match(r"\d*", unsigned).group()
            monomial = sp.Integer(sign * int(digits or "1"))
            for variable, exponent in re.findall(
                r"([cbtr])(\d*)", unsigned[len(digits):]
            ):
                monomial *= symbols[variable] ** int(exponent or "1")
            expression += monomial
        return sp.Poly(expression, c, b, t, r, modulus=PRIME)

    def singular(expression):
        return str(
            sp.Poly(expression, c, b, t, modulus=PRIME).as_expr()
        ).replace("**", "^")

    payload = json.loads(Path(REMOTE_STRUCTURE).read_text())
    rows = [
        row for row in payload.get("rows", [])
        if row["epsilon"] == [epsilon_1, epsilon_2]
    ]
    if not payload.get("complete") or len(rows) != 6:
        raise RuntimeError("invalid structure payload")
    basis = [
        parse_singular(item["expression"]).as_expr().subs(r, r_value)
        for item in rows[0]["lex_basis"]
    ]
    definitions = "\n".join(
        f"poly k{index}={singular(expression)};"
        for index, expression in enumerate(basis, start=1)
    )
    guard = "*".join((
        "b", "c", "t", "(b-1)", "(b+1)", "(c-1)", "(c+1)",
        "(b-c)", "(b+c)", "(t^2-1)", "(t^2+1)",
        f"(t^2-{r_value * r_value % PRIME})",
        f"(t^2+{r_value * r_value % PRIME})",
    ))
    program = f"""
ring R={PRIME},(z,c,b,t),dp;
option(redSB);
{definitions}
poly H={guard};
ideal I=k1,k2,k3,k4,k5,k6,k7,k8,z*H-1;
ideal G=slimgb(I);
print("DP_DIM="+string(dim(G))); print("DP_SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("DP_UNIT=1"); }}
else {{
  print("DP_UNIT=0");
  ring L={PRIME},(z,c,b,t),lp;
  option(redSB);
  ideal J=fglm(R,G);
  print("LEX_BEGIN"); print("LEX_SIZE="+string(size(J))); J; print("LEX_END");
}}
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=240,
        )
    except subprocess.TimeoutExpired as error:
        stdout = (
            error.stdout.decode("utf-8", errors="replace")
            if isinstance(error.stdout, bytes) else error.stdout or ""
        )
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "boundary": boundary,
            "r": r_value,
            "status": "TIMEOUT",
            "partial_stdout": stdout[-4000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout
    lex_match = re.search(r"LEX_BEGIN\n(.*?)\nLEX_END", stdout, re.DOTALL)
    lex_rows = []
    if lex_match:
        lex_rows = [
            "".join(value.split())
            for _, value in re.findall(r"J\[(\d+)\]=(.*)", lex_match.group(1))
        ]
    factors = []
    linear_t_roots = []
    if lex_rows:
        converted = re.sub(r"([zcbt])(\d+)", r"\1**\2", lex_rows[0])
        converted = re.sub(r"(?<=\d)(?=[zcbt])", "*", converted)
        eliminant = sp.Poly(sp.sympify(converted), t, modulus=PRIME)
        _, factor_rows = sp.factor_list(
            eliminant.as_expr(), t, modulus=PRIME
        )
        for factor, multiplicity in factor_rows:
            polynomial = sp.Poly(factor, t, modulus=PRIME).monic()
            factors.append({
                "degree": int(polynomial.degree()),
                "multiplicity": int(multiplicity),
                "expression": str(polynomial.as_expr()),
                "sha256": hashlib.sha256(
                    str(polynomial.as_expr()).encode()
                ).hexdigest(),
            })
            if polynomial.degree() == 1:
                leading, constant = (
                    int(value) % PRIME for value in polynomial.all_coeffs()
                )
                linear_t_roots.extend([
                    (-constant * pow(leading, -1, PRIME)) % PRIME
                ] * int(multiplicity))

    def parse_lex(text):
        expression = 0
        lex_symbols = {
            "z": sp.symbols("z"), "c": c, "b": b, "t": t,
        }
        for term in re.findall(r"[+-]?[^+-]+", text):
            sign = -1 if term.startswith("-") else 1
            unsigned = term.lstrip("+-")
            digits = re.match(r"\d*", unsigned).group()
            monomial = sp.Integer(sign * int(digits or "1"))
            for variable, exponent in re.findall(
                r"([zcbt])(\d*)", unsigned[len(digits):]
            ):
                monomial *= lex_symbols[variable] ** int(exponent or "1")
            expression += monomial
        return expression

    b_factors = []
    points = []
    if len(linear_t_roots) == 1 and len(lex_rows) == 4:
        t_value = linear_t_roots[0]
        b_expression = parse_lex(lex_rows[1]).subs(t, t_value)
        b_polynomial = sp.Poly(b_expression, b, modulus=PRIME)
        _, b_factor_rows = sp.factor_list(
            b_polynomial.as_expr(), b, modulus=PRIME
        )
        b_roots = []
        for factor, multiplicity in b_factor_rows:
            polynomial = sp.Poly(factor, b, modulus=PRIME).monic()
            b_factors.append({
                "degree": int(polynomial.degree()),
                "multiplicity": int(multiplicity),
                "expression": str(polynomial.as_expr()),
                "sha256": hashlib.sha256(
                    str(polynomial.as_expr()).encode()
                ).hexdigest(),
            })
            if polynomial.degree() == 1:
                leading, constant = (
                    int(value) % PRIME for value in polynomial.all_coeffs()
                )
                b_roots.extend([
                    (-constant * pow(leading, -1, PRIME)) % PRIME
                ] * int(multiplicity))
        z_symbol = sp.symbols("z")
        for b_value in sorted(b_roots):
            point = {"r": r_value, "t": t_value, "b": b_value}
            for expression_text, variable, name in (
                (lex_rows[2], c, "c"), (lex_rows[3], z_symbol, "z")
            ):
                expression = parse_lex(expression_text).subs({
                    t: t_value, b: b_value,
                })
                polynomial = sp.Poly(expression, variable, modulus=PRIME)
                coefficient = int(polynomial.coeff_monomial(variable)) % PRIME
                constant = int(polynomial.coeff_monomial(1)) % PRIME
                point[name] = (
                    -constant * pow(coefficient, -1, PRIME)
                ) % PRIME
            cv = point["c"]
            guards = (
                r_value, t_value, b_value, cv,
                b_value - 1, b_value + 1, cv - 1, cv + 1,
                b_value - cv, b_value + cv,
                r_value*r_value - 1, r_value*r_value + 1,
                t_value*t_value - 1, t_value*t_value + 1,
                t_value*t_value - r_value*r_value,
                t_value*t_value + r_value*r_value,
            )
            point["guard_nonzero"] = all(value % PRIME for value in guards)
            points.append(point)

    def integer(label):
        match = re.search(rf"(?:^|\n){label}=(-?\d+)", stdout)
        return int(match.group(1)) if match else None

    valid = (
        process.returncode == 0 and "END" in stdout and "?" not in stdout
    )
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "boundary": boundary,
        "r": r_value,
        "status": "COMPLETE" if valid else "ERROR",
        "unit": "DP_UNIT=1" in stdout,
        "dimension": integer("DP_DIM"),
        "basis_size": integer("DP_SIZE"),
        "lex_basis_size": integer("LEX_SIZE"),
        "lex_basis": lex_rows,
        "t_factors": factors,
        "linear_t_roots": sorted(linear_t_roots),
        "b_factors": b_factors,
        "rational_points": points,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stdout_tail": stdout[-4000:],
        "stderr_tail": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main():
    tower = json.loads(TOWER.read_text())
    def route_guarded(value):
        return all((
            value % PRIME,
            (value - 1) % PRIME,
            (value + 1) % PRIME,
            (value * value - 1) % PRIME,
            (value * value + 1) % PRIME,
        ))

    cases = []
    for row in tower["rows"]:
        if row["c_row_index"] != 5:
            continue
        for boundary, key in (
            ("b_leading", "b_leading_deployed_roots"),
            ("c_leading", "c_leading_deployed_roots"),
        ):
            for value in row[key]:
                case = (*row["epsilon"], boundary, value)
                if route_guarded(value) and case not in cases:
                    cases.append(case)
    raw = list(classify.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, result in zip(cases, raw):
        if isinstance(result, BaseException):
            rows.append({
                "epsilon": list(case[:2]),
                "boundary": case[2], "r": case[3],
                "status": "REMOTE_ERROR", "error": repr(result),
            })
        else:
            rows.append(result)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell12-tower-boundary-v1",
        "field": PRIME,
        "scope": (
            "Exact deployed-field classification of the three non-guard "
            "leading-coefficient fibers in one cell-12 common chart."
        ),
        "source_structure_sha256": hashlib.sha256(
            STRUCTURE.read_bytes()
        ).hexdigest(),
        "source_tower_sha256": hashlib.sha256(TOWER.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                key: result.get(key) for key in (
                    "epsilon", "boundary", "r", "status", "unit", "dimension",
                    "basis_size", "lex_basis_size", "linear_t_roots"
                )
            }
            for result in rows
        ],
    }, sort_keys=True))
