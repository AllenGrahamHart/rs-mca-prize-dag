#!/usr/bin/env python3
"""Exact section/class resource census for DLI ell=2 weight four."""

from __future__ import annotations

import gzip
import io
import itertools
import json
import math
import subprocess
import time
from pathlib import Path

import modal


ORDER = 1024
HALF = 512
WEIGHT = 4
RAW_COUNT = math.comb(HALF, WEIGHT) * 2 ** (WEIGHT - 1)
SECTION_CONSTRUCTION_UPPER = 9 * math.comb(ORDER - 4, WEIGHT - 2)
OUTPUT = Path(__file__).with_name("dli_wcl_ell2_weight4_resource_result.json.gz")

app = modal.App("rs-mca-dli-wcl-ell2-weight4-resource")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


def valuation_two(value: int) -> int:
    exponent = 0
    while value and value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


def encode(full_terms: tuple[int, ...]) -> int:
    reduced = sorted((term % HALF, 1 if term < HALF else -1) for term in full_terms)
    if len(reduced) != WEIGHT or len({exponent for exponent, _ in reduced}) != WEIGHT:
        raise AssertionError("antipodal collision")
    if reduced[0][1] < 0:
        reduced = [(exponent, -sign) for exponent, sign in reduced]
    key = 0
    for index, (exponent, sign) in enumerate(reduced):
        key |= (exponent | ((sign < 0) << 9)) << (10 * index)
    return key


def decode_full(key: int) -> tuple[int, ...]:
    terms = []
    for index in range(WEIGHT):
        term = (key >> (10 * index)) & 0x3FF
        terms.append((term & 0x1FF) + (HALF if term & 0x200 else 0))
    return tuple(terms)


def normalized_transforms(full: tuple[int, ...]) -> set[int]:
    transformed = set()
    for left in full:
        for right in full:
            if left == right:
                continue
            difference = (right - left) % ORDER
            v2 = valuation_two(difference)
            if v2 >= 9:
                continue
            modulus = 1 << (10 - v2)
            base = pow(difference >> v2, -1, modulus)
            for lift in range(1 << v2):
                dilation = base + lift * modulus
                shift = -dilation * left
                transformed.add(
                    encode(tuple((dilation * term + shift) % ORDER for term in full))
                )
    return transformed


@app.function(image=image, cpu=2, memory=8192, timeout=300)
def enumerate_classes() -> dict[str, object]:
    started = time.monotonic()
    section = set()
    universe = range(ORDER)
    for v2 in range(9):
        pinned = 1 << v2
        forbidden = {0, HALF, pinned, pinned + HALF}
        available = [term for term in universe if term not in forbidden]
        for tail in itertools.combinations(available, WEIGHT - 2):
            full = (0, pinned, *tail)
            if any(
                (left - right) % ORDER == HALF
                for left, right in itertools.combinations(full, 2)
            ):
                continue
            section.add(encode(full))
    if len(section) > SECTION_CONSTRUCTION_UPPER:
        raise AssertionError("section upper bound")

    remaining = set(section)
    representatives = []
    section_orbit_sum = 0
    max_section_orbit = 0
    while remaining:
        key = next(iter(remaining))
        full = decode_full(key)
        orbit = normalized_transforms(full)
        if key not in orbit or not orbit <= section:
            raise AssertionError("normalized orbit escaped section")
        intersection = orbit & remaining
        remaining.difference_update(orbit)
        section_orbit_sum += len(intersection)
        max_section_orbit = max(max_section_orbit, len(orbit))
        representatives.append(
            {
                "key": key,
                "exponents": [term % HALF for term in full],
                "signs": [1 if term < HALF else -1 for term in full],
                "section_orbit_size": len(orbit),
            }
        )
    if section_orbit_sum != len(section):
        raise AssertionError("section partition")
    return {
        "raw_count": RAW_COUNT,
        "section_construction_upper": SECTION_CONSTRUCTION_UPPER,
        "section_count": len(section),
        "class_count": len(representatives),
        "max_section_orbit": max_section_orbit,
        "enumeration_seconds": round(time.monotonic() - started, 6),
        "representatives": representatives,
    }


