#!/usr/bin/env python3
"""Compile the admissible FFF graph over F_p(t) on Modal."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
GRAPH = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_basis_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_basis_result.json"
REMOTE_GRAPH = "/root/graph.json"
REMOTE_PROGRAM = "/root/fff_generic_t_basis_program.py"
PRIME = 2130706433
GRAPH_SHA256 = "5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-generic-t-basis")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(GRAPH, REMOTE_GRAPH)
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
def compile_basis():
    core = load("fff_generic_t_basis_program", REMOTE_PROGRAM)
    graph = json.loads(Path(REMOTE_GRAPH).read_text())
    built = core.build(graph)
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
    profile = re.search(
        r"(?:^|\n)GENERIC_DIM=(-?\d+),GENERIC_SIZE=(\d+),GENERIC_VDIM=(\d+)",
        stdout,
    )
    basis_match = re.search(r"BASIS_BEGIN\n(.*?)\nBASIS_END", stdout, re.DOTALL)
    basis = []
    if basis_match:
        basis = [
            "".join(value.split())
            for value in re.findall(
                r"H\[\d+\]=(.*?)(?=^H\[\d+\]=|\Z)",
                basis_match.group(1), re.MULTILINE | re.DOTALL,
            )
        ]
    valid = (
        process.returncode == 0 and "END" in stdout and "?" not in stdout
        and profile is not None and len(basis) == int(profile.group(2))
    )
    encoded = json.dumps(basis, separators=(",", ":"))
    return {
        **common,
        "status": "COMPLETE" if valid else "ERROR",
        "dimension": int(profile.group(1)) if profile else None,
        "basis_size": int(profile.group(2)) if profile else None,
        "vector_space_dimension": int(profile.group(3)) if profile else None,
        "basis": basis,
        "basis_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "stdout_tail": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, collection_complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-generic-t-basis-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-generic-t-basis",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_graph_sha256": GRAPH_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(GRAPH.read_bytes()).hexdigest() == GRAPH_SHA256,
            "graph custody")
    write_checkpoint(None, collection_complete=False)
    try:
        row = compile_basis.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, collection_complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "collection_complete": complete,
        "status": row["status"],
        "dimension": row.get("dimension"),
        "basis_size": row.get("basis_size"),
        "vector_space_dimension": row.get("vector_space_dimension"),
    }, sort_keys=True))
