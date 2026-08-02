#!/usr/bin/env python3
"""Triangularize the deployed cell-0 positive common curve on Modal."""

import hashlib
import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
COMMON = DIRECTORY / "rate_half_kb_positive_433_1a_common_vieta_compiler.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell0_common_triangle_result.json"
REMOTE_COMMON = "/root/rate_half_kb_positive_433_1a_common_vieta_compiler.py"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell0-common-triangle")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(COMMON, REMOTE_COMMON)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=2.0, memory=4096, timeout=180)
def triangularize():
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_common_vieta_compiler import compile_cell

    variables, equations, metadata = compile_cell(0, -1, -1, strip_fast=True)
    t, r, c, b = variables
    labels = metadata["labels"]
    guards = [
        labels[left] - labels[right]
        for left in range(5) for right in range(left + 1, 5)
    ]
    guards.extend((
        r, t, b, c, b - 1, b + 1, c - 1, c + 1, b - c, b + c,
    ))
    guard_product = sp.prod(guards)

    def singular(expression):
        return str(
            sp.Poly(expression, t, r, c, b, modulus=PRIME).as_expr()
        ).replace("**", "^")

    equation_text = [singular(value) for value in equations]
    guard_text = singular(guard_product)
    definitions = "\n".join(
        f"poly f{index}={value};"
        for index, value in enumerate(equation_text)
    )
    program = f"""
ring R={PRIME},(u,t,r,c,b),(dp(1),dp(4));
option(redSB);
{definitions}
poly guard={guard_text};
ideal F=f0,f1,f2,f3,f4,f5,u*guard-1;
ideal GF=std(F);
print("BEGIN_BLOCK_SUMMARY"); print(dim(GF)); print(size(GF));
print("BEGIN_BLOCK_BASIS"); GF; print("END_BLOCK_BASIS");
ideal E=eliminate(GF,u);
ring P={PRIME},(r,c,b,t),lp;
option(redSB);
ideal EP=imap(R,E);
ideal GP=std(EP);
print("BEGIN_LEX_SUMMARY"); print(dim(GP)); print(size(GP));
print("BEGIN_LEX_BASIS"); GP; print("END_LEX_BASIS");
quit;
"""
    header = {
        "field": PRIME,
        "cell": 0,
        "epsilon": [-1, -1],
        "matching": metadata["matching"],
        "equation_sha256": [digest(value) for value in equation_text],
        "guard_sha256": digest(guard_text),
        "program_sha256": digest(program),
    }
    b_roots = [
        ((6 + root) * pow(2, -1, PRIME)) % PRIME
        for root in sp.sqrt_mod(32, PRIME, all_roots=True)
    ]
    rational_witnesses = []
    for b_value in b_roots:
        t_value = 2
        r_value = (-16711679 * t_value**2) % PRIME
        denominator = (
            b_value - 3 - 33423356 * t_value**2
        ) % PRIME
        c_value = (
            (
                16711679 * (b_value + 1)
                - 16711680 * (b_value - 1) * t_value**2
            )
            * pow(denominator, -1, PRIME)
        ) % PRIME
        substitutions = {
            t: t_value, r: r_value, c: c_value, b: b_value,
        }
        equation_values = [
            int(sp.expand(equation).subs(substitutions)) % PRIME
            for equation in equations
        ]
        guard_values = [
            int(sp.expand(guard).subs(substitutions)) % PRIME
            for guard in guards
        ]
        rational_witnesses.append({
            "t": t_value,
            "r": r_value,
            "c": c_value,
            "b": b_value,
            "equation_values": equation_values,
            "guard_values": guard_values,
            "valid": not any(equation_values) and all(guard_values),
        })
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
            "partial_stdout": decoded(error.stdout)[-50000:],
            "partial_stderr": decoded(error.stderr)[-4000:],
        }
    stdout = process.stdout
    valid = (
        process.returncode == 0
        and "END_LEX_BASIS" in stdout
        and "?" not in stdout
    )
    return {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "rational_witnesses": rational_witnesses,
        "stdout": stdout[-50000:],
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell0-common-triangle-v1",
        "scope": (
            "Exact deployed-field localized cell-0 common block and lex "
            "bases; no rational-point, outside, route, K3, or Prize claim."
        ),
        "result": triangularize.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "status": output["result"].get("status"),
    }, sort_keys=True))
