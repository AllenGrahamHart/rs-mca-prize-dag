#!/usr/bin/env python3
"""Bounded exact scout for the genuinely new cell-5 epsilon2=+1 orbit."""

import hashlib
import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMMON = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_epsilon2_plus_scout_result.json"
REMOTE_COMMON = "/root/rate_half_kb_positive_433_1a_common_vieta_compiler.py"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell5-epsilon2-plus-scout")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=2.0, memory=4096, timeout=180)
def compile_ratio_packet():
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_common_vieta_compiler import (
        IOTA,
        compile_cell,
    )

    variables, equations, metadata = compile_cell(5, -1, 1, strip_fast=True)
    t, r, c, b = variables
    x = sp.symbols("x")
    atomic_guards = (
        t - 1, t + 1, r - 1, r + 1, r - IOTA, r + IOTA,
        t - r, t + r, t - IOTA * r, t + IOTA * r, t - IOTA, t + IOTA,
        r, t, b, c, b - 1, b + 1, c - 1, c + 1, c - b, b + c,
    )

    localized = []
    removed = []
    for equation in equations[:3]:
        polynomial = sp.Poly(equation, *variables, modulus=PRIME).monic()
        row_removed = []
        for guard in atomic_guards:
            divisor = sp.Poly(guard, *variables, modulus=PRIME).monic()
            while True:
                quotient, remainder = polynomial.div(divisor)
                if not remainder.is_zero:
                    break
                polynomial = quotient.monic()
                row_removed.append(str(divisor.as_expr()))
        localized.append(polynomial.as_expr())
        removed.append(row_removed)

    ratio_polynomials = []
    b_valuations = []
    for equation in localized:
        substituted = sp.Poly(
            sp.expand(equation.subs(c, b * x)), b, t, r, x, modulus=PRIME
        )
        valuation = min(monomial[0] for monomial, _ in substituted.terms())
        b_valuations.append(valuation)
        ratio_polynomials.append(
            sp.Poly(sp.expand(substituted.as_expr() / b**valuation), b,
                    domain="EX")
        )

    degrees = [polynomial.degree() for polynomial in ratio_polynomials]
    eliminants = []
    reconstruction = None
    if degrees[0] == 1:
        linear = ratio_polynomials[0]
        a0, a1 = linear.nth(0), linear.nth(1)
        reconstruction = {"a0": str(a0), "a1": str(a1)}
        for polynomial in ratio_polynomials[1:]:
            coefficients = [
                polynomial.nth(degree)
                for degree in range(polynomial.degree() + 1)
            ]
            degree = polynomial.degree()
            cleared = sp.Integer(0)
            for power, coefficient in enumerate(coefficients):
                cleared += coefficient * (-a0) ** power * a1 ** (degree - power)
            eliminants.append(str(sp.Poly(
                sp.expand(cleared), t, r, x, modulus=PRIME
            ).monic().as_expr()))

    strings = [
        str(sp.Poly(value, *variables, modulus=PRIME).monic().as_expr())
        for value in localized
    ]
    ratio_strings = [str(polynomial.as_expr()) for polynomial in ratio_polynomials]
    output = {
        "status": "COMPLETE",
        "field": PRIME,
        "iota": IOTA,
        "cell": 5,
        "epsilon": [-1, 1],
        "labels": [str(value) for value in metadata["labels"]],
        "removed_atomic_guard_factors": removed,
        "localized_polynomials": strings,
        "localized_sha256": [digest(value) for value in strings],
        "localized_terms": [
            len(sp.Poly(value, *variables, modulus=PRIME).terms())
            for value in localized
        ],
        "b_valuations": b_valuations,
        "ratio_degrees_in_b": degrees,
        "ratio_polynomials": ratio_strings,
        "ratio_sha256": [digest(value) for value in ratio_strings],
        "linear_reconstruction": reconstruction,
        "generic_eliminants": eliminants,
        "generic_eliminant_sha256": [digest(value) for value in eliminants],
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = digest(canonical)
    return output


@app.function(image=image, cpu=2.0, memory=4096, timeout=180)
def analyze_localized_structure():
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_common_vieta_compiler import compile_cell

    variables, equations, metadata = compile_cell(5, -1, 1, strip_fast=True)
    t, r, c, b = variables
    labels = metadata["labels"]
    guards = [
        labels[left] - labels[right]
        for left in range(5) for right in range(left + 1, 5)
    ]
    guards.extend((
        r, t, b, c, b - 1, b + 1, c - 1, c + 1, b - c, b + c,
    ))

    def singular(expression):
        return str(sp.Poly(expression, t, r, c, b, modulus=PRIME).as_expr()) \
            .replace("**", "^")

    chart = [singular(value) for value in equations[:3]]
    guard = singular(sp.prod(guards))
    program = f"""
ring R={PRIME},(z,t,r,c,b),(dp(1),dp(4));
option(redSB);
poly f0={chart[0]};
poly f1={chart[1]};
poly f2={chart[2]};
poly guard={guard};
ideal S=f0,f1,f2,z*guard-1;
ideal G=std(S);
print("LOCALIZED"); print(dim(G)); print(size(G)); print(vdim(G));
ideal E=eliminate(S,z);
ring P={PRIME},(t,r,c,b),dp;
ideal EP=imap(R,E);
ideal GE=std(EP);
print("PROJECTED"); print(dim(GE)); print(size(GE)); print(vdim(GE));
print("PROJECTED_BASIS"); GE; print("END");
quit;
"""
    header = {
        "field": PRIME,
        "cell": 5,
        "epsilon": [-1, 1],
        "program_sha256": digest(program),
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=145,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            **header,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout),
            "partial_stderr": decoded(error.stderr)[-4000:],
        }
    return {
        **header,
        "status": "COMPLETE" if process.returncode == 0 else "ERROR",
        "stdout": process.stdout,
        "stderr": process.stderr[-4000:],
    }


