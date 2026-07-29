#!/usr/bin/env python3
"""Independent critical-value integration audit for the normal forms."""

from fractions import Fraction
from pathlib import Path


NODE = Path(__file__).resolve().parent
Q = Fraction


def poly_mul(left, right):
    result = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def integral_between(polynomial, left, right):
    return sum(
        coefficient * (right ** (index + 1) - left ** (index + 1)) / (index + 1)
        for index, coefficient in enumerate(polynomial)
    )


def sqrt5_add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def sqrt5_mul(left, right):
    return (
        left[0] * right[0] + 5 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def main() -> None:
    proof = (NODE / "proof.md").read_text()
    assert "Riemann-Hurwitz" in proof
    assert "five derivative-integration normal" in (NODE / "source_evidence.md").read_text()

    # D5 Galois closure with inertia orders 5,2,2 has genus zero.
    rhs = Q(10) * (Q(-2) + Q(4, 5) + Q(1, 2) + Q(1, 2))
    assert rhs == -2

    # S5 (3,2)+(2): the common critical value fixes c=3/5.
    # Integral_0^1 x^2(x-1)(x-c) dx = (-3+5c)/60.
    for c in (Q(3, 5), Q(2, 5)):
        derivative = poly_mul(
            poly_mul([Q(0), Q(0), Q(1)], [Q(-1), Q(1)]),
            [-c, Q(1)],
        )
        value = integral_between(derivative, Q(0), Q(1))
        assert (value == 0) == (c == Q(3, 5))

    # A5 (3)+(2,2): direct expansion of the equality condition.
    # Integral_1^t x^2(x-1)(x-t) dx
    #   = -(t-1)^3(3t^2+4t+3)/60.
    for t in (Q(2), Q(-1), Q(3, 2)):
        derivative = poly_mul(
            poly_mul([Q(0), Q(0), Q(1)], [Q(-1), Q(1)]),
            [-t, Q(1)],
        )
        value = integral_between(derivative, Q(1), t)
        expected = -(t - 1) ** 3 * (3 * t * t + 4 * t + 3) / 60
        assert value == expected

    # S5 (2)+(2)+(2,2): the colliding pair at 0,1 imposes the one
    # symmetric relation 5(u+v)-10uv-3=0.
    for u, v in ((Q(2), Q(7, 5)), (Q(-1), Q(4)), (Q(3, 2), Q(5, 7))):
        derivative = poly_mul(
            poly_mul([Q(0), Q(1)], [Q(-1), Q(1)]),
            poly_mul([-u, Q(1)], [-v, Q(1)]),
        )
        value = integral_between(derivative, Q(0), Q(1))
        expected = (-3 + 5 * (u + v) - 10 * u * v) / 60
        assert value == expected

    # Independently multiply the dihedral factors in Q(sqrt(5)).
    A = (Q(1, 2), Q(1, 2))
    C = (Q(1, 2), Q(-1, 2))
    B = (Q(-5, 2), Q(1, 2))
    D = (Q(-5, 2), Q(-1, 2))
    assert sqrt5_add(A, C) == (1, 0)
    assert sqrt5_add(sqrt5_mul(A, C), (2, 0)) == (1, 0)
    assert sqrt5_add(B, D) == (-5, 0)
    assert sqrt5_add(sqrt5_mul(A, D), sqrt5_mul(B, C)) == (-5, 0)
    assert sqrt5_mul(B, D) == (5, 0)
    print("RATE_HALF_KB_M12_OUTER_NORMAL_FORM_COMPILER_AUDIT_PASS")


if __name__ == "__main__":
    main()
