#!/usr/bin/env python3
"""Extract the q5 quotient multiplication bank with Groebner.jl."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile

import modal


DIRECTORY = Path(__file__).parent
CACHE = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
GENERIC = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json"
Q5 = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_bank_extension_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_q5_multiplication_bank_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_q5_multiplication_bank_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_GENERIC = "/root/generic.json"
REMOTE_Q5 = "/root/q5.json"
REMOTE_PROGRAM = "/root/fff_q5_multiplication_bank_program.py"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
GENERIC_SHA256 = "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e"
Q5_SHA256 = "b5320657fc191da5adf2743ad020ab6a30934fd584f7f3f3a995caf9a712953c"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-q5-multiplication-bank")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; "
        'Pkg.add(["AbstractAlgebra", "Groebner"]); Pkg.precompile()\''
    )
    .add_local_file(CACHE, REMOTE_CACHE)
    .add_local_file(GENERIC, REMOTE_GENERIC)
    .add_local_file(Q5, REMOTE_Q5)
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
def extract_bank():
    core = load("fff_q5_multiplication_bank", REMOTE_PROGRAM)
    built = core.build(json.loads(Path(REMOTE_CACHE).read_text()),
                       json.loads(Path(REMOTE_GENERIC).read_text()),
                       json.loads(Path(REMOTE_Q5).read_text()))
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
    matrix_profile = re.search(r"(?:^|\n)MATRIX_PROFILE (\d+) (\d+) (\d+)", stdout)
    kernel_profiles = [{"label": f"k{index}", "degree": int(degree),
                        "term_count": int(terms)}
                       for index, degree, terms in re.findall(
                           r"(?:^|\n)KERNEL_NORMAL (\d+) (-?\d+) (\d+)", stdout)]
    certified = "MULTIPLICATION_BANK_CERTIFIED" in stdout
    quotient_path = Path("/tmp/fff_q5_quotient_basis.txt")
    matrices_path = Path("/tmp/fff_q5_matrices.txt")
    kernels_path = Path("/tmp/fff_q5_kernel_normals.txt")
    kernel_entries_path = Path("/tmp/fff_q5_kernel_entries.txt")
    quotient_basis = quotient_path.read_text().splitlines() if certified and quotient_path.exists() else []
    matrix_entries = []
    if certified and matrices_path.exists():
        for line in matrices_path.read_text().splitlines():
            label, row, column, numerator, denominator = line.split("\t", 4)
            matrix_entries.append({"label": label, "row": int(row), "column": int(column),
                                   "numerator": [int(x) for x in numerator.split(",")],
                                   "denominator": [int(x) for x in denominator.split(",")]})
    kernel_normals = []
    if certified and kernels_path.exists():
        for line in kernels_path.read_text().splitlines():
            label, polynomial = line.split("\t", 1)
            kernel_normals.append({"label": label, "polynomial": polynomial,
                                   "polynomial_sha256": hashlib.sha256(polynomial.encode()).hexdigest()})
    kernel_entries = []
    if certified and kernel_entries_path.exists():
        for line in kernel_entries_path.read_text().splitlines():
            label, term_index, numerator, denominator = line.split("\t", 3)
            kernel_entries.append({"label": label, "term_index": int(term_index),
                                   "numerator": [int(x) for x in numerator.split(",")],
                                   "denominator": [int(x) for x in denominator.split(",")]})
    qtext = "\n".join(quotient_basis)
    mtext = json.dumps(matrix_entries, separators=(",", ":"))
    kntext = json.dumps(kernel_normals, separators=(",", ":"))
    ketext = json.dumps(kernel_entries, separators=(",", ":"))
    valid = (process.returncode == 0 and certified and matrix_profile is not None
             and len(quotient_basis) == 16 and matrix_entries
             and len(kernel_profiles) == len(kernel_normals) == 6 and kernel_entries)
    return {
        **common, "status": "COMPLETE" if valid else "ERROR",
        "quotient_dimension": int(matrix_profile.group(1)) if matrix_profile else None,
        "matrix_count": int(matrix_profile.group(2)) if matrix_profile else None,
        "matrix_nonzero_entry_count": int(matrix_profile.group(3)) if matrix_profile else None,
        "quotient_basis": quotient_basis,
        "quotient_basis_sha256": hashlib.sha256(qtext.encode()).hexdigest(),
        "matrix_entries": matrix_entries,
        "matrix_entries_sha256": hashlib.sha256(mtext.encode()).hexdigest(),
        "kernel_profiles": kernel_profiles, "kernel_normals": kernel_normals,
        "kernel_normals_sha256": hashlib.sha256(kntext.encode()).hexdigest(),
        "kernel_entries": kernel_entries,
        "kernel_entries_sha256": hashlib.sha256(ketext.encode()).hexdigest(),
        "stdout_tail": stdout[-30000:], "stderr_tail": process.stderr[-30000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, complete):
    RESULT.write_text(json.dumps({
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-q5-multiplication-bank-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-q5-multiplication-bank",
        "collection_complete": complete, "field": 2130706433,
        "source_cache_sha256": CACHE_SHA256,
        "source_generic_sha256": GENERIC_SHA256,
        "source_q5_sha256": Q5_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    for path, digest, label in ((CACHE, CACHE_SHA256, "cache"),
                                (GENERIC, GENERIC_SHA256, "generic"),
                                (Q5, Q5_SHA256, "q5")):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                f"{label} custody")
    write_checkpoint(None, False)
    try:
        row = extract_bank.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}; write_checkpoint(row, complete)
    print(json.dumps({"result": str(RESULT), "status": row["status"],
                      "quotient_dimension": row.get("quotient_dimension"),
                      "matrix_count": row.get("matrix_count"),
                      "matrix_nonzero_entry_count": row.get("matrix_nonzero_entry_count"),
                      "kernel_profiles": row.get("kernel_profiles")}, sort_keys=True))
