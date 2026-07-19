#!/usr/bin/env python3
"""Independent finite checks for the ell-two weight-five router."""

from __future__ import annotations

import itertools


def antipodal_free(values: frozenset[int], p: int) -> bool:
    return all((-value) % p not in values for value in values)


def moments(values: frozenset[int], p: int) -> tuple[int, int]:
    return sum(values) % p, sum(pow(value, 3, p) for value in values) % p


def normalized_direct_relations(p: int) -> set[frozenset[int]]:
    out: set[frozenset[int]] = set()
    for raw in itertools.combinations(range(1, p), 5):
        values = frozenset(raw)
        if not antipodal_free(values, p) or moments(values, p) != (0, 0):
            continue
        for e in values:
            inverse = pow(e, -1, p)
            out.add(frozenset(value * inverse % p for value in values))
    return out


def routed_relations(p: int) -> set[frozenset[int]]:
    out: set[frozenset[int]] = set()
    nonzero = range(1, p)
    for x, y in itertools.combinations((value for value in nonzero if value != 1), 2):
        seed = frozenset((1, x, y))
        if len(seed) != 3 or not antipodal_free(seed, p):
            continue
        u = (x + y) % p
        product = x * y % p
        v = (-1 - u) % p
        if u == 0 or v == 0:
            continue
        final_product = u * (v - product) * pow(v, -1, p) % p
        roots = [
            value
            for value in nonzero
            if (value * value - v * value + final_product) % p == 0
        ]
        if len(roots) != 2:
            continue
        values = frozenset((*seed, *roots))
        if len(values) != 5 or not antipodal_free(values, p):
            continue
        if moments(values, p) != (0, 0):
            raise AssertionError((p, x, y, values))
        out.add(values)
    return out


def dickson(order: int, v: int, product: int, p: int) -> int:
    previous, current = 2 % p, v % p
    if order == 0:
        return previous
    for _ in range(2, order + 1):
        previous, current = current, (v * current - product * previous) % p
    return current


def check_dickson_membership(p: int, order: int) -> tuple[int, int]:
    if (p - 1) % order:
        raise AssertionError((p, order))
    subgroup = {value for value in range(1, p) if pow(value, order, p) == 1}
    positives = 0
    negatives = 0
    for v in range(1, p):
        for product in range(1, p):
            if (v * v - 4 * product) % p == 0:
                continue
            roots = [
                value
                for value in range(1, p)
                if (value * value - v * value + product) % p == 0
            ]
            direct = len(roots) == 2 and set(roots) <= subgroup
            recurrence = (
                pow(product, order, p) == 1
                and dickson(order, v, product, p) == 2 % p
            )
            if direct != recurrence:
                raise AssertionError((p, order, v, product, roots, direct, recurrence))
            positives += direct
            negatives += not direct
    return positives, negatives


def main() -> None:
    relation_counts = {}
    total_relations = 0
    for p in (11, 13, 17, 19, 23):
        direct = normalized_direct_relations(p)
        routed = routed_relations(p)
        if direct != routed:
            raise AssertionError((p, direct - routed, routed - direct))
        relation_counts[p] = len(direct)
        total_relations += len(direct)
    if total_relations == 0:
        raise AssertionError("vacuous relation checks")

    dickson_rows = {
        (17, 8): check_dickson_membership(17, 8),
        (17, 16): check_dickson_membership(17, 16),
        (97, 16): check_dickson_membership(97, 16),
        (97, 32): check_dickson_membership(97, 32),
    }
    if any(positives == 0 or negatives == 0 for positives, negatives in dickson_rows.values()):
        raise AssertionError(dickson_rows)
    print(
        "DLI_WCL_ELL2_WEIGHT5_PAIR_QUADRATIC_ROUTER_PASS "
        f"relations={relation_counts} dickson={dickson_rows}"
    )


if __name__ == "__main__":
    main()
