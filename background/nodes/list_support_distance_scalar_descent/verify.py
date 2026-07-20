#!/usr/bin/env python3
"""Verify support-distance scalar descent for Reed-Solomon lists."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "list_support_distance_scalar_descent"
CONSUMER = "rate_half_list_adjacent_crossing"


def projective_counts(q: int, degree: int) -> tuple[int, int]:
    assert q >= 2 and degree >= 1
    total = (q**degree - 1) // (q - 1)
    killed = (q ** (degree - 1) - 1) // (q - 1)
    return total, killed


def deployed_check() -> None:
    q = 2**31 - 1
    degree = 4
    n, k, agreement, size = 2**21, 2**20, 1_116_023, 2**24
    errors = n - agreement
    gap = agreement - k + 1
    total, killed = projective_counts(q, degree)
    left = size * errors * killed
    right = gap * total
    assert (errors, gap) == (981_129, 67_448)
    assert total == 9_903_520_305_059_670_166_633_185_280
    assert killed == 4_611_686_016_279_904_257
    assert left == 75_911_179_514_902_718_909_260_442_370_048
    assert right == 667_972_637_535_664_633_399_075_080_765_440
    assert right - left == 592_061_458_020_761_914_489_814_638_395_392
    assert q**4 // 2**100 == size - 1
    assert q * killed < total


Element = tuple[int, int]
Polynomial = tuple[Element, ...]


def add(left: Element, right: Element, q: int) -> Element:
    return ((left[0] + right[0]) % q, (left[1] + right[1]) % q)


def scale(value: Element, scalar: int, q: int) -> Element:
    return (scalar * value[0] % q, scalar * value[1] % q)


def evaluate(polynomial: Polynomial, point: int, q: int) -> Element:
    output = (0, 0)
    power = 1
    for coefficient in polynomial:
        output = add(output, scale(coefficient, power, q), q)
        power = power * point % q
    return output


def functional(value: Element, chart: tuple[int, int], q: int) -> int:
    return (chart[0] * value[0] + chart[1] * value[1]) % q


def tiny_exhaustive_check() -> tuple[int, int]:
    # GF(9)/GF(3) is used only as a two-dimensional GF(3) vector space;
    # evaluation points are in the base field, so extension multiplication is
    # not needed for this degree-one code.
    q, n, k, agreement = 3, 3, 2, 2
    elements = tuple(product(range(q), repeat=2))
    domain = tuple(range(n))
    polynomials = tuple(product(elements, repeat=k))
    words = {
        polynomial: tuple(evaluate(polynomial, point, q) for point in domain)
        for polynomial in polynomials
    }
    charts = ((1, 0), (1, 1), (1, 2), (0, 1))
    assert len(charts) == projective_counts(q, 2)[0]
    for value in elements[1:]:
        assert sum(functional(value, chart, q) == 0 for chart in charts) == 1

    max_extension = 0
    full_centers = 0
    saw_colliding_chart = False
    for center in product(elements, repeat=n):
        listed = [
            polynomial
            for polynomial, word in words.items()
            if sum(word[index] == center[index] for index in domain) >= agreement
        ]
        max_extension = max(max_extension, len(listed))
        if len(listed) < 3:
            continue
        full_centers += 1
        good = 0
        for chart in charts:
            projected = {
                tuple(functional(coefficient, chart, q) for coefficient in polynomial)
                for polynomial in listed
            }
            if len(projected) != len(listed):
                saw_colliding_chart = True
                continue
            projected_center = tuple(functional(value, chart, q) for value in center)
            for polynomial in projected:
                word = tuple(
                    sum(coefficient * point**index for index, coefficient in enumerate(polynomial)) % q
                    for point in domain
                )
                assert sum(word[index] == projected_center[index] for index in domain) >= agreement
            good += 1
        assert good >= 1

    base_elements = tuple(range(q))
    base_polynomials = tuple(product(base_elements, repeat=k))
    base_words = {
        polynomial: tuple(
            sum(coefficient * point**index for index, coefficient in enumerate(polynomial)) % q
            for point in domain
        )
        for polynomial in base_polynomials
    }
    max_base = 0
    for center in product(base_elements, repeat=n):
        size = sum(
            sum(word[index] == center[index] for index in domain) >= agreement
            for word in base_words.values()
        )
        max_base = max(max_base, size)

    total, killed = projective_counts(q, 2)
    errors, gap, size = n - agreement, agreement - k + 1, 3
    assert size * errors * killed < gap * total
    assert max_extension == max_base == 3
    assert full_centers > 0 and saw_colliding_chart
    return full_centers, max_extension


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text() for name in required if name.endswith(".md")
    )
    for marker in (
        "L t H_r < g N_r",
        "B_E(a)>=L  if and only if  B_F(a)>=L",
        "D subset F",
        "592061458020761914489814638395392",
        "target `2^-100`, not the",
        "No list upper bound or adjacent crossing is proved",
    ):
        assert marker in text


def main() -> None:
    deployed_check()
    centers, maximum = tiny_exhaustive_check()
    packet_check()
    print(
        "LIST_SUPPORT_DISTANCE_SCALAR_DESCENT_PASS "
        f"gf9_centers={centers} max_list={maximum} deployed_margin=592061458020761914489814638395392"
    )


if __name__ == "__main__":
    main()
