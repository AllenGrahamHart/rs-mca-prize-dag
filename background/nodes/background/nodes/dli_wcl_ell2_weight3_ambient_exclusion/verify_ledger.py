#!/usr/bin/env python3
"""Verify the ell=2 weight-3 section, norms, and factor ledger."""

from __future__ import annotations

import copy
import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "experiments/prize_resolution/dli_wcl_ell2_weight3_classes_result.json"
ORDER = 1024
HALF = 512
WEIGHT = 3
RAW_COUNT = math.comb(HALF, WEIGHT) * 2 ** (WEIGHT - 1)
SECTION_COUNT = 521_220
CLASS_COUNT = 510
FACTOR_RECORDS = 1_329
FACTOR_ROOTS = 1_141
NORM_BOUND = 3**512
CAP = 2**256


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


def encode(full_terms: tuple[int, ...] | list[int]) -> int:
    reduced = sorted((term % HALF, 1 if term < HALF else -1) for term in full_terms)
    if len(reduced) != WEIGHT or len({exponent for exponent, _ in reduced}) != WEIGHT:
        raise Reject("antipodal collision")
    if reduced[0][1] < 0:
        reduced = [(exponent, -sign) for exponent, sign in reduced]
    key = 0
    for index, (exponent, sign) in enumerate(reduced):
        key |= (exponent | ((sign < 0) << 9)) << (10 * index)
    return key


def normalized_orbit(exponents: list[int], signs: list[int]) -> set[int]:
    terms = tuple(
        exponent if sign > 0 else exponent + HALF
        for exponent, sign in zip(exponents, signs)
    )
    orbit = set()
    for dilation in range(1, ORDER, 2):
        dilated = tuple(dilation * term % ORDER for term in terms)
        for anchor in dilated:
            orbit.add(encode(tuple((term - anchor) % ORDER for term in dilated)))
    return orbit


def build_section() -> set[int]:
    section = set()
    for left, right in itertools.combinations(range(1, ORDER), 2):
        if left == HALF or right == HALF or (right - left) % ORDER == HALF:
            continue
        section.add(encode((0, left, right)))
    if len(section) != SECTION_COUNT:
        raise Reject("section count")
    return section


