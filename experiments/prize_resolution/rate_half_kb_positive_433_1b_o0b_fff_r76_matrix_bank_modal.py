#!/usr/bin/env python3
"""Build the exact generic FFF R76 multiplication-matrix bank on Modal."""

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
BASE_PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_q6_block_determinant_program.py"
R76_PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_multiplication_determinant_program.py"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_matrix_bank_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_r76_matrix_bank_result.json"
REMOTE_BANK = "/root/q5_multiplication_bank.json"
REMOTE_Q7 = "/root/q7_coefficients.json"
REMOTE_BASE_PROGRAM = "/root/fff_q6_block_determinant_program.py"
REMOTE_R76_PROGRAM = "/root/fff_r76_multiplication_determinant_program.py"
REMOTE_PROGRAM = "/root/fff_r76_matrix_bank_program.py"
BANK_SHA256 = "3d216da7d91c82a1360f932673ce3529278c90f81e6a8a6767f14a34ad73a45e"
Q7_SHA256 = "37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d"
BASE_PROGRAM_SHA256 = "fff178007fdea5ae7c14a0bee59fde6053aacc1a47f7a23f5d0c3bc654ab6224"
R76_PROGRAM_SHA256 = "ac73c2251e90e6a84b45574dd171474c682586ff56415206d3453f355d49e33f"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-r76-matrix-bank")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands("julia -e 'using Pkg; Pkg.add(\"AbstractAlgebra\"); Pkg.precompile()'")
    .add_local_file(BANK, REMOTE_BANK)
    .add_local_file(Q7, REMOTE_Q7)
    .add_local_file(BASE_PROGRAM, REMOTE_BASE_PROGRAM)
    .add_local_file(R76_PROGRAM, REMOTE_R76_PROGRAM)
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
    match = re.search(r"(?:^|\n)WITNESS_COMPLETE (\d+) (\d+) (\d+)", stdout)
    if match is None or "WITNESS_CERTIFIED" not in stdout:
        return {"witness_complete": False}
    return {
        "witness_complete": True,
        "witness_t": int(match.group(1)),
        "witness_determinant": int(match.group(2)),
        "witness_nonzero_entries": int(match.group(3)),
    }


@app.function(image=image, cpu=1.0, memory=24576, timeout=1860)
def build_matrix_bank():
    base_core = load("fff_q6_block_determinant", REMOTE_BASE_PROGRAM)
    r76_core = load("fff_r76_multiplication_determinant", REMOTE_R76_PROGRAM)
    core = load("fff_r76_matrix_bank", REMOTE_PROGRAM)
    built = core.build(base_core, r76_core,
                       json.loads(Path(REMOTE_BANK).read_text()),
                       json.loads(Path(REMOTE_Q7).read_text()))
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jl") as handle:
        handle.write(program)
        handle.flush()
        try:
            process = subprocess.run(
                ["julia", "--startup-file=no", handle.name], capture_output=True,
                text=True, timeout=1800
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
    profile = re.search(r"(?:^|\n)SYMBOLIC_R76_MATRIX (\d+)", stdout)
    certified = "R76_MATRIX_BANK_CERTIFIED" in stdout
    entries_path = Path("/tmp/fff_r76_matrix_entries.txt")
    entries = []
    if certified and entries_path.exists():
        for line in entries_path.read_text().splitlines():
            row, column, numerator, denominator = line.split("\t", 3)
            entries.append({
                "row": int(row), "column": int(column),
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
    canonical = [{"row": entry["row"], "column": entry["column"],
                  "numerator": entry["numerator"],
                  "denominator": entry["denominator"]} for entry in entries]
    valid = (
        process.returncode == 0 and witness.get("witness_complete") is True and
        profile is not None and int(profile.group(1)) == 256 and certified and
        len(entries) == 256
    )
    return {
        **common, **witness, "status": "COMPLETE" if valid else "ERROR",
        "matrix_nonzero_entry_count": int(profile.group(1)) if profile else None,
        "matrix_entries": entries,
        "matrix_entries_sha256": hashlib.sha256(
            json.dumps(canonical, separators=(",", ":")).encode()
        ).hexdigest(),
        "unique_denominators": unique_denominators,
        "unique_denominator_count": len(unique_denominators),
        "unique_denominators_sha256": hashlib.sha256(
            json.dumps(unique_denominators, separators=(",", ":")).encode()
        ).hexdigest(),
        "stdout_tail": stdout[-50000:], "stderr_tail": process.stderr[-50000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-r76-matrix-bank-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-r76-matrix-bank",
        "collection_complete": complete,
        "field": 2130706433,
        "source_bank_sha256": BANK_SHA256,
        "source_q7_sha256": Q7_SHA256,
        "source_base_program_sha256": BASE_PROGRAM_SHA256,
        "source_r76_program_sha256": R76_PROGRAM_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }
    RESULT.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")


@app.local_entrypoint()
def main():
    for path, digest, label in ((BANK, BANK_SHA256, "bank"),
                                (Q7, Q7_SHA256, "q7"),
                                (BASE_PROGRAM, BASE_PROGRAM_SHA256, "base program"),
                                (R76_PROGRAM, R76_PROGRAM_SHA256, "R76 program")):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                f"{label} custody")
    write_checkpoint(None, False)
    try:
        row = build_matrix_bank.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, complete)
    print(json.dumps({
        "result": str(RESULT), "status": row["status"],
        "witness_complete": row.get("witness_complete"),
        "matrix_nonzero_entry_count": row.get("matrix_nonzero_entry_count"),
        "unique_denominator_count": row.get("unique_denominator_count"),
    }, sort_keys=True))
