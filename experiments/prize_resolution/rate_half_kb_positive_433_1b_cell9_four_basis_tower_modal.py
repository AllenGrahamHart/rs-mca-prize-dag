#!/usr/bin/env python3
"""Compile guarded four-basis presentations of the cell-9 common curve."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
STRUCTURE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_global_common_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell9_four_basis_tower_result.json"
)
REMOTE_STRUCTURE = "/root/structure.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell9-four-basis-tower")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=4)
def compile_tower(case):
    import sympy as sp

    epsilon_1, epsilon_2, b_row_index, c_row_index = case
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

    payload = json.loads(Path(REMOTE_STRUCTURE).read_text())
    row = next(
        item for item in payload["rows"]
        if item["epsilon"] == [epsilon_1, epsilon_2]
    )
    if row.get("status") != "COMPLETE" or not row.get("ideals_equal"):
        raise RuntimeError("invalid global common-locus row")
    basis = [parse_singular(item["expression"]) for item in row["lex_basis"]]
    if len(basis) != 7:
        raise RuntimeError("expected seven-row cell-9 lex basis")

    base = sp.Poly(basis[0].as_expr(), t, r, modulus=PRIME)
    if base.degree(t) != 2:
        raise RuntimeError("expected quadratic t relation")
    b_relation = basis[b_row_index - 1]
    b_polynomial = sp.Poly(b_relation.as_expr(), b)
    if b_polynomial.degree() != 2:
        raise RuntimeError("expected quadratic b relation")
    b_leading = sp.Poly(
        b_polynomial.coeff_monomial(b**2), t, r, modulus=PRIME
    )
    c_relation = basis[c_row_index - 1]
    c_polynomial = sp.Poly(c_relation.as_expr(), c)
    if c_polynomial.degree() != 1:
        raise RuntimeError("expected linear c relation")
    c_leading = sp.Poly(
        c_polynomial.coeff_monomial(c), b, t, r, modulus=PRIME
    )
    b_cover_leadings = []
    for index in (2, 3):
        polynomial = sp.Poly(basis[index - 1].as_expr(), b)
        b_cover_leadings.append(sp.Poly(
            polynomial.coeff_monomial(b**2), t, r, modulus=PRIME
        ))
    c_cover_leadings = []
    for index in (4, 5, 6):
        polynomial = sp.Poly(basis[index - 1].as_expr(), c)
        c_cover_leadings.append(sp.Poly(
            polynomial.coeff_monomial(c), b, t, r, modulus=PRIME
        ))

    definitions = "\n".join(
        f"poly k{index}={singular(polynomial)};"
        for index, polynomial in enumerate(basis, start=1)
    )
    reductions = "\n".join(
        f'print("ROW={index},BEGIN"); print(reduce(k{index},Q)); '
        f'print("ROW={index},END");'
        for index in range(1, 8)
    )
    b_cover_definitions = "\n".join(
        f"poly bc{index}={singular(polynomial)};"
        for index, polynomial in enumerate(b_cover_leadings, start=1)
    )
    c_cover_definitions = "\n".join(
        f"poly cc{index}={singular(polynomial)};"
        for index, polynomial in enumerate(c_cover_leadings, start=1)
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
{b_cover_definitions}
{c_cover_definitions}
poly H={guard};
ideal K=k1,k2,k3,k4,k5,k6,k7,z*H-1; K=slimgb(K);
ideal Q=frel,brel,crel,z*H*bden*cden-1; Q=slimgb(Q);
ideal JB=K,bc1,bc2; JB=slimgb(JB);
ideal JC=K,cc1,cc2,cc3; JC=slimgb(JC);
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
        stdout = error.stdout or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "b_row_index": b_row_index,
            "c_row_index": c_row_index,
            "status": "TIMEOUT",
            "partial_stdout": stdout[-2000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }

    def integer(label):
        match = re.search(rf"(?:^|\n){label}=(-?\d+)", process.stdout)
        return int(match.group(1)) if match else None

    remainders = []
    for index in range(1, 8):
        match = re.search(
            rf"ROW={index},BEGIN\n(.*?)\nROW={index},END",
            process.stdout, re.DOTALL,
        )
        remainders.append("".join(match.group(1).split()) if match else None)
    valid = (
        process.returncode == 0 and "END" in process.stdout
        and "?" not in process.stdout
    )
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "b_row_index": b_row_index,
        "c_row_index": c_row_index,
        "status": "COMPLETE" if valid else "ERROR",
        "base": summary(base),
        "b_relation": summary(b_relation),
        "b_leading": summary(b_leading),
        "c_relation": summary(c_relation),
        "c_leading": summary(c_leading),
        "kernel_dimension": integer("KDIM"),
        "kernel_basis_size": integer("KSIZE"),
        "tower_dimension": integer("QDIM"),
        "tower_basis_size": integer("QSIZE"),
        "b_cover_complete": "JBUNIT=1" in process.stdout,
        "b_cover_boundary_dimension": integer("JBDIM"),
        "b_cover_boundary_basis_size": integer("JBSIZE"),
        "c_cover_complete": "JCUNIT=1" in process.stdout,
        "c_cover_boundary_dimension": integer("JCDIM"),
        "c_cover_boundary_basis_size": integer("JCSIZE"),
        "remainders": remainders,
        "exact": remainders == ["0"] * 7,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stdout_tail": process.stdout[-2000:],
        "stderr_tail": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main():
    cases = tuple(
        (epsilon_1, epsilon_2, b_row_index, c_row_index)
        for epsilon_1 in (-1, 1) for epsilon_2 in (-1, 1)
        for b_row_index in (2, 3)
        for c_row_index in (4, 5, 6)
    )
    raw = list(compile_tower.map(
        cases, order_outputs=True, return_exceptions=True
    ))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "b_row_index": case[2],
                "c_row_index": case[3],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell9-four-basis-tower-v1",
        "field": PRIME,
        "scope": (
            "Exact quadratic-over-quadratic common tower with one linear c "
            "recovery on the guarded cell-9 chart; no source-cut, outside, "
            "cell, route, K3, or Prize claim."
        ),
        "source_structure_sha256": hashlib.sha256(
            STRUCTURE.read_bytes()
        ).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [{key: row.get(key) for key in (
            "epsilon", "c_row_index", "status", "kernel_dimension",
            "b_row_index", "tower_dimension", "tower_basis_size",
            "b_cover_complete", "c_cover_complete", "exact",
        )} for row in rows],
    }, sort_keys=True))