@app.function(image=image, cpu=1, memory=2048, timeout=120, max_containers=48)
def factor_sample(representative: dict[str, object]) -> dict[str, object]:
    from flint import fmpz_poly

    started = time.monotonic()
    coefficients = [0] * HALF
    for exponent, sign in zip(representative["exponents"], representative["signs"]):
        coefficients[int(exponent)] += int(sign)
    polynomial = fmpz_poly(coefficients)
    cyclotomic = fmpz_poly([1] + [0] * (HALF - 1) + [1])
    norm = abs(int(cyclotomic.resultant(polynomial)))
    if norm == 0:
        raise AssertionError("characteristic-zero vanisher")
    program = (
        f"n={norm};f=factor(n);"
        'for(i=1,matsize(f)[1],print(f[i,1]," : ",f[i,2]));quit()\n'
    )
    completed = subprocess.run(
        ["gp", "-q", "-s", "268435456"],
        input=program,
        text=True,
        capture_output=True,
        timeout=110,
        check=True,
    )
    factors = []
    product = 1
    for line in completed.stdout.splitlines():
        if ":" not in line:
            continue
        prime_text, exponent_text = (part.strip() for part in line.split(":", 1))
        prime = int(prime_text)
        exponent = int(exponent_text)
        factors.append(
            {
                "prime": prime_text,
                "exponent": exponent,
                "bits": prime.bit_length(),
                "v2_prime_minus_1": valuation_two(prime - 1),
            }
        )
        product *= prime**exponent
    if product != norm:
        raise AssertionError("incomplete factorization")
    return {
        **representative,
        "norm": str(norm),
        "norm_bits": norm.bit_length(),
        "factors": factors,
        "ambient_candidates": [
            factor
            for factor in factors
            if int(factor["prime"]) < 2**256 and factor["v2_prime_minus_1"] >= 41
        ],
        "worker_seconds": round(time.monotonic() - started, 6),
    }


def write_result(result: dict[str, object]) -> None:
    with OUTPUT.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as compressed:
            with io.TextIOWrapper(compressed, encoding="utf-8") as handle:
                json.dump(result, handle, indent=2, sort_keys=True)
                handle.write("\n")


def spread_sample(rows: list[dict[str, object]], size: int) -> list[dict[str, object]]:
    if size >= len(rows):
        return rows
    indices = {round(index * (len(rows) - 1) / (size - 1)) for index in range(size)}
    return [rows[index] for index in sorted(indices)]


@app.local_entrypoint()
def main(sample_size: int = 256) -> None:
    result = {
        "schema": "dli-wcl-ell2-weight4-resource-v1",
        "status": "ENUMERATION_IN_PROGRESS",
        "raw_count": RAW_COUNT,
        "section_construction_upper": SECTION_CONSTRUCTION_UPPER,
    }
    write_result(result)
    print(
        "DLI_WCL_ELL2_WEIGHT4_PREFLIGHT "
        f"raw={RAW_COUNT} section_upper={SECTION_CONSTRUCTION_UPPER}",
        flush=True,
    )
    result.update(enumerate_classes.remote())
    sample = spread_sample(result["representatives"], sample_size)
    result.update(
        {
            "status": "SAMPLE_IN_PROGRESS",
            "sample_size": len(sample),
            "sample_keys": [row["key"] for row in sample],
            "sample_completed": [],
            "sample_worker_errors": [],
        }
    )
    write_result(result)
    print(
        "DLI_WCL_ELL2_WEIGHT4_CLASSES "
        f"section={result['section_count']} classes={result['class_count']} "
        f"seconds={result['enumeration_seconds']}",
        flush=True,
    )
    for payload, row in zip(sample, factor_sample.map(sample, return_exceptions=True)):
        if isinstance(row, BaseException):
            result["sample_worker_errors"].append(
                {"key": payload["key"], "error": repr(row)}
            )
        else:
            result["sample_completed"].append(row)
        write_result(result)
    result["status"] = "SAMPLE_COMPLETE" if not result["sample_worker_errors"] else "SAMPLE_PARTIAL"
    result["sample_factor_records"] = sum(
        len(row["factors"]) for row in result["sample_completed"]
    )
    result["sample_candidate_count"] = sum(
        len(row["ambient_candidates"]) for row in result["sample_completed"]
    )
    result["sample_worker_seconds"] = sum(
        row["worker_seconds"] for row in result["sample_completed"]
    )
    write_result(result)
    print(
        "DLI_WCL_ELL2_WEIGHT4_RESOURCE_RESULT "
        f"status={result['status']} completed={len(result['sample_completed'])}/"
        f"{len(sample)} factor_records={result['sample_factor_records']} "
        f"candidates={result['sample_candidate_count']}"
    )
