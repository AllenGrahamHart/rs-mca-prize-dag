#!/usr/bin/env python3
"""Classify one routed other-xi candidate against all four source cores."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
PRIMARY = HERE / "kb_c2_112_near_moving_template_probe.py"
CHARACTERISTIC = 2130706433


def load_primary():
    spec = importlib.util.spec_from_file_location("moving_primary", PRIMARY)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load moving primary helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_cores(allocation, root, cache_dir, b, c, d, primary):
    path = cache_dir / f"kb_c2_112_other_{allocation}_{root}_cores.json"
    payload = json.loads(path.read_text())
    if payload["allocation"] != allocation or payload["root"] != root:
        raise RuntimeError("core cache scope")
    values = {}
    for kind in ("product", "sum"):
        terms = {
            tuple(monomial): sp.Rational(coefficient)
            for monomial, coefficient in payload["polynomials"][kind]
        }
        value = sp.Poly.from_dict(terms, (b, c, d), domain=sp.QQ)
        if primary.digest(value) != payload["digests"][kind]:
            raise RuntimeError(f"core cache digest {root}/{kind}")
        values[kind] = value
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "allocation", choices=("square-xi", "square-ell", "mixed")
    )
    parser.add_argument("index", type=int)
    parser.add_argument("--cache-dir", type=Path, default=Path("/tmp"))
    args = parser.parse_args()
    primary = load_primary()
    b, c, d, inverse = sp.symbols("b c d inverse")
    candidates = {
        "square-xi": (
            "d - 53820732",
            "d**2 - 193204367*d - 98068426",
            "d + 261596606", "d + 982346495",
            "d - 1020436165", "d - 901544254",
            "d + 583634928", "d - 583634934",
        ),
        "square-ell": (
            "d - 594504303", "d - 538097078",
            "d**2 - 568598655*d - 374354523",
            "d**6 - 642577042*d**5 + 588486998*d**4 + 926294591*d**3 + 679398950*d**2 - 111286545*d - 26700929",
            "d + 251370115", "d - 299352588",
            "d + 579618345", "d + 996338454",
            "d + 583634928", "d - 583634934",
            "d**2 + 16458322*d - 979475259",
            "d**2 + 699968870*d - 224576527",
            "d**2 + 703795947*d - 753996681",
            "d**2 + 957200620*d + 246061440",
            "d**2 - 97750688*d + 1",
            "d - 499377018", "d - 151267790",
            "d**3 - 414708410*d**2 + 399639044*d - 799507796",
            "d**2 + 462837669*d + 643446795",
            "d**2 + 1033375787*d - 244556338",
            "d**2 - 748014748*d + 1",
            "d**6 + 52868123*d**5 + 322738914*d**4 - 848385901*d**3 + 322738914*d**2 + 52868123*d + 1",
        ),
        "mixed": (
            "d - 814817489", "d - 783212336",
            "d + 204450215",
            "d**2 + 789879454*d + 82723665",
            "d + 710235477", "d + 152359007", "d + 506691192",
            "d**2 - 185559879*d - 988128217",
            "d + 136159215", "d + 137914370",
            "d + 773535750", "d - 1033497818",
            "d - 773535752", "d - 70784153",
            "d + 231959116", "d + 833394101",
            "d**2 + 72236946*d + 480334988",
            "d**2 + 307529315*d + 88673483",
            "d**2 + 349791372*d + 686936261",
            "d**2 + 583377876*d - 781526165",
            "d**3 - 404702624*d**2 - 606457571*d + 293107194",
            "d**6 + 1050209485*d**5 + 485933422*d**4 - 170239540*d**3 + 890733766*d**2 + 922536397*d + 640345259",
        ),
    }[args.allocation]
    if not 0 <= args.index < len(candidates):
        raise RuntimeError("candidate index")
    key = candidates[args.index]
    candidate = sp.Poly(
        sp.sympify(key, locals={"d": d}), d, modulus=CHARACTERISTIC
    ).monic()
    cores = []
    for root in ("c", "d"):
        by_kind = load_cores(
            args.allocation, root, args.cache_dir, b, c, d, primary
        )
        cores.extend(by_kind[kind].as_expr() for kind in ("product", "sum"))
    if args.allocation == "mixed" and candidate.degree() >= 3:
        coefficient_ring = sp.GF(CHARACTERISTIC).poly_ring(b, c)
        divisor = sp.Poly(
            candidate.as_expr(), d, domain=coefficient_ring
        )
        cores = [
            sp.Poly(value, d, domain=coefficient_ring).prem(divisor).as_expr()
            for value in cores
        ]
        print(
            f"stage=candidate_reduce degree={candidate.degree()} "
            f"terms={[len(sp.Poly(value, b, c, d, modulus=CHARACTERISTIC).terms()) for value in cores]}",
            flush=True,
        )
    print(f"stage=cache_load candidate={key!r}", flush=True)
    basis = sp.groebner(
        [*cores, candidate.as_expr()],
        b, c, d,
        order="lex",
        modulus=CHARACTERISTIC,
    )
    unit = len(basis.polys) == 1 and basis.polys[0].as_expr() == 1
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
    remainder_zero = unit or basis.reduce(forbidden)[1] == 0
    saturated_unit = remainder_zero
    if not saturated_unit:
        saturated = sp.groebner(
            [
                *(value.as_expr() for value in basis.polys),
                inverse * forbidden - 1,
            ],
            inverse, b, c, d,
            order="lex",
            modulus=CHARACTERISTIC,
        )
        saturated_unit = (
            len(saturated.polys) == 1
            and saturated.polys[0].as_expr() == 1
        )
    records = [
        (
            tuple(value.degree(variable) for variable in (b, c, d)),
            len(value.terms()), primary.digest(value),
        )
        for value in basis.polys
    ]
    print(
        f"stage=classification index={args.index} candidate={key!r} "
        f"basis={records} unit={unit} forbidden_remainder_zero={remainder_zero} "
        f"forbidden_saturation_unit={saturated_unit}",
        flush=True,
    )
    if not saturated_unit:
        raise RuntimeError("admissible candidate survives")


if __name__ == "__main__":
    main()
