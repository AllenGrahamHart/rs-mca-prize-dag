#!/usr/bin/env python3
"""Run the E=e^2 necessary subsystem for the canonical O0b FFF chart."""

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
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_square_subsystem_program.py"
RATIO_TIMEOUT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_ratio_reduction_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_square_subsystem_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_BASIS = "/root/basis.json"
REMOTE_PROGRAM = "/root/fff_square_subsystem_program.py"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
RATIO_TIMEOUT_SHA256 = "0f9cb1df4d58e5c55ac742beb9d041a7c23ec9d282101c43d67acb4bfabfb4f5"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-square-subsystem")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(CACHE, REMOTE_CACHE)
    .add_local_file(BASIS, REMOTE_BASIS)
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
def decide_subsystem():
    core = load("fff_square_subsystem_program", REMOTE_PROGRAM)
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    basis_payload = json.loads(Path(REMOTE_BASIS).read_text())
    packet_row = next(row for row in cache["rows"] if row["epsilon"] == [-1, -1])
    basis_row = next(row for row in basis_payload["rows"] if row["epsilon"] == [-1, -1])
    built = core.build(packet_row, basis_row)
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
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
    equation_stages = [
        {"equation": int(eq), "dimension": int(dim), "basis_size": int(size)}
        for eq, dim, size in re.findall(
            r"(?:^|\n)EQUATION=(\d+),DIM=(-?\d+),SIZE=(\d+)", stdout
        )
    ]
    route_stages = [
        {"guard_index": int(index), "dimension": int(dim), "basis_size": int(size)}
        for index, dim, size in re.findall(
            r"(?:^|\n)ROUTE=(\d+),DIM=(-?\d+),SIZE=(\d+)", stdout
        )
    ]
    extra_stages = [
        {"guard_index": int(index), "dimension": int(dim), "basis_size": int(size)}
        for index, dim, size in re.findall(
            r"(?:^|\n)EXTRA=(\d+),DIM=(-?\d+),SIZE=(\d+)", stdout
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
        "equation_stages": equation_stages,
        "route_stages": route_stages,
        "extra_stages": extra_stages,
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
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-square-subsystem-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-square-subsystem",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_cache_sha256": CACHE_SHA256,
        "source_basis_sha256": BASIS_SHA256,
        "source_ratio_timeout_sha256": RATIO_TIMEOUT_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    require(hashlib.sha256(RATIO_TIMEOUT.read_bytes()).hexdigest() ==
            RATIO_TIMEOUT_SHA256, "ratio-timeout custody")
    write_checkpoint(None, collection_complete=False)
    try:
        row = decide_subsystem.remote()
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
        "equation_stages": row.get("equation_stages"),
    }, sort_keys=True))
