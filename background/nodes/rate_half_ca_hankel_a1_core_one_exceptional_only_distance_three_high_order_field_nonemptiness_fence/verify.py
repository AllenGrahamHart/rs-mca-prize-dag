#!/usr/bin/env python3
"""Lucas certificates for both distance-three high-order field strata."""

from __future__ import annotations

from functools import cache
from math import gcd, isqrt


Certificate = tuple[dict[int, int], dict[int, int]]


CERTIFICATES: dict[int, Certificate] = {
    1013: ({2: 2, 11: 1, 23: 1}, {2: 2, 11: 3, 23: 2}),
    1531: ({2: 1, 3: 2, 5: 1, 17: 1}, {2: 2, 3: 2, 5: 2, 17: 2}),
    2027: ({2: 1, 1013: 1}, {2: 2, 1013: 2}),
    3391: ({2: 1, 3: 1, 5: 1, 113: 1}, {2: 3, 3: 3, 5: 3, 113: 2}),
    3581: ({2: 2, 5: 1, 179: 1}, {2: 2, 5: 2, 179: 2}),
    3613: ({2: 2, 3: 1, 7: 1, 43: 1}, {2: 2, 3: 2, 7: 2, 43: 2}),
    9187: ({2: 1, 3: 1, 1531: 1}, {2: 2, 3: 3, 1531: 2}),
    21487: ({2: 1, 3: 1, 3581: 1}, {2: 3, 3: 3, 3581: 2}),
    33911: ({2: 1, 5: 1, 3391: 1}, {2: 11, 5: 2, 3391: 2}),
    174763: ({2: 1, 3: 2, 7: 1, 19: 1, 73: 1}, {2: 2, 3: 11, 7: 3, 19: 2, 73: 3}),
    224209: ({2: 4, 3: 4, 173: 1}, {2: 7, 3: 2, 173: 2}),
    524287: ({2: 1, 3: 3, 7: 1, 19: 1, 73: 1}, {2: 3, 3: 3, 7: 3, 19: 2, 73: 3}),
    20178811: ({2: 1, 3: 2, 5: 1, 224209: 1}, {2: 2, 3: 2, 5: 2, 224209: 2}),
    7506517693: ({2: 2, 3: 1, 31: 1, 20178811: 1}, {2: 2, 3: 3, 31: 2, 20178811: 2}),
    138945979217: ({2: 4, 11: 1, 353: 1, 619: 1, 3613: 1}, {2: 3, 11: 2, 353: 2, 619: 2, 3613: 2}),
    3612595459643: ({2: 1, 13: 1, 138945979217: 1}, {2: 2, 13: 2, 138945979217: 2}),
    14833675282790944213: (
        {2: 2, 3: 1, 137: 1, 593: 1, 2027: 1, 7506517693: 1},
        {2: 2, 3: 2, 137: 2, 593: 2, 2027: 2, 7506517693: 2},
    ),
    1661926226357084884519: (
        {2: 1, 3: 1, 7: 1, 17: 1, 19: 1, 33911: 1, 3612595459643: 1},
        {2: 3, 3: 2, 7: 2, 17: 2, 19: 2, 33911: 2, 3612595459643: 2},
    ),
    187072209578695855896992631304045809902474217127937: (
        {2: 42, 13: 1, 174763: 1, 524287: 1, 21487: 1, 1661926226357084884519: 1},
        {2: 3, 13: 2, 174763: 2, 524287: 2, 21487: 2, 1661926226357084884519: 2},
    ),
    187072209578695855896992636341236724945103917940737: (
        {2: 41, 3: 2, 757: 1, 174763: 1, 9187: 1, 524287: 1, 14833675282790944213: 1},
        {2: 5, 3: 2, 757: 2, 174763: 2, 9187: 2, 524287: 2, 14833675282790944213: 2},
    ),
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def trial_prime(number: int) -> bool:
    if number < 2:
        return False
    return all(number % divisor for divisor in range(2, isqrt(number) + 1))


@cache
def verify_prime(number: int) -> bool:
    if number <= 1000:
        return trial_prime(number)
    if number not in CERTIFICATES:
        return False

    factors, witnesses = CERTIFICATES[number]
    product = 1
    for prime, exponent in factors.items():
        if not verify_prime(prime):
            return False
        product *= prime**exponent
    if product != number - 1 or witnesses.keys() != factors.keys():
        return False

    for prime, witness in witnesses.items():
        if pow(witness, number - 1, number) != 1:
            return False
        if gcd(pow(witness, (number - 1) // prime, number) - 1, number) != 1:
            return False
    return True


def main() -> None:
    n = 1 << 41
    e = (1 << 38) - 1
    r = (1 << 39) - 1
    budget = (1 << 39) + 1
    primes = {
        e // 3: 187072209578695855896992631304045809902474217127937,
        e: 187072209578695855896992636341236724945103917940737,
    }

    for expected_gcd, prime in primes.items():
        require(verify_prime(prime), f"Lucas certificate failed for {prime}")
        require(prime // (1 << 128) == budget, "prime is outside the adjacent-row interval")
        require((prime - 1) % n == 0, "smooth-domain order does not divide p-1")
        require(gcd(e, prime - 1) == expected_gcd, "wrong field-order gcd")
        require(gcd(r, prime - 1) == 1, "dual residue gate is not automatic")

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_DISTANCE_THREE_"
        "HIGH_ORDER_FIELD_NONEMPTINESS_FENCE_PASS "
        f"certified_primes={len(primes)} certificate_nodes={len(CERTIFICATES)}"
    )


if __name__ == "__main__":
    main()
