#!/usr/bin/env python3
"""Construct the rigid S6 [6,5,2] unordered-pair quotient exactly."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "experiments/prize_resolution/rate_half_kb_m4_s6_652_pair_quotient_result.json"
SOURCE_COMMIT = "7d5b899b0741ebd505363f7f811e5737e906abee"
SOURCE_BLOB = "454b284b8d09d855b1fde5c86dac2c28859f0f67"
SOURCE_PATH = "belyi_db/6/6T16-[6,5,2]-6-51-21111-g0.m"


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
    x, y, z, m, w, u = sp.symbols("x y z m w u")
    numerator = sp.Rational(625, 624) * x**6
    denominator = (
        x**6
        - sp.Rational(16, 715) * x**5
        - sp.Rational(192, 1573) * x**4
        - sp.Rational(16384, 51909) * x**3
        - sp.Rational(65536, 190333) * x**2
        + sp.Rational(67108864, 345454395)
    )
    quadratic = x**2 - y * x + z
    remainder_n = sp.rem(numerator, quadratic, x)
    remainder_d = sp.rem(denominator, quadratic, x)
    n0, n1 = (sp.Poly(remainder_n, x).nth(index) for index in range(2))
    d0, d1 = (sp.Poly(remainder_d, x).nth(index) for index in range(2))
    curve = primitive(n0 * d1 - n1 * d0, y, z)
    expected_curve = -(
        4194304 * y**5
        - 7434240 * y**3 * z**2
        - 16777216 * y**3 * z
        - 6814720 * y**2 * z**3
        - 2635380 * y * z**4
        + 14868480 * y * z**3
        + 12582912 * y * z**2
        - 483153 * z**5
        + 6814720 * z**4
    )
    assert sp.expand(curve - expected_curve) == 0
    _, curve_factors = sp.factor_list(curve, y, z)
    assert len(curve_factors) == 1
    assert curve_factors[0][1] == 1
    assert sp.Poly(curve_factors[0][0], y, z).total_degree() == 5

    projected = sp.cancel(curve.subs(z, m * y) / y**3)
    assert sp.degree(projected, y) == 2
    discriminant = sp.factor(sp.discriminant(projected, y))
    expected_discriminant = (
        1048576
        * m**2
        * (11 * m + 16) ** 4
        * (3025 * m**2 - 2816 * m + 1024)
    )
    assert sp.expand(discriminant - expected_discriminant) == 0

    m_u = sp.factor(-64 * (u + 44) / ((u - 55) * (u + 55)))
    w_u = sp.factor(-32 * (u**2 + 88 * u + 3025) / ((u - 55) * (u + 55)))
    assert sp.factor(w_u**2 - (3025 * m_u**2 - 2816 * m_u + 1024)) == 0
    square_root = 1024 * m * (11 * m + 16) ** 2 * w
    projected_poly = sp.Poly(projected, y)
    y_m = sp.factor(
        (-projected_poly.nth(1) + square_root) / (2 * projected_poly.nth(2))
    )
    y_u = sp.factor(y_m.subs({m: m_u, w: w_u}))
    z_u = sp.factor(m_u * y_u)
    expected_y = sp.factor(
        -192
        * (u - 55)
        * (u + 44)
        * (u + 55) ** 2
        / (
            u**5
            + 55 * u**4
            - 9680 * u**3
            - 425920 * u**2
            + 28623155 * u
            + 1257325157
        )
    )
    expected_z = sp.factor(
        12288
        * (u + 44) ** 2
        * (u + 55)
        / (
            u**5
            + 55 * u**4
            - 9680 * u**3
            - 425920 * u**2
            + 28623155 * u
            + 1257325157
        )
    )
    assert sp.factor(y_u - expected_y) == 0
    assert sp.factor(z_u - expected_z) == 0
    assert sp.factor(curve.subs({y: y_u, z: z_u})) == 0

    quotient = sp.cancel((n0 / d0).subs({y: y_u, z: z_u}))
    quotient_n, quotient_d = quotient.as_numer_denom()
    quartic = u**4 + 176 * u**3 + 14520 * u**2 + 660176 * u + 12576619
    sextic = (
        u**6
        - 330 * u**5
        + 22143 * u**4
        + 3380740 * u**3
        - 372423117 * u**2
        - 39333485730 * u
        - 870224422859
    )
    expected_n = -9566429400000 * (u + 44) ** 6 * (u + 55) ** 3
    expected_d = (u + 143) * quartic**2 * sextic
    expected_difference = -(u + 77) ** 5 * (u**2 - 44 * u - 4961) ** 5
    assert sp.expand(quotient_n - expected_n) == 0
    assert sp.expand(quotient_d - expected_d) == 0
    assert sp.expand(quotient_n - quotient_d - expected_difference) == 0
    factors = (u + 143, quartic, sextic)
    assert all(sp.gcd(factor, sp.diff(factor, u)) == 1 for factor in factors)
    assert all(
        sp.gcd(factors[left], factors[right]) == 1
        for left in range(len(factors))
        for right in range(left + 1, len(factors))
    )

    pole_quadratic = u**2 - 44 * u - 4961
    pole_discriminant = sp.discriminant(pole_quadratic, u)
    assert pole_discriminant == 66**2 * 5
    p = 2130706433
    tower_multiplier = sum(p**index for index in range(6))
    assert p not in (2, 3, 5, 11)
    assert tower_multiplier % 2 == 0

    data: dict[str, object] = {
        "schema": "rate_half_kb_m4_s6_652_pair_quotient_v1",
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
            "label": "6T16-[6,5,2]-6-51-21111-g0",
            "numerator": expression_string(numerator),
            "denominator": expression_string(denominator),
            "zero_profile": [6],
            "one_profile": [5, 1],
            "pole_profile": [2, 1, 1, 1, 1],
        },
        "pair_curve": {
            "equation": expression_string(curve),
            "projection": "z=m*y",
            "projected_degree": 2,
            "discriminant": expression_string(discriminant),
            "conic": "w^2=3025*m^2-2816*m+1024",
            "m_of_u": expression_string(m_u),
            "w_of_u": expression_string(w_u),
            "y_of_u": expression_string(y_u),
            "z_of_u": expression_string(z_u),
        },
        "quotient": {
            "degree": 15,
            "numerator": expression_string(expected_n),
            "denominator": expression_string(expected_d),
            "numerator_minus_denominator": expression_string(expected_difference),
            "quartic": expression_string(quartic),
            "sextic": expression_string(sextic),
            "fiber_zero": [6, 6, 3],
            "fiber_one": [5, 5, 5],
            "fiber_infinity": [2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
            "total_branch_index": 28,
        },
        "challenge_field": {
            "p": p,
            "extension_degree": 6,
            "pole_coordinate_linear": "u+77",
            "pole_coordinate_quadratic": expression_string(pole_quadratic),
            "pole_quadratic_discriminant": int(pole_discriminant),
            "pole_points": ["-77", "22+33*sqrt(5)", "22-33*sqrt(5)"],
            "all_base_field_units_square": True,
            "pole_fiber_splits": True,
        },
        "conclusion": {
            "passport": "S6: 5.1,2.1.1.1.1,6",
            "terminal": "M4_S6_652_RIGID_PAIR_QUOTIENT_AND_POLE_DESCENT",
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
