#!/usr/bin/env python3
"""Exact e=1 replay for the cleared-lift quartic router."""

from __future__ import annotations


P = 17


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
    work = numerator[:]
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse_lead = pow(denominator[-1], P - 2, P)
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
        out = add(out, scale(basis, values[index] * pow(denominator, P - 2, P)))
    return out


def check_e1_sharpness() -> list[tuple[int, int, tuple[int, ...]]]:
    e = 1
    a = [10, 10, 1]
    b = [10, 7, 3, 1]
    q_e = add(b, scale(a, -1))
    ab = mul(a, b)
    external = {15: (4, 9, 11), 2: (6, 7, 10), 4: (8, 12, 16)}
    p_z = locator(tuple(external))
    c = evaluate(p_z, 1)
    rho = evaluate(derivative(p_z), 1) * pow(c, P - 2, P) % P

    # Here D_1=A, E_1=B, lambda_1=1, I=z-1, and R=cA.
    r_term = scale(a, c)
    u_1 = scale(a, c * rho)
    n_1 = add(mul(b, u_1), scale(mul(a, q_e), -c))
    require(len(b) - 1 == 2 * e + 1, "wrong E_1 degree")
    require(len(n_1) - 1 <= 2 * e + 3, "wrong N_1 degree")

    d_common = mul(ab, q_e)
    d_y = mul(mul(a, q_e), n_1)
    active = tuple(value for block in external.values() for value in block)
    c_poly = locator(tuple(sorted(active)))

    records: list[tuple[int, int, tuple[int, ...]]] = []
    for gamma, block in external.items():
        i_value = (gamma - 1) % P
        f_gamma = add(
            mul(d_common, r_term),
            add(
                scale(mul(ab, ab), i_value * i_value),
                scale(d_y, i_value),
            ),
        )
        require(len(f_gamma) - 1 <= 4 * e + 6, "cleared degree exceeds 4e+6")

        block_poly = locator(block)
        complement = divide_exact(c_poly, block_poly)
        quartic = divide_exact(f_gamma, complement)
        roots = tuple(value for value in range(P) if evaluate(quartic, value) == 0)
        require(len(quartic) - 1 == 4, "quartic bound is not sharp")
        require(roots == (2, 5), "unexpected base-field quartic roots")

        for value in active:
            q_value = add(a, scale(q_e, gamma))
            if value in block:
                g_x = [(-gamma) % P, 1]
                h_x = divide_exact(p_z, g_x)
                expected = evaluate(mul(ab, ab), value) * evaluate(h_x, gamma) % P
                require(evaluate(f_gamma, value) == expected != 0, "incident value mismatch")
                require(evaluate(q_value, value) == 0, "block is not a Q fiber")
            else:
                require(evaluate(f_gamma, value) == 0, "missing nonincidence root")
        records.append((gamma, len(quartic) - 1, roots))

    return records


