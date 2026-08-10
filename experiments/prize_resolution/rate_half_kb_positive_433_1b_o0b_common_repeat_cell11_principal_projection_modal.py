#!/usr/bin/env python3
"""Project precompiled cell-11 repeated-BC common curves to (c,b)."""

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
    "cell11_principal_projection_result.json"
)
REMOTE_INPUT = "/root/input.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-o0b-cell11-repeat-projection")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(INPUT, REMOTE_INPUT)
)


@app.function(image=image, cpu=1.0, memory=2048, timeout=240, max_containers=8)
def project(case):
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
    program = f"""
ring R={PRIME},(z,t,r,c,b),(dp(1),dp(4));
option(redSB);
{definitions}
poly common_guard={singular(common['guard'])};
poly rank_guard={singular(product['rank_minor'])};
ideal I=f0,f1,f2,f3,f4,f5,z*common_guard-1;
ideal G=std(I);
print("FULL_BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
print("FULL_END");
ideal E=eliminate(G,z*t*r); ideal H=std(E);
print("ELIM_BEGIN"); print("DIM="+string(dim(H))); print("SIZE="+string(size(H)));
print(H); print("ELIM_END"); print("END"); quit;
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
    stdout = process.stdout
    full_match = re.search(r"FULL_BEGIN\n(.*?)\nFULL_END", stdout, re.DOTALL)
    elimination_match = re.search(
        r"ELIM_BEGIN\n(.*?)\nELIM_END", stdout, re.DOTALL
    )
    valid = (
        process.returncode == 0 and "END" in stdout and "?" not in stdout
        and full_match and elimination_match
    )

    def value(pattern, text):
        match = re.search(pattern, text or "")
        return int(match.group(1)) if match else None

    return {
        "epsilon": [epsilon_1, epsilon_2], "bc_sign": bc_sign,
        "status": "COMPLETE" if valid else "ERROR",
        "product_rank_saturated": False,
        "rank_guard_sha256": product["rank_minor_sha256"],
        "full_dimension": value(r"DIM=(-?\d+)",
                                full_match.group(1) if full_match else ""),
        "full_size": value(r"SIZE=(\d+)",
                           full_match.group(1) if full_match else ""),
        "elimination_dimension": value(
            r"DIM=(-?\d+)",
            elimination_match.group(1) if elimination_match else "",
        ),
        "elimination_size": value(
            r"SIZE=(\d+)",
            elimination_match.group(1) if elimination_match else "",
        ),
        "elimination_output": (
            elimination_match.group(1).strip() if elimination_match else None
        ),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr": process.stderr[-2000:],
        "seconds": time.perf_counter() - started,
    }


@app.local_entrypoint()
def main(limit: int = 0):
    cases = tuple(itertools.product((-1, 1), (-1, 1), (-1, 1)))
    if limit:
        cases = cases[:limit]
    raw = list(project.map(cases, order_outputs=True, return_exceptions=True))
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
            "cell11-principal-projection-v1"
        ),
        "scope": (
            "Exact guarded common-curve projection to target coordinates "
            "(c,b), with the product-rank exceptional divisor retained."
        ),
        "source_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        "case_count": len(rows),
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
            "full": [row.get("full_dimension"), row.get("full_size")],
            "elimination": [row.get("elimination_dimension"),
                            row.get("elimination_size")],
            "elimination_output": row.get("elimination_output"),
            "seconds": row.get("seconds"),
        } for row in rows],
    }, sort_keys=True))
