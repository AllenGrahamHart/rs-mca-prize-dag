#!/usr/bin/env python3
"""Verify every recursive Pocklington node in the ell=2 weight-3 packet."""

from __future__ import annotations

import copy
import gzip
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
LEDGER = ROOT / "experiments/prize_resolution/dli_wcl_ell2_weight3_classes_result.json"
CERT = ROOT / "experiments/prize_resolution/dli_wcl_ell2_weight3_prime_cert_result.json.gz"
ROOT_COUNT = 1_141
NODE_COUNT = 5_608


class Reject(ValueError):
    pass


def trial_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, math.isqrt(value) + 1, 2))


def expected_roots() -> list[str]:
    ledger = json.loads(LEDGER.read_text())
    if ledger.get("status") != "COMPLETE":
        raise Reject("factor ledger incomplete")
    return sorted(
        {factor["prime"] for row in ledger["completed"] for factor in row["factors"]},
        key=int,
    )


def verify_tree(roots: list[str], nodes: dict[str, object], require_all: bool = True) -> int:
    verified: set[int] = set()

    def visit(value: int) -> None:
        if value in verified:
            return
        node = nodes.get(str(value))
        if not isinstance(node, dict):
            raise Reject("missing prime node")
        if node == {"method": "trial"}:
            if value >= 10_000 or not trial_prime(value):
                raise Reject("trial prime")
            verified.add(value)
            return
        if set(node) != {"method", "minus_one_factors", "witnesses"} or node["method"] != "pocklington":
            raise Reject("Pocklington schema")
        factors = node["minus_one_factors"]
        witnesses = node["witnesses"]
        if not isinstance(factors, list) or not isinstance(witnesses, dict):
            raise Reject("Pocklington payload")
        product = 1
        primes = set()
        for pair in factors:
            if not isinstance(pair, list) or len(pair) != 2:
                raise Reject("factor pair")
            prime = int(pair[0])
            exponent = pair[1]
            if (
                str(prime) != pair[0] or prime in primes
                or not isinstance(exponent, int) or isinstance(exponent, bool) or exponent <= 0
            ):
                raise Reject("factor")
            visit(prime)
            primes.add(prime)
            product *= prime**exponent
        if product != value - 1 or product <= math.isqrt(value):
            raise Reject("incomplete factorization")
        if set(witnesses) != {str(prime) for prime in primes}:
            raise Reject("witness set")
        for prime in primes:
            base = witnesses[str(prime)]
            if not isinstance(base, int) or isinstance(base, bool):
                raise Reject("witness type")
            if pow(base, value - 1, value) != 1:
                raise Reject("Fermat condition")
            if math.gcd(pow(base, (value - 1) // prime, value) - 1, value) != 1:
                raise Reject("gcd condition")
        verified.add(value)

    for root in roots:
        visit(int(root))
    if require_all and {str(value) for value in verified} != set(nodes):
        raise Reject("orphan node")
    return len(verified)


def main() -> None:
    roots = expected_roots()
    with gzip.open(CERT, "rt", encoding="utf-8") as handle:
        certificate = json.load(handle)
    if not isinstance(certificate, dict) or set(certificate) != {
        "nodes", "roots", "schema", "status", "worker_errors"
    }:
        raise Reject("certificate schema")
    if (
        certificate["schema"] != "dli-wcl-ell2-weight3-prime-cert-v1"
        or certificate["status"] != "COMPLETE" or certificate["worker_errors"] != []
        or certificate["roots"] != roots or len(roots) != ROOT_COUNT
        or not isinstance(certificate["nodes"], dict)
        or len(certificate["nodes"]) != NODE_COUNT
    ):
        raise Reject("certificate header")
    nodes = certificate["nodes"]
    verified = verify_tree(roots, nodes)

    root = next(root for root in roots if nodes[root].get("method") == "pocklington")
    controls = 0
    mutations = (
        lambda item: item[root]["witnesses"].__setitem__(next(iter(item[root]["witnesses"])), 1),
        lambda item: item[root]["minus_one_factors"][0].__setitem__(1, item[root]["minus_one_factors"][0][1] + 1),
        lambda item: item.__setitem__("2", {"method": "trial-bad"}),
    )
    for mutate in mutations:
        altered = copy.deepcopy(nodes)
        mutate(altered)
        try:
            verify_tree([root], altered, require_all=False)
        except (Reject, KeyError, TypeError, ValueError):
            controls += 1
    if controls != len(mutations):
        raise AssertionError(f"negative controls caught {controls}/{len(mutations)}")
    print(
        "DLI_WCL_ELL2_WEIGHT3_PRIMES_PASS "
        f"roots={len(roots)} nodes={verified} negative_controls={controls}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
