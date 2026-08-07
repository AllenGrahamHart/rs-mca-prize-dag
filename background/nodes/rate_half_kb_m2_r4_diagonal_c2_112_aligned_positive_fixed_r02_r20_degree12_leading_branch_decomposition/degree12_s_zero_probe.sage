#!/usr/bin/env sage
"""Test the s=0 leading-drop branch of the fixed degree-12 route."""

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
    parser.add_argument("--prime", type=int, default=2130706433)
    args = parser.parse_args()
    print(canonical_json({"phase": "START", "cell": args.cell}), flush=True)

    library = load_library()
    branch = library["build_branch"](args.cell)
    base = branch["base"]
    r_factors = [
        record["factor"]
        for record in branch["factors"]["R"]
        if not record["named_unit_factor"]
    ]
    selected = r_factors[2]

    field = GF(ZZ(args.prime))
    ring = PolynomialRing(field, names=("x", "p"), order="degrevlex")
    x, p = ring.gens()

    def specialize(value):
        output = ring(0)
        for monomial, coefficient in base(value).dict().items():
            ex, es, ep = monomial
            if es:
                continue
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += reduced * x ** ex * p ** ep
        return output

    generators = [
        specialize(selected),
        specialize(branch["essential"]["E2"]),
        specialize(branch["essential"]["E3"]),
    ]
    print(
        canonical_json(
            {
                "phase": "SPECIALIZED",
                "generators": [
                    {
                        "degree": int(value.total_degree()) if value else -1,
                        "degrees": [int(value.degree(generator)) for generator in (x, p)],
                        "terms": int(len(value.monomials())) if value else 0,
                        "sha256": digest(value),
                    }
                    for value in generators
                ],
            }
        ),
        flush=True,
    )
    assert all(generators)

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
    nilpotence_index = 1 if unit_ideal else None
    if not unit_ideal:
        for index, factor in enumerate(branch["unit_factors"], start=1):
            specialized = specialize(factor)
            localizer = (localizer * specialized).reduce(basis)
            step = {
                "index": index,
                "specialized_factor_zero": not bool(specialized),
                "zero": not bool(localizer),
                "degree": int(localizer.total_degree()) if localizer else None,
                "terms": int(len(localizer.monomials())) if localizer else None,
                "sha256": digest(localizer),
            }
            steps.append(step)
            if not localizer:
                nilpotence_index = 1
                break
        if localizer:
            current = localizer
            for exponent in range(2, 5):
                current = (current * localizer).reduce(basis)
                if not current:
                    nilpotence_index = exponent
                    break

    result = {
        "phase": "DONE",
        "cell": args.cell,
        "selected_sha256": digest(selected),
        "basis_size": len(basis),
        "basis_sha256": digest("\n".join(str(value) for value in basis)),
        "dimension": dimension,
        "unit_ideal": unit_ideal,
        "localizer_steps": steps,
        "localizer_nilpotence_index": nilpotence_index,
        "terminal": (
            "DEGREE12_S_ZERO_EMPTY"
            if nilpotence_index is not None
            else "DEGREE12_S_ZERO_SURVIVES"
        ),
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
