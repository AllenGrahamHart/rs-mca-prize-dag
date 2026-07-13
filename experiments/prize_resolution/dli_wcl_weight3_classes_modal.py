#!/usr/bin/env python3
"""Complete affine-Galois norm sweep for terminal DLI weight three.

A reduced signed weight-3 polynomial at order 512 is encoded as a three-set
in Z/512 with no antipodal pair: a negative coefficient at exponent ``e`` is
the positive monomial ``z^(e+256)``.  Signed shifts and odd Galois dilations
act by

    s -> a*s+b mod 512,  a odd.

They preserve the absolute cyclotomic norm.  The first Modal stage exhausts
all ``C(256,3)*4`` reduced signed polynomials modulo this action.  Independent
workers then compute and completely factor one exact FLINT resultant per
class.  Any prime factor below ``2^256`` with ``v_2(q-1)>=41`` is an immediate
official-tower WCL falsifier at the terminal ``ell=1`` block.

The local entrypoint writes the class list before launching factor workers and
updates the result after every completed worker, preserving partial progress.
"""

from __future__ import annotations

import itertools
import json
import math
import re
import subprocess
from pathlib import Path

import modal


ORDER = 512
HALF = 256
WEIGHT = 3
RAW_COUNT = math.comb(HALF, WEIGHT) * 2 ** (WEIGHT - 1)
OUTPUT = Path(__file__).with_name("dli_wcl_weight3_classes_result.json")

app = modal.App("rs-mca-dli-wcl-weight3-classes")
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
        key |= (exponent | ((sign < 0) << 8)) << (9 * index)
    return key


def decode(key: int) -> tuple[list[int], list[int]]:
    exponents = []
    signs = []
    for index in range(WEIGHT):
        term = (key >> (9 * index)) & 0x1FF
        exponents.append(term & 0xFF)
        signs.append(-1 if term & 0x100 else 1)
    return exponents, signs


@app.function(image=image, cpu=2, memory=4096, timeout=180)
def enumerate_classes() -> dict[str, object]:
    seen: set[int] = set()
    representatives: list[int] = []
    odds = range(1, ORDER, 2)

    for support in itertools.combinations(range(HALF), WEIGHT):
        for tail_signs in itertools.product((1, -1), repeat=WEIGHT - 1):
            signs = (1,) + tail_signs
            full = tuple(
                exponent if sign > 0 else exponent + HALF
                for exponent, sign in zip(support, signs)
            )
            key = encode(full)
            if key in seen:
                continue
            representatives.append(key)
            for dilation in odds:
                dilated = tuple(dilation * term % ORDER for term in full)
                for shift in range(ORDER):
                    seen.add(encode(tuple((term + shift) % ORDER for term in dilated)))

    if len(seen) != RAW_COUNT:
        raise AssertionError((len(seen), RAW_COUNT))
    decoded = []
    for key in representatives:
        exponents, signs = decode(key)
        decoded.append({"key": key, "exponents": exponents, "signs": signs})
    return {
        "raw_count": RAW_COUNT,
        "class_count": len(decoded),
        "representatives": decoded,
    }


def parse_factors(output: str, value: int) -> list[list[object]]:
    if value == 1:
        return []
    factors = []
    for line in output.splitlines():
        match = re.fullmatch(r"\s*(\d+)\s*:\s*(\d+)\s*", line)
        if match:
            factors.append([match.group(1), int(match.group(2))])
    product = 1
    for prime, exponent in factors:
        product *= int(prime) ** exponent
    if not factors or product != value:
        raise AssertionError("incomplete PARI factorization")
    return factors


@app.function(image=image, cpu=1, memory=1536, timeout=90, max_containers=48)
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
        ["gp", "-q"],
        input=program,
        text=True,
        capture_output=True,
        timeout=80,
        check=True,
    )
    factors = parse_factors(completed.stdout, norm)
    records = []
    official_candidates = []
    for prime_text, exponent in factors:
        prime = int(prime_text)
        record = {
            "prime": prime_text,
            "exponent": exponent,
            "bits": prime.bit_length(),
            "v2_prime_minus_1": valuation_two(prime - 1),
        }
        records.append(record)
        if prime < 2**256 and record["v2_prime_minus_1"] >= 41:
            official_candidates.append(record)
    return {
        "key": representative["key"],
        "exponents": representative["exponents"],
        "signs": representative["signs"],
        "norm": str(norm),
        "norm_bits": norm.bit_length(),
        "factors": records,
        "official_candidates": official_candidates,
    }


