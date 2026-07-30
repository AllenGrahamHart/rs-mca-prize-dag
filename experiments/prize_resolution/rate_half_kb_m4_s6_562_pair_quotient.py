#!/usr/bin/env python3
"""Construct the rigid S6 [5,6,2] unordered-pair quotient exactly."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "experiments/prize_resolution/rate_half_kb_m4_s6_562_pair_quotient_result.json"
SOURCE_COMMIT = "7d5b899b0741ebd505363f7f811e5737e906abee"
SOURCE_BLOB = "94cff64a36672ba6bde9e6cbc1fa251230aa8001"
SOURCE_PATH = "belyi_db/6/6T16-[5,6,2]-51-321-222-g0.m"


def canonical_hash(data: dict[str, object]) -> str:
    payload = copy.deepcopy(data)
    payload.pop("payload_sha256", None)
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def primitive(expression: sp.Expr, *variables: sp.Symbol) -> sp.Expr:
    numerator = sp.together(expression).as_numer_denom()[0]
    return sp.Poly(numerator, *variables).primitive()[1].as_expr()


def expression_string(expression: sp.Expr) -> str:
    return str(sp.factor(expression))


def build() -> dict[str, object]:
    x, y, z, u = sp.symbols("x y z u")
    numerator = sp.Rational(34992, 17689) * x**6 - sp.Rational(59778, 17689) * x**5
    denominator = (
        x**6
        - sp.Rational(5043, 532) * x**5
        + sp.Rational(14700345, 1132096) * x**4
        + sp.Rational(43764835, 566048) * x**3
        - sp.Rational(42386415, 323456) * x**2
        - sp.Rational(347568603, 2264192) * x
        + sp.Rational(4750104241, 18113536)
    )
    assert sp.factor(numerator) == 1458 * x**5 * (24 * x - 41) / 17689
    assert sp.factor(denominator) == (
        4256 * x**3 - 20172 * x**2 - 20172 * x + 68921
    ) ** 2 / 18113536
    assert sp.factor(numerator - denominator) == (
        (8 * x + 41) ** 2 * (22 * x - 41) ** 3 * (26 * x + 41) / 18113536
    )

    quadratic = x**2 - y * x + z
    remainder_n = sp.rem(numerator, quadratic, x)
    remainder_d = sp.rem(denominator, quadratic, x)
    n0, n1 = (sp.Poly(remainder_n, x).nth(index) for index in range(2))
    d0, d1 = (sp.Poly(remainder_d, x).nth(index) for index in range(2))
    curve = primitive(n0 * d1 - n1 * d0, y, z)
    expected_curve = (
        -2780548824 * y**5
        + 1627638336 * y**4 * z
        + 4750104241 * y**4
        + 1389447360 * y**3 * z**2
        + 8341646472 * y**3 * z
        - 819790080 * y**2 * z**3
        - 7256554248 * y**2 * z**2
        - 14250312723 * y**2 * z
        - 137681280 * y * z**4
        - 1378420000 * y * z**3
        - 2780548824 * y * z**2
        + 82396160 * z**5
        + 1054995600 * z**4
        + 4001277576 * z**3
        + 4750104241 * z**2
    )
    assert sp.expand(curve - expected_curve) == 0
    _, factors = sp.factor_list(curve, y, z)
    assert len(factors) == 1 and factors[0][1] == 1

    h0 = (
        z
        * (
            1586864 * y**2
            - 289952 * y * z
            - 2343314 * y
            - 319744 * z**2
            - 1728068 * z
            - 2825761
        )
        / 1586864
    )
    h1 = (
        97592136 * y**3
        - 166719899 * y**2
        - 24010912 * y * z**2
        - 124609168 * y * z
        - 3678464 * z**3
        - 18780132 * z**2
        - 42386415 * z
    ) / 97592136
    pencil = primitive(h0 - u * h1, y, z, u)
    resultant = sp.resultant(curve, pencil, z)
    factor_rows = sorted(
        (int(sp.degree(factor, y)), int(sp.degree(factor, u)), int(exponent))
        for factor, exponent in sp.factor_list(resultant, y, u)[1]
    )
    assert factor_rows == [
        (1, 0, 1),
        (1, 0, 1),
        (1, 0, 2),
        (1, 0, 4),
        (1, 5, 1),
        (3, 0, 2),
    ]
    moving = next(
        factor
        for factor, exponent in sp.factor_list(resultant, y, u)[1]
        if sp.degree(factor, y) == 1 and sp.degree(factor, u) == 5 and exponent == 1
    )
    moving_poly = sp.Poly(moving, y)
    y_u = sp.factor(-moving_poly.nth(0) / moving_poly.nth(1))
    a2 = 25444 * u**2 - 50922 * u + 15129
    c3 = 36517864 * u**3 - 276920478 * u**2 + 608911992 * u - 414973341
    e5 = (
        144800664832 * u**5
        - 559791696960 * u**4
        - 97900305120 * u**3
        + 3171741595920 * u**2
        - 4974655751100 * u
        + 2391178738527
    )
    expected_y = sp.factor(a2 * c3 / (3 * e5))
    z_u = sp.factor(-41 * (188 * u - 287) * a2**2 / (4 * e5))
    assert sp.factor(y_u - expected_y) == 0
    assert sp.factor(curve.subs({y: y_u, z: z_u})) == 0
    assert sp.factor((h0 - u * h1).subs({y: y_u, z: z_u})) == 0

    quotient = sp.cancel((n0 / d0).subs({y: y_u, z: z_u}))
    quotient_n, quotient_d = quotient.as_numer_denom()
    cubic = 14658356 * u**3 - 31403007 * u**2 - 8441982 * u + 33495606
    sextic = (
        915512069923328 * u**6
        + 6554290056691968 * u**5
        - 83250949083482880 * u**4
        + 290661295480797960 * u**3
        - 474965645409866205 * u**2
        + 379227334439635443 * u
        - 119893424310248247
    )
    expected_n = 177147 * (188 * u - 287) ** 5 * a2**5
    expected_d = cubic * sextic**2
    expected_difference = (
        3125
        * (88 * u + 123) ** 2
        * (89 * u - 123) ** 3
        * (208 * u - 369) ** 6
        * (683 * u - 1107) ** 3
        * (980 * u - 1599)
    )
    assert sp.expand(quotient_n - expected_n) == 0
    assert sp.expand(quotient_d - expected_d) == 0
    assert sp.expand(quotient_n - quotient_d - expected_difference) == 0
    denominator_factors = (cubic, sextic)
    assert all(sp.gcd(factor, sp.diff(factor, u)) == 1 for factor in denominator_factors)
    assert sp.gcd(cubic, sextic) == 1
    assert sp.gcd(188 * u - 287, a2) == 1
    assert sp.gcd(a2, sp.diff(a2, u)) == 1

    pole_discriminant = sp.discriminant(a2, u)
    assert pole_discriminant == 14514**2 * 5
    p = 2130706433
    assert all(p % prime for prime in (2, 3, 5, 41, 59))
    assert sum(p**index for index in range(6)) % 2 == 0

    data: dict[str, object] = {
        "schema": "rate_half_kb_m4_s6_562_pair_quotient_v1",
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
        "companion": {
            "degree": 6,
            "label": "6T16-[5,6,2]-51-321-222-g0",
            "zero_profile": [5, 1],
            "one_profile": [3, 2, 1],
            "pole_profile": [2, 2, 2],
        },
        "pair_curve": {
            "equation": expression_string(curve),
            "adjoint_h0": expression_string(h0),
            "adjoint_h1": expression_string(h1),
            "resultant_factor_degrees": [list(row) for row in factor_rows],
            "moving_factor": expression_string(moving),
            "y_of_u": expression_string(y_u),
            "z_of_u": expression_string(z_u),
        },
        "quotient": {
            "degree": 15,
            "numerator": expression_string(expected_n),
            "denominator": expression_string(expected_d),
            "numerator_minus_denominator": expression_string(expected_difference),
            "cubic": expression_string(cubic),
            "sextic": expression_string(sextic),
            "fiber_zero": [5, 5, 5],
            "fiber_one": [6, 3, 3, 2, 1],
            "fiber_infinity": [2, 2, 2, 2, 2, 2, 1, 1, 1],
            "total_branch_index": 28,
        },
        "challenge_field": {
            "p": p,
            "extension_degree": 6,
            "pole_coordinate_linear": "188*u-287",
            "pole_coordinate_quadratic": expression_string(a2),
            "pole_quadratic_discriminant": int(pole_discriminant),
            "pole_points": [
                "287/188",
                "(25461+7257*sqrt(5))/25444",
                "(25461-7257*sqrt(5))/25444",
            ],
            "pole_fiber_splits": True,
        },
        "conclusion": {
            "passport": "S6: 5.1,2.2.2,3.2.1",
            "terminal": "M4_S6_562_RIGID_PAIR_QUOTIENT_AND_POLE_DESCENT",
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
    parser.add_argument("--write", action="store_true")
    arguments = parser.parse_args()
    data = build()
    if arguments.write:
        OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
