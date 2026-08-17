#!/usr/bin/env python3
"""Compute the incremental generic q5 extension with Groebner.jl."""

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
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_julia_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q5_julia_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_GENERIC = "/root/generic.json"
REMOTE_PROGRAM = "/root/fff_generic_q5_program.py"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
GENERIC_SHA256 = "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-generic-q5-julia")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; "
        'Pkg.add(["AbstractAlgebra", "Groebner"]); Pkg.precompile()\''
    )
    .add_local_file(CACHE, REMOTE_CACHE)
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


@app.function(image=image, cpu=1.0, memory=8192, timeout=360)
def compute_q5():
    core = load("fff_generic_q5", REMOTE_PROGRAM)
    built = core.build(
        json.loads(Path(REMOTE_CACHE).read_text()),
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
                capture_output=True, text=True, timeout=300,
            )
        except subprocess.TimeoutExpired as error:
            return {
                **common,
                "status": "TIMEOUT",
                "partial_stdout": decoded(error.stdout)[-30000:],
                "partial_stderr": decoded(error.stderr)[-30000:],
            }
    stdout = process.stdout
    normal_profile = re.search(r"(?:^|\n)Q5_NORMAL (-?\d+) (\d+)", stdout)
    profile = re.search(r"(?:^|\n)Q5_COMPLETE ([01]) (-?\d+) (\d+) (\d+)", stdout)
    certified = "Q5_CERTIFIED" in stdout
    normal_path = Path("/tmp/fff_generic_q5_normal.txt")
    basis_path = Path("/tmp/fff_generic_q5_basis.txt")
    coefficient_path = Path("/tmp/fff_generic_q5_coefficients.txt")
    normal = normal_path.read_text().strip() if certified and normal_path.exists() else ""
    basis = basis_path.read_text().splitlines() if certified and basis_path.exists() else []
    entries = []
    if certified and coefficient_path.exists():
        for line in coefficient_path.read_text().splitlines():
            kind, value_index, term_index, numerator, denominator = line.split("\t", 4)
            entries.append({
                "kind": kind,
                "value_index": int(value_index),
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
    basis_text = "\n".join(basis)
    entries_text = json.dumps(entries, separators=(",", ":"))
    denominators_text = json.dumps(unique_denominators, separators=(",", ":"))
    valid = (
        process.returncode == 0 and certified and normal_profile is not None
        and profile is not None and normal and len(basis) == int(profile.group(3))
        and entries
    )
    return {
        **common,
        "status": "COMPLETE" if valid else "ERROR",
        "normal_degree": int(normal_profile.group(1)) if normal_profile else None,
        "normal_term_count": int(normal_profile.group(2)) if normal_profile else None,
        "normal": normal,
        "normal_sha256": hashlib.sha256(normal.encode()).hexdigest(),
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
        "stdout_tail": stdout[-30000:],
        "stderr_tail": process.stderr[-30000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, collection_complete):
    RESULT.write_text(json.dumps({
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-generic-q5-julia-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-generic-q5-julia",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_cache_sha256": CACHE_SHA256,
        "source_generic_sha256": GENERIC_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(GENERIC.read_bytes()).hexdigest() == GENERIC_SHA256,
            "generic custody")
    write_checkpoint(None, False)
    try:
        row = compute_q5.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, complete)
    print(json.dumps({
        "result": str(RESULT),
        "status": row["status"],
        "normal_degree": row.get("normal_degree"),
        "normal_term_count": row.get("normal_term_count"),
        "unit": row.get("unit"),
        "dimension": row.get("dimension"),
        "basis_size": row.get("basis_size"),
        "quotient_dimension": row.get("quotient_dimension"),
        "unique_denominator_count": row.get("unique_denominator_count"),
    }, sort_keys=True))
