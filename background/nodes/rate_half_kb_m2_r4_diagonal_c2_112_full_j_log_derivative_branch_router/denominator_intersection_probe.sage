#!/usr/bin/env sage
"""Intersect cubic/J11 routes with symmetric logarithmic denominator unions."""

import argparse
import hashlib
import json
from pathlib import Path


LIBRARY = Path("/branch_core.sage")
FULL_IDENTITY = Path("/full_identity.json")
LOG_DERIVATIVE = Path("/log_derivative.json")


def load_library():
    namespace = dict(globals())
    namespace.update({"__name__": "branch_core_library", "__file__": str(LIBRARY)})
    exec(compile(LIBRARY.read_text(), str(LIBRARY), "exec"), namespace)
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
    parser.add_argument("--target", choices=("R02", "R20"), required=True)
    parser.add_argument("--pair-index", type=int, choices=(0, 1), required=True)
    parser.add_argument("--prime", type=int, default=2130706433)
    args = parser.parse_args()
    cell = f"F04-{args.target}"
    qslice_factor_index = 0 if args.target == "R02" else 1
    print(
        canonical_json(
            {
                "phase": "START",
                "cell": cell,
                "pair_index": args.pair_index,
            }
        ),
        flush=True,
    )

    library = load_library()
    frontier = library["load_frontier"]()
    parent = frontier["PARENT"]
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
    full_row = full_data["results"][0]
    full_done = next(
        record for record in full_row["records"] if record.get("phase") == "DONE"
    )
    full_factors = full_done["identities"]["J"]["descended_factors"]
    nonunit_full = [
        record for record in full_factors if record["metric"]["degree"] > 1
    ]
    assert [record["metric"]["degree"] for record in nonunit_full] == [8, 8, 11, 12]
    j11_record = nonunit_full[2]
    assert j11_record["polynomial"] is not None

    log_data = json.loads(LOG_DERIVATIVE.read_text())
    log_row = log_data["results"][0]
    compiled = next(
        record
        for record in log_row["records"]
        if record.get("phase") == "LOG_DERIVATIVE_COMPILED"
    )
    denominator_factors = [
        record
        for record in compiled["denominator_factors"]
        if not record["named_unit"]
    ]
    assert [record["metric"]["degree"] for record in denominator_factors] == [
        7,
        7,
        11,
        11,
    ]
    selected_records = denominator_factors[2 * args.pair_index : 2 * args.pair_index + 2]
    assert all(record["polynomial"] is not None for record in selected_records)
    source_ring = parent["R"]
    source_pair = source_ring.prod(
        source_ring(record["polynomial"]) for record in selected_records
    )
    descended_pair = parent["symmetric_cd_dict"](source_pair)

    qring = PolynomialRing(QQ, names=("x", "s", "p", "w"), order="degrevlex")
    descended_pair = qring(descended_pair)
    j11 = qring(j11_record["polynomial"])
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

    def reconstruct(value):
        value = to_univariate(value)
        degree = int(value.degree())
        return base(
            sum(
                value[index] * (-U) ** index * V ** (degree - index)
                for index in range(degree + 1)
            )
        )

    def essential(value):
        output = base(1)
        records = []
        for factor, exponent in base(value).factor():
            named = library["normalized_key"](factor) in branch["unit_keys"]
            records.append(
                {
                    "degree": int(factor.total_degree()),
                    "terms": int(len(factor.monomials())),
                    "sha256": digest(factor),
                    "exponent": int(exponent),
                    "named_unit_factor": named,
                }
            )
            if not named:
                output *= factor ** exponent
        return base(output), records

    transformed_pair = reconstruct(descended_pair)
    transformed_j11 = reconstruct(j11)
    essential_pair, pair_factors = essential(transformed_pair)
    essential_j11, j11_factors = essential(transformed_j11)

    def metric(value):
        value = value.parent()(value)
        return {
            "degree": int(value.total_degree()) if value else -1,
            "degrees": [int(value.degree(generator)) for generator in value.parent().gens()],
            "terms": int(len(value.monomials())) if value else 0,
            "sha256": digest(value),
        }

    print(
        canonical_json(
            {
                "phase": "BRANCH_COMPILED",
                "source_degrees": [record["metric"]["degree"] for record in selected_records],
                "source_pair": parent["metric"](source_pair),
                "descended_pair": metric(descended_pair),
                "transformed_pair": metric(transformed_pair),
                "pair_factors": pair_factors,
                "essential_pair": metric(essential_pair),
                "j11_factors": j11_factors,
                "essential_j11": metric(essential_j11),
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

    generators = [
        convert(qslice_factor),
        convert(branch["essential"]["E2"]),
        convert(branch["essential"]["E3"]),
        convert(essential_j11),
        convert(essential_pair),
    ]
    print(canonical_json({"phase": "GROEBNER_BEGIN"}), flush=True)
    basis = list(ring.ideal(generators).groebner_basis(algorithm="singular:slimgb"))
    unit_ideal = basis == [ring(1)]
    dimension = -1 if unit_ideal else int(ring.ideal(basis).dimension())
    localizer = ring(1)
    steps = []
    nilpotence_index = 1 if unit_ideal else None
    if not unit_ideal:
        for index, factor in enumerate(branch["unit_factors"], start=1):
            localizer = (localizer * convert(factor)).reduce(basis)
            step = {
                "index": index,
                "zero": not bool(localizer),
                "degree": int(localizer.total_degree()) if localizer else None,
                "terms": int(len(localizer.monomials())) if localizer else None,
                "sha256": digest(localizer),
            }
            steps.append(step)
            if not localizer:
                nilpotence_index = 1
                break
    result = {
        "phase": "DONE",
        "cell": cell,
        "pair_index": args.pair_index,
        "source_degrees": [record["metric"]["degree"] for record in selected_records],
        "basis_size": len(basis),
        "basis_sha256": digest("\n".join(str(value) for value in basis)),
        "dimension": dimension,
        "unit_ideal": unit_ideal,
        "localizer_steps": steps,
        "localizer_nilpotence_index": nilpotence_index,
        "terminal": (
            "FULL_J_LOG_DENOMINATOR_UNION_EMPTY"
            if nilpotence_index is not None
            else "FULL_J_LOG_DENOMINATOR_UNION_SURVIVES"
        ),
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
