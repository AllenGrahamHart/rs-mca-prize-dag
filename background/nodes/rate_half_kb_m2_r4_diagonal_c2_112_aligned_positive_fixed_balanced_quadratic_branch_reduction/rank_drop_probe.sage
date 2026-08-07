#!/usr/bin/env sage
"""Exact factorwise probe for the balanced fixed V=0 rank-drop chart."""

import argparse
import hashlib
import json
from pathlib import Path


LIBRARY = Path("/branch_core.sage")


def load_library():
    namespace = dict(globals())
    namespace.update({"__name__": "branch_core_library", "__file__": str(LIBRARY)})
    raw = LIBRARY.read_text()
    exec(compile(raw, str(LIBRARY), "exec"), namespace)
    return namespace


def digest(value):
    return hashlib.sha256(str(value).encode()).hexdigest()


def canonical_json(value):
    return json.dumps(
        value,
        sort_keys=True,
        default=lambda item: int(item) if item in ZZ else str(item),
    )


def normalized_key(value):
    value = value.parent()(value)
    return str(value / value.lc()) if value else "0"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cell",
        choices=tuple(
            f"{assignment}-{target}"
            for assignment in ("F04", "F05", "F06", "F07")
            for target in ("R02", "R11", "R20")
        ),
        required=True,
    )
    parser.add_argument("--factor-index", type=int, choices=tuple(range(6)), default=0)
    parser.add_argument("--structure-only", action="store_true")
    parser.add_argument("--prime", type=int, default=2130706433)
    args = parser.parse_args()
    print(
        canonical_json(
            {
                "phase": "START",
                "cell": args.cell,
                "factor_index": args.factor_index,
                "prime": args.prime,
            }
        ),
        flush=True,
    )

    library = load_library()
    branch = library["build_branch"](args.cell)
    base = branch["base"]
    source = branch["converted"][0].parent()
    qring = PolynomialRing(QQ, names=("x", "s", "p", "w"), order="degrevlex")

    def univariate_to_qring(value):
        output = qring(0)
        for w_exponent, coefficient in source(value).dict().items():
            for monomial, scalar in base(coefficient).dict().items():
                output += QQ(scalar) * prod(
                    generator ** exponent
                    for generator, exponent in zip(
                        qring.gens(), (*monomial, int(w_exponent))
                    )
                )
        return output

    qrows = [univariate_to_qring(value) for value in branch["converted"]]
    frontier = library["load_frontier"]()
    parent = frontier["PARENT"]
    named_units = parent["middle_units"](parent["S"], True)

    def source_to_qring(value):
        output = qring(0)
        for monomial, coefficient in parent["S"](value).dict().items():
            output += QQ(coefficient) * prod(
                generator ** exponent
                for generator, exponent in zip(qring.gens(), monomial)
            )
        return output

    unit_factors = {}
    for value in named_units:
        for factor, _ in source_to_qring(value).factor():
            unit_factors[normalized_key(factor)] = factor
    unit_keys = set(unit_factors)

    def essential(value):
        kept = qring(1)
        for factor, exponent in qring(value).factor():
            if normalized_key(factor) not in unit_keys:
                kept *= factor ** exponent
        return qring(kept)

    essential_rows = [essential(value) for value in qrows]
    v_factors = []
    for factor, exponent in branch["equations"]["V"].factor():
        embedded = qring(str(factor))
        if normalized_key(embedded) not in unit_keys:
            v_factors.append((embedded, int(exponent)))
    factor_census = [
        {
            "index": int(index),
            "exponent": int(exponent),
            "degree": int(factor.total_degree()),
            "degrees": [int(factor.degree(g)) for g in qring.gens()],
            "terms": int(len(factor.monomials())),
            "sha256": digest(factor),
            "polynomial": str(factor) if len(factor.monomials()) <= 300 else None,
        }
        for index, (factor, exponent) in enumerate(v_factors)
    ]
    if args.structure_only:
        print(
            canonical_json(
                {
                    "phase": "DONE",
                    "cell": args.cell,
                    "nonnamed_v_factor_count": len(v_factors),
                    "factor_census": factor_census,
                    "unit_factor_count": len(unit_factors),
                    "terminal": "RANK_DROP_FACTOR_CENSUS_ONLY",
                }
            ),
            flush=True,
        )
        return
    assert args.factor_index < len(v_factors)
    selected, selected_exponent = v_factors[args.factor_index]
    print(
        canonical_json(
            {
                "phase": "BRANCH",
                "nonnamed_v_factor_count": len(v_factors),
                "factor_census": factor_census,
                "selected": {
                    "index": args.factor_index,
                    "exponent": selected_exponent,
                    "degree": int(selected.total_degree()),
                    "degrees": [int(selected.degree(g)) for g in qring.gens()],
                    "terms": int(len(selected.monomials())),
                    "sha256": digest(selected),
                    "polynomial": str(selected) if len(selected.monomials()) <= 300 else None,
                },
                "row_metrics": [
                    {
                        "degree": int(value.total_degree()),
                        "terms": int(len(value.monomials())),
                        "sha256": digest(value),
                    }
                    for value in essential_rows
                ],
                "unit_factor_count": len(unit_factors),
            }
        ),
        flush=True,
    )

    field = GF(ZZ(args.prime))
    ring = PolynomialRing(field, names=("x", "s", "p", "w"), order="degrevlex")

    def convert(value):
        output = ring(0)
        for monomial, coefficient in qring(value).dict().items():
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += reduced * prod(
                generator ** exponent
                for generator, exponent in zip(ring.gens(), monomial)
            )
        return output

    generators = [convert(value) for value in essential_rows]
    generators.append(convert(selected))
    print(canonical_json({"phase": "GROEBNER_BEGIN"}), flush=True)
    basis = list(ring.ideal(generators).groebner_basis(algorithm="singular:slimgb"))
    unit_ideal = basis == [ring(1)]
    dimension = -1 if unit_ideal else int(ring.ideal(basis).dimension())
    print(
        canonical_json(
            {
                "phase": "GROEBNER_DONE",
                "unit_ideal": unit_ideal,
                "dimension": dimension,
                "basis_size": len(basis),
                "basis_sha256": digest("\n".join(str(value) for value in basis)),
            }
        ),
        flush=True,
    )

    localizer = ring(1)
    steps = []
    if not unit_ideal:
        for index, factor in enumerate(
            [unit_factors[key] for key in sorted(unit_factors)], start=1
        ):
            localizer = (localizer * convert(factor)).reduce(basis)
            step = {
                "index": int(index),
                "zero": not bool(localizer),
                "degree": int(localizer.total_degree()) if localizer else None,
                "terms": int(len(localizer.monomials())) if localizer else None,
                "sha256": digest(localizer),
            }
            steps.append(step)
            print(canonical_json({"phase": "LOCALIZER_FACTOR", **step}), flush=True)
            if not localizer:
                break
    nilpotence_index = 1 if unit_ideal or not localizer else None
    powers = []
    if not unit_ideal and localizer:
        current = ring(1)
        for exponent in range(1, 5):
            current = (current * localizer).reduce(basis)
            power = {
                "exponent": int(exponent),
                "zero": not bool(current),
                "degree": int(current.total_degree()) if current else None,
                "terms": int(len(current.monomials())) if current else None,
                "sha256": digest(current),
            }
            powers.append(power)
            print(canonical_json({"phase": "LOCALIZER_POWER", **power}), flush=True)
            if not current:
                nilpotence_index = int(exponent)
                break

    result = {
        "phase": "DONE",
        "cell": args.cell,
        "factor_index": args.factor_index,
        "prime": args.prime,
        "selected_v_factor_sha256": digest(selected),
        "basis_size": len(basis),
        "basis_sha256": digest("\n".join(str(value) for value in basis)),
        "dimension": dimension,
        "unit_ideal": unit_ideal,
        "localizer_factor_count": len(unit_factors),
        "localizer_steps": steps,
        "localizer_powers": powers,
        "localizer_nilpotence_index": nilpotence_index,
        "terminal": (
            "RANK_DROP_FACTOR_EMPTY_AFTER_NAMED_LOCALIZATION"
            if nilpotence_index is not None
            else "RANK_DROP_FACTOR_SURVIVES"
        ),
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
