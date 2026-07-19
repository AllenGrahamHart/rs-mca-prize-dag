#!/usr/bin/env python3
"""Verify every recursive Pocklington node in the weight-4 certificate."""

from __future__ import annotations

import gzip
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
LEDGER = ROOT / "experiments/prize_resolution/dli_wcl_weight4_section_result.json.gz"
CERT = ROOT / "experiments/prize_resolution/dli_wcl_weight4_prime_cert_result.json.gz"
ROOT_COUNT = 44_599
NODE_COUNT = 154_086


class Reject(ValueError):
    pass


def trial_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, math.isqrt(value) + 1, 2))


def expected_roots() -> list[str]:
    with gzip.open(LEDGER, "rt", encoding="utf-8") as handle:
        ledger = json.load(handle)
    if ledger.get("status") != "FULL_COMPLETE":
        raise Reject("factor ledger incomplete")
    return sorted(
        {
            factor["prime"]
            for row in ledger["full_completed"]
            for factor in row["factors"]
        },
        key=int,
    )


def verify_header(certificate: object, roots: list[str]) -> tuple[list[str], dict[str, object]]:
    if not isinstance(certificate, dict) or set(certificate) != {
        "nodes", "roots", "schema", "status", "worker_errors"
    }:
        raise Reject("certificate schema")
    if (
        certificate["schema"] != "dli-wcl-weight4-prime-cert-v1"
        or certificate["status"] != "COMPLETE"
        or certificate["worker_errors"] != []
        or certificate["roots"] != roots
        or len(roots) != ROOT_COUNT
        or len(set(roots)) != ROOT_COUNT
        or not isinstance(certificate["nodes"], dict)
        or len(certificate["nodes"]) != NODE_COUNT
    ):
        raise Reject("certificate header")
    return certificate["roots"], certificate["nodes"]


def verify_tree(
    roots: list[str], nodes: dict[str, object], require_all_nodes: bool = True
) -> int:
    verified: set[int] = set()

    def visit(value: int) -> None:
        if value in verified:
            return
        node = nodes.get(str(value))
        if not isinstance(node, dict):
            raise Reject("missing prime node")
        if node == {"method": "trial"}:
            if value >= 10_000 or not trial_prime(value):
                raise Reject("bad trial prime")
            verified.add(value)
            return
        if set(node) != {"method", "minus_one_factors", "witnesses"}:
            raise Reject("Pocklington node schema")
        if node["method"] != "pocklington":
            raise Reject("Pocklington method")
        factors = node["minus_one_factors"]
        witnesses = node["witnesses"]
        if not isinstance(factors, list) or not isinstance(witnesses, dict):
            raise Reject("Pocklington payload")
        product = 1
        primes: set[int] = set()
        for pair in factors:
            if not isinstance(pair, list) or len(pair) != 2:
                raise Reject("Pocklington factor pair")
            prime = int(pair[0])
            exponent = pair[1]
            if (
                str(prime) != pair[0]
                or prime in primes
                or not isinstance(exponent, int)
                or isinstance(exponent, bool)
                or exponent <= 0
            ):
                raise Reject("Pocklington factor")
            visit(prime)
            primes.add(prime)
            product *= prime**exponent
        if product != value - 1 or product <= math.isqrt(value):
            raise Reject("incomplete Pocklington factorization")
        if set(witnesses) != {str(prime) for prime in primes}:
            raise Reject("Pocklington witnesses")
        for prime in primes:
            base = witnesses[str(prime)]
            if not isinstance(base, int) or isinstance(base, bool):
                raise Reject("Pocklington base")
            if pow(base, value - 1, value) != 1:
                raise Reject("Pocklington Fermat condition")
            if math.gcd(pow(base, (value - 1) // prime, value) - 1, value) != 1:
                raise Reject("Pocklington gcd condition")
        verified.add(value)

    for root in roots:
        visit(int(root))
    if require_all_nodes and {str(value) for value in verified} != set(nodes):
        raise Reject("orphan prime certificate node")
    return len(verified)


def rejected(root: str, nodes: dict[str, object], mutate, restore) -> bool:
    mutate()
    try:
        verify_tree([root], nodes, require_all_nodes=False)
    except (Reject, KeyError, TypeError, ValueError):
        caught = True
    else:
        caught = False
    finally:
        restore()
    return caught


def main() -> None:
    roots = expected_roots()
    with gzip.open(CERT, "rt", encoding="utf-8") as handle:
        certificate = json.load(handle)
    certified_roots, nodes = verify_header(certificate, roots)
    verified = verify_tree(certified_roots, nodes)

    root = "1000001957"
    node = nodes[root]
    old_witness = node["witnesses"]["2"]
    old_exponent = node["minus_one_factors"][0][1]
    controls = [
        rejected(
            root,
            nodes,
            lambda: node["witnesses"].__setitem__("2", 1),
            lambda: node["witnesses"].__setitem__("2", old_witness),
        ),
        rejected(
            root,
            nodes,
            lambda: node["minus_one_factors"][0].__setitem__(1, old_exponent + 1),
            lambda: node["minus_one_factors"][0].__setitem__(1, old_exponent),
        ),
        rejected(
            "2",
            nodes,
            lambda: nodes.__setitem__("2", {"method": "trial-bad"}),
            lambda: nodes.__setitem__("2", {"method": "trial"}),
        ),
    ]
    old_root = certificate["roots"].pop()
    try:
        try:
            verify_header(certificate, roots)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    finally:
        certificate["roots"].append(old_root)
    caught = sum(controls)
    if caught != len(controls):
        raise AssertionError(f"negative controls caught {caught}/{len(controls)}")
    print(
        "DLI_WCL_WEIGHT4_PRIMES_PASS "
        f"roots={len(roots)} nodes={verified} negative_controls={caught}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
