#!/usr/bin/env python3
"""Independently verify the terminal DLI weight-3 exclusion certificate."""

from __future__ import annotations

import copy
import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "experiments/prize_resolution/dli_wcl_weight3_classes_result.json"
ORDER = 512
HALF = 256
WEIGHT = 3
RAW_COUNT = math.comb(HALF, WEIGHT) * 2 ** (WEIGHT - 1)
CLASS_COUNT = 254
AMBIENT_V2 = 41
CAP = 2**256
NORM_BOUND = 3**256


class Reject(ValueError):
    pass


def trial_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, math.isqrt(value) + 1, 2))


def valuation_two(value: int) -> int:
    return ((value & -value).bit_length() - 1) if value else 0


def encode(full_terms: tuple[int, int, int]) -> int:
    reduced = sorted((term % HALF, 1 if term < HALF else -1) for term in full_terms)
    if len({exponent for exponent, _ in reduced}) != WEIGHT:
        raise Reject("antipodal collision")
    if reduced[0][1] < 0:
        reduced = [(exponent, -sign) for exponent, sign in reduced]
    key = 0
    for index, (exponent, sign) in enumerate(reduced):
        key |= (exponent | ((sign < 0) << 8)) << (9 * index)
    return key


def verify_prime_tree(certificate: object, expected_roots: set[str]) -> int:
    if not isinstance(certificate, dict) or set(certificate) != {"nodes", "roots"}:
        raise Reject("prime certificate schema")
    roots = certificate["roots"]
    nodes = certificate["nodes"]
    if (
        not isinstance(roots, list)
        or roots != sorted(expected_roots, key=int)
        or len(roots) != len(set(roots))
        or not isinstance(nodes, dict)
    ):
        raise Reject("prime roots")

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
    if {str(value) for value in verified} != set(nodes):
        raise Reject("orphan prime certificate node")
    return len(verified)


