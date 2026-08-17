#!/usr/bin/env python3
"""Run direct b+1 Rabinowitsch tests for four multi-finite O0b charts."""

import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
CACHE = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
COMPILER = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_projective_chart_boundary_program.py"
PILOT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_chart_remaining_pilot_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_chart_multifinite_boundary_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_BASIS = "/root/basis.json"
REMOTE_COMPILER = "/root/cached_outside_core.py"
REMOTE_PROGRAM = "/root/projective_chart_boundary_program.py"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
PILOT_SHA256 = "09d854294bb4b0f3d33fc45f140f12ca86eebbb568c1f845a061b4143c50dba0"
CASE = (3, "S0", -1, -1, -1, 2, 0)
MASKS = tuple(
    mask for mask in product(("finite", "infinity"), repeat=3)
    if mask.count("finite") >= 2
)

app = modal.App("rs-mca-positive-433-1b-o0b-chart-multifinite-boundary")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(CACHE, REMOTE_CACHE)
    .add_local_file(BASIS, REMOTE_BASIS)
    .add_local_file(COMPILER, REMOTE_COMPILER)
    .add_local_file(PROGRAM, REMOTE_PROGRAM)
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def decoded(value):
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value or ""


@app.function(image=image, cpu=1.0, memory=4096, timeout=300, max_containers=4)
def decide_chart(indexed_mask):
    index, chart_mask = indexed_mask
    chart_mask = tuple(chart_mask)
    compiler = load("cached_outside_core", REMOTE_COMPILER)
    program_core = load("projective_chart_boundary_program", REMOTE_PROGRAM)
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    basis_payload = json.loads(Path(REMOTE_BASIS).read_text())
    packet_row = next(
        row for row in cache["rows"] if row["epsilon"] == list(CASE[3:5])
    )
    basis_row = next(
        row for row in basis_payload["rows"] if row["epsilon"] == list(CASE[3:5])
    )
    built = program_core.build(case=CASE, chart_mask=chart_mask,
                               packet_row=packet_row, basis_row=basis_row,
                               compiler_core=compiler)
    program = built.pop("program")
    common = {
        "index": index,
        **built,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=240,
        )
    except subprocess.TimeoutExpired as error:
        return {
            **common,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout)[-30000:],
            "partial_stderr": decoded(error.stderr)[-1000:],
        }
    stdout = process.stdout
    dimension_match = re.search(r"(?:^|\n)DIM=(-?\d+)", stdout)
    size_match = re.search(r"(?:^|\n)SIZE=(\d+)", stdout)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    unit = "UNIT=1" in stdout
    return {
        **common,
        "status": "COMPLETE" if valid else "ERROR",
        "unit": unit,
        "dimension": int(dimension_match.group(1)) if dimension_match else None,
        "basis_size": int(size_match.group(1)) if size_match else None,
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "input_program": "" if unit else program,
    }


def write_checkpoint(rows, errors, collection_complete):
    ordered = sorted(rows, key=lambda row: row["index"])
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-chart-multifinite-boundary-v1",
        "app": "rs-mca-positive-433-1b-o0b-chart-multifinite-boundary",
        "collection_complete": collection_complete,
        "field": PRIME,
        "case": list(CASE),
        "chart_masks": [list(mask) for mask in MASKS],
        "source_cache_sha256": CACHE_SHA256,
        "source_basis_sha256": BASIS_SHA256,
        "source_compiler_sha256": COMPILER_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "source_seven_chart_pilot_sha256": PILOT_SHA256,
        "expected_row_count": len(MASKS),
        "processed_row_count": len(ordered),
        "remote_errors": errors,
        "unit_count": sum(row.get("unit", False) for row in ordered),
        "rows": ordered,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
            "compiler custody")
    require(hashlib.sha256(PILOT.read_bytes()).hexdigest() == PILOT_SHA256,
            "pilot custody")
    require(len(MASKS) == 4 and len(set(MASKS)) == 4, "mask census")
    rows = []
    errors = []
    write_checkpoint(rows, errors, collection_complete=False)
    remote_rows = decide_chart.map(
        tuple(enumerate(MASKS)), order_outputs=False, return_exceptions=True
    )
    for row in remote_rows:
        if isinstance(row, BaseException):
            errors.append(repr(row))
        else:
            rows.append(row)
        complete = len(rows) == len(MASKS) and not errors
        write_checkpoint(rows, errors, collection_complete=complete)
    complete = len(rows) == len(MASKS) and not errors
    write_checkpoint(rows, errors, collection_complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "collection_complete": complete,
        "processed": len(rows),
        "remote_errors": len(errors),
        "unit": sum(row.get("unit", False) for row in rows),
        "statuses": {
            str(row["index"]): row["status"] for row in sorted(
                rows, key=lambda value: value["index"]
            )
        },
    }, sort_keys=True))
