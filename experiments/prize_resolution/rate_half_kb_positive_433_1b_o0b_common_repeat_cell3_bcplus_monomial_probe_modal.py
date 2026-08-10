#!/usr/bin/env python3
"""Certify the guarded cell-3 repeated-BC+ common torus locus."""

import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
KERNEL = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cells3_6_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_monomial_probe_result.json"
)
REMOTE_KERNEL = "/root/compact.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-o0b-cell3-bcplus-monomial")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=4)
def probe(epsilon):
    import sympy as sp

    payload = json.loads(Path(REMOTE_KERNEL).read_text())
    row = next(item for item in payload["rows"]
               if item["cell"] == 3 and item["epsilon"] == list(epsilon)
               and item["bc_sign"] == 1)
    t, r, c, b, u = sp.symbols("t r c b u")
    equations = [sp.sympify(item["expression"])
                 for item in row["compact_equations"]]
    sign_product = epsilon[0] * epsilon[1]
    substitution = {t: sign_product * r**2, b: -u**-3, c: u}
    common_labels = (1, t**2, -1, r**2, -r**2)
    guards = [
        common_labels[left] - common_labels[right]
        for left in range(5) for right in range(left + 1, 5)
    ]
    guards.extend((r, t, b, c, b - 1, b + 1, c - 1, c + 1, b - c, b + c))
    guard_numerator, _ = sp.fraction(sp.cancel(sp.prod(guards).subs(substitution)))
    guard_polynomial = sp.Poly(sp.expand(guard_numerator), r, u, modulus=PRIME).monic()
    numerators = []
    for equation in equations:
        numerator, _ = sp.fraction(sp.cancel(equation.subs(substitution)))
        polynomial = sp.Poly(sp.expand(numerator), r, u, modulus=PRIME)
        numerators.append(polynomial.monic().as_expr())
    common_gcd = sp.gcd(sp.gcd(
        sp.Poly(numerators[0], r, u, modulus=PRIME),
        sp.Poly(numerators[1], r, u, modulus=PRIME)),
        sp.Poly(numerators[2], r, u, modulus=PRIME),
    ).monic().as_expr()
    torus_core = sp.Poly(
        u*r**2
        - epsilon[0]*(IOTA + epsilon[1])*r*(u**2 + 1)
        + epsilon[1]*IOTA*u,
        r, u, modulus=PRIME,
    ).monic().as_expr()
    expected_gcd = sp.Poly(
        r**2*(u**2 - 1)**2*torus_core,
        r, u, modulus=PRIME,
    ).monic().as_expr()
    if not sp.Poly(common_gcd - expected_gcd, r, u, modulus=PRIME).is_zero:
        raise RuntimeError("torus-core gcd identity")
    primitive = []
    for numerator in numerators:
        quotient, remainder = sp.div(
            sp.Poly(numerator, r, u, modulus=PRIME),
            sp.Poly(common_gcd, r, u, modulus=PRIME),
        )
        if not remainder.is_zero:
            raise RuntimeError("gcd division")
        primitive.append(quotient.monic().as_expr())
    basis = sp.groebner(primitive, r, u, modulus=PRIME, order="lex")

    def singular(expression):
        return str(sp.Poly(expression, r, u, modulus=PRIME).as_expr()).replace("**", "^")

    definitions = "\n".join(
        f"poly f{index}={singular(value)};"
        for index, value in enumerate(primitive)
    )
    program = f"""
ring R={PRIME},(z,r,u),(dp(1),dp(2));
option(redSB);
{definitions}
poly guard={singular(guard_polynomial.as_expr())};
ideal I=f0,f1,f2,z*guard-1;
ideal G=std(I);
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }} else {{ print("UNIT=0"); }}
print("BASIS_BEGIN"); print(G); print("BASIS_END"); print("END"); quit;
"""
    process = subprocess.run(
        ["Singular", "--quiet"], input=program, capture_output=True,
        text=True, timeout=140,
    )
    stdout = process.stdout
    if process.returncode or "END" not in stdout or "?" in stdout:
        raise RuntimeError(f"Singular saturation failed: {process.stderr[-1000:]}")
    basis_match = re.search(r"BASIS_BEGIN\n(.*?)\nBASIS_END", stdout, re.DOTALL)

    def singular_original(expression):
        return str(sp.Poly(expression, t, r, c, b, modulus=PRIME).as_expr()).replace("**", "^")

    original_definitions = "\n".join(
        f"poly q{index}={singular_original(value)};"
        for index, value in enumerate(equations)
    )
    direct_program = f"""
ring S={PRIME},(z,t,r,c,b,u),(dp(1),dp(5));
option(redSB);
{original_definitions}
poly guard={singular_original(sp.prod(guards))};
ideal I=q0,q1,q2,z*guard-1; ideal G=std(I);
print("ORIGINAL_BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
print("T_REL_BEGIN"); print(reduce(t-({sign_product})*r^2,G)); print("T_REL_END");
print("MONOMIAL_REL_BEGIN"); print(reduce(c^3*b+1,G)); print("MONOMIAL_REL_END");
ideal J=q0,q1,q2,z*guard-1,u-c,b*u^3+1; ideal H=std(J);
print("PARAM_BEGIN"); print("DIM="+string(dim(H))); print("SIZE="+string(size(H)));
if ((size(H)==1) && (H[1]==1)) {{ print("UNIT=1"); }} else {{ print("UNIT=0"); }}
print("PARAM_END"); print("END"); quit;
"""
    direct_process = subprocess.run(
        ["Singular", "--quiet"], input=direct_program, capture_output=True,
        text=True, timeout=140,
    )
    direct_stdout = direct_process.stdout
    if direct_process.returncode or "PARAM_END" not in direct_stdout or "?" in direct_stdout:
        raise RuntimeError(f"direct parameter audit failed: {direct_process.stderr[-1000:]}")

    def between(text, left, right):
        match = re.search(rf"{left}\n(.*?)\n{right}", text, re.DOTALL)
        return "".join(match.group(1).split()) if match else None

    def summary(expression):
        polynomial = sp.Poly(expression, r, u, modulus=PRIME)
        text = str(polynomial.as_expr())
        output = {
            "degree": polynomial.total_degree(),
            "degree_r": polynomial.degree(r),
            "degree_u": polynomial.degree(u),
            "terms": len(polynomial.terms()),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
            "expression": text,
        }
        return output

    return {
        "epsilon": list(epsilon),
        "status": "COMPLETE",
        "substitution": {
            "t": f"{sign_product}*r^2", "b": "-u^-3", "c": "u",
        },
        "numerators": [summary(value) for value in numerators],
        "removed_gcd": summary(common_gcd),
        "torus_core": summary(torus_core),
        "gcd_identity": True,
        "primitive_equations": [summary(value) for value in primitive],
        "groebner_basis": [summary(value) for value in basis.polys],
        "is_zero_dimensional": basis.is_zero_dimensional,
        "transformed_guard": summary(guard_polynomial.as_expr()),
        "saturated_unit": "UNIT=1" in stdout,
        "saturated_dimension": int(re.search(r"DIM=(-?\d+)", stdout).group(1)),
        "saturated_basis_size": int(re.search(r"SIZE=(\d+)", stdout).group(1)),
        "saturated_basis": basis_match.group(1).strip() if basis_match else None,
        "saturation_program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "original_dimension": int(re.search(
            r"ORIGINAL_BEGIN\nDIM=(-?\d+)", direct_stdout).group(1)),
        "t_relation_remainder": between(direct_stdout, "T_REL_BEGIN", "T_REL_END"),
        "monomial_relation_remainder": between(
            direct_stdout, "MONOMIAL_REL_BEGIN", "MONOMIAL_REL_END"),
        "parameter_unit": "PARAM_BEGIN" in direct_stdout and "UNIT=1" in direct_stdout,
        "parameter_dimension": int(re.search(
            r"PARAM_BEGIN\nDIM=(-?\d+)", direct_stdout).group(1)),
        "direct_program_sha256": hashlib.sha256(direct_program.encode()).hexdigest(),
    }


@app.local_entrypoint()
def main():
    cases = tuple(itertools.product((-1, 1), repeat=2))
    raw = list(probe.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({"epsilon": list(case), "status": "REMOTE_ERROR",
                         "error": repr(row)})
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-torus-v1",
        "scope": (
            "Exact guarded common-locus audit for all four root-sign rows in "
            "cell 3 with repeated BC sign +1; no outside, route, or Prize claim."
        ),
        "source_sha256": hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [{
            "epsilon": row.get("epsilon"), "status": row.get("status"),
            "torus_core": (row.get("torus_core") or {}).get("expression"),
            "gcd_identity": row.get("gcd_identity"),
            "saturated_unit": row.get("saturated_unit"),
            "saturated_dimension": row.get("saturated_dimension"),
            "t_remainder": row.get("t_relation_remainder"),
            "monomial_remainder": row.get("monomial_relation_remainder"),
            "parameter_unit": row.get("parameter_unit"),
            "parameter_dimension": row.get("parameter_dimension"),
        } for row in rows],
    }, sort_keys=True))
