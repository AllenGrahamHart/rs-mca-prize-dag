#!/usr/bin/env python3
"""Run one O0b cells-3/6 outside diagnostic from the global common basis."""

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
CORE = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_diagnostic_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_BASIS = "/root/basis.json"
REMOTE_CORE = "/root/rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
CASE = (3, "S0", -1, -1, -1, 0, 0)

app = modal.App("rs-mca-positive-433-1b-o0b-cells3-6-basis-diagnostic")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("singular")
    .add_local_file(CACHE, REMOTE_CACHE)
    .add_local_file(BASIS, REMOTE_BASIS)
    .add_local_file(CORE, REMOTE_CORE)
)


def load_core(path):
    spec = importlib.util.spec_from_file_location("cached_outside_core", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def case_key(case):
    cell, lane, sigma_o, epsilon_1, epsilon_2, xi_index, pairing_index = case
    return {
        "cell": cell,
        "lane": lane,
        "sigma_o": sigma_o,
        "epsilon": [epsilon_1, epsilon_2],
        "xi_index": xi_index,
        "pairing_index": pairing_index,
    }


@app.function(image=image, cpu=1.0, memory=4096, timeout=300)
def decide_case(case):
    core = load_core(REMOTE_CORE)
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    basis_payload = json.loads(Path(REMOTE_BASIS).read_text())
    packet_row = next(
        row for row in cache["rows"] if row["epsilon"] == list(case[3:5])
    )
    basis_row = next(
        row for row in basis_payload["rows"] if row["epsilon"] == list(case[3:5])
    )
    if packet_row["status"] != "COMPLETE" or basis_row["status"] != "COMPLETE":
        raise RuntimeError("source row status")
    compiled = core.compile_case(case, packet_row["packet"])
    # Drop q0,q1,q2: the 21-polynomial common basis replaces them.
    case_definitions = compiled["definitions"][3:]
    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(basis_row["basis"])
    )
    outside_equations = compiled["equations"][3:]
    guard_definitions = tuple(
        f"poly h{index}={value};"
        for index, value in enumerate(compiled["guards"])
    )
    cofactor_definitions = tuple(
        f"poly c{index}={value};"
        for index, value in enumerate(compiled["rank_cofactors"])
    )
    saturation_stages = "\n".join(
        f"ideal H{index}=h{index}; "
        f"list S{index}=sat(G,H{index}); G=S{index}[1]; G=slimgb(G); "
        f'print("SAT={index},DIM="+string(dim(G))+",SIZE="+string(size(G)));'
        for index in range(len(compiled["guards"]))
    )
    initial_generators = (
        *(f"g{index}" for index in range(len(basis_row["basis"]))),
        *outside_equations,
    )
    program = f"""
LIB "elim.lib";
ring R={PRIME},({','.join(compiled['variables'])}),dp;
option(redSB);
{chr(10).join(basis_definitions)}
{chr(10).join(case_definitions)}
{chr(10).join(guard_definitions)}
{chr(10).join(cofactor_definitions)}
ideal I={','.join(initial_generators)};
ideal G=slimgb(I);
print("INITIAL_DIM="+string(dim(G))+",INITIAL_SIZE="+string(size(G)));
{saturation_stages}
ideal C={','.join(f'c{index}' for index in range(6))};
list SC=sat(G,C); G=SC[1]; G=slimgb(G);
print("COFACTOR_DIM="+string(dim(G))+",COFACTOR_SIZE="+string(size(G)));
print("BEGIN"); print("DIM="+string(dim(G))); print("SIZE="+string(size(G)));
if ((size(G)==1) && (G[1]==1)) {{ print("UNIT=1"); }}
else {{ print("UNIT=0"); G; }}
print("END"); quit;
"""
    key = case_key(case)
    try:
        process = subprocess.run(
            ["Singular", "--quiet"], input=program, capture_output=True,
            text=True, timeout=240,
        )
    except subprocess.TimeoutExpired as error:
        def decoded(value):
            if isinstance(value, bytes):
                return value.decode("utf-8", errors="replace")
            return value or ""

        return {
            **key,
            "status": "TIMEOUT",
            "partial_stdout": decoded(error.stdout)[-30000:],
            "partial_stderr": decoded(error.stderr)[-1000:],
            "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
            "packet_sha256": packet_row["packet_sha256"],
            "basis_sha256": basis_row["basis_sha256"],
        }
    stdout = process.stdout
    dimensions = re.findall(r"(?:^|\n)DIM=(-?\d+)", stdout)
    basis_sizes = re.findall(r"(?:^|\n)SIZE=(\d+)", stdout)
    valid = process.returncode == 0 and "END" in stdout and "?" not in stdout
    unit = "UNIT=1" in stdout
    return {
        **key,
        "status": "COMPLETE" if valid else "ERROR",
        "unit": unit,
        "dimension": int(dimensions[-1]) if dimensions else None,
        "basis_size": int(basis_sizes[-1]) if basis_sizes else None,
        "common_basis_size": len(basis_row["basis"]),
        "outside_equation_count": len(outside_equations),
        "guard_count": len(compiled["guards"]),
        "rank_cofactor_count": len(compiled["rank_cofactors"]),
        "stdout": stdout[-30000:],
        "stderr": process.stderr[-1000:],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "packet_sha256": packet_row["packet_sha256"],
        "basis_sha256": basis_row["basis_sha256"],
        "input_program": "" if unit else program,
    }


def write_checkpoint(row, complete):
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-split-cells3-6-basis-diagnostic-v1",
        "app": "rs-mca-positive-433-1b-o0b-cells3-6-basis-diagnostic",
        "complete": complete,
        "field": PRIME,
        "source_cache_sha256": CACHE_SHA256,
        "source_basis_sha256": BASIS_SHA256,
        "source_core_sha256": hashlib.sha256(CORE.read_bytes()).hexdigest(),
        "case": list(CASE),
        "row": row,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")


@app.local_entrypoint()
def main():
    if hashlib.sha256(CACHE.read_bytes()).hexdigest() != CACHE_SHA256:
        raise RuntimeError("cache custody")
    if hashlib.sha256(BASIS.read_bytes()).hexdigest() != BASIS_SHA256:
        raise RuntimeError("basis custody")
    write_checkpoint(None, complete=False)
    try:
        row = decide_case.remote(CASE)
    except BaseException as error:
        row = {**case_key(CASE), "status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] == "COMPLETE"
    write_checkpoint(row, complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "complete": complete,
        "status": row["status"],
        "unit": row.get("unit"),
        "dimension": row.get("dimension"),
        "basis_size": row.get("basis_size"),
        "partial_stdout": row.get("partial_stdout"),
    }, sort_keys=True))
