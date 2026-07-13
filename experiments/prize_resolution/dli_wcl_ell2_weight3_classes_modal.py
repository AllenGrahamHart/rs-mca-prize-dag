#!/usr/bin/env python3
"""Exhaustive order-1024 norm census for the DLI ell=2 weight-3 window."""

from __future__ import annotations

import itertools
import json
import math
import re
import subprocess
from pathlib import Path

import modal


ORDER = 1024
HALF = 512
WEIGHT = 3
RAW_COUNT = math.comb(HALF, WEIGHT) * 2 ** (WEIGHT - 1)
OUTPUT = Path(__file__).with_name("dli_wcl_ell2_weight3_classes_result.json")

app = modal.App("rs-mca-dli-wcl-ell2-weight3-classes")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


def valuation_two(value: int) -> int:
    exponent = 0
    while value and value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


def encode(full_terms: tuple[int, ...] | list[int]) -> int:
    reduced = sorted((term % HALF, 1 if term < HALF else -1) for term in full_terms)
    if len({exponent for exponent, _ in reduced}) != WEIGHT:
        raise AssertionError("antipodal collision")
    if reduced[0][1] < 0:
        reduced = [(exponent, -sign) for exponent, sign in reduced]
    key = 0
    for index, (exponent, sign) in enumerate(reduced):
        key |= (exponent | ((sign < 0) << 9)) << (10 * index)
    return key


def decode(key: int) -> tuple[list[int], list[int]]:
    exponents = []
    signs = []
    for index in range(WEIGHT):
        term = (key >> (10 * index)) & 0x3FF
        exponents.append(term & 0x1FF)
        signs.append(-1 if term & 0x200 else 1)
    return exponents, signs


def full_terms(key: int) -> tuple[int, ...]:
    exponents, signs = decode(key)
    return tuple(
        exponent if sign > 0 else exponent + HALF
        for exponent, sign in zip(exponents, signs)
    )


def normalized_orbit(key: int) -> set[int]:
    terms = full_terms(key)
    orbit = set()
    for dilation in range(1, ORDER, 2):
        dilated = tuple(dilation * term % ORDER for term in terms)
        for anchor in dilated:
            orbit.add(encode(tuple((term - anchor) % ORDER for term in dilated)))
    return orbit


@app.function(image=image, cpu=2, memory=2048, timeout=180)
def enumerate_classes() -> dict[str, object]:
    section: set[int] = set()
    for left, right in itertools.combinations(range(1, ORDER), 2):
        if left == HALF or right == HALF or (right - left) % ORDER == HALF:
            continue
        section.add(encode((0, left, right)))

    seen: set[int] = set()
    representatives = []
    for key in sorted(section):
        if key in seen:
            continue
        orbit = normalized_orbit(key)
        if not orbit <= section:
            raise AssertionError("normalized orbit escaped section")
        if seen & orbit:
            raise AssertionError("normalized orbit overlap")
        seen.update(orbit)
        exponents, signs = decode(key)
        representatives.append({"key": key, "exponents": exponents, "signs": signs})
    if seen != section:
        raise AssertionError("normalized section not covered")
    return {
        "raw_count": RAW_COUNT,
        "section_count": len(section),
        "class_count": len(representatives),
        "representatives": representatives,
    }


def parse_factors(output: str, value: int) -> list[list[object]]:
    if value == 1:
        return []
    factors = []
    for line in output.splitlines():
        match = re.fullmatch(r"\s*(\d+)\s*:\s*(\d+)\s*", line)
        if match:
            factors.append([match.group(1), int(match.group(2))])
    if not factors or math.prod(int(prime) ** exponent for prime, exponent in factors) != value:
        raise AssertionError("incomplete PARI factorization")
    return factors


@app.function(image=image, cpu=1, memory=2048, timeout=120, max_containers=48)
def factor_class(representative: dict[str, object]) -> dict[str, object]:
    from flint import fmpz_poly

    coefficients = [0] * HALF
    for exponent, sign in zip(representative["exponents"], representative["signs"]):
        coefficients[int(exponent)] = int(sign)
    polynomial = fmpz_poly(coefficients)
    cyclotomic = fmpz_poly([1] + [0] * (HALF - 1) + [1])
    norm = abs(int(cyclotomic.resultant(polynomial)))
    if norm == 0:
        raise AssertionError("characteristic-zero weight-3 vanisher")
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
    candidates = []
    for prime_text, exponent in parse_factors(completed.stdout, norm):
        prime = int(prime_text)
        row = {
            "prime": prime_text,
            "exponent": exponent,
            "bits": prime.bit_length(),
            "v2_prime_minus_1": valuation_two(prime - 1),
        }
        factors.append(row)
        if prime < 2**256 and row["v2_prime_minus_1"] >= 41:
            candidates.append(row)
    return {
        **representative,
        "norm": str(norm),
        "norm_bits": norm.bit_length(),
        "factors": factors,
        "ambient_candidates": candidates,
    }


@app.local_entrypoint()
def main(resume: bool = True) -> None:
    if resume and OUTPUT.exists():
        result = json.loads(OUTPUT.read_text())
        if result.get("schema") != "dli-wcl-ell2-weight3-affine-galois-v1":
            raise AssertionError("resume schema mismatch")
        completed_keys = {row["key"] for row in result["completed"]}
        result["worker_errors"] = []
        payloads = [
            row for row in result["representatives"] if row["key"] not in completed_keys
        ]
    else:
        classes = enumerate_classes.remote()
        result = {
            "schema": "dli-wcl-ell2-weight3-affine-galois-v1",
            "status": "FACTORIZATION_IN_PROGRESS",
            **classes,
            "completed": [],
            "worker_errors": [],
        }
        payloads = list(result["representatives"])
    result["status"] = "FACTORIZATION_IN_PROGRESS"
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_ELL2_WEIGHT3_CLASSES "
        f"raw={result['raw_count']} section={result['section_count']} "
        f"classes={result['class_count']}",
        flush=True,
    )
    for payload, row in zip(payloads, factor_class.map(payloads, return_exceptions=True)):
        if isinstance(row, BaseException):
            result["worker_errors"].append({"key": payload["key"], "error": repr(row)})
        else:
            result["completed"].append(row)
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    result["status"] = "COMPLETE" if not result["worker_errors"] else "PARTIAL"
    result["candidate_count"] = sum(
        len(row["ambient_candidates"]) for row in result["completed"]
    )
    result["max_v2_below_cap"] = max(
        (
            factor["v2_prime_minus_1"]
            for row in result["completed"]
            for factor in row["factors"]
            if int(factor["prime"]) < 2**256
        ),
        default=0,
    )
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_ELL2_WEIGHT3_RESULT "
        f"status={result['status']} completed={len(result['completed'])}/"
        f"{result['class_count']} candidates={result['candidate_count']} "
        f"max_v2_below_cap={result['max_v2_below_cap']}"
    )
