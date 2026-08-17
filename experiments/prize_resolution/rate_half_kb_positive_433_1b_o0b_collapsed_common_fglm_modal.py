#!/usr/bin/env python3
"""Run FGLM on the zero-dimensional O0b collapsed common basis."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_collapsed_common_basis_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_collapsed_common_fglm_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_collapsed_common_fglm_result.json"
REMOTE_SOURCE = "/root/collapsed_common_basis.json"
REMOTE_PROGRAM = "/root/collapsed_common_fglm_program.py"
PRIME = 2130706433
SOURCE_SHA256 = "01a48b8003766b3e34d6b47423c8aaaf8ad8e521f77b1ce01cd1a9b5a6a7f65d"

app = modal.App("rs-mca-positive-433-1b-o0b-collapsed-common-fglm")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(SOURCE, REMOTE_SOURCE)
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


def integer(label, stdout):
    match = re.search(rf"(?:^|\n){label}=(-?\d+)", stdout)
    return int(match.group(1)) if match else None


@app.function(image=image, cpu=1.0, memory=4096, timeout=150)
def convert_basis():
    core = load("collapsed_common_fglm_program", REMOTE_PROGRAM)
    source = json.loads(Path(REMOTE_SOURCE).read_text())
    built = core.build(source)
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=120,
        )
    except subprocess.TimeoutExpired as error:
        stdout = decoded(error.stdout)
        return {
            **common,
            "status": "TIMEOUT",
            "dp_dimension": integer("DP_DIM", stdout),
            "dp_basis_size": integer("DP_SIZE", stdout),
            "dp_vdim": integer("DP_VDIM", stdout),
            "partial_stdout": stdout[-30000:],
            "partial_stderr": decoded(error.stderr)[-1000:],
        }
    stdout = process.stdout
    basis_match = re.search(
        r"LEX_BASIS_BEGIN\n(.*?)\nLEX_BASIS_END", stdout, re.DOTALL
    )
    lex_basis = []
    if basis_match:
        lex_basis = [
            "".join(value.split())
            for value in re.findall(
                r"H\[\d+\]=(.*?)(?=^H\[\d+\]=|\Z)",
                basis_match.group(1), re.MULTILINE | re.DOTALL,
            )
        ]
    lex_size = integer("LEX_SIZE", stdout)
    valid = (
        process.returncode == 0 and "LEX_END" in stdout and "?" not in stdout
        and lex_size is not None and len(lex_basis) == lex_size
    )
    return {
        **common,
        "status": "COMPLETE" if valid else "ERROR",
        "dp_dimension": integer("DP_DIM", stdout),
        "dp_basis_size": integer("DP_SIZE", stdout),
        "dp_vdim": integer("DP_VDIM", stdout),
        "lex_dimension": integer("LEX_DIM", stdout),
        "lex_basis_size": lex_size,
        "lex_vdim": integer("LEX_VDIM", stdout),
        "lex_basis": lex_basis,
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, collection_complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-collapsed-common-fglm-v1",
        "app": "rs-mca-positive-433-1b-o0b-collapsed-common-fglm",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_basis_sha256": SOURCE_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "source-basis custody")
    write_checkpoint(None, collection_complete=False)
    try:
        row = convert_basis.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, collection_complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "collection_complete": complete,
        "status": row["status"],
        "dp_vdim": row.get("dp_vdim"),
        "lex_vdim": row.get("lex_vdim"),
        "lex_basis_size": row.get("lex_basis_size"),
    }, sort_keys=True))