def check_e3_first_jets() -> int:
    global P
    original_field = P
    P = 1009
    try:
        e = 3
        internal = [2, 3, 5]
        lambdas = [11, 13, 17]
        pair_roots = [(31, 37), (41, 43), (47, 53)]
        triple_roots = (59, 61, 67)
        a = locator(tuple(value for pair in pair_roots for value in pair))
        b = locator(triple_roots)
        d_polys = [locator(pair) for pair in pair_roots]
        a_over_d = [divide_exact(a, d_poly) for d_poly in d_polys]
        i_poly = locator(tuple(internal))
        delta_zero = evaluate(i_poly, 0)
        phi = scale(i_poly, pow(delta_zero, P - 2, P))
        l_basis = [
            scale(
                locator(tuple(point for point in internal if point != xi)),
                pow(evaluate(derivative(i_poly), xi), P - 2, P),
            )
            for xi in internal
        ]

        checked = 0
        for row in (101, 103, 107, 109):
            a_value = evaluate(a, row)
            b_value = evaluate(b, row)
            q_row = scale(phi, a_value)
            for xi, lam, basis, quotient in zip(
                internal, lambdas, l_basis, a_over_d, strict=True
            ):
                alpha = lam * pow(xi, P - 2, P) % P
                term = mul([0, 1], basis)
                q_row = add(
                    q_row,
                    scale(term, b_value * alpha * evaluate(quotient, row)),
                )
            q_e_value = q_row[-1]
            require(q_e_value != 0, "synthetic row lost exact degree")
            g_row = scale(q_row, pow(q_e_value, P - 2, P))

            h_row = locator((211, 223, 227, 229, 233, 239))
            p_z = mul(g_row, h_row)
            constants = [
                evaluate(p_z, xi) * pow(lam, P - 2, P) % P
                for xi, lam in zip(internal, lambdas, strict=True)
            ]
            r_row = interpolate(
                internal,
                [
                    constant * evaluate(d_poly, row) % P
                    for constant, d_poly in zip(constants, d_polys, strict=True)
                ],
            )
            scale_value = b_value * evaluate(g_row, 0) % P
            scaled_h = scale(h_row, scale_value)
            j_row = divide_exact(add(scaled_h, scale(r_row, -1)), i_poly)
            require(j_row[-1] == scale_value, "synthetic lift leading coefficient mismatch")

            n_values: list[int] = []
            for index, (xi, lam, d_poly, quotient) in enumerate(
                zip(internal, lambdas, d_polys, a_over_d, strict=True)
            ):
                i_prime = evaluate(derivative(i_poly), xi)
                d_value = evaluate(d_poly, row)
                e_value = b_value * evaluate(quotient, row) % P
                rho = evaluate(derivative(p_z), xi) * pow(evaluate(p_z, xi), P - 2, P) % P
                u_value = (
                    constants[index] * d_value * rho
                    - evaluate(derivative(r_row), xi)
                ) * pow(i_prime, P - 2, P) % P
                n_value = (
                    e_value * u_value
                    - constants[index]
                    * d_value
                    * evaluate(derivative(q_row), xi)
                    * pow(lam * i_prime, P - 2, P)
                ) % P
                require(
                    evaluate(j_row, xi) == n_value * pow(e_value, P - 2, P) % P,
                    "synthetic first-jet identity mismatch",
                )
                n_values.append(n_value)

            reconstructed_j = scale(i_poly, scale_value)
            for n_value, basis, d_poly, quotient in zip(
                n_values, l_basis, d_polys, a_over_d, strict=True
            ):
                e_value = b_value * evaluate(quotient, row) % P
                reconstructed_j = add(
                    reconstructed_j,
                    scale(basis, n_value * pow(e_value, P - 2, P)),
                )
            require(reconstructed_j == j_row, "synthetic lift reconstruction mismatch")

            cleared = scale(r_row, a_value * b_value * q_e_value)
            bracket = scale(mul(i_poly, i_poly), (a_value * b_value) ** 2)
            jet_sum = [0]
            for n_value, basis, d_poly in zip(n_values, l_basis, d_polys, strict=True):
                jet_sum = add(jet_sum, scale(basis, evaluate(d_poly, row) * n_value))
            bracket = add(bracket, scale(mul(i_poly, jet_sum), q_e_value))
            cleared = add(cleared, bracket)
            require(
                cleared == scale(h_row, (a_value * b_value) ** 2),
                "synthetic cleared identity mismatch",
            )
            checked += 1
        return checked
    finally:
        P = original_field


def main() -> None:
    records = check_e1_sharpness()
    synthetic_rows = check_e3_first_jets()
    print(
        "RATE_HALF_DISTANCE_THREE_CLEARED_LIFT_QUARTIC_ROUTER_PASS "
        f"field=17 external={len(records)} records={records} "
        f"synthetic_e3_rows={synthetic_rows}"
    )


if __name__ == "__main__":
    main()
