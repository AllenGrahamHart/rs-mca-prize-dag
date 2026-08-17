#!/usr/bin/env python3
"""Adjoin q7 to the generic q5 quotient with Groebner.jl."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile

import modal


DIRECTORY = Path(__file__).parent
Q5 = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_bank_extension_result.json"
Q7 = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_coefficients_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_extension_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_extension_result.json"
REMOTE_Q5 = "/root/q5.json"
REMOTE_Q7 = "/root/q7.json"
REMOTE_PROGRAM = "/root/fff_generic_q7_extension_program.py"
Q5_SHA256 = "b5320657fc191da5adf2743ad020ab6a30934fd584f7f3f3a995caf9a712953c"
Q7_SHA256 = "37e2f17f8546e195024c23766f63cd36ba8681c115f3bf18f7410c19c902c45d"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-generic-q7-extension")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; "
        'Pkg.add(["AbstractAlgebra", "Groebner"]); Pkg.precompile()\''
    )
    .add_local_file(Q5, REMOTE_Q5)
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


@app.function(image=image, cpu=1.0, memory=16384, timeout=660)
def extend_q7():
    core = load("fff_generic_q7_extension", REMOTE_PROGRAM)
    built = core.build(json.loads(Path(REMOTE_Q5).read_text()),
                       json.loads(Path(REMOTE_Q7).read_text()))
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jl") as handle:
        handle.write(program); handle.flush()
        try:
            process = subprocess.run(["julia", "--startup-file=no", handle.name],
                                     capture_output=True, text=True, timeout=600)
        except subprocess.TimeoutExpired as error:
            return {**common, "status": "TIMEOUT",
                    "partial_stdout": decoded(error.stdout)[-30000:],
                    "partial_stderr": decoded(error.stderr)[-30000:]}
    stdout = process.stdout
    input_profile = re.search(r"(?:^|\n)Q7_INPUT (\d+)", stdout)
    profile = re.search(r"(?:^|\n)Q7_COMPLETE ([01]) (-?\d+) (\d+) (\d+)", stdout)
    certified = "Q7_EXTENSION_CERTIFIED" in stdout
    basis_path = Path("/tmp/fff_generic_q7_basis.txt")
    entries_path = Path("/tmp/fff_generic_q7_entries.txt")
    basis = basis_path.read_text().splitlines() if certified and basis_path.exists() else []
    entries = []
    if certified and entries_path.exists():
        for line in entries_path.read_text().splitlines():
            basis_index, term_index, numerator, denominator = line.split("\t", 3)
            entries.append({"basis_index": int(basis_index), "term_index": int(term_index),
                            "numerator": [int(value) for value in numerator.split(",")],
                            "denominator": [int(value) for value in denominator.split(",")]})
    unique_denominators = []
    seen = set()
    for entry in entries:
        key = tuple(entry["denominator"])
        if key not in seen:
            seen.add(key); unique_denominators.append(entry["denominator"])
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
        "basis": basis, "basis_sha256": hashlib.sha256(basis_text.encode()).hexdigest(),
        "coefficient_entries": entries, "coefficient_entry_count": len(entries),
        "coefficient_entries_sha256": hashlib.sha256(entries_text.encode()).hexdigest(),
        "unique_denominators": unique_denominators,
        "unique_denominator_count": len(unique_denominators),
        "unique_denominators_sha256": hashlib.sha256(denominators_text.encode()).hexdigest(),
        "stdout_tail": stdout[-30000:], "stderr_tail": process.stderr[-30000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, complete):
    RESULT.write_text(json.dumps({
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-generic-q7-extension-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-generic-q7-extension",
        "collection_complete": complete, "field": 2130706433,
        "source_q5_sha256": Q5_SHA256, "source_q7_sha256": Q7_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(Q5.read_bytes()).hexdigest() == Q5_SHA256, "q5 custody")
    require(hashlib.sha256(Q7.read_bytes()).hexdigest() == Q7_SHA256, "q7 custody")
    write_checkpoint(None, False)
    try:
        row = extend_q7.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}; write_checkpoint(row, complete)
    print(json.dumps({"result": str(RESULT), "status": row["status"],
                      "input_term_count": row.get("input_term_count"),
                      "unit": row.get("unit"), "dimension": row.get("dimension"),
                      "basis_size": row.get("basis_size"),
                      "quotient_dimension": row.get("quotient_dimension"),
                      "unique_denominator_count": row.get("unique_denominator_count")},
                     sort_keys=True))
