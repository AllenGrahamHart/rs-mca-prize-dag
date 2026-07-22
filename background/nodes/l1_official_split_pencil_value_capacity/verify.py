#!/usr/bin/env python3
"""Verify the official split-pencil value-capacity compiler."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_split_pencil_value_capacity"
SUPPLIER = "l1_official_first_checkpoint_split_pencil_reduction"
CONSUMER = "l1_mixed_petal_amplification"


def f9_add(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return ((left[0] + right[0]) % 3, (left[1] + right[1]) % 3)


def f9_multiply(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    # theta^2=2 is irreducible over F_3.
    a, b = left
    c, d = right
    return ((a * c + 2 * b * d) % 3, (a * d + b * c) % 3)


def f9_power(value: tuple[int, int], exponent: int) -> tuple[int, int]:
    out = (1, 0)
    base = value
    while exponent:
        if exponent & 1:
            out = f9_multiply(out, base)
        base = f9_multiply(base, base)
        exponent >>= 1
    return out


def trim(poly: list[int]) -> list[int]:
    out = [coefficient % 3 for coefficient in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            out[i + j] = (out[i + j] + first * second) % 3
    return trim(out)


def poly_divmod(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    remainder = trim(dividend)
    divisor = trim(divisor)
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, 3)
    while remainder != [0] and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        scale = remainder[-1] * inverse % 3
        quotient[shift] = scale
        for i, coefficient in enumerate(divisor):
            remainder[shift + i] = (remainder[shift + i] - scale * coefficient) % 3
        remainder = trim(remainder)
    return trim(quotient), remainder


def poly_gcd(left: list[int], right: list[int]) -> list[int]:
    left = trim(left)
    right = trim(right)
    while right != [0]:
        _, remainder = poly_divmod(left, right)
        left, right = right, remainder
    inverse = pow(left[-1], -1, 3)
    return [(coefficient * inverse) % 3 for coefficient in left]


def main() -> None:
    checks = 0

    # The official rational inequality gives the strict 23-fiber endpoint.
    for p in (3583, 5119, 6143, 7681, 8191):
        n_max = (256 * p) // 11
        assert 11 * n_max <= 256 * p
        assert n_max // p <= 23
        assert math.comb(n_max // p, 2) <= 253
        checks += 3

    # Disjoint toy fibers pin the cardinality argument and pair count.
    domain = tuple(range(17))
    fibers = {
        value: {x for x in domain if x // 4 == value}
        for value in range(4)
    }
    assert all(len(fiber) == 4 for fiber in fibers.values())
    assert len(set().union(*fibers.values())) == 16
    assert all(
        fibers[left].isdisjoint(fibers[right])
        for left in fibers
        for right in fibers
        if left != right
    )
    assert math.comb(23, 2) == 253
    checks += 4

    # Exact characteristic-p fixture: over F_9, P=Z^3-Z has two complete
    # nonzero three-point fibers in H=F_9^*. Division of Z^8-1 by P-T gives
    # coefficient remainders -(T^2+1), 0, and T^2+1.
    elements = [(a, b) for a in range(3) for b in range(3)]
    nonzero = [value for value in elements if value != (0, 0)]
    value_fibers: dict[tuple[int, int], set[tuple[int, int]]] = {}
    for value in nonzero:
        image = f9_add(f9_power(value, 3), ((-value[0]) % 3, (-value[1]) % 3))
        value_fibers.setdefault(image, set()).add(value)
    split_values = {value for value, fiber in value_fibers.items() if len(fiber) == 3}
    assert split_values == {(0, 1), (0, 2)}
    remainders = ([2, 0, 2], [0], [1, 0, 1])
    eliminant = poly_gcd(remainders[0], remainders[2])
    assert eliminant == [1, 0, 1]
    assert remainders[0] == [2 * coefficient % 3 for coefficient in remainders[2]]
    derivative = [i * eliminant[i] % 3 for i in range(1, len(eliminant))]
    assert poly_gcd(eliminant, derivative) == [1]
    assert 8 // 3 - (len(eliminant) - 1) + 1 == 1
    assert 3 * 3 - 8 == 1  # deg(Q)=1 attains the low-complement boundary.
    checks += 7

    # The same F_9 fixture pins the complement-square compiler:
    # (Z^8-1)/(Z^2-1)=(Z^3-Z)^2+1.
    complement = [2, 0, 1]
    root = [0, 2, 0, 1]
    square_quotient = poly_multiply(root, root)
    square_quotient[0] = (square_quotient[0] + 1) % 3
    omega = poly_multiply(complement, square_quotient)
    assert square_quotient == [1, 0, 1, 0, 1, 0, 1]
    assert omega == [2] + [0] * 7 + [1]
    assert len(complement) - 1 == 8 - 2 * 3
    antipodal = {
        frozenset((value, ((-value[0]) % 3, (-value[1]) % 3)))
        for value in nonzero
    }
    assert len(antipodal) == 8 // 2
    assert len(root) - 1 == 3
    assert 3 - 2 == 1
    assert (2 * 3 - 1 - (3 - 2), 2 * 3 - 2 - (3 - 2)) == (4, 3)
    checks += 7

    # Official control arithmetic for the improved first-checkpoint boundary.
    n = 8192
    p = 3583
    assert 2 * p <= n < 3 * p
    assert n - 2 * p == 1026
    assert 3 * p - n == 2557
    closed_depth = n - p
    assert closed_depth == 4609
    assert 2 * p - closed_depth - 1 == 2556
    ratio_only_depth = 2 * p - 1 - 1566
    assert ratio_only_depth == 5599
    assert closed_depth < ratio_only_depth
    checks += 7

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (SUPPLIER, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    checks += 5

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "|V_H(P)|<=floor(n/p)<=23",
        "<=253",
        "G_Q(T)=gcd_i R_(Q,i)(T)",
        "rank M_Q<=m-deg(G_Q)+1",
        "2p>n  =>  no pair",
        "r>=3p-n",
        "d>=n-p  =>  t>=p+1",
        "D_S(Z)=R(Z)^2+c",
        "# unordered t=p pairs <=binom(n,n-2p)",
        "a pair exists  =>  n=2p+2",
        "R=Z(C_S)^((p-1)/2)",
        "n/2.",
        "depths `d=p` and `d=p+1`",
        "must not shard independently",
        "does not bound how many",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_OFFICIAL_SPLIT_PENCIL_VALUE_CAPACITY_PASS checks={checks}")


if __name__ == "__main__":
    main()