@app.function(image=image, cpu=2.0, memory=4096, timeout=180)
def compile_deployed_atlas():
    import math
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_common_vieta_compiler import compile_cell

    variables, equations, metadata = compile_cell(5, -1, 1, strip_fast=True)
    t, r, c, b = variables
    labels = metadata["labels"]
    guards = [
        labels[left] - labels[right]
        for left in range(5) for right in range(left + 1, 5)
    ]
    guards.extend((
        r, t, b, c, b - 1, b + 1, c - 1, c + 1, b - c, b + c,
    ))

    def singular(expression):
        return str(sp.Poly(expression, t, r, c, b, modulus=PRIME).as_expr()) \
            .replace("**", "^")

    chart = [singular(value) for value in equations[:3]]
    guard = singular(sp.prod(guards))
    coefficient_lines = []
    for index in range(5):
        derivative = "bpoly"
        for _ in range(index):
            derivative = f"diff({derivative},b)"
        coefficient_lines.append(
            f"poly coefficient{index}=subst({derivative},b,0)/{math.factorial(index)};"
        )
    program = "\n".join((
        f"ring L={PRIME},(s,t,r,c,b),(dp(1),dp(4));",
        "option(redSB);",
        f"poly common0={chart[0]};",
        f"poly common1={chart[1]};",
        f"poly common2={chart[2]};",
        f"poly guard={guard};",
        "ideal S=common0,common1,common2,s*guard-1;",
        "ideal E=eliminate(S,s);",
        f"ring R={PRIME},(z0,z1,y,v,t,r,c,b),dp;",
        "option(redSB);",
        "ideal ER=imap(L,E);",
        "ideal G=std(ER);",
        f"ring Z={PRIME},(r,c,b,t),(dp(2),dp(2));",
        "option(redSB);",
        "ideal H=std(imap(R,G));",
        'print("DEPLOYED_BLOCK_BASIS"); print(dim(H)); print(size(H));',
        "ideal BT=std(eliminate(H,r*c));",
        'print("DEPLOYED_BT"); print(dim(BT)); print(size(BT));',
        "poly bpoly=BT[1];",
        'print("BPOLY_DEGREE_TERMS"); print(deg(bpoly)); print(size(bpoly));',
        *coefficient_lines,
        (
            "poly reciprocal4=coefficient0*b^4+coefficient1*b^3"
            "+coefficient2*b^2+coefficient3*b+coefficient4;"
        ),
        (
            "poly quadratic_lift=coefficient0*(b^4+2*b^2+1)"
            "+coefficient1*(b^3+b)"
            "+(coefficient2-2*coefficient0)*b^2;"
        ),
        'print("RECIPROCAL_CHECK");',
        "print(reciprocal4-bpoly==0); print(quadratic_lift-bpoly==0);",
        'print("BPOLY"); print(bpoly);',
        "ideal EC=std(eliminate(H,r));",
        'print("C_LIFT"); print(dim(EC)); print(size(EC));',
        "for (int j=1; j<=size(EC); j++)",
        "{",
        "  poly cj=diff(EC[j],c);",
        "  if ((cj!=0) && (diff(cj,c)==0))",
        "  { print(j); print(deg(EC[j])); print(size(EC[j])); print(cj); print(subst(EC[j],c,0)); }",
        "}",
        "ideal ER2=std(eliminate(H,c));",
        'print("R_LIFT"); print(dim(ER2)); print(size(ER2));',
        "for (int k=1; k<=size(ER2); k++)",
        "{",
        "  poly rk=diff(ER2[k],r);",
        "  if ((rk!=0) && (diff(rk,r)==0))",
        "  { print(k); print(deg(ER2[k])); print(size(ER2[k])); print(rk); print(subst(ER2[k],r,0)); }",
        "}",
        'print("END_ATLAS");',
        "quit;",
    ))
    header = {
        "field": PRIME,
        "cell": 5,
        "epsilon": [-1, 1],
        "program_sha256": digest(program),
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=145,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            **header,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout)[-30000:],
            "partial_stderr": decoded(error.stderr)[-4000:],
        }
    valid = (
        process.returncode == 0
        and "END_ATLAS" in process.stdout
        and "?" not in process.stdout
    )
    return {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "stdout": process.stdout[-30000:],
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main(phase: str = "scout"):
    if phase == "scout":
        ratio = compile_ratio_packet.remote()
        structure = analyze_localized_structure.remote()
        output = {
            "schema": "rate-half-kb-positive-433-1a-cell5-epsilon2-plus-scout-v1",
            "scope": (
                "Exact deployed-field common-chart scout for cell 5 signs "
                "(-1,+1); no outside equation, emptiness, route, or Prize claim."
            ),
            "ratio": ratio,
            "structure": structure,
        }
    elif phase == "atlas":
        if not RESULT.exists():
            raise RuntimeError("run phase=scout first")
        output = json.loads(RESULT.read_text())
        output["deployed_atlas"] = compile_deployed_atlas.remote()
    else:
        raise ValueError("phase must be scout or atlas")
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "phase": phase,
        "ratio_status": output.get("ratio", {}).get("status"),
        "ratio_degrees": output.get("ratio", {}).get("ratio_degrees_in_b"),
        "structure_status": output.get("structure", {}).get("status"),
        "atlas_status": output.get("deployed_atlas", {}).get("status"),
    }, sort_keys=True))
