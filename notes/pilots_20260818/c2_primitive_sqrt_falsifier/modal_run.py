#!/usr/bin/env python3
"""Parallel Modal launcher for the preregistered exact t=2 grid."""

from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction
import json
import math
from pathlib import Path
import subprocess
import time

import modal


HERE = Path(__file__).resolve().parent
ROWS = [
    (32, 97),
    (32, 5857),
    (64, 193),
    (64, 257),
    (64, 449),
    (64, 577),
    (64, 769),
    (64, 1153),
    (128, 257),
    (128, 641),
    (128, 769),
    (128, 1153),
    (256, 769),
]

app = modal.App("rs-mca-c2-primitive-sqrt-falsifier")
image = modal.Image.debian_slim().apt_install("g++", "libboost-dev").add_local_file(
    str(HERE / "exact_t2.cpp"), "/root/exact_t2.cpp"
)


def log2_ratio_text(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "-Infinity"
    with localcontext() as context:
        context.prec = 80
        value = (Decimal(numerator).ln() - Decimal(denominator).ln()) / Decimal(2).ln()
        return f"{value:.40E}"


@app.function(image=image, cpu=4.0, memory=4096, timeout=300, max_containers=20)
def exact_row(row: tuple[int, int]) -> dict[str, object]:
    n, q = row
    started = time.monotonic()
    try:
        subprocess.run(
            ["g++", "-O3", "-fopenmp", "-std=c++17", "/root/exact_t2.cpp", "-o", "/tmp/exact_t2"],
            check=True,
            capture_output=True,
            text=True,
            timeout=45,
        )
        process = subprocess.run(
            ["/tmp/exact_t2", str(n), str(q)],
            check=True,
            capture_output=True,
            text=True,
            timeout=240,
        )
        values = dict(line.split("=", 1) for line in process.stdout.splitlines())
        numerator = int(values["numerator"])
        denominator = int(values["denominator"])
        ratio = Fraction(numerator, denominator)
        return {
            "status": "PASS",
            "n": n,
            "q": q,
            "z0": values["z0"],
            "c1": values["c1"],
            "z1": values["z1"],
            "b0": values["b0"],
            "primitive": values["primitive"],
            "ratio_numerator": str(ratio.numerator),
            "ratio_denominator": str(ratio.denominator),
            "ratio_bits": log2_ratio_text(ratio.numerator, ratio.denominator),
            "sqrt_bound_bits": 0.5 * math.log2(2 * n),
            "fires": values["fires"] == "1",
            "seconds": time.monotonic() - started,
        }
    except subprocess.TimeoutExpired as error:
        return {
            "status": "TIMEOUT",
            "n": n,
            "q": q,
            "stage": str(error.cmd[0]),
            "seconds": time.monotonic() - started,
        }
    except Exception as error:
        return {
            "status": "ERROR",
            "n": n,
            "q": q,
            "error": repr(error),
            "seconds": time.monotonic() - started,
        }


@app.local_entrypoint()
def main(output: str = str(HERE / "results.json")) -> None:
    destination = Path(output)
    results = []
    for result in exact_row.map(ROWS, order_outputs=False):
        results.append(result)
        payload = {
            "schema": "c2-primitive-sqrt-falsifier-v1",
            "rows_requested": len(ROWS),
            "rows_returned": len(results),
            "results": sorted(results, key=lambda row: (row["n"], row["q"])),
        }
        destination.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        print(json.dumps(result, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
