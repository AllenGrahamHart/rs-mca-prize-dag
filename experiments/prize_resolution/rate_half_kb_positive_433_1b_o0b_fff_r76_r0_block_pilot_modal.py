#!/usr/bin/env python3
"""Run one R76[0] block-square pilot on Modal."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
GRAPH = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_result.json"
BRACKETS = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_brackets_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_r0_block_pilot_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_r0_block_pilot_result.json"
REMOTE_GRAPH = "/root/graph.json"
REMOTE_BRACKETS = "/root/brackets.json"
REMOTE_PROGRAM = "/root/fff_r76_r0_block_pilot_program.py"
PRIME = 2130706433
GRAPH_SHA256 = "5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1"
BRACKETS_SHA256 = "08dc7fefd108d4b8d17a1c7a5345f37312b65b9a74389cf7e7dfc94827b0446f"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-r76-r0-block-pilot")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(GRAPH, REMOTE_GRAPH)
    .add_local_file(BRACKETS, REMOTE_BRACKETS)
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
def run_pilot():
    core = load("fff_r76_r0_block_pilot_program", REMOTE_PROGRAM)
    graph = json.loads(Path(REMOTE_GRAPH).read_text())
    brackets = json.loads(Path(REMOTE_BRACKETS).read_text())
    built = core.build(graph, brackets)
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
    input_terms = re.search(r"(?:^|\n)INPUT_TERMS=(\d+)", stdout)
    raw = re.search(r"(?:^|\n)RAW_DEG=(-?\d+),RAW_SIZE=(\d+)", stdout)
    normal = re.search(
        r"(?:^|\n)NORMAL_DEG=(-?\d+),NORMAL_SIZE=(\d+)", stdout
    )
    value_match = re.search(r"NORMAL_BEGIN\n(.*?)\nNORMAL_END", stdout, re.DOTALL)
    value = "".join(value_match.group(1).split()) if value_match else ""
    valid = (
        process.returncode == 0 and "END" in stdout and "?" not in stdout
        and input_terms is not None and raw is not None and normal is not None
        and value_match is not None
    )
    return {
        **common,
        "status": "COMPLETE" if valid else "ERROR",
        "observed_input_terms": int(input_terms.group(1)) if input_terms else None,
        "raw_degree": int(raw.group(1)) if raw else None,
        "raw_term_count": int(raw.group(2)) if raw else None,
        "normal_degree": int(normal.group(1)) if normal else None,
        "normal_term_count": int(normal.group(2)) if normal else None,
        "normal_polynomial": value,
        "normal_sha256": hashlib.sha256(value.encode()).hexdigest(),
        "stdout_tail": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, collection_complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-r76-r0-block-pilot-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-r76-r0-block-pilot",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_graph_sha256": GRAPH_SHA256,
        "source_brackets_sha256": BRACKETS_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(GRAPH.read_bytes()).hexdigest() == GRAPH_SHA256,
            "graph custody")
    require(hashlib.sha256(BRACKETS.read_bytes()).hexdigest() == BRACKETS_SHA256,
            "bracket custody")
    write_checkpoint(None, collection_complete=False)
    try:
        row = run_pilot.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, collection_complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "collection_complete": complete,
        "status": row["status"],
        "raw_term_count": row.get("raw_term_count"),
        "normal_term_count": row.get("normal_term_count"),
    }, sort_keys=True))
