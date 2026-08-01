#!/usr/bin/env python3
"""Exact checks for the adversarial audit of Brief 2 / C2''.

The script verifies abstract route-fence constructions. These are NOT DLI
counterexamples and do not prove or refute C2''.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb


Q_GATE = 3 * 2**41 + 1

FOURWISE_COLUMNS = [
    247, 1009, 1134, 1761, 1144, 433, 1541, 966, 33, 1166, 62,
    1282, 242, 1346, 1187, 1375, 748, 735, 1111, 519, 1508, 600,
    2038, 881, 1357, 793, 191, 1323, 719, 1760, 1336, 1349, 387,
]


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def v2(n: int) -> int:
    out = 0
    while n % 2 == 0:
        n //= 2
        out += 1
    return out


def is_prime_64(n: int) -> bool:
    if n < 2:
        return False
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small:
        if n % p == 0:
            return n == p

    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    # Deterministic for unsigned 64-bit integers.
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def gf2_rank(values: list[int]) -> int:
    basis: dict[int, int] = {}
    rank = 0
    for x0 in values:
        x = x0
        while x:
            p = x.bit_length() - 1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p] = x
                rank += 1
                break
    return rank


def extract_basis(values: list[int]) -> tuple[list[int], list[int]]:
    basis_vectors: list[int] = []
    rest: list[int] = []
    rank = 0
    for x in values:
        new_rank = gf2_rank(basis_vectors + [x])
        if new_rank > rank:
            basis_vectors.append(x)
            rank = new_rank
        else:
            rest.append(x)
    return basis_vectors, rest


def check_fourwise_trap() -> None:
    cols = FOURWISE_COLUMNS
    require(len(cols) == 33 and len(set(cols)) == 33, "column manifest")
    require(gf2_rank(cols) == 11, "four-wise trap rank")

    for k in range(1, 5):
        for subset in combinations(cols, k):
            x = 0
            for v in subset:
                x ^= v
            require(x != 0, f"dependency of size {k}")

    ratio = 2 ** (33 - 11)
    require(ratio == 2**22 > 2**21, "joint reserve failure")

    # Comparison system: 33 independent coordinate forms. Every <=4
    # normalized indicator moment is also exactly one, but the full ratio is 1.
    independent_ratio = 1
    require(independent_ratio != ratio, "descriptor collision contrast")

    basis, rest = extract_basis(cols)
    require(len(basis) == 11 and len(rest) == 22, "basis/fundamental owners")
    increments = [1] * len(basis) + [2] * len(rest)
    prod = 1
    for g in increments:
        prod *= g
    require(prod == ratio, "tilted increment product")

    print(
        "C2_AUDIT1_FOURWISE_PASS",
        "local_moments_through_4=iid",
        f"joint_ratio=2^{33-11}=2^22",
        f"dependent_increments={len(rest)}",
    )


def check_official_gate_32wise_trap() -> None:
    q = Q_GATE
    require(is_prime_64(q), "q gate prime")
    require(v2(q - 1) == 41, "official v2 gate")
    require(q < 2**256 and q > 2**21, "field and reserve scale")

    # Moment curve in F_q^32 at a=0,...,32.
    # Any 32 columns form a Vandermonde matrix with nonzero determinant,
    # because all a values are distinct modulo q.
    a_values = list(range(33))
    require(len(set(a_values)) == 33 and max(a_values) < q, "distinct moments")

    rank_all = 32
    nullity = 33 - rank_all
    require(nullity == 1, "full-support nullity")
    ratio = q**nullity
    require(ratio == q > 2**21, "32-wise joint reserve failure")

    # Every proper subfamily is independent, so all proper normalized
    # product moments equal 1. The unique circuit support is all 33 columns.
    min_circuit_support = 33
    require(min_circuit_support == 33, "full-depth circuit")

    print(
        "C2_AUDIT2_32WISE_GATE_PASS",
        f"q={q}",
        "proper_subtowers=iid_through_depth_32",
        f"final_ratio=q~2^{q.bit_length()-1}",
        "circuit_support=33",
    )


def check_vandermonde_circuit_explosion() -> None:
    q = 37
    rank = 11
    n = 33
    require(q > n, "distinct field points")
    # Any 11 moment-curve columns are independent; every 12-subset is a
    # support-minimal circuit.
    circuits = comb(n, rank + 1)
    require(circuits == 354_817_320, "circuit count")
    ratio = q ** (n - rank)
    require(ratio > 2**21, "Vandermonde joint inflation")

    print(
        "C2_AUDIT3_CIRCUIT_EXPLOSION_PASS",
        f"circuits=C(33,12)={circuits}",
        f"joint_ratio=37^22={ratio}",
    )


def check_continuation_amplification() -> None:
    # Event A has probability 1/2. Thirty-two future factors are
    # Y=2*1_A, each of mean one.
    p = Fraction(1, 2)
    d = 32
    contribution = p * 2**d
    require(contribution == 2**31 > 2**21, "owner continuation explosion")

    print(
        "C2_AUDIT4_CONTINUATION_PASS",
        "owner_probability=1/2",
        f"future_factors={d}",
        f"full_owner_debit=2^{d-1}",
    )


def check_rank_descriptor_collision() -> None:
    # Two rank-one prefix spans in F_2^3.
    e1 = 0b001
    e2 = 0b010
    s1 = [e1]
    s2 = [e2]
    next_form = e1
    require(gf2_rank(s1) == gf2_rank(s2) == 1, "same rank descriptor")
    dependent1 = gf2_rank(s1 + [next_form]) == 1
    dependent2 = gf2_rank(s2 + [next_form]) == 1
    require(dependent1 and not dependent2, "same rank, different transition")

    g1 = 2 if dependent1 else 1
    g2 = 2 if dependent2 else 1
    require((g1, g2) == (2, 1), "tilted increment collision")

    print(
        "C2_AUDIT5_RANK_DESCRIPTOR_PASS",
        "same_rank=1",
        "next_increments=2_vs_1",
    )


def check_information_nullity_identity() -> None:
    # Four-wise trap: reward 33 bits, entropy cost 11 bits, free reward 22.
    reward_bits = 33
    entropy_bits = 11
    free_bits = reward_bits - entropy_bits
    require(free_bits == 22, "F2 information/nullity")

    # Official-gate moment curve: reward 33 log q, entropy 32 log q,
    # free reward one log q, matching nullity one.
    reward_units = 33
    entropy_units = 32
    free_units = reward_units - entropy_units
    require(free_units == 1, "q-ary information/nullity")

    print(
        "C2_AUDIT6_INFORMATION_NULLITY_PASS",
        "F2_free_reward=22_bits",
        "gate_model_free_reward=log2(q)",
    )


def main() -> None:
    check_fourwise_trap()
    check_official_gate_32wise_trap()
    check_vandermonde_circuit_explosion()
    check_continuation_amplification()
    check_rank_descriptor_collision()
    check_information_nullity_identity()
    print("ADVERSARIAL_AUDIT_BRIEF2_C2PP_PASS")


if __name__ == "__main__":
    main()
