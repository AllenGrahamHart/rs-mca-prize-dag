#!/usr/bin/env python3
"""Saturate the O0b collapsed common basis by exact base admissibility."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_collapsed_common_basis_result.json"
CACHE = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
FGLM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_collapsed_common_fglm_result.json"
FACTOR = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_collapsed_common_eliminant_factor.py"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_collapsed_common_admissible_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_collapsed_common_admissible_result.json"
REMOTE_SOURCE = "/root/collapsed_common_basis.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_PROGRAM = "/root/collapsed_common_admissible_program.py"
PRIME = 2130706433
SOURCE_SHA256 = "01a48b8003766b3e34d6b47423c8aaaf8ad8e521f77b1ce01cd1a9b5a6a7f65d"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
FGLM_SHA256 = "a72b2fe045538562352b3954b016dab60c5f8fdb01a22839088e72512d61f53f"
FACTOR_SHA256 = "8d0c74703d84ff3eebaf43e5c867fc23ed6ea387a05497f8acc7fafed2a570e1"

app = modal.App("rs-mca-positive-433-1b-o0b-collapsed-common-admissible")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(SOURCE, REMOTE_SOURCE)
    .add_local_file(CACHE, REMOTE_CACHE)
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


@app.function(image=image, cpu=1.0, memory=2048, timeout=90)
def saturate_basis():
    core = load("collapsed_common_admissible_program", REMOTE_PROGRAM)
    source = json.loads(Path(REMOTE_SOURCE).read_text())
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    packet_row = next(row for row in cache["rows"] if row["epsilon"] == [-1, -1])
    built = core.build(source, packet_row)
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=60,
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
    stages = [
        {"guard_index": int(index), "dimension": int(dimension), "basis_size": int(size)}
        for index, dimension, size in re.findall(
            r"(?:^|\n)SAT=(\d+),DIM=(-?\d+),SIZE=(\d+)", stdout
        )
    ]
    cofactor_match = re.search(
        r"(?:^|\n)COFACTOR_DIM=(-?\d+),COFACTOR_SIZE=(\d+)", stdout
    )
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    unit = "UNIT=1" in stdout
    return {
        **common,
        "status": "COMPLETE" if valid else "ERROR",
        "unit": unit,
        "initial_dimension": 0,
        "initial_basis_size": 43,
        "initial_vdim": 65,
        "stages": stages,
        "cofactor_dimension": int(cofactor_match.group(1)) if cofactor_match else None,
        "cofactor_basis_size": int(cofactor_match.group(2)) if cofactor_match else None,
        "dimension": int(dimension_match.group(1)) if dimension_match else None,
        "basis_size": int(size_match.group(1)) if size_match else None,
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, collection_complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-collapsed-common-admissible-v1",
        "app": "rs-mca-positive-433-1b-o0b-collapsed-common-admissible",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_basis_sha256": SOURCE_SHA256,
        "source_cache_sha256": CACHE_SHA256,
        "source_fglm_sha256": FGLM_SHA256,
        "source_factor_sha256": FACTOR_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "source-basis custody")
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(FGLM.read_bytes()).hexdigest() == FGLM_SHA256,
            "FGLM custody")
    require(hashlib.sha256(FACTOR.read_bytes()).hexdigest() == FACTOR_SHA256,
            "factor custody")
    write_checkpoint(None, collection_complete=False)
    try:
        row = saturate_basis.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, collection_complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "collection_complete": complete,
        "status": row["status"],
        "unit": row.get("unit"),
        "dimension": row.get("dimension"),
        "basis_size": row.get("basis_size"),
        "stages": row.get("stages"),
    }, sort_keys=True))
