#!/usr/bin/env python3
"""Probe the projected common curve for repeated-BC cell-3 BC-."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess
import time

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cells3_6_compact_kernel_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell3_bcminus_curve_probe_result.json"
)
REMOTE_SOURCE = "/root/compact.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-o0b-cell3-bcminus-curve-probe")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(SOURCE, REMOTE_SOURCE)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=4)
def probe(epsilon):
    import sympy as sp

    started = time.perf_counter()
    payload = json.loads(Path(REMOTE_SOURCE).read_text())
    row = next(item for item in payload["rows"]
               if item["cell"] == 3 and item["epsilon"] == list(epsilon)
               and item["bc_sign"] == -1)
    t, r, c, b = sp.symbols("t r c b")
    equations = [sp.sympify(item["expression"])
                 for item in row["compact_equations"]]
    sign_product = epsilon[0]*epsilon[1]
    substitution = {t: sign_product*r**2}
    transformed = [
        sp.Poly(sp.expand(value.subs(substitution)), r, c, b, modulus=PRIME)
        for value in equations
    ]
    common_gcd = sp.gcd(sp.gcd(transformed[0], transformed[1]), transformed[2])
    primitive = []
    for value in transformed:
        quotient, remainder = sp.div(value, common_gcd)
        if not remainder.is_zero:
            raise RuntimeError("nonexact transformed gcd")
        primitive.append(quotient.monic())

    labels = (1, t**2, -1, r**2, -r**2)
    guards = [
        labels[left]-labels[right]
        for left in range(5) for right in range(left+1, 5)
    ]
    guards.extend((r, t, b, c, b-1, b+1, c-1, c+1, b-c, b+c))
    guard = sp.Poly(
        sp.expand(sp.prod(guards).subs(substitution)), r, c, b,
        modulus=PRIME,
    )

    def singular(value):
        return str(value.as_expr()).replace("**", "^")

    definitions = "\n".join(
        f"poly f{index}={singular(value)};"
        for index, value in enumerate(primitive)
    )
    program = f"""
ring R={PRIME},(z,r,c,b),(dp(1),dp(1),dp(2));
option(redSB);
{definitions}
poly guard={singular(guard)};
ideal I=f0,f1,f2,z*guard-1;
ideal G=std(I);
print("FULL_BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
print("FULL_END");
ideal E=eliminate(G,z*r); ideal H=std(E);
print("ELIM_BEGIN"); print("DIM="+string(dim(H))); print("SIZE="+string(size(H)));
print(H); print("ELIM_END"); print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=150,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "epsilon": list(epsilon), "status": "TIMEOUT",
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
            "partial_stdout": (error.stdout or "")[-8000:],
            "partial_stderr": (error.stderr or "")[-2000:],
            "seconds": time.perf_counter()-started,
        }
    stdout = process.stdout
    match = re.search(r"ELIM_BEGIN\n(.*?)\nELIM_END", stdout, re.DOTALL)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    return {
        "epsilon": list(epsilon),
        "status": "COMPLETE" if valid and match else "ERROR",
        "substitution": {"t": f"{sign_product}*r^2"},
        "transformed_degrees": [value.total_degree() for value in transformed],
        "transformed_terms": [len(value.terms()) for value in transformed],
        "removed_gcd": {
            "degree": common_gcd.total_degree(),
            "terms": len(common_gcd.terms()),
            "expression": str(common_gcd.as_expr()),
        },
        "primitive_degrees": [value.total_degree() for value in primitive],
        "primitive_terms": [len(value.terms()) for value in primitive],
        "full_dimension": int(re.search(r"DIM=(-?\d+)", stdout).group(1))
            if "DIM=" in stdout else None,
        "elimination_output": match.group(1).strip() if match else None,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-2000:],
        "seconds": time.perf_counter()-started,
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
        "schema": "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-curve-probe-v1",
        "scope": (
            "Exact guard-saturated projection of the four cell-3 BC- common "
            "curves to target coordinates (c,b); outside systems unpaid."
        ),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "status_counts": dict(sorted(Counter(
            row["status"] for row in rows
        ).items())),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "status_counts": output["status_counts"],
        "rows": [{
            "epsilon": row["epsilon"], "status": row["status"],
            "full_dimension": row.get("full_dimension"),
            "elimination_output": row.get("elimination_output"),
            "seconds": row.get("seconds"),
        } for row in rows],
    }, sort_keys=True))
