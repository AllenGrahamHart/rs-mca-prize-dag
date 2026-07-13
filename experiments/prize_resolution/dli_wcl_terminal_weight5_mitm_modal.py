#!/usr/bin/env python3
"""Bounded falsification round for official terminal weight-5 relations."""

from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

import modal


CPP = Path(__file__).with_name("dli_wcl_terminal_weight5_mitm.cpp")
OUTPUT = Path(__file__).with_name("dli_wcl_terminal_weight5_mitm_result.json")
COUNT = 64
K_LIMIT = 20_000

base = modal.Image.debian_slim().apt_install("pari-gp", "g++")
image = (
    base.add_local_file(str(CPP), "/root/search.cpp", copy=True)
    .run_commands("g++ -O3 -std=c++17 /root/search.cpp -o /usr/local/bin/weight5_mitm")
)
app = modal.App("rs-mca-dli-wcl-terminal-weight5-mitm")


@app.function(image=image, cpu=1, memory=1024, timeout=60)
def find_primes(count: int, k_limit: int) -> dict[str, list[dict[str, object]]]:
    program = (
        f"c=0;for(k=1,{k_limit},q=k*2^41+1;"
        f"if(isprime(q),g=lift(znprimroot(q));"
        f"print(\"P : \",k,\" : \",q,\" : \",g);c++;if(c=={count},break),"
        f"f=factor(q)[1,1];print(\"C : \",k,\" : \",q,\" : \",f)));quit()\n"
    )
    completed = subprocess.run(
        ["gp", "-q", "-s", "268435456"],
        input=program,
        text=True,
        capture_output=True,
        timeout=50,
        check=True,
    )
    primes = []
    composite_witnesses = []
    for line in completed.stdout.splitlines():
        parts = [part.strip() for part in line.split(":")]
        if len(parts) != 4:
            continue
        if parts[0] == "P":
            primes.append({"k": int(parts[1]), "q": parts[2], "generator": parts[3]})
        elif parts[0] == "C":
            composite_witnesses.append(
                {"k": int(parts[1]), "q": parts[2], "divisor": parts[3]}
            )
    if len(primes) != count:
        raise AssertionError((len(primes), count, completed.stderr))
    if len(primes) + len(composite_witnesses) != int(primes[-1]["k"]):
        raise AssertionError("incomplete first-prime partition")
    return {"primes": primes, "composite_witnesses": composite_witnesses}


@app.function(image=image, cpu=1, memory=1024, timeout=60, max_containers=64)
def search_prime(row: dict[str, object]) -> dict[str, object]:
    completed = subprocess.run(
        ["/usr/local/bin/weight5_mitm", row["q"], row["generator"]],
        text=True,
        capture_output=True,
        timeout=55,
        check=True,
    )
    result = json.loads(completed.stdout)
    return {"k": row["k"], **result}


@app.function(image=image, cpu=1, memory=512, timeout=60, max_containers=64)
def certify_prime(row: dict[str, object]) -> dict[str, object]:
    q = int(row["q"])
    remaining = int(row["k"])
    factors: list[list[object]] = []
    exponent_two = 41
    while remaining % 2 == 0:
        remaining //= 2
        exponent_two += 1
    factors.append(["2", exponent_two])
    divisor = 3
    while divisor * divisor <= remaining:
        if remaining % divisor:
            divisor += 2
            continue
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        factors.append([str(divisor), exponent])
        divisor += 2
    if remaining > 1:
        factors.append([str(remaining), 1])
    if math.prod(int(prime) ** exponent for prime, exponent in factors) != q - 1:
        raise AssertionError("q-1 factorization")
    witnesses = {}
    for prime_text, _ in factors:
        prime = int(prime_text)
        for base in range(2, 100_000):
            if (
                pow(base, q - 1, q) == 1
                and math.gcd(pow(base, (q - 1) // prime, q) - 1, q) == 1
            ):
                witnesses[prime_text] = base
                break
        else:
            raise AssertionError((q, prime, "no Pocklington witness"))
    generator = int(row["generator"])
    if any(pow(generator, (q - 1) // int(prime), q) == 1 for prime, _ in factors):
        raise AssertionError("generator is not primitive")
    return {
        "k": row["k"],
        "q": row["q"],
        "minus_one_factors": factors,
        "witnesses": witnesses,
    }


@app.local_entrypoint()
def main() -> None:
    discovery = find_primes.remote(COUNT, K_LIMIT)
    primes = discovery["primes"]
    result = {
        "schema": "dli-wcl-terminal-weight5-mitm-v1",
        "status": "IN_PROGRESS",
        "preregistered_count": COUNT,
        "k_limit": K_LIMIT,
        "primes": primes,
        "composite_witnesses": discovery["composite_witnesses"],
        "completed": [],
        "worker_errors": [],
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_WEIGHT5_MITM_START "
        f"count={COUNT} k_range={primes[0]['k']}..{primes[-1]['k']}",
        flush=True,
    )
    for row, found in zip(primes, search_prime.map(primes, return_exceptions=True)):
        if isinstance(found, BaseException):
            result["worker_errors"].append({"k": row["k"], "error": repr(found)})
        else:
            result["completed"].append(found)
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    result["status"] = "COMPLETE" if not result["worker_errors"] else "PARTIAL"
    result["relation_count"] = sum(row["found"] for row in result["completed"])
    if not result["worker_errors"]:
        result["prime_certificates"] = list(certify_prime.map(primes))
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_WEIGHT5_MITM_RESULT "
        f"status={result['status']} completed={len(result['completed'])}/{COUNT} "
        f"relations={result['relation_count']}"
    )
