#!/usr/bin/env python3
"""Certify the guarded genus-two tower for repeated-BC cell-3 BC-."""

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
    "cell3_bcminus_tower_certificate_result.json"
)
REMOTE_SOURCE = "/root/compact.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-o0b-cell3-bcminus-tower")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(SOURCE, REMOTE_SOURCE)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=4)
def certify(epsilon):
    import sympy as sp

    started = time.perf_counter()
    payload = json.loads(Path(REMOTE_SOURCE).read_text())
    row = next(item for item in payload["rows"]
               if item["cell"] == 3 and item["epsilon"] == list(epsilon)
               and item["bc_sign"] == -1)
    t, r, c, b = sp.symbols("t r c b")
    equations = [sp.sympify(item["expression"])
                 for item in row["compact_equations"]]
    epsilon_1, epsilon_2 = epsilon
    sign_product = epsilon_1*epsilon_2
    transformed = [
        sp.Poly(sp.expand(value.subs(t, sign_product*r**2)), r, c, b,
                modulus=PRIME)
        for value in equations
    ]
    common_gcd = sp.gcd(sp.gcd(transformed[0], transformed[1]), transformed[2])
    primitive = []
    for value in transformed:
        quotient, remainder = sp.div(value, common_gcd)
        if not remainder.is_zero:
            raise RuntimeError("nonexact transformed gcd")
        primitive.append(quotient.monic())

    projection = sp.Poly(
        b**3*c**3+b**2*c**4+3*b**2*c**3-2*b**2*c**2
        -2*b**2*c-b**2-b*c**4-2*b*c**3-2*b*c**2+3*b*c+b+c,
        r, c, b, modulus=PRIME,
    )
    r_relation = sp.Poly(
        (b*c-1)*(sign_product*r**2+epsilon_1*IOTA)
        -(epsilon_2*IOTA+1)*r*(c-b),
        r, c, b, modulus=PRIME,
    )
    labels = (1, t**2, -1, r**2, -r**2)
    guards = [
        labels[left]-labels[right]
        for left in range(5) for right in range(left+1, 5)
    ]
    guards.extend((r, t, b, c, b-1, b+1, c-1, c+1, b-c, b+c))
    guard = sp.Poly(
        sp.expand(sp.prod(guards).subs(t, sign_product*r**2)), r, c, b,
        modulus=PRIME,
    )

    def singular(value):
        return str(value.as_expr()).replace("**", "^")

    definitions = "\n".join(
        f"poly f{index}={singular(value)};"
        for index, value in enumerate(primitive)
    )
    program = f"""
ring R={PRIME},(z,r,c,b),(dp(1),dp(3));
option(redSB);
{definitions}
poly guard={singular(guard)};
poly projection={singular(projection)};
poly rrelation={singular(r_relation)};
ideal I=f0,f1,f2,z*guard-1; ideal G=std(I);
ideal J=projection,rrelation,z*guard-1; ideal H=std(J);
print("ORIGINAL_DIM="+string(dim(G)));
print("TOWER_DIM="+string(dim(H)));
print("F0_BEGIN"); print(reduce(f0,H)); print("F0_END");
print("F1_BEGIN"); print(reduce(f1,H)); print("F1_END");
print("F2_BEGIN"); print(reduce(f2,H)); print("F2_END");
print("PROJECTION_BEGIN"); print(reduce(projection,G)); print("PROJECTION_END");
print("RRELATION_BEGIN"); print(reduce(rrelation,G)); print("RRELATION_END");
print("END"); quit;
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

    def between(left, right):
        match = re.search(rf"{left}\n(.*?)\n{right}", stdout, re.DOTALL)
        return "".join(match.group(1).split()) if match else None

    remainders = {
        "primitive_0_mod_tower": between("F0_BEGIN", "F0_END"),
        "primitive_1_mod_tower": between("F1_BEGIN", "F1_END"),
        "primitive_2_mod_tower": between("F2_BEGIN", "F2_END"),
        "projection_mod_original": between("PROJECTION_BEGIN", "PROJECTION_END"),
        "r_relation_mod_original": between("RRELATION_BEGIN", "RRELATION_END"),
    }
    valid = (
        process.returncode == 0 and "END" in stdout and "?" not in stdout
        and all(value == "0" for value in remainders.values())
    )
    return {
        "epsilon": list(epsilon),
        "status": "COMPLETE" if valid else "ERROR",
        "substitution": {"t": f"{sign_product}*r^2"},
        "removed_gcd": str(common_gcd.as_expr()),
        "projection": str(projection.as_expr()),
        "r_relation": str(r_relation.as_expr()),
        "original_dimension": int(re.search(
            r"ORIGINAL_DIM=(-?\d+)", stdout).group(1))
            if "ORIGINAL_DIM=" in stdout else None,
        "tower_dimension": int(re.search(
            r"TOWER_DIM=(-?\d+)", stdout).group(1))
            if "TOWER_DIM=" in stdout else None,
        "remainders": remainders,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-2000:],
        "seconds": time.perf_counter()-started,
    }


@app.local_entrypoint()
def main():
    cases = tuple(itertools.product((-1, 1), repeat=2))
    raw = list(certify.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({"epsilon": list(case), "status": "REMOTE_ERROR",
                         "error": repr(row)})
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-tower-v1",
        "scope": (
            "Bidirectional guarded ideal certificate for the four cell-3 "
            "BC- common curves; outside systems unpaid."
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
            "original_dimension": row.get("original_dimension"),
            "tower_dimension": row.get("tower_dimension"),
            "remainders": row.get("remainders"),
            "seconds": row.get("seconds"),
        } for row in rows],
    }, sort_keys=True))