@app.function(image=image, cpu=2, memory=2048, timeout=300)
def certify_factors(prime_texts: list[str]) -> dict[str, object]:
    nodes: dict[str, dict[str, object]] = {}

    def factor(value: int) -> list[list[object]]:
        program = (
            f"n={value};f=factor(n);"
            'for(i=1,matsize(f)[1],print(f[i,1]," : ",f[i,2]));quit()\n'
        )
        completed = subprocess.run(
            ["gp", "-q"],
            input=program,
            text=True,
            capture_output=True,
            timeout=80,
            check=True,
        )
        return parse_factors(completed.stdout, value)

    def certify(candidate: int) -> None:
        key = str(candidate)
        if key in nodes:
            return
        if candidate < 10_000:
            if candidate < 2 or any(candidate % d == 0 for d in range(2, math.isqrt(candidate) + 1)):
                raise AssertionError(f"nonprime leaf {candidate}")
            nodes[key] = {"method": "trial"}
            return
        factors = factor(candidate - 1)
        for factor_text, _ in factors:
            certify(int(factor_text))
        witnesses = {}
        for factor_text, _ in factors:
            divisor = int(factor_text)
            for base in range(2, 100_000):
                if (
                    pow(base, candidate - 1, candidate) == 1
                    and math.gcd(pow(base, (candidate - 1) // divisor, candidate) - 1, candidate) == 1
                ):
                    witnesses[factor_text] = base
                    break
            else:
                raise AssertionError((candidate, divisor, "no witness"))
        nodes[key] = {
            "method": "pocklington",
            "minus_one_factors": factors,
            "witnesses": witnesses,
        }

    for prime_text in prime_texts:
        certify(int(prime_text))
    return {"roots": prime_texts, "nodes": nodes}


@app.local_entrypoint()
def main(resume: bool = True) -> None:
    if resume and OUTPUT.exists():
        result = json.loads(OUTPUT.read_text())
        if result.get("schema") != "dli-wcl-weight3-affine-galois-v1":
            raise AssertionError("resume schema mismatch")
        completed_keys = {row["key"] for row in result["completed"]}
        result["worker_errors"] = []
        result["status"] = "FACTORIZATION_IN_PROGRESS"
        payloads = [
            row for row in result["representatives"] if row["key"] not in completed_keys
        ]
    else:
        classes = enumerate_classes.remote()
        result = {
            "schema": "dli-wcl-weight3-affine-galois-v1",
            "status": "FACTORIZATION_IN_PROGRESS",
            **classes,
            "completed": [],
            "worker_errors": [],
        }
        payloads = list(result["representatives"])
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_WEIGHT3_CLASSES "
        f"raw={result['raw_count']} classes={result['class_count']}",
        flush=True,
    )

    if payloads:
        for payload, row in zip(
            payloads,
            factor_class.map(payloads, return_exceptions=True),
        ):
            if isinstance(row, BaseException):
                result["worker_errors"].append({"key": payload["key"], "error": repr(row)})
            else:
                result["completed"].append(row)
            OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    result["status"] = "COMPLETE" if not result["worker_errors"] else "PARTIAL"
    result["candidate_count"] = sum(
        len(row["official_candidates"]) for row in result["completed"]
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
    if not result["worker_errors"]:
        distinct_primes = sorted(
            {
                factor["prime"]
                for row in result["completed"]
                for factor in row["factors"]
            },
            key=int,
        )
        result["factor_pocklington"] = certify_factors.remote(distinct_primes)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_WEIGHT3_RESULT "
        f"status={result['status']} completed={len(result['completed'])}/"
        f"{result['class_count']} candidates={result['candidate_count']} "
        f"max_v2_below_cap={result['max_v2_below_cap']}"
    )
