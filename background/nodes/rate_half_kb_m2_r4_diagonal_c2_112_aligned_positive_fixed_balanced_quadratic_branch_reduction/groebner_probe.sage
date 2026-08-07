#!/usr/bin/env sage
"""Bounded modular Groebner probe for the three essential generic cores."""

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
        choices=("F04-R11", "F05-R11", "F06-R11", "F07-R11"),
        required=True,
    )
    parser.add_argument("--prime", type=int, required=True)
    args = parser.parse_args()
    print(canonical_json({"phase": "START", "cell": args.cell, "prime": args.prime}), flush=True)

    library = load_library()
    branch = library["build_branch"](args.cell)
    source = branch["base"]
    field = GF(ZZ(args.prime))
    ring = PolynomialRing(field, names=("x", "s", "p"), order="degrevlex")

    def convert(value):
        output = ring(0)
        for monomial, coefficient in source(value).dict().items():
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += reduced * prod(
                generator ** exponent for generator, exponent in zip(ring.gens(), monomial)
            )
        return output

    names = ("R", "E2", "E3")
    cores = [convert(branch["essential"][name]) for name in names]
    print(
        canonical_json(
            {
                "phase": "CORES",
                "metrics": [
                    {
                        "name": name,
                        "degree": int(core.total_degree()),
                        "degrees": [int(core.degree(g)) for g in ring.gens()],
                        "terms": int(len(core.monomials())),
                        "sha256": digest(core),
                    }
                    for name, core in zip(names, cores)
                ],
            }
        ),
        flush=True,
    )
    print(canonical_json({"phase": "GROEBNER_BEGIN", "algorithm": "singular:slimgb"}), flush=True)
    ideal = ring.ideal(cores)
    basis = list(ideal.groebner_basis(algorithm="singular:slimgb"))
    unit = basis == [ring(1)]
    basis_ideal = ring.ideal(basis)
    try:
        dimension = int(basis_ideal.dimension())
    except Exception as error:
        dimension = f"ERROR:{type(error).__name__}:{error}"
    try:
        vector_space_dimension = int(basis_ideal.vector_space_dimension())
    except Exception as error:
        vector_space_dimension = f"ERROR:{type(error).__name__}:{error}"

    print(
        canonical_json(
            {
                "phase": "LOCALIZER_BEGIN",
                "factor_count": len(branch["unit_factors"]),
            }
        ),
        flush=True,
    )
    localizer = ring(1)
    localizer_steps = []
    for index, factor in enumerate(branch["unit_factors"], start=1):
        localizer = (localizer * convert(factor)).reduce(basis)
        step = {
            "index": int(index),
            "zero": not bool(localizer),
            "degree": int(localizer.total_degree()) if localizer else None,
            "terms": int(len(localizer.monomials())) if localizer else None,
            "sha256": digest(localizer),
        }
        localizer_steps.append(step)
        print(canonical_json({"phase": "LOCALIZER_FACTOR", **step}), flush=True)
        if not localizer:
            break

    powers = []
    nilpotence_index = 1 if not localizer else None
    if localizer:
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
                nilpotence_index = exponent
                break
    result = {
        "phase": "DONE",
        "cell": args.cell,
        "prime": args.prime,
        "unit_ideal": unit,
        "dimension": dimension,
        "vector_space_dimension": vector_space_dimension,
        "localizer_factor_count": len(branch["unit_factors"]),
        "localizer_steps": localizer_steps,
        "localizer_powers": powers,
        "localizer_nilpotence_index": nilpotence_index,
        "basis_size": len(basis),
        "basis_sha256": digest("\n".join(str(value) for value in basis)),
        "basis_metrics": [
            {
                "degree": int(value.total_degree()),
                "terms": int(len(value.monomials())),
                "sha256": digest(value),
            }
            for value in basis[:20]
        ],
        "terminal": (
            "EMPTY_AFTER_ESSENTIAL_CORE_LOCALIZATION"
            if unit or nilpotence_index is not None
            else "ESSENTIAL_CORE_LOCALIZED_SURVIVES"
        ),
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
