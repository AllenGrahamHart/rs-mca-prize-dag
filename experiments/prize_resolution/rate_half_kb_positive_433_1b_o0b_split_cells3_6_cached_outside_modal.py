#!/usr/bin/env python3
"""Run the repaired cached-input O0b split cells-3/6 pilot on Modal."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
CACHE = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
REPRESENTATIVES = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_representatives.json"
CORE = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_pilot_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_CORE = "/root/rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
MANIFEST_SHA256 = "409e0e0851f2cef35501123b3dcb5818318380a291864090a7792accf599dfc2"
REPRESENTATIVES_SHA256 = "39fb277a94d8ee3a24e3a8f9e1f0bb50014665ca7c151659d4dc8fcd912392d6"
PILOT_SHA256 = "a1853f2a70cd7fc46c173f1401e4b7e8820f9fa1c01e8a8b3571bfefa2969c96"

app = modal.App("rs-mca-positive-433-1b-o0b-split-cells3-6-cached-pilot")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(CACHE, REMOTE_CACHE)
    .add_local_file(CORE, REMOTE_CORE)
)


def load_core(path):
    spec = importlib.util.spec_from_file_location("cached_outside_core", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pilot_cases():
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "common cache custody")
    require(hashlib.sha256(REPRESENTATIVES.read_bytes()).hexdigest() == MANIFEST_SHA256,
            "representative manifest custody")
    payload = json.loads(REPRESENTATIVES.read_text())
    require(payload["representatives_sha256"] == REPRESENTATIVES_SHA256,
            "complete representative custody")
    require(payload["pilot_representatives_sha256"] == PILOT_SHA256,
            "pilot representative custody")
    cases = tuple(tuple(row) for row in payload["pilot_representatives"])
    require(len(cases) == 24 and payload["pilot_stratum_count"] == 56,
            "pilot census")
    require(all(case[0] == 3 for case in cases), "canonical cell-3 pilot")
    return cases


def case_key(case):
    cell, lane, sigma_o, epsilon_1, epsilon_2, xi_index, pairing_index = case
    return {
        "cell": cell,
        "lane": lane,
        "sigma_o": sigma_o,
        "epsilon": [epsilon_1, epsilon_2],
        "xi_index": xi_index,
        "pairing_index": pairing_index,
    }


@app.function(image=image, cpu=1.0, memory=3072, timeout=300, max_containers=24)
def decide_case(case):
    core = load_core(REMOTE_CORE)
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    packet_row = next(
        row for row in cache["rows"] if row["epsilon"] == list(case[3:5])
    )
    require(packet_row["status"] == "COMPLETE", "cached packet status")
    compiled = core.compile_case(case, packet_row["packet"])
    guard_definitions = "\n".join(
        f"poly h{index}={value};"
        for index, value in enumerate(compiled["guards"])
    )
    cofactor_definitions = "\n".join(
        f"poly c{index}={value};"
        for index, value in enumerate(compiled["rank_cofactors"])
    )
    saturation_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G); "
        f'print("SAT={index},DIM="+string(dim(G))+",SIZE="+string(size(G)));'
        for index in range(len(compiled["guards"]))
    )
    program = f"""
LIB "elim.lib";
ring R={PRIME},({','.join(compiled['variables'])}),dp;
option(redSB);
{chr(10).join(compiled['definitions'])}
{guard_definitions}
{cofactor_definitions}
ideal I={','.join(compiled['equations'])};
ideal G=slimgb(I);
{saturation_stages}
ideal C={','.join(f'c{index}' for index in range(len(compiled['rank_cofactors'])))};
list SC=sat(G,C); G=SC[1]; G=slimgb(G);
print("COFACTOR_DIM="+string(dim(G))+",COFACTOR_SIZE="+string(size(G)));
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); G; }}
print("END"); quit;
"""
    key = case_key(case)
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
            **key,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout)[-30000:],
            "partial_stderr": decoded(error.stderr)[-1000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
            "packet_sha256": packet_row["packet_sha256"],
        }
    stdout = process.stdout
    dimensions = re.findall(r"(?:^|\n)DIM=(-?\d+)", stdout)
    basis_sizes = re.findall(r"(?:^|\n)SIZE=(\d+)", stdout)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    unit = "UNIT=1" in stdout
    return {
        **key,
        "status": "COMPLETE" if valid else "ERROR",
        "unit": unit,
        "dimension": int(dimensions[-1]) if dimensions else None,
        "basis_size": int(basis_sizes[-1]) if basis_sizes else None,
        "common_equation_count": compiled["common_equation_count"],
        "outside_equation_count": compiled["outside_equation_count"],
        "guard_count": len(compiled["guards"]),
        "rank_cofactor_count": len(compiled["rank_cofactors"]),
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "packet_sha256": packet_row["packet_sha256"],
        "input_program": "" if unit else program,
    }


def write_checkpoint(cases, rows, complete):
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-split-cells3-6-cached-pilot-v1",
        "app": "rs-mca-positive-433-1b-o0b-split-cells3-6-cached-pilot",
        "scope": "pilot",
        "complete": complete,
        "field": PRIME,
        "source_cache_sha256": CACHE_SHA256,
        "source_manifest_sha256": MANIFEST_SHA256,
        "source_core_sha256": hashlib.sha256(CORE.read_bytes()).hexdigest(),
        "representatives_sha256": REPRESENTATIVES_SHA256,
        "selected_cases_sha256": PILOT_SHA256,
        "expected_case_count": len(cases),
        "processed_case_count": len(rows),
        "status_counts": {
            status: sum(row["status"] == status for row in rows)
            for status in sorted({row["status"] for row in rows})
        },
        "unit_count": sum(row.get("unit", False) for row in rows),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    cases = pilot_cases()
    rows = []
    write_checkpoint(cases, rows, complete=False)
    remote_rows = decide_case.map(cases, order_outputs=True, return_exceptions=True)
    for case, row in zip(cases, remote_rows):
        rows.append({
            **case_key(case), "status": "REMOTE_ERROR", "error": repr(row)
        } if isinstance(row, BaseException) else row)
        write_checkpoint(cases, rows, complete=False)
    complete = len(rows) == len(cases) and all(
        row["status"] == "COMPLETE" for row in rows
    )
    write_checkpoint(cases, rows, complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "complete": complete,
        "expected": len(cases),
        "processed": len(rows),
        "status_counts": {
            status: sum(row["status"] == status for row in rows)
            for status in sorted({row["status"] for row in rows})
        },
        "unit": sum(row.get("unit", False) for row in rows),
        "nonunit": sum(
            row["status"] == "COMPLETE" and not row.get("unit", False)
            for row in rows
        ),
    }, sort_keys=True))
