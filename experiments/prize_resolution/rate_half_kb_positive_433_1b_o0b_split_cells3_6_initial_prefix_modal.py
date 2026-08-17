#!/usr/bin/env python3
"""Locate the first hard outside-equation prefix for one O0b case."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
CACHE = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
COMPILER = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_initial_prefix_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_BASIS = "/root/basis.json"
REMOTE_COMPILER = "/root/rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
CASE = (3, "S0", -1, -1, -1, 2, 0)
PREFIX_COUNTS = (1, 2, 3, 4, 5)

app = modal.App("rs-mca-positive-433-1b-o0b-cells3-6-initial-prefix")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(CACHE, REMOTE_CACHE)
    .add_local_file(BASIS, REMOTE_BASIS)
    .add_local_file(COMPILER, REMOTE_COMPILER)
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_compiler(path):
    spec = importlib.util.spec_from_file_location("cached_outside_core", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def decoded(value):
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value or ""


@app.function(image=image, cpu=1.0, memory=4096, timeout=230, max_containers=5)
def compute_prefix(prefix_count):
    compiler = load_compiler(REMOTE_COMPILER)
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    basis_payload = json.loads(Path(REMOTE_BASIS).read_text())
    packet_row = next(
        row for row in cache["rows"] if row["epsilon"] == list(CASE[3:5])
    )
    basis_row = next(
        row for row in basis_payload["rows"] if row["epsilon"] == list(CASE[3:5])
    )
    require(packet_row["status"] == "COMPLETE", "packet status")
    require(basis_row["status"] == "COMPLETE", "basis status")
    compiled = compiler.compile_case(CASE, packet_row["packet"])
    outside_equations = compiled["equations"][3:]
    require(prefix_count in PREFIX_COUNTS, "prefix domain")
    require(len(outside_equations) == 5, "outside-equation ledger")
    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(basis_row["basis"])
    )
    # Definitions 0..2 are replaced by the saturated common basis.
    case_definitions = compiled["definitions"][3:]
    generators = (
        *(f"g{index}" for index in range(len(basis_row["basis"]))),
        *outside_equations[:prefix_count],
    )
    program = f"""
ring R={PRIME},({','.join(compiled['variables'])}),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(case_definitions)}
ideal I={','.join(generators)};
ideal G=slimgb(I);
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
print("BASIS_BEGIN"); G; print("BASIS_END"); print("END"); quit;
"""
    common = {
        "prefix_count": prefix_count,
        "outside_equations": list(outside_equations[:prefix_count]),
        "common_basis_size": len(basis_row["basis"]),
        "packet_sha256": packet_row["packet_sha256"],
        "source_basis_sha256": basis_row["basis_sha256"],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=180,
        )
    except subprocess.TimeoutExpired as error:
        return {
            **common,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout)[-30000:],
            "partial_stderr": decoded(error.stderr)[-1000:],
        }
    stdout = process.stdout
    dimension_match = re.search(r"(?:^|\n)DIM=(-?\d+)", stdout)
    size_match = re.search(r"(?:^|\n)SIZE=(\d+)", stdout)
    basis_match = re.search(r"BASIS_BEGIN\n(.*?)\nBASIS_END", stdout, re.DOTALL)
    basis = []
    if basis_match:
        basis = [
            "".join(value.split())
            for value in re.findall(
                r"G\[\d+\]=(.*?)(?=^G\[\d+\]=|\Z)",
                basis_match.group(1), re.MULTILINE | re.DOTALL,
            )
        ]
    valid = (
        process.returncode == 0 and "END" in stdout and "?" not in stdout
        and dimension_match is not None and size_match is not None
        and len(basis) == int(size_match.group(1))
    )
    encoded = json.dumps(basis, separators=(",", ":"))
    return {
        **common,
        "status": "COMPLETE" if valid else "ERROR",
        "dimension": int(dimension_match.group(1)) if dimension_match else None,
        "basis_size": int(size_match.group(1)) if size_match else None,
        "basis": basis,
        "basis_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
    }


def write_checkpoint(rows, errors, collection_complete):
    ordered = sorted(rows, key=lambda row: row["prefix_count"])
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-cells3-6-initial-prefix-v1",
        "app": "rs-mca-positive-433-1b-o0b-cells3-6-initial-prefix",
        "collection_complete": collection_complete,
        "field": PRIME,
        "case": list(CASE),
        "prefix_counts": list(PREFIX_COUNTS),
        "source_cache_sha256": CACHE_SHA256,
        "source_global_basis_sha256": BASIS_SHA256,
        "source_compiler_sha256": COMPILER_SHA256,
        "expected_row_count": len(PREFIX_COUNTS),
        "processed_row_count": len(ordered),
        "remote_errors": errors,
        "rows": ordered,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
            "compiler custody")
    rows = []
    errors = []
    write_checkpoint(rows, errors, collection_complete=False)
    remote_rows = compute_prefix.map(
        PREFIX_COUNTS, order_outputs=False, return_exceptions=True
    )
    for row in remote_rows:
        if isinstance(row, BaseException):
            errors.append(repr(row))
        else:
            rows.append(row)
        complete = len(rows) == len(PREFIX_COUNTS) and not errors
        write_checkpoint(rows, errors, collection_complete=complete)
    complete = len(rows) == len(PREFIX_COUNTS) and not errors
    write_checkpoint(rows, errors, collection_complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "collection_complete": complete,
        "processed": len(rows),
        "remote_errors": len(errors),
        "statuses": {
            row["prefix_count"]: row["status"] for row in sorted(
                rows, key=lambda value: value["prefix_count"]
            )
        },
    }, sort_keys=True))