def split_moduli() -> list[tuple[int, int]]:
    moduli = []
    product = 1
    candidate = ((2**31 - 2) // ORDER) * ORDER + 1
    while product <= 2 * NORM_BOUND:
        if trial_prime(candidate):
            omega = next(
                (
                    pow(base, (candidate - 1) // ORDER, candidate)
                    for base in range(2, 1000)
                    if pow(
                        pow(base, (candidate - 1) // ORDER, candidate), HALF, candidate
                    )
                    == candidate - 1
                ),
                None,
            )
            if omega is None or pow(omega, ORDER, candidate) != 1:
                raise Reject("split root")
            moduli.append((candidate, omega))
            product *= candidate
        candidate -= ORDER
    return moduli


def verify_resultants(rows: list[dict[str, object]]) -> int:
    moduli = split_moduli()
    if math.prod(prime for prime, _ in moduli) <= 2 * NORM_BOUND:
        raise Reject("CRT modulus")
    for prime, omega in moduli:
        roots = []
        root = omega
        step = omega * omega % prime
        for _ in range(HALF):
            roots.append(root)
            root = root * step % prime
        powers = [[1] * HALF for _ in range(HALF)]
        for index, root in enumerate(roots):
            for exponent in range(1, HALF):
                powers[exponent][index] = powers[exponent - 1][index] * root % prime
        for row in rows:
            resultant = 1
            exponents = row["exponents"]
            signs = row["signs"]
            for index in range(HALF):
                value = sum(
                    sign * powers[exponent][index]
                    for exponent, sign in zip(exponents, signs)
                ) % prime
                resultant = resultant * value % prime
            if resultant != int(row["norm"]) % prime:
                raise Reject("modular resultant")
    return len(moduli)


def verify_payload(payload: object, expensive: bool = True) -> dict[str, int]:
    if not isinstance(payload, dict) or set(payload) != {
        "candidate_count", "class_count", "completed", "max_v2_below_cap",
        "raw_count", "representatives", "schema", "section_count", "status",
        "worker_errors"
    }:
        raise Reject("payload schema")
    if (
        payload["schema"] != "dli-wcl-ell2-weight3-affine-galois-v1"
        or payload["status"] != "COMPLETE"
        or payload["raw_count"] != RAW_COUNT
        or payload["section_count"] != SECTION_COUNT
        or payload["class_count"] != CLASS_COUNT
        or payload["candidate_count"] != 0
        or payload["max_v2_below_cap"] != 21
        or payload["worker_errors"] != []
    ):
        raise Reject("payload header")
    representatives = payload["representatives"]
    completed = payload["completed"]
    if not isinstance(representatives, list) or not isinstance(completed, list):
        raise Reject("class lists")
    if len(representatives) != CLASS_COUNT or len(completed) != CLASS_COUNT:
        raise Reject("class count")

    reps_by_key = {}
    for row in representatives:
        if not isinstance(row, dict) or set(row) != {"exponents", "key", "signs"}:
            raise Reject("representative schema")
        exponents = row["exponents"]
        signs = row["signs"]
        if (
            not isinstance(exponents, list) or not isinstance(signs, list)
            or len(exponents) != WEIGHT or len(signs) != WEIGHT
            or exponents != sorted(exponents) or len(set(exponents)) != WEIGHT
            or exponents[0] != 0
            or any(not isinstance(value, int) or isinstance(value, bool) or not 0 <= value < HALF for value in exponents)
            or any(sign not in (-1, 1) for sign in signs) or signs[0] != 1
        ):
            raise Reject("representative")
        full = tuple(
            exponent if sign > 0 else exponent + HALF
            for exponent, sign in zip(exponents, signs)
        )
        key = row["key"]
        if not isinstance(key, int) or isinstance(key, bool) or key != encode(full) or key in reps_by_key:
            raise Reject("representative key")
        reps_by_key[key] = row

    roots = set()
    completed_keys = set()
    factor_records = 0
    max_v2 = 0
    for row in completed:
        if not isinstance(row, dict) or set(row) != {
            "ambient_candidates", "exponents", "factors", "key", "norm",
            "norm_bits", "signs"
        }:
            raise Reject("completed schema")
        key = row["key"]
        if key in completed_keys or key not in reps_by_key:
            raise Reject("completed key")
        completed_keys.add(key)
        rep = reps_by_key[key]
        if row["exponents"] != rep["exponents"] or row["signs"] != rep["signs"]:
            raise Reject("completed representative")
        norm = int(row["norm"])
        if str(norm) != row["norm"] or not 0 < norm <= NORM_BOUND or row["norm_bits"] != norm.bit_length():
            raise Reject("norm")
        factors = row["factors"]
        if not isinstance(factors, list):
            raise Reject("factor list")
        product = 1
        row_candidates = []
        row_primes = set()
        for factor in factors:
            if not isinstance(factor, dict) or set(factor) != {
                "bits", "exponent", "prime", "v2_prime_minus_1"
            }:
                raise Reject("factor schema")
            prime = int(factor["prime"])
            exponent = factor["exponent"]
            if (
                str(prime) != factor["prime"] or prime in row_primes
                or not isinstance(exponent, int) or isinstance(exponent, bool) or exponent <= 0
                or factor["bits"] != prime.bit_length()
                or factor["v2_prime_minus_1"] != valuation_two(prime - 1)
            ):
                raise Reject("factor")
            row_primes.add(prime)
            roots.add(factor["prime"])
            factor_records += 1
            product *= prime**exponent
            if prime < CAP:
                max_v2 = max(max_v2, factor["v2_prime_minus_1"])
                if factor["v2_prime_minus_1"] >= 41:
                    row_candidates.append(factor)
        if product != norm or row["ambient_candidates"] != row_candidates or row_candidates:
            raise Reject("factor reconstruction")
    if completed_keys != set(reps_by_key):
        raise Reject("completed coverage")
    if factor_records != FACTOR_RECORDS or len(roots) != FACTOR_ROOTS or max_v2 != 21:
        raise Reject("factor census")

    section_size = classes = moduli = 0
    if expensive:
        section = build_section()
        seen = set()
        for row in representatives:
            orbit = normalized_orbit(row["exponents"], row["signs"])
            if not orbit <= section or seen & orbit:
                raise Reject("section orbit partition")
            seen.update(orbit)
        if seen != section:
            raise Reject("section coverage")
        section_size = len(section)
        classes = len(representatives)
        moduli = verify_resultants(completed)
    return {
        "section": section_size,
        "classes": classes,
        "moduli": moduli,
        "factor_records": factor_records,
        "factor_roots": len(roots),
        "max_v2": max_v2,
    }


def main() -> None:
    payload = json.loads(RESULT.read_text())
    summary = verify_payload(payload)
    factor_row = next(
        index for index, row in enumerate(payload["completed"]) if row["factors"]
    )
    mutators = (
        lambda item: item.__setitem__("candidate_count", 1),
        lambda item: item.__setitem__("section_count", SECTION_COUNT - 1),
        lambda item: item["representatives"][0]["exponents"].__setitem__(0, 1),
        lambda item: item["completed"][factor_row]["factors"][0].__setitem__("exponent", 2),
        lambda item: item.__setitem__("max_v2_below_cap", 20),
    )
    caught = 0
    for mutate in mutators:
        altered = copy.deepcopy(payload)
        mutate(altered)
        try:
            verify_payload(altered, expensive=False)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    if caught != len(mutators):
        raise AssertionError(f"negative controls caught {caught}/{len(mutators)}")
    print(
        "DLI_WCL_ELL2_WEIGHT3_LEDGER_PASS "
        f"section={summary['section']} classes={summary['classes']} "
        f"crt_moduli={summary['moduli']} factor_records={summary['factor_records']} "
        f"factor_roots={summary['factor_roots']} max_v2={summary['max_v2']} "
        f"negative_controls={caught}/{len(mutators)}"
    )


if __name__ == "__main__":
    main()
