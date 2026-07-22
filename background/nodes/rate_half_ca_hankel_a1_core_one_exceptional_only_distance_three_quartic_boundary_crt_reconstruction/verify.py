#!/usr/bin/env python3
"""Exact F_97 replay for the quartic-boundary CRT gate."""

from __future__ import annotations


P = 97


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % P == 0:
        poly.pop()
    return [value % P for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % P
    return trim(out)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value % P for value in poly])


def mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    return trim(out)


def locator(roots: tuple[int, ...]) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % P, 1])
    return out


def evaluate(poly: list[int], point: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * point + coefficient) % P
    return out


def derivative(poly: list[int]) -> list[int]:
    return [index * poly[index] % P for index in range(1, len(poly))] or [0]


def divide_exact(numerator: list[int], denominator: list[int]) -> list[int]:
    require(len(numerator) >= len(denominator), "negative quotient degree")
    work = numerator[:]
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse_lead = pow(denominator[-1], -1, P)
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient = work[shift + len(denominator) - 1] * inverse_lead % P
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            work[shift + index] = (work[shift + index] - coefficient * value) % P
    require(not any(work[: len(denominator) - 1]), "nonexact polynomial division")
    return trim(quotient)


def interpolate(points: list[int], values: list[int]) -> list[int]:
    out = [0]
    for index, point in enumerate(points):
        basis = [1]
        denominator = 1
        for other_index, other in enumerate(points):
            if other_index == index:
                continue
            basis = mul(basis, [(-other) % P, 1])
            denominator = denominator * (point - other) % P
        out = add(out, scale(basis, values[index] * pow(denominator, -1, P)))
    return out


def primitive_root() -> int:
    for candidate in range(2, P):
        if pow(candidate, (P - 1) // 2, P) != 1 and pow(
            candidate, (P - 1) // 3, P
        ) != 1:
            return candidate
    raise AssertionError("no primitive root")


