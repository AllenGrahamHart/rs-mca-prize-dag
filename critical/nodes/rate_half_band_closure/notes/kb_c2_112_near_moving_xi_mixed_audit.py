#!/usr/bin/env python3
"""Independent fraction-free and quotient-Frobenius mixed-chart audit."""

from __future__ import annotations

import argparse
import hashlib

import sympy as sp
from sympy.polys.matrices import DomainMatrix


P = 2130706433


def check(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def digest(polynomial: sp.Poly) -> str:
    payload = repr([
        (monomial, str(coefficient))
        for monomial, coefficient in polynomial.monic().terms()
    ]).encode("ascii")
    return hashlib.sha256(payload).hexdigest()[:16]


def edge_vector(x, y):
    return sp.Matrix([x * y, -(x + y), 1])


def rows_at(x):
    return (
        sp.Matrix([[1, x, x**2, 0, 0]]),
        sp.Matrix([[0, 0, 0, 1 + x**2, x]]),
        sp.Matrix([[x**2, x, 1, 0, 0]]),
    )


def numerator_poly(expression, b, c, d):
    numerator = sp.fraction(sp.cancel(expression))[0]
    return sp.Poly(numerator, b, c, d, domain=sp.QQ).primitive()[1]


def reconstruct_cores(*, fraction_free: bool):
    b, c, d = sp.symbols("b c d", nonzero=True)
    a = sp.Rational(2)
    w = 1 / c
    q0 = c * d
    q1 = -(c + d)
    odd0 = q0 - w
    odd2 = 1 - w * q0
    odd1 = q1 * (1 - w)
    z = sp.cancel(
        -(odd0 + a * odd1 + a**2 * odd2)
        / (odd2 + a * odd1 + a**2 * odd0)
    )
    odd_at_z = sp.Matrix([
        odd0 + z * odd2,
        (1 + z) * odd1,
        odd2 + z * odd0,
    ])
    ell1 = odd_at_z[2]
    ell0 = odd_at_z[1] + a * odd_at_z[2]
    fixed = edge_vector(a, 1 / a)
    moving = edge_vector(a, b)
    interpolation = sp.Matrix([
        sp.cancel(value)
        for value in (
            ((ell0 + b * ell1) * fixed
             + (ell0 + sp.Rational(1, 2) * ell1) * moving)
            / (b - sp.Rational(1, 2))
        )
    ])

    at_w = rows_at(w)
    at_z = rows_at(z)
    source_matrix = sp.Matrix.vstack(
        at_w[0] - q0 * at_w[2],
        at_w[1] - q1 * at_w[2],
        *at_z,
    )
    source_rhs = sp.Matrix([0, 0, *interpolation])
    if fraction_free:
        matrix_domain = DomainMatrix.from_Matrix(source_matrix)
        rhs_domain = DomainMatrix.from_Matrix(source_rhs)
        matrix_domain, rhs_domain = matrix_domain.unify(rhs_domain, fmt="dense")
        numerator, denominator = matrix_domain.solve_den(rhs_domain)
        check(
            matrix_domain.matmul(numerator)
            == rhs_domain.scalarmul(denominator),
            "fraction-free source identity",
        )
        denominator_expression = matrix_domain.domain.to_sympy(denominator)
        coefficients = [
            sp.cancel(value / denominator_expression)
            for value in numerator.to_Matrix()
        ]
    else:
        coefficients = [
            sp.cancel(value)
            for value in source_matrix.inv(method="DM") * source_rhs
        ]

    def residual(root):
        x0, x1, x2, x3, x4 = coefficients
        even0 = sp.cancel(x0 + root * x3 + root**2 * x2)
        even1 = sp.cancel(x1 + root * x4 + root**2 * x1)
        even2 = sp.cancel(x2 + root * x3 + root**2 * x0)
        local_odd0 = sp.cancel(odd0 + root * odd1 + root**2 * odd2)
        local_odd1 = sp.cancel(odd2 + root * odd1 + root**2 * odd0)
        check(
            sp.cancel(even0 + w * even1 + w**2 * even2) == 0,
            "even forced root",
        )
        check(
            sp.cancel(local_odd0 + w * local_odd1) == 0,
            "odd forced root",
        )
        leading = sp.cancel(even2**2)
        middle = sp.cancel(
            2 * even1 * even2 - local_odd1**2 + 2 * w * leading
        )
        constant = sp.cancel(even0**2 / w**2)
        return leading, middle, constant

    finite_incidence = (
        4 * c**2 * d - 2 * c**2 - 3 * c * d
        + 3 * c + 2 * d - 4
    )
    cores = {}
    for root_name, root in (("c", c), ("d", d)):
        leading, middle, constant = residual(root)
        equations = {
            "product": constant - leading / (b * d),
            "sum": middle + (1 / b + 1 / d) * leading,
        }
        for kind, equation in equations.items():
            polynomial = numerator_poly(equation, b, c, d)
            if kind == "product":
                polynomial = polynomial.exquo(
                    sp.Poly(
                        finite_incidence**2,
                        b,
                        c,
                        d,
                        domain=sp.QQ,
                    )
                ).primitive()[1]
            cores[(root_name, kind)] = polynomial

    expected = {
        ("c", "product"): ((3, 6, 5), 154, "5117a5676cc0bdb9"),
        ("c", "sum"): ((3, 10, 7), 341, "b052e13bbf0f28fe"),
        ("d", "product"): ((3, 6, 5), 150, "70cb7c16ac2f1e3e"),
        ("d", "sum"): ((3, 10, 7), 341, "0ed07280609cd604"),
    }
    for key, (degrees, terms, wanted_digest) in expected.items():
        polynomial = cores[key]
        check(
            tuple(polynomial.degree(x) for x in (b, c, d)) == degrees,
            f"audit core degrees {key}",
        )
        check(len(polynomial.terms()) == terms, f"audit core terms {key}")
        check(digest(polynomial) == wanted_digest, f"audit core digest {key}")
    return (b, c, d), cores, finite_incidence


def integral_expression(polynomial: sp.Poly):
    _, integral = polynomial.clear_denoms(convert=True)
    return integral.as_expr()


def terminal_subresultant(left, right, eliminate, *remaining):
    sequence = sp.subresultants(left.as_expr(), right.as_expr(), eliminate)
    check(bool(sequence), "empty subresultant sequence")
    terminal = sp.Poly(sequence[-1], eliminate, *remaining, domain=sp.QQ)
    check(terminal.degree(eliminate) == 0, "nonconstant terminal subresultant")
    return sp.Poly(
        terminal.as_expr(), *remaining, domain=sp.QQ
    ).primitive()[1]


def audit_router(mode, variables, cores):
    b, c, d = variables
    parent_pairs = {
        "parent-c": (("c", "product"), ("c", "sum")),
        "parent-d": (("d", "product"), ("d", "sum")),
        "parent-product": (("c", "product"), ("d", "product")),
    }
    expected_parent = {
        "parent-c": (
            "497875a2420d1711",
            {
                "4aa033e0505df8f1": 4, "73c55ff149852dee": 4,
                "19d832b1f64387da": 2, "dbe56c4d43b264a2": 4,
                "cb4fd487538b0eff": 4, "7a7743ce53fe8f77": 8,
                "477785c532483181": 10, "bed4496a0af11b8c": 2,
                "842d5d9a084f107e": 1,
            },
        ),
        "parent-d": (
            "67d9beffee34fed1",
            {
                "6a515ecf832aff78": 4, "e31255d5e81e2509": 4,
                "19d832b1f64387da": 2, "4975135dd6af0fc0": 4,
                "7a7743ce53fe8f77": 4, "dbe56c4d43b264a2": 4,
                "824f64bb4a05a043": 4, "cb4fd487538b0eff": 4,
                "477785c532483181": 6, "8d63799ea7b1c3fc": 2,
                "39ad8e659560b1b1": 1,
            },
        ),
        "parent-product": (
            "f3c414f60e67c7c5",
            {
                "6a515ecf832aff78": 2, "e31255d5e81e2509": 2,
                "19d832b1f64387da": 1, "7a7743ce53fe8f77": 1,
                "824f64bb4a05a043": 2, "a4ef916fb9e856d1": 3,
                "477785c532483181": 5, "dbe56c4d43b264a2": 5,
                "cb4fd487538b0eff": 7, "ddb8e78f19e438e9": 1,
                "9274da18c1badf2f": 1,
            },
        ),
    }
    if mode in parent_pairs:
        left_key, right_key = parent_pairs[mode]
        resultant = terminal_subresultant(
            cores[left_key], cores[right_key], b, c, d
        )
        factors = {
            digest(sp.Poly(value, c, d, domain=sp.QQ)): exponent
            for value, exponent in sp.factor_list(resultant.as_expr())[1]
        }
        expected_digest, expected_factors = expected_parent[mode]
        check(digest(resultant) == expected_digest, "parent subresultant digest")
        check(factors == expected_factors, "parent subresultant factor census")
        print(
            "KB_C2_112_NEAR_MOVING_XI_MIXED_PARENT_AUDIT_PASS "
            f"router={mode}",
            flush=True,
        )
        return

    low_c = sp.Poly(
        2*c**3*d**2 - 5*c**3*d + 2*c**3
        - 14*c**2*d**2 + 11*c**2*d - 2*c**2
        + 4*c*d**2 + 5*c*d - 8*c + 2*d**2 - 11*d + 14,
        c, d, domain=sp.QQ,
    )
    low_d = sp.Poly(
        2*c**3*d**2 - 2*c**3 - 19*c**2*d**2
        + 6*c**2*d + 7*c**2 + 13*c*d**2 - 13*c
        - 2*d**2 - 6*d + 14,
        c, d, domain=sp.QQ,
    )
    if mode == "low00":
        projection = terminal_subresultant(low_c, low_d, c, d)
        check(digest(projection) == "0a919d544c404dbc", "low/low audit digest")
        factors = {
            digest(sp.Poly(value, d, domain=sp.QQ)): exponent
            for value, exponent in sp.factor_list(projection.as_expr())[1]
        }
        check(
            factors == {
                "f93c38ef339888a3": 1, "b8907990ebf04ed3": 1,
                "6e8238e7c5913d2e": 1, "3e8b7ae50a0eb368": 3,
                "bc3da4bcdb93303f": 3, "96c6e25ebf804bc6": 1,
            },
            "low/low audit factor census",
        )
        modular_factors = sp.factor_list(
            sp.Poly(projection.as_expr(), d, modulus=P).monic().as_expr(),
            modulus=P,
        )[1]
        actual_relevant = {
            str(sp.Poly(value, d, modulus=P).monic().as_expr())
            for value, _ in modular_factors
            if 6 % sp.Poly(value, d, modulus=P).degree() == 0
        }
        expected_relevant = {
            str(sp.Poly(value, d, modulus=P).monic().as_expr())
            for value in (
                d - 2, 2*d - 1, d - 1, d + 1,
                d + 784997106, d + 229355720,
                d**2 + 835997487*d - 634784751,
            )
        }
        check(
            actual_relevant == expected_relevant,
            "low/low audit relevant-field coverage",
        )
        print("KB_C2_112_NEAR_MOVING_XI_MIXED_LOW_ROUTER_AUDIT_PASS", flush=True)
        return

    within = {}
    roots_needed = ("c", "d") if mode in ("w01", "w10") else ("c",)
    for root_name in roots_needed:
        value = terminal_subresultant(
            cores[(root_name, "product")],
            cores[(root_name, "sum")],
            b,
            c,
            d,
        )
        selected = [
            sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
            for factor, _ in sp.factor_list(value.as_expr())[1]
            if (sp.Poly(factor, c, d).degree(c),
                sp.Poly(factor, c, d).degree(d)) in ((3, 2), (16, 14))
        ]
        check(len(selected) == 2, "audit within-component count")
        within[root_name] = sorted(selected, key=lambda item: item.degree(c))

    if mode in ("w01", "w10"):
        left_index, right_index = ((0, 1) if mode == "w01" else (1, 0))
        left = within["c"][left_index]
        right = within["d"][right_index]
        projection = terminal_subresultant(left, right, c, d)
        expected = {
            "w01": ("f3a12aa7b6f6df31", "995db6566e31698c", [1, 2, 2, 4, 4, 27]),
            "w10": ("dc1340ad1ecc496b", "e364442d07376273", [1, 1, 6, 32]),
        }[mode]
        check(digest(projection) == expected[0], "degree-40 audit projection")
        factors = [
            (sp.Poly(value, d, domain=sp.QQ).primitive()[1], exponent)
            for value, exponent in sp.factor_list(projection.as_expr())[1]
        ]
        candidate = next(value for value, _ in factors if value.degree() == 40)
        check(digest(candidate) == expected[1], "degree-40 audit factor")
        _, integral = candidate.clear_denoms(convert=True)
        modular_factors = sp.factor_list(integral.as_expr(), modulus=P)[1]
        check(
            sorted(
                sp.Poly(value, d, modulus=P).degree()
                for value, exponent in modular_factors
                for _ in range(exponent)
            ) == expected[2],
            "degree-40 audit modular census",
        )
        relevant_candidates = {
            "w01": (
                d - 616787200,
                d**2 - 746249270*d - 422041203,
                d**2 - 588829660*d + 482711260,
            ),
            "w10": (
                d + 288571956,
                d - 487213652,
                d**6 + 714848107*d**5 + 703111546*d**4
                + 252897233*d**3 + 344006764*d**2
                - 1006662141*d - 110939493,
            ),
        }[mode]
        actual_relevant = {
            str(sp.Poly(value, d, modulus=P).monic().as_expr())
            for value, _ in modular_factors
            if 6 % sp.Poly(value, d, modulus=P).degree() == 0
        }
        expected_relevant = {
            str(sp.Poly(value, d, modulus=P).monic().as_expr())
            for value in relevant_candidates
        }
        check(
            actual_relevant == expected_relevant,
            "degree-40 audit relevant-field coverage",
        )
        print(
            "KB_C2_112_NEAR_MOVING_XI_MIXED_DEGREE40_ROUTER_AUDIT_PASS "
            f"router={mode}",
            flush=True,
        )
        return

    check(mode in ("hp0", "hp1"), "unknown router mode")
    high = within["c"][1]
    product_cross = terminal_subresultant(
        cores[("c", "product")], cores[("d", "product")], b, c, d
    )
    cross_digest = "ddb8e78f19e438e9" if mode == "hp0" else "9274da18c1badf2f"
    cross = next(
        sp.Poly(value, c, d, domain=sp.QQ).primitive()[1]
        for value, _ in sp.factor_list(product_cross.as_expr())[1]
        if digest(sp.Poly(value, c, d, domain=sp.QQ)) == cross_digest
    )
    coefficient_domain = sp.GF(P).poly_ring(d)
    high_mod = sp.Poly(high.as_expr(), c, domain=coefficient_domain)
    cross_mod = sp.Poly(cross.as_expr(), c, domain=coefficient_domain)
    sequence = high_mod.subresultants(cross_mod)
    check(bool(sequence) and sequence[-1].degree(c) == 0,
          "modular terminal subresultant")
    projection = sp.Poly(sequence[-1].as_expr(), d, modulus=P).monic()
    expected = {
        "hp0": ("6970b9ab5bbc89f6", [
            (1, 1), (1, 2), (1, 10), (2, 1), (2, 1), (2, 2),
            (4, 1), (5, 1), (7, 1), (7, 1),
        ]),
        "hp1": ("883a93b7debea09a", [
            (1, 1), (1, 14), (1, 26), (1, 40), (1, 42),
            (2, 1), (2, 1), (3, 1), (3, 1), (4, 1), (6, 1),
            (7, 1), (7, 1), (8, 1), (11, 1), (12, 1),
            (17, 1), (25, 1), (52, 1),
        ]),
    }[mode]
    check(digest(projection) == expected[0], "high audit projection digest")
    modular_factors = sp.factor_list(projection.as_expr(), modulus=P)[1]
    check(
        sorted(
            (sp.Poly(value, d, modulus=P).degree(), exponent)
            for value, exponent in modular_factors
        ) == expected[1],
        "high audit modular factor census",
    )
    relevant_candidates = {
        "hp0": (
            2*d - 1,
            d + 927463048, d + 80227901,
            d**2 + 958999809*d + 65368811,
            d**2 - 826991582*d - 202957287,
            d**2 - 80227901*d - 730078611,
        ),
        "hp1": (
            d + 1, d - 2, d - 1, 2*d - 1,
            d + 895796957,
            d**2 + 8543134*d - 269706851,
            d**2 - 832867459*d - 841426149,
            d**3 + 720406365*d**2 + 262219802*d + 854470722,
            d**3 - 562719028*d**2 + 744345501*d + 69494986,
            d**6 - 346957095*d**5 + 367719326*d**4
            + 829539208*d**3 + 382622521*d**2
            - 497110350*d + 206580260,
        ),
    }[mode]
    actual_relevant = {
        str(sp.Poly(value, d, modulus=P).monic().as_expr())
        for value, _ in modular_factors
        if 6 % sp.Poly(value, d, modulus=P).degree() == 0
    }
    expected_relevant = {
        str(sp.Poly(value, d, modulus=P).monic().as_expr())
        for value in relevant_candidates
    }
    check(
        actual_relevant == expected_relevant,
        "high audit relevant-field coverage",
    )
    print(
        "KB_C2_112_NEAR_MOVING_XI_MIXED_HIGH_ROUTER_AUDIT_PASS "
        f"router={mode}",
        flush=True,
    )


def quotient_power(basis, value, exponent):
    result = sp.Integer(1)
    base = basis.reduce(value)[1]
    while exponent:
        if exponent & 1:
            result = basis.reduce(result * base)[1]
        exponent >>= 1
        if exponent:
            base = basis.reduce(base * base)[1]
    return basis.reduce(result)[1]


def audit_field(mode, variables, cores, finite_incidence):
    b, c, d = variables
    candidates = {
        "field-low-d17": d + 784997106,
        "field-low-q3-l": d + 229355720,
        "field-low-q3-q": d**2 + 835997487*d - 634784751,
        "field-w01-l": d - 616787200,
        "field-w01-q0": d**2 - 746249270*d - 422041203,
        "field-w01-q1": d**2 - 588829660*d + 482711260,
        "field-w10-l0": d + 288571956,
        "field-w10-l1": d - 487213652,
        "field-w10-s6": (
            d**6 + 714848107*d**5 + 703111546*d**4
            + 252897233*d**3 + 344006764*d**2
            - 1006662141*d - 110939493
        ),
        "field-hp0-l0": d + 927463048,
        "field-hp0-l1": d + 80227901,
        "field-hp0-q0": d**2 + 958999809*d + 65368811,
        "field-hp0-q1": d**2 - 826991582*d - 202957287,
        "field-hp0-q2": d**2 - 80227901*d - 730078611,
        "field-hp1-l0": d + 895796957,
        "field-hp1-q0": d**2 + 8543134*d - 269706851,
        "field-hp1-q1": d**2 - 832867459*d - 841426149,
        "field-hp1-r0": d**3 + 720406365*d**2 + 262219802*d + 854470722,
        "field-hp1-r1": d**3 - 562719028*d**2 + 744345501*d + 69494986,
        "field-hp1-s6": (
            d**6 - 346957095*d**5 + 367719326*d**4
            + 829539208*d**3 + 382622521*d**2
            - 497110350*d + 206580260
        ),
    }
    candidate = sp.Poly(candidates[mode], d, modulus=P).monic()
    factorization = sp.factor_list(candidate.as_expr(), modulus=P)[1]
    check(
        len(factorization) == 1
        and factorization[0][1] == 1
        and sp.Poly(factorization[0][0], d, modulus=P).monic() == candidate,
        "audit candidate irreducibility",
    )
    basis = sp.groebner(
        [
            *(integral_expression(value) for value in cores.values()),
            candidate.as_expr(),
        ],
        b,
        c,
        d,
        order="lex",
        modulus=P,
    )
    print(
        f"audit_stage=field_basis fiber={mode} size={len(basis.polys)}",
        flush=True,
    )
    if len(basis.polys) == 1 and basis.polys[0].as_expr() == 1:
        print(
            "KB_C2_112_NEAR_MOVING_XI_MIXED_FIELD_AUDIT_PASS "
            f"fiber={mode} reason=unit",
            flush=True,
        )
        return

    extension_degree = candidate.degree()
    relation = tuple(
        int(value) % P
        for value in reversed(candidate.monic().all_coeffs()[1:])
    )
    zero = (0,) * extension_degree
    one = (1,) + (0,) * (extension_degree - 1)

    def kvalue(value):
        return (int(value) % P,) + (0,) * (extension_degree - 1)

    d_root = (
        ((-relation[0]) % P,) if extension_degree == 1
        else (0, 1) + (0,) * (extension_degree - 2)
    )

    def kadd(left, right):
        return tuple((x + y) % P for x, y in zip(left, right))

    def ksub(left, right):
        return tuple((x - y) % P for x, y in zip(left, right))

    def kmul(left, right):
        product = [0] * (2 * extension_degree - 1)
        for i, x in enumerate(left):
            for j, y in enumerate(right):
                product[i + j] = (product[i + j] + x * y) % P
        for degree in range(
            2 * extension_degree - 2, extension_degree - 1, -1
        ):
            coefficient = product[degree]
            if coefficient:
                for index, value in enumerate(relation):
                    target = degree - extension_degree + index
                    product[target] = (
                        product[target] - coefficient * value
                    ) % P
        return tuple(product[:extension_degree])

    def kinv(value):
        check(value != zero, "zero residue-field inverse")
        return kpow(value, P**extension_degree - 2)

    def kpow(value, exponent):
        result = one
        base = value
        while exponent:
            if exponent & 1:
                result = kmul(result, base)
            exponent >>= 1
            if exponent:
                base = kmul(base, base)
        return result

    def trim(polynomial):
        result = list(polynomial)
        while result and result[-1] == zero:
            result.pop()
        return result

    def padd(left, right):
        return trim([
            kadd(
                left[index] if index < len(left) else zero,
                right[index] if index < len(right) else zero,
            )
            for index in range(max(len(left), len(right)))
        ])

    def psub(left, right):
        return trim([
            ksub(
                left[index] if index < len(left) else zero,
                right[index] if index < len(right) else zero,
            )
            for index in range(max(len(left), len(right)))
        ])

    def pmul(left, right):
        if not left or not right:
            return []
        result = [zero] * (len(left) + len(right) - 1)
        for i, left_value in enumerate(left):
            for j, right_value in enumerate(right):
                result[i + j] = kadd(
                    result[i + j], kmul(left_value, right_value)
                )
        return trim(result)

    def pdivmod(dividend, divisor):
        remainder = trim(dividend)
        divisor = trim(divisor)
        check(bool(divisor), "zero residue-field polynomial divisor")
        quotient = [zero] * max(0, len(remainder) - len(divisor) + 1)
        inverse_lead = kinv(divisor[-1])
        while len(remainder) >= len(divisor):
            shift = len(remainder) - len(divisor)
            coefficient = kmul(remainder[-1], inverse_lead)
            quotient[shift] = coefficient
            remainder = psub(
                remainder,
                [zero] * shift
                + [kmul(coefficient, value) for value in divisor],
            )
        return trim(quotient), remainder

    def pmonic(polynomial):
        polynomial = trim(polynomial)
        if not polynomial:
            return []
        scale = kinv(polynomial[-1])
        return [kmul(scale, value) for value in polynomial]

    def pgcd(left, right):
        left = trim(left)
        right = trim(right)
        while right:
            left, right = right, pdivmod(left, right)[1]
        return pmonic(left)

    def ppowmod(base, exponent, modulus_polynomial):
        result = [one]
        base = pdivmod(base, modulus_polynomial)[1]
        while exponent:
            if exponent & 1:
                result = pdivmod(
                    pmul(result, base), modulus_polynomial
                )[1]
            exponent >>= 1
            if exponent:
                base = pdivmod(pmul(base, base), modulus_polynomial)[1]
        return result

    def split_linear(polynomial, output):
        polynomial = pmonic(polynomial)
        degree = len(polynomial) - 1
        if degree == 1:
            output.append(polynomial)
            return
        field_order = P**extension_degree
        for seed in range(1, 257):
            constant = tuple(
                pow(seed, index + 1, P)
                for index in range(extension_degree)
            )
            trial = [constant, one]
            powered = ppowmod(
                trial, (field_order - 1) // 2, polynomial
            )
            divisor = pgcd(polynomial, psub(powered, [one]))
            divisor_degree = len(divisor) - 1
            if 0 < divisor_degree < degree:
                quotient, remainder = pdivmod(polynomial, divisor)
                check(not remainder, "residue-field split remainder")
                split_linear(divisor, output)
                split_linear(quotient, output)
                return
        raise RuntimeError("deterministic residue-field split failed")

    c_eliminant = next(
        value for value in basis.polys
        if value.degree(b) == 0 and value.degree(c) > 0
    )
    c_source = sp.Poly(c_eliminant.as_expr(), c, d, modulus=P)
    c_polynomial = [zero] * (c_source.degree(c) + 1)
    for (c_degree, d_degree), coefficient in c_source.terms():
        c_polynomial[c_degree] = kadd(
            c_polynomial[c_degree],
            kmul(kvalue(int(coefficient)), kpow(d_root, d_degree)),
        )
    c_polynomial = pmonic(c_polynomial)
    x_polynomial = [zero, one]
    c_target = pgcd(
        c_polynomial,
        psub(ppowmod(x_polynomial, P**6, c_polynomial), x_polynomial),
    )
    c_base = pgcd(
        c_target,
        psub(
            ppowmod(
                x_polynomial, P**extension_degree, c_polynomial
            ),
            x_polynomial,
        ),
    )
    check(c_target == c_base, "relative c roots omitted by base-field audit")
    c_factors = []
    if len(c_base) > 1:
        split_linear(c_base, c_factors)
    check(
        len(c_factors) == len(c_base) - 1,
        "incomplete residue-field c splitting",
    )

    integral_cores = [
        sp.Poly(integral_expression(value), b, c, d, modulus=P)
        for value in cores.values()
    ]
    point_count = 0
    label_count = 0
    half = kvalue(pow(2, -1, P))
    minus_one = kvalue(-1)
    two = kvalue(2)
    for c_factor in c_factors:
        c_root = ksub(zero, c_factor[0])
        b_polynomials = []
        for source in integral_cores:
            coefficients = [zero] * (source.degree(b) + 1)
            for (b_degree, c_degree, d_degree), coefficient in source.terms():
                coefficients[b_degree] = kadd(
                    coefficients[b_degree],
                    kmul(
                        kvalue(int(coefficient)),
                        kmul(
                            kpow(c_root, c_degree),
                            kpow(d_root, d_degree),
                        ),
                    ),
                )
            b_polynomials.append(trim(coefficients))
        b_common = b_polynomials[0]
        for polynomial in b_polynomials[1:]:
            b_common = pgcd(b_common, polynomial)
        if len(b_common) <= 1:
            continue
        b_target = pgcd(
            b_common,
            psub(ppowmod(x_polynomial, P**6, b_common), x_polynomial),
        )
        b_base = pgcd(
            b_target,
            psub(
                ppowmod(
                    x_polynomial, P**extension_degree, b_common
                ),
                x_polynomial,
            ),
        )
        check(
            b_target == b_base,
            "relative b roots omitted by base-field audit",
        )
        b_factors = []
        if len(b_base) > 1:
            split_linear(b_base, b_factors)
        check(
            len(b_factors) == len(b_base) - 1,
            "incomplete residue-field b splitting",
        )
        for b_factor in b_factors:
            b_root = ksub(zero, b_factor[0])
            point_count += 1
            reconstruction = kadd(
                ksub(
                    ksub(
                        kmul(kvalue(5), kmul(c_root, d_root)),
                        kmul(kvalue(4), c_root),
                    ),
                    kmul(kvalue(4), d_root),
                ),
                kvalue(5),
            )
            incidence = kadd(
                ksub(
                    kadd(
                        ksub(
                            kmul(
                                kvalue(4),
                                kmul(kmul(c_root, c_root), d_root),
                            ),
                            kmul(kvalue(2), kmul(c_root, c_root)),
                        ),
                        kmul(kvalue(3), c_root),
                    ),
                    kmul(kvalue(3), kmul(c_root, d_root)),
                ),
                ksub(kmul(kvalue(2), d_root), kvalue(4)),
            )
            forbidden = (
                b_root == zero or c_root == zero or d_root == zero
                or b_root in (one, minus_one, two, half)
                or c_root in (one, minus_one, two, half)
                or d_root in (one, minus_one, two, half)
                or b_root == c_root or b_root == d_root or c_root == d_root
                or kmul(b_root, c_root) == one
                or kmul(b_root, d_root) == one
                or kmul(c_root, d_root) == one
                or reconstruction == zero or incidence == zero
            )
            check(forbidden, "admissible residue-field point")
            label_count += int(forbidden)
    print(
        "KB_C2_112_NEAR_MOVING_XI_MIXED_FIELD_AUDIT_PASS "
        f"fiber={mode} c_roots={len(c_factors)} "
        f"points={point_count} forbidden={label_count}",
        flush=True,
    )


def main() -> None:
    router_modes = (
        "parent-c", "parent-d", "parent-product",
        "low00", "w01", "w10", "hp0", "hp1",
    )
    field_modes = (
        "field-low-d17", "field-low-q3-l", "field-low-q3-q",
        "field-w01-l", "field-w01-q0", "field-w01-q1",
        "field-w10-l0", "field-w10-l1", "field-w10-s6",
        "field-hp0-l0", "field-hp0-l1",
        "field-hp0-q0", "field-hp0-q1", "field-hp0-q2",
        "field-hp1-l0", "field-hp1-q0", "field-hp1-q1",
        "field-hp1-r0", "field-hp1-r1", "field-hp1-s6",
    )
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode", choices=("source", *router_modes, *field_modes)
    )
    args = parser.parse_args()
    variables, cores, finite_incidence = reconstruct_cores(
        fraction_free=args.mode == "source"
    )
    print(
        "audit_stage="
        + ("fraction_free_source" if args.mode == "source" else "direct_source"),
        flush=True,
    )
    if args.mode == "source":
        print(
            "KB_C2_112_NEAR_MOVING_XI_MIXED_SOURCE_AUDIT_PASS",
            flush=True,
        )
        return
    if args.mode in router_modes:
        audit_router(args.mode, variables, cores)
        return
    audit_field(args.mode, variables, cores, finite_incidence)


if __name__ == "__main__":
    main()
