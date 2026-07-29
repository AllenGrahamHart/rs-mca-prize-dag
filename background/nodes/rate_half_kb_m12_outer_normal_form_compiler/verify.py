#!/usr/bin/env python3
"""Verify the KoalaBear m12 outer normal-form compiler."""

from fractions import Fraction
from pathlib import Path


NODE = Path(__file__).resolve().parent
Q = Fraction


def trim(polynomial):
    result = list(polynomial)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_add(left, right):
    size = max(len(left), len(right))
    result = [Q(0)] * size
    for index in range(size):
        result[index] = (
            left[index] if index < len(left) else Q(0)
        ) + (right[index] if index < len(right) else Q(0))
    return trim(result)


def poly_mul(left, right):
    result = [Q(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return trim(result)


def derivative(polynomial):
    return trim([index * polynomial[index] for index in range(1, len(polynomial))])


def evaluate(polynomial, value):
    result = Q(0)
    for coefficient in reversed(polynomial):
        result = result * value + coefficient
    return result


def qadd(left, right):
    return (left[0] + right[0], left[1] + right[1])


def qmul(left, right, theta_square):
    # theta^2 = theta_square[0] + theta_square[1]*theta.
    ac = left[0] * right[0]
    cross = left[0] * right[1] + left[1] * right[0]
    bd = left[1] * right[1]
    return (
        ac + bd * theta_square[0],
        cross + bd * theta_square[1],
    )


def qscale(value, scalar):
    return (scalar * value[0], scalar * value[1])


def qpoly_derivative(polynomial):
    return [qscale(polynomial[index], index) for index in range(1, len(polynomial))]


def qpoly_evaluate(polynomial, value, theta_square):
    result = (Q(0), Q(0))
    for coefficient in reversed(polynomial):
        result = qadd(qmul(result, value, theta_square), coefficient)
    return result


def tadd(left, right):
    size = max(len(left), len(right))
    result = [Q(0)] * size
    for index in range(size):
        result[index] = (
            left[index] if index < len(left) else Q(0)
        ) + (right[index] if index < len(right) else Q(0))
    return tuple(trim(result))


def tmul(left, right):
    result = [Q(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return tuple(trim(result))


def txpoly_mul(left, right):
    zero = (Q(0),)
    result = [zero] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] = tadd(result[i + j], tmul(left_value, right_value))
    return result


def txpoly_derivative(polynomial):
    return [tuple(index * value for value in polynomial[index]) for index in range(1, len(polynomial))]


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "five rigid affine classes plus one one-parameter family" in statement
    assert "No family is deleted" in contract

    # Dickson identity from the standard recurrence D_n=xD_(n-1)-aD_(n-2).
    # Coefficients are in x, with a specialized to an exact rational control.
    a = Q(7, 3)
    d0 = [Q(2)]
    d1 = [Q(0), Q(1)]
    dickson = [d0, d1]
    for _ in range(2, 6):
        next_value = poly_add(
            poly_mul([Q(0), Q(1)], dickson[-1]),
            [-a * coefficient for coefficient in dickson[-2]],
        )
        dickson.append(next_value)
    assert dickson[5] == [Q(0), 5 * a * a, Q(0), -5 * a, Q(0), Q(1)]

    # The two quadratic divided-difference factors over Q(sqrt(5)).
    sqrt5_square = (Q(5), Q(0))
    one = (Q(1), Q(0))
    s = (Q(0), Q(1))
    A = qscale(qadd(one, s), Q(1, 2))
    C = qscale(qadd(one, qscale(s, -1)), Q(1, 2))
    B = qscale(qadd((Q(-5), Q(0)), s), Q(1, 2))
    D = qscale(qadd((Q(-5), Q(0)), qscale(s, -1)), Q(1, 2))
    assert qadd(A, C) == one
    assert qadd(qmul(A, C, sqrt5_square), (Q(2), Q(0))) == one
    assert qadd(B, D) == (Q(-5), Q(0))
    assert qadd(qmul(A, D, sqrt5_square), qmul(B, C, sqrt5_square)) == (
        Q(-5),
        Q(0),
    )
    assert qmul(B, D, sqrt5_square) == (Q(5), Q(0))

    # Fixed normal forms and their exact critical multiplicities.
    a5_33 = [Q(0), Q(0), Q(0), Q(10), Q(-15), Q(6)]
    assert derivative(a5_33) == poly_mul([Q(0), Q(0), Q(30)], [Q(1), Q(-2), Q(1)])
    assert evaluate(a5_33, Q(0)) == 0
    assert evaluate(a5_33, Q(1)) == 1

    s5_32 = poly_mul([Q(0), Q(0), Q(0), Q(1)], [Q(1), Q(-2), Q(1)])
    assert derivative(s5_32) == poly_mul(
        [Q(0), Q(0), Q(1)],
        poly_mul([Q(-1), Q(1)], [Q(-3), Q(5)]),
    )
    assert evaluate(s5_32, Q(0)) == evaluate(s5_32, Q(1)) == 0

    s5_42 = [Q(0), Q(0), Q(0), Q(0), Q(5), Q(-4)]
    assert derivative(s5_42) == [Q(0), Q(0), Q(0), Q(20), Q(-20)]
    assert evaluate(s5_42, Q(0)) == 0
    assert evaluate(s5_42, Q(1)) == 1

    # The rigid A5 (3),(2,2) form over Q[t]/(3t^2+4t+3).
    t_square = (Q(-1), Q(-4, 3))
    qt = (Q(0), Q(1))
    qone = (Q(1), Q(0))
    a5_322 = [
        (Q(0), Q(0)),
        (Q(0), Q(0)),
        (Q(0), Q(0)),
        qscale(qt, 20),
        qscale(qadd(qone, qt), -15),
        (Q(12), Q(0)),
    ]
    assert qpoly_derivative(a5_322) == [
        (Q(0), Q(0)),
        (Q(0), Q(0)),
        qscale(qt, 60),
        qscale(qadd(qone, qt), -60),
        (Q(60), Q(0)),
    ]
    assert qpoly_evaluate(a5_322, qone, t_square) == qpoly_evaluate(
        a5_322, qt, t_square
    )

    # The one-parameter S5 form, as a polynomial in x over Q[t].
    z = (Q(0),)
    one_t = (Q(1),)
    tvar = (Q(0), Q(1))
    x2 = [z, z, one_t]
    xm1sq = [one_t, (Q(-2),), one_t]
    linear = [tuple(-5 * value for value in tvar), (Q(2),)]
    parameter_form = txpoly_mul(txpoly_mul(x2, xm1sq), linear)
    expected_derivative = txpoly_mul(
        [z, one_t],
        txpoly_mul(
            [(Q(-1),), one_t],
            [tuple(5 * value for value in tvar), (-Q(3), -Q(10)), (Q(5),)],
        ),
    )
    expected_derivative = [tuple(2 * value for value in item) for item in expected_derivative]
    assert txpoly_derivative(parameter_form) == expected_derivative
    print("RATE_HALF_KB_M12_OUTER_NORMAL_FORM_COMPILER_PASS")


if __name__ == "__main__":
    main()
