#!/usr/bin/env python3
"""Search exact small generating subsets of the cell-12 common lex ideal."""

import hashlib
import itertools
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
STRUCTURE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_pivot_route_scout_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_tower_subset_result.json"
)
REMOTE_STRUCTURE = "/root/structure.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell12-tower-subset")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
)


def parse_tests(stdout):
    rows = []
    for match in re.finditer(
        r"TEST=(\d+):([0-9,]+):([01]):(\d+)", stdout
    ):
        rows.append({
            "subset_size": int(match.group(1)),
            "indices": [int(value) for value in match.group(2).split(",")],
            "exact": match.group(3) == "1",
            "remainder_basis_size": int(match.group(4)),
        })
    return rows


@app.function(image=image, cpu=2.0, memory=4096, timeout=300)
def search_subsets():
    payload = json.loads(Path(REMOTE_STRUCTURE).read_text())
    if not payload.get("complete") or len(payload.get("rows", [])) != 4:
        raise RuntimeError("incomplete structure payload")
    rows = payload["rows"]
    signatures = {
        tuple(item["sha256"] for item in row["lex_basis"])
        for row in rows
    }
    if len(signatures) != 1 or any(
        row["status"] != "COMPLETE" or row["lex_basis_size"] != 8
        for row in rows
    ):
        raise RuntimeError("pivot lex bases disagree")
    expressions = [item["expression"] for item in rows[0]["lex_basis"]]
    if any(expression is None for expression in expressions):
        raise RuntimeError("missing compact lex expression")

    definitions = "\n".join(
        f"poly k{index}={expression};"
        for index, expression in enumerate(expressions, start=1)
    )
    tests = []
    for size in (3, 4):
        for indices in itertools.combinations(range(1, 9), size):
            label = ",".join(str(index) for index in indices)
            generators = ",".join(f"k{index}" for index in indices)
            tests.append(f"""
ideal Q={generators}; Q=std(Q);
ideal KR=reduce(K,Q);
if ((size(KR)==1) && (KR[1]==0)) {{
  print("TEST={size}:{label}:1:"+string(size(KR)));
}} else {{
  print("TEST={size}:{label}:0:"+string(size(KR)));
}}
kill Q; kill KR;
""")
    program = f"""
ring R={PRIME},(c,b,t,r),lp;
option(redSB);
{definitions}
ideal K=k1,k2,k3,k4,k5,k6,k7,k8; K=std(K);
{"".join(tests)}
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"],
            input=program,
            capture_output=True,
            text=True,
            timeout=270,
        )
    except subprocess.TimeoutExpired as error:
        stdout = (
            error.stdout.decode("utf-8", errors="replace")
            if isinstance(error.stdout, bytes) else error.stdout or ""
        )
        return {
            "status": "TIMEOUT",
            "tests": parse_tests(stdout),
            "partial_stdout": stdout[-2000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    valid = (
        process.returncode == 0
        and "END" in process.stdout
        and "?" not in process.stdout
    )
    return {
        "status": "COMPLETE" if valid else "ERROR",
        "tests": parse_tests(process.stdout),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stdout_tail": process.stdout[-2000:],
        "stderr_tail": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main():
    row = search_subsets.remote()
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell12-tower-subset-v1",
        "field": PRIME,
        "scope": (
            "Unsaturated exact three- and four-generator search in one "
            "guarded cell-12 common lex chart; no outside or route claim."
        ),
        "source_structure_sha256": hashlib.sha256(
            STRUCTURE.read_bytes()
        ).hexdigest(),
        **row,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    exact = [item for item in row["tests"] if item["exact"]]
    minimum = min(
        (item["remainder_basis_size"] for item in row["tests"]),
        default=None,
    )
    print(json.dumps({
        "result": str(RESULT),
        "status": row["status"],
        "tested": len(row["tests"]),
        "exact": exact,
        "minimum_remainder_basis_size": minimum,
    }, sort_keys=True))
