#!/usr/bin/env python3
"""Bounded independent factor probes for the sole WCL (1,5) hard tail."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


NORM = int(
    "648504938724625892617537595827566622528651020454874372151735040370465231483079169"
)
OUTPUT = Path(__file__).with_name("tail191_ecm_result.json")
app = modal.App("rs-mca-wcl15-tail191-ecm")
image = (
    modal.Image.debian_slim()
    .apt_install("gmp-ecm", "pari-gp")
    .pip_install("python-flint")
)


def text(value: str | bytes | None) -> str:
    if value is None:
        return ""
    return value.decode(errors="replace") if isinstance(value, bytes) else value


@app.function(image=image, cpu=1, memory=2048, timeout=330, max_containers=10)
def probe(strategy: dict[str, int | str]) -> dict[str, object]:
    import re
    import subprocess
    import time

    started = time.monotonic()
    kind = str(strategy["kind"])
    if kind == "ecm":
        command = [
            "ecm",
            "-q",
            "-sigma",
            str(strategy["sigma"]),
            "-c",
            str(strategy["curves"]),
            str(strategy["b1"]),
        ]
        stdin = f"{NORM}\n"
    elif kind == "pari":
        command = ["gp", "-q", "-s", "1073741824"]
        stdin = (
            f"n={NORM};print(\"PRIME:\",isprime(n));f=factor(n);"
            "for(j=1,matsize(f)[1],print(\"F:\",f[j,1],\":\",f[j,2]));quit()\n"
        )
    elif kind == "flint":
        command = ["python3", "-c", f"from flint import fmpz; print(fmpz({NORM}).factor())"]
        stdin = ""
    else:
        raise AssertionError(kind)

    timed_out = False
    return_code = None
    try:
        completed = subprocess.run(
            command,
            input=stdin,
            text=True,
            capture_output=True,
            timeout=300,
            check=False,
        )
        stdout, stderr = completed.stdout, completed.stderr
        return_code = completed.returncode
    except subprocess.TimeoutExpired as error:
        timed_out = True
        stdout, stderr = text(error.stdout), text(error.stderr)

    candidates = set()
    for token in re.findall(r"\d+", stdout + "\n" + stderr):
        value = int(token)
        if 1 < value < NORM and NORM % value == 0:
            candidates.add(value)
            candidates.add(NORM // value)

    completion = []
    if candidates:
        smallest = min(candidates)
        remaining = max(5, min(60, int(325 - (time.monotonic() - started))))
        program = (
            f"n={smallest};m={NORM // smallest};"
            "forstep(i=1,2,1,x=if(i==1,n,m);f=factor(x);"
            "for(j=1,matsize(f)[1],print(\"C:\",f[j,1],\":\",f[j,2],\":\",isprime(f[j,1]))));quit()\n"
        )
        try:
            checked = subprocess.run(
                ["gp", "-q", "-s", "1073741824"],
                input=program,
                text=True,
                capture_output=True,
                timeout=remaining,
                check=False,
            )
            for prime, exponent, primality in re.findall(
                r"C:(\d+):(\d+):(\d+)", checked.stdout
            ):
                completion.append([prime, int(exponent), int(primality)])
        except subprocess.TimeoutExpired:
            pass

    return {
        "strategy": strategy,
        "timed_out": timed_out,
        "return_code": return_code,
        "divisors": [str(value) for value in sorted(candidates)],
        "completion": completion,
        "stdout_tail": stdout[-4000:],
        "stderr_tail": stderr[-4000:],
        "seconds": round(time.monotonic() - started, 6),
    }


@app.local_entrypoint()
def main() -> None:
    strategies = [
        {"kind": "ecm", "b1": 100_000, "curves": 100_000, "sigma": 2026080601 + i}
        for i in range(4)
    ]
    strategies += [
        {"kind": "ecm", "b1": 1_000_000, "curves": 10_000, "sigma": 2026080611 + i}
        for i in range(3)
    ]
    strategies += [
        {"kind": "ecm", "b1": 5_000_000, "curves": 1_000, "sigma": 2026080621},
        {"kind": "pari", "seed": 2026080631},
        {"kind": "flint", "seed": 2026080641},
    ]
    rows = list(probe.map(strategies, order_outputs=False, return_exceptions=True))
    results = []
    errors = []
    for row in rows:
        if isinstance(row, BaseException):
            errors.append(repr(row))
        else:
            results.append(row)
    divisors = sorted(
        {int(value) for row in results for value in row["divisors"]}
    )
    payload = {
        "schema": "wcl15-tail191-ecm-v1",
        "norm": str(NORM),
        "norm_bits": NORM.bit_length(),
        "status": "FACTOR_FOUND" if divisors else "NO_FACTOR_WITHIN_CAP",
        "strategies": strategies,
        "results": results,
        "client_errors": errors,
        "divisors": [str(value) for value in divisors],
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        "WCL15_TAIL191_ECM "
        + json.dumps(
            {
                "status": payload["status"],
                "workers": len(results),
                "errors": len(errors),
                "timeouts": sum(int(row["timed_out"]) for row in results),
                "divisors": len(divisors),
            },
            sort_keys=True,
        )
    )
