#!/usr/bin/env python3
"""Test the target-free DE+/DE-/BE family on the two cell-0 t=2 points."""

import hashlib
import json
from pathlib import Path
import subprocess

import modal


DIRECTORY = Path(__file__).parent
KERNEL = DIRECTORY / "rate_half_kb_positive_433_1a_cell0_kernel_reduction_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell0_t2_signed_family_result.json"
REMOTE_KERNEL = "/root/cell0_kernel_reduction_result.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell0-t2-signed-family")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(KERNEL, REMOTE_KERNEL)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=2.0, memory=4096, timeout=180, max_containers=2)
def test_branch(branch_root):
    import sympy as sp

    payload = json.loads(Path(REMOTE_KERNEL).read_text())
    branches = {
        row["b"]: row
        for row in payload["result"]["branch_rational_coefficients"]
    }
    branch = branches[branch_root]
    t, z0, z1, z2 = sp.symbols("t z0 z1 z2")
    names = ("a20", "a21", "a22", "a00", "a01", "a02", "b10", "b11")
    coefficients = {
        name: sp.Poly(
            sp.sympify(branch["normalized_coefficients"][name]["polynomial"]),
            t, modulus=PRIME,
        ).eval(2) % PRIME
        for name in names
    }

    def evaluate(prefix, source_root):
        square = source_root**2
        return sum(
            coefficients[f"{prefix}{index}"] * square**index
            for index in range(3)
        )

    roots = (z0, z1, z2)
    denominators = [evaluate("a2", root) for root in roots]
    numerators = [evaluate("a0", root) for root in roots]
    q_values = [
        root * (coefficients["b10"] + coefficients["b11"] * root**2)
        for root in roots
    ]
    d0, d1, d2 = denominators
    n0, n1, n2 = numerators
    q0, q1, q2 = q_values
    cross = q1 * d0 - q0 * d1
    equations = (
        n1 * d0 + n0 * d1,
        q0**2 * d1**2 - q1**2 * d0**2 - 4 * n0 * d0 * d1**2,
        2 * n2 * d0 * d1 - branch_root * d2 * cross,
        -2 * q2 * d0 * d1 - 2 * branch_root * d0 * d1 * d2 - d2 * cross,
    )
    common_labels = (4, 1, PRIME - 1, PRIME - 16, 16)
    guards = [z0, z1, z2, d0, d1, d2]
    for left in range(3):
        for right in range(left + 1, 3):
            guards.append(roots[left]**2 - roots[right]**2)
    for root in roots:
        guards.extend(root**2 - label for label in common_labels)
    guard_product = sp.prod(guards)

    def singular(expression):
        return str(
            sp.Poly(expression, z0, z1, z2, modulus=PRIME).as_expr()
        ).replace("**", "^")

    equation_text = [singular(value) for value in equations]
    guard_text = singular(guard_product)
    program = f"""
ring R={PRIME},(u,z0,z1,z2),(dp(1),dp(3));
option(redSB);
poly f0={equation_text[0]};
poly f1={equation_text[1]};
poly f2={equation_text[2]};
poly f3={equation_text[3]};
poly guard={guard_text};
ideal I=f0,f1,f2,f3,u*guard-1;
ideal G=std(I);
print("BEGIN_SUMMARY"); print(dim(G)); print(size(G));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); print("BEGIN_BASIS"); G; print("END_BASIS"); }}
print("END_SUMMARY");
quit;
"""
    header = {
        "field": PRIME,
        "cell": 0,
        "epsilon": [-1, -1],
        "t": 2,
        "b": branch_root,
        "coefficient_values": {name: int(value) for name, value in coefficients.items()},
        "equation_shape": [
            {
                "degree": sp.Poly(value, z0, z1, z2,
                                  modulus=PRIME).total_degree(),
                "terms": len(sp.Poly(value, z0, z1, z2,
                                     modulus=PRIME).terms()),
            }
            for value in equations
        ],
        "guard_shape": {
            "degree": sp.Poly(guard_product, z0, z1, z2,
                              modulus=PRIME).total_degree(),
            "terms": len(sp.Poly(guard_product, z0, z1, z2,
                                 modulus=PRIME).terms()),
        },
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
    stdout = process.stdout
    valid = (
        process.returncode == 0
        and "END_SUMMARY" in stdout
        and "?" not in stdout
    )
    return {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "unit": "UNIT=1" in stdout,
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main():
    roots = (1547071505, 583634934)
    rows = list(test_branch.map(roots, return_exceptions=True))
    normalized = []
    for root, row in zip(roots, rows):
        if isinstance(row, BaseException):
            normalized.append({"b": root, "status": "REMOTE_ERROR", "error": repr(row)})
        else:
            normalized.append(row)
    normalized.sort(key=lambda row: row["b"])
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell0-t2-signed-family-v1",
        "scope": (
            "Target-free DE+/DE-/BE family at the two exact cell-0 t=2 "
            "common points; specialization evidence only, no generic, "
            "outside-case, route, K3, or Prize conclusion."
        ),
        "rows": normalized,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {"b": row.get("b"), "status": row.get("status"), "unit": row.get("unit")}
            for row in normalized
        ],
    }, sort_keys=True))
