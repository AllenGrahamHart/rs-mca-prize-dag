#!/usr/bin/env sage
"""Intersect surviving F04 cubic q-slice curves with full-J factors."""

import argparse
import hashlib
import json
from pathlib import Path


LIBRARY = Path("/branch_core.sage")
FULL_IDENTITY = Path("/full_identity.json")


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
    parser.add_argument("--target", choices=("R02", "R20"), required=True)
    parser.add_argument("--j-factor-index", type=int, choices=(0, 1, 2, 3), required=True)
    parser.add_argument("--prime", type=int, default=2130706433)
    args = parser.parse_args()
    cell = f"F04-{args.target}"
    qslice_factor_index = 0 if args.target == "R02" else 1
    print(
        canonical_json(
            {
                "phase": "START",
                "cell": cell,
                "qslice_factor_index": qslice_factor_index,
                "j_factor_index": args.j_factor_index,
            }
        ),
        flush=True,
    )

    library = load_library()
    branch = library["build_branch"](cell)
    base = branch["base"]
    r_factors = [
        record["factor"]
        for record in branch["factors"]["R"]
        if not record["named_unit_factor"]
    ]
    assert len(r_factors) == 3
    qslice_factor = r_factors[qslice_factor_index]

    full_data = json.loads(FULL_IDENTITY.read_text())
    row = full_data["results"][0]
    assert row["assignment"] == "F04" and row["status"] == "PASS"
    done = next(record for record in row["records"] if record.get("phase") == "DONE")
    factor_records = done["identities"]["J"]["descended_factors"]
    nonunit_records = [record for record in factor_records if record["metric"]["degree"] > 1]
    assert len(nonunit_records) == 4
    selected_record = nonunit_records[args.j_factor_index]
    assert selected_record["polynomial"] is not None

    qring = PolynomialRing(QQ, names=("x", "s", "p", "w"), order="degrevlex")
    j_factor = qring(selected_record["polynomial"])
    univariate = PolynomialRing(base, "w")
    w = univariate.gen()

    def to_univariate(value):
        output = univariate(0)
        for monomial, coefficient in qring(value).dict().items():
            output += (
                QQ(coefficient)
                * prod(
                    generator ** exponent
                    for generator, exponent in zip(base.gens(), monomial[:3])
                )
                * w ** monomial[3]
            )
        return output

    U = branch["equations"]["U"]
    V = branch["equations"]["V"]
    j_univariate = to_univariate(j_factor)
    degree = int(j_univariate.degree())
    transformed = base(
        sum(
            j_univariate[index] * (-U) ** index * V ** (degree - index)
            for index in range(degree + 1)
        )
    )
    essential_j = base(1)
    transformed_factors = []
    for factor, exponent in transformed.factor():
        named = normalized_key(factor) in branch["unit_keys"]
        transformed_factors.append(
            {
                "degree": int(factor.total_degree()),
                "terms": int(len(factor.monomials())),
                "sha256": digest(factor),
                "exponent": int(exponent),
                "named_unit_factor": named,
            }
        )
        if not named:
            essential_j *= factor ** exponent
    essential_j = base(essential_j)
    print(
        canonical_json(
            {
                "phase": "TRANSFORMED_J",
                "source_factor": {
                    "degree": selected_record["metric"]["degree"],
                    "terms": selected_record["metric"]["terms"],
                    "sha256": selected_record["metric"]["sha256"],
                },
                "transformed_degree": int(transformed.total_degree()),
                "transformed_terms": int(len(transformed.monomials())),
                "transformed_sha256": digest(transformed),
                "factors": transformed_factors,
                "essential_degree": int(essential_j.total_degree()),
                "essential_terms": int(len(essential_j.monomials())),
                "essential_sha256": digest(essential_j),
            }
        ),
        flush=True,
    )

    if essential_j.is_constant():
        result = {
            "phase": "DONE",
            "cell": cell,
            "qslice_factor_index": qslice_factor_index,
            "j_factor_index": args.j_factor_index,
            "terminal": "FULL_J_FACTOR_IS_GENERIC_UNIT",
            "localizer_nilpotence_index": 1,
        }
        print(canonical_json(result), flush=True)
        return

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

    generators = [
        convert(qslice_factor),
        convert(branch["essential"]["E2"]),
        convert(branch["essential"]["E3"]),
        convert(essential_j),
    ]
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
    if not unit_ideal and localizer:
        current = localizer
        for exponent in range(2, 5):
            current = (current * localizer).reduce(basis)
            print(
                canonical_json(
                    {
                        "phase": "LOCALIZER_POWER",
                        "exponent": int(exponent),
                        "zero": not bool(current),
                    }
                ),
                flush=True,
            )
            if not current:
                nilpotence_index = int(exponent)
                break

    result = {
        "phase": "DONE",
        "cell": cell,
        "qslice_factor_index": qslice_factor_index,
        "j_factor_index": args.j_factor_index,
        "basis_size": len(basis),
        "basis_sha256": digest("\n".join(str(value) for value in basis)),
        "dimension": dimension,
        "localizer_steps": steps,
        "localizer_nilpotence_index": nilpotence_index,
        "terminal": (
            "FULL_J_FACTOR_INTERSECTION_EMPTY"
            if nilpotence_index is not None
            else "FULL_J_FACTOR_INTERSECTION_SURVIVES"
        ),
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
