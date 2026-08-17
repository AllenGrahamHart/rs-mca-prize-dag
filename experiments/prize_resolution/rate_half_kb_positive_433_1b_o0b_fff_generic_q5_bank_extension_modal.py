#!/usr/bin/env python3
"""Adjoin the completed generic q5 coefficient bank with Groebner.jl."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile

import modal


DIRECTORY = Path(__file__).parent
GENERIC = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json"
FRONTIER = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_coefficients_julia_result.json"
C1 = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_c1_resume_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_bank_extension_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_bank_extension_result.json"
REMOTE_GENERIC = "/root/generic.json"
REMOTE_FRONTIER = "/root/frontier.json"
REMOTE_C1 = "/root/c1.json"
REMOTE_PROGRAM = "/root/fff_generic_q5_bank_extension_program.py"
GENERIC_SHA256 = "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e"
FRONTIER_SHA256 = "29a3236a322bf5ec1b797615fed99ccbb0b584981656eec04bd41da00989700c"
C1_SHA256 = "899f7706130a8ef3d6556ecc14aeda397868dcd8261db5f6df96c85519d3fc1c"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-generic-q5-bank-extension")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; "
        'Pkg.add(["AbstractAlgebra", "Groebner"]); Pkg.precompile()\''
    )
    .add_local_file(GENERIC, REMOTE_GENERIC)
    .add_local_file(FRONTIER, REMOTE_FRONTIER)
    .add_local_file(C1, REMOTE_C1)
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


@app.function(image=image, cpu=1.0, memory=8192, timeout=420)
def extend_q5():
    core = load("fff_generic_q5_bank_extension", REMOTE_PROGRAM)
    built = core.build(
        json.loads(Path(REMOTE_GENERIC).read_text()),
        json.loads(Path(REMOTE_FRONTIER).read_text()),
        json.loads(Path(REMOTE_C1).read_text()),
    )
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jl") as handle:
        handle.write(program)
        handle.flush()
        try:
            process = subprocess.run(
                ["julia", "--startup-file=no", handle.name],
                capture_output=True, text=True, timeout=360,
            )
        except subprocess.TimeoutExpired as error:
            return {
                **common, "status": "TIMEOUT",
                "partial_stdout": decoded(error.stdout)[-30000:],
                "partial_stderr": decoded(error.stderr)[-30000:],
            }
    stdout = process.stdout
    input_profile = re.search(r"(?:^|\n)Q5_BANK_INPUT (\d+)", stdout)
    profile = re.search(
        r"(?:^|\n)Q5_BANK_COMPLETE ([01]) (-?\d+) (\d+) (\d+)", stdout
    )
    certified = "Q5_BANK_CERTIFIED" in stdout
    basis_path = Path("/tmp/fff_generic_q5_bank_basis.txt")
    entries_path = Path("/tmp/fff_generic_q5_bank_coefficients.txt")
    basis = basis_path.read_text().splitlines() if certified and basis_path.exists() else []
    entries = []
    if certified and entries_path.exists():
        for line in entries_path.read_text().splitlines():
            basis_index, term_index, numerator, denominator = line.split("\t", 3)
            entries.append({
                "basis_index": int(basis_index), "term_index": int(term_index),
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
    basis_text = "\n".join(basis)
    entries_text = json.dumps(entries, separators=(",", ":"))
    denominators_text = json.dumps(unique_denominators, separators=(",", ":"))
    valid = (process.returncode == 0 and certified and input_profile is not None
             and profile is not None and len(basis) == int(profile.group(3)) and entries)
    return {
        **common, "status": "COMPLETE" if valid else "ERROR",
        "input_term_count": int(input_profile.group(1)) if input_profile else None,
        "unit": bool(int(profile.group(1))) if profile else None,
        "dimension": int(profile.group(2)) if profile else None,
        "basis_size": int(profile.group(3)) if profile else None,
        "quotient_dimension": int(profile.group(4)) if profile else None,
        "basis": basis,
        "basis_sha256": hashlib.sha256(basis_text.encode()).hexdigest(),
        "coefficient_entries": entries,
        "coefficient_entry_count": len(entries),
        "coefficient_entries_sha256": hashlib.sha256(entries_text.encode()).hexdigest(),
        "unique_denominators": unique_denominators,
        "unique_denominator_count": len(unique_denominators),
        "unique_denominators_sha256":
            hashlib.sha256(denominators_text.encode()).hexdigest(),
        "stdout_tail": stdout[-30000:], "stderr_tail": process.stderr[-30000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, complete):
    RESULT.write_text(json.dumps({
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-generic-q5-bank-extension-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-generic-q5-bank-extension",
        "collection_complete": complete,
        "field": 2130706433,
        "source_generic_sha256": GENERIC_SHA256,
        "source_frontier_sha256": FRONTIER_SHA256,
        "source_c1_sha256": C1_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    for path, digest, label in ((GENERIC, GENERIC_SHA256, "generic"),
                                (FRONTIER, FRONTIER_SHA256, "frontier"),
                                (C1, C1_SHA256, "c1")):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                f"{label} custody")
    write_checkpoint(None, False)
    try:
        row = extend_q5.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, complete)
    print(json.dumps({
        "result": str(RESULT), "status": row["status"],
        "input_term_count": row.get("input_term_count"), "unit": row.get("unit"),
        "dimension": row.get("dimension"), "basis_size": row.get("basis_size"),
        "quotient_dimension": row.get("quotient_dimension"),
        "unique_denominator_count": row.get("unique_denominator_count"),
    }, sort_keys=True))
