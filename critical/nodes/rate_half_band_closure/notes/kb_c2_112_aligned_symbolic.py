#!/usr/bin/env python3
"""Bounded symbolic factors for the aligned saturated (1,1,2) q-slice.

Only the two matching-preserving internal-edge templates are considered.
The first target is the negative-sign reconstruction-plane determinant.
"""

import argparse

import sympy as sp


def edge(left, right):
    return sp.Matrix([left * right, -(left + right), 1])


def evaluation(epsilon, point):
    if epsilon == 1:
        return sp.Matrix([
            [1, point, point**2, 0, 0],
            [0, 0, 0, 1 + point**2, point],
            [point**2, point, 1, 0, 0],
        ])
    return sp.Matrix([
        [1, point, point**2, 0],
        [0, 0, 0, 1 - point**2],
        [-point**2, -point, -1, 0],
    ])


def negative_plane_factor(template):
    # The centralizer of T -> 1/T is transitive on nonfixed reciprocal
    # pairs.  Normalize the common J_0 endpoint to 2 in this affine chart.
    a = sp.Rational(2)
    b, c, d, w = sp.symbols("b c d w", nonzero=True)
    W = sp.Symbol("W")
    q = sp.Matrix([c * d, -(c + d), 1])
    epsilon = -1
    f = q[0] - epsilon * w * q[2]
    g = epsilon * q[2] - w * q[0]
    m = q[1] * (1 - epsilon * w)
    v = sp.Matrix([
        f + g * W,
        m * (1 + epsilon * W),
        epsilon * (g + f * W),
    ])
    numerator = f + m * a + epsilon * g * a**2
    denominator = g + epsilon * m * a + epsilon * f * a**2
    z = sp.cancel(-numerator / denominator)
    vz = v.subs({W: z})
    l1 = vz[2]
    l0 = vz[1] + a * l1

    first = edge(a, 1 / a) if template == "fixed-moving" else edge(a, b)
    second = edge(a, b) if template == "fixed-moving" else edge(a, 1 / b)
    first_other = 1 / a if template == "fixed-moving" else b
    second_other = b if template == "fixed-moving" else 1 / b
    target = sp.together(
        ((l0 + second_other * l1) * first
         + (l0 + first_other * l1) * second)
        / (second_other - first_other)
    )

    at_w = evaluation(epsilon, w)
    at_z = evaluation(epsilon, z)
    cut = sp.Matrix.vstack(
        at_w[0, :] - q[0] * at_w[2, :],
        at_w[1, :] - q[1] * at_w[2, :],
        at_z,
    )
    augmented = cut.row_join(sp.Matrix([0, 0, *target]))
    determinant = sp.together(augmented.det(method="domain-ge"))
    numerator_factor, denominator_factor = sp.fraction(determinant)
    incidence = c * d * w + 4 * c * d - 2 * c * w - 2 * c - 2 * d * w - 2 * d + 4 * w + 1
    common = ((c - 2) * (2 * c - 1) * (d - 2) * (2 * d - 1)
              * (w - 1)**5 * (w + 1)**5 * (c * d - 1)**2)
    factor_a = 5 * c * d - 4 * c - 4 * d + 5
    factor_b = b * c * d - 2 * b * c - 2 * b * d + b + 2 * c * d - c - d + 2
    factor_c = 2 * b * c * d - b * c - b * d + 2 * b + c * d - 2 * c - 2 * d + 1
    if template == "fixed-moving":
        expected_numerator = -6 * common * factor_a**2 * factor_b
        expected_denominator = (2 * b - 1) * incidence**5
    else:
        expected_numerator = 6 * common * factor_a * factor_b * factor_c
        expected_denominator = (b - 1) * (b + 1) * incidence**5
    if (sp.factor(numerator_factor) != sp.factor(expected_numerator)
            or sp.factor(denominator_factor) != sp.factor(expected_denominator)):
        raise RuntimeError("factorization mismatch")
    return sp.factor(expected_numerator), sp.factor(expected_denominator)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "template", choices=("fixed-moving", "moving-moving")
    )
    args = parser.parse_args()
    numerator, denominator = negative_plane_factor(args.template)
    print(f"template={args.template}")
    print(f"negative_plane_numerator={numerator}")
    print(f"negative_plane_denominator={denominator}")


if __name__ == "__main__":
    main()
