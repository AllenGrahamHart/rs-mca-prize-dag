#!/usr/bin/env python3
"""Certify the generic FFF q6 block determinant on Modal."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile

import modal


DIRECTORY = Path(__file__).parent
BANK = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_q5_multiplication_bank_result.json"
Q7 = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_coefficients_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_q6_block_determinant_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_q6_block_determinant_result.json"
REMOTE_BANK = "/root/q5_multiplication_bank.json"
REMOTE_Q7 = "/root/q7_coefficients.json"
REMOTE_PROGRAM = "/root/fff_q6_block_determinant_program.py"
BANK_SHA256 = "3d216da7d91c82a1360f932673ce3529278c90f81e6a8a6767f14a34ad73a45e"
Q7_SHA256 = "37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-q6-block-determinant")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands("julia -e 'using Pkg; Pkg.add(\"AbstractAlgebra\"); Pkg.precompile()'")
    .add_local_file(BANK, REMOTE_BANK)
    .add_local_file(Q7, REMOTE_Q7)
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


def parse_witness(stdout):
    match = re.search(r"(?:^|\n)WITNESS_COMPLETE (\d+) (\d+) (\d+) (\d+)", stdout)
    if match is None or "WITNESS_CERTIFIED" not in stdout:
        return {"witness_complete": False}
    return {
        "witness_complete": True,
        "witness_t": int(match.group(1)),
        "witness_d2_determinant": int(match.group(2)),
        "witness_q6_determinant": int(match.group(3)),
        "witness_q6_nonzero_entries": int(match.group(4)),
        "witness_q7_identity": True,
    }


@app.function(image=image, cpu=1.0, memory=24576, timeout=1260)
def certify_block_determinant():
    core = load("fff_q6_block_determinant", REMOTE_PROGRAM)
    built = core.build(json.loads(Path(REMOTE_BANK).read_text()),
                       json.loads(Path(REMOTE_Q7).read_text()))
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jl") as handle:
        handle.write(program)
        handle.flush()
        try:
            process = subprocess.run(
                ["julia", "--startup-file=no", handle.name], capture_output=True,
                text=True, timeout=1200
            )
        except subprocess.TimeoutExpired as error:
            stdout = decoded(error.stdout)
            return {
                **common, **parse_witness(stdout), "status": "TIMEOUT",
                "partial_stdout": stdout[-50000:],
                "partial_stderr": decoded(error.stderr)[-50000:],
            }
    stdout = process.stdout
    witness = parse_witness(stdout)
    d2_profile = re.search(
        r"(?:^|\n)SYMBOLIC_D2_COMPLETE (\d+) (\d+) (\d+) (\d+)", stdout
    )
    q6_matrix_profile = re.search(r"(?:^|\n)SYMBOLIC_Q6_MATRIX (\d+)", stdout)
    q6_profile = re.search(
        r"(?:^|\n)SYMBOLIC_Q6_COMPLETE (\d+) (\d+) (\d+) (\d+)", stdout
    )
    certified = "Q6_BLOCK_DETERMINANT_CERTIFIED" in stdout
    determinant_path = Path("/tmp/fff_q6_block_determinants.txt")
    determinants = {}
    if certified and determinant_path.exists():
        for line in determinant_path.read_text().splitlines():
            label, values = line.split("\t", 1)
            determinants[label] = [int(value) for value in values.split(",")]
    labels = ["D2_NUM", "D2_DEN", "Q6_NUM", "Q6_DEN"]
    canonical = [{"label": label, "coefficients": determinants.get(label, [])}
                 for label in labels]
    valid = (
        process.returncode == 0 and witness.get("witness_complete") is True and
        d2_profile is not None and q6_matrix_profile is not None and
        q6_profile is not None and certified and
        all(determinants.get(label) for label in labels)
    )
    return {
        **common, **witness, "status": "COMPLETE" if valid else "ERROR",
        "symbolic_d2_numerator_degree": int(d2_profile.group(1)) if d2_profile else None,
        "symbolic_d2_denominator_degree": int(d2_profile.group(2)) if d2_profile else None,
        "symbolic_d2_numerator_terms": int(d2_profile.group(3)) if d2_profile else None,
        "symbolic_d2_denominator_terms": int(d2_profile.group(4)) if d2_profile else None,
        "symbolic_q6_nonzero_entries": int(q6_matrix_profile.group(1))
        if q6_matrix_profile else None,
        "symbolic_q6_numerator_degree": int(q6_profile.group(1)) if q6_profile else None,
        "symbolic_q6_denominator_degree": int(q6_profile.group(2)) if q6_profile else None,
        "symbolic_q6_numerator_terms": int(q6_profile.group(3)) if q6_profile else None,
        "symbolic_q6_denominator_terms": int(q6_profile.group(4)) if q6_profile else None,
        "symbolic_determinants": canonical,
        "symbolic_determinants_sha256": hashlib.sha256(
            json.dumps(canonical, separators=(",", ":")).encode()
        ).hexdigest(),
        "stdout_tail": stdout[-50000:], "stderr_tail": process.stderr[-50000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, complete):
    RESULT.write_text(json.dumps({
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-q6-block-determinant-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-q6-block-determinant",
        "collection_complete": complete,
        "field": 2130706433,
        "source_bank_sha256": BANK_SHA256,
        "source_q7_sha256": Q7_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(BANK.read_bytes()).hexdigest() == BANK_SHA256,
            "multiplication-bank custody")
    require(hashlib.sha256(Q7.read_bytes()).hexdigest() == Q7_SHA256,
            "q7 custody")
    write_checkpoint(None, False)
    try:
        row = certify_block_determinant.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, complete)
    print(json.dumps({
        "result": str(RESULT), "status": row["status"],
        "witness_complete": row.get("witness_complete"),
        "witness_t": row.get("witness_t"),
        "witness_d2_determinant": row.get("witness_d2_determinant"),
        "witness_q6_determinant": row.get("witness_q6_determinant"),
        "symbolic_q6_numerator_degree": row.get("symbolic_q6_numerator_degree"),
        "symbolic_q6_denominator_degree": row.get("symbolic_q6_denominator_degree"),
    }, sort_keys=True))
