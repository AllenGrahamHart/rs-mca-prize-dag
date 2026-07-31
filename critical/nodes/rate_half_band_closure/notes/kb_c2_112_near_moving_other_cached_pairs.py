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
            "square-xi": {
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
            },
            "square-ell": {
                (0, 0): ("ff1037d63f8c13a0", [
                    (1, 1, "f93c38ef339888a3"),
                    (1, 1, "b8907990ebf04ed3"),
                    (1, 3, "3e8b7ae50a0eb368"),
                    (10, 1, "17ccba716c0e13e1"),
                ]),
                (0, 1): ("219a64c00e4cb01b", [
                    (1, 8, "f93c38ef339888a3"),
                    (1, 8, "b8907990ebf04ed3"),
                    (1, 16, "3e8b7ae50a0eb368"),
                    (40, 1, "9b745023825455d5"),
                ]),
                (1, 0): ("b9fc77fc477d33ea", [
                    (1, 2, "f93c38ef339888a3"),
                    (1, 2, "b8907990ebf04ed3"),
                    (1, 5, "3e8b7ae50a0eb368"),
                    (15, 1, "82e7a17ef1d1e402"),
                ]),
                (1, 1): ("30db7d2c7e8bff84", [
                    (1, 18, "f93c38ef339888a3"),
                    (1, 18, "b8907990ebf04ed3"),
                    (1, 28, "3e8b7ae50a0eb368"),
                    (2, 2, "039d9aaf13f5aa0d"),
                    (44, 1, "c06e614ff568a72d"),
                ]),
                (2, 0): ("5a73d058fdbb04d7", [
                    (1, 1, "f93c38ef339888a3"),
                    (1, 1, "b8907990ebf04ed3"),
                    (1, 2, "3e8b7ae50a0eb368"),
                    (5, 1, "fcaf8b1fcb0453c6"),
                ]),
                (2, 1): ("6209b4ab207d7275", [
                    (1, 8, "f93c38ef339888a3"),
                    (1, 8, "b8907990ebf04ed3"),
                    (1, 12, "3e8b7ae50a0eb368"),
                    (12, 1, "9700cbc5bf3e459b"),
                ]),
            },
        }[args.allocation][(args.left, args.right)]
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
            "square-xi": {
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
            },
            "square-ell": {
                (0, 0): [
                    (1, 1, "d + 1065353216"),
                    (1, 1, "d - 594504303"),
                    (1, 1, "d - 538097078"), (1, 1, "d - 2"),
                    (1, 3, "d - 1"),
                    (2, 1, "d**2 - 568598655*d - 374354523"),
                    (6, 1, "d**6 - 642577042*d**5 + 588486998*d**4 + 926294591*d**3 + 679398950*d**2 - 111286545*d - 26700929"),
                ],
                (0, 1): [
                    (1, 8, "d + 1065353216"), (1, 8, "d - 2"),
                    (1, 16, "d - 1"), (20, 1, None), (20, 1, None),
                ],
                (1, 0): [
                    (1, 1, "d + 251370115"),
                    (1, 1, "d - 299352588"),
                    (1, 2, "d + 1065353216"), (1, 2, "d - 2"),
                    (1, 5, "d - 1"), (13, 1, None),
                ],
                (1, 1): [
                    (1, 1, "d + 579618345"),
                    (1, 1, "d + 996338454"),
                    (1, 2, "d + 583634928"),
                    (1, 2, "d - 583634934"),
                    (1, 18, "d + 1065353216"), (1, 18, "d - 2"),
                    (1, 28, "d - 1"),
                    (2, 1, "d**2 + 16458322*d - 979475259"),
                    (2, 1, "d**2 + 699968870*d - 224576527"),
                    (2, 1, "d**2 + 703795947*d - 753996681"),
                    (2, 1, "d**2 + 957200620*d + 246061440"),
                    (2, 1, "d**2 - 97750688*d + 1"),
                    (10, 1, None), (11, 1, None), (11, 1, None),
                ],
                (2, 0): [
                    (1, 1, "d + 1065353216"),
                    (1, 1, "d - 499377018"),
                    (1, 1, "d - 151267790"), (1, 1, "d - 2"),
                    (1, 2, "d - 1"),
                    (3, 1, "d**3 - 414708410*d**2 + 399639044*d - 799507796"),
                ],
                (2, 1): [
                    (1, 8, "d + 1065353216"), (1, 8, "d - 2"),
                    (1, 12, "d - 1"),
                    (2, 1, "d**2 + 462837669*d + 643446795"),
                    (2, 1, "d**2 + 1033375787*d - 244556338"),
                    (2, 1, "d**2 - 748014748*d + 1"),
                    (6, 1, "d**6 + 52868123*d**5 + 322738914*d**4 - 848385901*d**3 + 322738914*d**2 + 52868123*d + 1"),
                ],
            },
        }[args.allocation][(args.left, args.right)]
        if modular != expected_modular:
            raise RuntimeError("pair modular census")
        print(
            f"KB_C2_112_NEAR_MOVING_OTHER_{args.allocation.replace('-', '_').upper()}_PAIR_{args.left}{args.right}_PRIMARY_PASS",
            flush=True,
        )
    print(f"stage=pair_modular pair={args.left},{args.right} factors={modular}", flush=True)


if __name__ == "__main__":
    main()
