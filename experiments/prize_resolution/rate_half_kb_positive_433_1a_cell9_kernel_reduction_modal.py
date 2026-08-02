#!/usr/bin/env python3
"""Reduce the cell-9 common coefficient kernel modulo its lex curve basis."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
SCOUT = DIRECTORY / "rate_half_kb_positive_433_1a_remaining_lex_scout_result.json"
PROBE = DIRECTORY / "rate_half_kb_positive_433_1a_outside_edge_specialization_probe.py"
BASE = DIRECTORY / "rate_half_kb_positive_433_1a_product_base_rank_compiler.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1a_cell9_kernel_reduction_result.json"
REMOTE_SCOUT = "/root/remaining_lex_scout.json"
REMOTE_PROBE = "/root/rate_half_kb_positive_433_1a_outside_edge_specialization_probe.py"
REMOTE_BASE = "/root/rate_half_kb_positive_433_1a_product_base_rank_compiler.py"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1a-cell9-kernel-reduction")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(SCOUT, REMOTE_SCOUT)
    .add_local_file(PROBE, REMOTE_PROBE)
    .add_local_file(BASE, REMOTE_BASE)
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


@app.function(image=image, cpu=2.0, memory=4096, timeout=180)
def reduce_kernel():
    import sys

    import sympy as sp

    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_outside_edge_specialization_probe import (
        common_kernel,
    )

    scout = json.loads(Path(REMOTE_SCOUT).read_text())
    row = next(
        item for item in scout["rows"]
        if item.get("cell") == 9
        and item.get("order") == ["c", "r", "b", "t"]
    )
    basis = re.findall(r"^GP\[\d+\]=(.*)$", row["stdout"], re.MULTILINE)
    if len(basis) != 11:
        raise RuntimeError("unexpected cell-9 lex basis")

    a2, a0, b1, common_gcd, _ = common_kernel(9, -1, -1)
    names = ("a20", "a21", "a22", "a00", "a01", "a02", "b10", "b11")
    expressions = (*a2, *a0, *b1)
    c, r, b, t = sp.symbols("c r b t")

    def singular(expression):
        return str(sp.Poly(expression, c, r, b, t,
                           modulus=PRIME).as_expr()).replace("**", "^")

    definitions = "\n".join(
        f"poly {name}={singular(expression)};"
        for name, expression in zip(names, expressions)
    )
    reductions = "\n".join(
        f'print("BEGIN_{name}"); print(reduce({name},G)); '
        f'print("END_{name}");' for name in names
    )
    program = f"""
ring R={PRIME},(c,r,b,t),lp;
option(redSB);
ideal L={','.join(basis)}; ideal G=std(L);
print("BEGIN_BASIS_SUMMARY"); print(dim(G)); print(size(G));
{definitions}
{reductions}
quit;
"""
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
            "status": "TIMEOUT", "program_sha256": digest(program),
            "partial_stdout": decoded(error.stdout)[-50000:],
            "partial_stderr": decoded(error.stderr)[-4000:],
        }
    stdout = process.stdout
    reduced = {}
    for name in names:
        match = re.search(rf"BEGIN_{name}\n(.*?)\nEND_{name}", stdout,
                          re.DOTALL)
        if match is None:
            raise RuntimeError(f"missing reduction {name}")
        reduced[name] = "".join(match.group(1).split())
    valid = process.returncode == 0 and all(
        f"END_{name}" in stdout for name in names
    ) and "?" not in stdout
    return {
        "status": "COMPLETE" if valid else "ERROR",
        "field": PRIME, "cell": 9, "epsilon": [-1, -1],
        "basis_size": len(basis),
        "basis_sha256": [digest(value) for value in basis],
        "source_program_sha256": row["program_sha256"],
        "input_shape": {
            name: {
                "degree": sp.Poly(expression, c, r, b, t,
                                  modulus=PRIME).total_degree(),
                "terms": len(sp.Poly(expression, c, r, b, t,
                                     modulus=PRIME).terms()),
            }
            for name, expression in zip(names, expressions)
        },
        "common_gcd_shape": {
            "degree": sp.Poly(common_gcd, t, r, c, b,
                              modulus=PRIME).total_degree(),
            "terms": len(sp.Poly(common_gcd, t, r, c, b,
                                 modulus=PRIME).terms()),
        },
        "reduced_coefficients": reduced,
        "reduced_sha256": {name: digest(value) for name, value in reduced.items()},
        "program_sha256": digest(program),
        "stdout": stdout[-50000:], "stderr": process.stderr[-4000:],
    }


@app.local_entrypoint()
def main():
    output = {
        "schema": "rate-half-kb-positive-433-1a-cell9-kernel-reduction-v1",
        "scope": (
            "Exact reduction of the unique common coefficient kernel modulo "
            "the cell-9 lex curve basis; no outside, route, K3, or Prize claim."
        ),
        "result": reduce_kernel.remote(),
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT), "status": output["result"].get("status"),
        "basis_size": output["result"].get("basis_size"),
        "reduced_lengths": {
            name: len(value) for name, value in
            output["result"].get("reduced_coefficients", {}).items()
        },
    }, sort_keys=True))
