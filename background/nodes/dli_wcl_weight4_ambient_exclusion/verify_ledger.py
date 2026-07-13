#!/usr/bin/env python3
"""Verify the weight-4 normalized orbit and exact norm/factor ledger."""

from __future__ import annotations

import itertools
import gzip
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "experiments/prize_resolution/dli_wcl_weight4_section_result.json.gz"
ORDER = 512
HALF = 256
WEIGHT = 4
RAW_COUNT = math.comb(HALF, WEIGHT) * 2 ** (WEIGHT - 1)
SECTION_COUNT = 1_014_080
CLASS_COUNT = 24_979
FACTOR_RECORDS = 88_086
FACTOR_ROOTS = 44_599
AMBIENT_V2 = 41
CAP = 2**256
NORM_BOUND = 4**256


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


def encode(full_terms: tuple[int, ...]) -> int:
    reduced = sorted((term % HALF, 1 if term < HALF else -1) for term in full_terms)
    if len(reduced) != WEIGHT or len({exponent for exponent, _ in reduced}) != WEIGHT:
        raise Reject("antipodal collision")
    if reduced[0][1] < 0:
        reduced = [(exponent, -sign) for exponent, sign in reduced]
    key = 0
    for index, (exponent, sign) in enumerate(reduced):
        key |= (exponent | ((sign < 0) << 8)) << (9 * index)
    return key


def normalized_transforms(full: tuple[int, ...]) -> set[int]:
    transformed: set[int] = set()
    for left in full:
        for right in full:
            if left == right:
                continue
            difference = (right - left) % ORDER
            v2 = valuation_two(difference)
            if v2 >= 8:
                continue
            modulus = 1 << (9 - v2)
            base = pow(difference >> v2, -1, modulus)
            for lift in range(1 << v2):
                dilation = base + lift * modulus
                shift = -dilation * left
                transformed.add(
                    encode(tuple((dilation * term + shift) % ORDER for term in full))
                )
    return transformed


def validate_representatives(rows: object) -> dict[int, dict[str, object]]:
    if not isinstance(rows, list) or len(rows) != CLASS_COUNT:
        raise Reject("representative count")
    by_key: dict[int, dict[str, object]] = {}
    for row in rows:
        if not isinstance(row, dict) or set(row) != {
            "exponents", "key", "section_orbit_size", "signs"
        }:
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
            or not isinstance(row["section_orbit_size"], int)
            or row["section_orbit_size"] <= 0
        ):
            raise Reject("representative support")
        full = tuple(
            exponent if sign > 0 else exponent + HALF
            for exponent, sign in zip(exponents, signs)
        )
        key = row["key"]
        if not isinstance(key, int) or isinstance(key, bool) or key != encode(full) or key in by_key:
            raise Reject("representative key")
        by_key[key] = row
    return by_key


def verify_section_partition(representatives: list[dict[str, object]]) -> tuple[int, int]:
    remaining: set[int] = set()
    universe = range(ORDER)
    for v2 in range(8):
        pinned = 1 << v2
        forbidden = {0, HALF, pinned, pinned + HALF}
        available = [term for term in universe if term not in forbidden]
        for tail in itertools.combinations(available, WEIGHT - 2):
            full = (0, pinned, *tail)
            if any(
                (left - right) % ORDER == HALF
                for left, right in itertools.combinations(full, 2)
            ):
                continue
            remaining.add(encode(full))
    if len(remaining) != SECTION_COUNT:
        raise Reject("normalized section size")
    max_orbit = 0
    for row in representatives:
        full = tuple(
            exponent if sign > 0 else exponent + HALF
            for exponent, sign in zip(row["exponents"], row["signs"])
        )
        orbit = normalized_transforms(full)
        if len(orbit) != row["section_orbit_size"] or not orbit <= remaining:
            raise Reject("normalized orbit partition")
        max_orbit = max(max_orbit, len(orbit))
        remaining.difference_update(orbit)
    if remaining:
        raise Reject("uncovered normalized section")
    return SECTION_COUNT, max_orbit


