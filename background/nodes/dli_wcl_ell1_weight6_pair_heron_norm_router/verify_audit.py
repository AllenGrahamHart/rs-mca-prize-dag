#!/usr/bin/env python3
"""Independent finite-field audit of the pair-Heron router."""

from __future__ import annotations

import itertools
import random


def pairings(labels):
    if not labels:
        return [()]
    first = labels[0]
    out = []
    for index in range(1, len(labels)):
        rest = labels[1:index] + labels[index + 1 :]
        for tail in pairings(rest):
            out.append(((first, labels[index]),) + tail)
    return out


def direct(roots, anchor, p):
    product = 1
    for tail in itertools.product((1, -1), repeat=5):
        signs = iter(tail)
        value = sum(
            root * (1 if index == anchor else next(signs))
            for index, root in enumerate(roots)
        )
        product = product * value % p
    return product


def routed(roots, pairing, p):
    product = 1
    for internal in itertools.product((1, -1), repeat=3):
        squares = []
        for sign, (left, right) in zip(internal, pairing):
            squares.append((roots[left] + sign * roots[right]) ** 2 % p)
        u, v, w = squares
        factor = (u*u + v*v + w*w - 2*(u*v + u*w + v*w)) % p
        product = product * factor % p
    return product


def main():
    all_pairings = pairings(tuple(range(6)))
    rng = random.Random(20260806)
    checks = 0
    zero_checks = 0
    for p in (97, 193, 257, 769, 12289):
        for _ in range(12):
            roots = tuple(rng.randrange(1, p) for _ in range(6))
            for pairing in all_pairings:
                anchor = pairing[0][0]
                left = direct(roots, anchor, p)
                right = routed(roots, pairing, p)
                if left != right:
                    raise AssertionError((p, roots, pairing, left, right))
                checks += 1
                zero_checks += (left == 0) == (right == 0)
    if checks != 900 or zero_checks != checks:
        raise AssertionError((checks, zero_checks))
    print(
        "DLI_WCL_ELL1_WEIGHT6_PAIR_HERON_ROUTER_AUDIT_PASS "
        f"pairings={len(all_pairings)} finite_field_checks={checks}"
    )


if __name__ == "__main__":
    main()
