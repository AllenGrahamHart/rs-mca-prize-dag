#!/usr/bin/env python3
"""Compute the exact cleared R76 determinant by NTT on Modal."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile

import modal


DIRECTORY = Path(__file__).parent
MATRIX = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_polynomial_matrix_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_ntt_determinant_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_ntt_determinant_result.json"
REMOTE_MATRIX = "/root/r76_polynomial_matrix.json"
REMOTE_PROGRAM = "/root/fff_r76_ntt_determinant_program.py"
MATRIX_SHA256 = "ea218c257268a7887bf296dcb7d9e8f97ca3591866ca04e6595b3cd8170a0dae"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-r76-ntt-determinant")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("g++")
    .add_local_file(MATRIX, REMOTE_MATRIX)
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


@app.function(image=image, cpu=8.0, memory=8192, timeout=660)
def compute_determinant():
    core = load("fff_r76_ntt_determinant", REMOTE_PROGRAM)
    built = core.build(json.loads(Path(REMOTE_MATRIX).read_text()))
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    with tempfile.TemporaryDirectory() as temporary:
        source = Path(temporary) / "determinant.cpp"
        binary = Path(temporary) / "determinant"
        source.write_text(program)
        compile_process = subprocess.run(
            ["g++", "-O3", "-std=c++17", "-fopenmp", "-march=x86-64",
             str(source), "-o", str(binary)], capture_output=True, text=True,
            timeout=180
        )
        if compile_process.returncode != 0:
            return {**common, "status": "COMPILE_ERROR",
                    "compile_stdout": compile_process.stdout[-50000:],
                    "compile_stderr": compile_process.stderr[-50000:],
                    "input_program": program}
        try:
            process = subprocess.run([str(binary)], capture_output=True, text=True,
                                     timeout=420)
        except subprocess.TimeoutExpired as error:
            return {**common, "status": "TIMEOUT",
                    "partial_stdout": decoded(error.stdout)[-50000:],
                    "partial_stderr": decoded(error.stderr)[-50000:]}
    stdout = process.stdout
    ntt_profile = re.search(
        r"(?:^|\n)NTT_PROFILE (\d+) (\d+) (\d+) (\d+)", stdout
    )
    witness = re.search(
        r"(?:^|\n)WITNESS_COMPLETE (\d+) (\d+) (\d+) (\d+)", stdout
    )
    determinant_profile = re.search(
        r"(?:^|\n)DETERMINANT_COMPLETE (\d+) (\d+)", stdout
    )
    certified = "R76_NTT_DETERMINANT_CERTIFIED" in stdout
    determinant_path = Path("/tmp/fff_r76_ntt_determinant.txt")
    coefficients = []
    if certified and determinant_path.exists():
        coefficients = [int(value) for value in
                        determinant_path.read_text().strip().split(",")]
    valid = (
        process.returncode == 0 and ntt_profile is not None and
        int(ntt_profile.group(1)) == 32768 and
        int(ntt_profile.group(2)) == 1168510561 and
        int(ntt_profile.group(3)) == 22208 and witness is not None and
        int(witness.group(1)) == 2 and int(witness.group(2)) == 1087830147 and
        int(witness.group(3)) == 3 and determinant_profile is not None and
        len(coefficients) == int(determinant_profile.group(1)) + 1 and certified
    )
    return {
        **common, "status": "COMPLETE" if valid else "ERROR",
        "worker_threads": int(ntt_profile.group(4)) if ntt_profile else None,
        "witness_t": int(witness.group(1)) if witness else None,
        "witness_determinant": int(witness.group(2)) if witness else None,
        "holdout_t": int(witness.group(3)) if witness else None,
        "holdout_determinant": int(witness.group(4)) if witness else None,
        "determinant_degree": int(determinant_profile.group(1))
        if determinant_profile else None,
        "determinant_term_count": int(determinant_profile.group(2))
        if determinant_profile else None,
        "determinant_coefficients": coefficients,
        "determinant_coefficients_sha256": hashlib.sha256(
            json.dumps(coefficients, separators=(",", ":")).encode()
        ).hexdigest(),
        "stdout_tail": stdout[-50000:], "stderr_tail": process.stderr[-50000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-r76-ntt-determinant-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-r76-ntt-determinant",
        "collection_complete": complete,
        "field": 2130706433,
        "source_matrix_sha256": MATRIX_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }
    RESULT.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(MATRIX.read_bytes()).hexdigest() == MATRIX_SHA256,
            "polynomial-matrix custody")
    write_checkpoint(None, False)
    try:
        row = compute_determinant.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, complete)
    print(json.dumps({
        "result": str(RESULT), "status": row["status"],
        "determinant_degree": row.get("determinant_degree"),
        "determinant_term_count": row.get("determinant_term_count"),
        "witness_determinant": row.get("witness_determinant"),
        "holdout_determinant": row.get("holdout_determinant"),
        "worker_threads": row.get("worker_threads"),
    }, sort_keys=True))
