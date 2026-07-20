#!/usr/bin/env python3
"""Verify the background-overlap inequality and sharp F_17 boundary."""

from __future__ import annotations


P = 17
ELL = 2
CORE = (0, 1, 2, 3)
SUPPORT = (4, 5, 6)
FILLERS = (7, 8, 9)
BACKGROUND = (10,)
LABELS = (1, 2, 3)
D0 = (0, 1)
D1 = (2, 3)
F0 = (0, 16, 1)
W0 = (1, 14, 11)
F1 = (6, 12, 1)
W1 = (0, 15, 7)


def trim(poly: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    out = [value % P for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def mul(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % P
    return trim(out)


def sub(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0)
        - (right[i] if i < len(right) else 0)
        for i in range(size)
    ])


def evaluate(poly: tuple[int, ...], point: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % P
    return value


def locator(points: tuple[int, ...]) -> tuple[int, ...]:
    out = (1,)
    for point in points:
        out = mul(out, ((-point) % P, 1))
    return out


def check_pair(
    defect: tuple[int, ...], f: tuple[int, ...], w: tuple[int, ...]
) -> tuple[int, ...]:
    assert f == locator(defect)
    assert all(evaluate(w, point) != 0 for point in defect)
    assert all(
        evaluate(w, point) == label * evaluate(f, point) % P
        for point, label in zip(SUPPORT, LABELS)
    )
    assert all(
        evaluate(w, point) != label * evaluate(f, point) % P
        for point, label in zip(FILLERS, LABELS)
    )
    assert evaluate(w, BACKGROUND[0]) == 0
    retained = tuple(point for point in CORE if point not in defect)
    return mul(locator(retained), w)


def arithmetic_audit() -> tuple[int, int]:
    paid = 0
    boundary = 0
    for n_core in range(2, 31):
        for ell in range(1, min(10, n_core + 2)):
            for b in range(ell):
                gap = ell - b
                for d in range(n_core + 1):
                    a = n_core - d
                    for s in range(gap, a + 1):
                        h = d + s
                        common_background = ell - 2 * s + gap
                        if a + s < ell + gap:
                            assert common_background > n_core - h >= 0
                            paid += 1
                        elif a + s == ell + gap:
                            assert common_background == n_core - h
                            boundary += 1
    return paid, boundary


def main() -> None:
    p0 = check_pair(D0, F0, W0)
    p1 = check_pair(D1, F1, W1)
    assert p0 != p1
    difference = sub(p1, p0)
    assert len(difference) - 1 == len(CORE)
    assert all(evaluate(difference, point) == 0 for point in SUPPORT + BACKGROUND)

    n_core, d, h = len(CORE), len(D0), len(SUPPORT)
    a, s = n_core - d, h - d
    gap = ELL - len(BACKGROUND)
    assert a + s == ELL + gap == 3
    agreement = a + h + len(BACKGROUND)
    assert agreement == (n_core + 1) + ELL - 1 == 6

    paid, boundary = arithmetic_audit()
    assert paid > 0 and boundary > 0
    print(
        "L1_BACKGROUND_OVERLAP_SINGLETON_PASS "
        f"agreement={agreement} equality={a + s} "
        f"paid={paid} boundary={boundary}"
    )


if __name__ == "__main__":
    main()
