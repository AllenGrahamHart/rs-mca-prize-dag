#!/usr/bin/env python3
"""Test the O0b q3 -> q7 -> q5 equation ordering."""

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
SOURCE = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_single_extensions_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_q7_q5_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_COMPILER = "/root/rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
REMOTE_SOURCE = "/root/single_extensions.json"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
SOURCE_SHA256 = "ce0396a9f6d951270a5ec3ba9b8371919020dcac75ca11af488d9fabc5e0edb9"
SOURCE_BASIS_SHA256 = "679c448e3587f4bb11f39a6742aa7439d9b909ad68cf19834ca463d634c5aceb"
CASE = (3, "S0", -1, -1, -1, 2, 0)

app = modal.App("rs-mca-positive-433-1b-o0b-cells3-6-q7-q5")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(CACHE, REMOTE_CACHE)
    .add_local_file(COMPILER, REMOTE_COMPILER)
    .add_local_file(SOURCE, REMOTE_SOURCE)
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


@app.function(image=image, cpu=1.0, memory=4096, timeout=300)
def extend_q7_by_q5():
    compiler = load_compiler(REMOTE_COMPILER)
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    source_payload = json.loads(Path(REMOTE_SOURCE).read_text())
    packet_row = next(
        row for row in cache["rows"] if row["epsilon"] == list(CASE[3:5])
    )
    source_row = next(
        row for row in source_payload["rows"] if row["equation_name"] == "q7"
    )
    require(packet_row["status"] == "COMPLETE", "packet status")
    require(source_row["status"] == "COMPLETE", "source status")
    require(source_row["basis_sha256"] == SOURCE_BASIS_SHA256 and
            source_row["basis_size"] == 128 and source_row["dimension"] == 3,
            "source basis ledger")
    compiled = compiler.compile_case(CASE, packet_row["packet"])
    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(source_row["basis"])
    )
    case_definitions = compiled["definitions"][3:]
    program = f"""
ring R={PRIME},({','.join(compiled['variables'])}),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(case_definitions)}
ideal G={','.join(f'g{index}' for index in range(len(source_row['basis'])))};
attrib(G,"isSB",1);
poly nf=reduce(q5,G);
print("NF_DEG="+string(deg(nf))); print("NF_TERMS="+string(size(nf)));
ideal I=G; I[size(I)+1]=nf;
ideal H=slimgb(I);
print("BEGIN"); print("DIM="+string(dim(H))); print("SIZE="+string(size(H)));
print("BASIS_BEGIN"); H; print("BASIS_END"); print("END"); quit;
"""
    common = {
        "source_equations": ["q3", "q7"],
        "added_equation": "q5",
        "source_basis_size": len(source_row["basis"]),
        "source_basis_sha256": source_row["basis_sha256"],
        "packet_sha256": packet_row["packet_sha256"],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "standard_basis_attribute_set": True,
    }
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=240,
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
        and "not a standard basis" not in stdout
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


def write_checkpoint(row, collection_complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-cells3-6-q7-q5-v1",
        "app": "rs-mca-positive-433-1b-o0b-cells3-6-q7-q5",
        "collection_complete": collection_complete,
        "field": PRIME,
        "case": list(CASE),
        "source_cache_sha256": CACHE_SHA256,
        "source_compiler_sha256": COMPILER_SHA256,
        "source_single_extensions_sha256": SOURCE_SHA256,
        "row": row,
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
            "compiler custody")
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "source custody")
    write_checkpoint(None, collection_complete=False)
    try:
        row = extend_q7_by_q5.remote()
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
    }, sort_keys=True))
