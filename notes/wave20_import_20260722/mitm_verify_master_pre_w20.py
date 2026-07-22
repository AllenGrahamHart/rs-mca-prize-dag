#!/usr/bin/env python3
"""Verify and exactly replay the first-64 terminal weight-5 MITM packet."""

from __future__ import annotations

import copy
import hashlib
import json
import math
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "experiments/prize_resolution/dli_wcl_terminal_weight5_mitm_result.json"
SOURCE = ROOT / "experiments/prize_resolution/dli_wcl_terminal_weight5_mitm.cpp"
SOURCE_SHA256 = "dd61eb4c0f57334a4a03974b85a91e2447bbad042d0bb47adb4d03df86d76c5c"
COUNT = 64
LAST_K = 996
PAIR_COUNT = 130_560
TRIPLE_COUNT = 22_108_160


class Reject(ValueError):
    pass


def integer(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise Reject("integer field")
    return value


def canonical_positive(text: object) -> int:
    if not isinstance(text, str):
        raise Reject("integer string")
    value = int(text)
    if value <= 0 or str(value) != text:
        raise Reject("noncanonical integer string")
    return value


def trial_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, math.isqrt(value) + 1, 2))


def validate(data: object) -> list[dict[str, object]]:
    if not isinstance(data, dict) or set(data) != {
        "completed",
        "composite_witnesses",
        "k_limit",
        "preregistered_count",
        "prime_certificates",
        "primes",
        "relation_count",
        "schema",
        "status",
        "worker_errors",
    }:
        raise Reject("top-level schema")
    if (
        data["schema"] != "dli-wcl-terminal-weight5-mitm-v1"
        or data["status"] != "COMPLETE"
        or data["worker_errors"] != []
        or integer(data["preregistered_count"]) != COUNT
        or integer(data["k_limit"]) != 20_000
        or integer(data["relation_count"]) != 0
    ):
        raise Reject("header")

    primes = data["primes"]
    composites = data["composite_witnesses"]
    certificates = data["prime_certificates"]
    completed = data["completed"]
    if not all(isinstance(rows, list) for rows in (primes, composites, certificates, completed)):
        raise Reject("row collections")
    if not (len(primes) == len(certificates) == len(completed) == COUNT):
        raise Reject("prime row count")
    if len(composites) != LAST_K - COUNT:
        raise Reject("composite row count")

    prime_by_k: dict[int, dict[str, object]] = {}
    for row in primes:
        if not isinstance(row, dict) or set(row) != {"generator", "k", "q"}:
            raise Reject("prime row schema")
        k = integer(row["k"])
        q = canonical_positive(row["q"])
        canonical_positive(row["generator"])
        if q != k * 2**41 + 1 or k in prime_by_k:
            raise Reject("prime row")
        prime_by_k[k] = row

    composite_by_k: dict[int, dict[str, object]] = {}
    for row in composites:
        if not isinstance(row, dict) or set(row) != {"divisor", "k", "q"}:
            raise Reject("composite row schema")
        k = integer(row["k"])
        q = canonical_positive(row["q"])
        divisor = canonical_positive(row["divisor"])
        if q != k * 2**41 + 1 or not 1 < divisor < q or q % divisor or k in composite_by_k:
            raise Reject("composite witness")
        composite_by_k[k] = row
    if set(prime_by_k).isdisjoint(composite_by_k) is False:
        raise Reject("row overlap")
    if set(prime_by_k) | set(composite_by_k) != set(range(1, LAST_K + 1)):
        raise Reject("first-prime partition")
    if sorted(prime_by_k)[-1] != LAST_K:
        raise Reject("last prime row")

    certificate_by_k: dict[int, dict[str, object]] = {}
    for row in certificates:
        if not isinstance(row, dict) or set(row) != {
            "k", "minus_one_factors", "q", "witnesses"
        }:
            raise Reject("certificate schema")
        k = integer(row["k"])
        q = canonical_positive(row["q"])
        prime_row = prime_by_k.get(k)
        if prime_row is None or q != canonical_positive(prime_row["q"]):
            raise Reject("certificate row")
        factors = row["minus_one_factors"]
        witnesses = row["witnesses"]
        if not isinstance(factors, list) or not isinstance(witnesses, dict):
            raise Reject("certificate payload")
        product = 1
        factor_primes: set[int] = set()
        for pair in factors:
            if not isinstance(pair, list) or len(pair) != 2:
                raise Reject("factor pair")
            factor = canonical_positive(pair[0])
            exponent = integer(pair[1])
            if exponent <= 0 or factor in factor_primes or not trial_prime(factor):
                raise Reject("factorization")
            product *= factor**exponent
            factor_primes.add(factor)
        if product != q - 1 or set(witnesses) != {str(factor) for factor in factor_primes}:
            raise Reject("complete q-1 factorization")
        for factor in factor_primes:
            base = integer(witnesses[str(factor)])
            if pow(base, q - 1, q) != 1:
                raise Reject("Pocklington Fermat condition")
            if math.gcd(pow(base, (q - 1) // factor, q) - 1, q) != 1:
                raise Reject("Pocklington gcd condition")
        generator = canonical_positive(prime_row["generator"])
        if any(pow(generator, (q - 1) // factor, q) == 1 for factor in factor_primes):
            raise Reject("nonprimitive generator")
        certificate_by_k[k] = row
    if set(certificate_by_k) != set(prime_by_k):
        raise Reject("certificate coverage")

    completed_by_k: dict[int, dict[str, object]] = {}
    for row in completed:
        if not isinstance(row, dict) or set(row) != {
            "found", "generator", "k", "omega", "pair_count", "q", "relation",
            "seconds", "triples_checked"
        }:
            raise Reject("search row schema")
        k = integer(row["k"])
        prime_row = prime_by_k.get(k)
        if prime_row is None or row["q"] != prime_row["q"] or row["generator"] != prime_row["generator"]:
            raise Reject("search row identity")
        q = canonical_positive(row["q"])
        omega = canonical_positive(row["omega"])
        generator = canonical_positive(row["generator"])
        seconds = row["seconds"]
        if not isinstance(seconds, (int, float)) or isinstance(seconds, bool) or seconds < 0:
            raise Reject("search timing")
        if (
            integer(row["pair_count"]) != PAIR_COUNT
            or integer(row["triples_checked"]) != TRIPLE_COUNT
            or row["found"] is not False
            or row["relation"] != []
            or pow(omega, 512, q) != 1
            or pow(omega, 256, q) != q - 1
            or omega != pow(generator, (q - 1) // 512, q)
            or k in completed_by_k
        ):
            raise Reject("search result")
        completed_by_k[k] = row
    if set(completed_by_k) != set(prime_by_k):
        raise Reject("search coverage")
    return [prime_by_k[k] for k in sorted(prime_by_k)]


def replay(rows: list[dict[str, object]]) -> None:
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_SHA256:
        raise Reject("search source hash")
    with tempfile.TemporaryDirectory() as directory:
        binary = Path(directory) / "weight5_mitm"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(SOURCE), "-o", str(binary)],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        for row in rows:
            process = subprocess.run(
                [str(binary), str(row["q"]), str(row["generator"])],
                check=True,
                capture_output=True,
                text=True,
                timeout=10,
            )
            result = json.loads(process.stdout)
            if (
                result.get("q") != row["q"]
                or result.get("generator") != row["generator"]
                or result.get("pair_count") != PAIR_COUNT
                or result.get("triples_checked") != TRIPLE_COUNT
                or result.get("found") is not False
                or result.get("relation") != []
            ):
                raise Reject("exact replay")


def main() -> None:
    data = json.loads(RESULT.read_text())
    rows = validate(data)
    controls = []
    mutations = (
        lambda item: item["composite_witnesses"][0].__setitem__("divisor", "1"),
        lambda item: item["prime_certificates"][0]["witnesses"].__setitem__("2", 1),
        lambda item: item["completed"][0].__setitem__("found", True),
        lambda item: item["completed"][0].__setitem__("triples_checked", TRIPLE_COUNT - 1),
        lambda item: item["primes"].pop(),
    )
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError(f"negative controls caught {sum(controls)}/{len(controls)}")
    replay(rows)
    print(
        "DLI_WCL_WEIGHT5_FIRST64_PASS "
        f"primes={len(rows)} composites={LAST_K-COUNT} "
        f"pairs_per_row={PAIR_COUNT} triples_per_row={TRIPLE_COUNT} "
        f"negative_controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
