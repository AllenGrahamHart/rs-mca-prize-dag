#!/usr/bin/env python3
"""No-import source and certificate audit for the mixed other-xi chart."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix


PRIME = 2130706433


def check(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def digest(polynomial: sp.Poly) -> str:
    payload = repr([
        (monomial, str(coefficient))
        for monomial, coefficient in polynomial.monic().terms()
    ]).encode("ascii")
    return hashlib.sha256(payload).hexdigest()[:16]


def edge(left, right):
    return sp.Matrix([left * right, -(left + right), 1])


def evaluation(point):
    return (
        sp.Matrix([[1, point, point**2, 0, 0]]),
        sp.Matrix([[0, 0, 0, 1 + point**2, point]]),
        sp.Matrix([[point**2, point, 1, 0, 0]]),
    )


def numerator_poly(expression, *variables):
    numerator = sp.fraction(sp.cancel(expression))[0]
    return sp.Poly(numerator, *variables, domain=sp.QQ).primitive()[1]


def reconstruct():
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
    first = edge(a, b)
    second = edge(a, 1 / b)
    target = sp.Matrix([
        sp.cancel(value)
        for value in (
            ((ell0 + ell1 / b) * first + (ell0 + b * ell1) * second)
            / (1 / b - b)
        )
    ])
    at_w = evaluation(w)
    at_z = evaluation(z)
    matrix = sp.Matrix.vstack(
        at_w[0] - q0 * at_w[2],
        at_w[1] - q1 * at_w[2],
        *at_z,
    )
    rhs = sp.Matrix([0, 0, *target])
    matrix_domain = DomainMatrix.from_Matrix(matrix)
    rhs_domain = DomainMatrix.from_Matrix(rhs)
    matrix_domain, rhs_domain = matrix_domain.unify(rhs_domain, fmt="dense")
    solution, denominator = matrix_domain.solve_den(rhs_domain)
    check(
        matrix_domain.matmul(solution) == rhs_domain.scalarmul(denominator),
        "fraction-free source identity",
    )
    denominator_expression = matrix_domain.domain.to_sympy(denominator)
    coefficients = [
        sp.cancel(value / denominator_expression)
        for value in solution.to_Matrix()
    ]
    incidence = sp.Poly(
        4*c**2*d - 2*c**2 - 3*c*d + 3*c + 2*d - 4,
        b, c, d, domain=sp.QQ,
    )
    cores = {}
    residuals = {}
    for root_name, root in (("c", c), ("d", d)):
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
        residuals[root_name] = (even0, even2)
        equations = {
            "product": constant - leading / (b * d),
            "sum": middle + leading * (1 / b + 1 / d),
        }
        for kind, expression in equations.items():
            value = numerator_poly(expression, b, c, d)
            if kind == "product":
                power = 0
                while True:
                    quotient, remainder = value.div(incidence)
                    if not remainder.is_zero:
                        break
                    value = quotient.primitive()[1]
                    power += 1
                check(power == 2, f"incidence power {root_name}")
            cores[(root_name, kind)] = value
    ratio_gates = {
        str(sign): numerator_poly(
            residuals["c"][0] * residuals["d"][1]
            + sign * residuals["d"][0] * residuals["c"][1],
            b, c, d,
        )
        for sign in (-1, 1)
    }
    for sign, value in ratio_gates.items():
        while True:
            quotient, remainder = value.div(incidence)
            if not remainder.is_zero:
                break
            value = quotient.primitive()[1]
        ratio_gates[sign] = value
    return (b, c, d), cores, ratio_gates


def load_sparse(path: Path, section: str, variables):
    payload = json.loads(path.read_text())
    value = sp.Poly.from_dict(
        {
            tuple(monomial): sp.Rational(coefficient)
            for monomial, coefficient in payload["polynomials"][section]
        },
        variables, domain=sp.QQ,
    )
    check(digest(value) == payload["digests"][section], "cache digest")
    return value


def modular_record(record, d):
    return sp.Poly.from_dict(
        {(monomial[1],): int(coefficient) for monomial, coefficient in record},
        (d,), modulus=PRIME,
    )


def audit_source(data_dir: Path) -> None:
    (b, c, d), cores, ratio_gates = reconstruct()
    expected = {
        ("c", "product"): ((5, 8, 7), 392, "84ac13783b55222a"),
        ("c", "sum"): ((5, 12, 9), 745, "8a23e86f78587abe"),
        ("d", "product"): ((5, 6, 7), 290, "9274e57561535a30"),
        ("d", "sum"): ((5, 10, 9), 627, "4833ed35f7b07ba5"),
    }
    for key, (degrees, terms, wanted_digest) in expected.items():
        value = cores[key]
        check(
            tuple(value.degree(variable) for variable in (b, c, d)) == degrees,
            f"core degrees {key}",
        )
        check(len(value.terms()) == terms, f"core terms {key}")
        check(digest(value) == wanted_digest, f"core digest {key}")
        cached = load_sparse(
            data_dir / f"kb_c2_112_other_mixed_{key[0]}_cores.json",
            key[1], (b, c, d),
        )
        check(value.monic() == cached.monic(), f"core cache {key}")
    wanted_ratio = {
        "-1": ((4, 5, 5), 112, "66c6964895c7eb78"),
        "1": ((4, 7, 6), 264, "598fd83fe93660e6"),
    }
    for sign, (degrees, terms, wanted_digest) in wanted_ratio.items():
        value = ratio_gates[sign]
        check(
            tuple(value.degree(variable) for variable in (b, c, d)) == degrees,
            f"ratio degrees {sign}",
        )
        check(len(value.terms()) == terms, f"ratio terms {sign}")
        check(digest(value) == wanted_digest, f"ratio digest {sign}")
        cached = load_sparse(
            data_dir / "kb_c2_112_other_mixed_ratio_gates.json",
            sign, (b, c, d),
        )
        check(value.monic() == cached.monic(), f"ratio cache {sign}")
    factors = [
        sp.Poly(factor, b, c, d, domain=sp.QQ).primitive()[1]
        for factor, _ in sp.factor_list(ratio_gates["-1"].as_expr())[1]
    ]
    check(
        sorted((value.degree(b), value.degree(c), value.degree(d)) for value in factors)
        == [(0, 1, 1), (0, 1, 1), (1, 1, 1), (1, 1, 1), (2, 1, 1)],
        "minus ratio factor census",
    )
    plus = ratio_gates["1"]
    check(len(sp.factor_list(plus.as_expr())[1]) == 1, "plus ratio irreducibility")
    in_b = sp.Poly(plus.as_expr(), b)
    check(in_b.nth(0) == in_b.nth(4), "plus reciprocal endpoints")
    check(in_b.nth(1) == in_b.nth(3), "plus reciprocal interior")
    print("KB_C2_112_NEAR_MOVING_OTHER_MIXED_SOURCE_AUDIT_PASS")


def rebuild_factor_product(payload, d):
    product = sp.Poly(1, d, modulus=PRIME)
    for record in payload["factors"]:
        check(record["polynomial"] is not None, "missing factor polynomial")
        factor = modular_record(record["polynomial"], d).monic()
        product *= factor**record["exponent"]
    return product.monic()


def audit_artifacts(data_dir: Path) -> None:
    d = sp.symbols("d")
    affine = json.loads((
        data_dir / "kb_c2_112_other_mixed_quartic_affine_mod_gcd.json"
    ).read_text())
    check(affine["prime"] == PRIME, "affine prime")
    affine_poly = modular_record(affine["terms"], d).monic()
    check(affine_poly.degree() == 352, "affine gcd degree")
    check(rebuild_factor_product(affine, d) == affine_poly, "affine factor product")
    check(
        [record["degree"] for record in affine["factors"]]
        == [1, 1, 5, 12, 12, 1, 1, 2, 2, 4, 4, 1, 1],
        "affine factor census",
    )
    affine_fibers = json.loads((
        data_dir / "kb_c2_112_other_mixed_quartic_affine_fibers.json"
    ).read_text())
    check(len(affine_fibers["fibers"]) == 13, "affine fiber count")
    check(
        all(record["saturated_unit"] for record in affine_fibers["fibers"]),
        "affine saturated fiber",
    )
    last = [
        modular_record(record["d_factor"], d).monic()
        for record in affine_fibers["fibers"][-2:]
    ]
    check(
        (last[0] * last[1]).monic()
        == sp.Poly(d**2 + 1, d, modulus=PRIME).monic(),
        "quadratic survivor pair",
    )
    check(
        affine_fibers["fibers"][-2]["b_gcd_degrees"] == [4]
        and affine_fibers["fibers"][-1]["b_gcd_degrees"] == [4]
        and affine_fibers["fibers"][-2]["admissible_degrees"] == [0]
        and affine_fibers["fibers"][-1]["admissible_degrees"] == [0],
        "quadratic survivor saturation",
    )

    boundary = json.loads((
        data_dir / "kb_c2_112_other_mixed_quartic_boundary_mod_gcd.json"
    ).read_text())
    boundary_poly = modular_record(boundary["terms"], d).monic()
    check(boundary_poly.degree() == 772, "boundary gcd degree")
    check(
        rebuild_factor_product(boundary, d) == boundary_poly,
        "boundary factor product",
    )
    check(
        [record["degree"] for record in boundary["factors"]]
        == [1, 1, 2, 2, 4, 4, 1, 1, 1, 1, 1],
        "boundary factor census",
    )
    boundary_fibers = json.loads((
        data_dir / "kb_c2_112_other_mixed_quartic_boundary_fibers.json"
    ).read_text())
    check(len(boundary_fibers["fibers"]) == 11, "boundary fiber count")
    check(
        all(record["saturated_unit"] for record in boundary_fibers["fibers"]),
        "boundary saturated fiber",
    )
    check(
        sum(record["d_forbidden"] for record in boundary_fibers["fibers"]) == 5,
        "boundary standard fiber count",
    )
    for name in (
        "sums", "product", "product-d", "cross"
    ):
        projection = json.loads((
            data_dir
            / f"kb_c2_112_other_mixed_quartic_{name}_mod_projection.json"
        ).read_text())
        check(projection["prime"] == PRIME, f"projection prime {name}")
        check(len(projection["terms"]) > 9800, f"projection support {name}")
    print("KB_C2_112_NEAR_MOVING_OTHER_MIXED_ARTIFACT_AUDIT_PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("source", "artifacts"))
    parser.add_argument("--data-dir", type=Path, required=True)
    args = parser.parse_args()
    if args.mode == "source":
        audit_source(args.data_dir)
    else:
        audit_artifacts(args.data_dir)


if __name__ == "__main__":
    main()
