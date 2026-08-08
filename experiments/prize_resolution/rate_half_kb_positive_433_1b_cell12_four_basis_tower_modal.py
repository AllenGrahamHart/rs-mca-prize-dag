#!/usr/bin/env python3
"""Compile guarded four-basis presentations of the cell-12 common curve."""

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
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json"
)
REMOTE_STRUCTURE = "/root/structure.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell12-four-basis-tower")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=2)
def compile_tower(case):
    import sympy as sp

    epsilon_1, epsilon_2, c_row_index = case

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

    def summary(polynomial):
        text = str(polynomial.as_expr())
        return {
            "degrees": (
                [None] * len(polynomial.gens) if polynomial.is_zero
                else [int(polynomial.degree(value)) for value in polynomial.gens]
            ),
            "total_degree": (
                None if polynomial.is_zero else int(polynomial.total_degree())
            ),
            "terms": len(polynomial.terms()),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "expression": text,
        }

    def singular(polynomial):
        return str(polynomial.as_expr()).replace("**", "^")

    def factor_profile(polynomial):
        coefficient, factors = sp.factor_list(
            polynomial.as_expr(), modulus=PRIME
        )
        return {
            "coefficient": int(coefficient) % PRIME,
            "factors": [
                {
                    **summary(sp.Poly(factor, *polynomial.gens, modulus=PRIME)),
                    "multiplicity": int(multiplicity),
                }
                for factor, multiplicity in factors
            ],
        }

    def univariate_roots(polynomial, variable):
        value = sp.Poly(polynomial.as_expr(), variable, modulus=PRIME)
        _, factors = sp.factor_list(value.as_expr(), variable, modulus=PRIME)
        roots = []
        for factor, multiplicity in factors:
            factor_polynomial = sp.Poly(factor, variable, modulus=PRIME)
            if factor_polynomial.degree() != 1:
                continue
            leading, constant = (
                int(coefficient) % PRIME
                for coefficient in factor_polynomial.all_coeffs()
            )
            root = (-constant * pow(leading, -1, PRIME)) % PRIME
            roots.extend([root] * int(multiplicity))
        return sorted(roots)

    payload = json.loads(Path(REMOTE_STRUCTURE).read_text())
    rows = [
        row for row in payload.get("rows", [])
        if row["epsilon"] == [epsilon_1, epsilon_2]
    ]
    signatures = {
        tuple(item["sha256"] for item in row["lex_basis"])
        for row in rows
    }
    if not payload.get("complete") or len(rows) != 6 or len(signatures) != 1:
        raise RuntimeError("invalid structure payload")
    basis = [parse_singular(item["expression"]) for item in rows[0]["lex_basis"]]
    base = sp.Poly(basis[0].as_expr(), t, r, modulus=PRIME)
    b_relation = basis[1]
    b_polynomial = sp.Poly(b_relation.as_expr(), b)
    if b_polynomial.degree() != 2:
        raise RuntimeError("expected quadratic b relation")
    b_leading = sp.Poly(
        b_polynomial.coeff_monomial(b**2), t, r, modulus=PRIME
    )
    b_linear = sp.Poly(
        b_polynomial.coeff_monomial(b), t, r, modulus=PRIME
    )
    b_constant = sp.Poly(
        b_polynomial.coeff_monomial(1), t, r, modulus=PRIME
    )
    c_relation = basis[c_row_index - 1]
    c_polynomial = sp.Poly(c_relation.as_expr(), c)
    if c_polynomial.degree() != 1:
        raise RuntimeError("expected linear c relation")
    c_leading = sp.Poly(
        c_polynomial.coeff_monomial(c), b, t, r, modulus=PRIME
    )
    c_constant = sp.Poly(
        c_polynomial.coeff_monomial(1), b, t, r, modulus=PRIME
    )
    discriminant = sp.Poly(
        sp.discriminant(base.as_expr(), t), r, modulus=PRIME
    )

    definitions = "\n".join(
        f"poly k{index}={singular(polynomial)};"
        for index, polynomial in enumerate(basis, start=1)
    )
    reductions = "\n".join(
        f'print("ROW={index},BEGIN"); print(reduce(k{index},Q)); '
        f'print("ROW={index},END");'
        for index in range(1, 9)
    )
    guard = "*".join((
        "b", "c", "r", "t", "(b-1)", "(b+1)", "(c-1)", "(c+1)",
        "(b-c)", "(b+c)", "(r^2-1)", "(r^2+1)", "(t^2-1)",
        "(t^2+1)", "(t^2-r^2)", "(t^2+r^2)",
    ))
    program = f"""
ring R={PRIME},(z,c,b,t,r),dp;
option(redSB);
{definitions}
poly frel={singular(base)};
poly brel={singular(b_relation)};
poly bden={singular(b_leading)};
poly crel={singular(c_relation)};
poly cden={singular(c_leading)};
poly H={guard};
ideal K=k1,k2,k3,k4,k5,k6,k7,k8,z*H-1; K=slimgb(K);
ideal Q=frel,brel,crel,z*H*bden*cden-1; Q=slimgb(Q);
ideal JB=K,bden; JB=slimgb(JB);
ideal JC=K,cden; JC=slimgb(JC);
print("BEGIN");
print("KDIM="+string(dim(K))); print("KSIZE="+string(size(K)));
print("QDIM="+string(dim(Q))); print("QSIZE="+string(size(Q)));
print("JBDIM="+string(dim(JB))); print("JBSIZE="+string(size(JB)));
print("JCDIM="+string(dim(JC))); print("JCSIZE="+string(size(JC)));
if ((size(JB)==1) && (JB[1]==1)) {{ print("JBUNIT=1"); }}
else {{ print("JBUNIT=0"); }}
if ((size(JC)==1) && (JC[1]==1)) {{ print("JCUNIT=1"); }}
else {{ print("JCUNIT=0"); }}
{reductions}
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
            "c_row_index": c_row_index,
            "status": "TIMEOUT",
            "partial_stdout": stdout[-2000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    remainders = []
    for index in range(1, 9):
        match = re.search(
            rf"ROW={index},BEGIN\n(.*?)\nROW={index},END",
            process.stdout, re.DOTALL,
        )
        remainders.append(
            "".join(match.group(1).split()) if match else None
        )
    valid = (
        process.returncode == 0
        and "END" in process.stdout
        and "?" not in process.stdout
    )

    def integer(label):
        match = re.search(rf"(?:^|\n){label}=(-?\d+)", process.stdout)
        return int(match.group(1)) if match else None

    return {
        "epsilon": [epsilon_1, epsilon_2],
        "c_row_index": c_row_index,
        "status": "COMPLETE" if valid else "ERROR",
        "base": summary(base),
        "base_discriminant": summary(discriminant),
        "base_discriminant_factors": factor_profile(discriminant),
        "base_discriminant_squarefree": sp.gcd(
            discriminant, discriminant.diff()
        ).degree() == 0,
        "b_relation": summary(b_relation),
        "b_leading": summary(b_leading),
        "b_leading_factors": factor_profile(b_leading),
        "b_leading_deployed_roots": univariate_roots(b_leading, r),
        "b_linear": summary(b_linear),
        "b_constant": summary(b_constant),
        "b_palindromic": b_leading == b_constant,
        "c_relation": summary(c_relation),
        "c_leading": summary(c_leading),
        "c_leading_deployed_roots": (
            univariate_roots(c_leading, r)
            if c_leading.degree(b) == 0 and c_leading.degree(t) == 0
            else None
        ),
        "c_constant": summary(c_constant),
        "kernel_dimension": integer("KDIM"),
        "kernel_basis_size": integer("KSIZE"),
        "tower_dimension": integer("QDIM"),
        "tower_basis_size": integer("QSIZE"),
        "b_boundary_unit": "JBUNIT=1" in process.stdout,
        "b_boundary_dimension": integer("JBDIM"),
        "b_boundary_basis_size": integer("JBSIZE"),
        "c_boundary_unit": "JCUNIT=1" in process.stdout,
        "c_boundary_dimension": integer("JCDIM"),
        "c_boundary_basis_size": integer("JCSIZE"),
        "remainders": remainders,
        "exact": remainders == ["0"] * 8,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stdout_tail": process.stdout[-2000:],
        "stderr_tail": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main():
    cases = tuple(
        (epsilon_1, epsilon_2, c_row_index)
        for epsilon_1 in (-1, 1)
        for epsilon_2 in (-1, 1)
        for c_row_index in (5, 6)
    )
    raw = list(compile_tower.map(
        cases, order_outputs=True, return_exceptions=True
    ))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]),
                "c_row_index": case[2],
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell12-four-basis-tower-v1",
        "field": PRIME,
        "scope": (
            "Exact quadratic-over-quadratic common tower with one linear c "
            "recovery on one guarded cell-12 chart; no outside claim."
        ),
        "source_structure_sha256": hashlib.sha256(
            STRUCTURE.read_bytes()
        ).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                key: row.get(key) for key in (
                    "epsilon", "c_row_index", "status", "kernel_dimension",
                    "tower_dimension", "tower_basis_size", "b_boundary_unit",
                    "c_boundary_unit", "exact", "b_palindromic",
                    "base_discriminant_squarefree"
                )
            }
            for row in rows
        ],
    }, sort_keys=True))
