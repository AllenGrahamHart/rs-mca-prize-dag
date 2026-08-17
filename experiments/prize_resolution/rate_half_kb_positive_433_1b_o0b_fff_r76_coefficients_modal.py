#!/usr/bin/env python3
"""Reduce and retain Res_E(q7,q6) coefficients on the FFF base graph."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
CACHE = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
GRAPH = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_coefficients_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_coefficients_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_GRAPH = "/root/graph.json"
REMOTE_PROGRAM = "/root/fff_r76_coefficients_program.py"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
GRAPH_SHA256 = "5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-r76-coefficients")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(CACHE, REMOTE_CACHE)
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


def parse_coefficients(stdout):
    stages = [
        {"coefficient": int(index), "degree": int(degree),
         "term_count": int(size)}
        for index, degree, size in re.findall(
            r"(?:^|\n)COEFFICIENT=(\d+),DEG=(-?\d+),SIZE=(\d+)", stdout
        )
    ]
    values = []
    for index in range(9):
        match = re.search(
            rf"C{index}_BEGIN\n(.*?)\nC{index}_END", stdout, re.DOTALL
        )
        if match:
            value = "".join(match.group(1).split())
            values.append({
                "coefficient": index,
                "polynomial": value,
                "polynomial_sha256": hashlib.sha256(value.encode()).hexdigest(),
            })
    return stages, values


@app.function(image=image, cpu=1.0, memory=4096, timeout=300)
def reduce_coefficients():
    core = load("fff_r76_coefficients_program", REMOTE_PROGRAM)
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    graph = json.loads(Path(REMOTE_GRAPH).read_text())
    packet_row = next(row for row in cache["rows"] if row["epsilon"] == [-1, -1])
    built = core.build(packet_row, graph)
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=240,
        )
    except subprocess.TimeoutExpired as error:
        stdout = decoded(error.stdout)
        stages, values = parse_coefficients(stdout)
        return {
            **common,
            "status": "TIMEOUT",
            "coefficient_stages": stages,
            "coefficients": values,
            "partial_stdout": stdout[-30000:],
            "partial_stderr": decoded(error.stderr)[-1000:],
        }
    stdout = process.stdout
    stages, values = parse_coefficients(stdout)
    valid = (
        process.returncode == 0 and "END" in stdout and "?" not in stdout
        and len(stages) == 9 and len(values) == 9
    )
    return {
        **common,
        "status": "COMPLETE" if valid else "ERROR",
        "coefficient_stages": stages,
        "coefficients": values,
        "stdout_tail": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, collection_complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-r76-coefficients-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-r76-coefficients",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_cache_sha256": CACHE_SHA256,
        "source_graph_sha256": GRAPH_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(GRAPH.read_bytes()).hexdigest() == GRAPH_SHA256,
            "graph custody")
    write_checkpoint(None, collection_complete=False)
    try:
        row = reduce_coefficients.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, collection_complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "collection_complete": complete,
        "status": row["status"],
        "coefficient_stages": row.get("coefficient_stages"),
        "coefficient_count": len(row.get("coefficients", [])),
    }, sort_keys=True))
