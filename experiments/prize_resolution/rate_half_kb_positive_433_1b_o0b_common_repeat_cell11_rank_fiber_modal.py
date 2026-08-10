#!/usr/bin/env python3
"""Certify the cell-11 t relation and selected rank-exception fibers."""

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
    "cell11_rank_fiber_result.json"
)
REMOTE_INPUT = "/root/input.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-o0b-cell11-rank-fiber")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(INPUT, REMOTE_INPUT)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=180, max_containers=8)
def certify(case):
    started = time.perf_counter()
    epsilon_1, epsilon_2, bc_sign = case
    payload = json.loads(Path(REMOTE_INPUT).read_text())
    common = next(
        row for row in payload["common_rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
        and row["bc_sign"] == bc_sign
    )
    product = next(
        row for row in payload["product_rows"]
        if row["bc_sign"] == bc_sign
    )

    def singular(value):
        return value.replace("**", "^")

    definitions = "\n".join(
        f"poly f{index}={singular(value)};"
        for index, value in enumerate(common["equations"])
    )
    sign_product = epsilon_1 * epsilon_2
    program = f"""
ring R={PRIME},(z,t,r,c,b),(dp(1),dp(4));
option(redSB);
{definitions}
poly common_guard={singular(common['guard'])};
poly rank_guard={singular(product['rank_minor'])};
poly t_relation=t-({sign_product})*r^2;
ideal I=f0,f1,f2,f3,f4,f5,z*common_guard-1;
ideal G=std(I);
poly tr=reduce(t_relation,G);
poly rr=reduce(rank_guard,G);
ideal K=G,rank_guard; ideal H=std(K);
print("FULL_DIM="+string(dim(G)));
print("FULL_SIZE="+string(size(G)));
print("TR_BEGIN"); print(tr); print("TR_END");
print("RR_BEGIN"); print(rr); print("RR_END");
print("RANK_DIM="+string(dim(H)));
print("RANK_SIZE="+string(size(H)));
if (dim(H)==0) {{ print("RANK_VDIM="+string(vdim(H))); }};
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=150,
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

    def value(label):
        match = re.search(rf"{label}=(-?\d+)", process.stdout)
        return int(match.group(1)) if match else None

    def between(left, right):
        match = re.search(rf"{left}\n(.*?)\n{right}", process.stdout, re.DOTALL)
        return "".join(match.group(1).split()) if match else None

    t_remainder = between("TR_BEGIN", "TR_END")
    rank_remainder = between("RR_BEGIN", "RR_END")
    valid = (
        process.returncode == 0 and "END" in process.stdout
        and "?" not in process.stdout and t_remainder == "0"
        and rank_remainder not in (None, "", "0")
    )
    return {
        "epsilon": [epsilon_1, epsilon_2], "bc_sign": bc_sign,
        "status": "COMPLETE" if valid else "ERROR",
        "t_relation": f"t={sign_product}*r^2",
        "t_relation_remainder": t_remainder,
        "selected_rank_minor_sha256": product["rank_minor_sha256"],
        "selected_rank_minor_remainder": rank_remainder,
        "selected_rank_minor_remainder_sha256": hashlib.sha256(
            (rank_remainder or "").encode()
        ).hexdigest(),
        "full_dimension": value("FULL_DIM"),
        "full_basis_size": value("FULL_SIZE"),
        "selected_rank_fiber_dimension": value("RANK_DIM"),
        "selected_rank_fiber_basis_size": value("RANK_SIZE"),
        "selected_rank_fiber_vdim": value("RANK_VDIM"),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-2000:],
        "seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main(limit: int = 0):
    cases = tuple(itertools.product((-1, 1), (-1, 1), (-1, 1)))
    if limit:
        cases = cases[:limit]
    raw = list(certify.map(cases, order_outputs=True, return_exceptions=True))
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
            "cell11-rank-fiber-v1"
        ),
        "scope": (
            "Exact t-relation membership and selected product-rank cofactor "
            "fiber dimensions for all eight cell-11 common rows."
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
            "status": row["status"], "t": row.get("t_relation_remainder"),
            "rank_fiber": [row.get("selected_rank_fiber_dimension"),
                           row.get("selected_rank_fiber_vdim")],
            "seconds": row.get("seconds"),
        } for row in rows],
    }, sort_keys=True))
