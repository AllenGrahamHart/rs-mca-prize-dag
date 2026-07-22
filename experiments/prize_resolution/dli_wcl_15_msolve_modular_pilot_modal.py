#!/usr/bin/env python3
"""Capped msolve/F4 pilot for the WCL (ell,w)=(1,5) quotient ideal.

The container regenerates the five exponent-256 remainder polynomials over
F_32003 with FLINT, checks their term counts and content hashes, subtracts one
from the constant coefficient, and gives msolve at most four minutes. A unit
result is modular route evidence only; it is not an integer Nullstellensatz
certificate or a WCL closure.
"""

from __future__ import annotations

import hashlib
import json
import os
import signal
import subprocess
import time
from pathlib import Path

import modal


APP_NAME = "dli-wcl-15-msolve-modular-pilot"
MODULUS = 32_003
ALGEBRA_TIMEOUT = 210
EXPECTED_COUNTS = (183_162, 191_699, 189_670, 186_887, 185_330)
EXPECTED_HASHES = (
    "735baaf4c765bff2da760560913dcbd11fcc51ea63c6a2bec7f44012d07f5c06",
    "43ebc8299aae2b3341bfbd80d2b64a07e652e73b128f1ab7d116eac85710f737",
    "c79d7ba146912df590481d1e3499e16103cb9b83edeec418c950f7c3c95caa9c",
    "3e49b3a1355076a893c0283316fdea45feda7309b995307a0d32614d703ec856",
    "0bd441cbfeeb88815458883143021c2ce8b6ed0b767951959e7af5974aeb7e03",
)

app = modal.App(APP_NAME)
image = (
    modal.Image.from_registry("python:3.12-slim-trixie")
    .run_commands(
        "printf 'deb http://deb.debian.org/debian unstable main\\n' "
        "> /etc/apt/sources.list.d/unstable.list",
        "apt-get update && apt-get install -y -t unstable msolve time",
    )
    .pip_install("python-flint==0.9.0")
)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def tail(path: Path, limit: int = 8_000) -> str:
    if not path.exists():
        return ""
    with path.open("rb") as handle:
        handle.seek(0, os.SEEK_END)
        size = handle.tell()
        handle.seek(max(0, size - limit))
        return handle.read().decode("utf-8", errors="replace")


def quotient_polynomials():
    from flint import nmod_mpoly_ctx

    ctx = nmod_mpoly_ctx.get(("c0", "c1", "b"), MODULUS, "degrevlex")
    c0, c1, b = ctx.gens()
    divisor = [
        ctx.constant(MODULUS - 1),
        c0**2 - 2 * b,
        2 * c0 * c1 - b**2,
        c1**2 + 2 * c0,
        2 * c1,
    ]
    zero = ctx.constant(0)
    remainder = [zero, ctx.constant(1), zero, zero, zero]

    for stage in range(1, 9):
        raw = [ctx.constant(0) for _ in range(9)]
        for left in range(5):
            for right in range(left, 5):
                product = remainder[left] * remainder[right]
                raw[left + right] += product if left == right else 2 * product
        for degree in range(8, 4, -1):
            leading = raw[degree]
            if leading.is_zero():
                continue
            shift = degree - 5
            for index in range(5):
                raw[shift + index] -= leading * divisor[index]
        remainder = raw[:5]
        print(
            "WCL15_MSOLVE_EXPANSION "
            + json.dumps(
                {
                    "stage": stage,
                    "exponent": 1 << stage,
                    "terms": [sum(1 for _ in poly.terms()) for poly in remainder],
                },
                sort_keys=True,
            ),
            flush=True,
        )
    return ctx, remainder


def content_fingerprint(poly) -> tuple[int, str]:
    digest = hashlib.sha256()
    count = 0
    for exponents, coefficient in poly.terms():
        line = "\t".join(map(str, (*exponents, int(coefficient)))) + "\n"
        digest.update(line.encode("ascii"))
        count += 1
    return count, digest.hexdigest()


def write_msolve_polynomial(handle, poly) -> None:
    names = ("c0", "c1", "b")
    first = True
    for exponents, raw_coefficient in poly.terms():
        coefficient = int(raw_coefficient) % MODULUS
        if coefficient == 0:
            continue
        factors = []
        for name, exponent in zip(names, exponents):
            if exponent == 1:
                factors.append(name)
            elif exponent > 1:
                factors.append(f"{name}^{exponent}")
        if factors:
            monomial = "*".join(factors)
            term = monomial if coefficient == 1 else f"{coefficient}*{monomial}"
        else:
            term = str(coefficient)
        if not first:
            handle.write("+")
        handle.write(term)
        first = False
    if first:
        handle.write("0")


