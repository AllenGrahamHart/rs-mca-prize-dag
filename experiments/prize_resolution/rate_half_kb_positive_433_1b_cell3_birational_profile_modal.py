#!/usr/bin/env python3
"""Profile block-lex recovery over the small cell-3 (t,r) projection."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
PRODUCT = DIRECTORY / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_birational_profile_result.json"
REMOTE_PRODUCT = "/root/product.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-cell3-birational-profile")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(PRODUCT, REMOTE_PRODUCT)
)


@app.function(image=image, cpu=4.0, memory=8192, timeout=300, max_containers=4)
def profile(case):
    import sympy as sp

    epsilon_1, epsilon_2, chart = case
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

    equations = [strip_factors(value) for value in equations]
    product_payload = json.loads(Path(REMOTE_PRODUCT).read_text())
    product_row = next(
        row for row in product_payload["rows"] if row["cell"] == 3
    )
    cofactor = sp.sympify(product_row["stripped_expressions"][chart])
    guards = [cofactor, *route_guards]

    def singular(expression):
        return str(
            sp.Poly(expression, *variables, modulus=PRIME).as_expr()
        ).replace("**", "^")

    equation_definitions = "\n".join(
        f"poly q{index}={singular(value)};"
        for index, value in enumerate(equations)
    )
    guard_definitions = "\n".join(
        f"poly h{index}={singular(value)};"
        for index, value in enumerate(guards)
    )
    saturation_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G);"
        for index in range(len(guards))
    )
    c_boundary_stages = "\n".join(
        f"list CS{index}=sat(Jc,H{index}); Jc=CS{index}[1]; Jc=slimgb(Jc);"
        for index in range(len(guards))
    )
    b_boundary_stages = "\n".join(
        f"list BS{index}=sat(Jb,H{index}); Jb=BS{index}[1]; Jb=slimgb(Jb);"
        for index in range(len(guards))
    )
    c_denominator = t - epsilon_1 * epsilon_2 * r * r
    b_leading = r * r * (t + epsilon_2 * IOTA * r)
    quotient_reductions = "\n".join(
        f'print("QROW={index},BEGIN"); print(reduce(K[{index + 1}],Q)); '
        f'print("QROW={index},END");'
        for index in range(10)
    )
    quotient_saturation_stages = "\n".join(
        f"ideal LH{index}=imap(R,H{index}); "
        f"list QS{index}=sat(Q,LH{index}); Q=QS{index}[1]; Q=std(Q);"
        for index in range(len(guards))
    )
    program = f"""
