#!/usr/bin/env python3
"""Extend one retained O0b q3 basis by q4, q5, q6, or q7."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

import modal


DIRECTORY = Path(__file__).parent
CACHE = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
COMPILER = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
PREFIX = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_initial_prefix_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_single_extensions_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_COMPILER = "/root/rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
REMOTE_PREFIX = "/root/prefix.json"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
PREFIX_SHA256 = "486c36b63335f0b30aa17008481df341869f5d37b32456d58fc40438deb7daa6"
CASE = (3, "S0", -1, -1, -1, 2, 0)
EQUATION_INDICES = (4, 5, 6, 7)

app = modal.App("rs-mca-positive-433-1b-o0b-cells3-6-single-extensions")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(CACHE, REMOTE_CACHE)
    .add_local_file(COMPILER, REMOTE_COMPILER)
    .add_local_file(PREFIX, REMOTE_PREFIX)
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


def marker(pattern, text):
    match = re.search(pattern, text)
    return int(match.group(1)) if match else None


@app.function(image=image, cpu=1.0, memory=4096, timeout=230, max_containers=4)
def extend(equation_index):
    require(equation_index in EQUATION_INDICES, "equation-index domain")
    compiler = load_compiler(REMOTE_COMPILER)
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    prefix_payload = json.loads(Path(REMOTE_PREFIX).read_text())
    packet_row = next(
        row for row in cache["rows"] if row["epsilon"] == list(CASE[3:5])
    )
    prefix_row = next(
        row for row in prefix_payload["rows"] if row["prefix_count"] == 1
    )
    require(packet_row["status"] == "COMPLETE", "packet status")
    require(prefix_row["status"] == "COMPLETE", "prefix status")
    require(prefix_row["dimension"] == 3 and prefix_row["basis_size"] == 51,
            "prefix ledger")
    compiled = compiler.compile_case(CASE, packet_row["packet"])
    require(compiled["equations"][3:] == ("q3", "q4", "q5", "q6", "q7"),
            "outside-equation order")
    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(prefix_row["basis"])
    )
    case_definitions = compiled["definitions"][3:]
    program = f"""
ring R={PRIME},({','.join(compiled['variables'])}),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(case_definitions)}
ideal G={','.join(f'g{index}' for index in range(len(prefix_row['basis'])))};
poly nf=reduce(q{equation_index},G);
print("NF_DEG="+string(deg(nf))); print("NF_TERMS="+string(size(nf)));
ideal I=G; I[size(I)+1]=nf;
ideal H=slimgb(I);
print("BEGIN"); print("DIM="+string(dim(H))); print("SIZE="+string(size(H)));
print("BASIS_BEGIN"); H; print("BASIS_END"); print("END"); quit;
"""
    common = {
        "equation_index": equation_index,
        "equation_name": f"q{equation_index}",
        "source_prefix_count": 1,
        "source_prefix_basis_size": len(prefix_row["basis"]),
        "source_prefix_basis_sha256": prefix_row["basis_sha256"],
        "packet_sha256": packet_row["packet_sha256"],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=180,
        )
    except subprocess.TimeoutExpired as error:
        partial_stdout = decoded(error.stdout)[-30000:]
        return {
            **common,
            "status": "TIMEOUT",
            "normal_form_degree": marker(r"(?:^|\n)NF_DEG=(-?\d+)", partial_stdout),
            "normal_form_terms": marker(r"(?:^|\n)NF_TERMS=(\d+)", partial_stdout),
            "partial_stdout": partial_stdout,
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
                r"H\[\d+\]=(.*?)(?=^H\[\d+\]=|\Z)",
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
        "normal_form_degree": marker(r"(?:^|\n)NF_DEG=(-?\d+)", stdout),
        "normal_form_terms": marker(r"(?:^|\n)NF_TERMS=(\d+)", stdout),
        "dimension": int(dimension_match.group(1)) if dimension_match else None,
        "basis_size": int(size_match.group(1)) if size_match else None,
        "basis": basis,
        "basis_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
    }


def write_checkpoint(rows, errors, collection_complete):
    ordered = sorted(rows, key=lambda row: row["equation_index"])
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-cells3-6-single-extensions-v1",
        "app": "rs-mca-positive-433-1b-o0b-cells3-6-single-extensions",
        "collection_complete": collection_complete,
        "field": PRIME,
        "case": list(CASE),
        "equation_indices": list(EQUATION_INDICES),
        "source_cache_sha256": CACHE_SHA256,
        "source_compiler_sha256": COMPILER_SHA256,
        "source_prefix_sha256": PREFIX_SHA256,
        "expected_row_count": len(EQUATION_INDICES),
        "processed_row_count": len(ordered),
        "remote_errors": errors,
        "rows": ordered,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
            "compiler custody")
    require(hashlib.sha256(PREFIX.read_bytes()).hexdigest() == PREFIX_SHA256,
            "prefix custody")
    rows = []
    errors = []
    write_checkpoint(rows, errors, collection_complete=False)
    remote_rows = extend.map(
        EQUATION_INDICES, order_outputs=False, return_exceptions=True
    )
    for row in remote_rows:
        if isinstance(row, BaseException):
            errors.append(repr(row))
        else:
            rows.append(row)
        complete = len(rows) == len(EQUATION_INDICES) and not errors
        write_checkpoint(rows, errors, collection_complete=complete)
    complete = len(rows) == len(EQUATION_INDICES) and not errors
    write_checkpoint(rows, errors, collection_complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "collection_complete": complete,
        "processed": len(rows),
        "remote_errors": len(errors),
        "statuses": {
            row["equation_name"]: row["status"] for row in sorted(
                rows, key=lambda value: value["equation_index"]
            )
        },
    }, sort_keys=True))