@app.function(
    image=image,
    cpu=8.0,
    memory=32_768,
    timeout=300,
    max_containers=1,
)
def pilot() -> dict[str, object]:
    began = time.monotonic()
    version = subprocess.run(
        ["msolve", "-V"], text=True, capture_output=True, check=False
    )
    print("WCL15_MSOLVE_VERSION " + (version.stdout + version.stderr).strip(), flush=True)

    ctx, polynomials = quotient_polynomials()
    fingerprints = [content_fingerprint(poly) for poly in polynomials]
    counts = tuple(item[0] for item in fingerprints)
    hashes = tuple(item[1] for item in fingerprints)
    if counts != EXPECTED_COUNTS or hashes != EXPECTED_HASHES:
        raise RuntimeError(f"FLINT endpoint mismatch: counts={counts} hashes={hashes}")

    # The pinned hashes describe Y^256 mod G. The unit ideal is generated by
    # the coefficients of Y^256-1 mod G.
    polynomials[0] -= ctx.constant(1)
    work = Path("/tmp/wcl15-msolve")
    work.mkdir(parents=True, exist_ok=True)
    input_path = work / "wcl15.in"
    output_path = work / "wcl15.out"
    stdout_path = work / "msolve.stdout"
    stderr_path = work / "msolve.stderr"
    timing_path = work / "msolve.time"
    with input_path.open("w", encoding="ascii", newline="\n") as handle:
        handle.write("c0,c1,b\n")
        handle.write(f"{MODULUS}\n")
        for index, poly in enumerate(polynomials):
            write_msolve_polynomial(handle, poly)
            handle.write("\n" if index == len(polynomials) - 1 else ",\n")

    input_summary = {
        "input_bytes": input_path.stat().st_size,
        "input_sha256": file_sha256(input_path),
        "term_counts": counts,
        "content_hashes": hashes,
        "preparation_seconds": time.monotonic() - began,
    }
    print("WCL15_MSOLVE_INPUT " + json.dumps(input_summary, sort_keys=True), flush=True)

    command = [
        "/usr/bin/time", "-v", "-o", str(timing_path),
        "msolve", "-f", str(input_path), "-o", str(output_path),
        "-t", "8", "-v", "2", "-g", "2",
    ]
    algebra_began = time.monotonic()
    with stdout_path.open("wb") as stdout_handle, stderr_path.open("wb") as stderr_handle:
        process = subprocess.Popen(
            command,
            stdout=stdout_handle,
            stderr=stderr_handle,
            start_new_session=True,
        )
        next_checkpoint = 30
        timed_out = False
        while process.poll() is None:
            elapsed = time.monotonic() - algebra_began
            if elapsed >= next_checkpoint:
                print(
                    "WCL15_MSOLVE_CHECKPOINT "
                    + json.dumps({"elapsed": elapsed, "pid": process.pid}, sort_keys=True),
                    flush=True,
                )
                next_checkpoint += 30
            if elapsed >= ALGEBRA_TIMEOUT:
                timed_out = True
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                break
            time.sleep(2)

    output_text = output_path.read_text(encoding="utf-8", errors="replace") if output_path.exists() else ""
    unit = output_text.strip() == "[-1]" if not timed_out and process.returncode == 0 else None
    result = {
        "app": APP_NAME,
        "status": "TIMEOUT" if timed_out else ("COMPLETE" if process.returncode == 0 else "ERROR"),
        "modulus": MODULUS,
        "msolve_version": (version.stdout + version.stderr).strip(),
        "command": command,
        "returncode": process.returncode,
        "unit_ideal_mod_p": unit,
        "algebra_seconds": time.monotonic() - algebra_began,
        "total_seconds": time.monotonic() - began,
        "input": input_summary,
        "output_bytes": output_path.stat().st_size if output_path.exists() else 0,
        "output_sha256": file_sha256(output_path) if output_path.exists() else None,
        "output_head": output_text[:2_000],
        "output_tail": output_text[-4_000:],
        "stdout_tail": tail(stdout_path),
        "stderr_tail": tail(stderr_path),
        "timing": timing_path.read_text(encoding="utf-8", errors="replace") if timing_path.exists() else "",
        "nonclaim": "modular route pilot only; no characteristic-zero or WCL conclusion",
    }
    print("WCL15_MSOLVE_RESULT " + json.dumps(result, sort_keys=True), flush=True)
    return result


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(pilot.remote(), indent=2, sort_keys=True))
