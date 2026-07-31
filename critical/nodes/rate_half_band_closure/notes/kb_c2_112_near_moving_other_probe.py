#!/usr/bin/env python3
"""Bounded direct-elimination probe for the moving-moving other-xi orbit."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
PRIMARY = HERE / "kb_c2_112_near_moving_template_probe.py"


def load_primary():
    spec = importlib.util.spec_from_file_location("moving_primary", PRIMARY)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load moving primary helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def factor_records(polynomial: sp.Poly, *variables):
    primary = load_primary()
    return [
        (
            tuple(value.degree(variable) for variable in variables),
            len(value.terms()),
            exponent,
            primary.digest(value),
        )
        for factor, exponent in sp.factor_list(polynomial.as_expr())[1]
        for value in [
            sp.Poly(factor, *variables, domain=sp.QQ).primitive()[1]
        ]
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("allocation", choices=("square-xi", "square-ell", "mixed"))
    parser.add_argument("--cache-dir", type=Path, default=Path("/tmp"))
    parser.add_argument(
        "mode",
        choices=(
            "cores", "symmetry", "parent-c", "parent-d",
            "subparent-c", "subparent-d", "modparent-c", "modparent-d",
            "cache-c", "cache-d",
            "traceparent-d",
            "mixed-gate", "cache-mixed-gate",
            "mixed-ratio-gate", "cache-mixed-ratio-gate",
            "mixed-ratio-sign",
        ),
    )
    args = parser.parse_args()
    primary = load_primary()

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
    first = primary.edge(a, b)
    second = primary.edge(a, 1 / b)
    target = sp.Matrix([
        sp.cancel(value)
        for value in (
            ((ell0 + ell1 / b) * first + (ell0 + b * ell1) * second)
            / (1 / b - b)
        )
    ])
    at_w = primary.evaluation(w)
    at_z = primary.evaluation(z)
    matrix = sp.Matrix.vstack(
        at_w[0] - q0 * at_w[2],
        at_w[1] - q1 * at_w[2],
        *at_z,
    )
    coefficients = [
        sp.cancel(value)
        for value in matrix.inv(method="DM") * sp.Matrix([0, 0, *target])
    ]

    residual_coefficients = {}

    def residual(root_name, root):
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
        residual_coefficients[root_name] = (even0, even2)
        return leading, middle, constant

    kappa_xi = 1 / b
    kappa_ell = 1 / d
    targets = {
        "square-xi": {
            "c": (kappa_xi, kappa_xi),
            "d": (kappa_ell, kappa_ell),
        },
        "square-ell": {
            "c": (kappa_ell, kappa_ell),
            "d": (kappa_xi, kappa_xi),
        },
        "mixed": {
            "c": (kappa_xi, kappa_ell),
            "d": (kappa_xi, kappa_ell),
        },
    }[args.allocation]
    incidence = sp.Poly(
        4*c**2*d - 2*c**2 - 3*c*d + 3*c + 2*d - 4,
        b, c, d, domain=sp.QQ,
    )
    cores = {}
    roots = (("c", c), ("d", d))
    if args.mode.endswith("-c"):
        roots = (("c", c),)
    elif args.mode.endswith("-d"):
        roots = (("d", d),)
    for root_name, root in roots:
        leading, middle, constant = residual(root_name, root)
        root_targets = targets[root_name]
        equations = {
            "product": constant - leading * root_targets[0] * root_targets[1],
            "sum": middle + leading * sum(root_targets),
        }
        for kind, expression in equations.items():
            value = primary.numerator_poly(expression, b, c, d)
            incidence_power = 0
            if kind == "product":
                while True:
                    quotient, remainder = value.div(incidence)
                    if not remainder.is_zero:
                        break
                    value = quotient.primitive()[1]
                    incidence_power += 1
            cores[(root_name, kind)] = value
            print(
                f"stage={root_name}_{kind} "
                f"degrees={tuple(value.degree(x) for x in (b,c,d))} "
                f"terms={len(value.terms())} incidence_power={incidence_power} "
                f"digest={primary.digest(value)}",
                flush=True,
            )
    if args.mode == "cores":
        return

    if args.mode == "mixed-ratio-sign":
        if args.allocation != "mixed":
            raise RuntimeError("ratio sign is mixed-only")
        even0_c, even2_c = residual_coefficients["c"]
        even0_d, even2_d = residual_coefficients["d"]
        ratio_product = sp.cancel(
            even0_c * even0_d / (even2_c * even2_d)
        )
        numerator, denominator = sp.fraction(ratio_product)
        numerator_poly = sp.Poly(
            numerator, b, c, d, domain=sp.QQ
        ).primitive()[1]
        denominator_poly = sp.Poly(
            denominator, b, c, d, domain=sp.QQ
        ).primitive()[1]
        print(
            f"stage=mixed_ratio_sign numerator_degrees="
            f"{tuple(numerator_poly.degree(x) for x in (b,c,d))} "
            f"numerator_terms={len(numerator_poly.terms())} "
            f"numerator_factors={[(str(factor), exponent) for factor, exponent in sp.factor_list(numerator_poly.as_expr())[1]]} "
            f"denominator_degrees={tuple(denominator_poly.degree(x) for x in (b,c,d))} "
            f"denominator_terms={len(denominator_poly.terms())} "
            f"denominator_factors={[(str(factor), exponent) for factor, exponent in sp.factor_list(denominator_poly.as_expr())[1]]}",
            flush=True,
        )
        return

    if args.mode in ("mixed-gate", "cache-mixed-gate"):
        if args.allocation != "mixed":
            raise RuntimeError("constant-leading gate is mixed-only")
        constant_c, leading_c = residual_coefficients["c"]
        constant_d, leading_d = residual_coefficients["d"]
        gates = {}
        for sign in (-1, 1):
            gate = primary.numerator_poly(
                c**2 * b * d * constant_c * constant_d
                + sign * leading_c * leading_d,
                b, c, d,
            )
            core = gate
            incidence_power = 0
            while True:
                quotient, remainder = core.div(incidence)
                if not remainder.is_zero:
                    break
                core = quotient.primitive()[1]
                incidence_power += 1
            if incidence_power != 2:
                raise RuntimeError("mixed gate incidence power")
            gates[str(sign)] = core
            print(
                f"stage=mixed_gate sign={sign:+d} "
                f"degrees={tuple(core.degree(x) for x in (b,c,d))} "
                f"terms={len(core.terms())} incidence_power={incidence_power} "
                f"digest={primary.digest(core)}",
                flush=True,
            )
        if args.mode == "cache-mixed-gate":
            args.cache_dir.mkdir(parents=True, exist_ok=True)
            cache = args.cache_dir / "kb_c2_112_other_mixed_gates.json"
            payload = {
                "allocation": "mixed",
                "polynomials": {
                    sign: [
                        [list(monomial), str(coefficient)]
                        for monomial, coefficient in value.terms()
                    ]
                    for sign, value in gates.items()
                },
                "digests": {
                    sign: primary.digest(value)
                    for sign, value in gates.items()
                },
            }
            cache.write_text(json.dumps(payload, sort_keys=True))
            print(
                f"stage=mixed_gate_cache path={cache} bytes={cache.stat().st_size} "
                f"digests={payload['digests']}",
                flush=True,
            )
        return

    if args.mode in ("mixed-ratio-gate", "cache-mixed-ratio-gate"):
        if args.allocation != "mixed":
            raise RuntimeError("ratio gate is mixed-only")
        constant_c, leading_c = residual_coefficients["c"]
        constant_d, leading_d = residual_coefficients["d"]
        ratios = {}
        for sign in (-1, 1):
            ratio = primary.numerator_poly(
                constant_c * leading_d + sign * constant_d * leading_c,
                b, c, d,
            )
            core = ratio
            incidence_power = 0
            while True:
                quotient, remainder = core.div(incidence)
                if not remainder.is_zero:
                    break
                core = quotient.primitive()[1]
                incidence_power += 1
            ratios[str(sign)] = core
            print(
                f"stage=mixed_ratio_gate sign={sign:+d} "
                f"degrees={tuple(core.degree(x) for x in (b,c,d))} "
                f"terms={len(core.terms())} incidence_power={incidence_power} "
                f"digest={primary.digest(core)} "
                f"factors={factor_records(core, b, c, d)}",
                flush=True,
            )
        if args.mode == "cache-mixed-ratio-gate":
            args.cache_dir.mkdir(parents=True, exist_ok=True)
            cache = args.cache_dir / "kb_c2_112_other_mixed_ratio_gates.json"
            payload = {
                "allocation": "mixed",
                "polynomials": {
                    sign: [
                        [list(monomial), str(coefficient)]
                        for monomial, coefficient in value.terms()
                    ]
                    for sign, value in ratios.items()
                },
                "digests": {
                    sign: primary.digest(value)
                    for sign, value in ratios.items()
                },
            }
            cache.write_text(json.dumps(payload, sort_keys=True))
            print(
                f"stage=mixed_ratio_gate_cache path={cache} "
                f"bytes={cache.stat().st_size} digests={payload['digests']}",
                flush=True,
            )
        return

    if args.mode.startswith("cache"):
        args.cache_dir.mkdir(parents=True, exist_ok=True)
        cache = args.cache_dir / (
            f"kb_c2_112_other_{args.allocation}_{args.mode[-1]}_cores.json"
        )
        payload = {
            "allocation": args.allocation,
            "root": args.mode[-1],
            "polynomials": {
                kind: [
                    [list(monomial), str(coefficient)]
                    for monomial, coefficient in cores[(args.mode[-1], kind)].terms()
                ]
                for kind in ("product", "sum")
            },
            "digests": {
                kind: primary.digest(cores[(args.mode[-1], kind)])
                for kind in ("product", "sum")
            },
        }
        cache.write_text(json.dumps(payload, sort_keys=True))
        print(
            f"stage=cache path={cache} bytes={cache.stat().st_size} "
            f"digests={payload['digests']}",
            flush=True,
        )
        return

    if args.mode == "traceparent-d":
        s = sp.symbols("s")
        traces = {}
        for kind in ("product", "sum"):
            trace, removed = primary.reciprocal_trace(
                cores[("d", kind)], b, c, d, s
            )
            if trace is None:
                raise RuntimeError(f"d trace failed: {removed}")
            traces[kind] = trace
            print(
                f"stage=d_trace kind={kind} "
                f"degrees={tuple(trace.degree(x) for x in (s,c,d))} "
                f"terms={len(trace.terms())} digest={primary.digest(trace)}",
                flush=True,
            )
        resultant = sp.Poly(
            sp.resultant(
                traces["product"].as_expr(), traces["sum"].as_expr(), s
            ),
            c, d, domain=sp.QQ,
        ).primitive()[1]
        print(
            f"stage=d_trace_parent degrees=({resultant.degree(c)},{resultant.degree(d)}) "
            f"terms={len(resultant.terms())} digest={primary.digest(resultant)} "
            f"factors={factor_records(resultant, c, d)}",
            flush=True,
        )
        return

    if args.mode == "symmetry":
        for key, value in cores.items():
            degree = value.degree(b)
            reciprocal = sp.Poly(
                sp.expand(b**degree * value.as_expr().subs(b, 1 / b)),
                b, c, d, domain=sp.QQ,
            ).primitive()[1]
            gcd = sp.gcd(value, reciprocal).primitive()[1]
            print(
                f"stage=symmetry key={key} reciprocal_digest={primary.digest(reciprocal)} "
                f"gcd_degrees={tuple(gcd.degree(x) for x in (b,c,d))} "
                f"gcd_terms={len(gcd.terms())} gcd_digest={primary.digest(gcd)}",
                flush=True,
            )
        return

    root_name = args.mode[-1]
    if args.mode.startswith("modparent"):
        characteristic = 2130706433
        left = sp.Poly(
            cores[(root_name, "product")].as_expr(),
            b, c, d, modulus=characteristic,
        )
        right = sp.Poly(
            cores[(root_name, "sum")].as_expr(),
            b, c, d, modulus=characteristic,
        )
        resultant = left.resultant(right)
        if not isinstance(resultant, sp.Poly):
            resultant = sp.Poly(resultant, c, d, modulus=characteristic)
        resultant = resultant.monic()
        print(
            f"stage=mod_parent root={root_name} "
            f"degrees=({resultant.degree(c)},{resultant.degree(d)}) "
            f"terms={len(resultant.terms())} digest={primary.digest(resultant)}",
            flush=True,
        )
        return
    if args.mode.startswith("subparent"):
        sequence = sp.subresultants(
            cores[(root_name, "product")].as_expr(),
            cores[(root_name, "sum")].as_expr(),
            b,
        )
        terminal = sp.Poly(sequence[-1], b, c, d, domain=sp.QQ)
        if terminal.degree(b) != 0:
            raise RuntimeError("terminal subresultant retains b")
        resultant = sp.Poly(
            terminal.as_expr(), c, d, domain=sp.QQ
        ).primitive()[1]
    else:
        resultant = sp.Poly(
            sp.resultant(
                cores[(root_name, "product")].as_expr(),
                cores[(root_name, "sum")].as_expr(),
                b,
            ),
            c, d, domain=sp.QQ,
        ).primitive()[1]
    print(
        f"stage=parent root={root_name} "
        f"degrees=({resultant.degree(c)},{resultant.degree(d)}) "
        f"terms={len(resultant.terms())} digest={primary.digest(resultant)}",
        flush=True,
    )
    print(
        f"stage=parent_factors root={root_name} "
        f"factors={factor_records(resultant, c, d)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