def build_fixture() -> dict[str, object]:
    e = 3
    domain_order = 32
    generator = pow(primitive_root(), (P - 1) // domain_order, P)
    domain: list[int] = []
    value = 1
    for _ in range(domain_order):
        domain.append(value)
        value = value * generator % P
    require(value == 1 and len(set(domain)) == domain_order, "bad subgroup")

    s, x_0 = domain[:2]
    pairs = [tuple(domain[index : index + 2]) for index in (2, 4, 6)]
    triple = tuple(domain[8:11])
    active = tuple(domain[11:])
    exceptional = [root for pair in pairs for root in pair]

    a_poly = locator(tuple(exceptional))
    b_poly = locator(triple)
    c_poly = locator(active)
    d_polys = [locator(pair) for pair in pairs]
    a_over_d = [divide_exact(a_poly, d_poly) for d_poly in d_polys]

    internal = [2, 3, 5]
    lambdas = [11, 13, 17]
    i_poly = locator(tuple(internal))
    i_prime = derivative(i_poly)
    i_zero = evaluate(i_poly, 0)
    l_basis = [
        scale(
            locator(tuple(point for point in internal if point != xi)),
            pow(evaluate(i_prime, xi), -1, P),
        )
        for xi in internal
    ]

    # Pair-Lagrange Q, stored as z coefficients which are polynomials in X.
    phi = scale(i_poly, pow(i_zero, -1, P))
    q_coefficients = [scale(a_poly, phi[index]) for index in range(e + 1)]
    for xi, lam, basis, quotient in zip(
        internal, lambdas, l_basis, a_over_d, strict=True
    ):
        parameter_factor = mul(b_poly, quotient)
        z_basis = [0] + basis
        scalar = lam * pow(xi, -1, P) % P
        for index, coefficient in enumerate(z_basis):
            q_coefficients[index] = add(
                q_coefficients[index], scale(parameter_factor, scalar * coefficient)
            )
    q_e = q_coefficients[-1]

    p_z_roots = tuple(value for value in range(6, 40) if value not in internal)[: 3 * e]
    p_z = locator(p_z_roots)
    p_z_prime = derivative(p_z)
    c_values = [
        evaluate(p_z, xi) * pow(lam, -1, P) % P
        for xi, lam in zip(internal, lambdas, strict=True)
    ]
    rho_values = [
        evaluate(p_z_prime, xi) * pow(evaluate(p_z, xi), -1, P) % P
        for xi in internal
    ]

    sigmas = [sum(pair) % P for pair in pairs]
    products = [pair[0] * pair[1] % P for pair in pairs]
    r_polys = [
        interpolate(internal, [c * product % P for c, product in zip(c_values, products)]),
        interpolate(internal, [-c * sigma % P for c, sigma in zip(c_values, sigmas)]),
        interpolate(internal, c_values),
    ]
    r_derivatives = [derivative(poly) for poly in r_polys]

    # The CRT label is the degree-<2e interpolation of xi_i on both roots of D_i.
    delta = interpolate(
        exceptional,
        [xi for xi in internal for _ in range(2)],
    )
    for xi, pair in zip(internal, pairs, strict=True):
        require(all(evaluate(delta, root) == xi for root in pair), "bad CRT label")

    boundary_values: list[list[int]] = []
    quotient_values: list[list[int]] = []
    for pair_index, pair in enumerate(pairs):
        for row in pair:
            n_values: list[int] = []
            for xi, lam, d_poly, quotient, c_i, rho_i in zip(
                internal,
                lambdas,
                d_polys,
                a_over_d,
                c_values,
                rho_values,
                strict=True,
            ):
                d_value = evaluate(d_poly, row)
                e_value = evaluate(mul(b_poly, quotient), row)
                derivative_r = sum(
                    pow(row, power, P) * evaluate(r_derivatives[power], xi)
                    for power in range(3)
                ) % P
                u_value = (
                    c_i * d_value * rho_i - derivative_r
                ) * pow(evaluate(i_prime, xi), -1, P) % P
                derivative_q = sum(
                    index * evaluate(q_coefficients[index], row)
                    for index in range(1, e + 1)
                ) % P
                n_value = (
                    e_value * u_value
                    - c_i
                    * d_value
                    * derivative_q
                    * pow(lam * evaluate(i_prime, xi), -1, P)
                ) % P
                n_values.append(n_value)

            s_row = [0]
            for d_poly, n_value, basis in zip(
                d_polys, n_values, l_basis, strict=True
            ):
                s_row = add(s_row, scale(basis, evaluate(d_poly, row) * n_value))

            xi = internal[pair_index]
            v_row = divide_exact(s_row, [(-xi) % P, 1])
            require(len(v_row) - 1 <= e - 2, "CRT quotient degree too large")

            # Check the pair-Lagrange boundary specialization used in the proof.
            q_row = [evaluate(coefficient, row) for coefficient in q_coefficients]
            expected_q = scale(
                divide_exact(mul([0, 1], i_poly), [(-xi) % P, 1]),
                evaluate(q_e, row),
            )
            require(trim(q_row) == expected_q, "exceptional Q specialization mismatch")

            inverse_c = (
                row
                * (row - s)
                * (row - x_0)
                * evaluate(derivative(a_poly), row)
                * evaluate(b_poly, row)
                * pow(domain_order, -1, P)
            ) % P
            require(inverse_c * evaluate(c_poly, row) % P == 1, "bad C inverse")
            omega_row = scale(v_row, evaluate(q_e, row) ** 2 * inverse_c)

            # FQ=C*z*I^2*Omega at A=0, checked as a z-polynomial identity.
            f_row = scale(mul(i_poly, s_row), evaluate(q_e, row))
            left = mul(f_row, q_row)
            right = scale(
                mul(mul([0, 1], mul(i_poly, i_poly)), omega_row),
                evaluate(c_poly, row),
            )
            require(left == right, "exceptional boundary weld mismatch")
            boundary_values.append(omega_row)
            quotient_values.append(v_row)

    omega_coefficients = []
    for z_degree in range(e - 1):
        omega_coefficients.append(
            interpolate(
                exceptional,
                [
                    value[z_degree] if z_degree < len(value) else 0
                    for value in boundary_values
                ],
            )
        )

    degrees = [len(poly) - 1 for poly in omega_coefficients]
    require(degrees == [5, 5], "random control unexpectedly passed degree-four gate")
    require(
        all(poly[5] != 0 for poly in omega_coefficients),
        "fifth divided-difference control vanished",
    )

    return {
        "a_poly": a_poly,
        "b_poly": b_poly,
        "boundary_values": boundary_values,
        "degrees": degrees,
        "domain_order": domain_order,
        "exceptional": exceptional,
        "q_e": q_e,
        "quotient_values": quotient_values,
        "s": s,
        "x_0": x_0,
    }


def main() -> None:
    fixture = build_fixture()
    print(
        "RATE_HALF_DISTANCE_THREE_QUARTIC_BOUNDARY_CRT_PASS "
        f"field={P} e=3 subgroup={fixture['domain_order']} "
        f"candidate_degrees={fixture['degrees']} rejected=True"
    )


if __name__ == "__main__":
    main()
