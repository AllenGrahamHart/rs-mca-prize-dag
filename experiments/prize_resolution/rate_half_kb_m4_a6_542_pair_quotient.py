#!/usr/bin/env python3
"""Construct the rigid A6 [5,4,2] unordered-pair quotient exactly."""

from __future__ import annotations

import argparse
import copy
from functools import reduce
import hashlib
import json
from math import gcd
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = (
    ROOT
    / "experiments/prize_resolution/rate_half_kb_m4_a6_542_pair_quotient_result.json"
)
SOURCE_COMMIT = "7d5b899b0741ebd505363f7f811e5737e906abee"
SOURCE_BLOB = "55e23bc1ef1d939329a5a6b377d03c07f0ac9f2d"
SOURCE_PATH = "belyi_db/6/6T15-[5,4,2]-51-42-2211-g0.m"


def canonical_hash(data: dict[str, object]) -> str:
    payload = copy.deepcopy(data)
    payload.pop("payload_sha256", None)
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def expression_string(expression: sp.Expr) -> str:
    return str(sp.expand(expression))


def factored_string(expression: sp.Expr) -> str:
    return str(sp.factor(expression, extension=NU))


def normalize_field_vector(field, vector, coordinate):
    """Scale a field vector so the selected coordinate is one."""
    scale = vector[coordinate]
    assert scale != field.zero
    return [field.to_sympy(value / scale) for value in vector]


def integral_rational_parts(field, expression, variable):
    """Return a common integral K-scaling of a rational function's parts."""
    numerator, denominator = sp.cancel(expression, extension=field.ext).as_numer_denom()
    polys = (
        sp.Poly(numerator, variable, domain=field),
        sp.Poly(denominator, variable, domain=field),
    )
    field_coefficients = [
        field.from_sympy(coefficient)
        for polynomial in polys
        for coefficient in polynomial.all_coeffs()
    ]
    rationals = []
    for coefficient in field_coefficients:
        for item in coefficient.to_list():
            rationals.append(sp.Rational(item.numerator, item.denominator))
    scale = sp.ilcm(*(item.q for item in rationals))
    integers = [int(item * scale) for item in rationals]
    content = reduce(gcd, (abs(value) for value in integers if value), 0)
    multiplier = field.from_sympy(sp.Rational(scale, content))

    def scaled(polynomial):
        result = sp.Integer(0)
        for degree in range(polynomial.degree() + 1):
            coefficient = field.from_sympy(polynomial.nth(degree)) * multiplier
            result += field.to_sympy(coefficient) * variable**degree
        return sp.expand(result)

    return scaled(polys[0]), scaled(polys[1])


def integral_poly_pair(field, numerator, denominator):
    """Jointly clear coefficient denominators/content in two K[u] polynomials."""
    field_coefficients = [
        field.from_sympy(coefficient)
        for polynomial in (numerator, denominator)
        for coefficient in polynomial.all_coeffs()
    ]
    rationals = []
    for coefficient in field_coefficients:
        for item in coefficient.to_list():
            rationals.append(sp.Rational(item.numerator, item.denominator))
    scale = sp.ilcm(*(item.q for item in rationals))
    integers = [int(item * scale) for item in rationals]
    content = reduce(gcd, (abs(value) for value in integers if value), 0)
    multiplier = field.from_sympy(sp.Rational(scale, content))

    def scaled(polynomial):
        result = sp.Integer(0)
        for degree in range(polynomial.degree() + 1):
            coefficient = field.from_sympy(polynomial.nth(degree)) * multiplier
            result += field.to_sympy(coefficient) * U**degree
        return sp.expand(result)

    return scaled(numerator), scaled(denominator)


