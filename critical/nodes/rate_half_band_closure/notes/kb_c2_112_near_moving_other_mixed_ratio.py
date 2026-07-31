#!/usr/bin/env python3
"""Bounded eliminations on the mixed other-xi ratio-gate branches."""

from __future__ import annotations

import argparse
from functools import reduce
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


def load_sparse(path: Path, section: str, variables, primary):
    payload = json.loads(path.read_text())
    terms = {
        tuple(monomial): sp.Rational(coefficient)
        for monomial, coefficient in payload["polynomials"][section]
    }
    value = sp.Poly.from_dict(terms, variables, domain=sp.QQ)
    if primary.digest(value) != payload["digests"][section]:
        raise RuntimeError("cache digest")
    return value


def records(polynomial: sp.Poly, variables, primary):
    return [
        (
            tuple(value.degree(variable) for variable in variables),
            len(value.terms()), exponent, primary.digest(value),
        )
        for factor, exponent in sp.factor_list(polynomial.as_expr())[1]
        for value in [
            sp.Poly(factor, *variables, domain=sp.QQ).primitive()[1]
        ]
    ]


def modular_records(polynomial: sp.Poly, variable):
    _, integral = polynomial.clear_denoms(convert=True)
    records_out = []
    for factor, exponent in sp.factor_list(
        integral.as_expr(), modulus=2130706433
    )[1]:
        value = sp.Poly(factor, variable, modulus=2130706433).monic()
        records_out.append((
            value.degree(), exponent,
            str(value.as_expr()) if value.degree() <= 6 else None,
        ))
    return records_out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode",
        choices=(
            "inspect", "linear0", "linear1",
            "linear0-common", "linear1-common",
            "quadratic", "quadratic-sextic",
            "quartic-trace-field-cache",
            "quartic-trace-product-field-cache",
            "quartic-trace-field-det-cache",
            "quartic-trace-field-compat-cache",
            "quartic-trace-field-equations-cache",
            "quartic-trace-product-system-cache",
            "quartic-trace-product-equations-cache",
            "quartic-trace-product-reduce-cache",
            "quartic-boundary-linear-cache",
            "quartic-boundary-equations-cache",
        ),
    )
    parser.add_argument("--cache-dir", type=Path, default=Path("/tmp"))
    parser.add_argument("--root", choices=("c", "d"), default="c")
    parser.add_argument("--product-root", choices=("c", "d"))
    args = parser.parse_args()
    primary = load_primary()
    b, c, d = sp.symbols("b c d")
    ratio_path = args.cache_dir / "kb_c2_112_other_mixed_ratio_gates.json"
    ratio_cores = {
        sign: load_sparse(ratio_path, sign, (b, c, d), primary)
        for sign in ("-1", "1")
    }
    factors = [
        sp.Poly(factor, b, c, d, domain=sp.QQ).primitive()[1]
        for factor, _ in sp.factor_list(ratio_cores["-1"].as_expr())[1]
    ]
    admissible = [value for value in factors if value.degree(b) > 0]
    admissible.append(ratio_cores["1"])
    admissible.sort(key=primary.digest)
    if args.mode == "inspect":
        print(
            "stage=branches records="
            f"{[(primary.digest(value), tuple(value.degree(x) for x in (b,c,d)), len(value.terms())) for value in admissible]}",
            flush=True,
        )
        return

    if args.mode == "quartic-boundary-linear-cache":
        branches = [value for value in admissible if value.degree(b) == 4]
        if len(branches) != 1:
            raise RuntimeError("quartic boundary branch census")
        branch_in_b = sp.Poly(branches[0].as_expr(), b)
        q3 = sp.Poly(branch_in_b.nth(3), c, d, domain=sp.QQ)
        q2 = sp.Poly(branch_in_b.nth(2), c, d, domain=sp.QQ)
        quadratic = sp.Poly(
            q3.as_expr() * b**2 + q2.as_expr() * b + q3.as_expr(),
            b, c, d, domain=sp.QQ,
        )
        relations = {}
        for root in ("c", "d"):
            relations[root] = {}
            for kind in ("product", "sum"):
                source = load_sparse(
                    args.cache_dir
                    / f"kb_c2_112_other_mixed_{root}_cores.json",
                    kind, (b, c, d), primary,
                )
                remainder = sp.Poly(
                    sp.prem(source.as_expr(), quadratic.as_expr(), b),
                    b, c, d, domain=sp.QQ,
                ).primitive()[1]
                in_b = sp.Poly(remainder.as_expr(), b)
                coefficients = [
                    sp.Poly(in_b.nth(power), c, d, domain=sp.QQ)
                    for power in (0, 1)
                ]
                content = reduce(sp.gcd, coefficients).primitive()[1]
                coefficients = [
                    value.exquo(content).primitive()[1]
                    for value in coefficients
                ]
                relations[root][kind] = coefficients
                print(
                    f"stage=quartic_boundary_linear root={root} kind={kind} "
                    f"content=({content.degree(c)},{content.degree(d)},{len(content.terms())},{primary.digest(content)}) "
                    f"records={[(value.degree(c), value.degree(d), len(value.terms()), primary.digest(value)) for value in coefficients]}",
                    flush=True,
                )
        path = (
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_boundary_linear.json"
        )
        path.write_text(json.dumps({
            "allocation": "mixed",
            "relations": {
                root: {
                    kind: [
                        {
                            "digest": primary.digest(value),
                            "terms": [
                                [list(monomial), str(coefficient)]
                                for monomial, coefficient in value.terms()
                            ],
                        }
                        for value in coefficients
                    ]
                    for kind, coefficients in by_kind.items()
                }
                for root, by_kind in relations.items()
            },
        }, sort_keys=True))
        print(
            f"stage=quartic_boundary_linear_cache path={path} "
            f"bytes={path.stat().st_size}",
            flush=True,
        )
        return

    if args.mode == "quartic-boundary-equations-cache":
        branches = [value for value in admissible if value.degree(b) == 4]
        if len(branches) != 1:
            raise RuntimeError("quartic boundary equation branch census")
        branch_in_b = sp.Poly(branches[0].as_expr(), b)
        q = sp.Poly(branch_in_b.nth(4), c, d, domain=sp.QQ)
        q3 = sp.Poly(branch_in_b.nth(3), c, d, domain=sp.QQ)
        q2 = sp.Poly(branch_in_b.nth(2), c, d, domain=sp.QQ)
        payload = json.loads((
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_boundary_linear.json"
        ).read_text())

        def load_record(record):
            value = sp.Poly.from_dict(
                {
                    tuple(monomial): sp.Rational(coefficient)
                    for monomial, coefficient in record["terms"]
                },
                (c, d), domain=sp.QQ,
            )
            if primary.digest(value) != record["digest"]:
                raise RuntimeError("quartic boundary linear digest")
            return value

        relations = {
            root: {
                kind: [load_record(record) for record in records_in]
                for kind, records_in in by_kind.items()
            }
            for root, by_kind in payload["relations"].items()
        }
        equations = {"q": q, "q3": q3, "q2": q2}
        for root in ("c", "d"):
            product_z, product_a = relations[root]["product"]
            sum_z, sum_a = relations[root]["sum"]
            equations[f"det_{root}"] = (
                product_a * sum_z - product_z * sum_a
            ).primitive()[1]
            equations[f"compat_{root}"] = (
                q3 * product_z * product_z
                - q2 * product_a * product_z
                + q3 * product_a * product_a
            ).primitive()[1]
        print(
            f"stage=quartic_boundary_equations records="
            f"{[(name, value.degree(c), value.degree(d), len(value.terms()), primary.digest(value)) for name, value in equations.items()]}",
            flush=True,
        )
        path = (
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_boundary_equations.json"
        )
        path.write_text(json.dumps({
            "allocation": "mixed",
            "equations": {
                name: {
                    "digest": primary.digest(value),
                    "terms": [
                        [list(monomial), str(coefficient)]
                        for monomial, coefficient in value.terms()
                    ],
                }
                for name, value in equations.items()
            },
        }, sort_keys=True))
        print(
            f"stage=quartic_boundary_equations_cache path={path} "
            f"bytes={path.stat().st_size}",
            flush=True,
        )
        return

    if args.mode == "quartic-trace-product-system-cache":
        system_root = args.root
        product_root = args.product_root or system_root
        suffix = (
            "" if (system_root, product_root) == ("c", "c")
            else "_d" if (system_root, product_root) == ("d", "d")
            else f"_{system_root}_{product_root}"
        )
        branches = [value for value in admissible if value.degree(b) == 4]
        if len(branches) != 1:
            raise RuntimeError("quartic product-system branch census")
        in_b = sp.Poly(branches[0].as_expr(), b)
        q2 = sp.Poly(in_b.nth(2), c, d, domain=sp.QQ)
        q3 = sp.Poly(in_b.nth(3), c, d, domain=sp.QQ)
        q = sp.Poly(in_b.nth(4), c, d, domain=sp.QQ).primitive()[1]
        if q != sp.Poly(in_b.nth(4), c, d, domain=sp.QQ):
            raise RuntimeError("quartic product-system normalization")

        def scaled_relation(path, root):
            payload = json.loads(path.read_text())
            if payload["allocation"] != "mixed":
                raise RuntimeError("quartic relation cache scope")
            numerators = []
            denominators = []
            for part in ("coefficient", "constant"):
                for power in ("0", "1"):
                    record = payload["remainders"][root][part][power]
                    numerators.append(sp.Poly.from_dict(
                        {
                            tuple(monomial): sp.Rational(coefficient)
                            for monomial, coefficient
                            in record["numerator"]
                        },
                        (c, d), domain=sp.QQ,
                    ))
                    denominators.append(sp.Poly.from_dict(
                        {
                            tuple(monomial): sp.Rational(coefficient)
                            for monomial, coefficient
                            in record["denominator"]
                        },
                        (c, d), domain=sp.QQ,
                    ))
            content = reduce(sp.gcd, numerators).primitive()[1]
            numerators = [value.exquo(content) for value in numerators]
            if denominators[0] != denominators[1]:
                raise RuntimeError("quartic relation A denominator")
            if denominators[2] != denominators[3]:
                raise RuntimeError("quartic relation Z denominator")
            scale_a = denominators[0].exquo(q**3)
            scale_z = denominators[2].exquo(q**2)
            if scale_a.total_degree() != 0 or scale_z.total_degree() != 0:
                raise RuntimeError("quartic relation denominator power")
            a0, a1, z0, z1 = numerators
            a0 = a0.mul_ground(scale_z.LC())
            a1 = a1.mul_ground(scale_z.LC())
            z0 = z0.mul_ground(scale_a.LC()) * q
            z1 = z1.mul_ground(scale_a.LC()) * q
            return (a0, a1, z0, z1), content

        sum_relation, sum_content = scaled_relation(
            args.cache_dir / "kb_c2_112_other_mixed_quartic_trace.json",
            system_root,
        )
        product_relation, product_content = scaled_relation(
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_product_trace.json",
            product_root,
        )
        sa0, sa1, sz0, sz1 = sum_relation
        pa0, pa1, pz0, pz1 = product_relation
        determinant_2 = sa1 * pz1 - sz1 * pa1
        determinant_1 = (
            sa1 * pz0 + sa0 * pz1 - sz1 * pa0 - sz0 * pa1
        )
        determinant_0 = sa0 * pz0 - sz0 * pa0
        det_a = q * determinant_1 - q3 * determinant_2
        det_z = q * determinant_0 - (q2 - 2 * q) * determinant_2
        print(
            f"stage=quartic_product_determinant records="
            f"{[(value.degree(c), value.degree(d), len(value.terms()), primary.digest(value)) for value in (det_a, det_z)]}",
            flush=True,
        )
        az1 = pa1 * pz0 + pa0 * pz1
        com_a = (
            -q3 * q * pz1 * pz1 + 2 * q**2 * pz1 * pz0
            + pa1 * pz1 * (q3**2 - (q2 - 2 * q) * q)
            - az1 * q3 * q + pa0 * pz0 * q**2
            - q3 * q * pa1 * pa1 + 2 * q**2 * pa1 * pa0
        )
        com_z = (
            -(q2 - 2 * q) * q * pz1 * pz1 + q**2 * pz0 * pz0
            + pa1 * pz1 * q3 * (q2 - 2 * q)
            - az1 * (q2 - 2 * q) * q
            - (q2 - 2 * q) * q * pa1 * pa1 + q**2 * pa0 * pa0
        )
        print(
            f"stage=quartic_product_compatibility records="
            f"{[(value.degree(c), value.degree(d), len(value.terms()), primary.digest(value)) for value in (com_a, com_z)]}",
            flush=True,
        )
        component_path = (
            args.cache_dir
            / f"kb_c2_112_other_mixed_quartic_product{suffix}_system.json"
        )
        component_path.write_text(json.dumps({
            "allocation": "mixed",
            "components": {
                name: {
                    "digest": primary.digest(value),
                    "terms": [
                        [list(monomial), str(coefficient)]
                        for monomial, coefficient in value.terms()
                    ],
                }
                for name, value in (
                    ("det_a", det_a), ("det_z", det_z),
                    ("com_a", com_a), ("com_z", com_z),
                )
            },
            "contents": [
                {
                    "digest": primary.digest(value),
                    "terms": [
                        [list(monomial), str(coefficient)]
                        for monomial, coefficient in value.terms()
                    ],
                }
                for value in (sum_content, product_content)
            ],
        }, sort_keys=True))
        print(
            f"stage=quartic_product_system_cache path={component_path} "
            f"bytes={component_path.stat().st_size}",
            flush=True,
        )
        return

    if args.mode == "quartic-trace-product-equations-cache":
        product_root = args.product_root or args.root
        suffix = (
            "" if (args.root, product_root) == ("c", "c")
            else "_d" if (args.root, product_root) == ("d", "d")
            else f"_{args.root}_{product_root}"
        )
        branches = [value for value in admissible if value.degree(b) == 4]
        if len(branches) != 1:
            raise RuntimeError("quartic product-equations branch census")
        in_b = sp.Poly(branches[0].as_expr(), b)
        q2 = sp.Poly(in_b.nth(2), c, d, domain=sp.QQ)
        q3 = sp.Poly(in_b.nth(3), c, d, domain=sp.QQ)
        q = sp.Poly(in_b.nth(4), c, d, domain=sp.QQ).primitive()[1]
        component_path = (
            args.cache_dir
            / f"kb_c2_112_other_mixed_quartic_product{suffix}_system.json"
        )
        component_payload = json.loads(component_path.read_text())
        if component_payload["allocation"] != "mixed":
            raise RuntimeError("quartic product-system cache scope")

        def load_component(name):
            record = component_payload["components"][name]
            value = sp.Poly.from_dict(
                {
                    tuple(monomial): sp.Rational(coefficient)
                    for monomial, coefficient in record["terms"]
                },
                (c, d), domain=sp.QQ,
            )
            if primary.digest(value) != record["digest"]:
                raise RuntimeError("quartic product-system cache digest")
            return value

        det_a, det_z, com_a, com_z = [
            load_component(name)
            for name in ("det_a", "det_z", "com_a", "com_z")
        ]
        print("stage=quartic_product_system_load", flush=True)
        cross = (det_a * com_z - det_z * com_a).primitive()[1]
        print("stage=quartic_product_cross", flush=True)
        trace_compatibility = (
            q * det_z * det_z - q3 * det_a * det_z
            + (q2 - 2 * q) * det_a * det_a
        ).primitive()[1]
        print("stage=quartic_product_trace_compatibility", flush=True)
        raw_path = (
            args.cache_dir
            / f"kb_c2_112_other_mixed_quartic_product{suffix}_raw_equations.json"
        )
        raw_path.write_text(json.dumps({
            "allocation": "mixed",
            "equations": [
                {
                    "digest": primary.digest(value),
                    "terms": [
                        [list(monomial), str(coefficient)]
                        for monomial, coefficient in value.terms()
                    ],
                }
                for value in (cross, trace_compatibility)
            ],
        }, sort_keys=True))
        print(
            f"stage=quartic_product_raw_equations_cache path={raw_path} "
            f"bytes={raw_path.stat().st_size}",
            flush=True,
        )
        return

    if args.mode == "quartic-trace-product-reduce-cache":
        product_root = args.product_root or args.root
        suffix = (
            "" if (args.root, product_root) == ("c", "c")
            else "_d" if (args.root, product_root) == ("d", "d")
            else f"_{args.root}_{product_root}"
        )
        raw_path = (
            args.cache_dir
            / f"kb_c2_112_other_mixed_quartic_product{suffix}_raw_equations.json"
        )
        raw_payload = json.loads(raw_path.read_text())
        if raw_payload["allocation"] != "mixed":
            raise RuntimeError("quartic product raw-equation scope")
        raw_equations = []
        for record in raw_payload["equations"]:
            value = sp.Poly.from_dict(
                {
                    tuple(monomial): sp.Rational(coefficient)
                    for monomial, coefficient in record["terms"]
                },
                (c, d), domain=sp.QQ,
            )
            if primary.digest(value) != record["digest"]:
                raise RuntimeError("quartic product raw-equation digest")
            raw_equations.append(value)
        cross, trace_compatibility = raw_equations
        print("stage=quartic_product_raw_equations_load", flush=True)
        common = sp.gcd(cross, trace_compatibility).primitive()[1]
        equations = [
            cross.exquo(common).primitive()[1],
            trace_compatibility.exquo(common).primitive()[1],
        ]
        print(
            f"stage=quartic_product_system common=({common.degree(c)},{common.degree(d)},{len(common.terms())},{primary.digest(common)}) "
            f"common_factors={records(common, (c,d), primary)} "
            f"equations={[(value.degree(c), value.degree(d), len(value.terms()), primary.digest(value)) for value in equations]}",
            flush=True,
        )
        equation_path = (
            args.cache_dir
            / f"kb_c2_112_other_mixed_quartic_product{suffix}_equations.json"
        )
        equation_path.write_text(json.dumps({
            "allocation": "mixed",
            "equations": [
                {
                    "digest": primary.digest(value),
                    "terms": [
                        [list(monomial), str(coefficient)]
                        for monomial, coefficient in value.terms()
                    ],
                }
                for value in equations
            ],
        }, sort_keys=True))
        print(
            f"stage=quartic_product_equations_cache path={equation_path} "
            f"bytes={equation_path.stat().st_size}",
            flush=True,
        )
        return

    if args.mode == "quartic-trace-field-projection":
        equation_path = (
            args.cache_dir
            / "kb_c2_112_other_mixed_quartic_equations.json"
        )
        payload = json.loads(equation_path.read_text())
        if payload["allocation"] != "mixed":
            raise RuntimeError("quartic equation cache scope")
        equations = []
        for record in payload["equations"]:
            value = sp.Poly.from_dict(
                {
                    tuple(monomial): sp.Rational(coefficient)
                    for monomial, coefficient in record["terms"]
                },
                (c, d), domain=sp.QQ,
            )
            if primary.digest(value) != record["digest"]:
                raise RuntimeError("quartic equation cache digest")
            equations.append(value)
        print("stage=quartic_cached_equations_load", flush=True)
        sequence = sp.subresultants(
            equations[0].as_expr(), equations[1].as_expr(), c
        )
        terminal = sp.Poly(sequence[-1], c, d, domain=sp.QQ)
        if terminal.degree(c) != 0:
            raise RuntimeError("quartic cached projection retains c")
        projection = sp.Poly(
            terminal.as_expr(), d, domain=sp.QQ
        ).primitive()[1]
        print(
            f"stage=quartic_cached_projection degree={projection.degree()} "
            f"terms={len(projection.terms())} digest={primary.digest(projection)} "
            f"factors={records(projection, (d,), primary)}",
            flush=True,
        )
        print(
            f"stage=quartic_cached_modular factors={modular_records(projection, d)}",
            flush=True,
        )
        return

    if args.mode in ("quadratic", "quadratic-sextic"):
        branch = [
            value for value in admissible if value.degree(b) == 2
        ]
        if len(branch) != 1:
            raise RuntimeError("quadratic branch census")
        branch = branch[0]
        remainders = []
        for root in ("c", "d"):
            source = load_sparse(
                args.cache_dir / f"kb_c2_112_other_mixed_{root}_cores.json",
                "sum", (b, c, d), primary,
            )
            raw = sp.Poly(
                sp.prem(source.as_expr(), branch.as_expr(), b),
                b, c, d, domain=sp.QQ,
            ).primitive()[1]
            raw_in_b = sp.Poly(raw.as_expr(), b)
            coefficient = sp.Poly(raw_in_b.nth(1), c, d, domain=sp.QQ)
            constant = sp.Poly(raw_in_b.nth(0), c, d, domain=sp.QQ)
            content = sp.gcd(coefficient, constant).primitive()[1]
            coefficient = coefficient.exquo(content).primitive()[1]
            constant = constant.exquo(content).primitive()[1]
            remainders.append((coefficient, constant))
            print(
                f"stage=quadratic_remainder root={root} branch={primary.digest(branch)} "
                f"raw_degrees={tuple(raw.degree(x) for x in (b,c,d))} "
                f"raw_terms={len(raw.terms())} content={primary.digest(content)} "
                f"content_factors={records(content, (c,d), primary)} "
                f"a=({coefficient.degree(c)},{coefficient.degree(d)},{len(coefficient.terms())},{primary.digest(coefficient)}) "
                f"z=({constant.degree(c)},{constant.degree(d)},{len(constant.terms())},{primary.digest(constant)})",
                flush=True,
            )
        (left_a, left_z), (right_a, right_z) = remainders
        determinant = sp.Poly(
            left_a.as_expr() * right_z.as_expr()
            - left_z.as_expr() * right_a.as_expr(),
            c, d, domain=sp.QQ,
        ).primitive()[1]
        branch_b = sp.Poly(branch.as_expr(), b)
        q2 = sp.Poly(branch_b.nth(2), c, d, domain=sp.QQ)
        q1 = sp.Poly(branch_b.nth(1), c, d, domain=sp.QQ)
        q0 = sp.Poly(branch_b.nth(0), c, d, domain=sp.QQ)
        compatibility = sp.Poly(
            q2.as_expr() * left_z.as_expr()**2
            - q1.as_expr() * left_a.as_expr() * left_z.as_expr()
            + q0.as_expr() * left_a.as_expr()**2,
            c, d, domain=sp.QQ,
        ).primitive()[1]
        common = sp.gcd(determinant, compatibility).primitive()[1]
        print(
            f"stage=quadratic_system det=({determinant.degree(c)},{determinant.degree(d)},{len(determinant.terms())},{primary.digest(determinant)}) "
            f"compat=({compatibility.degree(c)},{compatibility.degree(d)},{len(compatibility.terms())},{primary.digest(compatibility)}) "
            f"common=({common.degree(c)},{common.degree(d)},{len(common.terms())},{primary.digest(common)}) "
            f"common_factors={records(common, (c,d), primary)}",
            flush=True,
        )
        reduced = [
            determinant.exquo(common).primitive()[1],
            compatibility.exquo(common).primitive()[1],
        ]
        if args.mode == "quadratic-sextic":
            candidate = sp.Poly(
                d**6 + 1050209485*d**5 + 485933422*d**4
                - 170239540*d**3 + 890733766*d**2
                + 922536397*d + 640345259,
                d, modulus=2130706433,
            ).monic()
            basis = sp.groebner(
                [
                    *(value.as_expr() for value in reduced),
                    candidate.as_expr(),
                ],
                c, d, order="lex", modulus=2130706433,
            )
            forbidden = (
                c * d
                * (c - 2) * (2*c - 1) * (c - 1) * (c + 1)
                * (d - 2) * (2*d - 1) * (d - 1) * (d + 1)
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
                    inverse, c, d, order="lex", modulus=2130706433,
                )
                saturated_unit = (
                    len(saturated.polys) == 1
                    and saturated.polys[0].as_expr() == 1
                )
            print(
                f"stage=quadratic_sextic basis={[(tuple(value.degree(x) for x in (c,d)), len(value.terms()), primary.digest(value)) for value in basis.polys]} "
                f"unit={unit} forbidden_remainder_zero={remainder_zero} "
                f"forbidden_saturation_unit={saturated_unit}",
                flush=True,
            )
            if not saturated_unit:
                raise RuntimeError("quadratic sextic survives")
            return
        sequence = sp.subresultants(
            reduced[0].as_expr(), reduced[1].as_expr(), c
        )
        terminal = sp.Poly(sequence[-1], c, d, domain=sp.QQ)
        if terminal.degree(c) != 0:
            raise RuntimeError("quadratic subresultant retains c")
        projection = sp.Poly(
            terminal.as_expr(), d, domain=sp.QQ
        ).primitive()[1]
        print(
            f"stage=quadratic_projection degree={projection.degree()} "
            f"terms={len(projection.terms())} digest={primary.digest(projection)} "
            f"factors={records(projection, (d,), primary)}",
            flush=True,
        )
        print(
            f"stage=quadratic_modular factors={modular_records(projection, d)}",
            flush=True,
        )
        return

    if args.mode in (
        "quartic-trace-field-system",
        "quartic-trace-field-det-cache",
        "quartic-trace-field-compat-cache",
        "quartic-trace-field-equations-cache",
        "quartic-trace-field-final",
    ):
        branches = [
            value for value in admissible if value.degree(b) == 4
        ]
        if len(branches) != 1:
            raise RuntimeError("quartic cached-trace branch census")
        branch = branches[0]
        trace_variable = sp.symbols("s")
        in_b = sp.Poly(branch.as_expr(), b)
        q2 = sp.Poly(in_b.nth(2), c, d, domain=sp.QQ)
        q3 = sp.Poly(in_b.nth(3), c, d, domain=sp.QQ)
        q4 = sp.Poly(in_b.nth(4), c, d, domain=sp.QQ)
        coefficient_field = sp.QQ.frac_field(c, d)
        trace = sp.Poly(
            q4.as_expr() * (trace_variable**2 - 2)
            + q3.as_expr() * trace_variable + q2.as_expr(),
            trace_variable, domain=coefficient_field,
        ).monic()
        payload = json.loads(
            (args.cache_dir / "kb_c2_112_other_mixed_quartic_trace.json").read_text()
        )
        if payload["allocation"] != "mixed" or payload["branch"] != primary.digest(branch):
            raise RuntimeError("quartic trace cache scope")
        coefficient_ring = coefficient_field.get_ring()

        def load_fraction(record):
            numerator = coefficient_ring.dtype(
                {
                    tuple(monomial): sp.QQ.convert(sp.Rational(coefficient))
                    for monomial, coefficient in record["numerator"]
                }
            )
            denominator = coefficient_ring.dtype(
                {
                    tuple(monomial): sp.QQ.convert(sp.Rational(coefficient))
                    for monomial, coefficient in record["denominator"]
                }
            )
            return coefficient_field.dtype(numerator, denominator)

        sum_remainders = []
        reduced_numerators = {}
        cached_denominators = {}
        for root in ("c", "d"):
            pair = []
            numerator_polys = []
            denominator_polys = []
            for part in ("coefficient", "constant"):
                record = payload["remainders"][root][part]
                numerator_polys.extend(
                    sp.Poly.from_dict(
                        {
                            tuple(monomial): sp.Rational(coefficient)
                            for monomial, coefficient
                            in record[str(power)]["numerator"]
                        },
                        (c, d), domain=sp.QQ,
                    ).primitive()[1]
                    for power in (0, 1)
                )
                denominator_polys.extend(
                    sp.Poly.from_dict(
                        {
                            tuple(monomial): sp.Rational(coefficient)
                            for monomial, coefficient
                            in record[str(power)]["denominator"]
                        },
                        (c, d), domain=sp.QQ,
                    )
                    for power in (0, 1)
                )
                pair.append(sp.Poly.from_dict(
                    {
                        (power,): load_fraction(record[str(power)])
                        for power in (0, 1)
                    },
                    (trace_variable,), domain=coefficient_field,
                )
                )
            common_content = reduce(sp.gcd, numerator_polys).primitive()[1]
            reduced_numerators[root] = [
                value.exquo(common_content) for value in numerator_polys
            ]
            if denominator_polys[0] != denominator_polys[1]:
                raise RuntimeError("quartic coefficient denominator mismatch")
            if denominator_polys[2] != denominator_polys[3]:
                raise RuntimeError("quartic constant denominator mismatch")
            cached_denominators[root] = (
                denominator_polys[0], denominator_polys[2]
            )
            common_field = coefficient_field.convert(common_content.as_expr())
            pair = [value.mul_ground(1 / common_field) for value in pair]
            print(
                f"stage=quartic_field_content root={root} "
                f"degrees=({common_content.degree(c)},{common_content.degree(d)}) "
                f"terms={len(common_content.terms())} "
                f"digest={primary.digest(common_content)} "
                f"factors={records(common_content, (c,d), primary)}",
                flush=True,
            )
            sum_remainders.append(tuple(pair))
        print("stage=quartic_field_system_load", flush=True)
        (left_a, left_z), (right_a, right_z) = sum_remainders

        def field_element_record(value):
            value = coefficient_field.convert(value)
            return {
                "numerator": [
                    [list(monomial), str(coefficient)]
                    for monomial, coefficient in value.numer.items()
                ],
                "denominator": [
                    [list(monomial), str(coefficient)]
                    for monomial, coefficient in value.denom.items()
                ],
            }

        def field_poly_record(value):
            coefficients = value.rep.to_dict()
            return {
                str(power): field_element_record(
                    coefficients.get((power,), coefficient_field.zero)
                )
                for power in (0, 1)
            }

        if args.mode in (
            "quartic-trace-field-equations-cache",
            "quartic-trace-field-final",
        ):
            system_payload = json.loads(
                (args.cache_dir / "kb_c2_112_other_mixed_quartic_system.json").read_text()
            )
            determinant = sp.Poly.from_dict(
                {
                    (power,): load_fraction(
                        system_payload["determinant"][str(power)]
                    )
                    for power in (0, 1)
                },
                (trace_variable,), domain=coefficient_field,
            )
            compatibility = sp.Poly.from_dict(
                {
                    (power,): load_fraction(
                        system_payload["compatibility"][str(power)]
                    )
                    for power in (0, 1)
                },
                (trace_variable,), domain=coefficient_field,
            )
            print("stage=quartic_field_system_checkpoints", flush=True)
        else:
            determinant = None
            compatibility = None
            if args.mode in (
                "quartic-trace-field-system",
                "quartic-trace-field-det-cache",
            ):
                determinant = (
                    left_a * right_z - left_z * right_a
                ).rem(trace)
                print("stage=quartic_field_determinant", flush=True)
            if args.mode in (
                "quartic-trace-field-system",
                "quartic-trace-field-compat-cache",
            ):
                a0, a1, z0, z1 = reduced_numerators["d"]
                denominator_a, denominator_z = cached_denominators["d"]
                q = q4.primitive()[1]
                scale_a = denominator_a.exquo(q**3)
                scale_z = denominator_z.exquo(q**2)
                if scale_a.total_degree() != 0 or scale_z.total_degree() != 0:
                    raise RuntimeError("quartic denominator power census")
                print("stage=quartic_compat_scales", flush=True)
                a0 = a0.mul_ground(scale_z.LC())
                a1 = a1.mul_ground(scale_z.LC())
                z0 = z0.mul_ground(scale_a.LC()) * q
                z1 = z1.mul_ground(scale_a.LC()) * q
                r1 = q3
                r0 = q2 - 2 * q
                az1 = a1 * z0 + a0 * z1
                print("stage=quartic_compat_az", flush=True)
                compatibility_a = (
                    -r1 * q * z1 * z1 + 2 * q**2 * z1 * z0
                    + a1 * z1 * (r1**2 - r0 * q)
                    - az1 * r1 * q + a0 * z0 * q**2
                    - r1 * q * a1 * a1 + 2 * q**2 * a1 * a0
                )
                print("stage=quartic_compat_a", flush=True)
                compatibility_z = (
                    -r0 * q * z1 * z1 + q**2 * z0 * z0
                    + a1 * z1 * r1 * r0 - az1 * r0 * q
                    - r0 * q * a1 * a1 + q**2 * a0 * a0
                )
                print("stage=quartic_compat_z", flush=True)

                def polynomial_field_element(value):
                    numerator = coefficient_ring.dtype(
                        {
                            monomial: sp.QQ.convert(coefficient)
                            for monomial, coefficient in value.terms()
                        }
                    )
                    return coefficient_field.dtype(
                        numerator, coefficient_ring.one
                    )

                compatibility = sp.Poly.from_dict(
                    {
                        (1,): polynomial_field_element(compatibility_a),
                        (0,): polynomial_field_element(compatibility_z),
                    },
                    (trace_variable,), domain=coefficient_field,
                )
                print("stage=quartic_field_compatibility", flush=True)
            if args.mode.endswith("-cache"):
                system_path = (
                    args.cache_dir
                    / "kb_c2_112_other_mixed_quartic_system.json"
                )
                system_payload = (
                    json.loads(system_path.read_text())
                    if system_path.exists() else {}
                )
                key = (
                    "determinant"
                    if determinant is not None else "compatibility"
                )
                value = determinant if determinant is not None else compatibility
                system_payload[key] = field_poly_record(value)
                system_path.write_text(json.dumps(system_payload, sort_keys=True))
                print(
                    f"stage=quartic_field_system_cache key={key} "
                    f"path={system_path} bytes={system_path.stat().st_size}",
                    flush=True,
                )
                return
        if determinant.degree() > 1 or compatibility.degree() > 1:
            raise RuntimeError("quartic cached trace reduction degree")
        if args.mode in (
            "quartic-trace-field-equations-cache",
            "quartic-trace-field-final",
        ):
            def cached_numerator(record):
                return sp.Poly.from_dict(
                    {
                        tuple(monomial): sp.Rational(coefficient)
                        for monomial, coefficient in record["numerator"]
                    },
                    (c, d), domain=sp.QQ,
                )

            determinant_records = system_payload["determinant"]
            compatibility_records = system_payload["compatibility"]
            if (
                determinant_records["0"]["denominator"]
                != determinant_records["1"]["denominator"]
            ):
                raise RuntimeError("quartic determinant denominator mismatch")
            if any(
                record["denominator"] != [[[0, 0], "1"]]
                for record in compatibility_records.values()
            ):
                raise RuntimeError("quartic compatibility denominator")
            det_z = cached_numerator(determinant_records["0"])
            det_a = cached_numerator(determinant_records["1"])
            com_z = cached_numerator(compatibility_records["0"])
            com_a = cached_numerator(compatibility_records["1"])
            q = q4.primitive()[1]
            if q != q4:
                raise RuntimeError("quartic trace leading normalization")
            determinant_denominator = sp.Poly.from_dict(
                {
                    tuple(monomial): sp.Rational(coefficient)
                    for monomial, coefficient
                    in determinant_records["0"]["denominator"]
                },
                (c, d), domain=sp.QQ,
            )
            if determinant_denominator.exquo(q**3).total_degree() != 0:
                raise RuntimeError("quartic determinant denominator power")
            cross_poly = (
                det_a * com_z - det_z * com_a
            ).primitive()[1]
            print("stage=quartic_cached_cross", flush=True)
            compatibility_poly = (
                q * det_z * det_z
                - q3 * det_a * det_z
                + (q2 - 2 * q) * det_a * det_a
            ).primitive()[1]
            print("stage=quartic_cached_trace_compatibility", flush=True)
        else:
            det_a = determinant.nth(1)
            det_z = determinant.nth(0)
            com_a = compatibility.nth(1)
            com_z = compatibility.nth(0)
            cross = det_a * com_z - det_z * com_a
            t1 = trace.nth(1)
            t0 = trace.nth(0)
            trace_compatibility = (
                det_z * det_z - t1 * det_a * det_z
                + t0 * det_a * det_a
            )

            def clear_cached_field(value, name):
                expression = coefficient_field.to_sympy(value)
                numerator, denominator = sp.fraction(sp.cancel(expression))
                numerator_poly = sp.Poly(
                    numerator, c, d, domain=sp.QQ
                ).primitive()[1]
                denominator_poly = sp.Poly(
                    denominator, c, d, domain=sp.QQ
                ).primitive()[1]
                print(
                    f"stage=quartic_cached_clear name={name} "
                    f"numerator=({numerator_poly.degree(c)},{numerator_poly.degree(d)},{len(numerator_poly.terms())},{primary.digest(numerator_poly)}) "
                    f"denominator=({denominator_poly.degree(c)},{denominator_poly.degree(d)},{len(denominator_poly.terms())},{primary.digest(denominator_poly)}) "
                    f"denominator_factors={records(denominator_poly, (c,d), primary)}",
                    flush=True,
                )
                return numerator_poly

            cross_poly = clear_cached_field(cross, "cross")
            compatibility_poly = clear_cached_field(
                trace_compatibility, "compatibility"
            )
        common = sp.gcd(cross_poly, compatibility_poly).primitive()[1]
        print(
            f"stage=quartic_cached_system common=({common.degree(c)},{common.degree(d)},{len(common.terms())},{primary.digest(common)}) "
            f"common_factors={records(common, (c,d), primary)} "
            f"small_factor_expressions={[str(factor) for factor, _ in sp.factor_list(common.as_expr())[1] if len(sp.Poly(factor, c, d, domain=sp.QQ).terms()) <= 6]}",
            flush=True,
        )
        reduced_system = [
            cross_poly.exquo(common).primitive()[1],
            compatibility_poly.exquo(common).primitive()[1],
        ]
        if args.mode == "quartic-trace-field-equations-cache":
            equation_path = (
                args.cache_dir
                / "kb_c2_112_other_mixed_quartic_equations.json"
            )
            equation_payload = {
                "allocation": "mixed",
                "equations": [
                    {
                        "digest": primary.digest(value),
                        "terms": [
                            [list(monomial), str(coefficient)]
                            for monomial, coefficient in value.terms()
                        ],
                    }
                    for value in reduced_system
                ],
            }
            equation_path.write_text(
                json.dumps(equation_payload, sort_keys=True)
            )
            print(
                f"stage=quartic_cached_equations path={equation_path} "
                f"bytes={equation_path.stat().st_size} "
                f"records={[(value.degree(c), value.degree(d), len(value.terms()), primary.digest(value)) for value in reduced_system]}",
                flush=True,
            )
            return
        sequence = sp.subresultants(
            reduced_system[0].as_expr(), reduced_system[1].as_expr(), c
        )
        terminal = sp.Poly(sequence[-1], c, d, domain=sp.QQ)
        if terminal.degree(c) != 0:
            raise RuntimeError("quartic cached trace system retains c")
        projection = sp.Poly(
            terminal.as_expr(), d, domain=sp.QQ
        ).primitive()[1]
        print(
            f"stage=quartic_cached_projection degree={projection.degree()} "
            f"terms={len(projection.terms())} digest={primary.digest(projection)} "
            f"factors={records(projection, (d,), primary)}",
            flush=True,
        )
        print(
            f"stage=quartic_cached_modular factors={modular_records(projection, d)}",
            flush=True,
        )
        return

    if args.mode in (
        "quartic-trace-field", "quartic-trace-field-cache",
        "quartic-trace-product-field-cache",
    ):
        branches = [
            value for value in admissible if value.degree(b) == 4
        ]
        if len(branches) != 1:
            raise RuntimeError("quartic field-trace branch census")
        branch = branches[0]
        trace_variable = sp.symbols("s")
        in_b = sp.Poly(branch.as_expr(), b)
        q0 = sp.Poly(in_b.nth(0), c, d, domain=sp.QQ)
        q1 = sp.Poly(in_b.nth(1), c, d, domain=sp.QQ)
        q2 = sp.Poly(in_b.nth(2), c, d, domain=sp.QQ)
        q3 = sp.Poly(in_b.nth(3), c, d, domain=sp.QQ)
        q4 = sp.Poly(in_b.nth(4), c, d, domain=sp.QQ)
        if q0 != q4 or q1 != q3:
            raise RuntimeError("quartic field trace reciprocity")
        trace_expression = (
            q4.as_expr() * (trace_variable**2 - 2)
            + q3.as_expr() * trace_variable + q2.as_expr()
        )
        coefficient_field = sp.QQ.frac_field(c, d)
        trace = sp.Poly(
            trace_expression, trace_variable, domain=coefficient_field
        ).monic()
        powers_a = [sp.Integer(0), sp.Integer(1)]
        powers_z = [sp.Integer(1), sp.Integer(0)]
        for _ in range(2, 6):
            powers_a.append(
                sp.expand(trace_variable * powers_a[-1] - powers_a[-2])
            )
            powers_z.append(
                sp.expand(trace_variable * powers_z[-1] - powers_z[-2])
            )
        sum_remainders = []
        source_kind = (
            "product"
            if args.mode == "quartic-trace-product-field-cache" else "sum"
        )
        for root in ("c", "d"):
            source = load_sparse(
                args.cache_dir / f"kb_c2_112_other_mixed_{root}_cores.json",
                source_kind, (b, c, d), primary,
            )
            source_in_b = sp.Poly(source.as_expr(), b)
            coefficient_expression = sum(
                source_in_b.nth(index) * powers_a[index]
                for index in range(source.degree(b) + 1)
            )
            constant_expression = sum(
                source_in_b.nth(index) * powers_z[index]
                for index in range(source.degree(b) + 1)
            )
            coefficient = sp.Poly(
                coefficient_expression, trace_variable,
                domain=coefficient_field,
            ).rem(trace)
            constant = sp.Poly(
                constant_expression, trace_variable,
                domain=coefficient_field,
            ).rem(trace)
            sum_remainders.append((coefficient, constant))
            print(
                f"stage=quartic_field_sum root={root} "
                f"a_degree={coefficient.degree()} z_degree={constant.degree()}",
                flush=True,
            )
        if args.mode in (
            "quartic-trace-field-cache",
            "quartic-trace-product-field-cache",
        ):
            def fraction_record(value):
                expression = coefficient_field.to_sympy(value)
                numerator, denominator = sp.fraction(sp.cancel(expression))
                numerator_poly = sp.Poly(
                    numerator, c, d, domain=sp.QQ
                ).primitive()[1]
                denominator_poly = sp.Poly(
                    denominator, c, d, domain=sp.QQ
                ).primitive()[1]
                return {
                    "numerator": [
                        [list(monomial), str(coefficient)]
                        for monomial, coefficient in numerator_poly.terms()
                    ],
                    "denominator": [
                        [list(monomial), str(coefficient)]
                        for monomial, coefficient in denominator_poly.terms()
                    ],
                }

            payload = {
                "allocation": "mixed",
                "kind": source_kind,
                "branch": primary.digest(branch),
                "remainders": {
                    root: {
                        part: {
                            str(power): fraction_record(value.nth(power))
                            for power in (0, 1)
                        }
                        for part, value in zip(
                            ("coefficient", "constant"), pair
                        )
                    }
                    for root, pair in zip(("c", "d"), sum_remainders)
                },
            }
            cache = args.cache_dir / (
                "kb_c2_112_other_mixed_quartic_product_trace.json"
                if source_kind == "product"
                else "kb_c2_112_other_mixed_quartic_trace.json"
            )
            cache.write_text(json.dumps(payload, sort_keys=True))
            print(
                f"stage=quartic_field_cache path={cache} "
                f"bytes={cache.stat().st_size}",
                flush=True,
            )
            return
        (left_a, left_z), (right_a, right_z) = sum_remainders
        determinant = (left_a * right_z - left_z * right_a).rem(trace)
        compatibility = (
            left_z * left_z
            + sp.Poly(trace_variable, trace_variable, domain=coefficient_field)
            * left_a * left_z
            + left_a * left_a
        ).rem(trace)
        if determinant.degree() > 1 or compatibility.degree() > 1:
            raise RuntimeError("quartic field trace reduction degree")
        det_a = determinant.nth(1)
        det_z = determinant.nth(0)
        com_a = compatibility.nth(1)
        com_z = compatibility.nth(0)
        cross = det_a * com_z - det_z * com_a
        t1 = trace.nth(1)
        t0 = trace.nth(0)
        trace_compatibility = (
            det_z * det_z - t1 * det_a * det_z + t0 * det_a * det_a
        )

        def clear_field(value, name):
            expression = coefficient_field.to_sympy(value)
            numerator, denominator = sp.fraction(sp.cancel(expression))
            numerator_poly = sp.Poly(
                numerator, c, d, domain=sp.QQ
            ).primitive()[1]
            denominator_poly = sp.Poly(
                denominator, c, d, domain=sp.QQ
            ).primitive()[1]
            print(
                f"stage=quartic_field_clear name={name} "
                f"numerator=({numerator_poly.degree(c)},{numerator_poly.degree(d)},{len(numerator_poly.terms())},{primary.digest(numerator_poly)}) "
                f"denominator=({denominator_poly.degree(c)},{denominator_poly.degree(d)},{len(denominator_poly.terms())},{primary.digest(denominator_poly)}) "
                f"denominator_factors={records(denominator_poly, (c,d), primary)}",
                flush=True,
            )
            return numerator_poly

        cross_poly = clear_field(cross, "cross")
        compatibility_poly = clear_field(
            trace_compatibility, "compatibility"
        )
        common = sp.gcd(cross_poly, compatibility_poly).primitive()[1]
        print(
            f"stage=quartic_field_system common=({common.degree(c)},{common.degree(d)},{len(common.terms())},{primary.digest(common)}) "
            f"common_factors={records(common, (c,d), primary)}",
            flush=True,
        )
        reduced_system = [
            cross_poly.exquo(common).primitive()[1],
            compatibility_poly.exquo(common).primitive()[1],
        ]
        sequence = sp.subresultants(
            reduced_system[0].as_expr(), reduced_system[1].as_expr(), c
        )
        terminal = sp.Poly(sequence[-1], c, d, domain=sp.QQ)
        if terminal.degree(c) != 0:
            raise RuntimeError("quartic field trace system retains c")
        projection = sp.Poly(
            terminal.as_expr(), d, domain=sp.QQ
        ).primitive()[1]
        print(
            f"stage=quartic_field_projection degree={projection.degree()} "
            f"terms={len(projection.terms())} digest={primary.digest(projection)} "
            f"factors={records(projection, (d,), primary)}",
            flush=True,
        )
        print(
            f"stage=quartic_field_modular factors={modular_records(projection, d)}",
            flush=True,
        )
        return

    if args.mode == "quartic-trace":
        branches = [
            value for value in admissible if value.degree(b) == 4
        ]
        if len(branches) != 1:
            raise RuntimeError("quartic trace branch census")
        branch = branches[0]
        trace_variable = sp.symbols("s")
        in_b = sp.Poly(branch.as_expr(), b)
        q0 = sp.Poly(in_b.nth(0), c, d, domain=sp.QQ)
        q1 = sp.Poly(in_b.nth(1), c, d, domain=sp.QQ)
        q2 = sp.Poly(in_b.nth(2), c, d, domain=sp.QQ)
        q3 = sp.Poly(in_b.nth(3), c, d, domain=sp.QQ)
        q4 = sp.Poly(in_b.nth(4), c, d, domain=sp.QQ)
        if q0 != q4 or q1 != q3:
            raise RuntimeError("quartic branch is not reciprocal")
        trace = sp.Poly(
            q4.as_expr() * (trace_variable**2 - 2)
            + q3.as_expr() * trace_variable + q2.as_expr(),
            trace_variable, c, d, domain=sp.QQ,
        ).primitive()[1]
        lifted = sp.Poly(
            sp.together(
                b**2 * trace.as_expr().subs(
                    trace_variable, b + 1 / b
                )
            ),
            b, c, d, domain=sp.QQ,
        ).primitive()[1]
        if lifted.monic() != branch.monic():
            raise RuntimeError("quartic trace lift")
        print(
            f"stage=quartic_trace degrees={tuple(trace.degree(x) for x in (trace_variable,c,d))} "
            f"terms={len(trace.terms())} digest={primary.digest(trace)}",
            flush=True,
        )

        powers_a = [sp.Integer(0), sp.Integer(1)]
        powers_z = [sp.Integer(1), sp.Integer(0)]
        for _ in range(2, 6):
            powers_a.append(
                sp.expand(trace_variable * powers_a[-1] - powers_a[-2])
            )
            powers_z.append(
                sp.expand(trace_variable * powers_z[-1] - powers_z[-2])
            )
        sum_remainders = []
        for root in ("c", "d"):
            source = load_sparse(
                args.cache_dir / f"kb_c2_112_other_mixed_{root}_cores.json",
                "sum", (b, c, d), primary,
            )
            source_in_b = sp.Poly(source.as_expr(), b)
            coefficient = sp.Poly(
                sum(
                    source_in_b.nth(index) * powers_a[index]
                    for index in range(source.degree(b) + 1)
                ),
                trace_variable, c, d, domain=sp.QQ,
            ).primitive()[1]
            constant = sp.Poly(
                sum(
                    source_in_b.nth(index) * powers_z[index]
                    for index in range(source.degree(b) + 1)
                ),
                trace_variable, c, d, domain=sp.QQ,
            ).primitive()[1]
            content = sp.gcd(coefficient, constant).primitive()[1]
            coefficient = coefficient.exquo(content).primitive()[1]
            constant = constant.exquo(content).primitive()[1]
            trace_reduced = []
            trace_contents = []
            for value in (coefficient, constant):
                raw_reduced = sp.Poly(
                    sp.prem(value.as_expr(), trace.as_expr(), trace_variable),
                    trace_variable, c, d, domain=sp.QQ,
                ).primitive()[1]
                in_trace = sp.Poly(raw_reduced.as_expr(), trace_variable)
                trace_coefficients = [
                    sp.Poly(item, c, d, domain=sp.QQ)
                    for item in in_trace.all_coeffs()
                ]
                trace_content = trace_coefficients[0]
                for item in trace_coefficients[1:]:
                    trace_content = sp.gcd(
                        trace_content, item
                    ).primitive()[1]
                reduced_expression = sum(
                    item.exquo(trace_content).as_expr()
                    * trace_variable ** (in_trace.degree() - index)
                    for index, item in enumerate(trace_coefficients)
                )
                reduced_value = sp.Poly(
                    reduced_expression, trace_variable, c, d, domain=sp.QQ
                ).primitive()[1]
                trace_reduced.append(reduced_value)
                trace_contents.append(trace_content)
            coefficient, constant = trace_reduced
            sum_remainders.append((coefficient, constant))
            print(
                f"stage=quartic_trace_sum root={root} "
                f"content={tuple(content.degree(x) for x in (trace_variable,c,d))},{len(content.terms())},{primary.digest(content)} "
                f"content_factors={records(content, (trace_variable,c,d), primary)} "
                f"trace_contents={[(value.degree(c), value.degree(d), len(value.terms()), primary.digest(value), records(value, (c,d), primary)) for value in trace_contents]} "
                f"a={tuple(coefficient.degree(x) for x in (trace_variable,c,d))},{len(coefficient.terms())},{primary.digest(coefficient)} "
                f"z={tuple(constant.degree(x) for x in (trace_variable,c,d))},{len(constant.terms())},{primary.digest(constant)}",
                flush=True,
            )
        (left_a, left_z), (right_a, right_z) = sum_remainders
        determinant = sp.Poly(
            left_a.as_expr() * right_z.as_expr()
            - left_z.as_expr() * right_a.as_expr(),
            trace_variable, c, d, domain=sp.QQ,
        ).primitive()[1]
        compatibility = sp.Poly(
            left_z.as_expr()**2
            + trace_variable * left_a.as_expr() * left_z.as_expr()
            + left_a.as_expr()**2,
            trace_variable, c, d, domain=sp.QQ,
        ).primitive()[1]
        reduced_trace = []
        for name, value in (
            ("determinant", determinant), ("compatibility", compatibility)
        ):
            raw = sp.Poly(
                sp.prem(value.as_expr(), trace.as_expr(), trace_variable),
                trace_variable, c, d, domain=sp.QQ,
            ).primitive()[1]
            raw_in_s = sp.Poly(raw.as_expr(), trace_variable)
            coefficients = [
                sp.Poly(item, c, d, domain=sp.QQ)
                for item in raw_in_s.all_coeffs()
            ]
            content = coefficients[0]
            for item in coefficients[1:]:
                content = sp.gcd(content, item).primitive()[1]
            expression = sum(
                item.exquo(content).as_expr()
                * trace_variable ** (raw_in_s.degree() - index)
                for index, item in enumerate(coefficients)
            )
            reduced = sp.Poly(
                expression, trace_variable, c, d, domain=sp.QQ
            ).primitive()[1]
            if reduced.degree(trace_variable) > 1:
                raise RuntimeError("quartic trace reduction degree")
            reduced_trace.append(reduced)
            print(
                f"stage=quartic_trace_reduce name={name} "
                f"raw={tuple(raw.degree(x) for x in (trace_variable,c,d))},{len(raw.terms())},{primary.digest(raw)} "
                f"content=({content.degree(c)},{content.degree(d)},{len(content.terms())},{primary.digest(content)}) "
                f"content_factors={records(content, (c,d), primary)} "
                f"reduced={tuple(reduced.degree(x) for x in (trace_variable,c,d))},{len(reduced.terms())},{primary.digest(reduced)}",
                flush=True,
            )
        first_in_s = sp.Poly(reduced_trace[0].as_expr(), trace_variable)
        second_in_s = sp.Poly(reduced_trace[1].as_expr(), trace_variable)
        first_a = sp.Poly(first_in_s.nth(1), c, d, domain=sp.QQ)
        first_z = sp.Poly(first_in_s.nth(0), c, d, domain=sp.QQ)
        second_a = sp.Poly(second_in_s.nth(1), c, d, domain=sp.QQ)
        second_z = sp.Poly(second_in_s.nth(0), c, d, domain=sp.QQ)
        cross = sp.Poly(
            first_a.as_expr() * second_z.as_expr()
            - first_z.as_expr() * second_a.as_expr(),
            c, d, domain=sp.QQ,
        ).primitive()[1]
        trace_in_s = sp.Poly(trace.as_expr(), trace_variable)
        t2 = sp.Poly(trace_in_s.nth(2), c, d, domain=sp.QQ)
        t1 = sp.Poly(trace_in_s.nth(1), c, d, domain=sp.QQ)
        t0 = sp.Poly(trace_in_s.nth(0), c, d, domain=sp.QQ)
        trace_compatibility = sp.Poly(
            t2.as_expr() * first_z.as_expr()**2
            - t1.as_expr() * first_a.as_expr() * first_z.as_expr()
            + t0.as_expr() * first_a.as_expr()**2,
            c, d, domain=sp.QQ,
        ).primitive()[1]
        common = sp.gcd(cross, trace_compatibility).primitive()[1]
        print(
            f"stage=quartic_trace_system cross=({cross.degree(c)},{cross.degree(d)},{len(cross.terms())},{primary.digest(cross)}) "
            f"compat=({trace_compatibility.degree(c)},{trace_compatibility.degree(d)},{len(trace_compatibility.terms())},{primary.digest(trace_compatibility)}) "
            f"common=({common.degree(c)},{common.degree(d)},{len(common.terms())},{primary.digest(common)}) "
            f"common_factors={records(common, (c,d), primary)}",
            flush=True,
        )
        reduced_system = [
            cross.exquo(common).primitive()[1],
            trace_compatibility.exquo(common).primitive()[1],
        ]
        sequence = sp.subresultants(
            reduced_system[0].as_expr(), reduced_system[1].as_expr(), c
        )
        terminal = sp.Poly(sequence[-1], c, d, domain=sp.QQ)
        if terminal.degree(c) != 0:
            raise RuntimeError("quartic trace system retains c")
        projection = sp.Poly(
            terminal.as_expr(), d, domain=sp.QQ
        ).primitive()[1]
        print(
            f"stage=quartic_trace_projection degree={projection.degree()} "
            f"terms={len(projection.terms())} digest={primary.digest(projection)} "
            f"factors={records(projection, (d,), primary)}",
            flush=True,
        )
        print(
            f"stage=quartic_trace_modular factors={modular_records(projection, d)}",
            flush=True,
        )
        return

    if args.mode in (
        "quartic-inspect", "quartic-product-inspect",
        "quartic-sum-parent", "quartic-sum-modparent"
    ):
        branch = [
            value for value in admissible if value.degree(b) == 4
        ]
        if len(branch) != 1:
            raise RuntimeError("quartic branch census")
        branch = branch[0]
        source_kind = (
            "product" if args.mode == "quartic-product-inspect" else "sum"
        )
        reduced_sums = []
        for root in ("c", "d"):
            source = load_sparse(
                args.cache_dir / f"kb_c2_112_other_mixed_{root}_cores.json",
                source_kind, (b, c, d), primary,
            )
            raw = sp.Poly(
                sp.prem(source.as_expr(), branch.as_expr(), b),
                b, c, d, domain=sp.QQ,
            ).primitive()[1]
            in_b = sp.Poly(raw.as_expr(), b)
            coefficients = [
                sp.Poly(value, c, d, domain=sp.QQ)
                for value in in_b.all_coeffs()
            ]
            content = coefficients[0]
            for value in coefficients[1:]:
                content = sp.gcd(content, value).primitive()[1]
            reduced_expression = sum(
                value.exquo(content).as_expr()
                * b ** (in_b.degree() - index)
                for index, value in enumerate(coefficients)
            )
            reduced = sp.Poly(
                reduced_expression, b, c, d, domain=sp.QQ
            ).primitive()[1]
            reduced_sums.append(reduced)
            print(
                f"stage=quartic_remainder kind={source_kind} root={root} "
                f"branch={primary.digest(branch)} "
                f"raw_degrees={tuple(raw.degree(x) for x in (b,c,d))} "
                f"raw_terms={len(raw.terms())} content={primary.digest(content)} "
                f"content_factors={records(content, (c,d), primary)} "
                f"reduced_degrees={tuple(reduced.degree(x) for x in (b,c,d))} "
                f"reduced_terms={len(reduced.terms())} "
                f"reduced_digest={primary.digest(reduced)}",
                flush=True,
            )
        if args.mode == "quartic-product-inspect":
            coefficient_field = sp.QQ.frac_field(c, d)
            left = sp.Poly(
                reduced_sums[0].as_expr(), b, domain=coefficient_field
            )
            right = sp.Poly(
                reduced_sums[1].as_expr(), b, domain=coefficient_field
            )
            common = sp.gcd(left, right).monic()
            print(
                f"stage=quartic_product_relation equal={left.monic() == right.monic()} "
                f"gcd_degree={common.degree()}",
                flush=True,
            )
        if args.mode == "quartic-sum-parent":
            sequence = sp.subresultants(
                reduced_sums[0].as_expr(), reduced_sums[1].as_expr(), b
            )
            terminal = sp.Poly(sequence[-1], b, c, d, domain=sp.QQ)
            if terminal.degree(b) != 0:
                raise RuntimeError("quartic sum parent retains b")
            parent = sp.Poly(
                terminal.as_expr(), c, d, domain=sp.QQ
            ).primitive()[1]
            print(
                f"stage=quartic_sum_parent degrees=({parent.degree(c)},{parent.degree(d)}) "
                f"terms={len(parent.terms())} digest={primary.digest(parent)}",
                flush=True,
            )
        if args.mode == "quartic-sum-modparent":
            coefficient_ring = sp.GF(2130706433).poly_ring(c, d)
            left = sp.Poly(
                reduced_sums[0].as_expr(), b, domain=coefficient_ring
            )
            right = sp.Poly(
                reduced_sums[1].as_expr(), b, domain=coefficient_ring
            )
            sequence = left.subresultants(right)
            terminal = sequence[-1]
            if terminal.degree() != 0:
                raise RuntimeError("quartic modular sum parent retains b")
            parent = sp.Poly(
                terminal.as_expr(), c, d, modulus=2130706433
            ).monic()
            print(
                f"stage=quartic_sum_modparent degrees=({parent.degree(c)},{parent.degree(d)}) "
                f"terms={len(parent.terms())} digest={primary.digest(parent)}",
                flush=True,
            )
        return

    linear = sorted(
        (value for value in admissible if value.degree(b) == 1),
        key=primary.digest,
    )[int(args.mode.removeprefix("linear")[0])]
    lead = sp.Poly(sp.diff(linear.as_expr(), b), c, d, domain=sp.QQ)
    constant = sp.Poly(linear.as_expr().subs(b, 0), c, d, domain=sp.QQ)
    b_value = sp.cancel(-constant.as_expr() / lead.as_expr())
    sums = []
    for root in ("c", "d"):
        source = load_sparse(
            args.cache_dir / f"kb_c2_112_other_mixed_{root}_cores.json",
            "sum", (b, c, d), primary,
        )
        numerator = sp.fraction(sp.cancel(source.as_expr().subs(b, b_value)))[0]
        value = sp.Poly(numerator, c, d, domain=sp.QQ).primitive()[1]
        sums.append(value)
        print(
            f"stage=substitute root={root} branch={primary.digest(linear)} "
            f"degrees=({value.degree(c)},{value.degree(d)}) "
            f"terms={len(value.terms())} digest={primary.digest(value)}",
            flush=True,
        )
    common = sp.gcd(*sums).primitive()[1]
    print(
        f"stage=common degrees=({common.degree(c)},{common.degree(d)}) "
        f"terms={len(common.terms())} digest={primary.digest(common)} "
        f"factors={records(common, (c, d), primary)}",
        flush=True,
    )
    if args.mode.endswith("-common"):
        standard = {
            "6a515ecf832aff78", "e31255d5e81e2509",
            "cb4fd487538b0eff", "477785c532483181",
        }
        components = [
            sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
            for factor, _ in sp.factor_list(common.as_expr())[1]
            if primary.digest(
                sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
            ) not in standard
        ]
        if len(components) != 1:
            raise RuntimeError("linear common-component census")
        component = components[0]
        product = load_sparse(
            args.cache_dir / "kb_c2_112_other_mixed_c_cores.json",
            "product", (b, c, d), primary,
        )
        numerator = sp.fraction(
            sp.cancel(product.as_expr().subs(b, b_value))
        )[0]
        substituted = sp.Poly(
            numerator, c, d, domain=sp.QQ
        ).primitive()[1]
        remainder = sp.Poly(
            sp.prem(substituted.as_expr(), component.as_expr(), c),
            c, d, domain=sp.QQ,
        ).primitive()[1]
        print(
            f"stage=common_product component={primary.digest(component)} "
            f"product_degrees=({substituted.degree(c)},{substituted.degree(d)}) "
            f"product_terms={len(substituted.terms())} "
            f"remainder_degrees=({remainder.degree(c)},{remainder.degree(d)}) "
            f"remainder_terms={len(remainder.terms())} "
            f"remainder_digest={primary.digest(remainder)}",
            flush=True,
        )
        sequence = sp.subresultants(
            component.as_expr(), remainder.as_expr(), c
        )
        terminal = sp.Poly(sequence[-1], c, d, domain=sp.QQ)
        if terminal.degree(c) != 0:
            raise RuntimeError("common-product subresultant retains c")
        projection = sp.Poly(
            terminal.as_expr(), d, domain=sp.QQ
        ).primitive()[1]
        print(
            f"stage=common_product_projection degree={projection.degree()} "
            f"terms={len(projection.terms())} digest={primary.digest(projection)} "
            f"factors={records(projection, (d,), primary)}",
            flush=True,
        )
        print(
            f"stage=common_product_modular factors={modular_records(projection, d)}",
            flush=True,
        )
        return
    reduced = [value.exquo(common).primitive()[1] for value in sums]
    for index, value in enumerate(reduced):
        print(
            f"stage=reduced index={index} degrees=({value.degree(c)},{value.degree(d)}) "
            f"terms={len(value.terms())} digest={primary.digest(value)}",
            flush=True,
        )
    sequence = sp.subresultants(
        reduced[0].as_expr(), reduced[1].as_expr(), c
    )
    terminal = sp.Poly(sequence[-1], c, d, domain=sp.QQ)
    if terminal.degree(c) != 0:
        raise RuntimeError("terminal subresultant retains c")
    projection = sp.Poly(
        terminal.as_expr(), d, domain=sp.QQ
    ).primitive()[1]
    print(
        f"stage=projection degree={projection.degree()} terms={len(projection.terms())} "
        f"digest={primary.digest(projection)} factors={records(projection, (d,), primary)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
