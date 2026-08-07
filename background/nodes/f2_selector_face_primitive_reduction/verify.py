#!/usr/bin/env python3
"""Exact small-field replay for the selector-face primitive reduction."""

from __future__ import annotations

import itertools
import json
import math
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f2_selector_face_primitive_reduction"
CHECKS = 0
CASES = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def poly_from_roots(roots: tuple[int, ...], prime: int) -> tuple[int, ...]:
    coeffs = [1]
    for root in roots:
        out = [0] * (len(coeffs) + 1)
        for index, coeff in enumerate(coeffs):
            out[index] = (out[index] - root * coeff) % prime
            out[index + 1] = (out[index + 1] + coeff) % prime
        coeffs = out
    return tuple(coeffs)


def multiply(left: tuple[int, ...], right: tuple[int, ...], prime: int) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return tuple(out)


def top_prefix(poly: tuple[int, ...], depth: int) -> tuple[int, ...]:
    degree = len(poly) - 1
    return tuple(poly[degree - index] for index in range(1, min(depth, degree) + 1))


def selector(word: tuple[int, ...], theta: int, prime: int) -> tuple[int, ...]:
    roots = []
    for index, bit in enumerate(word):
        root = pow(theta, index, prime)
        roots.append(root if bit else (-root) % prime)
    return tuple(roots)


def syndrome(word: tuple[int, ...], theta: int, prime: int, rank: int) -> tuple[int, ...]:
    return tuple(
        sum(bit * pow(theta, index * (2 * row + 1), prime) for index, bit in enumerate(word)) % prime
        for row in range(rank)
    )


def shifted(support: frozenset[int], multiplier: int, prime: int) -> frozenset[int]:
    return frozenset(multiplier * value % prime for value in support)


def replay(prime: int, m: int, rank: int) -> None:
    global CASES
    CASES += 1
    generator = 3
    check(pow(generator, prime - 1, prime) == 1, "bad field generator candidate")
    theta = pow(generator, (prime - 1) // (2 * m), prime)
    check(pow(theta, 2 * m, prime) == 1 and pow(theta, m, prime) == prime - 1, "theta order")
    check(prime > 2 * rank, "Newton characteristic gate")

    fibers: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for word in itertools.product((0, 1), repeat=m):
        fibers[syndrome(word, theta, prime, rank)].append(word)

    domain = tuple(pow(theta, exponent, prime) for exponent in range(2 * m))
    check(len(set(domain)) == 2 * m, "cyclic domain size")

    for fiber in fibers.values():
        fixed = tuple(index for index in range(m) if len({word[index] for word in fiber}) == 1)
        common_roots = tuple(selector(fiber[0], theta, prime)[index] for index in fixed)
        g_poly = poly_from_roots(common_roots, prime)
        residual_polys = []
        residual_supports = []

        for word in fiber:
            roots = selector(word, theta, prime)
            l_poly = poly_from_roots(roots, prime)
            q_roots = tuple(root for index, root in enumerate(roots) if index not in fixed)
            q_poly = poly_from_roots(q_roots, prime)
            check(multiply(g_poly, q_poly, prime) == l_poly, "fixed-root factorization")
            residual_polys.append(q_poly)
            residual_supports.append(frozenset(q_roots))

        depth = min(2 * rank, m - len(fixed))
        prefixes = {top_prefix(poly, depth) for poly in residual_polys}
        check(len(prefixes) == 1, "residual prefix equality")

        if len(fixed) == m:
            check(len(fiber) == 1 and depth == 0, "all-fixed singleton")
            continue

        intersection = set(residual_supports[0])
        for support in residual_supports[1:]:
            intersection.intersection_update(support)
        check(not intersection, "residual family is gcd-trivial")

        for support in residual_supports:
            check(not (support & {(-value) % prime for value in support}), "antipodal-free residual")
            for exponent in range(1, 2 * m):
                multiplier = pow(theta, exponent, prime)
                check(shifted(support, multiplier, prime) != support, "aperiodic residual")

        c = len(fixed)
        locator_numerator = math.comb(2 * m - c, m - c)
        check(locator_numerator <= 1 << (2 * m - c), "locator box inequality")


def main() -> None:
    for case in ((17, 2, 1), (17, 4, 1), (17, 4, 2), (17, 8, 1), (17, 8, 2)):
        replay(*case)

    node_path = ROOT / "background" / "nodes" / NODE / "node.json"
    data = json.loads(node_path.read_text())
    check(data["node"]["status"] == "PROVED", "node status")
    check(
        {item["from"] for item in data["requires"]}
        == {"f2_antipodal_selector_prefix_transport", "f2_weighted_mass_max_fiber_sandwich"},
        "required suppliers",
    )
    check(data["evidence_for"] == [{"to": "f2_conditional_close"}], "consumer edge")

    print(f"F2_SELECTOR_FACE_PRIMITIVE_REDUCTION_PASS checks={CHECKS} cases={CASES}")


if __name__ == "__main__":
    main()
