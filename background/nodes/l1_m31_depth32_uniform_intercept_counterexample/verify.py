#!/usr/bin/env python3
"""Direct finite-field replay of the M31 depth-32 counterexample."""

from __future__ import annotations

from itertools import combinations
from math import comb


P = 2**31 - 1
SCALE = pow(2, -2047, P)
GENERATOR = (1717986917, 1288490189)
ANCHOR_CLASSES = (
    5, 7, 9, 11, 13, 17, 19, 45, 47, 51, 53, 55, 57, 59,
    69, 71, 73, 75, 77, 81, 83, 109, 111, 115, 117, 119,
    121, 123, 125,
)
SELECTED_T64 = (5, 7, 9, 11, 13, 17, 19)
COMPLEMENT_T64 = (15, 21, 23, 25, 27, 29, 31)
MIXED = (
    ((5,13,19,45,47,69,73,75,77,111,117,119), (29,35,37,39,41,85,95,97,101,103,105,107)),
    ((9,11,17,51,53,55,59,81,83,109,115,123), (21,23,25,27,31,33,43,87,89,91,93,99)),
    ((7,59,71,75,77,81,83,109,111,115,117,123), (21,25,39,43,79,85,91,93,99,101,107,113)),
    ((5,11,13,17,19,45,47,51,53,57,69,121), (15,21,27,29,35,37,43,49,85,89,103,107)),
    ((7,59,71,75,77,81,83,109,111,115,117,123), (23,25,39,41,79,87,91,93,99,101,105,113)),
    ((5,11,13,17,19,45,47,51,53,57,69,121), (15,23,27,29,35,37,41,49,87,89,103,105)),
    ((7,59,71,75,77,81,83,109,111,115,117,123), (25,31,33,39,79,91,93,95,97,99,101,113)),
    ((5,11,13,17,19,45,47,51,53,57,69,121), (15,27,29,31,33,35,37,49,89,95,97,103)),
    ((5,11,17,45,51,57,69,75,81,109,115,121), (15,23,33,39,41,49,65,79,97,103,113,127)),
    ((5,11,17,45,51,57,69,75,81,109,115,121), (21,23,33,39,41,43,65,85,97,103,107,127)),
    ((5,11,17,45,51,57,69,75,81,109,115,121), (23,27,33,37,39,41,65,91,97,101,103,127)),
    ((5,11,17,45,51,57,69,75,81,109,115,121), (23,29,33,35,39,41,65,93,97,99,103,127)),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def mul_pair(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    a, b = left
    c, d = right
    return ((a * c - b * d) % P, (a * d + b * c) % P)


def pow_pair(base: tuple[int, int], exponent: int) -> tuple[int, int]:
    out = (1, 0)
    while exponent:
        if exponent & 1:
            out = mul_pair(out, base)
        base = mul_pair(base, base)
        exponent >>= 1
    return out


def labels() -> dict[int, int]:
    return {
        r: SCALE * pow_pair(GENERATOR, r * 2**19)[0] % P
        for r in range(1, 2048, 2)
    }


def block16(a: int) -> frozenset[int]:
    return frozenset(
        r for r in range(1, 2048, 2) if r % 256 in {a, 256 - a}
    )


def block64(a: int) -> frozenset[int]:
    return frozenset(
        r for r in range(1, 2048, 2) if r % 64 in {a, 64 - a}
    )


def multiply_linear(poly: list[int], root: int) -> list[int]:
    out = [0] * (len(poly) + 1)
    for i, coefficient in enumerate(poly):
        out[i] = (out[i] - root * coefficient) % P
        out[i + 1] = (out[i + 1] + coefficient) % P
    return out


def locator(reps: frozenset[int], q: dict[int, int]) -> list[int]:
    poly = [1]
    for rep in sorted(reps):
        poly = multiply_linear(poly, q[rep])
    return poly


def prefix(reps: frozenset[int], q: dict[int, int], depth: int) -> tuple[int, ...]:
    poly = locator(reps, q)
    require(poly[-1] == 1, "locator not monic")
    return tuple(reversed(poly[:-1]))[:depth]


def support(classes: frozenset[int]) -> frozenset[int]:
    out = set(block16(3)) - {3}
    for name in classes:
        out.update(block16(name))
    return frozenset(out)


def owner64(name: int) -> int:
    residue = name % 64
    return min(residue, 64 - residue)


def main() -> None:
    conjugate = (GENERATOR[0], -GENERATOR[1] % P)
    require(mul_pair(GENERATOR, conjugate) == (1, 0), "generator norm")
    require(pow_pair(GENERATOR, 2**31) == (1, 0), "generator order")
    q = labels()
    require(len(q) == len(set(q.values())) == 1024, "quotient labels")

    classes16 = tuple(block16(a) for a in range(1, 128, 2))
    require(all(len(part) == 16 for part in classes16), "T16 class size")
    require(len(set().union(*classes16)) == 1024, "T16 partition")

    intact = SELECTED_T64 + COMPLEMENT_T64
    common_nonconstant = None
    for name in intact:
        reps = block64(name)
        require(len(reps) == 64 and 1 not in reps and 3 not in reps,
                f"T64 class {name}")
        poly = locator(reps, q)
        nonconstant = tuple(poly[1:])
        if common_nonconstant is None:
            common_nonconstant = nonconstant
        require(nonconstant == common_nonconstant,
                f"T64 factors differ above constant at {name}")

    anchor_classes = frozenset(ANCHOR_CLASSES)
    anchor = support(anchor_classes)
    allowed = set(range(1, 2048, 2)) - {1, 3}
    require(len(anchor) == 479 and anchor <= allowed, "anchor")
    require(
        set(anchor) == set(block16(3)) - {3} | set(block16(125)) |
        set().union(*(set(block64(name)) for name in SELECTED_T64)),
        "anchor T64 decomposition",
    )
    eta = prefix(anchor, q, 32)

    whole_keys = set()
    for removed in combinations(SELECTED_T64, 3):
        for added in combinations(COMPLEMENT_T64, 3):
            key = (frozenset(removed), frozenset(added))
            whole_keys.add(key)
            candidate = set(anchor)
            for name in removed:
                candidate.difference_update(block64(name))
            for name in added:
                candidate.update(block64(name))
            require(len(candidate) == 479, "whole support size")
            require(len(set(anchor) - candidate) == 192, "whole deficiency")
    require(len(whole_keys) == comb(7, 3) ** 2 == 1225, "whole count")

    mixed_class_sets = []
    for index, (removed, added) in enumerate(MIXED, start=1):
        removed_set, added_set = set(removed), set(added)
        require(removed_set <= anchor_classes, f"mixed {index} removal")
        require(not (added_set & anchor_classes), f"mixed {index} addition")
        classes = frozenset((set(anchor_classes) - removed_set) | added_set)
        candidate = support(classes)
        require(len(candidate) == 479 and candidate <= allowed,
                f"mixed {index} support")
        require(len(set(anchor) - candidate) == 192,
                f"mixed {index} deficiency")
        require(prefix(candidate, q, 32) == eta,
                f"mixed {index} prefix")
        occupancy = {}
        for name in classes - {125}:
            occupancy[owner64(name)] = occupancy.get(owner64(name), 0) + 1
        require(any(value not in (0, 4) for value in occupancy.values()),
                f"mixed {index} is a whole-T64 exchange")
        mixed_class_sets.append(classes)
    require(len(set(mixed_class_sets)) == 12, "duplicate mixed support")

    require(1225 + len(mixed_class_sets) == 1237 > 1233, "counterexample")
    require(33 <= 192 <= 213, "band membership")
    total = 1 + 1237 * 447 + 14456476
    require(total == 15009416 and 16777215 - total == 1767799,
            "compiler calibration")

    print(
        "L1_M31_DEPTH32_UNIFORM_INTERCEPT_COUNTEREXAMPLE_PASS "
        "labels=1024 anchor=479 whole=1225 mixed=12 rooted_degree>=1237 "
        f"eta0={eta[0]} eta31={eta[-1]}"
    )


if __name__ == "__main__":
    main()