def integral_polynomial(field, polynomial):
    """Clear rational denominators and integer content in one K[u] polynomial."""
    coefficients = [field.from_sympy(value) for value in polynomial.all_coeffs()]
    rationals = [
        sp.Rational(item.numerator, item.denominator)
        for coefficient in coefficients
        for item in coefficient.to_list()
    ]
    scale = sp.ilcm(*(item.q for item in rationals))
    integers = [int(item * scale) for item in rationals]
    content = reduce(gcd, (abs(value) for value in integers if value), 0)
    multiplier = field.from_sympy(sp.Rational(scale, content))
    return sp.expand(
        sum(
            field.to_sympy(field.from_sympy(polynomial.nth(degree)) * multiplier)
            * U**degree
            for degree in range(polynomial.degree() + 1)
        )
    )


def normalized_coordinate_pair(expression):
    numerator, denominator = sp.together(expression).as_numer_denom()
    numerator_poly = sp.Poly(numerator, U, domain=FIELD)
    denominator_poly = sp.Poly(denominator, U, domain=FIELD)
    leading = denominator_poly.LC()
    return numerator_poly.mul_ground(FIELD.one / leading), denominator_poly.monic()


def evaluate_bivariate(expression, y_pair, z_pair):
    """Evaluate a K[y,z] polynomial with a shared monic K[u] denominator."""
    y_numerator, y_denominator = y_pair
    z_numerator, z_denominator = z_pair
    assert y_denominator == z_denominator
    polynomial = sp.Poly(expression, Y, Z, domain=FIELD)
    max_degree = max(sum(monomial) for monomial, _ in polynomial.terms())
    result = sp.Poly(0, U, domain=FIELD)
    for (y_degree, z_degree), coefficient in polynomial.terms():
        total_degree = y_degree + z_degree
        term = (
            y_numerator**y_degree
            * z_numerator**z_degree
            * y_denominator ** (max_degree - total_degree)
        ).mul_ground(coefficient)
        result += term
    return result, max_degree


def normal_form_coordinates():
    u, nu = U, NU
    y_numerator = (
        7892138344902988389383102440048963192 * u**5
        - 1601690583942523480994736036934672974 * u**5 * nu
        - 1081994888609409281819196762384588880 * u**4
        + 4319799856605487063193998233981259070 * u**4 * nu
        - 2557080637017141887519303559626866320 * u**3
        - 269153890030150821757418687053079500 * u**3 * nu
        + 57351286341507867774723051292388320 * u**2
        - 65040744003628696964336068238139780 * u**2 * nu
        + 45440148237577313887698641729790680 * u
        - 27693186514939515340782600333170950 * u * nu
        - 8195695155042818791075721558758992
        + 9252066083213335649260504183692134 * nu
    )
    y_denominator = (
        47581127176233973807006209129958666013 * u**5
        - 33063091523335411524882986821658172913 * u**4
        + 20028103088327882229395977315529116076 * u**4 * nu
        + 2275903099068870370256681899125906882 * u**3
        - 7656689534122581774500550730770222384 * u**3 * nu
        + 86770964436494711769542767905886782 * u**2
        + 2353052971917333894796382384128976136 * u**2 * nu
        - 794372834757092768855423085524980623 * u
        - 309830442050531996649607665971007024 * u * nu
        + 92044158367195765493357300375554659
        - 16932117919710073775002280696344404 * nu
    )
    z_numerator = (
        70549704244659221672396489996795262460 * u**5
        - 161752816684601163543706226331421211040 * u**5 * nu
        + 215205390515079193083668319121630815060 * u**4
        + 16159421588292196559349526916857312080 * u**4 * nu
        + 11722270560645483957718891031328135960 * u**3
        + 23175659917134591802585820187583223680 * u**3 * nu
        - 10804379569753035346521855082299740440 * u**2
        + 9989093742569895952809841807061178080 * u**2 * nu
        - 2468558058630888743185108599997267540 * u
        + 225078189813767762770252154245547680 * u * nu
        - 442738400533747369910902712443061500
        - 25621140774049663433958038778658480 * nu
    )
    z_denominator = (
        2236312977282996768929291829108057302611 * u**5
        - 1553965301596764341669500380617934126911 * u**4
        + 941320845151410464781610933829868455572 * u**4 * nu
        + 106967445656236907402064049258917623454 * u**3
        - 359864408103761343401525884346200452048 * u**3 * nu
        + 4078235328515251453168510091576678754 * u**2
        + 110593489680114693055429972054061878392 * u**2 * nu
        - 37335523233583360136204885019674089281 * u
        - 14562030776375003842531560300637330128 * u * nu
        + 4326075443258200978187793117651068973
        - 795809542226373467425107192728186988 * nu
    )
    return y_numerator / y_denominator, z_numerator / z_denominator


