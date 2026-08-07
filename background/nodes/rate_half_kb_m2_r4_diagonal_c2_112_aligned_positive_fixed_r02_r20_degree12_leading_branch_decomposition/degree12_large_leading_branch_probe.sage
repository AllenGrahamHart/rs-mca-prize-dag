#!/usr/bin/env sage
"""Test an E2/E3 large x-leading-factor branch of the fixed degree-12 route."""

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


def x_leading(base, value):
    x, s, p = base.gens()
    degree_x = int(value.degree(x))
    return base(
        sum(
            QQ(coefficient) * s ** monomial[1] * p ** monomial[2]
            for monomial, coefficient in base(value).dict().items()
            if monomial[0] == degree_x
        )
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
    parser.add_argument("--row", choices=("E2", "E3"), required=True)
    parser.add_argument("--prime", type=int, default=2130706433)
    args = parser.parse_args()
    print(
        canonical_json({"phase": "START", "cell": args.cell, "row": args.row}),
        flush=True,
    )

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
    degree6_candidates = [
        factor
        for factor, _ in x_leading(base, selected).factor()
        if factor.total_degree() == 6
    ]
    assert len(degree6_candidates) == 1
    degree6 = degree6_candidates[0]

    target_row = branch["essential"][args.row]
    leading = x_leading(base, target_row)
    large_candidates = [
        factor
        for factor, _ in leading.factor()
        if factor.total_degree() >= 20
        and library["normalized_key"](factor) not in branch["unit_keys"]
    ]
    assert len(large_candidates) == 1
    large = large_candidates[0]

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
        "large": convert(large),
        "R12": convert(selected),
        "E2": convert(branch["essential"]["E2"]),
        "E3": convert(branch["essential"]["E3"]),
    }
    print(
        canonical_json(
            {
                "phase": "CONVERTED",
                "selected_sha256": digest(selected),
                "degree6": metric(converted["L6"], (x, s, p)),
                "large": {
                    **metric(converted["large"], (x, s, p)),
                    "polynomial": str(large),
                },
                "generators": {
                    name: metric(converted[name], (x, s, p))
                    for name in ("R12", "E2", "E3")
                },
            }
        ),
        flush=True,
    )

    print(canonical_json({"phase": "SEED_GROEBNER_BEGIN"}), flush=True)
    seed_basis = list(
        ring.ideal([converted["large"], converted["R12"]]).groebner_basis(
            algorithm="singular:slimgb"
        )
    )
    seed_unit = seed_basis == [ring(1)]
    seed_dimension = -1 if seed_unit else int(ring.ideal(seed_basis).dimension())
    print(
        canonical_json(
            {
                "phase": "SEED_GROEBNER_DONE",
                "unit_ideal": seed_unit,
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

    localizer_factors = [("prior_s", ring(s)), ("prior_L6", converted["L6"])]
    localizer_factors.extend(
        (f"unit_{index}", convert(factor))
        for index, factor in enumerate(branch["unit_factors"], start=1)
    )
    localizer = ring(1)
    steps = []
    nilpotence_index = 1 if unit_ideal else None
    if not unit_ideal:
        for index, (label, factor) in enumerate(localizer_factors, start=1):
            localizer = (localizer * factor).reduce(full_basis)
            steps.append(
                {
                    "index": index,
                    "label": label,
                    "factor_zero": not bool(factor),
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
        "DEGREE12_LARGE_LEADING_EMPTY"
        if nilpotence_index is not None
        else "DEGREE12_LARGE_LEADING_SURVIVES"
    )
    print(
        canonical_json(
            {
                "phase": "DONE",
                "cell": args.cell,
                "row": args.row,
                "selected_sha256": digest(selected),
                "degree6_sha256": digest(degree6),
                "large_sha256": digest(large),
                "large_degree": int(large.total_degree()),
                "large_terms": int(len(large.monomials())),
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
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
