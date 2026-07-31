#!/usr/bin/env python3
"""No-import audit for the moving-moving other-xi square-xi chart."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix


CHARACTERISTIC = 2130706433


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


def reciprocal_trace(source: sp.Poly, b, c, d, s):
    degree = source.degree(b)
    check(degree % 2 == 0, "odd reciprocal degree")
    check(
        sp.Poly(
            sp.expand(b**degree * source.as_expr().subs(b, 1 / b)),
            b, c, d, domain=sp.QQ,
        ).monic() == source.monic(),
        "reciprocal symmetry",
    )
    middle = degree // 2
    univariate = sp.Poly(source.as_expr(), b)
    dickson = [sp.Integer(2), s]
    for _ in range(2, middle + 1):
        dickson.append(sp.expand(s * dickson[-1] - dickson[-2]))
    expression = univariate.nth(middle)
    for offset in range(1, middle + 1):
        low = univariate.nth(middle - offset)
        high = univariate.nth(middle + offset)
        check(sp.expand(low - high) == 0, "reciprocal coefficient pair")
        expression += high * dickson[offset]
    trace = sp.Poly(expression, s, c, d, domain=sp.QQ).primitive()[1]
    lifted = numerator_poly(
        b**middle * trace.as_expr().subs(s, b + 1 / b), b, c, d
    )
    check(lifted.monic() == source.monic(), "reciprocal trace lift")
    return trace


def terminal_subresultant(left: sp.Poly, right: sp.Poly, eliminate, *remain):
    sequence = sp.subresultants(left.as_expr(), right.as_expr(), eliminate)
    check(bool(sequence), "empty subresultant sequence")
    terminal = sp.Poly(sequence[-1], eliminate, *remain, domain=sp.QQ)
    check(terminal.degree(eliminate) == 0, "terminal subresultant degree")
    return sp.Poly(
        terminal.as_expr(), *remain, domain=sp.QQ
    ).primitive()[1]


def factor_map(polynomial: sp.Poly, *variables):
    return {
        digest(sp.Poly(value, *variables, domain=sp.QQ).primitive()[1]): exponent
        for value, exponent in sp.factor_list(polynomial.as_expr())[1]
    }


def load_sparse(path: Path, section: str, variables):
    payload = json.loads(path.read_text())
    record = payload["polynomials"][section]
    terms = {
        tuple(monomial): sp.Rational(coefficient)
        for monomial, coefficient in record
    }
    value = sp.Poly.from_dict(terms, variables, domain=sp.QQ)
    check(digest(value) == payload["digests"][section], "core data digest")
    return value


def load_components(data_dir: Path, root, c, d):
    path = data_dir / f"kb_c2_112_other_square-xi_{root}_components.json"
    payload = json.loads(path.read_text())
    values = []
    for record in payload["components"]:
        terms = {
            tuple(monomial): sp.Rational(coefficient)
            for monomial, coefficient in record["terms"]
        }
        value = sp.Poly.from_dict(terms, (c, d), domain=sp.QQ)
        check(digest(value) == record["digest"], "component data digest")
        values.append((record["digest"], value))
    return values


def reconstruct_cores(root_name):
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
    domain_matrix = DomainMatrix.from_Matrix(matrix)
    domain_rhs = DomainMatrix.from_Matrix(rhs)
    domain_matrix, domain_rhs = domain_matrix.unify(domain_rhs, fmt="dense")
    solution, denominator = domain_matrix.solve_den(domain_rhs)
    check(
        domain_matrix.matmul(solution) == domain_rhs.scalarmul(denominator),
        "fraction-free source identity",
    )
    denominator_expression = domain_matrix.domain.to_sympy(denominator)
    coefficients = [
        sp.cancel(value / denominator_expression)
        for value in solution.to_Matrix()
    ]
    root = c if root_name == "c" else d
    x0, x1, x2, x3, x4 = coefficients
    even0 = sp.cancel(x0 + root * x3 + root**2 * x2)
    even1 = sp.cancel(x1 + root * x4 + root**2 * x1)
    even2 = sp.cancel(x2 + root * x3 + root**2 * x0)
    local_odd0 = sp.cancel(odd0 + root * odd1 + root**2 * odd2)
    local_odd1 = sp.cancel(odd2 + root * odd1 + root**2 * odd0)
    check(sp.cancel(even0 + w * even1 + w**2 * even2) == 0,
          "even forced root")
    check(sp.cancel(local_odd0 + w * local_odd1) == 0,
          "odd forced root")
    leading = sp.cancel(even2**2)
    middle = sp.cancel(
        2 * even1 * even2 - local_odd1**2 + 2 * w * leading
    )
    constant = sp.cancel(even0**2 / w**2)
    targets = (
        (1 / b, 1 / b) if root_name == "c" else (1 / d, 1 / d)
    )
    raw = {
        "product": numerator_poly(
            constant - leading * targets[0] * targets[1], b, c, d
        ),
        "sum": numerator_poly(middle + leading * sum(targets), b, c, d),
    }
    incidence = sp.Poly(
        4*c**2*d - 2*c**2 - 3*c*d + 3*c + 2*d - 4,
        b, c, d, domain=sp.QQ,
    )
    core = raw["product"]
    power = 0
    while True:
        quotient, remainder = core.div(incidence)
        if not remainder.is_zero:
            break
        core = quotient.primitive()[1]
        power += 1
    check(power == 2, "incidence power")
    raw["product"] = core
    return (b, c, d), raw


def main() -> None:
    parser = argparse.ArgumentParser()
    modes = [
        "source-c", "source-d", "components-c", "components-d",
        *(f"pair{left}{right}" for left in range(2) for right in range(3)),
        *(f"classify{index}" for index in range(8)),
    ]
    parser.add_argument("mode", choices=modes)
    parser.add_argument("--data-dir", type=Path, required=True)
    args = parser.parse_args()
    b, c, d = sp.symbols("b c d")
    if args.mode.startswith("source-"):
        root = args.mode[-1]
        (b, c, d), cores = reconstruct_cores(root)
        expected = {
            "c": {
                "product": ((6, 8, 6), 416, "4ab53941752202b3"),
                "sum": ((5, 12, 8), 684, "23b328b6dea34346"),
            },
            "d": {
                "product": ((4, 6, 8), 284, "72568ee71be7f479"),
                "sum": ((4, 10, 9), 532, "48c4bf1306aae34b"),
            },
        }[root]
        path = args.data_dir / f"kb_c2_112_other_square-xi_{root}_cores.json"
        for kind, value in cores.items():
            degrees, terms, wanted = expected[kind]
            check(tuple(value.degree(x) for x in (b, c, d)) == degrees,
                  f"source degrees {kind}")
            check(len(value.terms()) == terms, f"source terms {kind}")
            check(digest(value) == wanted, f"source digest {kind}")
            check(value.monic() == load_sparse(path, kind, (b, c, d)).monic(),
                  f"source checkpoint {kind}")
        print(
            f"KB_C2_112_NEAR_MOVING_OTHER_SQUARE_XI_SOURCE_{root.upper()}_AUDIT_PASS "
            "fraction_free_source=true",
            flush=True,
        )
        return

    core_paths = {
        root: args.data_dir / f"kb_c2_112_other_square-xi_{root}_cores.json"
        for root in ("c", "d")
    }
    cores = {
        (root, kind): load_sparse(core_paths[root], kind, (b, c, d))
        for root in ("c", "d") for kind in ("product", "sum")
    }
    standard = {
        "6a515ecf832aff78", "e31255d5e81e2509",
        "4aa033e0505df8f1", "73c55ff149852dee",
        "19d832b1f64387da", "4975135dd6af0fc0",
        "dbe56c4d43b264a2", "824f64bb4a05a043",
        "cb4fd487538b0eff", "477785c532483181",
        "7a7743ce53fe8f77",
    }
    if args.mode == "components-c":
        branches = sorted(
            (
                digest(value), value
            )
            for factor, exponent in sp.factor_list(
                cores[("c", "product")].as_expr()
            )[1]
            for value in [sp.Poly(factor, b, c, d, domain=sp.QQ).primitive()[1]]
            if exponent == 1
        )
        check([key for key, _ in branches] == [
            "f2dbb3bdc114d07d", "fd2b0e09a3a2312a"
        ], "c branch census")
        expected_parents = {
            "f2dbb3bdc114d07d": ("02901bcd7b5e39cc", {
                "e31255d5e81e2509": 2, "4aa033e0505df8f1": 4,
                "6a515ecf832aff78": 4, "73c55ff149852dee": 4,
                "dbe56c4d43b264a2": 4, "cb4fd487538b0eff": 4,
                "7a7743ce53fe8f77": 12, "477785c532483181": 14,
                "0d44f8f7254e1a65": 1, "13fb3d79b89daf53": 1,
            }),
            "fd2b0e09a3a2312a": ("0a2b29ced926a43d", {
                "6a515ecf832aff78": 2, "4aa033e0505df8f1": 6,
                "e31255d5e81e2509": 6, "73c55ff149852dee": 6,
                "dbe56c4d43b264a2": 8, "cb4fd487538b0eff": 8,
                "477785c532483181": 18, "7a7743ce53fe8f77": 18,
                "0d44f8f7254e1a65": 1,
            }),
        }
        selected = {}
        for branch_digest, branch in branches:
            parent = terminal_subresultant(
                branch, cores[("c", "sum")], b, c, d
            )
            wanted_digest, wanted_factors = expected_parents[branch_digest]
            check(digest(parent) == wanted_digest, "c parent digest")
            check(factor_map(parent, c, d) == wanted_factors,
                  "c parent factors")
            for factor, _ in sp.factor_list(parent.as_expr())[1]:
                value = sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
                if digest(value) not in standard:
                    selected[digest(value)] = value
        checkpoint = dict(load_components(args.data_dir, "c", c, d))
        check(set(selected) == set(checkpoint), "c component coverage")
        check(all(selected[key].monic() == checkpoint[key].monic()
                  for key in selected), "c component checkpoint")
        print("KB_C2_112_NEAR_MOVING_OTHER_SQUARE_XI_COMPONENTS_C_AUDIT_PASS", flush=True)
        return

    if args.mode == "components-d":
        s = sp.symbols("s")
        traces = {
            kind: reciprocal_trace(cores[("d", kind)], b, c, d, s)
            for kind in ("product", "sum")
        }
        check(digest(traces["product"]) == "f0bba9bf4f23b8d2", "d product trace")
        check(digest(traces["sum"]) == "2414ff4e8cdee299", "d sum trace")
        parent = terminal_subresultant(
            traces["product"], traces["sum"], s, c, d
        )
        check(digest(parent) == "43a8347e92f7f81d", "d parent digest")
        selected = {}
        for factor, _ in sp.factor_list(parent.as_expr())[1]:
            value = sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
            if digest(value) not in standard:
                selected[digest(value)] = value
        checkpoint = dict(load_components(args.data_dir, "d", c, d))
        check(set(selected) == set(checkpoint), "d component coverage")
        check(all(selected[key].monic() == checkpoint[key].monic()
                  for key in selected), "d component checkpoint")
        print("KB_C2_112_NEAR_MOVING_OTHER_SQUARE_XI_COMPONENTS_D_AUDIT_PASS", flush=True)
        return

    if args.mode.startswith("pair"):
        left_index, right_index = map(int, args.mode[-2:])
        left = load_components(args.data_dir, "c", c, d)[left_index][1]
        right = load_components(args.data_dir, "d", c, d)[right_index][1]
        projection = terminal_subresultant(left, right, c, d)
        expected = {
            (0, 0): ("45717df443835160", {
                "f93c38ef339888a3": 1, "bc3da4bcdb93303f": 1,
                "b8907990ebf04ed3": 1, "3e8b7ae50a0eb368": 2,
                "c85a04492dab7b12": 1,
            }),
            (0, 1): ("f17eb57458420432", {
                "f93c38ef339888a3": 1, "b8907990ebf04ed3": 1,
                "bc3da4bcdb93303f": 2, "3e8b7ae50a0eb368": 5,
                "fad413c4877dd87b": 1,
            }),
            (0, 2): ("fdc13f78c0f27fd7", {
                "f93c38ef339888a3": 2, "b8907990ebf04ed3": 2,
                "3e8b7ae50a0eb368": 7, "b46974c97473bd20": 1,
            }),
            (1, 0): ("1db833f7ec218a23", {
                "bc3da4bcdb93303f": 4, "f93c38ef339888a3": 8,
                "b8907990ebf04ed3": 8, "3e8b7ae50a0eb368": 10,
                "20f33c7cf156b9e0": 1,
            }),
            (1, 1): ("7b6dd06d29601e4b", {
                "f93c38ef339888a3": 8, "b8907990ebf04ed3": 8,
                "bc3da4bcdb93303f": 10, "3e8b7ae50a0eb368": 24,
                "2e7e4de29c38d633": 1,
            }),
            (1, 2): ("0b010d8c5566cd18", {
                "f93c38ef339888a3": 18, "b8907990ebf04ed3": 18,
                "3e8b7ae50a0eb368": 34, "039d9aaf13f5aa0d": 2,
                "8b0c6fd4e82d7f57": 1,
            }),
        }[(left_index, right_index)]
        check(digest(projection) == expected[0], "pair digest")
        check(factor_map(projection, d) == expected[1], "pair factors")
        print(
            f"KB_C2_112_NEAR_MOVING_OTHER_SQUARE_XI_PAIR_{left_index}{right_index}_AUDIT_PASS",
            flush=True,
        )
        return

    index = int(args.mode.removeprefix("classify"))
    candidates = (
        "d - 53820732",
        "d**2 - 193204367*d - 98068426",
        "d + 261596606", "d + 982346495",
        "d - 1020436165", "d - 901544254",
        "d + 583634928", "d - 583634934",
    )
    candidate = sp.Poly(
        sp.sympify(candidates[index], locals={"d": d}),
        d, modulus=CHARACTERISTIC,
    ).monic()
    basis = sp.groebner(
        [*(value.as_expr() for value in cores.values()), candidate.as_expr()],
        b, c, d, order="lex", modulus=CHARACTERISTIC,
    )
    forbidden = (
        b * c * d
        * (b - 2) * (2*b - 1) * (b - 1) * (b + 1)
        * (c - 2) * (2*c - 1) * (c - 1) * (c + 1)
        * (d - 2) * (2*d - 1) * (d - 1) * (d + 1)
        * (b - c) * (b*c - 1) * (b - d) * (b*d - 1)
        * (c - d) * (c*d - 1)
        * (5*c*d - 4*c - 4*d + 5)
        * (4*c**2*d - 2*c**2 - 3*c*d + 3*c + 2*d - 4)
    )
    unit = len(basis.polys) == 1 and basis.polys[0].as_expr() == 1
    remainder_zero = unit or basis.reduce(forbidden)[1] == 0
    saturated_unit = remainder_zero
    if not saturated_unit:
        inverse = sp.symbols("inverse")
        saturated = sp.groebner(
            [
                *(value.as_expr() for value in basis.polys),
                inverse * forbidden - 1,
            ],
            inverse, b, c, d, order="lex", modulus=CHARACTERISTIC,
        )
        saturated_unit = (
            len(saturated.polys) == 1
            and saturated.polys[0].as_expr() == 1
        )
    check(saturated_unit, "admissible candidate survives")
    print(
        f"KB_C2_112_NEAR_MOVING_OTHER_SQUARE_XI_CLASSIFY_{index}_AUDIT_PASS "
        f"candidate={candidates[index]!r}",
        flush=True,
    )


if __name__ == "__main__":
    main()
