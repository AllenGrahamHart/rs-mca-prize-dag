#!/usr/bin/env python3
"""Bounded exact probe for the nine near-positive moving-moving charts."""

from __future__ import annotations

import argparse
import hashlib

import sympy as sp


def require(condition: bool, message: str) -> None:
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


def numerator_poly(expression, b, c, d):
    numerator = sp.fraction(sp.cancel(expression))[0]
    return sp.Poly(numerator, b, c, d, domain=sp.QQ).primitive()[1]


def reciprocal_trace(polynomial: sp.Poly, b, c, d, s):
    """Return a trace polynomial after removing monomial/anti factors."""
    source = polynomial
    minimum = min(monomial[0] for monomial, _ in source.terms())
    if minimum:
        source = source.exquo(sp.Poly(b**minimum, b, c, d, domain=sp.QQ))
    removed = [f"b^{minimum}"] if minimum else []
    while True:
        degree = source.degree(b)
        reciprocal = sp.Poly(
            sp.expand(b**degree * source.as_expr().subs(b, 1 / b)),
            b,
            c,
            d,
            domain=sp.QQ,
        )
        if reciprocal.monic() == source.monic():
            break
        if reciprocal.monic() == sp.Poly(
            -source.as_expr(), b, c, d, domain=sp.QQ
        ).monic():
            divisor = sp.Poly(b**2 - 1, b, c, d, domain=sp.QQ)
            quotient, remainder = source.div(divisor)
            if not remainder.is_zero:
                return None, (*removed, "anti-nondivisible")
            source = quotient.primitive()[1]
            removed.append("b^2-1")
            continue
        return None, (*removed, "nonreciprocal")
    degree = source.degree(b)
    if degree % 2:
        return None, (*removed, "odd-palindromic-degree")
    middle = degree // 2
    in_b = sp.Poly(source.as_expr(), b)
    traces = [sp.Integer(2), s]
    for _ in range(2, middle + 1):
        traces.append(sp.expand(s * traces[-1] - traces[-2]))
    expression = in_b.nth(middle)
    for offset in range(1, middle + 1):
        high = in_b.nth(middle + offset)
        low = in_b.nth(middle - offset)
        if sp.expand(high - low) != 0:
            return None, (*removed, "coefficient-asymmetry")
        expression += high * traces[offset]
    trace = sp.Poly(
        sp.expand(expression), s, c, d, domain=sp.QQ
    ).primitive()[1]
    return trace, tuple(removed)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("xi", choices=("a", "tau", "other"))
    parser.add_argument(
        "allocation", choices=("square-xi", "square-ell", "mixed")
    )
    parser.add_argument(
        "mode",
        choices=(
            "cores", "trace", "c", "d", "pairs", "classify",
            "classify-low", "classify-high",
            *(f"pair{left}{right}" for left in range(3) for right in range(3)),
        ),
    )
    parser.add_argument("--prove", action="store_true")
    args = parser.parse_args()
    proof_chart = (args.xi, args.allocation)
    proof_label = {
        ("a", "square-xi"): "A_SQUARE",
        ("a", "square-ell"): "A_SQUARE_ELL",
        ("a", "mixed"): "A_MIXED",
        ("tau", "square-xi"): "TAU_SQUARE",
        ("tau", "square-ell"): "TAU_SQUARE_ELL",
        ("tau", "mixed"): "TAU_MIXED",
    }.get(proof_chart)
    if args.prove:
        sharded_charts = {("a", "square-xi"), ("tau", "square-xi")}
        single_shard_charts = {
            ("a", "square-ell"), ("a", "mixed"),
            ("tau", "square-ell"), ("tau", "mixed"),
        }
        require(
            (
                proof_chart in sharded_charts
                and args.mode in {
                    "cores", "trace", "c", "d", "pairs",
                    "classify-low", "classify-high",
                }
            ) or (
                proof_chart in single_shard_charts
                and args.mode in {"cores", "trace", "c", "d", "pairs", "classify"}
            ),
            "proof mode is not configured for this chart/stage",
        )

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
    coefficients = [
        sp.cancel(value)
        for value in matrix.inv(method="DM") * sp.Matrix([0, 0, *target])
    ]
    print("stage=moving_source_reconstruction", flush=True)

    def residual(root):
        x0, x1, x2, x3, x4 = coefficients
        even0 = sp.cancel(x0 + root * x3 + root**2 * x2)
        even1 = sp.cancel(x1 + root * x4 + root**2 * x1)
        even2 = sp.cancel(x2 + root * x3 + root**2 * x0)
        local_odd1 = sp.cancel(odd2 + root * odd1 + root**2 * odd0)
        leading = sp.cancel(even2**2)
        middle = sp.cancel(
            2 * even1 * even2 - local_odd1**2 + 2 * w * leading
        )
        constant = sp.cancel(even0**2 / w**2)
        return leading, middle, constant

    kappa_xi = {
        "a": sp.Rational(1, 2),
        "tau": sp.Integer(2),
        "other": 1 / b,
    }[args.xi]
    kappa_ell = 1 / d
    targets = {
        "square-xi": ((kappa_xi, kappa_xi),
                      (kappa_ell, kappa_ell)),
        "square-ell": ((kappa_ell, kappa_ell),
                       (kappa_xi, kappa_xi)),
        "mixed": ((kappa_xi, kappa_ell),
                  (kappa_xi, kappa_ell)),
    }[args.allocation]
    incidence = sp.Poly(
        4*c**2*d - 2*c**2 - 3*c*d + 3*c + 2*d - 4,
        b, c, d, domain=sp.QQ,
    )
    cores = {}
    for (root_name, root), target_roots in zip(
        (("c", c), ("d", d)), targets
    ):
        leading, middle, constant = residual(root)
        equations = {
            "product": constant
            - leading * target_roots[0] * target_roots[1],
            "sum": middle + leading * sum(target_roots),
        }
        for kind, equation in equations.items():
            polynomial = numerator_poly(equation, b, c, d)
            incidence_power = 0
            if kind == "product":
                while True:
                    quotient, remainder = polynomial.div(incidence)
                    if not remainder.is_zero:
                        break
                    polynomial = quotient.primitive()[1]
                    incidence_power += 1
            cores[(root_name, kind)] = polynomial
            print(
                f"stage={root_name}_{kind} "
                f"degrees={tuple(polynomial.degree(x) for x in (b,c,d))} "
                f"terms={len(polynomial.terms())} "
                f"incidence_power={incidence_power} digest={digest(polynomial)}",
                flush=True,
            )
    if args.prove:
        expected_cores = {
            ("a", "square-xi"): {
                ("c", "product"): ((4, 8, 6), 299, 2, "5b27d4da822910b2"),
                ("c", "sum"): ((4, 12, 8), 567, 0, "f5399a196459bb4f"),
                ("d", "product"): ((4, 6, 8), 284, 2, "72568ee71be7f479"),
                ("d", "sum"): ((4, 10, 9), 532, 0, "48c4bf1306aae34b"),
            },
            ("a", "square-ell"): {
                ("c", "product"): ((4, 8, 8), 380, 2, "a3c2f655933d7fa4"),
                ("c", "sum"): ((4, 12, 9), 632, 0, "f9448c2c1e47ba1b"),
                ("d", "product"): ((4, 5, 6), 194, 2, "a9568da9b73746f3"),
                ("d", "sum"): ((4, 9, 8), 432, 0, "34219e7d8f958227"),
            },
            ("a", "mixed"): {
                ("c", "product"): ((4, 8, 7), 344, 2, "35eb7004118a99f6"),
                ("c", "sum"): ((4, 12, 9), 634, 0, "61250edd35fc0302"),
                ("d", "product"): ((4, 6, 7), 264, 2, "3d61fea968400cdc"),
                ("d", "sum"): ((4, 10, 9), 534, 0, "7365d626fc5dc28f"),
            },
            ("tau", "square-xi"): {
                ("c", "product"): ((4, 8, 6), 299, 2, "358028760cd7cba0"),
                ("c", "sum"): ((4, 12, 8), 569, 0, "9f5ab54f14b259c8"),
                ("d", "product"): ((4, 6, 8), 284, 2, "72568ee71be7f479"),
                ("d", "sum"): ((4, 10, 9), 532, 0, "48c4bf1306aae34b"),
            },
            ("tau", "square-ell"): {
                ("c", "product"): ((4, 8, 8), 380, 2, "a3c2f655933d7fa4"),
                ("c", "sum"): ((4, 12, 9), 632, 0, "f9448c2c1e47ba1b"),
                ("d", "product"): ((4, 5, 6), 194, 2, "eb61169143695dcb"),
                ("d", "sum"): ((4, 9, 8), 434, 0, "1dc3011fa04a0715"),
            },
            ("tau", "mixed"): {
                ("c", "product"): ((4, 8, 7), 344, 2, "7989027e9c1d34fd"),
                ("c", "sum"): ((4, 12, 9), 632, 0, "2e50b8c81db25ee2"),
                ("d", "product"): ((4, 6, 7), 264, 2, "54ced314ef2e355e"),
                ("d", "sum"): ((4, 10, 9), 529, 0, "0c28c5e953424d27"),
            },
        }[proof_chart]
        for key, (degrees, terms, incidence_power, wanted_digest) \
                in expected_cores.items():
            value = cores[key]
            require(
                tuple(value.degree(variable) for variable in (b, c, d))
                == degrees,
                f"moving core degrees {key}",
            )
            require(len(value.terms()) == terms, f"moving core terms {key}")
            require(digest(value) == wanted_digest, f"moving core digest {key}")
            if key[1] == "product":
                original = numerator_poly(
                    (
                        residual(c if key[0] == "c" else d)[2]
                        - residual(c if key[0] == "c" else d)[0]
                        * targets[0 if key[0] == "c" else 1][0]
                        * targets[0 if key[0] == "c" else 1][1]
                    ),
                    b, c, d,
                )
                require(
                    original == value * incidence**incidence_power,
                    f"moving incidence quotient {key}",
                )
    if args.mode == "cores":
        if args.prove:
            print(
                "KB_C2_112_NEAR_MOVING_TEMPLATE_"
                f"{proof_label}_SOURCE_PRIMARY_PASS",
                flush=True,
            )
        return

    traces = {}
    for key, polynomial in cores.items():
        trace, removed = reciprocal_trace(polynomial, b, c, d, s)
        print(
            f"stage=trace key={key} removed={removed} "
            + (
                "failed=true" if trace is None else
                f"degrees={tuple(trace.degree(x) for x in (s,c,d))} "
                f"terms={len(trace.terms())} digest={digest(trace)}"
            ),
            flush=True,
        )
        if trace is None:
            raise RuntimeError(f"trace conversion failed for {key}")
        traces[key] = trace
    if args.prove:
        expected_traces = {
            ("a", "square-xi"): {
                ("c", "product"): ((2, 8, 6), 181, "736a52293558c61d"),
                ("c", "sum"): ((2, 12, 8), 342, "3164f186a76328f5"),
                ("d", "product"): ((2, 6, 8), 172, "f0bba9bf4f23b8d2"),
                ("d", "sum"): ((2, 10, 9), 321, "2414ff4e8cdee299"),
            },
            ("a", "square-ell"): {
                ("c", "product"): ((2, 8, 8), 230, "162035e9c06a96e0"),
                ("c", "sum"): ((2, 12, 9), 381, "a4fe8c32d48892ac"),
                ("d", "product"): ((2, 5, 6), 118, "a204237915868784"),
                ("d", "sum"): ((2, 9, 8), 261, "02be6fc5511268da"),
            },
            ("a", "mixed"): {
                ("c", "product"): ((2, 8, 7), 208, "c4cd8952673f0927"),
                ("c", "sum"): ((2, 12, 9), 382, "bcea0eb05a3f0389"),
                ("d", "product"): ((2, 6, 7), 160, "886ca4ba23104dc5"),
                ("d", "sum"): ((2, 10, 9), 322, "14d50a46ac8b6b61"),
            },
            ("tau", "square-xi"): {
                ("c", "product"): ((2, 8, 6), 181, "05c2e7899b89ec0e"),
                ("c", "sum"): ((2, 12, 8), 343, "c627b196276df586"),
                ("d", "product"): ((2, 6, 8), 172, "f0bba9bf4f23b8d2"),
                ("d", "sum"): ((2, 10, 9), 321, "2414ff4e8cdee299"),
            },
            ("tau", "square-ell"): {
                ("c", "product"): ((2, 8, 8), 230, "162035e9c06a96e0"),
                ("c", "sum"): ((2, 12, 9), 381, "a4fe8c32d48892ac"),
                ("d", "product"): ((2, 5, 6), 118, "5d8fbd6b0b3f749d"),
                ("d", "sum"): ((2, 9, 8), 262, "5e2df8c7faca28bc"),
            },
            ("tau", "mixed"): {
                ("c", "product"): ((2, 8, 7), 208, "b3fe3e2204921ff2"),
                ("c", "sum"): ((2, 12, 9), 381, "c3cb520e5c94e733"),
                ("d", "product"): ((2, 6, 7), 160, "788ff68c772c7958"),
                ("d", "sum"): ((2, 10, 9), 319, "4e3f87d61395b853"),
            },
        }[proof_chart]
        for key, (degrees, terms, wanted_digest) in expected_traces.items():
            value = traces[key]
            require(
                tuple(value.degree(variable) for variable in (s, c, d))
                == degrees,
                f"moving trace degrees {key}",
            )
            require(len(value.terms()) == terms, f"moving trace terms {key}")
            require(digest(value) == wanted_digest, f"moving trace digest {key}")
    if args.mode == "trace":
        if args.prove:
            print(
                "KB_C2_112_NEAR_MOVING_TEMPLATE_"
                f"{proof_label}_TRACE_PRIMARY_PASS",
                flush=True,
            )
        return

    characteristic = 2130706433
    candidate_keys_by_chart = {
        ("a", "square-xi"): {
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
        ("a", "square-ell"): {
            "d + 119912127", "d + 12573110",
            "d - 581055016", "d - 760966584",
        },
        ("a", "mixed"): {
            "d + 297646746", "d + 733504963", "d + 759603263",
            "d - 759603297",
            "d**2 - 171385344*d + 948574701",
            "d**2 - 21371382*d + 884638303",
            "d**2 - 690600778*d + 771988056",
            "d**2 - 955875534*d + 740291898",
            "d**2 - 976215692*d - 769168004",
            "d**3 - 508355909*d**2 - 775758617*d - 253189537",
        },
        ("tau", "square-xi"): {
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
        ("tau", "square-ell"): {
            "d + 439834256", "d + 774802338",
            "d - 315962789", "d - 62994143",
        },
        ("tau", "mixed"): {
            "d + 578766404", "d + 759603263", "d + 966474073",
            "d - 759603297",
            "d**2 + 525578422*d - 72234227",
            "d**2 + 658649332*d - 339877203",
            "d**2 + 932678459*d - 657765408",
            "d**2 - 965058281*d + 468185120",
            "d**2 - 414271596*d - 574170164",
            "d**3 + 121291852*d**2 + 279898868*d + 117308433",
        },
    }
    expected_candidate_keys = candidate_keys_by_chart.get(proof_chart, set())

    def within_components(root_name):
        resultant = sp.Poly(
            sp.resultant(
                traces[(root_name, "product")].as_expr(),
                traces[(root_name, "sum")].as_expr(),
                s,
            ),
            c,
            d,
            domain=sp.QQ,
        ).primitive()[1]
        factors = [
            (
                sp.Poly(value, c, d, domain=sp.QQ).primitive()[1],
                exponent,
            )
            for value, exponent in sp.factor_list(resultant.as_expr())[1]
        ]
        print(
            f"stage=within root={root_name} "
            f"degrees=({resultant.degree(c)},{resultant.degree(d)}) "
            f"terms={len(resultant.terms())} digest={digest(resultant)}",
            flush=True,
        )
        print(
            "stage=within_factors "
            f"root={root_name} factors={[(value.degree(c), value.degree(d), len(value.terms()), exponent, digest(value)) for value, exponent in factors]}",
            flush=True,
        )
        if args.prove:
            expected_resultants, expected_factors = {
                ("a", "square-xi"): ({
                    "c": "830a8747ce80372c", "d": "43a8347e92f7f81d",
                }, {
                    "c": {
                        "6a515ecf832aff78": 2, "e31255d5e81e2509": 2,
                        "4aa033e0505df8f1": 4, "73c55ff149852dee": 4,
                        "dbe56c4d43b264a2": 4, "cb4fd487538b0eff": 4,
                        "477785c532483181": 12, "7a7743ce53fe8f77": 12,
                        "fb37b983fcfb060a": 1, "9396ced8aa4cfa67": 1,
                        "21ee8a55421c92a9": 1,
                    },
                    "d": {
                        "6a515ecf832aff78": 8, "e31255d5e81e2509": 8,
                        "19d832b1f64387da": 2, "9622b8845f94fd73": 1,
                        "4975135dd6af0fc0": 4, "dbe56c4d43b264a2": 4,
                        "824f64bb4a05a043": 4, "cb4fd487538b0eff": 4,
                        "477785c532483181": 8, "c7aea723bf6f84a1": 1,
                        "dbac8f34560fc4e3": 1,
                    },
                }),
                ("a", "square-ell"): ({
                    "c": "4b4738172d468601", "d": "7f225ae889ff6913",
                }, {
                    "c": {
                        "4aa033e0505df8f1": 4, "6a515ecf832aff78": 4,
                        "e31255d5e81e2509": 4, "73c55ff149852dee": 4,
                        "19d832b1f64387da": 2, "dbe56c4d43b264a2": 4,
                        "cb4fd487538b0eff": 4, "477785c532483181": 12,
                        "7a7743ce53fe8f77": 12, "90db6ed8f237340f": 1,
                        "39a8eb9fc1019be9": 1, "4805246499888132": 1,
                    },
                    "d": {
                        "73c55ff149852dee": 1, "6a515ecf832aff78": 8,
                        "e31255d5e81e2509": 8, "824f64bb4a05a043": 2,
                        "4975135dd6af0fc0": 4, "dbe56c4d43b264a2": 4,
                        "cb4fd487538b0eff": 4, "477785c532483181": 8,
                        "c753072a5bf68171": 1, "6ba62bd34c05e0ff": 1,
                    },
                }),
                ("a", "mixed"): ({
                    "c": "ff275ab748f48780", "d": "345a2353ff8883f5",
                }, {
                    "c": {
                        "6a515ecf832aff78": 2, "e31255d5e81e2509": 2,
                        "4aa033e0505df8f1": 4, "73c55ff149852dee": 4,
                        "19d832b1f64387da": 2, "dbe56c4d43b264a2": 4,
                        "cb4fd487538b0eff": 4, "477785c532483181": 12,
                        "7a7743ce53fe8f77": 12, "067a3b42540bb240": 1,
                    },
                    "d": {
                        "6a515ecf832aff78": 8, "e31255d5e81e2509": 8,
                        "19d832b1f64387da": 2, "4975135dd6af0fc0": 4,
                        "dbe56c4d43b264a2": 4, "824f64bb4a05a043": 4,
                        "cb4fd487538b0eff": 4, "477785c532483181": 8,
                        "07c011183de4549a": 1,
                    },
                }),
                ("tau", "square-xi"): ({
                    "c": "1c20140f6e4a7549", "d": "43a8347e92f7f81d",
                }, {
                    "c": {
                        "6a515ecf832aff78": 2, "e31255d5e81e2509": 2,
                        "4aa033e0505df8f1": 4, "73c55ff149852dee": 4,
                        "dbe56c4d43b264a2": 4, "cb4fd487538b0eff": 4,
                        "477785c532483181": 12, "7a7743ce53fe8f77": 12,
                        "3abdced663de96c0": 1, "4c11afeb6140b7c8": 1,
                        "681ae7138c057bce": 1,
                    },
                    "d": {
                        "6a515ecf832aff78": 8, "e31255d5e81e2509": 8,
                        "19d832b1f64387da": 2, "9622b8845f94fd73": 1,
                        "4975135dd6af0fc0": 4, "dbe56c4d43b264a2": 4,
                        "824f64bb4a05a043": 4, "cb4fd487538b0eff": 4,
                        "477785c532483181": 8, "c7aea723bf6f84a1": 1,
                        "dbac8f34560fc4e3": 1,
                    },
                }),
                ("tau", "square-ell"): ({
                    "c": "4b4738172d468601", "d": "48395b300501d597",
                }, {
                    "c": {
                        "4aa033e0505df8f1": 4, "6a515ecf832aff78": 4,
                        "e31255d5e81e2509": 4, "73c55ff149852dee": 4,
                        "19d832b1f64387da": 2, "dbe56c4d43b264a2": 4,
                        "cb4fd487538b0eff": 4, "477785c532483181": 12,
                        "7a7743ce53fe8f77": 12, "90db6ed8f237340f": 1,
                        "39a8eb9fc1019be9": 1, "4805246499888132": 1,
                    },
                    "d": {
                        "4aa033e0505df8f1": 1, "6a515ecf832aff78": 8,
                        "e31255d5e81e2509": 8, "4975135dd6af0fc0": 2,
                        "dbe56c4d43b264a2": 4, "824f64bb4a05a043": 4,
                        "cb4fd487538b0eff": 4, "477785c532483181": 8,
                        "0274d6ca7d3e45b7": 1, "7d2994700e23736a": 1,
                    },
                }),
                ("tau", "mixed"): ({
                    "c": "610f5b1189c150ce", "d": "8173c0db21c9e654",
                }, {
                    "c": {
                        "6a515ecf832aff78": 2, "e31255d5e81e2509": 2,
                        "4aa033e0505df8f1": 4, "73c55ff149852dee": 4,
                        "19d832b1f64387da": 2, "dbe56c4d43b264a2": 4,
                        "cb4fd487538b0eff": 4, "477785c532483181": 12,
                        "7a7743ce53fe8f77": 12, "5db5e5fa2e141e59": 1,
                    },
                    "d": {
                        "6a515ecf832aff78": 8, "e31255d5e81e2509": 8,
                        "19d832b1f64387da": 2, "4975135dd6af0fc0": 4,
                        "dbe56c4d43b264a2": 4, "824f64bb4a05a043": 4,
                        "cb4fd487538b0eff": 4, "477785c532483181": 8,
                        "70ab1987477282b1": 1,
                    },
                }),
            }[proof_chart]
            require(
                digest(resultant) == expected_resultants[root_name],
                f"moving within digest {root_name}",
            )
            require(
                {digest(value): exponent for value, exponent in factors}
                == expected_factors[root_name],
                f"moving within factor census {root_name}",
            )
            selected = {
                ("a", "square-xi"): {
                    "c": {"fb37b983fcfb060a", "9396ced8aa4cfa67", "21ee8a55421c92a9"},
                    "d": {"9622b8845f94fd73", "c7aea723bf6f84a1", "dbac8f34560fc4e3"},
                },
                ("a", "square-ell"): {
                    "c": {"90db6ed8f237340f", "39a8eb9fc1019be9", "4805246499888132"},
                    "d": {"c753072a5bf68171", "6ba62bd34c05e0ff"},
                },
                ("a", "mixed"): {
                    "c": {"067a3b42540bb240"},
                    "d": {"07c011183de4549a"},
                },
                ("tau", "square-xi"): {
                    "c": {"3abdced663de96c0", "4c11afeb6140b7c8", "681ae7138c057bce"},
                    "d": {"9622b8845f94fd73", "c7aea723bf6f84a1", "dbac8f34560fc4e3"},
                },
                ("tau", "square-ell"): {
                    "c": {"90db6ed8f237340f", "39a8eb9fc1019be9", "4805246499888132"},
                    "d": {"0274d6ca7d3e45b7", "7d2994700e23736a"},
                },
                ("tau", "mixed"): {
                    "c": {"5db5e5fa2e141e59"},
                    "d": {"70ab1987477282b1"},
                },
            }[proof_chart][root_name]
            forbidden_parent = {
                ("a", "square-xi"): {
                    "c": (d - 1, d + 1, d - 2, 2*d - 1,
                          c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1, c + 1),
                    "d": (d - 1, d + 1, d, c - 2,
                          c*d - 1, 2*c - 1, 5*c*d - 4*c - 4*d + 5, c - 1),
                },
                ("a", "square-ell"): {
                    "c": (d - 2, d - 1, d + 1, 2*d - 1, d,
                          c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1, c + 1),
                    "d": (2*d - 1, d - 1, d + 1, 2*c - 1, c - 2,
                          c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1),
                },
                ("a", "mixed"): {
                    "c": (d - 1, d + 1, d - 2, 2*d - 1, d,
                          c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1, c + 1),
                    "d": (d - 1, d + 1, d, c - 2,
                          c*d - 1, 2*c - 1, 5*c*d - 4*c - 4*d + 5, c - 1),
                },
                ("tau", "square-xi"): {
                    "c": (d - 1, d + 1, d - 2, 2*d - 1,
                          c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1, c + 1),
                    "d": (d - 1, d + 1, d, c - 2,
                          c*d - 1, 2*c - 1, 5*c*d - 4*c - 4*d + 5, c - 1),
                },
                ("tau", "square-ell"): {
                    "c": (d - 2, d - 1, d + 1, 2*d - 1, d,
                          c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1, c + 1),
                    "d": (d - 2, d - 1, d + 1, c - 2, 2*c - 1,
                          c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1),
                },
                ("tau", "mixed"): {
                    "c": (d - 1, d + 1, d - 2, 2*d - 1, d,
                          c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1, c + 1),
                    "d": (d - 1, d + 1, d, c - 2,
                          c*d - 1, 2*c - 1, 5*c*d - 4*c - 4*d + 5, c - 1),
                },
            }[proof_chart][root_name]
            forbidden_digests = {
                digest(sp.Poly(value, c, d, domain=sp.QQ))
                for value in forbidden_parent
            }
            require(
                set(expected_factors[root_name]) == selected | forbidden_digests,
                f"moving parent forbidden binding {root_name}",
            )
        return factors

    if args.mode in ("c", "d"):
        within_components(args.mode)
        if args.prove:
            print(
                "KB_C2_112_NEAR_MOVING_TEMPLATE_"
                f"{proof_label}_"
                f"PARENT_{args.mode.upper()}_PRIMARY_PASS",
                flush=True,
            )
        return

    wanted_by_chart = {
        ("a", "square-xi"): {
            "c": (
                "fb37b983fcfb060a", "9396ced8aa4cfa67",
                "21ee8a55421c92a9",
            ),
            "d": (
                "9622b8845f94fd73", "c7aea723bf6f84a1",
                "dbac8f34560fc4e3",
            ),
        },
        ("a", "square-ell"): {
            "c": (
                "90db6ed8f237340f", "39a8eb9fc1019be9",
                "4805246499888132",
            ),
            "d": ("c753072a5bf68171", "6ba62bd34c05e0ff"),
        },
        ("a", "mixed"): {
            "c": ("067a3b42540bb240",),
            "d": ("07c011183de4549a",),
        },
        ("tau", "square-xi"): {
            "c": (
                "3abdced663de96c0", "4c11afeb6140b7c8",
                "681ae7138c057bce",
            ),
            "d": (
                "9622b8845f94fd73", "c7aea723bf6f84a1",
                "dbac8f34560fc4e3",
            ),
        },
        ("tau", "square-ell"): {
            "c": (
                "90db6ed8f237340f", "39a8eb9fc1019be9",
                "4805246499888132",
            ),
            "d": ("0274d6ca7d3e45b7", "7d2994700e23736a"),
        },
        ("tau", "mixed"): {
            "c": ("5db5e5fa2e141e59",),
            "d": ("70ab1987477282b1",),
        },
    }
    if (args.xi, args.allocation) not in wanted_by_chart:
        raise RuntimeError("pair modes are not configured for this chart")
    wanted = wanted_by_chart[(args.xi, args.allocation)]
    direct_classification = args.mode in ("classify-low", "classify-high")
    deployed_candidates = {}
    if direct_classification:
        ordered = sorted(expected_candidate_keys)
        selected = ordered[:10] if args.mode == "classify-low" else ordered[10:]
        deployed_candidates = {
            key: sp.Poly(
                sp.sympify(key, locals={"d": d}),
                d,
                modulus=characteristic,
            ).monic()
            for key in selected
        }
        components = {}
        pair_indices = []
    else:
        components = {}
        for root_name in ("c", "d"):
            by_digest = {
                digest(value): value for value, _ in within_components(root_name)
            }
            if not all(value in by_digest for value in wanted[root_name]):
                raise RuntimeError(f"moving component census drift for {root_name}")
            components[root_name] = [
                by_digest[value] for value in wanted[root_name]
            ]
        pair_indices = (
            [
                (left, right)
                for left in range(len(components["c"]))
                for right in range(len(components["d"]))
            ]
            if args.mode in ("pairs", "classify")
            else [(int(args.mode[-2]), int(args.mode[-1]))]
        )
    square_xi_pairs = {
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
    }
    square_ell_pairs = {
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
    }
    mixed_pairs = {
        (0, 0): ("70f26589e602e699", {
            "f93c38ef339888a3": 16,
            "b8907990ebf04ed3": 24,
            "3e8b7ae50a0eb368": 30,
            "badaaa15f719fc0a": 1,
            "7c38bfaa7ed117b9": 1,
            "ddc62481be50cdd9": 1,
            "c23e461afce62a1f": 1,
        }),
    }
    tau_square_xi_pairs = {
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
    }
    tau_square_ell_pairs = {
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
    }
    tau_mixed_pairs = {
        (0, 0): ("6c0e718979cba2e1", {
            "b8907990ebf04ed3": 16, "f93c38ef339888a3": 24,
            "3e8b7ae50a0eb368": 30, "badaaa15f719fc0a": 1,
            "db2acfdd67aea0a8": 1, "2ec31dcc2a54fbf4": 1,
            "249f7b73ad53d5ee": 1,
        }),
    }
    expected_pairs = {
        ("a", "square-xi"): square_xi_pairs,
        ("a", "square-ell"): square_ell_pairs,
        ("a", "mixed"): mixed_pairs,
        ("tau", "square-xi"): tau_square_xi_pairs,
        ("tau", "square-ell"): tau_square_ell_pairs,
        ("tau", "mixed"): tau_mixed_pairs,
    }.get(proof_chart, {})
    for left_index, right_index in pair_indices:
        left = components["c"][left_index]
        right = components["d"][right_index]
        projection = sp.Poly(
            sp.resultant(left.as_expr(), right.as_expr(), c),
            d,
            domain=sp.QQ,
        ).primitive()[1]
        factors = [
            (sp.Poly(value, d, domain=sp.QQ).primitive()[1], exponent)
            for value, exponent in sp.factor_list(projection.as_expr())[1]
        ]
        if args.prove:
            wanted_digest, wanted_factors = expected_pairs[
                (left_index, right_index)
            ]
            require(
                digest(projection) == wanted_digest,
                f"moving pair digest {left_index},{right_index}",
            )
            require(
                {digest(value): exponent for value, exponent in factors}
                == wanted_factors,
                f"moving pair factor census {left_index},{right_index}",
            )
        print(
            "stage=component_pair "
            f"pair={left_index},{right_index} degree={projection.degree()} "
            f"terms={len(projection.terms())} digest={digest(projection)} "
            f"factors={[(value.degree(), exponent, digest(value), str(value.as_expr()) if value.degree() <= 12 else None) for value, exponent in factors]}",
            flush=True,
        )
        _, integral = projection.clear_denoms(convert=True)
        modular_factors = sp.factor_list(
            integral.as_expr(), modulus=2130706433
        )[1]
        print(
            "stage=component_pair_modular "
            f"pair={left_index},{right_index} "
            f"factors={[(sp.Poly(value, d, modulus=2130706433).degree(), exponent, str(sp.Poly(value, d, modulus=2130706433).as_expr()) if sp.Poly(value, d, modulus=2130706433).degree() <= 6 else None) for value, exponent in modular_factors]}",
            flush=True,
        )
        standard = {
            str(sp.Poly(value, d, modulus=2130706433).monic().as_expr())
            for value in (d - 2, d - 1, d + 1, 2*d - 1)
        }
        for value, _ in modular_factors:
            polynomial = sp.Poly(value, d, modulus=2130706433).monic()
            key = str(polynomial.as_expr())
            if polynomial.degree() and 6 % polynomial.degree() == 0 \
                    and key not in standard:
                deployed_candidates[key] = polynomial

    if args.mode == "pairs" and args.prove:
        require(
            set(deployed_candidates) == expected_candidate_keys,
            "moving deployed candidate coverage",
        )
        print(
            "KB_C2_112_NEAR_MOVING_TEMPLATE_"
            f"{proof_label}_PAIRS_PRIMARY_PASS "
            f"characteristic=2130706433 candidates={len(deployed_candidates)}",
            flush=True,
        )
    if args.mode not in ("classify", "classify-low", "classify-high"):
        return
    saturation = sp.symbols("saturation")
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
    for key, candidate in sorted(deployed_candidates.items()):
        basis = sp.groebner(
            [*integral_traces, candidate.as_expr()],
            s,
            c,
            d,
            order="lex",
            modulus=characteristic,
        )
        unit = len(basis.polys) == 1 and basis.polys[0].as_expr() == 1
        remainder_zero = unit or basis.reduce(forbidden)[1] == 0
        saturated_unit = remainder_zero
        if not saturated_unit:
            saturated = sp.groebner(
                [
                    *(value.as_expr() for value in basis.polys),
                    saturation * forbidden - 1,
                ],
                saturation,
                s,
                c,
                d,
                order="lex",
                modulus=characteristic,
            )
            saturated_unit = (
                len(saturated.polys) == 1
                and saturated.polys[0].as_expr() == 1
            )
        records = [
            (
                tuple(value.degree(variable) for variable in (s, c, d)),
                len(value.terms()),
                digest(value),
            )
            for value in basis.polys
        ]
        print(
            "stage=candidate_classification "
            f"candidate={key!r} degree={candidate.degree()} "
            f"basis={records} unit={unit} "
            f"forbidden_remainder_zero={remainder_zero} "
            f"forbidden_saturation_unit={saturated_unit}",
            flush=True,
        )
        if args.prove:
            require(
                saturated_unit,
                f"admissible moving candidate survives: {key}",
            )
    if args.prove:
        expected_shard = sorted(expected_candidate_keys)
        if proof_chart in {("a", "square-xi"), ("tau", "square-xi")}:
            expected_shard = (
                expected_shard[:10]
                if args.mode == "classify-low"
                else expected_shard[10:]
            )
        require(
            set(deployed_candidates) == set(expected_shard),
            "moving deployed candidate shard coverage",
        )
        print(
            "KB_C2_112_NEAR_MOVING_TEMPLATE_"
            f"{proof_label}_"
            f"{args.mode.replace('-', '_').upper()}_PRIMARY_PASS "
            f"characteristic=2130706433 candidates={len(deployed_candidates)}",
            flush=True,
        )


if __name__ == "__main__":
    main()
