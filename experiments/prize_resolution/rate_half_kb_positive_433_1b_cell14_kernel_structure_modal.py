#!/usr/bin/env python3
"""Explore a low-degree kernel presentation of positive 433-1b cell 14."""

import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
PRODUCT = DIRECTORY / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_kernel_structure_result.json"
REMOTE_PRODUCT = "/root/product.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-cell14-kernel-structure")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=300, max_containers=24)
def analyze(case):
    import sympy as sp

    epsilon_1, epsilon_2, chart = case
    t, r, c, b = sp.symbols("t r c b")
    variables = (t, r, c, b)
    labels = (1, r*r, -r*r, -1, t*t)
    products = (-1, b, c, b*c, -b*c)
    sums = (0, 1+b, 1+c, b+c, b-c)
    roots = (1, r, epsilon_2*IOTA*r, epsilon_1*IOTA, t)
    q_values = tuple(sp.expand(root*edge_sum)
                     for root, edge_sum in zip(roots, sums))
    product_rows = [
        [-product, -product*label, -product*label**2,
         1, label, label**2, 0]
        for label, product in zip(labels, products)
    ]
    sum_rows = [
        [q_value, q_value*label, q_value*label**2,
         0, 0, 0, -label*(1-label)]
        for label, q_value in zip(labels, q_values)
    ]
    base_rows = [*product_rows, sum_rows[1]]
    equations = [
        sp.expand(sp.Matrix([*base_rows, sum_rows[index]]).det(method="domain-ge"))
        for index in (2, 3, 4)
    ]

    product_payload = json.loads(Path(REMOTE_PRODUCT).read_text())
    product_row = next(row for row in product_payload["rows"]
                       if row["cell"] == 14)
    cofactor = sp.sympify(product_row["stripped_expressions"][chart])
    reference_cofactor = sp.sympify(product_row["stripped_expressions"][3])
    route_guards = [
        b, c, r, t,
        b-1, b+1, c-1, c+1, b-c, b+c,
        r*r-1, r*r+1, t*t-1, t*t+1,
        t*t-r*r, t*t+r*r,
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

    equations = [strip_factors(value) for value in equations]
    guard_factors = [cofactor, *route_guards]

    def polynomial(expression):
        return sp.Poly(expression, *variables, modulus=PRIME).as_expr()

    normalized_guards = []
    seen = set()
    for expression in guard_factors:
        value = sp.Poly(expression, *variables, modulus=PRIME)
        if value.total_degree() == 0:
            continue
        normalized = value.monic().as_expr()
        key = str(normalized)
        if key not in seen:
            seen.add(key)
            normalized_guards.append(normalized)

    def singular(expression):
        return str(polynomial(expression)).replace("**", "^")

    equation_definitions = "\n".join(
        f"poly q{index}={singular(value)};"
        for index, value in enumerate(equations)
    )
    guard_definitions = "\n".join(
        f"poly h{index}={singular(value)};"
        for index, value in enumerate(normalized_guards)
    )
    saturation_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G); "
        f'print("SAT={index},DIM="+string(dim(G))+",SIZE="+string(size(G)));'
        for index in range(len(normalized_guards))
    )
    generators = ",".join(f"q{index}" for index in range(len(equations)))
    program = f"""
LIB "elim.lib";
ring R={PRIME},(t,r,c,b),dp;
option(redSB);
{equation_definitions}
{guard_definitions}
poly href={singular(reference_cofactor)};
ideal I={generators};
ideal G=slimgb(I);
{saturation_stages}
ideal Etr=eliminate(G,c*b); Etr=slimgb(Etr);
ideal Erb=eliminate(G,t*c); Erb=slimgb(Erb);
poly dt=diff(Etr[1],t);
poly dc=diff(G[1],c);
ideal Jt=G,dt; Jt=slimgb(Jt);
ideal Jc=G,dc; Jc=slimgb(Jc);
ideal Jref=G,href; Jref=slimgb(Jref);
print("BEGIN");
print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
print("ETR_DIM="+string(dim(Etr))); print("ETR_SIZE="+string(size(Etr)));
print("ERB_DIM="+string(dim(Erb))); print("ERB_SIZE="+string(size(Erb)));
print("JT_DIM="+string(dim(Jt))); print("JT_SIZE="+string(size(Jt)));
print("JC_DIM="+string(dim(Jc))); print("JC_SIZE="+string(size(Jc)));
print("JREF_DIM="+string(dim(Jref))); print("JREF_SIZE="+string(size(Jref)));
if ((size(Jt)==1) && (Jt[1]==1)) {{ print("DT_UNIT=1"); }}
else {{ print("DT_UNIT=0"); }}
if ((size(Jc)==1) && (Jc[1]==1)) {{ print("DC_UNIT=1"); }}
else {{ print("DC_UNIT=0"); }}
if ((size(Jref)==1) && (Jref[1]==1)) {{ print("REF_UNIT=1"); }}
else {{ print("REF_UNIT=0"); }}
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{
  print("UNIT=0");
  print("ETR_BEGIN"); Etr; print("ETR_END");
  print("ERB_BEGIN"); Erb; print("ERB_END");
  print("GB_BEGIN"); G; print("GB_END");
}}
print("END");
quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=270,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "epsilon": [epsilon_1, epsilon_2], "chart": chart,
            "status": "TIMEOUT", "partial_stdout": (error.stdout or "")[-4000:],
            "partial_stderr": (error.stderr or "")[-1000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout
    dimensions = re.findall(r"(?:^|\n)DIM=(-?\d+)", stdout)
    sizes = re.findall(r"(?:^|\n)SIZE=(\d+)", stdout)
    etr_dimension = re.search(r"ETR_DIM=(-?\d+)", stdout)
    etr_size = re.search(r"ETR_SIZE=(\d+)", stdout)
    erb_dimension = re.search(r"ERB_DIM=(-?\d+)", stdout)
    erb_size = re.search(r"ERB_SIZE=(\d+)", stdout)
    jt_dimension = re.search(r"JT_DIM=(-?\d+)", stdout)
    jt_size = re.search(r"JT_SIZE=(\d+)", stdout)
    jc_dimension = re.search(r"JC_DIM=(-?\d+)", stdout)
    jc_size = re.search(r"JC_SIZE=(\d+)", stdout)
    jref_dimension = re.search(r"JREF_DIM=(-?\d+)", stdout)
    jref_size = re.search(r"JREF_SIZE=(\d+)", stdout)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout

    def parse_singular_polynomial(body):
        expression = 0
        symbols = {"t": t, "r": r, "c": c, "b": b}
        for term in re.findall(r"[+-]?[^+-]+", body.strip()):
            sign = -1 if term.startswith("-") else 1
            unsigned = term.lstrip("+-")
            digits = re.match(r"\d*", unsigned).group()
            coefficient = int(digits or "1") * sign
            monomial = sp.Integer(coefficient)
            for variable, exponent in re.findall(r"([trcb])(\d*)", unsigned[len(digits):]):
                monomial *= symbols[variable] ** int(exponent or "1")
            expression += monomial
        return sp.Poly(expression, *variables, modulus=PRIME).as_expr()

    def extracted(begin, row_name, end):
        match = re.search(
            begin + r"\n" + row_name + r"\[1\]=(.*?)\n" + end,
            stdout,
            re.S,
        )
        return parse_singular_polynomial(match.group(1)) if match else None

    relation_t = extracted("ETR_BEGIN", "Etr", "ETR_END")
    relation_rb = extracted("ERB_BEGIN", "Erb", "ERB_END")
    relation_c_match = re.search(
        r"GB_BEGIN\nG\[1\]=(.*?)\nG\[2\]=", stdout, re.S
    )
    relation_c = (
        parse_singular_polynomial(relation_c_match.group(1))
        if relation_c_match else None
    )

    def relation_summary(value):
        if value is None:
            return None
        polynomial_value = sp.Poly(value, *variables, modulus=PRIME)
        return {
            "degree": polynomial_value.total_degree(),
            "terms": len(polynomial_value.terms()),
            "expression": str(polynomial_value.as_expr()),
        }

    return {
        "epsilon": [epsilon_1, epsilon_2],
        "chart": chart,
        "status": "COMPLETE" if valid else "ERROR",
        "unit": bool(re.search(r"(?:^|\n)UNIT=1(?:\n|$)", stdout)),
        "dimension": int(dimensions[-1]) if dimensions else None,
        "basis_size": int(sizes[-1]) if sizes else None,
        "etr_dimension": int(etr_dimension.group(1)) if etr_dimension else None,
        "etr_size": int(etr_size.group(1)) if etr_size else None,
        "erb_dimension": int(erb_dimension.group(1)) if erb_dimension else None,
        "erb_size": int(erb_size.group(1)) if erb_size else None,
        "t_exception_dimension": (
            int(jt_dimension.group(1)) if jt_dimension else None
        ),
        "t_exception_size": int(jt_size.group(1)) if jt_size else None,
        "c_exception_dimension": (
            int(jc_dimension.group(1)) if jc_dimension else None
        ),
        "c_exception_size": int(jc_size.group(1)) if jc_size else None,
        "reference_exception_dimension": (
            int(jref_dimension.group(1)) if jref_dimension else None
        ),
        "reference_exception_size": int(jref_size.group(1)) if jref_size else None,
        "t_denominator_unit": "DT_UNIT=1" in stdout,
        "c_denominator_unit": "DC_UNIT=1" in stdout,
        "reference_cofactor_unit": "REF_UNIT=1" in stdout,
        "relation_t": relation_summary(relation_t),
        "relation_c": relation_summary(relation_c),
        "relation_rb": relation_summary(relation_rb),
        "equation_summaries": [
            {
                "degree": sp.Poly(value, *variables, modulus=PRIME).total_degree(),
                "terms": len(sp.Poly(value, *variables, modulus=PRIME).terms()),
                "expression": singular(value),
            }
            for value in equations
        ],
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
    }


@app.local_entrypoint()
def main(
    signs: str = "-1:-1,-1:1,1:-1,1:1",
    charts: str = "3",
):
    selected_signs = tuple(
        tuple(int(value) for value in pair.split(":"))
        for pair in signs.split(",") if pair
    )
    cases = tuple(
        (epsilon_1, epsilon_2, int(chart))
        for epsilon_1, epsilon_2 in selected_signs
        for chart in charts.split(",") if chart
    )
    rows = list(analyze.map(cases, order_outputs=True, return_exceptions=True))
    normalized_rows = []
    for case, row in zip(cases, rows):
        if isinstance(row, BaseException):
            normalized_rows.append({
                "epsilon": list(case[:2]), "chart": case[2],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            normalized_rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell14-kernel-structure-v1",
        "field": PRIME,
        "scope": "Exploratory exact low-degree kernel presentation for cell 14.",
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "rows": normalized_rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                key: row.get(key) for key in (
                    "epsilon", "chart", "status", "unit", "dimension",
                    "basis_size", "etr_dimension", "etr_size",
                    "erb_dimension", "erb_size",
                    "t_denominator_unit", "c_denominator_unit",
                    "reference_cofactor_unit",
                    "t_exception_dimension", "t_exception_size",
                    "c_exception_dimension", "c_exception_size",
                    "reference_exception_dimension", "reference_exception_size",
                )
            }
            for row in normalized_rows
        ],
    }, sort_keys=True))