def split_moduli() -> list[tuple[int, int]]:
    """Return certified 31-bit p=1 mod 512 and one exact order-512 root."""
    moduli: list[tuple[int, int]] = []
    product = 1
    candidate = ((2**31 - 2) // ORDER) * ORDER + 1
    while product <= 2 * NORM_BOUND:
        if trial_prime(candidate):
            omega = next(
                (
                    pow(base, (candidate - 1) // ORDER, candidate)
                    for base in range(2, 100)
                    if pow(pow(base, (candidate - 1) // ORDER, candidate), HALF, candidate)
                    == candidate - 1
                ),
                None,
            )
            if omega is None:
                raise Reject("missing split root")
            moduli.append((candidate, omega))
            product *= candidate
        candidate -= ORDER
    return moduli


def verify_resultants(rows: list[dict[str, object]]) -> int:
    moduli = split_moduli()
    modulus_product = math.prod(prime for prime, _ in moduli)
    if modulus_product <= 2 * NORM_BOUND:
        raise Reject("insufficient CRT modulus")
    for row in rows:
        exponents = row["exponents"]
        signs = row["signs"]
        norm = int(row["norm"])
        if not 0 < norm <= NORM_BOUND:
            raise Reject("norm bound")
        for prime, omega in moduli:
            root = omega
            step = omega * omega % prime
            resultant = 1
            for _ in range(HALF):
                value = sum(
                    sign * pow(root, exponent, prime)
                    for exponent, sign in zip(exponents, signs)
                ) % prime
                resultant = resultant * value % prime
                root = root * step % prime
            if resultant != norm % prime:
                raise Reject("modular resultant")
    return len(moduli)


def verify_orbits(representatives: list[dict[str, object]]) -> tuple[int, int]:
    canonical_keys: set[int] = set()
    covered = 0
    for row in representatives:
        full = tuple(
            exponent if sign > 0 else exponent + HALF
            for exponent, sign in zip(row["exponents"], row["signs"])
        )
        orbit: set[int] = set()
        for dilation in range(1, ORDER, 2):
            dilated = tuple(dilation * term % ORDER for term in full)
            for shift in range(HALF):
                orbit.add(encode(tuple((term + shift) % ORDER for term in dilated)))
        canonical = min(orbit)
        if canonical in canonical_keys:
            raise Reject("duplicate affine orbit")
        canonical_keys.add(canonical)
        covered += len(orbit)
    if len(canonical_keys) != CLASS_COUNT or covered != RAW_COUNT:
        raise Reject("incomplete affine orbit partition")
    return len(canonical_keys), covered


def verify_payload(payload: object, expensive: bool = True) -> dict[str, int]:
    if not isinstance(payload, dict):
        raise Reject("payload type")
    expected_keys = {
        "candidate_count",
        "class_count",
        "completed",
        "factor_pocklington",
        "max_v2_below_cap",
        "raw_count",
        "representatives",
        "schema",
        "status",
        "worker_errors",
    }
    if set(payload) != expected_keys:
        raise Reject("payload schema")
    if (
        payload["schema"] != "dli-wcl-weight3-affine-galois-v1"
        or payload["status"] != "COMPLETE"
        or payload["raw_count"] != RAW_COUNT
        or payload["class_count"] != CLASS_COUNT
        or payload["worker_errors"] != []
    ):
        raise Reject("payload header")
    representatives = payload["representatives"]
    completed = payload["completed"]
    if (
        not isinstance(representatives, list)
        or not isinstance(completed, list)
        or len(representatives) != CLASS_COUNT
        or len(completed) != CLASS_COUNT
    ):
        raise Reject("class list")

    reps_by_key: dict[int, dict[str, object]] = {}
    for row in representatives:
        if not isinstance(row, dict) or set(row) != {"exponents", "key", "signs"}:
            raise Reject("representative schema")
        exponents = row["exponents"]
        signs = row["signs"]
        if (
            not isinstance(exponents, list)
            or not isinstance(signs, list)
            or len(exponents) != WEIGHT
            or len(signs) != WEIGHT
            or exponents != sorted(exponents)
            or len(set(exponents)) != WEIGHT
            or any(not isinstance(value, int) or isinstance(value, bool) or not 0 <= value < HALF for value in exponents)
            or any(sign not in (-1, 1) for sign in signs)
            or signs[0] != 1
        ):
            raise Reject("representative support")
        full = tuple(exponent if sign > 0 else exponent + HALF for exponent, sign in zip(exponents, signs))
        key = row["key"]
        if not isinstance(key, int) or isinstance(key, bool) or key != encode(full) or key in reps_by_key:
            raise Reject("representative key")
        reps_by_key[key] = row

    factors_seen: set[str] = set()
    candidates: list[dict[str, object]] = []
    max_v2 = 0
    completed_keys: set[int] = set()
    for row in completed:
        required = {
            "exponents",
            "factors",
            "key",
            "norm",
            "norm_bits",
            "official_candidates",
            "signs",
        }
        if not isinstance(row, dict) or set(row) != required:
            raise Reject("completed schema")
        key = row["key"]
        if key in completed_keys or key not in reps_by_key:
            raise Reject("completed key")
        completed_keys.add(key)
        rep = reps_by_key[key]
        if row["exponents"] != rep["exponents"] or row["signs"] != rep["signs"]:
            raise Reject("completed representative")
        norm = int(row["norm"])
        if str(norm) != row["norm"] or row["norm_bits"] != norm.bit_length():
            raise Reject("norm metadata")
        factors = row["factors"]
        if not isinstance(factors, list):
            raise Reject("factor list")
        product = 1
        row_candidates = []
        row_primes: set[int] = set()
        for factor in factors:
            if not isinstance(factor, dict) or set(factor) != {
                "bits", "exponent", "prime", "v2_prime_minus_1"
            }:
                raise Reject("factor schema")
            prime = int(factor["prime"])
            exponent = factor["exponent"]
            if (
                str(prime) != factor["prime"]
                or prime in row_primes
                or not isinstance(exponent, int)
                or isinstance(exponent, bool)
                or exponent <= 0
                or factor["bits"] != prime.bit_length()
                or factor["v2_prime_minus_1"] != valuation_two(prime - 1)
            ):
                raise Reject("factor metadata")
            row_primes.add(prime)
            factors_seen.add(str(prime))
            product *= prime**exponent
            if prime < CAP:
                max_v2 = max(max_v2, factor["v2_prime_minus_1"])
                if factor["v2_prime_minus_1"] >= AMBIENT_V2:
                    row_candidates.append(factor)
                    candidates.append(factor)
        if product != norm or row["official_candidates"] != row_candidates:
            raise Reject("factor reconstruction")
    if completed_keys != set(reps_by_key):
        raise Reject("missing completed class")
    if payload["candidate_count"] != len(candidates) or candidates:
        raise Reject("ambient candidate")
    if payload["max_v2_below_cap"] != max_v2 or max_v2 != 18:
        raise Reject("splitting-depth maximum")

    prime_nodes = verify_prime_tree(payload["factor_pocklington"], factors_seen)
    classes = covered = moduli = 0
    if expensive:
        classes, covered = verify_orbits(representatives)
        moduli = verify_resultants(completed)
    return {
        "classes": classes,
        "covered": covered,
        "moduli": moduli,
        "factor_roots": len(factors_seen),
        "prime_nodes": prime_nodes,
        "max_v2": max_v2,
    }


def rejected(payload: dict[str, object]) -> bool:
    try:
        verify_payload(payload, expensive=False)
    except (Reject, KeyError, TypeError, ValueError):
        return True
    return False


def main() -> None:
    payload = json.loads(RESULT.read_text())
    summary = verify_payload(payload)
    mutations = []
    mutators = (
        lambda item: item.__setitem__("candidate_count", 1),
        lambda item: item.__setitem__("max_v2_below_cap", 17),
        lambda item: item["completed"][0]["factors"][0].__setitem__("prime", "119811"),
        lambda item: item["representatives"][0]["exponents"].__setitem__(2, 3),
        lambda item: next(
            node for node in item["factor_pocklington"]["nodes"].values()
            if node.get("method") == "pocklington"
        )["witnesses"].__setitem__("2", 1),
    )
    for mutate in mutators:
        candidate = copy.deepcopy(payload)
        mutate(candidate)
        mutations.append(candidate)
    caught = sum(rejected(candidate) for candidate in mutations)
    if caught != len(mutations):
        raise AssertionError(f"negative controls caught {caught}/{len(mutations)}")
    print(
        "DLI_WCL_WEIGHT3_AMBIENT_EXCLUSION_PASS "
        f"classes={summary['classes']} covered={summary['covered']} "
        f"crt_moduli={summary['moduli']} factor_roots={summary['factor_roots']} "
        f"prime_nodes={summary['prime_nodes']} max_v2={summary['max_v2']} "
        f"negative_controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
