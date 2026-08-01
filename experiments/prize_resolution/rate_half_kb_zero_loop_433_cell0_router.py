#!/usr/bin/env python3
"""Sparse exact router for zero-loop 433 common-atlas cell 0."""

import argparse
import importlib.util
import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
ATLAS = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_zero_loop_433_common_atlas.py"
)
SPEC = importlib.util.spec_from_file_location("zero_loop_atlas", ATLAS)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
PRIME = BASE.PRIME


def parity_reduce(expression, t, r, x, y, c, b):
    output = 0
    polynomial = sp.Poly(expression, t, r, c, b, modulus=PRIME)
    for (t_degree, r_degree, c_degree, b_degree), coefficient in polynomial.terms():
        output += (
            coefficient
            * t**(t_degree % 2) * x**(t_degree // 2)
            * r**(r_degree % 2) * y**(r_degree // 2)
            * c**c_degree * b**b_degree
        )
    return sp.Poly(output, t, r, x, y, c, b, modulus=PRIME).as_expr()


def stats(expression, variables):
    polynomial = sp.Poly(expression, *variables, modulus=PRIME)
    return f"degree={polynomial.total_degree()} terms={len(polynomial.terms())}"


def reduced(expression, variables):
    numerator = sp.cancel(expression).as_numer_denom()[0]
    return sp.Poly(numerator, *variables, modulus=PRIME).as_expr()


def power_x_mod(exponent, modulus, variable):
    result = sp.Poly(1, variable, modulus=PRIME)
    base = sp.Poly(variable, variable, modulus=PRIME)
    while exponent:
        if exponent & 1:
            result = (result*base).rem(modulus)
        base = (base*base).rem(modulus)
        exponent >>= 1
    return result


def evaluate(expression, substitutions):
    return int(expression.subs(substitutions)) % PRIME


def linear_roots(polynomial, variable):
    _, factors = sp.factor_list(polynomial.as_expr(), modulus=PRIME)
    roots = []
    for factor, exponent in factors:
        factor_poly = sp.Poly(factor, variable, modulus=PRIME)
        if factor_poly.degree() != 1 or exponent != 1:
            raise RuntimeError("base-root gcd did not split linearly")
        leading, constant = factor_poly.all_coeffs()
        roots.append((-int(constant)*pow(int(leading), -1, PRIME)) % PRIME)
    return tuple(sorted(roots))


def base_points(polynomials, y, b):
    basis = sp.groebner(
        list(polynomials), y, b, order="lex", method="f5b", modulus=PRIME
    )
    if len(basis.polys) == 1 and basis.polys[0].as_expr() == 1:
        return (), (1, 0, 0)
    eliminants = [
        polynomial.as_expr() for polynomial in basis.polys
        if sp.degree(polynomial.as_expr(), y) == 0
    ]
    if len(eliminants) != 1:
        raise RuntimeError("lost branch is not zero-dimensional")
    eliminant = sp.Poly(eliminants[0], b, modulus=PRIME).monic()
    frobenius = power_x_mod(PRIME, eliminant, b)
    base_b = sp.gcd(
        eliminant, frobenius-sp.Poly(b, b, modulus=PRIME)
    ).monic()
    points = []
    for b_value in linear_roots(base_b, b):
        specialized = [
            sp.Poly(polynomial.subs(b, b_value), y, modulus=PRIME)
            for polynomial in polynomials
        ]
        nonzero = [polynomial for polynomial in specialized if not polynomial.is_zero]
        if not nonzero:
            raise RuntimeError("lost branch has a vertical component")
        candidate_y = nonzero[0]
        for polynomial in nonzero[1:]:
            candidate_y = sp.gcd(candidate_y, polynomial)
        candidate_y = candidate_y.monic()
        y_frobenius = power_x_mod(PRIME, candidate_y, y)
        base_y = sp.gcd(
            candidate_y, y_frobenius-sp.Poly(y, y, modulus=PRIME)
        ).monic()
        points.extend((b_value, y_value)
                      for y_value in linear_roots(base_y, y))
    return tuple(points), (len(basis.polys), eliminant.degree(), base_b.degree())


def reconstruct(epsilon_1, epsilon_2, b_roots, trace=False, route=None,
                cell_index=0):
    if route is None:
        route = compile_route(epsilon_1, epsilon_2, cell_index=cell_index)
    y, b = route["variables"]
    (t, r, c, b_original), original_equations, guard, _ = BASE.compile_cell(
        cell_index, epsilon_1, epsilon_2
    )
    packets = []
    for b_value in b_roots:
        t_square = sp.Poly(
            route["t_square_residual"].subs(b, b_value), y, modulus=PRIME
        )
        r_square = sp.Poly(
            route["r_square_residual"].subs(b, b_value), y, modulus=PRIME
        )
        candidate_y = sp.gcd(t_square, r_square).monic()
        frobenius = power_x_mod(PRIME, candidate_y, y)
        base_y = sp.gcd(
            candidate_y, frobenius-sp.Poly(y, y, modulus=PRIME)
        ).monic()
        y_roots = linear_roots(base_y, y)
        if trace:
            print(
                "KB_ZERO_LOOP_433_CELL0_RECONSTRUCT "
                f"b={b_value} candidate_y_degree={candidate_y.degree()} "
                f"base_y_degree={base_y.degree()} y_roots={y_roots}",
                flush=True,
            )
        for y_value in y_roots:
            substitutions = {y: y_value, b: b_value}
            denominators = {
                name: evaluate(route[name], substitutions)
                for name in (
                    "c_denominator", "x_denominator", "q_determinant",
                )
            }
            if not all(denominators.values()):
                if trace:
                    print(
                        "KB_ZERO_LOOP_433_CELL0_REJECT "
                        f"b={b_value} y={y_value} reason=denominator "
                        f"values={denominators}",
                        flush=True,
                    )
                continue
            c_value = (
                evaluate(route["c_numerator"], substitutions)
                * pow(denominators["c_denominator"], -1, PRIME)
            ) % PRIME
            x_value = (
                evaluate(route["x_numerator"], substitutions)
                * pow(denominators["x_denominator"], -1, PRIME)
            ) % PRIME
            t_value = (
                evaluate(route["t_numerator"], substitutions)
                * pow(denominators["q_determinant"], -1, PRIME)
            ) % PRIME
            r_value = (
                evaluate(route["r_numerator"], substitutions)
                * pow(denominators["q_determinant"], -1, PRIME)
            ) % PRIME
            if r_value*r_value % PRIME != y_value:
                if trace:
                    print(
                        "KB_ZERO_LOOP_433_CELL0_REJECT "
                        f"b={b_value} y={y_value} reason=r_square "
                        f"r={r_value}",
                        flush=True,
                    )
                continue
            if t_value*t_value % PRIME != x_value:
                if trace:
                    print(
                        "KB_ZERO_LOOP_433_CELL0_REJECT "
                        f"b={b_value} y={y_value} reason=t_square "
                        f"t={t_value} x={x_value}",
                        flush=True,
                    )
                continue
            original_substitutions = {
                t: t_value, r: r_value, c: c_value, b_original: b_value,
            }
            residuals = tuple(
                evaluate(equation, original_substitutions)
                for equation in original_equations
            )
            if any(residuals):
                if trace:
                    print(
                        "KB_ZERO_LOOP_433_CELL0_REJECT "
                        f"b={b_value} y={y_value} reason=original "
                        f"residuals={residuals}",
                        flush=True,
                    )
                continue
            if not evaluate(guard, original_substitutions):
                if trace:
                    print(
                        "KB_ZERO_LOOP_433_CELL0_REJECT "
                        f"b={b_value} y={y_value} reason=guard",
                        flush=True,
                    )
                continue
            packets.append((b_value, c_value, r_value, t_value))
    return tuple(packets)


def compile_route(epsilon_1, epsilon_2, cell_index=0):
    (t, r, c, b), equations, _, metadata = BASE.compile_cell(
        cell_index, epsilon_1, epsilon_2, strip_fast=(cell_index == 0)
    )
    if cell_index != 0:
        _, _, _, labels, _, _, denominator = metadata
        d0, d1 = denominator
        safe_factors = [
            b, c, b-1, b+1, c-1, c+1, b-c, b+c,
        ]
        safe_factors.extend(
            labels[left]-labels[right]
            for left, right in itertools.combinations(range(5), 2)
        )
        safe_factors.extend(d0+d1*label for label in labels)
        equations = tuple(
            BASE.BASE.strip_factors(
                equation, safe_factors, (t, r, c, b)
            )
            for equation in equations
        )
    x, y = sp.symbols("x y")
    parity_equations = tuple(
        parity_reduce(equation, t, r, x, y, c, b)
        for equation in equations
    )
    p0, p1, q0, q1 = parity_equations
    if sp.degree(p0, x) > 1 or sp.degree(p1, x) > 1:
        raise RuntimeError("product rows are not linear in x")
    a0, d0 = sp.diff(p0, x), p0.subs(x, 0)
    a1, d1 = sp.diff(p1, x), p1.subs(x, 0)
    compatibility = BASE.BASE.strip_factors(
        BASE.primitive(a0*d1-a1*d0, (y, c, b)),
        (b, c, b-1, b+1, c-1, c+1, b-c, b+c, y, y-1, y+1),
        (y, c, b),
    )
    if sp.degree(compatibility, c) != 1:
        raise RuntimeError("product compatibility is not linear in c")
    c_denominator = sp.diff(compatibility, c)
    c_numerator = -compatibility.subs(c, 0)
    c_value = c_numerator/c_denominator

    x_fraction = sp.cancel((-d0/a0).subs(c, c_value))
    x_numerator, x_denominator = x_fraction.as_numer_denom()
    x_numerator = reduced(x_numerator, (y, b))
    x_denominator = reduced(x_denominator, (y, b))

    q0_sub = BASE.primitive(
        sp.together(q0.subs({x: x_fraction, c: c_value})), (t, r, y, b)
    )
    q1_sub = BASE.primitive(
        sp.together(q1.subs({x: x_fraction, c: c_value})), (t, r, y, b)
    )
    if any(sp.degree(equation, t) > 1 or sp.degree(equation, r) > 1 or
           sp.diff(sp.diff(equation, t), r) != 0
           for equation in (q0_sub, q1_sub)):
        raise RuntimeError("q rows are not affine-linear in (t,r)")
    at0 = sp.diff(q0_sub, t)
    ar0 = sp.diff(q0_sub, r)
    ac0 = q0_sub.subs({t: 0, r: 0})
    at1 = sp.diff(q1_sub, t)
    ar1 = sp.diff(q1_sub, r)
    ac1 = q1_sub.subs({t: 0, r: 0})
    determinant = reduced(at0*ar1-at1*ar0, (y, b))
    t_numerator = reduced(ar0*ac1-ar1*ac0, (y, b))
    r_numerator = reduced(ac0*at1-ac1*at0, (y, b))
    common = sp.gcd(
        sp.gcd(
            sp.Poly(determinant, y, b, modulus=PRIME),
            sp.Poly(t_numerator, y, b, modulus=PRIME),
        ),
        sp.Poly(r_numerator, y, b, modulus=PRIME),
    )
    if common.total_degree() > 0:
        determinant = sp.Poly(determinant, y, b, modulus=PRIME).exquo(common).as_expr()
        t_numerator = sp.Poly(t_numerator, y, b, modulus=PRIME).exquo(common).as_expr()
        r_numerator = sp.Poly(r_numerator, y, b, modulus=PRIME).exquo(common).as_expr()
    t_square = BASE.primitive(
        t_numerator**2*x_denominator-x_numerator*determinant**2,
        (y, b),
    )
    r_square = BASE.primitive(
        r_numerator**2-y*determinant**2, (y, b)
    )
    square_gcd = sp.gcd(
        sp.Poly(t_square, y, b, modulus=PRIME),
        sp.Poly(r_square, y, b, modulus=PRIME),
    )
    t_square_residual = sp.Poly(
        t_square, y, b, modulus=PRIME
    ).exquo(square_gcd).as_expr()
    r_square_residual = sp.Poly(
        r_square, y, b, modulus=PRIME
    ).exquo(square_gcd).as_expr()
    return {
        "variables": (y, b),
        "c_numerator": reduced(c_numerator, (y, b)),
        "c_denominator": reduced(c_denominator, (y, b)),
        "x_numerator": x_numerator,
        "x_denominator": x_denominator,
        "product": compatibility,
        "q_determinant": determinant,
        "t_numerator": t_numerator,
        "r_numerator": r_numerator,
        "t_square": t_square,
        "r_square": r_square,
        "square_gcd": square_gcd.as_expr(),
        "t_square_residual": t_square_residual,
        "r_square_residual": r_square_residual,
    }


def generic_certificate(route):
    y, b = route["variables"]
    basis = sp.groebner(
        [route["t_square_residual"], route["r_square_residual"]],
        y, b, order="lex", method="f5b", modulus=PRIME,
    )
    if not basis.is_zero_dimensional:
        raise RuntimeError("generic branch is not zero-dimensional")
    eliminants = [
        polynomial.as_expr() for polynomial in basis.polys
        if sp.degree(polynomial.as_expr(), y) == 0
    ]
    if len(eliminants) != 1:
        raise RuntimeError("expected one b eliminant")
    eliminant = BASE.BASE.strip_factors(
        eliminants[0], (b, b-1, b+1), (b,)
    )
    eliminant_poly = sp.Poly(eliminant, b, modulus=PRIME).monic()
    frobenius = power_x_mod(PRIME, eliminant_poly, b)
    root_gcd = sp.gcd(
        eliminant_poly, frobenius-sp.Poly(b, b, modulus=PRIME)
    ).monic()
    return len(basis.polys), eliminant_poly, root_gcd


def branch_certificates(route):
    y, b = route["variables"]
    branches = {
        "c_lost": (route["c_numerator"], route["c_denominator"]),
        "x_lost": (route["x_numerator"], route["x_denominator"]),
        "q_singular": (
            route["q_determinant"], route["t_numerator"],
            route["r_numerator"],
        ),
    }
    return {
        name: base_points(polynomials, y, b)
        for name, polynomials in branches.items()
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", type=int, choices=range(15), default=0)
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--dump", action="store_true")
    parser.add_argument("--basis-dump", action="store_true")
    parser.add_argument("--groebner", action="store_true")
    parser.add_argument("--order", choices=("lex", "grlex", "grevlex"),
                        default="grevlex")
    parser.add_argument("--b-root", type=int, action="append", default=[])
    parser.add_argument("--trace", action="store_true")
    parser.add_argument("--branch-audit", action="store_true")
    arguments = parser.parse_args()
    route = compile_route(
        arguments.epsilon_1, arguments.epsilon_2,
        cell_index=arguments.cell,
    )
    variables = route["variables"]
    print(
        "KB_ZERO_LOOP_433_ROUTE "
        f"cell={arguments.cell} "
        f"eps={arguments.epsilon_1},{arguments.epsilon_2}",
        flush=True,
    )
    for name in (
        "c_numerator", "c_denominator", "x_numerator", "x_denominator",
        "q_determinant",
        "t_numerator", "r_numerator", "t_square", "r_square",
        "square_gcd", "t_square_residual", "r_square_residual",
    ):
        print(f"{name} {stats(route[name], variables)}", flush=True)
        if arguments.dump:
            print(f"{name}={sp.factor(route[name])}", flush=True)
    if arguments.b_root:
        packets = reconstruct(
            arguments.epsilon_1, arguments.epsilon_2, arguments.b_root,
            trace=arguments.trace, route=route, cell_index=arguments.cell,
        )
        print(
            "KB_ZERO_LOOP_433_CELL0_PACKETS "
            f"count={len(packets)} packets={packets}",
            flush=True,
        )
    if arguments.branch_audit:
        for name, (points, branch_stats) in branch_certificates(route).items():
            print(
                "KB_ZERO_LOOP_433_CELL0_BRANCH "
                f"name={name} basis={branch_stats[0]} "
                f"eliminant_degree={branch_stats[1]} "
                f"base_b_degree={branch_stats[2]} points={points}",
                flush=True,
            )
    if arguments.groebner:
        if arguments.order == "lex":
            basis_count, eliminant_poly, root_gcd = generic_certificate(route)
            print(
                "KB_ZERO_LOOP_433_CELL0_GENERIC "
                f"unit=0 basis={basis_count} zero_dimensional=1 order=lex",
                flush=True,
            )
            print(
                "KB_ZERO_LOOP_433_CELL0_BASE_ROOTS "
                f"eliminant_degree={eliminant_poly.degree()} "
                f"root_gcd_degree={root_gcd.degree()} "
                f"root_gcd={root_gcd.as_expr()}",
                flush=True,
            )
            return
        basis = sp.groebner(
            [route["t_square_residual"], route["r_square_residual"]],
            *variables, order=arguments.order, method="f5b", modulus=PRIME,
        )
        unit = len(basis.polys) == 1 and basis.polys[0].as_expr() == 1
        print(
            "KB_ZERO_LOOP_433_CELL0_GENERIC "
            f"unit={int(unit)} basis={len(basis.polys)} "
            f"zero_dimensional={int(basis.is_zero_dimensional)} "
            f"order={arguments.order}",
            flush=True,
        )
        if arguments.basis_dump:
            for index, polynomial in enumerate(basis.polys):
                expression = polynomial.as_expr()
                print(
                    f"basis[{index}] {stats(expression, variables)} "
                    f"degrees={tuple(sp.degree(expression, variable) for variable in variables)} "
                    f"expression={expression}",
                    flush=True,
                )


if __name__ == "__main__":
    main()