def companion_remainders():
    x, y, z, nu = X, Y, Z, NU
    numerator = (
        (67262400 * nu + 1902382848) * x**6 + (-350695008 * nu - 589286016) * x**5
    ) / 648626449
    denominator = (
        x**6
        + (2550981 * nu + 1416912) * x**5 / 3074059
        + (-1006504575 * nu + 57591900) * x**4 / 2594505796
        + (-142471950 * nu + 949516600) * x**3 / 648626449
        + (-75218250 * nu - 327741000) * x**2 / 648626449
        + (-49794600 * nu + 31384800) * x / 648626449
        + (19666500 * nu - 43658000) / 648626449
    )
    domain = FIELD.frac_field(y, z)
    quadratic = sp.Poly(x**2 - y * x + z, x, domain=domain)
    remainder_n = sp.Poly(numerator, x, domain=domain).rem(quadratic)
    remainder_d = sp.Poly(denominator, x, domain=domain).rem(quadratic)
    return (
        numerator,
        denominator,
        domain.to_sympy(remainder_n.nth(0)),
        domain.to_sympy(remainder_n.nth(1)),
        domain.to_sympy(remainder_d.nth(0)),
        domain.to_sympy(remainder_d.nth(1)),
    )


def build_adjoint_basis():
    y, z = Y, Z
    nu = NU
    curve = (
        y**5
        + (-sp.Rational(9, 5) + sp.Rational(3, 5) * nu) * y**4 * z
        + (-sp.Rational(1, 3) - nu / 6) * y**4
        + (sp.Rational(3, 4) + sp.Rational(15, 4) * nu) * y**3 * z**2
        - 3 * y**3 * z
        + (-sp.Rational(131, 10) - sp.Rational(24, 5) * nu) * y**2 * z**3
        + (sp.Rational(153, 20) - sp.Rational(19, 5) * nu) * y**2 * z**2
        + (1 + nu / 2) * y**2 * z
        + (-sp.Rational(621, 80) + sp.Rational(33, 8) * nu) * y * z**4
        + (-sp.Rational(1, 3) - sp.Rational(35, 12) * nu) * y * z**3
        + y * z**2
        + (sp.Rational(71203, 4800) - sp.Rational(70951, 4800) * nu) * z**5
        + (sp.Rational(295, 16) + sp.Rational(129, 32) * nu) * z**4
        + (-sp.Rational(81, 20) + sp.Rational(13, 5) * nu) * z**3
        + (-sp.Rational(1, 3) - nu / 6) * z**2
    )

    b = sp.Rational(14, 47) + sp.Rational(12, 47) * nu
    c = -sp.Rational(4, 23) - sp.Rational(9, 46) * nu
    pole_y = -sp.Rational(34, 211) - sp.Rational(189, 422) * nu
    pole_z = sp.Rational(40, 211) - sp.Rational(75, 211) * nu
    a = sp.Rational(1, 3) + nu / 6
    alpha = sp.Rational(17, 10) - sp.Rational(9, 10) * nu
    points = (
        (0, 0),
        (2 * b, b**2),
        (b + c, b * c),
        (pole_y, pole_z),
        (a, 0),
        (2 * c, c**2),
    )

    monomials = (sp.Integer(1), y, z, y**2, y * z, z**2, y**3, y**2 * z, y * z**2, z**3)
    row_expressions = []
    for point_y, point_z in points:
        row_expressions.append(
            [term.subs({y: point_y, z: point_z}) for term in monomials]
        )
    row_expressions.append([sp.diff(term, y).subs({y: 0, z: 0}) for term in monomials])
    q_y, q_z = points[2]
    row_expressions.append(
        [
            (-alpha * sp.diff(term, y) + sp.diff(term, z)).subs({y: q_y, z: q_z})
            for term in monomials
        ]
    )

    rows = [
        [FIELD.from_sympy(sp.expand(value)) for value in row] for row in row_expressions
    ]
    matrix = DomainMatrix(rows, (8, 10), FIELD)
    rref, pivots = matrix.rref()
    assert pivots == tuple(range(8))
    assert matrix.rank() == 8
    nullspace = matrix.nullspace().to_list()
    assert len(nullspace) == 2
    normalized = [normalize_field_vector(FIELD, row, 6) for row in nullspace]
    for row in normalized:
        for source_row in rows:
            total = FIELD.zero
            for coefficient, value in zip(row, source_row):
                total += FIELD.from_sympy(coefficient) * value
            assert total == FIELD.zero
    basis = [
        sp.expand(sum(coefficient * term for coefficient, term in zip(row, monomials)))
        for row in normalized
    ]
    return curve, basis, normalized, rref, pivots


