#!/usr/bin/env python3
"""Project one digest-checked other-xi parent-component pair."""

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


def load_components(allocation, root, cache_dir, c, d, primary):
    path = cache_dir / f"kb_c2_112_other_{allocation}_{root}_components.json"
    payload = json.loads(path.read_text())
    if payload["allocation"] != allocation or payload["root"] != root:
        raise RuntimeError("component cache scope")
    values = []
    for record in payload["components"]:
        terms = {
            tuple(monomial): sp.Rational(coefficient)
            for monomial, coefficient in record["terms"]
        }
        value = sp.Poly.from_dict(terms, (c, d), domain=sp.QQ)
        if primary.digest(value) != record["digest"]:
            raise RuntimeError("component cache digest")
        values.append((record["digest"], value))
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("allocation", choices=("square-xi", "square-ell", "mixed"))
    parser.add_argument("left", type=int)
    parser.add_argument("right", type=int)
    parser.add_argument("--cache-dir", type=Path, default=Path("/tmp"))
    parser.add_argument("--prove", action="store_true")
    args = parser.parse_args()
    primary = load_primary()
    c, d = sp.symbols("c d")
    left_components = load_components(
        args.allocation, "c", args.cache_dir, c, d, primary
    )
    right_components = load_components(
        args.allocation, "d", args.cache_dir, c, d, primary
    )
    left_digest, left = left_components[args.left]
    right_digest, right = right_components[args.right]
    projection = sp.Poly(
        sp.resultant(left.as_expr(), right.as_expr(), c),
        d, domain=sp.QQ,
    ).primitive()[1]
    factors = []
    for factor, exponent in sp.factor_list(projection.as_expr())[1]:
        value = sp.Poly(factor, d, domain=sp.QQ).primitive()[1]
        factors.append((value.degree(), exponent, primary.digest(value)))
    if args.prove:
        expected = {
            (0, 0): ("45717df443835160", [
                (1, 1, "f93c38ef339888a3"),
                (1, 1, "bc3da4bcdb93303f"),
                (1, 1, "b8907990ebf04ed3"),
                (1, 2, "3e8b7ae50a0eb368"),
                (6, 1, "c85a04492dab7b12"),
            ]),
            (0, 1): ("f17eb57458420432", [
                (1, 1, "f93c38ef339888a3"),
                (1, 1, "b8907990ebf04ed3"),
                (1, 2, "bc3da4bcdb93303f"),
                (1, 5, "3e8b7ae50a0eb368"),
                (8, 1, "fad413c4877dd87b"),
            ]),
            (0, 2): ("fdc13f78c0f27fd7", [
                (1, 2, "f93c38ef339888a3"),
                (1, 2, "b8907990ebf04ed3"),
                (1, 7, "3e8b7ae50a0eb368"),
                (17, 1, "b46974c97473bd20"),
            ]),
            (1, 0): ("1db833f7ec218a23", [
                (1, 4, "bc3da4bcdb93303f"),
                (1, 8, "f93c38ef339888a3"),
                (1, 8, "b8907990ebf04ed3"),
                (1, 10, "3e8b7ae50a0eb368"),
                (20, 1, "20f33c7cf156b9e0"),
            ]),
            (1, 1): ("7b6dd06d29601e4b", [
                (1, 8, "f93c38ef339888a3"),
                (1, 8, "b8907990ebf04ed3"),
                (1, 10, "bc3da4bcdb93303f"),
                (1, 24, "3e8b7ae50a0eb368"),
                (28, 1, "2e7e4de29c38d633"),
            ]),
            (1, 2): ("0b010d8c5566cd18", [
                (1, 18, "f93c38ef339888a3"),
                (1, 18, "b8907990ebf04ed3"),
                (1, 34, "3e8b7ae50a0eb368"),
                (2, 2, "039d9aaf13f5aa0d"),
                (54, 1, "8b0c6fd4e82d7f57"),
            ]),
        }[(args.left, args.right)]
        if primary.digest(projection) != expected[0] or factors != expected[1]:
            raise RuntimeError("pair characteristic-zero census")
    print(
        f"stage=pair pair={args.left},{args.right} "
        f"components={left_digest},{right_digest} degree={projection.degree()} "
        f"terms={len(projection.terms())} digest={primary.digest(projection)} "
        f"factors={factors}",
        flush=True,
    )
    _, integral = projection.clear_denoms(convert=True)
    modular = []
    for factor, exponent in sp.factor_list(
        integral.as_expr(), modulus=2130706433
    )[1]:
        value = sp.Poly(factor, d, modulus=2130706433).monic()
        modular.append((
            value.degree(), exponent,
            str(value.as_expr()) if value.degree() <= 6 else None,
        ))
    if args.prove:
        expected_modular = {
            (0, 0): [
                (1, 1, "d + 1"), (1, 1, "d + 1065353216"),
                (1, 1, "d - 53820732"), (1, 1, "d - 2"),
                (1, 2, "d - 1"),
                (5, 1, "d**5 - 46684291*d**4 - 380864582*d**3 + 430254279*d**2 + 112941434*d - 724150483"),
            ],
            (0, 1): [
                (1, 1, "d + 1065353216"), (1, 1, "d - 2"),
                (1, 2, "d + 1"), (1, 5, "d - 1"), (8, 1, None),
            ],
            (0, 2): [
                (1, 2, "d + 1065353216"), (1, 2, "d - 2"),
                (1, 7, "d - 1"),
                (2, 1, "d**2 - 193204367*d - 98068426"),
                (15, 1, None),
            ],
            (1, 0): [
                (1, 4, "d + 1"), (1, 8, "d + 1065353216"),
                (1, 8, "d - 2"), (1, 10, "d - 1"), (20, 1, None),
            ],
            (1, 1): [
                (1, 1, "d + 261596606"), (1, 1, "d + 982346495"),
                (1, 1, "d - 1020436165"), (1, 1, "d - 901544254"),
                (1, 8, "d + 1065353216"), (1, 8, "d - 2"),
                (1, 10, "d + 1"), (1, 24, "d - 1"),
                (8, 1, None), (8, 1, None), (8, 1, None),
            ],
            (1, 2): [
                (1, 2, "d + 583634928"), (1, 2, "d - 583634934"),
                (1, 18, "d + 1065353216"), (1, 18, "d - 2"),
                (1, 34, "d - 1"),
                (4, 1, "d**4 + 91676387*d**3 - 927443603*d**2 + 91676387*d + 1"),
                (4, 1, "d**4 - 1047434221*d**3 - 591739591*d**2 - 1047434221*d + 1"),
                (9, 1, None), (9, 1, None), (14, 1, None), (14, 1, None),
            ],
        }[(args.left, args.right)]
        if modular != expected_modular:
            raise RuntimeError("pair modular census")
        print(
            f"KB_C2_112_NEAR_MOVING_OTHER_SQUARE_XI_PAIR_{args.left}{args.right}_PRIMARY_PASS",
            flush=True,
        )
    print(f"stage=pair_modular pair={args.left},{args.right} factors={modular}", flush=True)


if __name__ == "__main__":
    main()
