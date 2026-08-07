#!/usr/bin/env python3
"""Exact constant-ratio degeneracy filter for h=3 rich curves."""

from __future__ import annotations

from dataclasses import dataclass


P = 193
H_SIZE = 32


def trim(poly: list[int], p: int = P) -> list[int]:
    out = [x % p for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def mul(a: list[int], b: list[int], p: int = P) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out, p)


def sub(a: list[int], b: list[int], p: int = P) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p
    return trim(out, p)


def scale(a: list[int], c: int, p: int = P) -> list[int]:
    return trim([(c * x) % p for x in a], p)


def eval_poly(poly: list[int], x: int, p: int = P) -> int:
    acc = 0
    for coeff in reversed(poly):
        acc = (acc * x + coeff) % p
    return acc


def subgroup(p: int = P, h: int = H_SIZE) -> set[int]:
    return {pow(x, (p - 1) // h, p) for x in range(1, p)}


@dataclass(frozen=True)
class Rat:
    num: tuple[int, ...]
    den: tuple[int, ...] = (1,)

    def n(self) -> list[int]:
        return trim(list(self.num))

    def d(self) -> list[int]:
        return trim(list(self.den))


def constant_ratio(r: Rat, s: Rat, p: int = P) -> int | None:
    """Return lambda if r/s is the constant lambda in F_p(X)."""

    left = mul(r.n(), s.d(), p)
    right = mul(s.n(), r.d(), p)
    if right == [0]:
        raise ValueError("zero rational map in denominator position")
    if left == [0]:
        return 0
    pivot = next((i for i, coeff in enumerate(right) if coeff % p), None)
    if pivot is None:
        raise ValueError("zero right side")
    lam = left[pivot] * pow(right[pivot], -1, p) % p if pivot < len(left) else 0
    if sub(left, scale(right, lam, p), p) == [0]:
        return lam
    return None


def classify_pair(r: Rat, s: Rat, hset: set[int], p: int = P) -> str:
    lam = constant_ratio(r, s, p)
    if lam is None:
        return "nonconstant"
    if lam == 0:
        return "zero_ratio_incompatible"
    if lam in hset:
        return "collapsed_H_ratio"
    return "incompatible_nonH_ratio"


def count_incidence(maps: tuple[Rat, Rat, Rat], hset: set[int], p: int = P) -> int:
    total = 0
    for x in range(p):
        ok = True
        for rat in maps:
            den = eval_poly(rat.d(), x, p)
            if den == 0:
                ok = False
                break
            value = eval_poly(rat.n(), x, p) * pow(den, -1, p) % p
            if value not in hset:
                ok = False
                break
        if ok:
            total += 1
    return total


def first_nonmember(hset: set[int], p: int = P) -> int:
    for x in range(1, p):
        if x not in hset:
            return x
    raise AssertionError("all nonzero field elements are in H")


def main() -> None:
    hset = subgroup()
    constants = sorted(hset)
    non_h = first_nonmember(hset)

    x = Rat((0, 1))
    collapsed = (x, Rat((0, constants[1])), Rat((0, constants[-1])))
    incompatible = (x, Rat((0, non_h)), Rat((0, constants[1])))
    shifted = (x, Rat((1, 1)), Rat((2, 1)))
    mobius = (
        Rat((0, 1), (1, 1)),
        Rat((0, constants[1]), (1, 1)),
        Rat((0, constants[-1]), (1, 1)),
    )

    rows = [
        ("collapsed_linear", collapsed, "collapsed_H_ratio", H_SIZE),
        ("incompatible_linear", incompatible, "incompatible_nonH_ratio", 0),
        ("shifted_nonconstant", shifted, "nonconstant", None),
        ("collapsed_mobius", mobius, "collapsed_H_ratio", H_SIZE - 1),
    ]

    print("case                    pair01_class              incidence")
    for name, maps, expected_class, expected_count in rows:
        cls = classify_pair(maps[0], maps[1], hset)
        count = count_incidence(maps, hset)
        if cls != expected_class:
            raise AssertionError((name, cls, expected_class))
        if expected_count is not None and count != expected_count:
            raise AssertionError((name, count, expected_count))
        print(f"{name:23s} {cls:25s} {count:9d}")

    print("H3_RICH_CURVE_DEGENERACY_FILTER_PASS")


if __name__ == "__main__":
    main()
