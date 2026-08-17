#!/usr/bin/env python3
"""Run six cross-stratum O0b cells-3/6 basis-fed cases on Modal."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
CACHE = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
CASES = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_cross_pilot_cases.json"
COMPILER = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_outside_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_cross_pilot_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_BASIS = "/root/basis.json"
REMOTE_COMPILER = "/root/rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
REMOTE_PROGRAM = "/root/rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_outside_program.py"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
CASES_SHA256 = "2e1eea3589e0737e9efa7a3a49a0492d6fece4577b93a36eb1f6badf0b499b42"

app = modal.App("rs-mca-positive-433-1b-o0b-cells3-6-basis-cross-pilot")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(CACHE, REMOTE_CACHE)
    .add_local_file(BASIS, REMOTE_BASIS)
    .add_local_file(COMPILER, REMOTE_COMPILER)
    .add_local_file(PROGRAM, REMOTE_PROGRAM)
)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def selected_cases():
    payload = json.loads(CASES.read_text())
    cases = tuple(tuple(row) for row in payload["cases"])
    encoded = json.dumps(cases, separators=(",", ":"))
    require(payload["case_count"] == 6 and len(cases) == 6, "case census")
    require(payload["cases_sha256"] == CASES_SHA256 and
            hashlib.sha256(encoded.encode()).hexdigest() == CASES_SHA256,
            "case hash")
    require((3, "S0", -1, -1, -1, 0, 0) not in cases,
            "exclude already closed diagnostic")
    require({(row[1], row[5]) for row in cases} == {
        (lane, xi) for lane in ("S0", "SDE") for xi in (0, 2, 6)
    }, "lane/xi cross cover")
    return cases


def case_key(index, case):
    cell, lane, sigma_o, epsilon_1, epsilon_2, xi_index, pairing_index = case
    return {
        "index": index,
        "cell": cell,
        "lane": lane,
        "sigma_o": sigma_o,
        "epsilon": [epsilon_1, epsilon_2],
        "xi_index": xi_index,
        "pairing_index": pairing_index,
    }


@app.function(image=image, cpu=1.0, memory=4096, timeout=300, max_containers=6)
def decide_case(indexed_case):
    index, case = indexed_case
    case = tuple(case)
    compiler = load("cached_outside_core", REMOTE_COMPILER)
    program_core = load("basis_outside_program", REMOTE_PROGRAM)
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    basis = json.loads(Path(REMOTE_BASIS).read_text())
    packet_row = next(row for row in cache["rows"] if row["epsilon"] == list(case[3:5]))
    basis_row = next(row for row in basis["rows"] if row["epsilon"] == list(case[3:5]))
    built = program_core.build(case, packet_row, basis_row, compiler)
    program = built.pop("program")
    key = case_key(index, case)
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
            **key, **built,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout)[-30000:],
            "partial_stderr": decoded(error.stderr)[-1000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        }
    stdout = process.stdout
    dimensions = re.findall(r"(?:^|\n)DIM=(-?\d+)", stdout)
    basis_sizes = re.findall(r"(?:^|\n)SIZE=(\d+)", stdout)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    unit = "UNIT=1" in stdout
    return {
        **key, **built,
        "status": "COMPLETE" if valid else "ERROR",
        "unit": unit,
        "dimension": int(dimensions[-1]) if dimensions else None,
        "basis_size": int(basis_sizes[-1]) if basis_sizes else None,
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "input_program": "" if unit else program,
    }


def write_checkpoint(cases, rows, errors, collection_complete):
    ordered_rows = sorted(rows, key=lambda row: row["index"])
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-split-cells3-6-basis-cross-pilot-v1",
        "app": "rs-mca-positive-433-1b-o0b-cells3-6-basis-cross-pilot",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_cache_sha256": CACHE_SHA256,
        "source_basis_sha256": BASIS_SHA256,
        "source_cases_sha256": hashlib.sha256(CASES.read_bytes()).hexdigest(),
        "source_compiler_sha256": hashlib.sha256(COMPILER.read_bytes()).hexdigest(),
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "selected_cases_sha256": CASES_SHA256,
        "expected_case_count": len(cases),
        "processed_case_count": len(ordered_rows),
        "remote_errors": errors,
        "status_counts": {
            status: sum(row["status"] == status for row in ordered_rows)
            for status in sorted({row["status"] for row in ordered_rows})
        },
        "unit_count": sum(row.get("unit", False) for row in ordered_rows),
        "rows": ordered_rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    cases = selected_cases()
    indexed_cases = tuple(enumerate(cases))
    rows = []
    errors = []
    write_checkpoint(cases, rows, errors, collection_complete=False)
    remote_rows = decide_case.map(
        indexed_cases, order_outputs=False, return_exceptions=True
    )
    for row in remote_rows:
        if isinstance(row, BaseException):
            errors.append(repr(row))
        else:
            rows.append(row)
        complete = len(rows) == len(cases) and not errors and {
            row["index"] for row in rows
        } == set(range(len(cases)))
        write_checkpoint(cases, rows, errors, collection_complete=complete)
    complete = len(rows) == len(cases) and not errors and {
        row["index"] for row in rows
    } == set(range(len(cases)))
    write_checkpoint(cases, rows, errors, collection_complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "collection_complete": complete,
        "processed": len(rows),
        "remote_errors": len(errors),
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
