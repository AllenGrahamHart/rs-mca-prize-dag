#!/usr/bin/env python3
"""Compute the staged generic q7 coefficient bank with Groebner.jl."""

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
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_coefficients_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_q7_coefficients_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_GENERIC = "/root/generic.json"
REMOTE_PROGRAM = "/root/fff_generic_q7_coefficients_program.py"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
GENERIC_SHA256 = "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-generic-q7-coefficients")
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


@app.function(image=image, cpu=1.0, memory=8192, timeout=420)
def compute_q7_coefficients():
    core = load("fff_generic_q7_coefficients", REMOTE_PROGRAM)
    built = core.build(
        json.loads(Path(REMOTE_CACHE).read_text()),
        json.loads(Path(REMOTE_GENERIC).read_text()),
    )
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jl") as handle:
        handle.write(program); handle.flush()
        try:
            process = subprocess.run(["julia", "--startup-file=no", handle.name],
                                     capture_output=True, text=True, timeout=360)
        except subprocess.TimeoutExpired as error:
            return {**common, "status": "TIMEOUT",
                    "partial_stdout": decoded(error.stdout)[-30000:],
                    "partial_stderr": decoded(error.stderr)[-30000:]}
    stdout = process.stdout
    profiles = [{"label": label, "degree": int(degree), "term_count": int(terms)}
                for label, degree, terms in re.findall(
                    r"(?:^|\n)Q7_VALUE (\S+) (-?\d+) (\d+)", stdout)]
    certified = "Q7_COEFFICIENTS_CERTIFIED" in stdout
    values_path = Path("/tmp/fff_generic_q7_values.txt")
    entries_path = Path("/tmp/fff_generic_q7_entries.txt")
    values = []
    if certified and values_path.exists():
        for line in values_path.read_text().splitlines():
            label, polynomial = line.split("\t", 1)
            values.append({"label": label, "polynomial": polynomial,
                           "polynomial_sha256": hashlib.sha256(polynomial.encode()).hexdigest()})
    entries = []
    if certified and entries_path.exists():
        for line in entries_path.read_text().splitlines():
            label, term_index, numerator, denominator = line.split("\t", 3)
            entries.append({"label": label, "term_index": int(term_index),
                            "numerator": [int(value) for value in numerator.split(",")],
                            "denominator": [int(value) for value in denominator.split(",")]})
    unique_denominators = []
    seen = set()
    for entry in entries:
        key = tuple(entry["denominator"])
        if key not in seen:
            seen.add(key); unique_denominators.append(entry["denominator"])
    values_text = json.dumps(values, separators=(",", ":"))
    entries_text = json.dumps(entries, separators=(",", ":"))
    denominators_text = json.dumps(unique_denominators, separators=(",", ":"))
    valid = (process.returncode == 0 and certified and len(profiles) == 7
             and len(values) == 7 and entries)
    return {
        **common, "status": "COMPLETE" if valid else "ERROR",
        "profiles": profiles, "values": values,
        "values_sha256": hashlib.sha256(values_text.encode()).hexdigest(),
        "coefficient_entries": entries,
        "coefficient_entry_count": len(entries),
        "coefficient_entries_sha256": hashlib.sha256(entries_text.encode()).hexdigest(),
        "unique_denominators": unique_denominators,
        "unique_denominator_count": len(unique_denominators),
        "unique_denominators_sha256": hashlib.sha256(denominators_text.encode()).hexdigest(),
        "stdout_tail": stdout[-30000:], "stderr_tail": process.stderr[-30000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, complete):
    RESULT.write_text(json.dumps({
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-generic-q7-coefficients-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-generic-q7-coefficients",
        "collection_complete": complete, "field": 2130706433,
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
        row = compute_q7_coefficients.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, complete)
    print(json.dumps({"result": str(RESULT), "status": row["status"],
                      "profiles": row.get("profiles"),
                      "unique_denominator_count": row.get("unique_denominator_count")},
                     sort_keys=True))