def split_moduli() -> list[tuple[int, int]]:
    moduli = []
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


def verify_resultants(rows: list[dict[str, object]], batch_size: int = 1000) -> int:
    moduli = split_moduli()
    if math.prod(prime for prime, _ in moduli) <= 2 * NORM_BOUND:
        raise Reject("insufficient CRT modulus")
    for prime, omega in moduli:
        table = np.empty((HALF, HALF), dtype=np.int64)
        root = omega
        step = omega * omega % prime
        for root_index in range(HALF):
            value = 1
            for exponent in range(HALF):
                table[root_index, exponent] = value
                value = value * root % prime
            root = root * step % prime
        for start in range(0, len(rows), batch_size):
            batch = rows[start : start + batch_size]
            exponents = np.asarray([row["exponents"] for row in batch], dtype=np.int64)
            signs = np.asarray([row["signs"] for row in batch], dtype=np.int64)
            values = np.zeros((HALF, len(batch)), dtype=np.int64)
            for term in range(WEIGHT):
                values += table[:, exponents[:, term]] * signs[:, term]
            values %= prime
            products = np.ones(len(batch), dtype=np.int64)
            for root_index in range(HALF):
                products = products * values[root_index] % prime
            expected = np.asarray([int(row["norm"]) % prime for row in batch], dtype=np.int64)
            if not np.array_equal(products, expected):
                raise Reject("modular resultant")
    return len(moduli)


def verify_payload(payload: object, expensive: bool = True) -> dict[str, int]:
    if not isinstance(payload, dict):
        raise Reject("payload type")
    expected_keys = {
        "class_count", "eligible_count", "enumeration_seconds", "full_candidate_count",
        "full_completed", "full_max_v2_below_cap", "full_worker_errors", "max_section_orbit",
        "max_v2_below_cap", "raw_count", "representatives", "sample_completed",
        "sample_requested", "schema", "section_count", "status", "worker_errors",
    }
    if set(payload) != expected_keys:
        raise Reject("payload schema")
    if (
        payload["schema"] != "dli-wcl-weight4-normalized-section-v1"
        or payload["status"] != "FULL_COMPLETE"
        or payload["raw_count"] != RAW_COUNT
        or payload["section_count"] != SECTION_COUNT
        or payload["class_count"] != CLASS_COUNT
        or payload["full_worker_errors"] != []
        or payload["worker_errors"] != []
    ):
        raise Reject("payload header")
    representatives = payload["representatives"]
    by_key = validate_representatives(representatives)
    completed = payload["full_completed"]
    if not isinstance(completed, list) or len(completed) != CLASS_COUNT:
        raise Reject("completed count")

    completed_by_key = {}
    roots: set[str] = set()
    factor_records = 0
    candidates = []
    max_v2 = 0
    for row in completed:
        required = {
            "eligible", "exponents", "factors", "key", "norm", "norm_bits",
            "section_orbit_size", "signs", "worker_seconds",
        }
        if not isinstance(row, dict) or set(row) != required:
            raise Reject("completed schema")
        key = row["key"]
        if key in completed_by_key or key not in by_key:
            raise Reject("completed key")
        completed_by_key[key] = row
        rep = by_key[key]
        for field in ("exponents", "signs", "section_orbit_size"):
            if row[field] != rep[field]:
                raise Reject("completed representative")
        norm = int(row["norm"])
        if (
            str(norm) != row["norm"]
            or not 0 < norm <= NORM_BOUND
            or row["norm_bits"] != norm.bit_length()
        ):
            raise Reject("norm metadata")
        factors = row["factors"]
        if not isinstance(factors, list):
            raise Reject("factor list")
        product = 1
        row_candidates = []
        row_roots = set()
        for factor in factors:
            if not isinstance(factor, dict) or set(factor) != {
                "bits", "exponent", "prime", "v2_prime_minus_1"
            }:
                raise Reject("factor schema")
            prime = int(factor["prime"])
            exponent = factor["exponent"]
            if (
                str(prime) != factor["prime"]
                or prime in row_roots
                or not isinstance(exponent, int)
                or isinstance(exponent, bool)
                or exponent <= 0
                or factor["bits"] != prime.bit_length()
                or factor["v2_prime_minus_1"] != valuation_two(prime - 1)
            ):
                raise Reject("factor metadata")
            row_roots.add(prime)
            roots.add(str(prime))
            factor_records += 1
            product *= prime**exponent
            if prime < CAP:
                max_v2 = max(max_v2, factor["v2_prime_minus_1"])
                if factor["v2_prime_minus_1"] >= AMBIENT_V2:
                    row_candidates.append(factor)
                    candidates.append(factor)
        if product != norm or row["eligible"] != row_candidates:
            raise Reject("factor reconstruction")
    if set(completed_by_key) != set(by_key):
        raise Reject("missing completed class")
    if factor_records != FACTOR_RECORDS or len(roots) != FACTOR_ROOTS:
        raise Reject("factor census")
    if payload["full_candidate_count"] != len(candidates) or candidates:
        raise Reject("ambient candidate")
    if payload["full_max_v2_below_cap"] != max_v2 or max_v2 != 29:
        raise Reject("splitting-depth maximum")

    section = max_orbit = moduli = 0
    if expensive:
        section, max_orbit = verify_section_partition(representatives)
        if payload["max_section_orbit"] != max_orbit:
            raise Reject("maximum normalized orbit")
        rows_for_norm = [completed_by_key[row["key"]] for row in representatives]
        moduli = verify_resultants(rows_for_norm)
    return {
        "section": section,
        "max_orbit": max_orbit,
        "moduli": moduli,
        "factor_records": factor_records,
        "factor_roots": len(roots),
        "max_v2": max_v2,
    }


