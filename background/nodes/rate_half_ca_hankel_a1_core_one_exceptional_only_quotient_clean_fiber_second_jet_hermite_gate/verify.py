#!/usr/bin/env python3
"""Exact checks for the clean-fiber second-jet Hermite gate."""

from __future__ import annotations


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    size = max(len(left), len(right))
    return [
        ((left[i] if i < len(left) else 0)
         + (right[i] if i < len(right) else 0)) % prime
        for i in range(size)
    ]


def scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return [scalar * value % prime for value in poly]


def evaluate(poly: list[int], value: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % prime
    return out


def derivative(poly: list[int], prime: int) -> list[int]:
    return [index * poly[index] % prime for index in range(1, len(poly))]


def main() -> None:
    prime = 101
    p_cl = [-6 % prime, 11, -6 % prime, 1]
    gamma = 1
    p_first = evaluate(derivative(p_cl, prime), gamma, prime)
    p_second = evaluate(derivative(derivative(p_cl, prime), prime), gamma, prime)

    # F=Y-P_cl(t), R_X=Y, W=1, E=1, N_sq=0, V_vee=-1.
    # Then F V_vee+R_X W=P_cl and the root curve is y=P_cl(t).
    dot_y = p_first
    ddot_y = p_second
    recovered_ddot = (-(-p_second)) % prime
    if recovered_ddot != ddot_y:
        raise AssertionError("implicit second derivative failed")
    second_jet_numerator = (p_second - ddot_y) % prime
    dot_w = second_jet_numerator * pow(2 * dot_y % prime, -1, prime) % prime
    if dot_w != 0:
        raise AssertionError("second-jet identity failed")

    a_w = [2, 3]
    b_w = [5, 7]
    d_values: dict[int, list[int]] = {}
    for root in (1, 2, 3):
        p_prime = evaluate(derivative(p_cl, prime), root, prime)
        w0_t = [2 * root % prime, 3]
        expected_d = add(scale(a_w, root, prime), b_w, prime)
        j_gamma = add(w0_t, scale(expected_d, p_prime, prime), prime)
        d_values[root] = scale(
            add(j_gamma, scale(w0_t, -1, prime), prime),
            pow(p_prime, -1, prime),
            prime,
        )

    alpha, beta = 1, 2
    inverse_gap = pow(beta - alpha, -1, prime)
    recovered_a = scale(
        add(d_values[beta], scale(d_values[alpha], -1, prime), prime),
        inverse_gap,
        prime,
    )
    recovered_b = scale(
        add(scale(d_values[alpha], beta, prime), scale(d_values[beta], -alpha, prime), prime),
        inverse_gap,
        prime,
    )
    if recovered_a != a_w or recovered_b != b_w:
        raise AssertionError("two-fiber correction reconstruction failed")
    if d_values[3] != add(scale(recovered_a, 3, prime), recovered_b, prime):
        raise AssertionError("affine clean-fiber consistency failed")

    mutated = add(d_values[3], [1, 0], prime)
    if mutated == add(scale(recovered_a, 3, prime), recovered_b, prime):
        raise AssertionError("non-affine mutation was not detected")

    print(
        "RATE_HALF_QUOTIENT_CLEAN_FIBER_SECOND_JET_PASS "
        f"prime={prime} slopes={len(d_values)} dot_y={dot_y} dot_w={dot_w}"
    )


if __name__ == "__main__":
    main()
