#!/usr/bin/env python3
"""Benchmark exact recursive norms on terminal weight-five affine classes."""

from __future__ import annotations

import json
from pathlib import Path

import modal


ORDER = 512
DEGREE = 256
CLASS_COUNT = 2_296_920
REPRESENTATIVE_FILE = "/classes/weight5_affine_representatives.bin"
OUTPUT = Path(__file__).with_name("dli_wcl_weight5_recursive_norm_pilot_result.json")

app = modal.App("rs-mca-dli-wcl-weight5-recursive-norm-pilot")
volume = modal.Volume.from_name("rs-mca-dli-wcl-weight5-affine-classes-v1")
image = modal.Image.debian_slim().pip_install("python-flint").apt_install("pari-gp")


@app.function(
    image=image,
    cpu=1,
    memory=2048,
    timeout=300,
    max_containers=128,
    volumes={"/classes": volume},
)
def factor_representative(payload: tuple[int, int]) -> dict[str, object]:
    import math
    import struct
    import subprocess
    import sys
    import time

    from flint import fmpz_poly

    sys.set_int_max_str_digits(0)
    sample_index, class_index = payload
    with open(REPRESENTATIVE_FILE, "rb") as handle:
        handle.seek(8 * class_index)
        packed = handle.read(8)
    if len(packed) != 8:
        raise AssertionError("representative read")
    key = struct.unpack("<Q", packed)[0]
    terms = tuple((key >> (9 * index)) & 0x1FF for index in range(5))
    if len({term & 0xFF for term in terms}) != 5:
        raise AssertionError("antipodal collision")
    coefficients = [0] * DEGREE
    for term in terms:
        coefficients[term & 0xFF] += -1 if term & 0x100 else 1
    polynomial = fmpz_poly(coefficients)

    def recursive_norm(value: fmpz_poly) -> int:
        width = DEGREE
        current = value
        while width > 1:
            next_width = width // 2
            even = fmpz_poly(
                [int(current[2 * index]) for index in range(next_width)]
            )
            odd = fmpz_poly(
                [int(current[2 * index + 1]) for index in range(next_width)]
            )
            paired = even * even - fmpz_poly([0, 1]) * odd * odd
            row = [int(paired[index]) for index in range(width)]
            for index in range(next_width, width):
                row[index - next_width] -= row[index]
            current = fmpz_poly(row[:next_width])
            width = next_width
        return abs(int(current[0]))

    norm_started = time.monotonic()
    norm = recursive_norm(polynomial)
    norm_seconds = time.monotonic() - norm_started
    if norm == 0:
        raise AssertionError("characteristic-zero vanisher")
    if sample_index < 8:
        cyclotomic = fmpz_poly([1] + [0] * (DEGREE - 1) + [1])
        generic = abs(int(cyclotomic.resultant(polynomial)))
        if generic != norm:
            raise AssertionError("generic norm mismatch")

    factor_started = time.monotonic()
    program = (
        f"n={norm};f=factor(n);"
        'for(i=1,matsize(f)[1],print(f[i,1]," : ",f[i,2]));quit()\n'
    )
    completed = subprocess.run(
        ["gp", "-q", "-s", "536870912"],
        input=program,
        text=True,
        capture_output=True,
        timeout=280,
        check=True,
    )
    factor_seconds = time.monotonic() - factor_started
    factors = []
    product = 1
    for line in completed.stdout.splitlines():
        if ":" not in line:
            continue
        prime_text, exponent_text = (part.strip() for part in line.split(":", 1))
        prime = int(prime_text)
        exponent = int(exponent_text)
        valuation = (prime - 1 & -(prime - 1)).bit_length() - 1
        factors.append(
            {
                "prime": prime_text,
                "exponent": exponent,
                "prime_bits": prime.bit_length(),
                "v2_prime_minus_1": valuation,
            }
        )
        product *= prime**exponent
    if product != norm:
        raise AssertionError("incomplete factorization")
    return {
        "sample_index": sample_index,
        "class_index": class_index,
        "key": key,
        "norm_bits": norm.bit_length(),
        "norm_seconds": round(norm_seconds, 6),
        "factor_seconds": round(factor_seconds, 6),
        "factors": factors,
        "eligible": [
            factor
            for factor in factors
            if int(factor["prime"]) < 2**256
            and int(factor["v2_prime_minus_1"]) >= 41
        ],
        "status": "COMPLETE",
    }


def percentile(values: list[float], numerator: int, denominator: int) -> float:
    if not values:
        return 0.0
    return values[(numerator * (len(values) - 1)) // denominator]


@app.local_entrypoint()
def main(sample_count: int = 2048) -> None:
    indices = sorted(
        {
            index * (CLASS_COUNT - 1) // (sample_count - 1)
            for index in range(sample_count)
        }
    )
    payloads = list(enumerate(indices))
    remote_rows = list(factor_representative.map(payloads, return_exceptions=True))
    rows = []
    errors = []
    for payload, row in zip(payloads, remote_rows):
        if isinstance(row, BaseException):
            errors.append({"sample_index": payload[0], "class_index": payload[1], "error": repr(row)})
        else:
            rows.append(row)
    norm_times = sorted(float(row["norm_seconds"]) for row in rows)
    factor_times = sorted(float(row["factor_seconds"]) for row in rows)
    factors = [factor for row in rows for factor in row["factors"]]
    eligible = [
        {"class_index": row["class_index"], **factor}
        for row in rows
        for factor in row["eligible"]
    ]
    result = {
        "schema": "dli-wcl-weight5-recursive-norm-pilot-v1",
        "scope": "uniform deterministic factor pilot; not an exclusion certificate",
        "status": "COMPLETE" if not errors and len(rows) == len(payloads) else "PARTIAL",
        "class_count": CLASS_COUNT,
        "sample_requested": sample_count,
        "sample_completed": len(rows),
        "errors": errors,
        "generic_norm_controls": min(8, len(rows)),
        "max_norm_bits": max((int(row["norm_bits"]) for row in rows), default=0),
        "max_norm_seconds": max(norm_times, default=0.0),
        "p95_norm_seconds": percentile(norm_times, 95, 100),
        "max_factor_seconds": max(factor_times, default=0.0),
        "p50_factor_seconds": percentile(factor_times, 50, 100),
        "p95_factor_seconds": percentile(factor_times, 95, 100),
        "factor_records": len(factors),
        "distinct_primes": len({factor["prime"] for factor in factors}),
        "max_prime_bits": max((int(factor["prime_bits"]) for factor in factors), default=0),
        "max_v2_prime_minus_1": max(
            (int(factor["v2_prime_minus_1"]) for factor in factors), default=-1
        ),
        "eligible": eligible,
        "rows": rows,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_WEIGHT5_RECURSIVE_NORM_PILOT "
        + json.dumps(
            {
                "status": result["status"],
                "completed": len(rows),
                "errors": len(errors),
                "max_norm_bits": result["max_norm_bits"],
                "p95_norm_seconds": result["p95_norm_seconds"],
                "p50_factor_seconds": result["p50_factor_seconds"],
                "p95_factor_seconds": result["p95_factor_seconds"],
                "max_factor_seconds": result["max_factor_seconds"],
                "distinct_primes": result["distinct_primes"],
                "max_v2": result["max_v2_prime_minus_1"],
                "eligible": len(eligible),
            },
            sort_keys=True,
        )
    )
