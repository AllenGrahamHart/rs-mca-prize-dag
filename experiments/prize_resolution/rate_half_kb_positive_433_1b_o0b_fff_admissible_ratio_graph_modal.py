#!/usr/bin/env python3
"""Run the guarded five-variable FFF base ratio graph."""

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
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_program.py"
SOURCE_TIMEOUT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_ratio_graph_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_BASIS = "/root/basis.json"
REMOTE_PROGRAM = "/root/fff_admissible_ratio_graph_program.py"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
SOURCE_TIMEOUT_SHA256 = "9992611165f31733a3c497b27b93c39f65b621f9e3acc1489ab46c3d78e7096e"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-admissible-ratio-graph")
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


def parse_stages(stdout):
    graph = re.search(r"(?:^|\n)GRAPH_DIM=(-?\d+),GRAPH_SIZE=(\d+)", stdout)
    guards = [
        {"guard_index": int(index), "dimension": int(dim), "basis_size": int(size)}
        for index, dim, size in re.findall(
            r"(?:^|\n)BASE_GUARD=(\d+),DIM=(-?\d+),SIZE=(\d+)", stdout
        )
    ]
    return {
        "graph_dimension": int(graph.group(1)) if graph else None,
        "graph_basis_size": int(graph.group(2)) if graph else None,
        "base_guard_stages": guards,
    }


@app.function(image=image, cpu=1.0, memory=4096, timeout=300)
def decide_graph():
    core = load("fff_admissible_ratio_graph_program", REMOTE_PROGRAM)
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    basis_payload = json.loads(Path(REMOTE_BASIS).read_text())
    packet_row = next(row for row in cache["rows"] if row["epsilon"] == [-1, -1])
    basis_row = next(row for row in basis_payload["rows"]
                     if row["epsilon"] == [-1, -1])
    built = core.build(packet_row, basis_row)
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=240,
        )
    except subprocess.TimeoutExpired as error:
        stdout = decoded(error.stdout)[-30000:]
        return {
            **common,
            "status": "TIMEOUT",
            **parse_stages(stdout),
            "partial_stdout": stdout,
            "partial_stderr": decoded(error.stderr)[-1000:],
        }
    stdout = process.stdout
    dimension = re.search(r"(?:^|\n)DIM=(-?\d+)", stdout)
    size = re.search(r"(?:^|\n)SIZE=(\d+)", stdout)
    basis_match = re.search(r"BASIS_BEGIN\n(.*?)\nBASIS_END", stdout, re.DOTALL)
    output_basis = []
    if basis_match:
        output_basis = [
            "".join(value.split())
            for value in re.findall(
                r"G\[\d+\]=(.*?)(?=^G\[\d+\]=|\Z)",
                basis_match.group(1), re.MULTILINE | re.DOTALL,
            )
        ]
    valid = (
        process.returncode == 0 and "END" in stdout and "?" not in stdout
        and dimension is not None and size is not None
        and (int(size.group(1)) == 1 or len(output_basis) == int(size.group(1)))
    )
    encoded = json.dumps(output_basis, separators=(",", ":"))
    return {
        **common,
        "status": "COMPLETE" if valid else "ERROR",
        "unit": "UNIT=1" in stdout,
        **parse_stages(stdout),
        "dimension": int(dimension.group(1)) if dimension else None,
        "basis_size": int(size.group(1)) if size else None,
        "basis_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "basis": output_basis,
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, collection_complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-admissible-ratio-graph-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-admissible-ratio-graph",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_cache_sha256": CACHE_SHA256,
        "source_basis_sha256": BASIS_SHA256,
        "source_timeout_sha256": SOURCE_TIMEOUT_SHA256,
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
    require(hashlib.sha256(SOURCE_TIMEOUT.read_bytes()).hexdigest() ==
            SOURCE_TIMEOUT_SHA256, "source-timeout custody")
    write_checkpoint(None, collection_complete=False)
    try:
        row = decide_graph.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, collection_complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "collection_complete": complete,
        "status": row["status"],
        "unit": row.get("unit"),
        "graph_dimension": row.get("graph_dimension"),
        "graph_basis_size": row.get("graph_basis_size"),
        "base_guard_stages": row.get("base_guard_stages"),
        "dimension": row.get("dimension"),
        "basis_size": row.get("basis_size"),
    }, sort_keys=True))
