#!/usr/bin/env python3
"""Factor the sparse common-K equations for one-loop 442 cells [3,6]."""

import argparse

import sympy as sp


PRIME = 2130706433
IOTA = 16711679


def primitive(expression, variables):
    numerator = sp.cancel(expression).as_numer_denom()[0]
    polynomial = sp.Poly(sp.expand(numerator), *variables, modulus=PRIME)
    return polynomial.monic().as_expr()


def evaluate_mod(expression, substitutions):
    numerator, denominator = sp.cancel(expression.subs(substitutions)).as_numer_denom()
    numerator_value = int(numerator) % PRIME
    denominator_value = int(denominator) % PRIME
    if denominator_value == 0:
        raise ZeroDivisionError("vanishing routed denominator")
    return numerator_value * pow(denominator_value, -1, PRIME) % PRIME


def equations(epsilon_1, epsilon_2):
    b, c, r, t = sp.symbols("b c r t")
    i = sp.Integer(IOTA)
    roots = (1, t, epsilon_1 * i, r, epsilon_2 * i * r)
    labels = tuple(root**2 for root in roots)
    products = (-b**2, b, -b, c, -c)
    sums = (0, 1 + b, 1 - b, 1 + c, 1 - c)
    q_values = tuple(root * edge_sum for root, edge_sum in zip(roots, sums))

    rows = [sp.Matrix([[-p, -p * label, 1, label]])
            for p, label in zip(products, labels)]
    product_equations = []
    for fourth in (3, 4):
        matrix = sp.Matrix.vstack(rows[0], rows[1], rows[2], rows[fourth])
        product_equations.append(sp.expand(matrix.det() / b))

    weld_equations = []
    for third in (3, 4):
        left, right = 1, 2
        differences = tuple(products[0] - value for value in products)
        weld = (
            q_values[left] * differences[right] * differences[third]
            * (labels[third] - labels[right])
            + q_values[right] * differences[left] * differences[third]
            * (labels[left] - labels[third])
            + q_values[third] * differences[left] * differences[right]
            * (labels[right] - labels[left])
        )
        weld_equations.append(sp.expand(weld / (b * (b - 1) * (b + 1))))
    return (b, c, r, t), product_equations, weld_equations


