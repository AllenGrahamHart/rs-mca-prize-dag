#!/usr/bin/env python3
"""Replay G2 closure and detect the false fixed-scale mutation."""

from __future__ import annotations


def rotate(mask: int, shift: int, order: int) -> int:
    full = (1 << order) - 1
    return ((mask << shift) | (mask >> (order - shift))) & full


def stabilizer(mask: int, order: int) -> tuple[int, ...]:
    return tuple(shift for shift in range(order) if rotate(mask, shift, order) == mask)


def full_fiber_count(mask: int, order: int, scale: int) -> int:
    step = order // scale
    count = 0
    for residue in range(step):
        fiber = sum(1 << (residue + step * index) for index in range(scale))
        count += (mask & fiber) == fiber
    return count


def exhaustive(order: int) -> int:
    checked = 0
    for mask in range(1, 1 << order):
        checked += 1
        c = len(stabilizer(mask, order))
        if c == 1:
            continue
        if c & (c - 1) or order % c:
            raise AssertionError((order, mask, c))
        fibers = full_fiber_count(mask, order, c)
        if fibers == 0 or fibers * c != mask.bit_count():
            raise AssertionError((order, mask, c, fibers))
    return checked


def mutation_control() -> None:
    order = 32
    support = (0, 4, 5, 9, 12, 13, 15, 16, 20, 21, 25, 28, 29, 31)
    mask = sum(1 << exponent for exponent in support)
    if len(stabilizer(mask, order)) != 2:
        raise AssertionError("witness stabilizer")
    if full_fiber_count(mask, order, 2) * 2 != len(support):
        raise AssertionError("closure scale")
    for false_scale in (4, 8):
        residual = len(support) - false_scale * full_fiber_count(
            mask, order, false_scale
        )
        if residual < false_scale:
            raise AssertionError(("fixed-scale mutation survived", false_scale))


def main() -> None:
    checked = exhaustive(8) + exhaustive(16)
    mutation_control()
    print(
        "PETAL_G2_SUPPORT_FORCING_PASS "
        f"nonempty_subsets={checked} mutation=fixed-scale-4,8"
    )


if __name__ == "__main__":
    main()