LIB "elim.lib";
ring R={PRIME},(t,r,c,b),dp;
option(redSB);
{equation_definitions}
{guard_definitions}
poly dc={singular(c_denominator)};
poly db={singular(b_leading)};
ideal DC=dc; ideal DB=db;
ideal I=q0,q1,q2; ideal G=slimgb(I);
{saturation_stages}
ideal Jc=G,dc; Jc=slimgb(Jc); {c_boundary_stages}
ideal Jb=G,db; Jb=slimgb(Jb); {b_boundary_stages}
print("BOUNDARY_BEGIN");
print("JC_DIM="+string(dim(Jc))); print("JC_SIZE="+string(size(Jc)));
if ((size(Jc)==1) && (Jc[1]==1)) {{ print("JC_UNIT=1"); }}
else {{ print("JC_UNIT=0"); }}
print("JB_DIM="+string(dim(Jb))); print("JB_SIZE="+string(size(Jb)));
if ((size(Jb)==1) && (Jb[1]==1)) {{ print("JB_UNIT=1"); }}
else {{ print("JB_UNIT=0"); }}
print("BOUNDARY_END");
ring L={PRIME},(c,b,t,r),lp;
option(redSB);
ideal K=imap(R,G); K=std(K);
ideal Q=K[1],K[3],K[7]; Q=std(Q);
{quotient_saturation_stages}
ideal LDC=imap(R,DC); list QSC=sat(Q,LDC); Q=QSC[1]; Q=std(Q);
ideal LDB=imap(R,DB); list QSB=sat(Q,LDB); Q=QSB[1]; Q=std(Q);
print("BEGIN"); print("DIM="+string(dim(K))); print("SIZE="+string(size(K)));
print("QDIM="+string(dim(Q))); print("QSIZE="+string(size(Q)));
{quotient_reductions}
print("LEX_BEGIN"); K; print("LEX_END"); print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=270,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "epsilon": [epsilon_1, epsilon_2], "chart": chart,
            "status": "TIMEOUT",
            "partial_stdout": (error.stdout or "")[-10000:],
            "partial_stderr": (error.stderr or "")[-2000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout
    match = re.search(r"LEX_BEGIN\n(.*?)\nLEX_END", stdout, re.DOTALL)
    raw_rows = [] if match is None else re.findall(
        r"^K\[\d+\]=(.*?)(?=^K\[\d+\]=|\Z)",
        match.group(1), re.MULTILINE | re.DOTALL,
    )

    def parse_polynomial(body):
        expression = 0
        symbols = {"c": c, "b": b, "t": t, "r": r}
        for term in re.findall(r"[+-]?[^+-]+", "".join(body.split())):
            sign = -1 if term.startswith("-") else 1
            unsigned = term.lstrip("+-")
            digits = re.match(r"\d*", unsigned).group()
            monomial = sp.Integer(int(digits or "1") * sign)
            for variable, exponent in re.findall(
                r"([cbtr])(\d*)", unsigned[len(digits):]
            ):
                monomial *= symbols[variable] ** int(exponent or "1")
            expression += monomial
        return sp.Poly(expression, c, b, t, r, modulus=PRIME)

    rows = []
    polynomials = []
    for raw in raw_rows:
        polynomial = parse_polynomial(raw)
        polynomials.append(polynomial)
        expression = str(polynomial.as_expr())
        rows.append({
            "degrees": [polynomial.degree(value) for value in (c, b, t, r)],
            "total_degree": polynomial.total_degree(),
            "terms": len(polynomial.terms()),
            "sha256": hashlib.sha256(expression.encode()).hexdigest(),
            "expression": expression if len(polynomial.terms()) <= 250 else None,
        })
    dimension = re.search(r"(?:^|\n)DIM=(-?\d+)", stdout)
    basis_size = re.search(r"(?:^|\n)SIZE=(\d+)", stdout)
    c_dimension = re.search(r"JC_DIM=(-?\d+)", stdout)
    c_size = re.search(r"JC_SIZE=(\d+)", stdout)
    b_dimension = re.search(r"JB_DIM=(-?\d+)", stdout)
    b_size = re.search(r"JB_SIZE=(\d+)", stdout)
    quotient_dimension = re.search(r"QDIM=(-?\d+)", stdout)
    quotient_size = re.search(r"QSIZE=(\d+)", stdout)
    quotient_remainders = []
    for index in range(10):
        remainder = re.search(
            rf"QROW={index},BEGIN\n(.*?)\nQROW={index},END",
            stdout,
            re.DOTALL,
        )
        quotient_remainders.append(
            "".join(remainder.group(1).split()) if remainder else None
        )
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout

    def coefficient_summary(expression, summary_variables=(t, r)):
        polynomial = sp.Poly(expression, *summary_variables, modulus=PRIME)
        text = str(polynomial.as_expr())
        return {
            "degree": polynomial.total_degree(),
            "terms": len(polynomial.terms()),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "expression": text,
        }

    b_polynomial = sp.Poly(polynomials[2].as_expr(), b)
    b_leading_actual = b_polynomial.coeff_monomial(b**2)
    b_linear = b_polynomial.coeff_monomial(b)
    b_constant = b_polynomial.coeff_monomial(1)
    b_leading_expected = r*r*(t + epsilon_2*IOTA*r)
    c_polynomial = sp.Poly(polynomials[6].as_expr(), c)
    c_denominator_actual = c_polynomial.coeff_monomial(c)
    c_constant = c_polynomial.coeff_monomial(1)
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "chart": chart,
        "status": "COMPLETE" if valid else "ERROR",
        "dimension": int(dimension.group(1)) if dimension else None,
        "basis_size": int(basis_size.group(1)) if basis_size else None,
        "c_denominator": str(c_denominator),
        "c_boundary_unit": "JC_UNIT=1" in stdout,
        "c_boundary_dimension": (
            int(c_dimension.group(1)) if c_dimension else None
        ),
        "c_boundary_size": int(c_size.group(1)) if c_size else None,
        "b_leading": str(b_leading),
        "b_boundary_unit": "JB_UNIT=1" in stdout,
        "b_boundary_dimension": (
            int(b_dimension.group(1)) if b_dimension else None
        ),
        "b_boundary_size": int(b_size.group(1)) if b_size else None,
        "basis": rows,
        "quotient_dimension": (
            int(quotient_dimension.group(1)) if quotient_dimension else None
        ),
        "quotient_basis_size": (
            int(quotient_size.group(1)) if quotient_size else None
        ),
        "quotient_remainders": quotient_remainders,
        "quotient_exact": quotient_remainders == ["0"] * 10,
        "quotient_interface": {
            "base_relation": rows[0],
            "b_relation": rows[2],
            "b_leading": coefficient_summary(b_leading_actual),
            "b_linear": coefficient_summary(b_linear),
            "b_constant": coefficient_summary(b_constant),
            "b_palindromic": sp.Poly(
                b_leading_actual-b_constant, t, r, modulus=PRIME
            ).is_zero,
            "b_leading_expected": sp.Poly(
                b_leading_actual-b_leading_expected,
                t, r, modulus=PRIME,
            ).is_zero,
            "c_relation": rows[6],
            "c_denominator": coefficient_summary(c_denominator_actual),
            "c_constant": coefficient_summary(c_constant, (b, t, r)),
            "c_denominator_expected": sp.Poly(
                c_denominator_actual-c_denominator,
                t, r, modulus=PRIME,
            ).is_zero,
        },
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-2000:],
    }


