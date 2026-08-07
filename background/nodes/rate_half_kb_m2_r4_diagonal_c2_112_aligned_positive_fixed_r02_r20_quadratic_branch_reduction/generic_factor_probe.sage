#!/usr/bin/env sage
"""Factorwise generic probe for the remaining fixed R02/R20 cells."""

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cell",
        choices=tuple(
            f"{assignment}-{target}"
            for assignment in ("F04", "F05", "F06", "F07")
            for target in ("R02", "R20")
        ),
        required=True,
    )
    parser.add_argument("--factor-index", type=int, choices=(0, 1, 2), required=True)
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
    r_factors = [
        record["factor"]
        for record in branch["factors"]["R"]
        if not record["named_unit_factor"]
    ]
    assert len(r_factors) == 3
    selected = r_factors[args.factor_index]
    e2 = branch["essential"]["E2"]
    e3 = branch["essential"]["E3"]
    print(
        canonical_json(
            {
                "phase": "BRANCH",
                "resultant_factor_count": len(r_factors),
                "selected": {
                    "degree": int(selected.total_degree()),
                    "degrees": [int(selected.degree(g)) for g in base.gens()],
                    "terms": int(len(selected.monomials())),
                    "sha256": digest(selected),
                    "polynomial": str(selected) if len(selected.monomials()) <= 300 else None,
                },
                "remaining_core_metrics": [
                    {
                        "degree": int(value.total_degree()),
                        "degrees": [int(value.degree(g)) for g in base.gens()],
                        "terms": int(len(value.monomials())),
                        "sha256": digest(value),
                    }
                    for value in (e2, e3)
                ],
                "transported_unit_factor_count": len(branch["unit_factors"]),
            }
        ),
        flush=True,
    )

    field = GF(ZZ(args.prime))
    ring = PolynomialRing(field, names=("x", "s", "p"), order="degrevlex")

    def convert(value):
        output = ring(0)
        for monomial, coefficient in base(value).dict().items():
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += reduced * prod(
                generator ** exponent
                for generator, exponent in zip(ring.gens(), monomial)
            )
        return output

    generators = [convert(selected), convert(e2), convert(e3)]
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
        for index, factor in enumerate(branch["unit_factors"], start=1):
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
        "selected_resultant_factor_sha256": digest(selected),
        "basis_size": len(basis),
        "basis_sha256": digest("\n".join(str(value) for value in basis)),
        "dimension": dimension,
        "unit_ideal": unit_ideal,
        "localizer_factor_count": len(branch["unit_factors"]),
        "localizer_steps": steps,
        "localizer_powers": powers,
        "localizer_nilpotence_index": nilpotence_index,
        "terminal": (
            "GENERIC_RESULTANT_FACTOR_EMPTY_AFTER_LOCALIZATION"
            if nilpotence_index is not None
            else "GENERIC_RESULTANT_FACTOR_SURVIVES"
        ),
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