V = sp.symbols("v")
X, Y, Z, U = sp.symbols("x y z u")
FIELD = sp.QQ.alg_field_from_poly(V**2 - V + 4, alias="nu")
NU = FIELD.ext


def derive_coordinates() -> None:
    curve, basis, normalized, _, pivots = build_adjoint_basis()
    print("rank=8 pivots=", pivots, flush=True)
    pencil = basis[0] - U * basis[1]
    domain = FIELD.frac_field(Y, U)
    resultant = sp.Poly(curve, Z, domain=domain).resultant(
        sp.Poly(pencil, Z, domain=domain)
    )
    resultant_expression = sp.together(resultant.as_expr()).as_numer_denom()[0]
    resultant_poly = sp.Poly(resultant_expression, Y, U, extension=NU)
    print(
        "resultant degrees:",
        resultant_poly.degree(Y),
        resultant_poly.degree(U),
        flush=True,
    )
    factorization = resultant_poly.factor_list()[1]
    factor_rows = sorted(
        (factor.degree(Y), factor.degree(U), exponent)
        for factor, exponent in factorization
    )
    assert factor_rows == [
        (1, 0, 1),
        (1, 0, 1),
        (1, 0, 2),
        (1, 0, 2),
        (1, 0, 4),
        (1, 0, 4),
        (1, 5, 1),
    ]
    print("factor rows:", factor_rows, flush=True)
    moving = next(
        factor
        for factor, exponent in factorization
        if factor.degree(Y) == 1 and factor.degree(U) == 5 and exponent == 1
    )
    moving_y = sp.Poly(moving.as_expr(), Y, domain=FIELD.frac_field(U))
    y_u = sp.factor(-moving_y.nth(0) / moving_y.nth(1), extension=NU)
    z_domain = FIELD.frac_field(Z, U)
    resultant_z = sp.Poly(curve, Y, domain=z_domain).resultant(
        sp.Poly(pencil, Y, domain=z_domain)
    )
    resultant_z_expression = sp.together(resultant_z.as_expr()).as_numer_denom()[0]
    resultant_z_poly = sp.Poly(resultant_z_expression, Z, U, extension=NU)
    print(
        "z-resultant degrees:",
        resultant_z_poly.degree(Z),
        resultant_z_poly.degree(U),
        flush=True,
    )
    z_factorization = resultant_z_poly.factor_list()[1]
    z_factor_rows = sorted(
        (factor.degree(Z), factor.degree(U), exponent)
        for factor, exponent in z_factorization
    )
    assert z_factor_rows == [
        (1, 0, 1),
        (1, 0, 2),
        (1, 0, 2),
        (1, 0, 4),
        (1, 0, 5),
        (1, 5, 1),
    ]
    print("z-factor rows:", z_factor_rows, flush=True)
    moving_z = next(
        factor
        for factor, exponent in z_factorization
        if factor.degree(Z) == 1 and factor.degree(U) > 0 and exponent == 1
    )
    moving_z_poly = sp.Poly(moving_z.as_expr(), Z, domain=FIELD.frac_field(U))
    z_u = sp.factor(-moving_z_poly.nth(0) / moving_z_poly.nth(1), extension=NU)
    y_parts = integral_rational_parts(FIELD, y_u, U)
    z_parts = integral_rational_parts(FIELD, z_u, U)
    expected_y, expected_z = normal_form_coordinates()
    expected_y_parts = integral_rational_parts(FIELD, expected_y, U)
    expected_z_parts = integral_rational_parts(FIELD, expected_z, U)
    for actual, expected in zip(y_parts + z_parts, expected_y_parts + expected_z_parts):
        assert sp.Poly(actual - expected, U, domain=FIELD).is_zero
    print("moving coordinates match frozen normal form", flush=True)


