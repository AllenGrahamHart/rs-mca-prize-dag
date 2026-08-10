#!/usr/bin/env python3
"""Classify the BE/CF missing-record cuts on the cell-3 BC+ torus."""

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
TORUS = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_monomial_probe_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_colored_missing_result.json"
)
REMOTE_TORUS = "/root/torus.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-o0b-cell3-bcplus-colored-missing")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(TORUS, REMOTE_TORUS)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=8)
def classify(case):
    import sympy as sp

    started = time.perf_counter()
    epsilon_1, epsilon_2, missing_record = case
    torus_payload = json.loads(Path(REMOTE_TORUS).read_text())
    torus_row = next(
        row for row in torus_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    b, r, u = sp.symbols("b r u")
    labels = (1, r**4, -1, r**2, -r**2)
    products = (-1, b, u, b*u, b*u)
    matrix = sp.Matrix([
        [-product, -product*label, -product*label**2,
         1, label, label**2]
        for product, label in zip(products, labels)
    ])
    cofactors = []
    for column in range(6):
        columns = [index for index in range(6) if index != column]
        value = (-1)**column*matrix[:, columns].det(method="berkowitz")
        cofactors.append(
            sp.Poly(sp.expand(value), b, r, u, modulus=PRIME).as_expr()
        )

    def singular(expression):
        return str(expression).replace("**", "^")

    cofactor_definitions = "\n".join(
        f"poly u{index}={singular(value)};"
        for index, value in enumerate(cofactors)
    )
    known = "b" if missing_record == "BE" else "u"
    core = singular(torus_row["torus_core"]["expression"])
    guard = singular(torus_row["transformed_guard"]["expression"])
    program = f"""
ring R=(integer,{PRIME}),(z,b,r,u),(dp(1),dp(3));
option(redSB);
{cofactor_definitions}
poly scale=r^4*(1-r^4);
poly a0=scale*u0; poly a1=scale*u1; poly a2=scale*u2;
poly b0=scale*u3; poly b1=scale*u4; poly b2=scale*u5;
poly ap=u0+u1*r^4+u2*r^8;
poly beta0=-({epsilon_1*epsilon_2})*r^2*(1+b)*ap; poly beta1=-beta0;
poly am=a0-a1*r^4+a2*r^8;
poly bm=b0-b1*r^4+b2*r^8;
poly betam=beta0-beta1*r^4;
poly q0={core};
poly q1=b*u^3+1;
poly q2=r^4*({known})^2*betam^2+(({known})^2*am+bm)^2;
poly guard={guard};
ideal I=q0,q1,q2,z*guard-1;
ideal G=std(I);
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }} else {{ print("UNIT=0"); }}
print("BASIS_BEGIN"); print(G); print("BASIS_END"); print("END"); quit;
"""
    compiled_seconds = time.perf_counter()-started
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=150,
        )
    except subprocess.TimeoutExpired as error:
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "missing_record": missing_record,
            "status": "TIMEOUT",
            "compiled_seconds": compiled_seconds,
            "seconds": time.perf_counter()-started,
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
            "stdout_tail": (error.stdout or "")[-1000:],
        }
    stdout = process.stdout
    if process.returncode or "END" not in stdout or "?" in stdout:
        return {
            "epsilon": [epsilon_1, epsilon_2],
            "missing_record": missing_record,
            "status": "ERROR",
            "compiled_seconds": compiled_seconds,
            "seconds": time.perf_counter()-started,
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
            "stdout_head": stdout[:3000], "stdout_tail": stdout[-1000:],
            "stderr_tail": process.stderr[-1000:],
        }
    basis_match = re.search(r"BASIS_BEGIN\n(.*?)\nBASIS_END", stdout, re.DOTALL)
    basis = basis_match.group(1).strip() if basis_match else None
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "missing_record": missing_record,
        "known_coordinate": known,
        "status": "COMPLETE",
        "unit": "UNIT=1" in stdout,
        "dimension": int(re.search(r"DIM=(-?\d+)", stdout).group(1)),
        "basis_size": int(re.search(r"SIZE=(\d+)", stdout).group(1)),
        "basis_sha256": hashlib.sha256(basis.encode()).hexdigest(),
        "basis": basis if len(basis) <= 12000 else None,
        "cofactor_sha256": [
            hashlib.sha256(singular(value).encode()).hexdigest()
            for value in cofactors
        ],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "compiled_seconds": compiled_seconds,
        "seconds": time.perf_counter()-started,
    }


@app.local_entrypoint()
def main():
    cases = tuple(itertools.product((-1, 1), (-1, 1), ("BE", "CF")))
    raw = list(classify.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "missing_record": case[2],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    status_counts = dict(sorted(Counter(row["status"] for row in rows).items()))
    complete = [row for row in rows if row["status"] == "COMPLETE"]
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-colored-missing-v1",
        "scope": (
            "Guarded common-only necessary cuts for missing BE and CF; a "
            "nonunit cut is a candidate and not an outside witness."
        ),
        "source_torus_sha256": hashlib.sha256(TORUS.read_bytes()).hexdigest(),
        "case_count": len(rows),
        "status_counts": status_counts,
        "unit_count": sum(row["unit"] for row in complete),
        "survivor_count": sum(not row["unit"] for row in complete),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "status_counts": status_counts,
        "unit": output["unit_count"],
        "survivors": output["survivor_count"],
        "maximum_seconds": max((row.get("seconds", 0) for row in rows), default=0),
        "rows": [[row.get("epsilon"), row.get("missing_record"),
                  row.get("status"), row.get("unit"),
                  row.get("dimension"), row.get("basis_size")]
                 for row in rows],
    }, sort_keys=True))

