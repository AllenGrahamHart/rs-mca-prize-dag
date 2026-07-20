#!/usr/bin/env python3
"""Replay the sparse subgroup-norm identity on the F_17 route fence."""

from __future__ import annotations


P = 17


def trim(poly: list[int]) -> list[int]:
    out = [value % P for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)
        for i in range(size)
    ])


def mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    return trim(out)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def power(poly: list[int], exponent: int) -> list[int]:
    out = [1]
    base = trim(poly)
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        base = mul(base, base)
        exponent //= 2
    return out


def locator(roots: tuple[int, ...]) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % P, 1])
    return out


def evaluate(poly: list[int], value: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % P
    return out


def product(values: list[int]) -> int:
    out = 1
    for value in values:
        out = out * value % P
    return out


def main() -> None:
    roots_a = (2, 5)
    triple = (3, 13, 15)
    active = (4, 9, 11, 6, 7, 10, 8, 12, 16)
    core = 1
    omitted = 14
    internal = (1,)
    external = (15, 2, 4)
    supported = (0, *internal, *external)
    rank_degree = 3

    a_poly = locator(roots_a) + [0]
    b_poly = locator(triple)
    q_1 = add(b_poly, scale(a_poly, -1))

    def q_row(x: int) -> list[int]:
        return trim([evaluate(a_poly, x), evaluate(q_1, x)])

    full_norm = [1]
    for x in range(1, P):
        full_norm = mul(full_norm, q_row(x))
    left = mul([0, 1], full_norm)

    p_sup = locator(supported)
    boundary = mul(q_row(core), q_row(omitted))
    right_without_scalar = mul(boundary, power(p_sup, rank_degree))

    # The explicit scalar is kappa_0*L in the theorem.
    kappa_a = product([evaluate(b_poly, a) for a in roots_a])
    kappa_b = product([evaluate(a_poly, t) for t in triple])
    leading_norm = product([evaluate(q_1, x) for x in active])
    delta_0 = (-internal[0]) % P
    kappa = kappa_a * kappa_b * leading_norm % P
    kappa = kappa * inv(pow(delta_0, 3, P)) % P
    assert kappa == 15
    assert left == scale(right_without_scalar, kappa)

    # The unconditional quotient form uses H before the external cube.
    active_norm = [1]
    for x in active:
        active_norm = mul(active_norm, q_row(x))
    internal_locator = locator(internal)
    unconditional_right = mul(
        boundary,
        mul(power(mul([0, 1], internal_locator), rank_degree), active_norm),
    )
    kappa_0 = kappa * inv(leading_norm) % P
    assert left == scale(unconditional_right, kappa_0)

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_SPARSE_SUBGROUP_NORM_ROUTER_PASS "
        f"field={P} full_norm_degree={len(full_norm)-1} "
        f"supported_degree={len(p_sup)-1} kappa={kappa}"
    )


if __name__ == "__main__":
    main()
