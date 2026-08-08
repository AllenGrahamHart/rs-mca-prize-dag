#!/usr/bin/env python3
"""Test candidate guarded generators of the cell-12 common lex ideal."""

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
SUBSETS = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_tower_subset_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_cell12_localized_tower_subset_result.json"
)
REMOTE_STRUCTURE = "/root/structure.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-cell12-localized-tower-subset")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(STRUCTURE, REMOTE_STRUCTURE)
)


@app.function(image=image, cpu=2.0, memory=4096, timeout=300, max_containers=5)
def test_subset(indices):
    payload = json.loads(Path(REMOTE_STRUCTURE).read_text())
    rows = payload.get("rows", [])
    if not payload.get("complete") or len(rows) != 4:
        raise RuntimeError("incomplete structure payload")
    signatures = {
        tuple(item["sha256"] for item in row["lex_basis"])
        for row in rows
    }
    if len(signatures) != 1:
        raise RuntimeError("pivot lex bases disagree")
    expressions = [item["expression"] for item in rows[0]["lex_basis"]]
    if any(expression is None for expression in expressions):
        raise RuntimeError("missing compact lex expression")
    definitions = "\n".join(
        f"poly k{index}={expression};"
        for index, expression in enumerate(expressions, start=1)
    )
    generators = ",".join(f"k{index}" for index in indices)
    reductions = "\n".join(
        f'print("ROW={index},BEGIN"); print(reduce(k{index},Q)); '
        f'print("ROW={index},END");'
        for index in range(1, 9)
    )
    guard = "*".join((
        "b", "c", "r", "t", "(b-1)", "(b+1)", "(c-1)", "(c+1)",
        "(b-c)", "(b+c)", "(r^2-1)", "(r^2+1)", "(t^2-1)",
        "(t^2+1)", "(t^2-r^2)", "(t^2+r^2)",
    ))
    program = f"""
ring R={PRIME},(z,c,b,t,r),dp;
option(redSB);
{definitions}
poly H={guard};
ideal Q={generators},z*H-1; Q=slimgb(Q);
print("BEGIN");
print("DIM="+string(dim(Q))); print("SIZE="+string(size(Q)));
{reductions}
print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=270,
        )
    except subprocess.TimeoutExpired as error:
        stdout = (
            error.stdout.decode("utf-8", errors="replace")
            if isinstance(error.stdout, bytes) else error.stdout or ""
        )
        return {
            "indices": list(indices),
            "status": "TIMEOUT",
            "partial_stdout": stdout[-2000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    remainders = []
    for index in range(1, 9):
        match = re.search(
            rf"ROW={index},BEGIN\n(.*?)\nROW={index},END",
            process.stdout, re.DOTALL,
        )
        remainders.append(
            "".join(match.group(1).split()) if match else None
        )
    valid = (
        process.returncode == 0
        and "END" in process.stdout
        and "?" not in process.stdout
    )
    dimension = re.search(r"DIM=(-?\d+)", process.stdout)
    basis_size = re.search(r"SIZE=(\d+)", process.stdout)
    return {
        "indices": list(indices),
        "status": "COMPLETE" if valid else "ERROR",
        "dimension": int(dimension.group(1)) if dimension else None,
        "basis_size": int(basis_size.group(1)) if basis_size else None,
        "remainders": remainders,
        "exact": remainders == ["0"] * 8,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stderr_tail": process.stderr[-1000:],
    }


@app.local_entrypoint()
def main():
    subset_payload = json.loads(SUBSETS.read_text())
    four_rows = [
        row for row in subset_payload["tests"] if row["subset_size"] == 4
    ]
    minimum = min(row["remainder_basis_size"] for row in four_rows)
    four_candidates = tuple(
        tuple(row["indices"])
        for row in four_rows if row["remainder_basis_size"] == minimum
    )
    triple_candidates = tuple(
        (1, *pair) for pair in itertools.combinations(range(2, 9), 2)
    )
    candidates = (*triple_candidates, *four_candidates)
    raw = list(test_subset.map(
        candidates, order_outputs=True, return_exceptions=True
    ))
    rows = []
    for indices, row in zip(candidates, raw):
        if isinstance(row, BaseException):
            rows.append({
                "indices": list(indices),
                "status": "REMOTE_ERROR",
                "error": repr(row),
            })
        else:
            rows.append(row)
    output = {
        "schema": (
            "rate-half-kb-positive-433-1b-cell12-localized-tower-subset-v1"
        ),
        "field": PRIME,
        "scope": (
            "Exact equality after inverting all printed common route guards "
            "for the five closest four-generator subsets; no outside claim."
        ),
        "source_structure_sha256": hashlib.sha256(
            STRUCTURE.read_bytes()
        ).hexdigest(),
        "source_subsets_sha256": hashlib.sha256(SUBSETS.read_bytes()).hexdigest(),
        "candidate_remainder_basis_size": minimum,
        "triple_candidate_count": len(triple_candidates),
        "four_candidate_count": len(four_candidates),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(RESULT),
        "rows": [
            {
                key: row.get(key) for key in (
                    "indices", "status", "dimension", "basis_size", "exact"
                )
            }
            for row in rows
        ],
    }, sort_keys=True))
