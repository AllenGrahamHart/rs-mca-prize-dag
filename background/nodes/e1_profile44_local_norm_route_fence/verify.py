#!/usr/bin/env python3
"""Verify the profile-(4,4) local-norm route fence."""

from collections import Counter
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = Path(__file__).resolve().parent
B_PRIZE = 317494674775468773183020924238786383963
VALUATIONS = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 17, 18, 20)
EXPECTED_BY_MU = {
    1: 533,
    2: 285,
    3: 155,
    4: 78,
    5: 42,
    6: 23,
    8: 4,
    9: 4,
    10: 3,
    12: 2,
    16: 1,
    17: 1,
    18: 1,
    20: 1,
}


def hasse_order(support: tuple[int, ...]) -> int:
    for derivative in range(32):
        parity = sum((derivative & ~residue) == 0 for residue in support) & 1
        if parity:
            return derivative
    raise AssertionError("nonempty degree-below-32 polynomial vanished")


def factor_odd(value: int) -> list[tuple[int, int]]:
    factors = []
    prime = 3
    while prime * prime <= value:
        if value % prime == 0:
            exponent = 0
            while value % prime == 0:
                value //= prime
                exponent += 1
            factors.append((prime, exponent))
        prime += 2
    if value > 1:
        factors.append((value, 1))
    return factors


def order_mod_256(value: int) -> int:
    residue = value % 256
    current = residue
    order = 1
    while current != 1:
        current = current * residue % 256
        order += 1
        assert order <= 64
    return order


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "None of the `1133`" in statement
    assert "cofactors is asserted to occur" in statement
    assert "method boundary" in proof

    orders = {}
    expected_orders = {
        2: {1, 2, 4, 8, 16},
        4: {1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 17, 18, 20, 24},
    }
    expected_counts = {
        2: {1: 256, 2: 128, 4: 64, 8: 32, 16: 16},
        4: {
            1: 17920,
            2: 8960,
            3: 4096,
            4: 2432,
            5: 1024,
            6: 512,
            8: 448,
            9: 256,
            10: 128,
            12: 64,
            17: 64,
            18: 32,
            20: 16,
            24: 8,
        },
    }
    for size in (2, 4):
        census = Counter(hasse_order(support) for support in combinations(range(32), size))
        assert set(census) == expected_orders[size]
        assert dict(census) == expected_counts[size]
        orders[size] = set(census)

    bound = 20**64 // (B_PRIZE * 2**128)
    assert bound == 1_707_433
    relevant = tuple(sorted((orders[2] | orders[4]) & set(range(21))))
    assert relevant == VALUATIONS

    before = 0
    survivors = []
    by_mu = Counter()
    for mu in VALUATIONS:
        odd = 1
        while (cofactor := (1 << mu) * odd) <= bound:
            before += 1
            factors = factor_odd(odd)
            if all(exponent % order_mod_256(prime) == 0 for prime, exponent in factors):
                survivors.append(cofactor)
                by_mu[mu] += 1
            odd += 256

    assert before == 6622
    assert len(survivors) == len(set(survivors)) == 1133
    assert dict(by_mu) == EXPECTED_BY_MU
    assert {(1 << mu) for mu in VALUATIONS} <= set(survivors)
    assert max(survivors) == 1_704_448

    residual = 515126704564295620156155116913120291239
    weight = 522452937039935372855706187881128712
    assert 2 * residual // weight == 1971
    assert 1971 // 256 == 7
    assert len(VALUATIONS) == 14 > 7
    print("E1_PROFILE44_LOCAL_NORM_ROUTE_FENCE_PASS")


if __name__ == "__main__":
    main()
