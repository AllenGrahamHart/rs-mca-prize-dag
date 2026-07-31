#!/usr/bin/env python3
"""Independent audit for the configured moving-moving near charts.

This file does not import the primary certificate.  It reconstructs the source
with ``DomainMatrix.solve_den``, checks the reciprocal trace lift directly, and
uses terminal subresultants for both elimination layers.
"""

from __future__ import annotations

import argparse
import hashlib

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


def edge_vector(left, right):
    return sp.Matrix([left * right, -(left + right), 1])


def evaluation_rows(point):
    return (
        sp.Matrix([[1, point, point**2, 0, 0]]),
        sp.Matrix([[0, 0, 0, 1 + point**2, point]]),
        sp.Matrix([[point**2, point, 1, 0, 0]]),
    )


def numerator_poly(expression, *variables):
    numerator = sp.fraction(sp.cancel(expression))[0]
    return sp.Poly(numerator, *variables, domain=sp.QQ).primitive()[1]


def reciprocal_trace_audit(source: sp.Poly, b, c, d, s):
    check(min(monomial[0] for monomial, _ in source.terms()) == 0,
          "unexpected b monomial factor")
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


def build_trace_cores(allocation, fraction_free):
    b, c, d, s = sp.symbols("b c d s", nonzero=True)
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
    first = edge_vector(a, b)
    second = edge_vector(a, 1 / b)
    target = sp.Matrix([
        sp.cancel(value)
        for value in (
            ((ell0 + ell1 / b) * first + (ell0 + b * ell1) * second)
            / (1 / b - b)
        )
    ])
    at_w = evaluation_rows(w)
    at_z = evaluation_rows(z)
    matrix = sp.Matrix.vstack(
        at_w[0] - q0 * at_w[2],
        at_w[1] - q1 * at_w[2],
        *at_z,
    )
    rhs = sp.Matrix([0, 0, *target])
    if fraction_free:
        domain_matrix = DomainMatrix.from_Matrix(matrix)
        domain_rhs = DomainMatrix.from_Matrix(rhs)
        domain_matrix, domain_rhs = domain_matrix.unify(domain_rhs, fmt="dense")
        numerator, denominator = domain_matrix.solve_den(domain_rhs)
        check(
            domain_matrix.matmul(numerator) == domain_rhs.scalarmul(denominator),
            "fraction-free source identity",
        )
        denominator_expression = domain_matrix.domain.to_sympy(denominator)
        coefficients = [
            sp.cancel(value / denominator_expression)
            for value in numerator.to_Matrix()
        ]
    else:
        coefficients = [
            sp.cancel(value) for value in matrix.inv(method="DM") * rhs
        ]

    def residual(root):
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
        return leading, middle, constant

    residuals = {"c": residual(c), "d": residual(d)}
    targets = {
        "square-xi": {
            "c": (sp.Rational(1, 2), sp.Rational(1, 2)),
            "d": (1 / d, 1 / d),
        },
        "square-ell": {
            "c": (1 / d, 1 / d),
            "d": (sp.Rational(1, 2), sp.Rational(1, 2)),
        },
        "mixed": {
            "c": (sp.Rational(1, 2), 1 / d),
            "d": (sp.Rational(1, 2), 1 / d),
        },
        "tau-square-xi": {
            "c": (sp.Integer(2), sp.Integer(2)),
            "d": (1 / d, 1 / d),
        },
        "tau-square-ell": {
            "c": (1 / d, 1 / d),
            "d": (sp.Integer(2), sp.Integer(2)),
        },
        "tau-mixed": {
            "c": (sp.Integer(2), 1 / d),
            "d": (sp.Integer(2), 1 / d),
        },
    }[allocation]
    incidence = sp.Poly(
        4*c**2*d - 2*c**2 - 3*c*d + 3*c + 2*d - 4,
        b, c, d, domain=sp.QQ,
    )
    expected_cores = {
        "square-xi": {
            ("c", "product"): ((4, 8, 6), 299, 2, "5b27d4da822910b2"),
            ("c", "sum"): ((4, 12, 8), 567, 0, "f5399a196459bb4f"),
            ("d", "product"): ((4, 6, 8), 284, 2, "72568ee71be7f479"),
            ("d", "sum"): ((4, 10, 9), 532, 0, "48c4bf1306aae34b"),
        },
        "square-ell": {
            ("c", "product"): ((4, 8, 8), 380, 2, "a3c2f655933d7fa4"),
            ("c", "sum"): ((4, 12, 9), 632, 0, "f9448c2c1e47ba1b"),
            ("d", "product"): ((4, 5, 6), 194, 2, "a9568da9b73746f3"),
            ("d", "sum"): ((4, 9, 8), 432, 0, "34219e7d8f958227"),
        },
        "mixed": {
            ("c", "product"): ((4, 8, 7), 344, 2, "35eb7004118a99f6"),
            ("c", "sum"): ((4, 12, 9), 634, 0, "61250edd35fc0302"),
            ("d", "product"): ((4, 6, 7), 264, 2, "3d61fea968400cdc"),
            ("d", "sum"): ((4, 10, 9), 534, 0, "7365d626fc5dc28f"),
        },
        "tau-square-xi": {
            ("c", "product"): ((4, 8, 6), 299, 2, "358028760cd7cba0"),
            ("c", "sum"): ((4, 12, 8), 569, 0, "9f5ab54f14b259c8"),
            ("d", "product"): ((4, 6, 8), 284, 2, "72568ee71be7f479"),
            ("d", "sum"): ((4, 10, 9), 532, 0, "48c4bf1306aae34b"),
        },
        "tau-square-ell": {
            ("c", "product"): ((4, 8, 8), 380, 2, "a3c2f655933d7fa4"),
            ("c", "sum"): ((4, 12, 9), 632, 0, "f9448c2c1e47ba1b"),
            ("d", "product"): ((4, 5, 6), 194, 2, "eb61169143695dcb"),
            ("d", "sum"): ((4, 9, 8), 434, 0, "1dc3011fa04a0715"),
        },
        "tau-mixed": {
            ("c", "product"): ((4, 8, 7), 344, 2, "7989027e9c1d34fd"),
            ("c", "sum"): ((4, 12, 9), 632, 0, "2e50b8c81db25ee2"),
            ("d", "product"): ((4, 6, 7), 264, 2, "54ced314ef2e355e"),
            ("d", "sum"): ((4, 10, 9), 529, 0, "0c28c5e953424d27"),
        },
    }[allocation]
    cores = {}
    for root_name in ("c", "d"):
        leading, middle, constant = residuals[root_name]
        root_targets = targets[root_name]
        raw = {
            "product": numerator_poly(
                constant - leading * root_targets[0] * root_targets[1],
                b, c, d,
            ),
            "sum": numerator_poly(
                middle + leading * sum(root_targets), b, c, d
            ),
        }
        for kind, polynomial in raw.items():
            incidence_power = 0
            core = polynomial
            if kind == "product":
                while True:
                    quotient, remainder = core.div(incidence)
                    if not remainder.is_zero:
                        break
                    core = quotient.primitive()[1]
                    incidence_power += 1
            expected = expected_cores[(root_name, kind)]
            check(
                tuple(core.degree(variable) for variable in (b, c, d))
                == expected[0],
                f"core degrees {root_name}/{kind}",
            )
            check(len(core.terms()) == expected[1],
                  f"core terms {root_name}/{kind}")
            check(incidence_power == expected[2],
                  f"incidence power {root_name}/{kind}")
            check(digest(core) == expected[3],
                  f"core digest {root_name}/{kind}")
            reconstructed = core * incidence**incidence_power
            check(reconstructed.monic() == polynomial.monic(),
                  f"incidence reconstruction {root_name}/{kind}")
            cores[(root_name, kind)] = core

    expected_traces = {
        "square-xi": {
            ("c", "product"): ((2, 8, 6), 181, "736a52293558c61d"),
            ("c", "sum"): ((2, 12, 8), 342, "3164f186a76328f5"),
            ("d", "product"): ((2, 6, 8), 172, "f0bba9bf4f23b8d2"),
            ("d", "sum"): ((2, 10, 9), 321, "2414ff4e8cdee299"),
        },
        "square-ell": {
            ("c", "product"): ((2, 8, 8), 230, "162035e9c06a96e0"),
            ("c", "sum"): ((2, 12, 9), 381, "a4fe8c32d48892ac"),
            ("d", "product"): ((2, 5, 6), 118, "a204237915868784"),
            ("d", "sum"): ((2, 9, 8), 261, "02be6fc5511268da"),
        },
        "mixed": {
            ("c", "product"): ((2, 8, 7), 208, "c4cd8952673f0927"),
            ("c", "sum"): ((2, 12, 9), 382, "bcea0eb05a3f0389"),
            ("d", "product"): ((2, 6, 7), 160, "886ca4ba23104dc5"),
            ("d", "sum"): ((2, 10, 9), 322, "14d50a46ac8b6b61"),
        },
        "tau-square-xi": {
            ("c", "product"): ((2, 8, 6), 181, "05c2e7899b89ec0e"),
            ("c", "sum"): ((2, 12, 8), 343, "c627b196276df586"),
            ("d", "product"): ((2, 6, 8), 172, "f0bba9bf4f23b8d2"),
            ("d", "sum"): ((2, 10, 9), 321, "2414ff4e8cdee299"),
        },
        "tau-square-ell": {
            ("c", "product"): ((2, 8, 8), 230, "162035e9c06a96e0"),
            ("c", "sum"): ((2, 12, 9), 381, "a4fe8c32d48892ac"),
            ("d", "product"): ((2, 5, 6), 118, "5d8fbd6b0b3f749d"),
            ("d", "sum"): ((2, 9, 8), 262, "5e2df8c7faca28bc"),
        },
        "tau-mixed": {
            ("c", "product"): ((2, 8, 7), 208, "b3fe3e2204921ff2"),
            ("c", "sum"): ((2, 12, 9), 381, "c3cb520e5c94e733"),
            ("d", "product"): ((2, 6, 7), 160, "788ff68c772c7958"),
            ("d", "sum"): ((2, 10, 9), 319, "4e3f87d61395b853"),
        },
    }[allocation]
    traces = {}
    for key, core in cores.items():
        trace = reciprocal_trace_audit(core, b, c, d, s)
        expected = expected_traces[key]
        check(
            tuple(trace.degree(variable) for variable in (s, c, d))
            == expected[0],
            f"trace degrees {key}",
        )
        check(len(trace.terms()) == expected[1], f"trace terms {key}")
        check(digest(trace) == expected[2], f"trace digest {key}")
        traces[key] = trace
    return (b, c, d, s), traces


