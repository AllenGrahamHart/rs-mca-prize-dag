#!/usr/bin/env python3
"""Run the exact z2=z5 collapsed O0b FFI boundary system."""

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
COMPILER = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_ffi_collapsed_program.py"
MSOLVE = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_ffi_msolve_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_ffi_collapsed_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_BASIS = "/root/basis.json"
REMOTE_COMPILER = "/root/cached_outside_core.py"
REMOTE_PROGRAM = "/root/ffi_collapsed_program.py"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
MSOLVE_SHA256 = "f0846e25f26981e045d4416233bd81d36dac6c3a44b0da7b2cd19912a02c57dd"

app = modal.App("rs-mca-positive-433-1b-o0b-ffi-collapsed")
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


@app.function(image=image, cpu=1.0, memory=4096, timeout=300)
def decide_chart():
    compiler = load("cached_outside_core", REMOTE_COMPILER)
    program_core = load("ffi_collapsed_program", REMOTE_PROGRAM)
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    basis_payload = json.loads(Path(REMOTE_BASIS).read_text())
    packet_row = next(row for row in cache["rows"] if row["epsilon"] == [-1, -1])
    basis_row = next(row for row in basis_payload["rows"] if row["epsilon"] == [-1, -1])
    built = program_core.build(packet_row, basis_row, compiler)
    program = built.pop("program")
    common = {
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


def write_checkpoint(row, collection_complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-ffi-collapsed-v1",
        "app": "rs-mca-positive-433-1b-o0b-ffi-collapsed",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_cache_sha256": CACHE_SHA256,
        "source_basis_sha256": BASIS_SHA256,
        "source_compiler_sha256": COMPILER_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "source_msolve_sha256": MSOLVE_SHA256,
        "row": row,
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
    require(hashlib.sha256(MSOLVE.read_bytes()).hexdigest() == MSOLVE_SHA256,
            "msolve-input custody")
    write_checkpoint(None, collection_complete=False)
    try:
        row = decide_chart.remote()
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
        "partial_stdout": row.get("partial_stdout"),
    }, sort_keys=True))