@app.local_entrypoint()
def main(
    signs: str = "-1:-1,-1:1,1:-1,1:1",
    charts: str = "0,1,2,3,4,5",
):
    selected_signs = tuple(
        tuple(int(value) for value in pair.split(":"))
        for pair in signs.split(",") if pair
    )
    selected_charts = tuple(int(value) for value in charts.split(",") if value)
    cases = tuple(
        (epsilon_1, epsilon_2, chart)
        for epsilon_1, epsilon_2 in selected_signs
        for chart in selected_charts
    )
    raw = list(profile.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "chart": case[2],
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell3-birational-profile-v1",
        "scope": (
            "Exact block-lex recovery profile above the (t,r) projection; "
            "no birationality, outside, route, or Prize claim unless certified."
        ),
        "source_product_sha256": hashlib.sha256(PRODUCT.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                "epsilon": row.get("epsilon"),
                "chart": row.get("chart"),
                "status": row.get("status"),
                "dimension": row.get("dimension"),
                "basis_size": row.get("basis_size"),
                "c_boundary": [
                    row.get("c_boundary_unit"),
                    row.get("c_boundary_dimension"),
                    row.get("c_boundary_size"),
                ],
                "b_boundary": [
                    row.get("b_boundary_unit"),
                    row.get("b_boundary_dimension"),
                    row.get("b_boundary_size"),
                ],
                "quotient_checks": (
                    {
                        key: row["quotient_interface"].get(key)
                        for key in (
                            "b_palindromic", "b_leading_expected",
                            "c_denominator_expected",
                        )
                    }
                    if row.get("quotient_interface") else None
                ),
                "quotient_exact": row.get("quotient_exact"),
                "basis_shapes": [
                    [item["degrees"], item["total_degree"], item["terms"]]
                    for item in row.get("basis", [])
                ],
            }
            for row in rows
        ],
    }, sort_keys=True))
