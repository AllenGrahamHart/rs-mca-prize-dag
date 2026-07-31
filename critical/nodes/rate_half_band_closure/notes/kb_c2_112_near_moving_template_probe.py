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
    if args.prove:
        require(
            (args.xi, args.allocation) == ("a", "square-xi")
            and args.mode in {
                "cores", "trace", "c", "d", "pairs",
                "classify-low", "classify-high",
            },
            "proof mode is pinned to a/square-xi certificate stages",
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
            ("c", "product"): ((4, 8, 6), 299, 2, "5b27d4da822910b2"),
            ("c", "sum"): ((4, 12, 8), 567, 0, "f5399a196459bb4f"),
            ("d", "product"): ((4, 6, 8), 284, 2, "72568ee71be7f479"),
            ("d", "sum"): ((4, 10, 9), 532, 0, "48c4bf1306aae34b"),
        }
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
                "KB_C2_112_NEAR_MOVING_TEMPLATE_A_SQUARE_SOURCE_PRIMARY_PASS",
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
            ("c", "product"): ((2, 8, 6), 181, "736a52293558c61d"),
            ("c", "sum"): ((2, 12, 8), 342, "3164f186a76328f5"),
            ("d", "product"): ((2, 6, 8), 172, "f0bba9bf4f23b8d2"),
            ("d", "sum"): ((2, 10, 9), 321, "2414ff4e8cdee299"),
        }
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
                "KB_C2_112_NEAR_MOVING_TEMPLATE_A_SQUARE_TRACE_PRIMARY_PASS",
                flush=True,
            )
        return

    characteristic = 2130706433
    expected_candidate_keys = {
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
    }

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
            expected_resultants = {
                "c": "830a8747ce80372c",
                "d": "43a8347e92f7f81d",
            }
            expected_factors = {
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
            }
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
                "c": {
                    "fb37b983fcfb060a", "9396ced8aa4cfa67",
                    "21ee8a55421c92a9",
                },
                "d": {
                    "9622b8845f94fd73", "c7aea723bf6f84a1",
                    "dbac8f34560fc4e3",
                },
            }[root_name]
            forbidden_parent = {
                "c": (d - 1, d + 1, d - 2, 2*d - 1,
                      c*d - 1, 5*c*d - 4*c - 4*d + 5, c - 1, c + 1),
                "d": (d - 1, d + 1, d, c - 2,
                      c*d - 1, 2*c - 1, 5*c*d - 4*c - 4*d + 5, c - 1),
            }[root_name]
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
                "KB_C2_112_NEAR_MOVING_TEMPLATE_A_SQUARE_"
                f"PARENT_{args.mode.upper()}_PRIMARY_PASS",
                flush=True,
            )
        return

    if (args.xi, args.allocation) != ("a", "square-xi"):
        raise RuntimeError("pair modes are pinned only for a/square-xi")
    wanted = {
        "c": ("fb37b983fcfb060a", "9396ced8aa4cfa67", "21ee8a55421c92a9"),
        "d": ("9622b8845f94fd73", "c7aea723bf6f84a1", "dbac8f34560fc4e3"),
    }
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
            [(left, right) for left in range(3) for right in range(3)]
            if args.mode in ("pairs", "classify")
            else [(int(args.mode[-2]), int(args.mode[-1]))]
        )
    expected_pairs = {
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
            "KB_C2_112_NEAR_MOVING_TEMPLATE_A_SQUARE_PAIRS_PRIMARY_PASS "
            "characteristic=2130706433 candidates=15",
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
            "KB_C2_112_NEAR_MOVING_TEMPLATE_A_SQUARE_"
            f"{args.mode.replace('-', '_').upper()}_PRIMARY_PASS "
            f"characteristic=2130706433 candidates={len(deployed_candidates)}",
            flush=True,
        )


if __name__ == "__main__":
    main()
