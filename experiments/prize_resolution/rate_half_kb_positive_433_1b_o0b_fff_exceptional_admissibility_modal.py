#!/usr/bin/env python3
"""Run guarded q4 replays for the nine exceptional FFF survivors on Modal."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
CACHE = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
SURVIVORS = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_specializations_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_admissibility_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_admissibility_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_SURVIVORS = "/root/survivors.json"
REMOTE_PROGRAM = "/root/exceptional_admissibility_program.py"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
SURVIVORS_SHA256 = "c066bb4f5813be4915e40a51225287cfde11284b3b3df4cabdae889778a97b88"
ROOT_VALUES = [
    0, 1, 16711679, 47655010, 451278922, 1629292471, 1893783428,
    2113994754, 2130706432,
]

app = modal.App("rs-mca-positive-433-1b-o0b-fff-exceptional-admissibility")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(CACHE, REMOTE_CACHE)
    .add_local_file(SURVIVORS, REMOTE_SURVIVORS)
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
            r"(?:^|\n)STAGE=([a-z0-9:]+),DIM=(-?\d+),SIZE=(\d+)", stdout
        )
    ]


@app.function(image=image, cpu=1.0, memory=8192, timeout=360)
def decide_root(root):
    core = load("exceptional_admissibility", REMOTE_PROGRAM)
    built = core.build(json.loads(Path(REMOTE_CACHE).read_text()),
                       json.loads(Path(REMOTE_SURVIVORS).read_text()), root)
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=300
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
        [stage["stage"] for stage in stages] == built["expected_stages"] and
        dimension is not None and size is not None and
        ((unit and int(size.group(1)) == 1) or
         (not unit and len(basis) == int(size.group(1))))
    )
    first_unit = next(
        (stage["stage"] for stage in stages
         if stage["dimension"] == -1 and stage["basis_size"] == 1), None
    )
    return {
        **common, "status": "COMPLETE" if valid else "ERROR",
        "stages": stages, "first_unit_stage": first_unit, "unit": unit,
        "dimension": int(dimension.group(1)) if dimension else None,
        "basis_size": int(size.group(1)) if size else None, "basis": basis,
        "basis_sha256": hashlib.sha256(
            json.dumps(basis, separators=(",", ":")).encode()
        ).hexdigest(),
        "stdout_tail": stdout[-50000:], "stderr_tail": process.stderr[-5000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(rows, complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-exceptional-admissibility-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-exceptional-admissibility",
        "collection_complete": complete, "field": 2130706433,
        "source_cache_sha256": CACHE_SHA256,
        "source_survivors_sha256": SURVIVORS_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "roots": ROOT_VALUES, "rows": rows,
    }
    RESULT.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")


@app.local_entrypoint()
def main():
    for path, digest in ((CACHE, CACHE_SHA256), (SURVIVORS, SURVIVORS_SHA256)):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "source custody")
    write_checkpoint([], False)
    rows = []
    for root, remote in zip(
            ROOT_VALUES,
            decide_root.map(ROOT_VALUES, order_outputs=True, return_exceptions=True)):
        rows.append({"root": root, "status": "REMOTE_ERROR", "error": repr(remote)}
                    if isinstance(remote, BaseException) else remote)
        write_checkpoint(rows, False)
    complete = all(row["status"] in {"COMPLETE", "TIMEOUT"} for row in rows)
    write_checkpoint(rows, complete)
    print(json.dumps({
        "result": str(RESULT), "collection_complete": complete,
        "rows": [{"root": row["root"], "status": row["status"],
                  "unit": row.get("unit"),
                  "first_unit_stage": row.get("first_unit_stage")}
                 for row in rows],
    }, sort_keys=True))
