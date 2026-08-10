#!/usr/bin/env python3
"""Eliminate cell-11 common curves to the symmetric source tower (r,x,y)."""

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
INPUT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_principal_input_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_symmetric_tower_result.json"
)
REMOTE_INPUT = "/root/input.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-o0b-cell11-symmetric-tower")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .pip_install("sympy==1.14.0")
    .add_local_file(INPUT, REMOTE_INPUT)
)


@app.function(image=image, cpu=1.0, memory=3072, timeout=240, max_containers=8)
def eliminate(case):
    import sympy as sp

    started = time.perf_counter()
    epsilon_1, epsilon_2, bc_sign = case
    payload = json.loads(Path(REMOTE_INPUT).read_text())
    common = next(
        row for row in payload["common_rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
        and row["bc_sign"] == bc_sign
    )
    t, r, c, b = sp.symbols("t r c b")
    local = {"t": t, "r": r, "c": c, "b": b}
    substitution = {t: epsilon_1 * epsilon_2 * r**2}
    equations = [
        sp.Poly(
            sp.sympify(value, locals=local).subs(substitution),
            r, c, b, modulus=PRIME,
        ).as_expr()
        for value in common["equations"]
    ]
    guard = sp.Poly(
        sp.sympify(common["guard"], locals=local).subs(substitution),
        r, c, b, modulus=PRIME,
    ).as_expr()

    def singular(value):
        return str(value).replace("**", "^")

    definitions = "\n".join(
        f"poly f{index}={singular(value)};"
        for index, value in enumerate(equations)
    )
    program = f"""
ring R={PRIME},(z,b,c,r,y,x),(dp(3),lp);
option(redSB);
{definitions}
poly common_guard={singular(guard)};
poly sx=x-b*c; poly sy=y-b-c;
ideal I=f0,f1,f2,f3,f4,f5,sx,sy,z*common_guard-1;
ideal G=std(I);
ideal H=std(eliminate(G,z*b*c));
ideal L=std(eliminate(G,z*c));
ideal P=std(eliminate(H,r));
print("FULL_DIM="+string(dim(G))); print("FULL_SIZE="+string(size(G)));
print("TOWER_BEGIN"); print("DIM="+string(dim(H))); print("SIZE="+string(size(H))); print(H); print("TOWER_END");
print("LIFT_BEGIN"); print("DIM="+string(dim(L))); print("SIZE="+string(size(L))); print(L); print("LIFT_END");
print("PLANE_BEGIN"); print("DIM="+string(dim(P))); print("SIZE="+string(size(P))); print(P); print("PLANE_END");
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=210,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""
        return {
            "epsilon": [epsilon_1, epsilon_2], "bc_sign": bc_sign,
            "status": "TIMEOUT",
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
            "partial_stdout": decoded(error.stdout)[-12000:],
            "partial_stderr": decoded(error.stderr)[-2000:],
            "seconds": time.perf_counter() - started,
        }

    def between(left, right):
        match = re.search(rf"{left}\n(.*?)\n{right}", process.stdout, re.DOTALL)
        return match.group(1).strip() if match else None

    def value(label, text):
        match = re.search(rf"{label}=(-?\d+)", text or "")
        return int(match.group(1)) if match else None

    tower = between("TOWER_BEGIN", "TOWER_END")
    lift = between("LIFT_BEGIN", "LIFT_END")
    plane = between("PLANE_BEGIN", "PLANE_END")
    valid = (
        process.returncode == 0 and "END" in process.stdout
        and "?" not in process.stdout and tower and lift and plane
    )
    return {
        "epsilon": [epsilon_1, epsilon_2], "bc_sign": bc_sign,
        "status": "COMPLETE" if valid else "ERROR",
        "substitution": f"t={epsilon_1 * epsilon_2}*r^2",
        "full_dimension": value("FULL_DIM", process.stdout),
        "full_size": value("FULL_SIZE", process.stdout),
        "tower_dimension": value("DIM", tower),
        "tower_size": value("SIZE", tower),
        "tower_output": tower,
        "ordered_lift_dimension": value("DIM", lift),
        "ordered_lift_size": value("SIZE", lift),
        "ordered_lift_output": lift,
        "plane_dimension": value("DIM", plane),
        "plane_size": value("SIZE", plane),
        "plane_output": plane,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-2000:],
        "seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main(limit: int = 0):
    cases = tuple(itertools.product((-1, 1), (-1, 1), (-1, 1)))
    if limit:
        cases = cases[:limit]
    raw = list(eliminate.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "bc_sign": case[2],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-o0b-common-repeat-"
            "cell11-symmetric-tower-v1"
        ),
        "scope": (
            "Exact guarded elimination to symmetric source coordinates "
            "x=bc, y=b+c after the certified t relation."
        ),
        "source_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        "status_counts": dict(sorted(Counter(
            row["status"] for row in rows
        ).items())),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT), "status_counts": output["status_counts"],
        "rows": [{
            "epsilon": row["epsilon"], "bc_sign": row["bc_sign"],
            "status": row["status"],
            "tower": [row.get("tower_dimension"), row.get("tower_size"),
                      row.get("tower_output")],
            "ordered_lift": [row.get("ordered_lift_dimension"),
                             row.get("ordered_lift_size"),
                             row.get("ordered_lift_output")],
            "plane": [row.get("plane_dimension"), row.get("plane_size"),
                      row.get("plane_output")],
            "seconds": row.get("seconds"),
        } for row in rows],
    }, sort_keys=True))
