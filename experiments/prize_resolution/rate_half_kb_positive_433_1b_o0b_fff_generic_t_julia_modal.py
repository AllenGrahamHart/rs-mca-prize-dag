#!/usr/bin/env python3
"""Compile and certify the generic-t FFF graph with Groebner.jl."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile

import modal


DIRECTORY = Path(__file__).parent
GRAPH = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_admissible_ratio_graph_result.json"
PROGRAM = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_program.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json"
REMOTE_GRAPH = "/root/graph.json"
REMOTE_PROGRAM = "/root/fff_generic_t_julia_program.py"
PRIME = 2130706433
GRAPH_SHA256 = "5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1"

app = modal.App("rs-mca-positive-433-1b-o0b-fff-generic-t-julia")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; "
        'Pkg.add(["AbstractAlgebra", "Groebner"]); Pkg.precompile()\''
    )
    .add_local_file(GRAPH, REMOTE_GRAPH)
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


@app.function(image=image, cpu=1.0, memory=4096, timeout=300)
def compile_basis():
    core = load("fff_generic_t_julia_program", REMOTE_PROGRAM)
    graph = json.loads(Path(REMOTE_GRAPH).read_text())
    built = core.build(graph)
    program = built.pop("program")
    common = {**built, "program_sha256": hashlib.sha256(program.encode()).hexdigest()}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jl") as handle:
        handle.write(program)
        handle.flush()
        try:
            process = subprocess.run(
                ["julia", "--startup-file=no", handle.name],
                capture_output=True, text=True, timeout=240,
            )
        except subprocess.TimeoutExpired as error:
            return {
                **common,
                "status": "TIMEOUT",
                "partial_stdout": decoded(error.stdout)[-30000:],
                "partial_stderr": decoded(error.stderr)[-30000:],
            }
    stdout = process.stdout
    profile = re.search(r"(?:^|\n)GENERIC_COMPLETE (-?\d+) (\d+) (\d+)", stdout)
    certified = "GENERIC_CERTIFIED" in stdout
    basis_path = Path("/tmp/fff_generic_t_basis.txt")
    coefficient_path = Path("/tmp/fff_generic_t_coefficients.txt")
    basis = basis_path.read_text().splitlines() if certified and basis_path.exists() else []
    entries = []
    if certified and coefficient_path.exists():
        for line in coefficient_path.read_text().splitlines():
            basis_index, term_index, numerator, denominator = line.split("\t", 3)
            entries.append({
                "basis_index": int(basis_index),
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
        process.returncode == 0 and certified and profile is not None
        and len(basis) == int(profile.group(2)) and entries
        and all(entry["numerator"] and entry["denominator"] for entry in entries)
    )
    return {
        **common,
        "status": "COMPLETE" if valid else "ERROR",
        "dimension": int(profile.group(1)) if profile else None,
        "basis_size": int(profile.group(2)) if profile else None,
        "quotient_dimension": int(profile.group(3)) if profile else None,
        "basis": basis,
        "basis_sha256": hashlib.sha256(basis_text.encode()).hexdigest(),
        "coefficient_entries": entries,
        "coefficient_entry_count": len(entries),
        "coefficient_entries_sha256":
            hashlib.sha256(entries_text.encode()).hexdigest(),
        "unique_denominators": unique_denominators,
        "unique_denominator_count": len(unique_denominators),
        "unique_denominators_sha256":
            hashlib.sha256(denominators_text.encode()).hexdigest(),
        "stdout_tail": stdout[-30000:],
        "stderr_tail": process.stderr[-30000:],
        "input_program": "" if valid else program,
    }


def write_checkpoint(row, collection_complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-fff-generic-t-julia-v1",
        "app": "rs-mca-positive-433-1b-o0b-fff-generic-t-julia",
        "collection_complete": collection_complete,
        "field": PRIME,
        "source_graph_sha256": GRAPH_SHA256,
        "source_program_sha256": hashlib.sha256(PROGRAM.read_bytes()).hexdigest(),
        "row": row,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(GRAPH.read_bytes()).hexdigest() == GRAPH_SHA256,
            "graph custody")
    write_checkpoint(None, collection_complete=False)
    try:
        row = compile_basis.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, collection_complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "collection_complete": complete,
        "status": row["status"],
        "dimension": row.get("dimension"),
        "basis_size": row.get("basis_size"),
        "quotient_dimension": row.get("quotient_dimension"),
        "coefficient_entry_count": row.get("coefficient_entry_count"),
        "unique_denominator_count": row.get("unique_denominator_count"),
    }, sort_keys=True))
