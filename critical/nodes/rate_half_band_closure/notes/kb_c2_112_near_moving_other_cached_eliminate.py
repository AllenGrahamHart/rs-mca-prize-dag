#!/usr/bin/env python3
"""Eliminate one hash-checked cached core pair from the other-xi probe."""

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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("allocation", choices=("square-xi", "square-ell", "mixed"))
    parser.add_argument("root", choices=("c", "d"))
    parser.add_argument("--cache-dir", type=Path, default=Path("/tmp"))
    parser.add_argument(
        "mode",
        choices=(
            "resultant", "subresultant", "modular", "field", "modfield",
            "factor-product", "factor-sum",
            "branch0", "branch1", "modbranch0", "modbranch1",
            "factorbranch0", "factorbranch1",
            "cache-components",
        ),
    )
    args = parser.parse_args()
    primary = load_primary()
    b, c, d = sp.symbols("b c d")
    cache = args.cache_dir / (
        f"kb_c2_112_other_{args.allocation}_{args.root}_cores.json"
    )
    payload = json.loads(cache.read_text())
    if payload["allocation"] != args.allocation or payload["root"] != args.root:
        raise RuntimeError("cache scope")

    cores = {}
    for kind in ("product", "sum"):
        terms = {
            tuple(monomial): sp.Rational(coefficient)
            for monomial, coefficient in payload["polynomials"][kind]
        }
        value = sp.Poly.from_dict(terms, (b, c, d), domain=sp.QQ)
        if primary.digest(value) != payload["digests"][kind]:
            raise RuntimeError(f"cache digest {kind}")
        cores[kind] = value
    print(f"stage=cache_load digests={payload['digests']}", flush=True)

    if args.mode == "cache-components":
        standard = {
            "6a515ecf832aff78", "e31255d5e81e2509",
            "4aa033e0505df8f1", "73c55ff149852dee",
            "19d832b1f64387da", "4975135dd6af0fc0",
            "dbe56c4d43b264a2", "824f64bb4a05a043",
            "cb4fd487538b0eff", "477785c532483181",
            "7a7743ce53fe8f77",
        }
        parents = []
        if args.root == "c":
            branches = []
            for factor, exponent in sp.factor_list(cores["product"].as_expr())[1]:
                if exponent != 1:
                    raise RuntimeError("product branch multiplicity")
                branches.append(
                    sp.Poly(factor, b, c, d, domain=sp.QQ).primitive()[1]
                )
            for branch in branches:
                parents.append(sp.Poly(
                    sp.resultant(
                        branch.as_expr(), cores["sum"].as_expr(), b
                    ),
                    c, d, domain=sp.QQ,
                ).primitive()[1])
        else:
            s = sp.symbols("s")
            traces = {}
            for kind in ("product", "sum"):
                trace, removed = primary.reciprocal_trace(
                    cores[kind], b, c, d, s
                )
                if trace is None:
                    raise RuntimeError(f"d trace failed: {removed}")
                traces[kind] = trace
            parents.append(sp.Poly(
                sp.resultant(
                    traces["product"].as_expr(), traces["sum"].as_expr(), s
                ),
                c, d, domain=sp.QQ,
            ).primitive()[1])
        components = {}
        for parent in parents:
            for factor, _ in sp.factor_list(parent.as_expr())[1]:
                value = sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
                key = primary.digest(value)
                if key not in standard:
                    components[key] = value
        component_payload = {
            "allocation": args.allocation,
            "root": args.root,
            "components": [
                {
                    "digest": key,
                    "terms": [
                        [list(monomial), str(coefficient)]
                        for monomial, coefficient in value.terms()
                    ],
                }
                for key, value in sorted(components.items())
            ],
        }
        component_cache = args.cache_dir / (
            f"kb_c2_112_other_{args.allocation}_{args.root}_components.json"
        )
        component_cache.write_text(json.dumps(component_payload, sort_keys=True))
        print(
            f"stage=component_cache path={component_cache} "
            f"bytes={component_cache.stat().st_size} "
            f"components={[(key, (value.degree(c), value.degree(d)), len(value.terms())) for key, value in sorted(components.items())]}",
            flush=True,
        )
        return

    if args.mode.startswith("factor-"):
        kind = args.mode.removeprefix("factor-")
        factors = []
        for factor, exponent in sp.factor_list(cores[kind].as_expr())[1]:
            value = sp.Poly(factor, b, c, d, domain=sp.QQ).primitive()[1]
            factors.append((
                tuple(value.degree(variable) for variable in (b, c, d)),
                len(value.terms()), exponent, primary.digest(value),
            ))
        print(f"stage={args.mode} factors={factors}", flush=True)
        return

    if "branch" in args.mode:
        branches = []
        for factor, exponent in sp.factor_list(cores["product"].as_expr())[1]:
            if exponent != 1:
                raise RuntimeError("product branch multiplicity")
            value = sp.Poly(factor, b, c, d, domain=sp.QQ).primitive()[1]
            branches.append((primary.digest(value), value))
        branches.sort()
        index = int(args.mode[-1])
        branch_digest, branch = branches[index]
        if args.mode.startswith("mod"):
            characteristic = 2130706433
            left = sp.Poly(
                branch.as_expr(), b, c, d, modulus=characteristic
            )
            right = sp.Poly(
                cores["sum"].as_expr(), b, c, d, modulus=characteristic
            )
            resultant = left.resultant(right)
            if not isinstance(resultant, sp.Poly):
                resultant = sp.Poly(resultant, c, d, modulus=characteristic)
            resultant = resultant.monic()
        else:
            resultant = sp.Poly(
                sp.resultant(branch.as_expr(), cores["sum"].as_expr(), b),
                c, d, domain=sp.QQ,
            ).primitive()[1]
        print(
            f"stage=branch_parent index={index} branch_digest={branch_digest} "
            f"degrees=({resultant.degree(c)},{resultant.degree(d)}) "
            f"terms={len(resultant.terms())} digest={primary.digest(resultant)}",
            flush=True,
        )
        if args.mode.startswith("factorbranch"):
            records = []
            for factor, exponent in sp.factor_list(resultant.as_expr())[1]:
                value = sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
                records.append((
                    (value.degree(c), value.degree(d)), len(value.terms()),
                    exponent, primary.digest(value),
                ))
            print(f"stage=branch_factors index={index} factors={records}", flush=True)
        return

    if args.mode in ("field", "modfield"):
        characteristic = 2130706433
        ground = sp.QQ if args.mode == "field" else sp.GF(characteristic)
        field = ground.frac_field(c, d)
        left = sp.Poly(cores["product"].as_expr(), b, domain=field)
        right = sp.Poly(cores["sum"].as_expr(), b, domain=field)
        field_resultant = left.resultant(right)
        expression = (
            field.to_sympy(field_resultant)
            if not isinstance(field_resultant, sp.Basic)
            else field_resultant
        )
        numerator = sp.fraction(sp.cancel(expression))[0]
        resultant = sp.Poly(
            numerator,
            c, d,
            **({"domain": sp.QQ} if args.mode == "field" else {"modulus": characteristic}),
        )
        resultant = resultant.primitive()[1] if args.mode == "field" else resultant.monic()
    elif args.mode == "modular":
        characteristic = 2130706433
        left = sp.Poly(
            cores["product"].as_expr(), b, c, d, modulus=characteristic
        )
        right = sp.Poly(
            cores["sum"].as_expr(), b, c, d, modulus=characteristic
        )
        resultant = left.resultant(right)
        if not isinstance(resultant, sp.Poly):
            resultant = sp.Poly(resultant, c, d, modulus=characteristic)
        resultant = resultant.monic()
    elif args.mode == "subresultant":
        sequence = sp.subresultants(
            cores["product"].as_expr(), cores["sum"].as_expr(), b
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
                cores["product"].as_expr(), cores["sum"].as_expr(), b
            ),
            c, d, domain=sp.QQ,
        ).primitive()[1]
    print(
        f"stage=parent mode={args.mode} root={args.root} "
        f"degrees=({resultant.degree(c)},{resultant.degree(d)}) "
        f"terms={len(resultant.terms())} digest={primary.digest(resultant)}",
        flush=True,
    )


if __name__ == "__main__":
    main()
