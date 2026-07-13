#!/usr/bin/env python3
"""Verify the algebraic and DAG interfaces of the ell=2 weight-4 exclusion."""

from __future__ import annotations

import copy
import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DAG = ROOT / "dag.json"
PIN = ROOT / "critical/nodes/dli_prime_weighted_large_block_support/DLI_CLOSE_PINNED.md"
NODE = "dli_wcl_ell2_weight4_newton_exclusion"
ZONE = "dli_wcl_zone_coverage"
TEST_PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31)


class Reject(ValueError):
    pass


def trial_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, math.isqrt(value) + 1))


def elementary(roots: tuple[int, ...], prime: int) -> tuple[int, int, int, int]:
    return tuple(
        sum(math.prod(part) for part in itertools.combinations(roots, size)) % prime
        for size in range(1, 5)
    )


def compile_newton(payload: object) -> dict[str, object]:
    if not isinstance(payload, dict) or set(payload) != {"prime", "roots"}:
        raise Reject("payload schema")
    prime = payload["prime"]
    roots = payload["roots"]
    if (
        not isinstance(prime, int)
        or isinstance(prime, bool)
        or prime in (2, 3)
        or not trial_prime(prime)
    ):
        raise Reject("field")
    if (
        not isinstance(roots, list)
        or len(roots) != 4
        or any(not isinstance(root, int) or isinstance(root, bool) for root in roots)
    ):
        raise Reject("roots")
    reduced = tuple(root % prime for root in roots)
    if 0 in reduced or len(set(reduced)) != 4:
        raise Reject("distinct nonzero roots")

    p1 = sum(reduced) % prime
    p2 = sum(root * root for root in reduced) % prime
    p3 = sum(root**3 for root in reduced) % prime
    a1, a2, a3, a4 = elementary(reduced, prime)
    if a1 != p1 or (p3 - a1 * p2 + a2 * p1 - 3 * a3) % prime:
        raise Reject("Newton identity")
    if p1 or p3:
        raise Reject("odd-power hypotheses")
    if a1 or a3:
        raise Reject("odd coefficients")

    for root in reduced:
        if (root**4 + a2 * root**2 + a4) % prime:
            raise Reject("root polynomial")
    antipodal = all((-root) % prime in reduced for root in reduced)
    if not antipodal:
        raise Reject("even polynomial did not pair roots")
    return {"antipodal": antipodal, "a2": a2, "a4": a4}


def exhaustive_field_check(prime: int) -> tuple[int, int]:
    hits = 0
    forbidden_reduced = 0
    for roots in itertools.combinations(range(1, prime), 4):
        if sum(roots) % prime or sum(root**3 for root in roots) % prime:
            continue
        hits += 1
        result = compile_newton({"prime": prime, "roots": list(roots)})
        if result["antipodal"]:
            forbidden_reduced += 1
    if hits != forbidden_reduced:
        raise AssertionError("non-antipodal solution")
    return hits, forbidden_reduced


def main() -> None:
    dag = json.loads(DAG.read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    pin = PIN.read_text()
    structural = {
        "node_proved": nodes[NODE]["status"] == "PROVED",
        "proof_closure": nodes[NODE]["closure"] == "proof",
        "zone_target": nodes[ZONE]["status"] == "TARGET",
        "evidence_edge": (NODE, ZONE, "ev") in edges,
        "odd_power_matrix": "A_{l,y} = x_y^{2l-1}" in pin,
    }
    if not all(structural.values()):
        raise AssertionError(structural)

    checked = 0
    hits = 0
    for prime in TEST_PRIMES:
        field_hits, paired = exhaustive_field_check(prime)
        if field_hits != paired:
            raise AssertionError("field census")
        checked += math.comb(prime - 1, 4)
        hits += field_hits
    if hits == 0:
        raise AssertionError("vacuous finite controls")

    # The cubic equation is load-bearing: first-power cancellation alone has
    # non-antipodal four-sets.
    first_only = next(
        (prime, roots)
        for prime in TEST_PRIMES
        for roots in itertools.combinations(range(1, prime), 4)
        if sum(roots) % prime == 0
        and any((-root) % prime not in roots for root in roots)
    )
    prime, roots = first_only
    invalid = {"prime": prime, "roots": list(roots)}
    controls = 0
    mutations = (
        lambda item: item.__setitem__("prime", 3),
        lambda item: item["roots"].__setitem__(1, item["roots"][0]),
        lambda item: item["roots"].__setitem__(0, 0),
        lambda item: item.__setitem__("extra", True),
    )
    for mutate in mutations:
        altered = copy.deepcopy(invalid)
        mutate(altered)
        try:
            compile_newton(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls += 1
    try:
        compile_newton(invalid)
    except Reject as error:
        if str(error) != "odd-power hypotheses":
            raise
        controls += 1
    if controls != len(mutations) + 1:
        raise AssertionError(f"negative controls caught {controls}/{len(mutations) + 1}")

    # Distinct reduced exponents can never encode an antipodal full pair.
    for exponents in itertools.combinations(range(8), 4):
        for signs in itertools.product((1, -1), repeat=4):
            full = tuple(e + (512 if sign < 0 else 0) for e, sign in zip(exponents, signs))
            if any((left - right) % 1024 == 512 for left, right in itertools.combinations(full, 2)):
                raise AssertionError("reduced support admitted antipodal terms")

    print(
        "DLI_WCL_ELL2_WEIGHT4_NEWTON_PASS "
        f"fields={len(TEST_PRIMES)} four_sets={checked} paired_hits={hits} "
        f"negative_controls={controls}/{len(mutations) + 1}"
    )


if __name__ == "__main__":
    main()