def build() -> dict[str, object]:
    companion_n, companion_d, n0, n1, d0, d1 = companion_remainders()
    x, nu = X, NU
    expected_n = (
        (1902382848 + 67262400 * nu)
        * x**5
        * (x - sp.Rational(1, 3) - nu / 6)
        / 648626449
    )
    expected_d = (
        x**2
        + (sp.Rational(2020, 14569) - sp.Rational(960, 14569) * nu) * x
        + sp.Rational(2020, 14569)
        - sp.Rational(960, 14569) * nu
    ) * (
        x**2
        + (sp.Rational(34, 211) + sp.Rational(189, 422) * nu) * x
        + sp.Rational(40, 211)
        - sp.Rational(75, 211) * nu
    ) ** 2
    expected_difference = (
        (1253756399 + 67262400 * nu)
        * (x - sp.Rational(14, 47) - sp.Rational(12, 47) * nu) ** 4
        * (x + sp.Rational(4, 23) + sp.Rational(9, 46) * nu) ** 2
        / 648626449
    )
    assert sp.Poly(companion_n - expected_n, x, domain=FIELD).is_zero
    assert sp.Poly(companion_d - expected_d, x, domain=FIELD).is_zero
    assert sp.Poly(
        companion_n - companion_d - expected_difference, x, domain=FIELD
    ).is_zero

    curve, basis, normalized, _, pivots = build_adjoint_basis()
    determinant = sp.Poly(n0 * d1 - n1 * d0, Y, Z, domain=FIELD)
    determinant_scale = FIELD.from_sympy(determinant.coeff_monomial(Y**5))
    determinant = determinant.mul_ground(FIELD.one / determinant_scale)
    assert sp.Poly(determinant.as_expr() - curve, Y, Z, domain=FIELD).is_zero
    curve_factors = sp.Poly(curve, Y, Z, domain=FIELD).factor_list()[1]
    assert len(curve_factors) == 1 and curve_factors[0][1] == 1

    y_u, z_u = normal_form_coordinates()
    y_pair = normalized_coordinate_pair(y_u)
    z_pair = normalized_coordinate_pair(z_u)
    assert y_pair[1] == z_pair[1]
    curve_value, _ = evaluate_bivariate(curve, y_pair, z_pair)
    assert curve_value.is_zero
    h0_value, h0_power = evaluate_bivariate(basis[0], y_pair, z_pair)
    h1_value, h1_power = evaluate_bivariate(basis[1], y_pair, z_pair)
    assert h0_power == h1_power == 3
    assert (h0_value - h1_value * sp.Poly(U, U, domain=FIELD)).is_zero

    evaluated_n, n_power = evaluate_bivariate(n0, y_pair, z_pair)
    evaluated_d, d_power = evaluate_bivariate(d0, y_pair, z_pair)
    common_denominator = y_pair[1]
    quotient_n_poly = evaluated_n * common_denominator**d_power
    quotient_d_poly = evaluated_d * common_denominator**n_power
    common = quotient_n_poly.gcd(quotient_d_poly)
    quotient_n_poly = quotient_n_poly.exquo(common)
    quotient_d_poly = quotient_d_poly.exquo(common)
    quotient_n, quotient_d = integral_poly_pair(FIELD, quotient_n_poly, quotient_d_poly)
    factorizations: dict[str, list[tuple[sp.Poly, int]]] = {}
    polynomials: dict[str, sp.Poly] = {}
    for label, expression in (
        ("numerator", quotient_n),
        ("denominator", quotient_d),
        ("difference", sp.expand(quotient_n - quotient_d)),
    ):
        polynomial = sp.Poly(expression, U, domain=FIELD)
        factors = polynomial.factor_list()[1]
        polynomials[label] = polynomial
        factorizations[label] = factors
    factor_rows = {
        label: sorted((factor.degree(), exponent) for factor, exponent in factors)
        for label, factors in factorizations.items()
    }
    assert factor_rows == {
        "numerator": [(1, 5), (2, 5)],
        "denominator": [(1, 1), (2, 1), (2, 2), (4, 2)],
        "difference": [(1, 1), (1, 2), (1, 4), (2, 4)],
    }
    assert all(polynomial.degree() == 15 for polynomial in polynomials.values())

    products: dict[str, sp.Poly] = {}
    for label in ("numerator", "denominator"):
        product = sp.Poly(1, U, domain=FIELD)
        for factor, exponent in factorizations[label]:
            integral = sp.Poly(integral_polynomial(FIELD, factor), U, domain=FIELD)
            product *= integral**exponent
        products[label] = product
    numerator_unit = FIELD.from_sympy(polynomials["numerator"].LC()) / FIELD.from_sympy(
        products["numerator"].LC()
    )
    denominator_unit = FIELD.from_sympy(
        polynomials["denominator"].LC()
    ) / FIELD.from_sympy(products["denominator"].LC())
    quotient_scalar = numerator_unit / denominator_unit

    p = 2130706433
    source_denominators = (
        2,
        3,
        5,
        6,
        10,
        12,
        16,
        20,
        23,
        32,
        46,
        47,
        211,
        422,
        14569,
        3074059,
        648626449,
        2594505796,
    )
    assert all(value % p for value in source_denominators)
    square_roots = sp.sqrt_mod(-15, p, all_roots=True)
    assert len(square_roots) == 2
    nu_residues = [((1 + root) * pow(2, -1, p)) % p for root in square_roots]
    zero_linear = next(
        factor
        for factor, exponent in factorizations["numerator"]
        if factor.degree() == 1 and exponent == 5
    )
    zero_quadratic = next(
        factor
        for factor, exponent in factorizations["numerator"]
        if factor.degree() == 2 and exponent == 5
    )
    discriminants = []
    collisions = []
    scalar_residues = []

    def reduce_field_element(value, nu_residue):
        element = value if hasattr(value, "to_list") else FIELD.from_sympy(value)
        coefficients = element.to_list()
        if not coefficients:
            return 0
        residues = [
            (int(item.numerator) * pow(int(item.denominator), -1, p)) % p
            for item in coefficients
        ]
        if len(residues) == 1:
            return residues[0]
        assert len(residues) == 2
        return (residues[0] * nu_residue + residues[1]) % p

    for nu_residue in nu_residues:
        coefficients = [
            reduce_field_element(value, nu_residue)
            for value in zero_quadratic.all_coeffs()
        ]
        leading, linear, constant = coefficients
        discriminants.append((linear * linear - 4 * leading * constant) % p)
        linear_coefficients = [
            reduce_field_element(value, nu_residue)
            for value in zero_linear.all_coeffs()
        ]
        linear_root = (-linear_coefficients[1] * pow(linear_coefficients[0], -1, p)) % p
        collisions.append(
            (leading * linear_root**2 + linear * linear_root + constant) % p
        )
        scalar_residues.append(reduce_field_element(quotient_scalar, nu_residue))
    assert 0 not in discriminants
    assert 0 not in collisions
    assert 0 not in scalar_residues
    proportionality, _ = evaluate_bivariate(n0 * d1 - n1 * d0, y_pair, z_pair)
    assert proportionality.is_zero

    coordinate_parts = {
        "y": integral_rational_parts(FIELD, y_u, U),
        "z": integral_rational_parts(FIELD, z_u, U),
    }

    def serialized_factors(label):
        return [
            {
                "degree": factor.degree(),
                "exponent": exponent,
                "polynomial": expression_string(integral_polynomial(FIELD, factor)),
            }
            for factor, exponent in factorizations[label]
        ]

    data: dict[str, object] = {
        "schema": "rate_half_kb_m4_a6_542_pair_quotient_v1",
        "payload_sha256": "",
        "producer": {
            "path": str(Path(__file__).resolve().relative_to(ROOT)),
            "sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "source": {
            "repository": "michaelmusty/BelyiDB",
            "commit": SOURCE_COMMIT,
            "blob": SOURCE_BLOB,
            "path": SOURCE_PATH,
        },
        "coefficient_field": {
            "generator": "nu",
            "minimal_polynomial": "nu^2-nu+4",
            "discriminant": -15,
        },
        "companion": {
            "degree": 6,
            "label": "6T15-[5,4,2]-51-42-2211-g0",
            "numerator_factorization": factored_string(expected_n),
            "denominator_factorization": factored_string(expected_d),
            "difference_factorization": factored_string(expected_difference),
            "zero_profile": [5, 1],
            "one_profile": [4, 2],
            "pole_profile": [2, 2, 1, 1],
        },
        "pair_curve": {
            "equation": expression_string(curve),
            "irreducible": True,
            "adjoint_rank": 8,
            "adjoint_pivots": list(pivots),
            "adjoint_h0": expression_string(basis[0]),
            "adjoint_h1": expression_string(basis[1]),
            "y_resultant_factor_degrees": [
                [1, 0, 1],
                [1, 0, 1],
                [1, 0, 2],
                [1, 0, 2],
                [1, 0, 4],
                [1, 0, 4],
                [1, 5, 1],
            ],
            "z_resultant_factor_degrees": [
                [1, 0, 1],
                [1, 0, 2],
                [1, 0, 2],
                [1, 0, 4],
                [1, 0, 5],
                [1, 5, 1],
            ],
            "normalized_adjoint_rows": [
                [expression_string(value) for value in row] for row in normalized
            ],
            "y_numerator": expression_string(coordinate_parts["y"][0]),
            "y_denominator": expression_string(coordinate_parts["y"][1]),
            "z_numerator": expression_string(coordinate_parts["z"][0]),
            "z_denominator": expression_string(coordinate_parts["z"][1]),
        },
        "quotient": {
            "degree": 15,
            "scalar": expression_string(FIELD.to_sympy(quotient_scalar)),
            "numerator_factors": serialized_factors("numerator"),
            "denominator_factors": serialized_factors("denominator"),
            "difference_factors": serialized_factors("difference"),
            "fiber_zero": [5, 5, 5],
            "fiber_one": [4, 4, 4, 2, 1],
            "fiber_infinity": [2, 2, 2, 2, 2, 2, 1, 1, 1],
            "total_branch_index": 28,
        },
        "challenge_field": {
            "p": p,
            "extension_degree": 6,
            "nu_residues": nu_residues,
            "zero_quadratic_discriminants": discriminants,
            "zero_linear_quadratic_separations": collisions,
            "zero_fiber_splits": True,
        },
        "conclusion": {
            "passport": "A6: 5.1,2.2.1.1,4.2",
            "terminal": "M4_A6_542_RIGID_PAIR_QUOTIENT_AND_POLE_DESCENT",
        },
        "scope_fence": [
            "no completely split unramified active fiber",
            "no quartic source-star incidence",
            "no m4 type deletion",
            "no owner, ledger, endpoint, or KoalaBear row closure",
        ],
    }
    data["payload_sha256"] = canonical_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--derive", action="store_true")
    parser.add_argument("--write", action="store_true")
    arguments = parser.parse_args()
    if arguments.derive:
        derive_coordinates()
    data = build()
    if arguments.write:
        OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