def route(epsilon_1, epsilon_2):
    (b, c, r, t), (p_left, p_right), (q_left, q_right) = equations(
        epsilon_1, epsilon_2
    )
    a_left = sp.diff(p_left, c)
    b_left = p_left.subs(c, 0)
    a_right = sp.diff(p_right, c)
    b_right = p_right.subs(c, 0)
    compatibility = primitive(a_left * b_right - a_right * b_left, (b, r, t))
    c_value = -b_left / a_left

    q_left_numerator = primitive(q_left.subs(c, c_value), (b, r, t))
    q_right_numerator = primitive(q_right.subs(c, c_value), (b, r, t))
    print(f"CELL36_SPARSE_ROW eps={epsilon_1},{epsilon_2}", flush=True)
    print(
        "raw_terms="
        f"{len(sp.Poly(compatibility, b, r, t, modulus=PRIME).terms())},"
        f"{len(sp.Poly(q_left_numerator, b, r, t, modulus=PRIME).terms())},"
        f"{len(sp.Poly(q_right_numerator, b, r, t, modulus=PRIME).terms())}",
        flush=True,
    )

    guard_factors = (b, b - 1, b + 1, r - t, r + t, r - IOTA, r + IOTA,
                     t - 1, t + 1, t - IOTA, t + IOTA, t**2 + 1)
    residual = sp.Poly(q_left_numerator, b, r, t, modulus=PRIME)
    removed = []
    for guard in guard_factors:
        guard_polynomial = sp.Poly(guard, b, r, t, modulus=PRIME)
        multiplicity = 0
        while True:
            quotient, remainder = sp.div(residual, guard_polynomial)
            if not remainder.is_zero:
                break
            residual = quotient
            multiplicity += 1
        if multiplicity:
            removed.append((guard, multiplicity))
    residual_expression = residual.monic().as_expr()
    if sp.Poly(residual_expression, b, r, t, modulus=PRIME).degree(t) != 1:
        raise RuntimeError("guard-stripped first weld is not linear in t")

    t_coefficient = sp.diff(residual_expression, t)
    t_constant = residual_expression.subs(t, 0)
    t_value = -t_constant / t_coefficient
    compatibility_routed = primitive(
        compatibility.subs(t, t_value), (b, r)
    )
    q_right_routed = primitive(q_right_numerator.subs(t, t_value), (b, r))
    print(f"removed_guards={removed}", flush=True)
    print(f"linear_t={residual_expression}", flush=True)
    print(f"t_value={sp.cancel(t_value)}", flush=True)
    print(
        "routed_terms="
        f"{len(sp.Poly(compatibility_routed, b, r, modulus=PRIME).terms())},"
        f"{len(sp.Poly(q_right_routed, b, r, modulus=PRIME).terms())}",
        flush=True,
    )
    routed_gcd = sp.gcd(
        sp.Poly(compatibility_routed, b, r, modulus=PRIME),
        sp.Poly(q_right_routed, b, r, modulus=PRIME),
    ).monic().as_expr()

    print(f"routed_gcd={routed_gcd}", flush=True)
    print(
        f"routed_factors={sp.factor_list(routed_gcd, modulus=PRIME)[1]}",
        flush=True,
    )
    compatibility_reduced = sp.exquo(
        sp.Poly(compatibility_routed, b, r, modulus=PRIME),
        sp.Poly(routed_gcd, b, r, modulus=PRIME),
    ).as_expr()
    q_right_reduced = sp.exquo(
        sp.Poly(q_right_routed, b, r, modulus=PRIME),
        sp.Poly(routed_gcd, b, r, modulus=PRIME),
    ).as_expr()
    resultant = primitive(
        sp.resultant(compatibility_reduced, q_right_reduced, b), (r,)
    )
    print(f"resultant_b={resultant}", flush=True)
    resultant_factors = sp.factor_list(resultant, modulus=PRIME)[1]
    print(f"resultant_factors={resultant_factors}", flush=True)
    for factor, _ in resultant_factors:
        factor_polynomial = sp.Poly(factor, r, modulus=PRIME)
        if factor_polynomial.degree() != 1:
            continue
        coefficient, constant = factor_polynomial.all_coeffs()
        root = int(-constant * coefficient**-1) % PRIME
        if root in (0, 1, PRIME - 1, IOTA, PRIME - IOTA):
            continue
        b_gcd = sp.gcd(
            sp.Poly(compatibility_reduced.subs(r, root), b, modulus=PRIME),
            sp.Poly(q_right_reduced.subs(r, root), b, modulus=PRIME),
        ).monic().as_expr()
        print(f"linear_root={root} b_gcd={b_gcd}", flush=True)
        for b_factor, _ in sp.factor_list(b_gcd, modulus=PRIME)[1]:
            b_polynomial = sp.Poly(b_factor, b, modulus=PRIME)
            if b_polynomial.degree() != 1:
                continue
            b_coefficient, b_constant = b_polynomial.all_coeffs()
            b_root = int(-b_constant * b_coefficient**-1) % PRIME
            t_root = evaluate_mod(t_value, {r: root})
            c_root = evaluate_mod(c_value, {r: root, t: t_root, b: b_root})
            labels = (1, t_root**2 % PRIME, PRIME - 1,
                      root**2 % PRIME, -(root**2) % PRIME)
            products = (-(b_root**2) % PRIME, b_root, -b_root % PRIME,
                        c_root, -c_root % PRIME)
            guarded = (
                0 not in labels and len(set(labels)) == 5
                and 0 not in products and len(set(products)) == 5
            )
            substitutions = {r: root, b: b_root, t: t_root, c: c_root}
            equations_hold = all(
                evaluate_mod(equation, substitutions) == 0
                for equation in (p_left, p_right, q_left, q_right)
            )
            print(
                f"witness r={root} b={b_root} t={t_root} c={c_root} "
                f"guarded={int(guarded)} equations={int(equations_hold)}",
                flush=True,
            )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), required=True)
    arguments = parser.parse_args()
    route(arguments.epsilon_1, arguments.epsilon_2)


if __name__ == "__main__":
    main()
