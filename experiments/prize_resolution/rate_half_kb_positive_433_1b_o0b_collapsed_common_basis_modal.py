#!/usr/bin/env python3
"""Compute the four-variable common basis after the O0b z2=z5 collapse."""

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
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_collapsed_common_basis_program.py"
COLLAPSE_PROOF = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_multifinite_infinity_collapse.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_collapsed_common_basis_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_BASIS = "/root/basis.json"
REMOTE_PROGRAM = "/root/collapsed_common_basis_program.py"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
COLLAPSE_PROOF_SHA256 = "ed7a70cee69571b946ceef6a2c60e1c9f50438d2fb4dab37d19094265fa102a0"

app = modal.App("rs-mca-positive-433-1b-o0b-collapsed-common-basis")
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


@app.function(image=image, cpu=1.0, memory=2048, timeout=90)
def compute_basis():
    core = load("collapsed_common_basis_program", REMOTE_PROGRAM)
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
    basis_match = re.search(r"BASIS_BEGIN\n(.*?)\nBASIS_END", stdout, re.DOTALL)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    unit = "UNIT=1" in stdout
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
        valid and dimension_match is not None and size_match is not None
        and (unit or len(basis) == int(size_match.group(1)))
    )
    return {
        **common,
        "status": "COMPLETE" if valid else "ERROR",
        "unit": unit,
        "dimension": int(dimension_match.group(1)) if dimension_match else None,
        "basis_size": int(size_match.group(1)) if size_match else None,
        "basis": basis,
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, collection_complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-collapsed-common-basis-v1",
        "app": "rs-mca-positive-433-1b-o0b-collapsed-common-basis",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_cache_sha256": CACHE_SHA256,
        "source_basis_sha256": BASIS_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "source_collapse_proof_sha256": COLLAPSE_PROOF_SHA256,
        "row": row,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    require(hashlib.sha256(COLLAPSE_PROOF.read_bytes()).hexdigest() ==
            COLLAPSE_PROOF_SHA256, "collapse-proof custody")
    write_checkpoint(None, collection_complete=False)
    try:
        row = compute_basis.remote()
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
    }, sort_keys=True))
