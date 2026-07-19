#!/usr/bin/env python3
"""Verify the exact factor ledger and recursive Pocklington certificate."""

from __future__ import annotations

import copy
import json
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "experiments/prize_resolution/dli_wcl_engineered_norm_result.json"
EXPECTED_Q = 61156209198655289707609620063727948198186060921658038067621917786894060626433
EXPECTED_NORM = 2 * EXPECTED_Q
EXPECTED_SUPPORT = [[0, 1], [33, -1], [40, 1], [136, -1], [143, -1], [145, 1]]


class Reject(ValueError):
    pass


def trial_prime(value: int) -> bool:
    return value >= 2 and all(value % divisor for divisor in range(2, isqrt(value) + 1))


def verify_pocklington(certificate: object) -> int:
    if not isinstance(certificate, dict) or set(certificate) != {"root", "nodes"}:
        raise Reject("certificate schema")
    root = int(certificate["root"])
    nodes = certificate["nodes"]
    if not isinstance(nodes, dict) or str(root) not in nodes:
        raise Reject("certificate root")
    verified: set[int] = set()

    def visit(value: int) -> None:
        if value in verified:
            return
        node = nodes.get(str(value))
        if not isinstance(node, dict):
            raise Reject("missing certificate node")
        if node == {"method": "trial"}:
            if value >= 10_000 or not trial_prime(value):
                raise Reject("invalid trial leaf")
            verified.add(value)
            return
        if set(node) != {"method", "minus_one_factors", "witnesses"} or node["method"] != "pocklington":
            raise Reject("invalid Pocklington node")
        factors = node["minus_one_factors"]
        witnesses = node["witnesses"]
        if not isinstance(factors, list) or not isinstance(witnesses, dict):
            raise Reject("invalid factor payload")
        product = 1
        distinct: set[int] = set()
        for pair in factors:
            if not isinstance(pair, list) or len(pair) != 2:
                raise Reject("invalid factor pair")
            prime, exponent = int(pair[0]), pair[1]
            if not isinstance(exponent, int) or isinstance(exponent, bool) or exponent <= 0:
                raise Reject("invalid exponent")
            visit(prime)
            product *= prime**exponent
            distinct.add(prime)
        if product != value - 1 or product <= isqrt(value):
            raise Reject("incomplete Pocklington factorization")
        if set(witnesses) != {str(prime) for prime in distinct}:
            raise Reject("witness keys")
        for prime in distinct:
            base = witnesses[str(prime)]
            if not isinstance(base, int) or isinstance(base, bool):
                raise Reject("invalid witness")
            if pow(base, value - 1, value) != 1:
                raise Reject("Fermat condition")
            if gcd(pow(base, (value - 1) // prime, value) - 1, value) != 1:
                raise Reject("Pocklington gcd condition")
        verified.add(value)

    visit(root)
    return root


def verify_record(record: object) -> tuple[int, int]:
    if not isinstance(record, dict):
        raise Reject("record type")
    if record.get("order") != 512 or record.get("support") != EXPECTED_SUPPORT:
        raise Reject("polynomial pin")
    norm = int(record.get("norm", 0))
    if norm != EXPECTED_NORM or record.get("norm_bits") != norm.bit_length():
        raise Reject("norm pin")
    factors = record.get("factors")
    if not isinstance(factors, list) or len(factors) != 2:
        raise Reject("norm factor count")
    product = 1
    primes = []
    for factor in factors:
        prime = int(factor["prime"])
        exponent = factor["exponent"]
        product *= prime**exponent
        primes.append(prime)
    if product != norm or sorted(primes) != [2, EXPECTED_Q]:
        raise Reject("norm reconstruction")
    q = verify_pocklington(record.get("large_factor_pocklington"))
    if q != EXPECTED_Q:
        raise Reject("large factor mismatch")

    minus_one = record.get("large_factor_minus_one_factors")
    reconstruction = 1
    for prime_text, exponent in minus_one:
        reconstruction *= int(prime_text) ** exponent
    if reconstruction != q - 1:
        raise Reject("q-1 reconstruction")
    lowbit = (q - 1) & -(q - 1)
    v2 = lowbit.bit_length() - 1
    if v2 != 9 or (q - 1) % 512 or (q - 1) % 2**41 == 0:
        raise Reject("splitting depth")
    if record.get("ambient_factor_count") != 0:
        raise Reject("ambient count")

    prime_divisors = {int(pair[0]) for pair in minus_one}
    generator = next(
        candidate
        for candidate in range(2, 100)
        if all(pow(candidate, (q - 1) // divisor, q) != 1 for divisor in prime_divisors)
    )
    omega = pow(generator, (q - 1) // 512, q)
    if pow(omega, 512, q) != 1 or pow(omega, 256, q) != q - 1:
        raise Reject("terminal root order")
    dilation = next(
        (
            candidate
            for candidate in range(1, 512, 2)
            if sum(
                sign * pow(omega, (candidate * exponent) % 512, q)
                for exponent, sign in EXPECTED_SUPPORT
            )
            % q
            == 0
        ),
        None,
    )
    if dilation is None:
        raise Reject("terminal relation")
    return generator, dilation, v2


def rejected(record: dict) -> bool:
    try:
        verify_record(record)
    except (Reject, KeyError, TypeError, ValueError, StopIteration):
        return True
    return False


def main() -> None:
    record = json.loads(RESULT.read_text())
    generator, dilation, v2 = verify_record(record)
    mutations = []
    for mutate in (
        lambda item: item.__setitem__("norm", str(EXPECTED_NORM + 2)),
        lambda item: item.__setitem__("ambient_factor_count", 1),
        lambda item: item["factors"][1].__setitem__("prime", str(EXPECTED_Q + 2)),
        lambda item: item["large_factor_pocklington"]["nodes"][str(EXPECTED_Q)]["witnesses"].__setitem__("2", 2),
        lambda item: item["support"][1].__setitem__(0, 34),
    ):
        candidate = copy.deepcopy(record)
        mutate(candidate)
        mutations.append(candidate)
    caught = sum(rejected(candidate) for candidate in mutations)
    if caught != len(mutations):
        raise AssertionError(f"negative controls caught {caught}/{len(mutations)}")
    print(
        "DLI_WCL_ENGINEERED_SCOPE_PASS "
        f"norm_bits={EXPECTED_NORM.bit_length()} q_bits={EXPECTED_Q.bit_length()} "
        f"generator={generator} dilation={dilation} v2(q-1)={v2} "
        f"negative_controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
