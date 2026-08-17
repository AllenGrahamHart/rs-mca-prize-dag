#!/usr/bin/env python3
"""Retain the exact reduced R76 bracket arrays on Modal."""

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
RAW_CORE = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_coefficients_program.py"
PROGRESSIVE = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_progressive_program.py"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_brackets_program.py"
SOURCE_TIMEOUT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_progressive_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_brackets_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_GRAPH = "/root/graph.json"
REMOTE_RAW_CORE = "/root/fff_r76_coefficients_program.py"
REMOTE_PROGRESSIVE = "/root/fff_r76_progressive_program.py"
REMOTE_PROGRAM = "/root/fff_r76_brackets_program.py"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
GRAPH_SHA256 = "5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1"
RAW_CORE_SHA256 = "7cb0d1b17e2c8175afd59a90be30b84f9409fdad457f3df454119fe2262a22f6"
PROGRESSIVE_SHA256 = "b73c4e888dc69353bc823c787babdf7c4b8b5d2a4c7efe708ffef16604f045ca"
SOURCE_TIMEOUT_SHA256 = "0a2173e080a4a5029713aa8fa8feea73056a5e84b8139bc780684d5545117d95"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-r76-brackets")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(CACHE, REMOTE_CACHE)
    .add_local_file(GRAPH, REMOTE_GRAPH)
    .add_local_file(RAW_CORE, REMOTE_RAW_CORE)
    .add_local_file(PROGRESSIVE, REMOTE_PROGRESSIVE)
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


def parse_transcript(stdout):
    intermediates = [
        {"family": family, "index": int(index), "degree": int(degree),
         "term_count": int(size)}
        for family, index, degree, size in re.findall(
            r"(?:^|\n)INTERMEDIATE=([A-Z0-9]+),INDEX=(\d+),"
            r"DEG=(-?\d+),SIZE=(\d+)", stdout
        )
    ]
    stages = [
        {"family": family, "index": int(index), "degree": int(degree),
         "term_count": int(size)}
        for family, index, degree, size in re.findall(
            r"(?:^|\n)BRACKET=(M[012]),INDEX=(\d+),"
            r"DEG=(-?\d+),SIZE=(\d+)", stdout
        )
    ]
    values = []
    for family, count in (("M0", 5), ("M1", 5), ("M2", 4)):
        for index in range(count):
            match = re.search(
                rf"{family}_{index}_BEGIN\n(.*?)\n{family}_{index}_END",
                stdout, re.DOTALL,
            )
            if match:
                value = "".join(match.group(1).split())
                values.append({
                    "family": family,
                    "index": index,
                    "polynomial": value,
                    "polynomial_sha256":
                        hashlib.sha256(value.encode()).hexdigest(),
                })
    return intermediates, stages, values


@app.function(image=image, cpu=1.0, memory=4096, timeout=300)
def retain_brackets():
    raw_core = load("fff_r76_coefficients_program", REMOTE_RAW_CORE)
    progressive = load("fff_r76_progressive_program", REMOTE_PROGRESSIVE)
    core = load("fff_r76_brackets_program", REMOTE_PROGRAM)
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    graph = json.loads(Path(REMOTE_GRAPH).read_text())
    packet_row = next(row for row in cache["rows"] if row["epsilon"] == [-1, -1])
    built = core.build(packet_row, graph, raw_core, progressive)
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=240,
        )
    except subprocess.TimeoutExpired as error:
        stdout = decoded(error.stdout)
        intermediates, stages, values = parse_transcript(stdout)
        return {
            **common,
            "status": "TIMEOUT",
            "intermediate_stages": intermediates,
            "bracket_stages": stages,
            "brackets": values,
            "partial_stdout": stdout[-30000:],
            "partial_stderr": decoded(error.stderr)[-1000:],
        }
    stdout = process.stdout
    intermediates, stages, values = parse_transcript(stdout)
    valid = (
        process.returncode == 0 and "END" in stdout and "?" not in stdout
        and len(intermediates) == 61 and len(stages) == 14 and len(values) == 14
    )
    return {
        **common,
        "status": "COMPLETE" if valid else "ERROR",
        "intermediate_stages": intermediates,
        "bracket_stages": stages,
        "brackets": values,
        "stdout_tail": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, collection_complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-r76-brackets-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-r76-brackets",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_cache_sha256": CACHE_SHA256,
        "source_graph_sha256": GRAPH_SHA256,
        "source_raw_core_sha256": RAW_CORE_SHA256,
        "source_progressive_sha256": PROGRESSIVE_SHA256,
        "source_timeout_sha256": SOURCE_TIMEOUT_SHA256,
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
    require(hashlib.sha256(RAW_CORE.read_bytes()).hexdigest() == RAW_CORE_SHA256,
            "raw-core custody")
    require(hashlib.sha256(PROGRESSIVE.read_bytes()).hexdigest() ==
            PROGRESSIVE_SHA256, "progressive-core custody")
    require(hashlib.sha256(SOURCE_TIMEOUT.read_bytes()).hexdigest() ==
            SOURCE_TIMEOUT_SHA256, "timeout custody")
    write_checkpoint(None, collection_complete=False)
    try:
        row = retain_brackets.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, collection_complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "collection_complete": complete,
        "status": row["status"],
        "intermediate_count": len(row.get("intermediate_stages", [])),
        "bracket_count": len(row.get("brackets", [])),
        "bracket_stages": row.get("bracket_stages"),
    }, sort_keys=True))
