#!/usr/bin/env python3
"""Build recursive Pocklington certificates for weight-six norm factors."""

from __future__ import annotations

import gzip
import io
import json
import math
import re
import subprocess
from pathlib import Path

import modal


FACTOR_RESULT = Path(__file__).with_name(
    "dli_wcl_ell2_weight6_recursive_norm_full_result.json"
)
OUTPUT = Path(__file__).with_name(
    "dli_wcl_ell2_weight6_recursive_norm_prime_cert_result.json.gz"
)

app = modal.App("rs-mca-dli-wcl-ell2-weight6-recursive-norm-prime-cert")
image = modal.Image.debian_slim().apt_install("pari-gp")


def parse_factors(output: str, value: int) -> list[list[object]]:
    factors = []
    for line in output.splitlines():
        match = re.fullmatch(r"\s*(\d+)\s*:\s*(\d+)\s*", line)
        if match:
            factors.append([match.group(1), int(match.group(2))])
    product = math.prod(int(prime) ** exponent for prime, exponent in factors)
    if not factors or product != value:
        raise AssertionError((value, product, output))
    return factors


@app.function(image=image, cpu=1, memory=2048, timeout=300, max_containers=64)
def certify_shard(prime_texts: list[str]) -> dict[str, object]:
    nodes: dict[str, dict[str, object]] = {}

    def factor(value: int) -> list[list[object]]:
        program = (
            f"n={value};f=factor(n);"
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
        return parse_factors(completed.stdout, value)

    def certify(candidate: int) -> None:
        key = str(candidate)
        if key in nodes:
            return
        if candidate < 10_000:
            if candidate < 2 or any(
                candidate % divisor == 0
                for divisor in range(2, math.isqrt(candidate) + 1)
            ):
                raise AssertionError(f"nonprime leaf {candidate}")
            nodes[key] = {"method": "trial"}
            return

        factors = factor(candidate - 1)
        for prime_text, _ in factors:
            certify(int(prime_text))
        witnesses: dict[str, int] = {}
        for prime_text, _ in factors:
            divisor = int(prime_text)
            for base in range(2, 100_000):
                if (
                    pow(base, candidate - 1, candidate) == 1
                    and math.gcd(
                        pow(base, (candidate - 1) // divisor, candidate) - 1,
                        candidate,
                    )
                    == 1
                ):
                    witnesses[prime_text] = base
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


def chunks(items: list[str], size: int) -> list[list[str]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def write_result(result: dict[str, object]) -> None:
    with OUTPUT.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as compressed:
            with io.TextIOWrapper(compressed, encoding="utf-8") as handle:
                json.dump(result, handle, indent=2, sort_keys=True)
                handle.write("\n")


@app.local_entrypoint()
def main(shard_size: int = 24) -> None:
    factor_result = json.loads(FACTOR_RESULT.read_text())
    if (
        factor_result.get("status") != "COMPLETE"
        or factor_result.get("scope") != "complete"
        or factor_result.get("covered_rows") != 404_740
        or factor_result.get("errors")
        or factor_result.get("high_gate_cases")
    ):
        raise AssertionError("factor ledger incomplete")
    roots = sorted(set(factor_result["distinct_primes"]), key=int)
    payloads = chunks(roots, shard_size)
    remote_rows = list(certify_shard.map(payloads, return_exceptions=True))
    errors = []
    merged: dict[str, dict[str, object]] = {}
    certified_roots = set()
    for payload, row in zip(payloads, remote_rows):
        if isinstance(row, BaseException):
            errors.append(
                {"first_root": payload[0], "root_count": len(payload), "error": repr(row)}
            )
            continue
        certified_roots.update(row["roots"])
        for key, node in row["nodes"].items():
            if key in merged and merged[key] != node:
                raise AssertionError(f"inconsistent shared node {key}")
            merged[key] = node
    result = {
        "schema": "dli-wcl-ell2-weight6-recursive-norm-prime-cert-v1",
        "status": "COMPLETE" if not errors and certified_roots == set(roots) else "PARTIAL",
        "roots": roots,
        "nodes": merged,
        "worker_errors": errors,
    }
    write_result(result)
    print(
        "DLI_WCL_ELL2_WEIGHT6_PRIME_CERT "
        f"status={result['status']} roots={len(roots)} nodes={len(merged)} "
        f"errors={len(errors)}"
    )
