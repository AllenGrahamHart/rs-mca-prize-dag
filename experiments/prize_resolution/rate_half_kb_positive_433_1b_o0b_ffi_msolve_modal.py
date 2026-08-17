#!/usr/bin/env python3
"""Run one exact O0b FFI boundary ideal with msolve F4."""

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
BASIS = DIRECTORY / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
COMPILER = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
INPUT_CORE = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_ffi_msolve_input.py"
SMOKE = DIRECTORY / "msolve_prime_field_smoke_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_o0b_ffi_msolve_result.json"
REMOTE_CACHE = "/root/cache.json"
REMOTE_BASIS = "/root/basis.json"
REMOTE_COMPILER = "/root/cached_outside_core.py"
REMOTE_INPUT_CORE = "/root/ffi_msolve_input.py"
PRIME = 2130706433
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"
SMOKE_SHA256 = "4bf0791c422e83438b65c2c871119eee0a7124be1e2a6d508185ce7a13e11d70"
CASE = (3, "S0", -1, -1, -1, 2, 0)
CHART_MASK = ("finite", "finite", "infinity")

app = modal.App("rs-mca-positive-433-1b-o0b-ffi-msolve")
image = (
    modal.Image.from_registry("debian:trixie-slim", add_python="3.12")
    .apt_install("msolve", "singular")
    .add_local_file(CACHE, REMOTE_CACHE)
    .add_local_file(BASIS, REMOTE_BASIS)
    .add_local_file(COMPILER, REMOTE_COMPILER)
    .add_local_file(INPUT_CORE, REMOTE_INPUT_CORE)
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


def unit_output(text):
    return bool(re.search(
        r"#length of basis:\s+1 element\s+#---\s+\[\s*1\s*\]:\s*$",
        text, re.DOTALL,
    ))


def smoke_test(root):
    source = root / "smoke.ms"
    output = root / "smoke.out"
    source.write_text(f"x\n{PRIME}\nx,\nx-1\n")
    process = subprocess.run(
        ["msolve", "-t", "1", "-g", "2", "-f", str(source),
         "-o", str(output)],
        capture_output=True, text=True, timeout=30,
    )
    text = output.read_text() if output.exists() else ""
    require(process.returncode == 0 and process.stderr == "" and unit_output(text),
            "msolve unit smoke")
    return text


@app.function(image=image, cpu=1.0, memory=8192, timeout=330)
def decide_chart():
    compiler = load("cached_outside_core", REMOTE_COMPILER)
    input_core = load("ffi_msolve_input", REMOTE_INPUT_CORE)
    cache = json.loads(Path(REMOTE_CACHE).read_text())
    basis_payload = json.loads(Path(REMOTE_BASIS).read_text())
    packet_row = next(
        row for row in cache["rows"] if row["epsilon"] == [-1, -1]
    )
    basis_row = next(
        row for row in basis_payload["rows"] if row["epsilon"] == [-1, -1]
    )
    built = input_core.build(packet_row, basis_row, compiler)
    exporter_program = built.pop("exporter_program")
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        version = subprocess.run(
            ["msolve", "-V"], capture_output=True, text=True, timeout=10
        )
        smoke_output = smoke_test(root)
        exporter = subprocess.run(
            ["Singular", "--quiet"], input=exporter_program,
            capture_output=True, text=True, timeout=30,
        )
        matches = re.findall(
            r"POLY_BEGIN=(\d+)\n(.*?)\nPOLY_END=\1",
            exporter.stdout, re.DOTALL,
        )
        polynomials = ["".join(value.split()) for _, value in matches]
        require(exporter.returncode == 0 and exporter.stderr == "" and
                "?" not in exporter.stdout and
                [int(index) for index, _ in matches] ==
                list(range(built["generator_count"])),
                "Singular explicit export")
        require(all("*" in value or value in {"0", "1"} or
                    re.fullmatch(r"-?\d+|[A-Za-z]\w*", value)
                    for value in polynomials), "explicit polynomial notation")
        msolve_input = (
            ",".join(built["variables"]) + "\n" + str(PRIME) + "\n" +
            ",\n".join(polynomials) + "\n"
        )
        source = root / "ffi.ms"
        output_path = root / "ffi.out"
        source.write_text(msolve_input)
        common = {
            **built,
            "case": list(CASE),
            "chart_mask": list(CHART_MASK),
            "msolve_version": version.stdout.strip(),
            "msolve_smoke_output": smoke_output,
            "exporter_program_sha256": hashlib.sha256(
                exporter_program.encode()
            ).hexdigest(),
            "exporter_stdout_sha256": hashlib.sha256(
                exporter.stdout.encode()
            ).hexdigest(),
            "msolve_input_sha256": hashlib.sha256(
                msolve_input.encode()
            ).hexdigest(),
            "msolve_input": msolve_input,
            "explicit_polynomial_count": len(polynomials),
        }
        command = [
            "msolve", "-t", "1", "-g", "2", "-v", "1",
            "-f", str(source), "-o", str(output_path),
        ]
        try:
            process = subprocess.run(
                command, capture_output=True, text=True, timeout=240,
            )
        except subprocess.TimeoutExpired as error:
            partial_output = output_path.read_text() if output_path.exists() else ""
            return {
                **common,
                "status": "TIMEOUT",
                "partial_stdout": decoded(error.stdout)[-30000:],
                "partial_stderr": decoded(error.stderr)[-30000:],
                "partial_output": partial_output[-30000:],
                "partial_output_sha256": hashlib.sha256(
                    partial_output.encode()
                ).hexdigest(),
            }
        output = output_path.read_text() if output_path.exists() else ""
        valid = (
            process.returncode == 0 and process.stderr == "" and
            output.startswith("#Reduced Groebner basis data")
        )
        unit = unit_output(output)
        return {
            **common,
            "status": "COMPLETE" if valid else "ERROR",
            "unit": unit,
            "stdout": process.stdout[-30000:],
            "stderr": process.stderr[-30000:],
            "output": output if len(output) <= 2_000_000 else output[-2_000_000:],
            "output_bytes": len(output.encode()),
            "output_sha256": hashlib.sha256(output.encode()).hexdigest(),
        }


def write_checkpoint(row, collection_complete):
    payload = {
        "schema": "rate-half-kb-positive-433-1b-o0b-ffi-msolve-v1",
        "app": "rs-mca-positive-433-1b-o0b-ffi-msolve",
        "collection_complete": collection_complete,
        "field": PRIME,
        "case": list(CASE),
        "chart_mask": list(CHART_MASK),
        "source_cache_sha256": CACHE_SHA256,
        "source_basis_sha256": BASIS_SHA256,
        "source_compiler_sha256": COMPILER_SHA256,
        "source_input_core_sha256": hashlib.sha256(INPUT_CORE.read_bytes()).hexdigest(),
        "source_smoke_sha256": SMOKE_SHA256,
        "row": row,
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
    require(hashlib.sha256(SMOKE.read_bytes()).hexdigest() == SMOKE_SHA256,
            "smoke custody")
    write_checkpoint(None, collection_complete=False)
    try:
        row = decide_chart.remote()
    except BaseException as error:
        row = {"status": "REMOTE_ERROR", "error": repr(error)}
    complete = row["status"] in {"COMPLETE", "TIMEOUT"}
    write_checkpoint(row, collection_complete=complete)
    print(json.dumps({
        "result": str(RESULT),
        "collection_complete": complete,
        "status": row["status"],
        "unit": row.get("unit"),
        "msolve_version": row.get("msolve_version"),
        "input_bytes": len(row.get("msolve_input", "").encode()),
        "output_bytes": row.get("output_bytes"),
    }, sort_keys=True))
