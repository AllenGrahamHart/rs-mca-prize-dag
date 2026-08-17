#!/usr/bin/env python3
"""Compile the guarded global cell-3 common Groebner bases on Modal."""

import hashlib
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
CACHE = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
REMOTE_CACHE = "/root/cache.json"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"

app = modal.App("rs-mca-positive-433-1b-cell3-global-common-basis")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(CACHE, REMOTE_CACHE)
)


@app.function(image=image, cpu=1.0, memory=4096, timeout=270, max_containers=4)
def compile_basis(signs):
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    row = next(value for value in cache["rows"] if value["epsilon"] == list(signs))
    if row["status"] != "COMPLETE":
        raise RuntimeError("cached packet status")
    packet = row["packet"]
    equation_definitions = "\n".join(
        f"poly q{index}={value};"
        for index, value in enumerate(packet["common_equations"])
    )
    guard_definitions = "\n".join(
        f"poly h{index}={value};"
        for index, value in enumerate(packet["route_guards"])
    )
    cofactor_definitions = "\n".join(
        f"poly c{index}={value};"
        for index, value in enumerate(packet["rank_cofactors"])
    )
    saturation_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G); "
        f'print("SAT={index},DIM="+string(dim(G))+",SIZE="+string(size(G)));'
        for index in range(len(packet["route_guards"]))
    )
    program = f"""
LIB "elim.lib";
ring R={PRIME},(t,r,c,b),dp;
option(redSB);
{equation_definitions}
{guard_definitions}
{cofactor_definitions}
ideal I=q0,q1,q2;
ideal G=slimgb(I);
{saturation_stages}
ideal C={','.join(f'c{index}' for index in range(6))};
list SC=sat(G,C); G=SC[1]; G=slimgb(G);
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
print("BASIS_BEGIN"); G; print("BASIS_END"); print("END"); quit;
"""
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=240,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            "epsilon": list(signs),
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout)[-30000:],
            "partial_stderr": decoded(error.stderr)[-1000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
            "packet_sha256": row["packet_sha256"],
        }
    stdout = process.stdout
    dimension_match = re.search(r"(?:^|\n)DIM=(-?\d+)", stdout)
    size_match = re.search(r"(?:^|\n)SIZE=(\d+)", stdout)
    basis_match = re.search(r"BASIS_BEGIN\n(.*?)\nBASIS_END", stdout, re.DOTALL)
    basis = []
    if basis_match:
        basis = [
            "".join(value.split())
            for value in re.findall(
                r"G\[\d+\]=(.*?)(?=^G\[\d+\]=|\Z)",
                basis_match.group(1), re.MULTILINE | re.DOTALL,
            )
        ]
    valid = (
        process.returncode == 0 and "END" in stdout and "?" not in stdout
        and dimension_match is not None and size_match is not None
        and len(basis) == int(size_match.group(1))
    )
    encoded = json.dumps(basis, separators=(",", ":"))
    return {
        "epsilon": list(signs),
        "status": "COMPLETE" if valid else "ERROR",
        "dimension": int(dimension_match.group(1)) if dimension_match else None,
        "basis_size": int(size_match.group(1)) if size_match else None,
        "basis_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "basis": basis,
        "packet_sha256": row["packet_sha256"],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
    }


def write_checkpoint(rows, complete):
    output = {
        "schema": "rate-half-kb-positive-433-1b-cell3-global-common-basis-v1",
        "field": PRIME,
        "complete": complete,
        "source_cache_sha256": CACHE_SHA256,
        "expected_row_count": 4,
        "processed_row_count": len(rows),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    if hashlib.sha256(CACHE.read_bytes()).hexdigest() != CACHE_SHA256:
        raise RuntimeError("cache custody")
    cases = tuple(
        (epsilon_1, epsilon_2)
        for epsilon_1 in (-1, 1) for epsilon_2 in (-1, 1)
    )
    rows = []
    write_checkpoint(rows, complete=False)
    remote_rows = compile_basis.map(cases, order_outputs=True, return_exceptions=True)
    for case, row in zip(cases, remote_rows):
        rows.append({
            "epsilon": list(case), "status": "REMOTE_ERROR", "error": repr(row)
        } if isinstance(row, BaseException) else row)
        write_checkpoint(rows, complete=False)
    complete = len(rows) == 4 and all(row["status"] == "COMPLETE" for row in rows)
    write_checkpoint(rows, complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "complete": complete,
        "rows": [{
            "epsilon": row.get("epsilon"),
            "status": row.get("status"),
            "dimension": row.get("dimension"),
            "basis_size": row.get("basis_size"),
            "basis_sha256": row.get("basis_sha256"),
        } for row in rows],
    }, sort_keys=True))
