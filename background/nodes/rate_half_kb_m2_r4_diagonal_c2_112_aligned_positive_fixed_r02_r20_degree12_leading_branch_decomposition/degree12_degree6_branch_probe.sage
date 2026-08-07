#!/usr/bin/env sage
"""Test the common degree-6 leading-drop branch of the fixed degree-12 route."""

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


def metric(value, generators):
    value = value.parent()(value)
    return {
        "degree": int(value.total_degree()) if value else -1,
        "degrees": [int(value.degree(generator)) for generator in generators],
        "terms": int(len(value.monomials())) if value else 0,
        "sha256": digest(value),
    }


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
    bx, bs, bp = base.gens()
    r_factors = [
        record["factor"]
        for record in branch["factors"]["R"]
        if not record["named_unit_factor"]
    ]
    selected = r_factors[2]
    degree_x = int(selected.degree(bx))
    leading = base(
        sum(
            QQ(coefficient) * bs ** monomial[1] * bp ** monomial[2]
            for monomial, coefficient in selected.dict().items()
            if monomial[0] == degree_x
        )
    )
    leading_factors = [
        factor
        for factor, exponent in leading.factor()
        if not library["normalized_key"](factor) in branch["unit_keys"]
        for _ in range(int(exponent))
    ]
    assert len(leading_factors) == 1
    degree6 = leading_factors[0]
    assert degree6.total_degree() == 6

    field = GF(ZZ(args.prime))
    ring = PolynomialRing(field, names=("x", "s", "p"), order="degrevlex")
    x, s, p = ring.gens()

    def convert(value):
        output = ring(0)
        for monomial, coefficient in base(value).dict().items():
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += (
                reduced
                * x ** monomial[0]
                * s ** monomial[1]
                * p ** monomial[2]
            )
        return output

    converted = {
        "L6": convert(degree6),
        "R12": convert(selected),
        "E2": convert(branch["essential"]["E2"]),
        "E3": convert(branch["essential"]["E3"]),
    }
    print(
        canonical_json(
            {
                "phase": "CONVERTED",
                "selected_sha256": digest(selected),
                "degree6_sha256": digest(degree6),
                "generators": {
                    name: metric(value, (x, s, p))
                    for name, value in converted.items()
                },
            }
        ),
        flush=True,
    )

    print(canonical_json({"phase": "SEED_GROEBNER_BEGIN"}), flush=True)
    seed_ideal = ring.ideal([converted["L6"], converted["R12"]])
    seed_basis = list(seed_ideal.groebner_basis(algorithm="singular:slimgb"))
    seed_dimension = int(ring.ideal(seed_basis).dimension())
    print(
        canonical_json(
            {
                "phase": "SEED_GROEBNER_DONE",
                "dimension": seed_dimension,
                "basis_size": len(seed_basis),
                "basis_sha256": digest("\n".join(str(value) for value in seed_basis)),
                "basis_metrics": [metric(value, (x, s, p)) for value in seed_basis],
            }
        ),
        flush=True,
    )

    reduced = {
        name: converted[name].reduce(seed_basis)
        for name in ("E2", "E3")
    }
    print(
        canonical_json(
            {
                "phase": "ESSENTIAL_REDUCED",
                "generators": {
                    name: metric(value, (x, s, p))
                    for name, value in reduced.items()
                },
            }
        ),
        flush=True,
    )

    print(canonical_json({"phase": "FULL_GROEBNER_BEGIN"}), flush=True)
    full_basis = list(
        ring.ideal(seed_basis + [reduced["E2"], reduced["E3"]]).groebner_basis(
            algorithm="singular:slimgb"
        )
    )
    unit_ideal = full_basis == [ring(1)]
    dimension = -1 if unit_ideal else int(ring.ideal(full_basis).dimension())
    print(
        canonical_json(
            {
                "phase": "FULL_GROEBNER_DONE",
                "unit_ideal": unit_ideal,
                "dimension": dimension,
                "basis_size": len(full_basis),
                "basis_sha256": digest("\n".join(str(value) for value in full_basis)),
                "basis_metrics": [metric(value, (x, s, p)) for value in full_basis],
            }
        ),
        flush=True,
    )

    localizer = ring(1)
    steps = []
    nilpotence_index = 1 if unit_ideal else None
    if not unit_ideal:
        for index, factor in enumerate(branch["unit_factors"], start=1):
            converted_factor = convert(factor)
            localizer = (localizer * converted_factor).reduce(full_basis)
            steps.append(
                {
                    "index": index,
                    "factor_zero": not bool(converted_factor),
                    "zero": not bool(localizer),
                    "metric": metric(localizer, (x, s, p)),
                }
            )
            if not localizer:
                nilpotence_index = 1
                break
        if localizer:
            current = localizer
            for exponent in range(2, 5):
                current = (current * localizer).reduce(full_basis)
                if not current:
                    nilpotence_index = exponent
                    break

    terminal = (
        "DEGREE12_DEGREE6_EMPTY"
        if nilpotence_index is not None
        else "DEGREE12_DEGREE6_SURVIVES"
    )
    result = {
        "phase": "DONE",
        "cell": args.cell,
        "selected_sha256": digest(selected),
        "degree6_sha256": digest(degree6),
        "seed_basis_size": len(seed_basis),
        "seed_basis_sha256": digest("\n".join(str(value) for value in seed_basis)),
        "basis_size": len(full_basis),
        "basis_sha256": digest("\n".join(str(value) for value in full_basis)),
        "dimension": dimension,
        "unit_ideal": unit_ideal,
        "localizer_steps": steps,
        "localizer_nilpotence_index": nilpotence_index,
        "terminal": terminal,
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
