#!/usr/bin/env python3
"""Build the column-cleared FFF R76 polynomial-matrix bank on Modal."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile

import modal


DIRECTORY = Path(__file__).parent
MATRIX = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_matrix_bank_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_polynomial_matrix_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_polynomial_matrix_result.json"
REMOTE_MATRIX = "/root/r76_matrix_bank.json"
REMOTE_PROGRAM = "/root/fff_r76_polynomial_matrix_program.py"
MATRIX_SHA256 = "701f4a255f2f573b4f50d7bbf3ea14b80ae8562ae09d93f96a8409cb45babbfb"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-r76-polynomial-matrix")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands("julia -e 'using Pkg; Pkg.add(\"AbstractAlgebra\"); Pkg.precompile()'")
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


@app.function(image=image, cpu=1.0, memory=16384, timeout=660)
def build_polynomial_matrix():
    core = load("fff_r76_polynomial_matrix", REMOTE_PROGRAM)
    built = core.build(json.loads(Path(REMOTE_MATRIX).read_text()))
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jl") as handle:
        handle.write(program)
        handle.flush()
        try:
            process = subprocess.run(
                ["julia", "--startup-file=no", handle.name], capture_output=True,
                text=True, timeout=600
            )
        except subprocess.TimeoutExpired as error:
            return {
                **common, "status": "TIMEOUT",
                "partial_stdout": decoded(error.stdout)[-50000:],
                "partial_stderr": decoded(error.stderr)[-50000:],
            }
    stdout = process.stdout
    lcm_profiles = [{"column": int(column), "degree": int(degree),
                     "term_count": int(terms)}
                    for column, degree, terms in re.findall(
                        r"(?:^|\n)COLUMN_LCM (\d+) (\d+) (\d+)", stdout)]
    matrix_profile = re.search(
        r"(?:^|\n)POLYNOMIAL_MATRIX_PROFILE (\d+) (\d+) (\d+)", stdout
    )
    witness = re.search(
        r"(?:^|\n)WITNESS_COMPLETE (\d+) (\d+) (\d+) (\d+)", stdout
    )
    certified = "R76_POLYNOMIAL_MATRIX_CERTIFIED" in stdout
    lcm_path = Path("/tmp/fff_r76_column_lcms.txt")
    matrix_path = Path("/tmp/fff_r76_polynomial_matrix.txt")
    column_lcms = []
    if certified and lcm_path.exists():
        for line in lcm_path.read_text().splitlines():
            column, coefficients = line.split("\t", 1)
            column_lcms.append({"column": int(column),
                                "coefficients": [int(x) for x in coefficients.split(",")]})
    entries = []
    if certified and matrix_path.exists():
        for line in matrix_path.read_text().splitlines():
            row, column, coefficients = line.split("\t", 2)
            entries.append({"row": int(row), "column": int(column),
                            "coefficients": [int(x) for x in coefficients.split(",")]})
    valid = (
        process.returncode == 0 and len(lcm_profiles) == len(column_lcms) == 16 and
        matrix_profile is not None and int(matrix_profile.group(1)) == 256 and
        witness is not None and int(witness.group(1)) == 2 and
        int(witness.group(2)) == 244686406 and certified and len(entries) == 256
    )
    return {
        **common, "status": "COMPLETE" if valid else "ERROR",
        "column_lcm_profiles": lcm_profiles,
        "column_lcms": column_lcms,
        "column_lcms_sha256": hashlib.sha256(
            json.dumps(column_lcms, separators=(",", ":")).encode()
        ).hexdigest(),
        "matrix_nonzero_entry_count": int(matrix_profile.group(1))
        if matrix_profile else None,
        "matrix_minimum_degree": int(matrix_profile.group(2))
        if matrix_profile else None,
        "matrix_maximum_degree": int(matrix_profile.group(3))
        if matrix_profile else None,
        "matrix_entries": entries,
        "matrix_entries_sha256": hashlib.sha256(
            json.dumps(entries, separators=(",", ":")).encode()
        ).hexdigest(),
        "witness_t": int(witness.group(1)) if witness else None,
        "witness_rational_determinant": int(witness.group(2)) if witness else None,
        "witness_polynomial_determinant": int(witness.group(3)) if witness else None,
        "witness_column_scaling": int(witness.group(4)) if witness else None,
        "stdout_tail": stdout[-50000:], "stderr_tail": process.stderr[-50000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-r76-polynomial-matrix-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-r76-polynomial-matrix",
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
            "matrix-bank custody")
    write_checkpoint(None, False)
    try:
        row = build_polynomial_matrix.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, complete)
    print(json.dumps({
        "result": str(RESULT), "status": row["status"],
        "column_lcm_degrees": [item["degree"] for item in
                               row.get("column_lcm_profiles", [])],
        "matrix_degree_range": [row.get("matrix_minimum_degree"),
                                row.get("matrix_maximum_degree")],
        "witness_polynomial_determinant": row.get("witness_polynomial_determinant"),
    }, sort_keys=True))
