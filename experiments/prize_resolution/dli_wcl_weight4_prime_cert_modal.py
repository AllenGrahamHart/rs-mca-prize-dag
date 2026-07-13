#!/usr/bin/env python3
"""Sharded recursive Pocklington certificates for weight-4 norm factors."""

from __future__ import annotations

import gzip
import io
import json
import math
import re
import subprocess
from pathlib import Path

import modal


ROOT = Path.cwd()
FACTOR_RESULT = ROOT / "experiments/prize_resolution/dli_wcl_weight4_section_result.json.gz"
OUTPUT = ROOT / "experiments/prize_resolution/dli_wcl_weight4_prime_cert_result.json.gz"

app = modal.App("rs-mca-dli-wcl-weight4-prime-cert")
image = modal.Image.debian_slim().apt_install("pari-gp")


def parse_factors(output: str, value: int) -> list[list[object]]:
    if value == 1:
        return []
    factors = []
    for line in output.splitlines():
        match = re.fullmatch(r"\s*(\d+)\s*:\s*(\d+)\s*", line)
        if match:
            factors.append([match.group(1), int(match.group(2))])
    product = math.prod(int(prime) ** exponent for prime, exponent in factors)
    if not factors or product != value:
        raise AssertionError(f"incomplete factorization value={value}")
    return factors


@app.function(image=image, cpu=1, memory=2048, timeout=300, max_containers=96)
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
            if candidate < 2 or any(candidate % divisor == 0 for divisor in range(2, math.isqrt(candidate) + 1)):
                raise AssertionError(f"nonprime leaf {candidate}")
            nodes[key] = {"method": "trial"}
            return
        factors = factor(candidate - 1)
        for prime_text, _ in factors:
            certify(int(prime_text))
        witnesses = {}
        for prime_text, _ in factors:
            divisor = int(prime_text)
            for base in range(2, 100_000):
                if (
                    pow(base, candidate - 1, candidate) == 1
                    and math.gcd(pow(base, (candidate - 1) // divisor, candidate) - 1, candidate) == 1
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
def main(shard_size: int = 500, resume: bool = True) -> None:
    with gzip.open(FACTOR_RESULT, "rt", encoding="utf-8") as handle:
        factor_result = json.load(handle)
    if factor_result.get("status") != "FULL_COMPLETE":
        raise AssertionError("weight-4 factor ledger is incomplete")
    roots = sorted(
        {
            factor["prime"]
            for row in factor_result["full_completed"]
            for factor in row["factors"]
        },
        key=int,
    )
    if resume and OUTPUT.exists():
        with gzip.open(OUTPUT, "rt", encoding="utf-8") as handle:
            result = json.load(handle)
        if result.get("schema") != "dli-wcl-weight4-prime-cert-v1":
            raise AssertionError("resume schema mismatch")
        completed_roots = {
            root for shard in result.get("completed_shards", []) for root in shard["roots"]
        }
        result["worker_errors"] = []
    else:
        result = {
            "schema": "dli-wcl-weight4-prime-cert-v1",
            "status": "IN_PROGRESS",
            "expected_roots": roots,
            "completed_shards": [],
            "worker_errors": [],
        }
        completed_roots = set()
    if result["expected_roots"] != roots:
        raise AssertionError("factor-root set changed")
    payloads = chunks([root for root in roots if root not in completed_roots], shard_size)
    result["status"] = "IN_PROGRESS"
    write_result(result)
    print(
        "DLI_WCL_WEIGHT4_CERT_START "
        f"roots={len(roots)} completed={len(completed_roots)} shards={len(payloads)}",
        flush=True,
    )
    for index, (payload, shard) in enumerate(
        zip(payloads, certify_shard.map(payloads, return_exceptions=True)), start=1
    ):
        if isinstance(shard, BaseException):
            result["worker_errors"].append(
                {"first_root": payload[0], "root_count": len(payload), "error": repr(shard)}
            )
        else:
            result["completed_shards"].append(shard)
        if index % 5 == 0 or index == len(payloads):
            write_result(result)

    if result["worker_errors"]:
        result["status"] = "PARTIAL"
        write_result(result)
        print(
            "DLI_WCL_WEIGHT4_CERT_RESULT "
            f"status=PARTIAL errors={len(result['worker_errors'])}"
        )
        return

    merged: dict[str, dict[str, object]] = {}
    certified_roots: set[str] = set()
    for shard in result["completed_shards"]:
        certified_roots.update(shard["roots"])
        for key, node in shard["nodes"].items():
            if key in merged and merged[key] != node:
                raise AssertionError(f"inconsistent shared node {key}")
            merged[key] = node
    if certified_roots != set(roots):
        raise AssertionError("incomplete certified root set")
    result = {
        "schema": "dli-wcl-weight4-prime-cert-v1",
        "status": "COMPLETE",
        "roots": roots,
        "nodes": merged,
        "worker_errors": [],
    }
    write_result(result)
    print(
        "DLI_WCL_WEIGHT4_CERT_RESULT "
        f"status=COMPLETE roots={len(roots)} nodes={len(merged)}"
    )