def mutation_rejected(payload: dict[str, object], mutate, restore) -> bool:
    mutate()
    try:
        verify_payload(payload, expensive=False)
    except (Reject, KeyError, TypeError, ValueError):
        caught = True
    else:
        caught = False
    finally:
        restore()
    return caught


def main() -> None:
    with gzip.open(RESULT, "rt", encoding="utf-8") as handle:
        payload = json.load(handle)
    summary = verify_payload(payload)
    factor = payload["full_completed"][0]["factors"][0]
    representative = payload["representatives"][0]
    controls = (
        (lambda: payload.__setitem__("full_candidate_count", 1), lambda: payload.__setitem__("full_candidate_count", 0)),
        (lambda: payload.__setitem__("full_max_v2_below_cap", 28), lambda: payload.__setitem__("full_max_v2_below_cap", 29)),
        (lambda: factor.__setitem__("prime", "3"), lambda: factor.__setitem__("prime", "2")),
        (lambda: representative["exponents"].__setitem__(1, 3), lambda: representative["exponents"].__setitem__(1, 2)),
        (lambda: payload.__setitem__("class_count", CLASS_COUNT - 1), lambda: payload.__setitem__("class_count", CLASS_COUNT)),
    )
    caught = sum(mutation_rejected(payload, mutate, restore) for mutate, restore in controls)
    if caught != len(controls):
        raise AssertionError(f"negative controls caught {caught}/{len(controls)}")
    print(
        "DLI_WCL_WEIGHT4_LEDGER_PASS "
        f"classes={CLASS_COUNT} section={summary['section']} max_orbit={summary['max_orbit']} "
        f"crt_moduli={summary['moduli']} factor_records={summary['factor_records']} "
        f"factor_roots={summary['factor_roots']} max_v2={summary['max_v2']} "
        f"negative_controls={caught}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
