#!/usr/bin/env python3
"""Normalized-section compiler for terminal DLI weight four.

Every reduced signed weight-4 polynomial is a four-set in Z/512 with no
antipodal pair, modulo translation, odd dilation, and global translation by
256.  Given two non-antipodal terms x,y, write v=v_2(y-x)<=7.  An odd
dilation and translation send that ordered pair to (0,2^v).  Hence every
affine orbit meets the much smaller normalized section consisting of supports
that contain one of (0,1),(0,2),...,(0,128).

The Modal compiler constructs this section exactly and removes one complete
normalized orbit at a time.  A deterministic spread sample then computes and
factors exact cyclotomic norms, providing a resource estimate before any full
factor sweep.  The local entrypoint writes enumeration before sampling and
updates after each worker result.
"""

from __future__ import annotations

import itertools
import gzip
import io
import json
import math
import subprocess
import time
from pathlib import Path

import modal


ORDER = 512
HALF = 256
WEIGHT = 4
RAW_COUNT = math.comb(HALF, WEIGHT) * 2 ** (WEIGHT - 1)
OUTPUT = Path(__file__).with_name("dli_wcl_weight4_section_result.json.gz")

app = modal.App("rs-mca-dli-wcl-weight4-section")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


def valuation_two(value: int) -> int:
    exponent = 0
    while value and value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


def encode(full_terms: tuple[int, ...] | list[int]) -> int:
    reduced = sorted((term % HALF, 1 if term < HALF else -1) for term in full_terms)
    if len(reduced) != WEIGHT or len({exponent for exponent, _ in reduced}) != WEIGHT:
        raise AssertionError("antipodal collision")
    if reduced[0][1] < 0:
        reduced = [(exponent, -sign) for exponent, sign in reduced]
    key = 0
    for index, (exponent, sign) in enumerate(reduced):
        key |= (exponent | ((sign < 0) << 8)) << (9 * index)
    return key


def decode_full(key: int) -> tuple[int, ...]:
    terms = []
    for index in range(WEIGHT):
        term = (key >> (9 * index)) & 0x1FF
        terms.append((term & 0xFF) + (HALF if term & 0x100 else 0))
    return tuple(terms)


def normalized_transforms(full: tuple[int, ...]) -> set[int]:
    transformed: set[int] = set()
    for left in full:
        for right in full:
            if left == right:
                continue
            difference = (right - left) % ORDER
            v2 = valuation_two(difference)
            if v2 >= 8:
                continue
            modulus = 1 << (9 - v2)
            odd_part = difference >> v2
            base = pow(odd_part, -1, modulus)
            for lift in range(1 << v2):
                dilation = base + lift * modulus
                shift = -dilation * left
                image_terms = tuple((dilation * term + shift) % ORDER for term in full)
                transformed.add(encode(image_terms))
    return transformed


@app.function(image=image, cpu=2, memory=4096, timeout=300)
def enumerate_classes() -> dict[str, object]:
    started = time.monotonic()
    section: set[int] = set()
    universe = range(ORDER)
    for v2 in range(8):
        pinned = 1 << v2
        forbidden = {0, HALF, pinned, pinned + HALF}
        available = [term for term in universe if term not in forbidden]
        for tail in itertools.combinations(available, WEIGHT - 2):
            full = (0, pinned, *tail)
            if any((left - right) % ORDER == HALF for left, right in itertools.combinations(full, 2)):
                continue
            section.add(encode(full))

    section_count = len(section)
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
        exponents = []
        signs = []
        for term in full:
            exponents.append(term % HALF)
            signs.append(1 if term < HALF else -1)
        representatives.append(
            {"key": key, "exponents": exponents, "signs": signs, "section_orbit_size": len(orbit)}
        )
    if section_orbit_sum != section_count:
        raise AssertionError("section partition")
    return {
        "raw_count": RAW_COUNT,
        "section_count": section_count,
        "class_count": len(representatives),
        "max_section_orbit": max_section_orbit,
        "enumeration_seconds": round(time.monotonic() - started, 6),
        "representatives": representatives,
    }


@app.function(image=image, cpu=1, memory=1536, timeout=90, max_containers=96)
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
        timeout=80,
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
        raise AssertionError(
            f"incomplete factorization norm={norm} product={product} "
            f"stdout={completed.stdout!r} stderr={completed.stderr!r}"
        )
    return {
        **representative,
        "norm": str(norm),
        "norm_bits": norm.bit_length(),
        "factors": factors,
        "eligible": [
            factor
            for factor in factors
            if int(factor["prime"]) < 2**256 and factor["v2_prime_minus_1"] >= 41
        ],
        "worker_seconds": round(time.monotonic() - started, 6),
    }


