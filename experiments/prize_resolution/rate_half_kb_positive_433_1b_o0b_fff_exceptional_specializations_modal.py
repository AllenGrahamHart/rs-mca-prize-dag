#!/usr/bin/env python3
"""Run the fourteen original-system FFF exceptional specializations on Modal."""

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
ROOTS = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_roots_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_specializations_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_specializations_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_GRAPH = "/root/graph.json"
REMOTE_ROOTS = "/root/roots.json"
REMOTE_PROGRAM = "/root/fff_exceptional_specializations_program.py"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
GRAPH_SHA256 = "5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1"
ROOTS_SHA256 = "e845607b89e7d21159bd308cbf00f9a3fd74a25120bc4d479a607f7e9d8751a7"
ROOT_VALUES = [
    0, 1, 16711679, 47655010, 451278922, 465887767, 666570304,
    676802667, 1036595577, 1141382033, 1629292471, 1893783428,
    2113994754, 2130706432,
]

app = modal.App("rs-mca-positive-433-1b-o0b-fff-exceptional-specializations")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(CACHE, REMOTE_CACHE)
    .add_local_file(GRAPH, REMOTE_GRAPH)
    .add_local_file(ROOTS, REMOTE_ROOTS)
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
    return [
        {"stage": stage, "dimension": int(dimension), "basis_size": int(size)}
        for stage, dimension, size in re.findall(
            r"(?:^|\n)STAGE=(base|q5|q7|q6),DIM=(-?\d+),SIZE=(\d+)", stdout
        )
    ]


@app.function(image=image, cpu=1.0, memory=16384, timeout=660)
def decide_root(root):
    core = load("fff_exceptional_specializations", REMOTE_PROGRAM)
    built = core.build(json.loads(Path(REMOTE_CACHE).read_text()),
                       json.loads(Path(REMOTE_GRAPH).read_text()),
                       json.loads(Path(REMOTE_ROOTS).read_text()), root)
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=600
        )
    except subprocess.TimeoutExpired as error:
        stdout = decoded(error.stdout)
        return {
            **common, "status": "TIMEOUT", "stages": parse_stages(stdout),
            "partial_stdout": stdout[-50000:],
            "partial_stderr": decoded(error.stderr)[-5000:],
        }
    stdout = process.stdout
    stages = parse_stages(stdout)
    dimension = re.search(r"(?:^|\n)DIM=(-?\d+)", stdout)
    size = re.search(r"(?:^|\n)SIZE=(\d+)", stdout)
    unit = "UNIT=1" in stdout
    basis_match = re.search(r"BASIS_BEGIN\n(.*?)\nBASIS_END", stdout, re.DOTALL)
    basis = []
    if basis_match:
        basis = ["".join(value.split()) for value in re.findall(
            r"G\[\d+\]=(.*?)(?=^G\[\d+\]=|\Z)", basis_match.group(1),
            re.MULTILINE | re.DOTALL)]
    valid = (
        process.returncode == 0 and "END" in stdout and "?" not in stdout and
        [stage["stage"] for stage in stages] == ["base", "q5", "q7", "q6"] and
        dimension is not None and size is not None and
        ((unit and int(size.group(1)) == 1) or
         (not unit and len(basis) == int(size.group(1))))
    )
    return {
        **common, "status": "COMPLETE" if valid else "ERROR",
        "stages": stages, "unit": unit,
        "dimension": int(dimension.group(1)) if dimension else None,
        "basis_size": int(size.group(1)) if size else None,
        "basis": basis,
        "basis_sha256": hashlib.sha256(
            json.dumps(basis, separators=(",", ":")).encode()
        ).hexdigest(),
        "stdout_tail": stdout[-50000:], "stderr_tail": process.stderr[-5000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(rows, complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-exceptional-specializations-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-exceptional-specializations",
        "collection_complete": complete,
        "field": 2130706433,
        "source_cache_sha256": CACHE_SHA256,
        "source_graph_sha256": GRAPH_SHA256,
        "source_roots_sha256": ROOTS_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "roots": ROOT_VALUES,
        "rows": rows,
    }
    RESULT.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")


@app.local_entrypoint()
def main():
    for path, digest in ((CACHE, CACHE_SHA256), (GRAPH, GRAPH_SHA256),
                         (ROOTS, ROOTS_SHA256)):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "source custody")
    require(json.loads(ROOTS.read_text())["row"]["roots"] == ROOT_VALUES,
            "root custody")
    write_checkpoint([], False)
    rows = []
    for root, remote in zip(
            ROOT_VALUES,
            decide_root.map(ROOT_VALUES, order_outputs=True, return_exceptions=True)):
        if isinstance(remote, BaseException):
            rows.append({"root": root, "status": "REMOTE_ERROR",
                         "error": repr(remote)})
        else:
            rows.append(remote)
        write_checkpoint(rows, False)
    complete = all(row["status"] in {"COMPLETE", "TIMEOUT"} for row in rows)
    write_checkpoint(rows, complete)
    print(json.dumps({
        "result": str(RESULT), "collection_complete": complete,
        "rows": [{"root": row["root"], "status": row["status"],
                  "unit": row.get("unit"), "stages": row.get("stages")}
                 for row in rows],
    }, sort_keys=True))
