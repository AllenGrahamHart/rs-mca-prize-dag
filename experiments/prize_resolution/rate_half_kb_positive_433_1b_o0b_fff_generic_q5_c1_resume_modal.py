#!/usr/bin/env python3
"""Bounded long-wall retry for the sole open generic q5 coefficient C1."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile

import modal


DIRECTORY = Path(__file__).parent
Q5 = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_q5_coefficients_result.json"
GENERIC = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json"
FRONTIER = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_coefficients_julia_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_coefficients_julia_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_c1_resume_result.json"
REMOTE_Q5 = "/root/q5.json"
REMOTE_GENERIC = "/root/generic.json"
REMOTE_PROGRAM = "/root/fff_generic_q5_coefficients_program.py"
Q5_SHA256 = "25b3ac23d74e0bb710c50d636048c0f95ea4b94d51f3c5e02634cbfdfddf5f6e"
GENERIC_SHA256 = "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e"
FRONTIER_SHA256 = "29a3236a322bf5ec1b797615fed99ccbb0b584981656eec04bd41da00989700c"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-generic-q5-c1-resume")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; "
        'Pkg.add(["AbstractAlgebra", "Groebner"]); Pkg.precompile()\''
    )
    .add_local_file(Q5, REMOTE_Q5)
    .add_local_file(GENERIC, REMOTE_GENERIC)
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


@app.function(image=image, cpu=1.0, memory=8192, timeout=720)
def reduce_c1():
    core = load("fff_generic_q5_coefficient", REMOTE_PROGRAM)
    built = core.build(
        1,
        json.loads(Path(REMOTE_Q5).read_text()),
        json.loads(Path(REMOTE_GENERIC).read_text()),
    )
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jl") as handle:
        handle.write(program)
        handle.flush()
        try:
            process = subprocess.run(
                ["julia", "--startup-file=no", handle.name],
                capture_output=True, text=True, timeout=660,
            )
        except subprocess.TimeoutExpired as error:
            return {
                **common,
                "status": "TIMEOUT",
                "partial_stdout": decoded(error.stdout)[-30000:],
                "partial_stderr": decoded(error.stderr)[-30000:],
            }
    stdout = process.stdout
    profile = re.search(r"(?:^|\n)COEFFICIENT_COMPLETE 1 (-?\d+) (\d+)", stdout)
    certified = "COEFFICIENT_CERTIFIED" in stdout
    normal_path = Path("/tmp/fff_generic_q5_coefficient.txt")
    entries_path = Path("/tmp/fff_generic_q5_coefficient_entries.txt")
    normal = normal_path.read_text().strip() if certified and normal_path.exists() else ""
    entries = []
    if certified and entries_path.exists():
        for line in entries_path.read_text().splitlines():
            term_index, numerator, denominator = line.split("\t", 2)
            entries.append({
                "term_index": int(term_index),
                "numerator": [int(value) for value in numerator.split(",")],
                "denominator": [int(value) for value in denominator.split(",")],
            })
    unique_denominators = []
    seen = set()
    for entry in entries:
        key = tuple(entry["denominator"])
        if key not in seen:
            seen.add(key)
            unique_denominators.append(entry["denominator"])
    entries_text = json.dumps(entries, separators=(",", ":"))
    denominators_text = json.dumps(unique_denominators, separators=(",", ":"))
    valid = process.returncode == 0 and certified and profile is not None and normal and entries
    return {
        **common,
        "status": "COMPLETE" if valid else "ERROR",
        "normal_degree": int(profile.group(1)) if profile else None,
        "normal_term_count": int(profile.group(2)) if profile else None,
        "normal": normal,
        "normal_sha256": hashlib.sha256(normal.encode()).hexdigest(),
        "coefficient_entries": entries,
        "coefficient_entry_count": len(entries),
        "coefficient_entries_sha256": hashlib.sha256(entries_text.encode()).hexdigest(),
        "unique_denominators": unique_denominators,
        "unique_denominator_count": len(unique_denominators),
        "unique_denominators_sha256":
            hashlib.sha256(denominators_text.encode()).hexdigest(),
        "stdout_tail": stdout[-30000:],
        "stderr_tail": process.stderr[-30000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, collection_complete):
    RESULT.write_text(json.dumps({
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-generic-q5-c1-resume-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-generic-q5-c1-resume",
        "collection_complete": collection_complete,
        "field": 2130706433,
        "source_q5_sha256": Q5_SHA256,
        "source_generic_sha256": GENERIC_SHA256,
        "source_frontier_sha256": FRONTIER_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(Q5.read_bytes()).hexdigest() == Q5_SHA256,
            "q5 custody")
    require(hashlib.sha256(GENERIC.read_bytes()).hexdigest() == GENERIC_SHA256,
            "generic custody")
    require(hashlib.sha256(FRONTIER.read_bytes()).hexdigest() == FRONTIER_SHA256,
            "frontier custody")
    frontier = json.loads(FRONTIER.read_text())["rows"]
    require([row["status"] for row in frontier] ==
            ["COMPLETE", "TIMEOUT", "COMPLETE"], "frontier profile")
    write_checkpoint(None, False)
    try:
        row = reduce_c1.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, complete)
    print(json.dumps({
        "result": str(RESULT),
        "status": row["status"],
        "normal_degree": row.get("normal_degree"),
        "normal_term_count": row.get("normal_term_count"),
        "normal_sha256": row.get("normal_sha256"),
    }, sort_keys=True))