def spread_sample(rows: list[dict[str, object]], size: int) -> list[dict[str, object]]:
    if size >= len(rows):
        return rows
    indices = {round(index * (len(rows) - 1) / (size - 1)) for index in range(size)}
    return [rows[index] for index in sorted(indices)]


def write_result(result: dict[str, object]) -> None:
    with OUTPUT.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as compressed:
            with io.TextIOWrapper(compressed, encoding="utf-8") as handle:
                json.dump(result, handle, indent=2, sort_keys=True)
                handle.write("\n")


@app.local_entrypoint()
def main(sample_size: int = 512, full: bool = False, resume: bool = True) -> None:
    if full:
        if not resume or not OUTPUT.exists():
            raise AssertionError("run the section sample before the full sweep")
        with gzip.open(OUTPUT, "rt", encoding="utf-8") as handle:
            result = json.load(handle)
        if result.get("schema") != "dli-wcl-weight4-normalized-section-v1":
            raise AssertionError("resume schema mismatch")
        completed = result.setdefault("full_completed", list(result.get("sample_completed", [])))
        completed_keys = {row["key"] for row in completed}
        result["full_worker_errors"] = []
        result["status"] = "FULL_FACTORIZATION_IN_PROGRESS"
        payloads = [row for row in result["representatives"] if row["key"] not in completed_keys]
        write_result(result)
        print(
            "DLI_WCL_WEIGHT4_FULL_START "
            f"completed={len(completed)}/{result['class_count']} remaining={len(payloads)}",
            flush=True,
        )
        for index, (payload, row) in enumerate(
            zip(payloads, factor_sample.map(payloads, return_exceptions=True)), start=1
        ):
            if isinstance(row, BaseException):
                result["full_worker_errors"].append({"key": payload["key"], "error": repr(row)})
            else:
                completed.append(row)
            if index % 25 == 0 or index == len(payloads):
                write_result(result)
        result["status"] = "FULL_COMPLETE" if not result["full_worker_errors"] else "FULL_PARTIAL"
        result["full_candidate_count"] = sum(len(row["eligible"]) for row in completed)
        result["full_max_v2_below_cap"] = max(
            (
                factor["v2_prime_minus_1"]
                for row in completed
                for factor in row["factors"]
                if int(factor["prime"]) < 2**256
            ),
            default=0,
        )
        write_result(result)
        print(
            "DLI_WCL_WEIGHT4_FULL_RESULT "
            f"status={result['status']} completed={len(completed)}/{result['class_count']} "
            f"errors={len(result['full_worker_errors'])} "
            f"eligible={result['full_candidate_count']} "
            f"max_v2={result['full_max_v2_below_cap']}"
        )
        return

    classes = enumerate_classes.remote()
    result = {
        "schema": "dli-wcl-weight4-normalized-section-v1",
        "status": "SAMPLE_IN_PROGRESS",
        **classes,
        "sample_requested": sample_size,
        "sample_completed": [],
        "worker_errors": [],
    }
    write_result(result)
    print(
        "DLI_WCL_WEIGHT4_SECTION "
        f"raw={result['raw_count']} section={result['section_count']} "
        f"classes={result['class_count']} seconds={result['enumeration_seconds']}",
        flush=True,
    )
    payloads = spread_sample(result["representatives"], sample_size)
    for payload, row in zip(payloads, factor_sample.map(payloads, return_exceptions=True)):
        if isinstance(row, BaseException):
            result["worker_errors"].append({"key": payload["key"], "error": repr(row)})
        else:
            result["sample_completed"].append(row)
        write_result(result)
    result["status"] = "SAMPLE_COMPLETE" if not result["worker_errors"] else "SAMPLE_PARTIAL"
    result["eligible_count"] = sum(len(row["eligible"]) for row in result["sample_completed"])
    result["max_v2_below_cap"] = max(
        (
            factor["v2_prime_minus_1"]
            for row in result["sample_completed"]
            for factor in row["factors"]
            if int(factor["prime"]) < 2**256
        ),
        default=0,
    )
    write_result(result)
    print(
        "DLI_WCL_WEIGHT4_SAMPLE "
        f"status={result['status']} completed={len(result['sample_completed'])}/{len(payloads)} "
        f"eligible={result['eligible_count']} max_v2={result['max_v2_below_cap']}"
    )