def expected_candidates(allocation):
    return {
        "square-xi": {
        "d + 74714126", "d + 783212335", "d + 814817488",
        "d - 348744034", "d - 556359354", "d - 729277070",
        "d**2 + 1039740829*d + 86175119",
        "d**2 + 418943894*d - 885630125",
        "d**2 + 475218768*d - 951068643",
        "d**2 + 65043334*d - 628088389",
        "d**2 + 814568104*d + 175500178",
        "d**3 + 467633272*d**2 + 328512070*d - 616337488",
        "d**3 - 407003079*d**2 - 685969478*d - 455850759",
        "d**3 - 55590487*d**2 - 1051050935*d + 972440423",
            "d**6 - 52037947*d**5 + 785177430*d**4 - 219206024*d**3 + 764602150*d**2 - 367395446*d - 783155787",
        },
        "square-ell": {
            "d + 119912127", "d + 12573110",
            "d - 581055016", "d - 760966584",
        },
        "mixed": {
            "d + 297646746", "d + 733504963", "d + 759603263",
            "d - 759603297",
            "d**2 - 171385344*d + 948574701",
            "d**2 - 21371382*d + 884638303",
            "d**2 - 690600778*d + 771988056",
            "d**2 - 955875534*d + 740291898",
            "d**2 - 976215692*d - 769168004",
            "d**3 - 508355909*d**2 - 775758617*d - 253189537",
        },
        "tau-square-xi": {
            "d + 106794058", "d + 472591055", "d + 751936539",
            "d + 968675331", "d - 112328292", "d - 751936540",
            "d**2 + 873862820*d - 938750153",
            "d**2 - 115060132*d - 38123999",
            "d**2 - 39960892*d - 577320431",
            "d**2 - 52838916*d - 177726665",
            "d**2 - 788966473*d - 260552146",
            "d**3 + 69073660*d**2 + 695812805*d + 749056474",
            "d**3 + 795807504*d**2 + 857533792*d - 778305301",
            "d**3 - 227601447*d**2 + 901721623*d + 765319207",
            "d**6 - 526590285*d**5 - 338851861*d**4 + 901768255*d**3 - 959127521*d**2 - 859850676*d - 880995540",
        },
        "tau-square-ell": {
            "d + 439834256", "d + 774802338",
            "d - 315962789", "d - 62994143",
        },
        "tau-mixed": {
            "d + 578766404", "d + 759603263", "d + 966474073",
            "d - 759603297",
            "d**2 + 525578422*d - 72234227",
            "d**2 + 658649332*d - 339877203",
            "d**2 + 932678459*d - 657765408",
            "d**2 - 965058281*d + 468185120",
            "d**2 - 414271596*d - 574170164",
            "d**3 + 121291852*d**2 + 279898868*d + 117308433",
        },
    }[allocation]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=(
        "source", "trace", "parent-c", "parent-d", "pairs",
        "classify", "classify-low", "classify-high",
    ))
    parser.add_argument(
        "--allocation", choices=(
            "square-xi", "square-ell", "mixed",
            "tau-square-xi", "tau-square-ell", "tau-mixed",
        ),
        default="square-xi",
    )
    args = parser.parse_args()
    if args.allocation in ("square-xi", "tau-square-xi"):
        check(args.mode != "classify", "square-xi audit uses bounded shards")
    else:
        check(args.mode not in ("classify-low", "classify-high"),
              "square-ell audit uses one classification shard")
    label = {
        "square-xi": "A_SQUARE",
        "square-ell": "A_SQUARE_ELL",
        "mixed": "A_MIXED",
        "tau-square-xi": "TAU_SQUARE",
        "tau-square-ell": "TAU_SQUARE_ELL",
        "tau-mixed": "TAU_MIXED",
    }[args.allocation]
    fraction_free = args.mode in ("source", "trace")
    (b, c, d, s), traces = build_trace_cores(args.allocation, fraction_free)
    if args.mode in ("source", "trace"):
        print(
            "KB_C2_112_NEAR_MOVING_TEMPLATE_"
            f"{label}_"
            f"{args.mode.upper()}_AUDIT_PASS fraction_free_source=true "
            "reciprocal_lift=true",
            flush=True,
        )
        return

    expected_resultants = {
        "square-xi": {
            "c": ("830a8747ce80372c", {
                "6a515ecf832aff78": 2, "e31255d5e81e2509": 2,
                "4aa033e0505df8f1": 4, "73c55ff149852dee": 4,
                "dbe56c4d43b264a2": 4, "cb4fd487538b0eff": 4,
                "477785c532483181": 12, "7a7743ce53fe8f77": 12,
                "fb37b983fcfb060a": 1, "9396ced8aa4cfa67": 1,
                "21ee8a55421c92a9": 1,
            }),
            "d": ("43a8347e92f7f81d", {
                "6a515ecf832aff78": 8, "e31255d5e81e2509": 8,
                "19d832b1f64387da": 2, "9622b8845f94fd73": 1,
                "4975135dd6af0fc0": 4, "dbe56c4d43b264a2": 4,
                "824f64bb4a05a043": 4, "cb4fd487538b0eff": 4,
                "477785c532483181": 8, "c7aea723bf6f84a1": 1,
                "dbac8f34560fc4e3": 1,
            }),
        },
        "square-ell": {
            "c": ("4b4738172d468601", {
                "4aa033e0505df8f1": 4, "6a515ecf832aff78": 4,
                "e31255d5e81e2509": 4, "73c55ff149852dee": 4,
                "19d832b1f64387da": 2, "dbe56c4d43b264a2": 4,
                "cb4fd487538b0eff": 4, "477785c532483181": 12,
                "7a7743ce53fe8f77": 12, "90db6ed8f237340f": 1,
                "39a8eb9fc1019be9": 1, "4805246499888132": 1,
            }),
            "d": ("7f225ae889ff6913", {
                "73c55ff149852dee": 1, "6a515ecf832aff78": 8,
                "e31255d5e81e2509": 8, "824f64bb4a05a043": 2,
                "4975135dd6af0fc0": 4, "dbe56c4d43b264a2": 4,
                "cb4fd487538b0eff": 4, "477785c532483181": 8,
                "c753072a5bf68171": 1, "6ba62bd34c05e0ff": 1,
            }),
        },
        "mixed": {
            "c": ("ff275ab748f48780", {
                "6a515ecf832aff78": 2, "e31255d5e81e2509": 2,
                "4aa033e0505df8f1": 4, "73c55ff149852dee": 4,
                "19d832b1f64387da": 2, "dbe56c4d43b264a2": 4,
                "cb4fd487538b0eff": 4, "477785c532483181": 12,
                "7a7743ce53fe8f77": 12, "067a3b42540bb240": 1,
            }),
            "d": ("345a2353ff8883f5", {
                "6a515ecf832aff78": 8, "e31255d5e81e2509": 8,
                "19d832b1f64387da": 2, "4975135dd6af0fc0": 4,
                "dbe56c4d43b264a2": 4, "824f64bb4a05a043": 4,
                "cb4fd487538b0eff": 4, "477785c532483181": 8,
                "07c011183de4549a": 1,
            }),
        },
        "tau-square-xi": {
            "c": ("1c20140f6e4a7549", {
                "6a515ecf832aff78": 2, "e31255d5e81e2509": 2,
                "4aa033e0505df8f1": 4, "73c55ff149852dee": 4,
                "dbe56c4d43b264a2": 4, "cb4fd487538b0eff": 4,
                "477785c532483181": 12, "7a7743ce53fe8f77": 12,
                "3abdced663de96c0": 1, "4c11afeb6140b7c8": 1,
                "681ae7138c057bce": 1,
            }),
            "d": ("43a8347e92f7f81d", {
                "6a515ecf832aff78": 8, "e31255d5e81e2509": 8,
                "19d832b1f64387da": 2, "9622b8845f94fd73": 1,
                "4975135dd6af0fc0": 4, "dbe56c4d43b264a2": 4,
                "824f64bb4a05a043": 4, "cb4fd487538b0eff": 4,
                "477785c532483181": 8, "c7aea723bf6f84a1": 1,
                "dbac8f34560fc4e3": 1,
            }),
        },
        "tau-square-ell": {
            "c": ("4b4738172d468601", {
                "4aa033e0505df8f1": 4, "6a515ecf832aff78": 4,
                "e31255d5e81e2509": 4, "73c55ff149852dee": 4,
                "19d832b1f64387da": 2, "dbe56c4d43b264a2": 4,
                "cb4fd487538b0eff": 4, "477785c532483181": 12,
                "7a7743ce53fe8f77": 12, "90db6ed8f237340f": 1,
                "39a8eb9fc1019be9": 1, "4805246499888132": 1,
            }),
            "d": ("48395b300501d597", {
                "4aa033e0505df8f1": 1, "6a515ecf832aff78": 8,
                "e31255d5e81e2509": 8, "4975135dd6af0fc0": 2,
                "dbe56c4d43b264a2": 4, "824f64bb4a05a043": 4,
                "cb4fd487538b0eff": 4, "477785c532483181": 8,
                "0274d6ca7d3e45b7": 1, "7d2994700e23736a": 1,
            }),
        },
        "tau-mixed": {
            "c": ("610f5b1189c150ce", {
                "6a515ecf832aff78": 2, "e31255d5e81e2509": 2,
                "4aa033e0505df8f1": 4, "73c55ff149852dee": 4,
                "19d832b1f64387da": 2, "dbe56c4d43b264a2": 4,
                "cb4fd487538b0eff": 4, "477785c532483181": 12,
                "7a7743ce53fe8f77": 12, "5db5e5fa2e141e59": 1,
            }),
            "d": ("8173c0db21c9e654", {
                "6a515ecf832aff78": 8, "e31255d5e81e2509": 8,
                "19d832b1f64387da": 2, "4975135dd6af0fc0": 4,
                "dbe56c4d43b264a2": 4, "824f64bb4a05a043": 4,
                "cb4fd487538b0eff": 4, "477785c532483181": 8,
                "70ab1987477282b1": 1,
            }),
        },
    }[args.allocation]

    def parent(root_name):
        value = terminal_subresultant(
            traces[(root_name, "product")],
            traces[(root_name, "sum")],
            s, c, d,
        )
        wanted_digest, wanted_factors = expected_resultants[root_name]
        check(digest(value) == wanted_digest, f"parent digest {root_name}")
        check(factor_map(value, c, d) == wanted_factors,
              f"parent factor census {root_name}")
        selected = {
            "square-xi": {
                "c": {"fb37b983fcfb060a", "9396ced8aa4cfa67", "21ee8a55421c92a9"},
                "d": {"9622b8845f94fd73", "c7aea723bf6f84a1", "dbac8f34560fc4e3"},
            },
            "square-ell": {
                "c": {"90db6ed8f237340f", "39a8eb9fc1019be9", "4805246499888132"},
                "d": {"c753072a5bf68171", "6ba62bd34c05e0ff"},
            },
            "mixed": {
                "c": {"067a3b42540bb240"},
                "d": {"07c011183de4549a"},
            },
            "tau-square-xi": {
                "c": {"3abdced663de96c0", "4c11afeb6140b7c8", "681ae7138c057bce"},
                "d": {"9622b8845f94fd73", "c7aea723bf6f84a1", "dbac8f34560fc4e3"},
            },
            "tau-square-ell": {
                "c": {"90db6ed8f237340f", "39a8eb9fc1019be9", "4805246499888132"},
                "d": {"0274d6ca7d3e45b7", "7d2994700e23736a"},
            },
            "tau-mixed": {
                "c": {"5db5e5fa2e141e59"},
                "d": {"70ab1987477282b1"},
            },
        }[args.allocation][root_name]
        forbidden_parent = {
            "square-xi": {
                "c": (d - 1, d + 1, d - 2, 2*d - 1,
                      c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1, c + 1),
                "d": (d - 1, d + 1, d, c - 2,
                      c*d - 1, 2*c - 1, 5*c*d - 4*c - 4*d + 5, c - 1),
            },
            "square-ell": {
                "c": (d - 2, d - 1, d + 1, 2*d - 1, d,
                      c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1, c + 1),
                "d": (2*d - 1, d - 1, d + 1, 2*c - 1, c - 2,
                      c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1),
            },
            "mixed": {
                "c": (d - 1, d + 1, d - 2, 2*d - 1, d,
                      c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1, c + 1),
                "d": (d - 1, d + 1, d, c - 2,
                      c*d - 1, 2*c - 1, 5*c*d - 4*c - 4*d + 5, c - 1),
            },
            "tau-square-xi": {
                "c": (d - 1, d + 1, d - 2, 2*d - 1,
                      c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1, c + 1),
                "d": (d - 1, d + 1, d, c - 2,
                      c*d - 1, 2*c - 1, 5*c*d - 4*c - 4*d + 5, c - 1),
            },
            "tau-square-ell": {
                "c": (d - 2, d - 1, d + 1, 2*d - 1, d,
                      c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1, c + 1),
                "d": (d - 2, d - 1, d + 1, c - 2, 2*c - 1,
                      c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1),
            },
            "tau-mixed": {
                "c": (d - 1, d + 1, d - 2, 2*d - 1, d,
                      c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1, c + 1),
                "d": (d - 1, d + 1, d, c - 2,
                      c*d - 1, 2*c - 1, 5*c*d - 4*c - 4*d + 5, c - 1),
            },
        }[args.allocation][root_name]
        forbidden_digests = {
            digest(sp.Poly(factor, c, d, domain=sp.QQ))
            for factor in forbidden_parent
        }
        check(
            set(wanted_factors) == selected | forbidden_digests,
            f"parent forbidden binding {root_name}",
        )
        return value

    if args.mode in ("parent-c", "parent-d"):
        root_name = args.mode[-1]
        parent(root_name)
        print(
            "KB_C2_112_NEAR_MOVING_TEMPLATE_"
            f"{label}_"
            f"PARENT_{root_name.upper()}_AUDIT_PASS terminal_subresultant=true",
            flush=True,
        )
        return

    candidate_keys = expected_candidates(args.allocation)
    if args.mode in ("classify", "classify-low", "classify-high"):
        ordered = sorted(candidate_keys)
        if args.mode == "classify-low":
            selected = ordered[:10]
        elif args.mode == "classify-high":
            selected = ordered[10:]
        else:
            selected = ordered
        candidates = {
            key: sp.Poly(
                sp.sympify(key, locals={"d": d}), d, modulus=CHARACTERISTIC
            ).monic()
            for key in selected
        }
    else:
        expected_pairs = {
            "square-xi": {
                (0, 0): ("1f08ddfc48ccd364", {
                    "f93c38ef339888a3": 1, "3e8b7ae50a0eb368": 1,
                    "bc3da4bcdb93303f": 1, "b8907990ebf04ed3": 3,
                }),
                (0, 1): ("7b1a60698f1d453d", {
                    "f93c38ef339888a3": 1, "bc3da4bcdb93303f": 2,
                    "b8907990ebf04ed3": 3, "3e8b7ae50a0eb368": 4,
                }),
                (0, 2): ("7baa9d358b67c4b3", {
                    "f93c38ef339888a3": 2, "b8907990ebf04ed3": 2,
                    "3e8b7ae50a0eb368": 5, "f5607dc060a8b24c": 1,
                }),
                (1, 0): ("266373746bf5a434", {
                    "f93c38ef339888a3": 1, "3e8b7ae50a0eb368": 1,
                    "b8907990ebf04ed3": 2, "35a1079ff1c3092b": 1,
                }),
                (1, 1): ("9088c346e4574364", {
                    "f93c38ef339888a3": 1, "b8907990ebf04ed3": 2,
                    "3e8b7ae50a0eb368": 3, "0d86b3fdadf538f8": 1,
                }),
                (1, 2): ("801c3e3307141c22", {
                    "f93c38ef339888a3": 2, "b8907990ebf04ed3": 2,
                    "3e8b7ae50a0eb368": 5, "8fb853f59f7d6c72": 1,
                }),
                (2, 0): ("259d7f61b4116377", {
                    "bc3da4bcdb93303f": 1, "f93c38ef339888a3": 2,
                    "3e8b7ae50a0eb368": 2, "b8907990ebf04ed3": 2,
                    "c89ad00032ecc4af": 1,
                }),
                (2, 1): ("2e12bb9e81d5076a", {
                    "f93c38ef339888a3": 2, "bc3da4bcdb93303f": 2,
                    "b8907990ebf04ed3": 2, "3e8b7ae50a0eb368": 7,
                    "e6d74fc277bac3f6": 1,
                }),
                (2, 2): ("4a842f51757132b7", {
                    "f93c38ef339888a3": 4, "b8907990ebf04ed3": 6,
                    "3e8b7ae50a0eb368": 10, "f8d3ce8d2ca2936b": 1,
                }),
            },
            "square-ell": {
                (0, 0): ("cacf0935414003b8", {
                    "3e8b7ae50a0eb368": 2, "b8907990ebf04ed3": 2,
                }),
                (0, 1): ("673e881e67dbe000", {
                    "f93c38ef339888a3": 2, "3e8b7ae50a0eb368": 2,
                    "b8907990ebf04ed3": 2, "47202e4cec41c165": 2,
                }),
                (1, 0): ("69f68b152fb0fb7e", {
                    "b8907990ebf04ed3": 2, "3e8b7ae50a0eb368": 3,
                    "b2323407968c3731": 1,
                }),
                (1, 1): ("e68bf89ec438dd41", {
                    "f93c38ef339888a3": 2, "b8907990ebf04ed3": 2,
                    "3e8b7ae50a0eb368": 3, "ec928b551828440d": 1,
                }),
                (2, 0): ("c76ed153d004aadf", {
                    "b8907990ebf04ed3": 2, "3e8b7ae50a0eb368": 5,
                    "1bfe0ebb9889813a": 1,
                }),
                (2, 1): ("9c685995254fb8b6", {
                    "f93c38ef339888a3": 4, "3e8b7ae50a0eb368": 5,
                    "b8907990ebf04ed3": 6, "279f89e289adc46e": 1,
                }),
            },
            "mixed": {
                (0, 0): ("70f26589e602e699", {
                    "f93c38ef339888a3": 16,
                    "b8907990ebf04ed3": 24,
                    "3e8b7ae50a0eb368": 30,
                    "badaaa15f719fc0a": 1,
                    "7c38bfaa7ed117b9": 1,
                    "ddc62481be50cdd9": 1,
                    "c23e461afce62a1f": 1,
                }),
            },
            "tau-square-xi": {
                (0, 0): ("3ad4140400e9ce65", {
                    "3e8b7ae50a0eb368": 1, "bc3da4bcdb93303f": 1,
                    "b8907990ebf04ed3": 1, "f93c38ef339888a3": 3,
                }),
                (0, 1): ("928fca15913ce5e7", {
                    "b8907990ebf04ed3": 1, "bc3da4bcdb93303f": 2,
                    "f93c38ef339888a3": 3, "3e8b7ae50a0eb368": 4,
                }),
                (0, 2): ("817d4efb72deb513", {
                    "f93c38ef339888a3": 2, "b8907990ebf04ed3": 2,
                    "3e8b7ae50a0eb368": 5, "52920a909c99bab6": 1,
                }),
                (1, 0): ("7e6ad36b97b4c04e", {
                    "3e8b7ae50a0eb368": 1, "b8907990ebf04ed3": 1,
                    "f93c38ef339888a3": 2, "dcc2356ca0e24715": 1,
                }),
                (1, 1): ("45e52720c83dbfe6", {
                    "b8907990ebf04ed3": 1, "f93c38ef339888a3": 2,
                    "3e8b7ae50a0eb368": 3, "9dec099865fa548f": 1,
                }),
                (1, 2): ("d597519a1517686e", {
                    "f93c38ef339888a3": 2, "b8907990ebf04ed3": 2,
                    "3e8b7ae50a0eb368": 5, "f12098462849824b": 1,
                }),
                (2, 0): ("8bf944afdda7cc06", {
                    "bc3da4bcdb93303f": 1, "f93c38ef339888a3": 2,
                    "3e8b7ae50a0eb368": 2, "b8907990ebf04ed3": 2,
                    "94c23a24a8038259": 1,
                }),
                (2, 1): ("c1c0cb27616f1047", {
                    "f93c38ef339888a3": 2, "bc3da4bcdb93303f": 2,
                    "b8907990ebf04ed3": 2, "3e8b7ae50a0eb368": 7,
                    "f2a25c156aa0a61e": 1,
                }),
                (2, 2): ("3a86abd59214a759", {
                    "b8907990ebf04ed3": 4, "f93c38ef339888a3": 6,
                    "3e8b7ae50a0eb368": 10, "bfd0f39529b5700a": 1,
                }),
            },
            "tau-square-ell": {
                (0, 0): ("7fd36498e8377b5b", {
                    "f93c38ef339888a3": 2, "3e8b7ae50a0eb368": 2,
                }),
                (0, 1): ("319a50d2845ae1eb", {
                    "f93c38ef339888a3": 2, "3e8b7ae50a0eb368": 2,
                    "b8907990ebf04ed3": 2, "b81870c975e426d3": 2,
                }),
                (1, 0): ("3ddbb93873503afe", {
                    "f93c38ef339888a3": 2, "3e8b7ae50a0eb368": 3,
                    "d0a7ef78715814e9": 1,
                }),
                (1, 1): ("3963fb6b9c4b5b28", {
                    "f93c38ef339888a3": 2, "b8907990ebf04ed3": 2,
                    "3e8b7ae50a0eb368": 3, "f00a0692b7d41f5c": 1,
                }),
                (2, 0): ("e972eec91546dea1", {
                    "f93c38ef339888a3": 2, "3e8b7ae50a0eb368": 5,
                    "1aa419972f5e45f9": 1,
                }),
                (2, 1): ("3fb19be3040f83d8", {
                    "b8907990ebf04ed3": 4, "3e8b7ae50a0eb368": 5,
                    "f93c38ef339888a3": 6, "c1dc268787c493ae": 1,
                }),
            },
            "tau-mixed": {
                (0, 0): ("6c0e718979cba2e1", {
                    "b8907990ebf04ed3": 16, "f93c38ef339888a3": 24,
                    "3e8b7ae50a0eb368": 30, "badaaa15f719fc0a": 1,
                    "db2acfdd67aea0a8": 1, "2ec31dcc2a54fbf4": 1,
                    "249f7b73ad53d5ee": 1,
                }),
            },
        }[args.allocation]
        wanted = {
            "square-xi": {
                "c": ("fb37b983fcfb060a", "9396ced8aa4cfa67", "21ee8a55421c92a9"),
                "d": ("9622b8845f94fd73", "c7aea723bf6f84a1", "dbac8f34560fc4e3"),
            },
            "square-ell": {
                "c": ("90db6ed8f237340f", "39a8eb9fc1019be9", "4805246499888132"),
                "d": ("c753072a5bf68171", "6ba62bd34c05e0ff"),
            },
            "mixed": {
                "c": ("067a3b42540bb240",),
                "d": ("07c011183de4549a",),
            },
            "tau-square-xi": {
                "c": ("3abdced663de96c0", "4c11afeb6140b7c8", "681ae7138c057bce"),
                "d": ("9622b8845f94fd73", "c7aea723bf6f84a1", "dbac8f34560fc4e3"),
            },
            "tau-square-ell": {
                "c": ("90db6ed8f237340f", "39a8eb9fc1019be9", "4805246499888132"),
                "d": ("0274d6ca7d3e45b7", "7d2994700e23736a"),
            },
            "tau-mixed": {
                "c": ("5db5e5fa2e141e59",),
                "d": ("70ab1987477282b1",),
            },
        }[args.allocation]
        components = {}
        for root_name in ("c", "d"):
            value = parent(root_name)
            by_digest = {
                digest(sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]):
                sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
                for factor, _ in sp.factor_list(value.as_expr())[1]
            }
            check(all(key in by_digest for key in wanted[root_name]),
                  f"parent component selection {root_name}")
            components[root_name] = [by_digest[key] for key in wanted[root_name]]
        candidates = {}
        standard = {
            str(sp.Poly(value, d, modulus=CHARACTERISTIC).monic().as_expr())
            for value in (d - 2, d - 1, d + 1, 2*d - 1)
        }
        for left_index in range(len(components["c"])):
            for right_index in range(len(components["d"])):
                projection = terminal_subresultant(
                    components["c"][left_index],
                    components["d"][right_index],
                    c, d,
                )
                wanted_digest, wanted_factors = expected_pairs[
                    (left_index, right_index)
                ]
                check(digest(projection) == wanted_digest,
                      f"pair digest {left_index},{right_index}")
                check(factor_map(projection, d) == wanted_factors,
                      f"pair factor census {left_index},{right_index}")
                _, integral = projection.clear_denoms(convert=True)
                for factor, _ in sp.factor_list(
                    integral.as_expr(), modulus=CHARACTERISTIC
                )[1]:
                    polynomial = sp.Poly(
                        factor, d, modulus=CHARACTERISTIC
                    ).monic()
                    key = str(polynomial.as_expr())
                    if polynomial.degree() and 6 % polynomial.degree() == 0 \
                            and key not in standard:
                        candidates[key] = polynomial
        check(set(candidates) == candidate_keys, "candidate router coverage")
        print(
            "KB_C2_112_NEAR_MOVING_TEMPLATE_"
            f"{label}_PAIRS_AUDIT_PASS terminal_subresultant=true "
            f"characteristic=2130706433 candidates={len(candidates)}",
            flush=True,
        )
        return

    forbidden = (
        c * d
        * (c - 2) * (2*c - 1) * (c - 1) * (c + 1)
        * (d - 2) * (2*d - 1) * (d - 1) * (d + 1)
        * (c - d) * (c*d - 1)
        * (2*s - 5) * (s**2 - 4)
        * (c*s - c**2 - 1) * (d*s - d**2 - 1)
        * (5*c*d - 4*c - 4*d + 5)
        * (4*c**2*d - 2*c**2 - 3*c*d + 3*c + 2*d - 4)
    )
    integral_traces = []
    for value in traces.values():
        _, integral = value.clear_denoms(convert=True)
        integral_traces.append(integral.as_expr())
    inverse = sp.symbols("inverse")
    for key, candidate in sorted(candidates.items()):
        saturated = sp.groebner(
            [
                *integral_traces,
                candidate.as_expr(),
                inverse * forbidden - 1,
            ],
            inverse, s, c, d,
            order="lex",
            modulus=CHARACTERISTIC,
        )
        check(
            len(saturated.polys) == 1
            and saturated.polys[0].as_expr() == 1,
            f"admissible candidate survives: {key}",
        )
    check(sp.isprime(CHARACTERISTIC), "audit characteristic is not prime")
    print(
        "KB_C2_112_NEAR_MOVING_TEMPLATE_"
        f"{label}_"
        f"{args.mode.replace('-', '_').upper()}_AUDIT_PASS "
        f"characteristic={CHARACTERISTIC} candidates={len(candidates)} "
        "forbidden_saturation=true",
        flush=True,
    )


if __name__ == "__main__":
    main()
