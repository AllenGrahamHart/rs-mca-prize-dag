#!/usr/bin/env sage
"""Intersect the guarded full-J logarithmic numerator with an F04 route."""

import argparse
import hashlib
import json
from pathlib import Path


LIBRARY = Path("/branch_core.sage")
FULL_IDENTITY = Path("/full_identity.json")


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


def metric(value, generators=None):
    value = value.parent()(value)
    generators = value.parent().gens() if generators is None else generators
    return {
        "degree": int(value.total_degree()) if value else -1,
        "degrees": [int(value.degree(generator)) for generator in generators],
        "terms": int(len(value.monomials())) if value else 0,
        "sha256": digest(value),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--assignment",
        choices=("F04", "F05", "F06", "F07"),
        default="F04",
    )
    parser.add_argument("--target", choices=("R02", "R20"), required=True)
    parser.add_argument("--prime", type=int, default=2130706433)
    args = parser.parse_args()
    cell = f"{args.assignment}-{args.target}"
    qslice_factor_index = 0 if args.target == "R02" else 1
    print(canonical_json({"phase": "START", "cell": cell}), flush=True)

    library = load_library()
    frontier = library["load_frontier"]()
    parent = frontier["PARENT"]
    atlas = parent["ATLAS"]
    source_u, source_v, source_z = parent["build_source_R"](args.assignment)
    source_ring = parent["R"]
    source_field = parent["K"]
    polynomial_w = atlas["KW"]
    W = atlas["W"]
    b, c, d, w_source = map(source_field, source_ring.gens())

    def g_at(label):
        uu = sum(
            polynomial_w(source_u[index]) * source_field(label) ** index
            for index in range(3)
        )
        vv = sum(
            polynomial_w(source_v[index]) * source_field(label) ** index
            for index in range(3)
        )
        return polynomial_w(uu ** 2 - W * vv ** 2)

    observed_labels = (source_field(2), source_field(1) / 2, b, 1 / b, c, d)
    expected_labels = (w_source, source_z, 1 / source_z, 1 / c, 1 / d)
    observed_log = source_field(0)
    for label in observed_labels:
        factor = g_at(label)
        assert factor[0]
        observed_log += source_field(factor[1]) / source_field(factor[0])
    expected_log = -4 * sum(1 / source_field(label) for label in expected_labels)
    expected_log -= 2 / c + 2 / d
    mismatch = source_field(observed_log - expected_log)
    numerator = parent["primitive_R"](mismatch.numerator())
    units = parent["named_units_R"](args.assignment)
    essential, _ = parent["essential"](numerator, units)
    descended = parent["symmetric_cd_dict"](essential)
    print(
        canonical_json(
            {
                "phase": "NUMERATOR_COMPILED",
                "raw": parent["metric"](numerator),
                "descended": metric(descended),
            }
        ),
        flush=True,
    )
    if args.assignment == "F04":
        assert metric(descended)["sha256"] == (
            "57f0d18de937af8c9bebb7e59b079861571ecd9cdf156f3fa4d0ab574331437e"
        )

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
    full_row = next(
        row for row in full_data["results"] if row["assignment"] == args.assignment
    )
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

    qring = PolynomialRing(QQ, names=("x", "s", "p", "w"), order="degrevlex")
    j11 = qring(j11_record["polynomial"])
    descended = qring(descended)
    base_univariate = PolynomialRing(base, "w")
    base_w = base_univariate.gen()

    def to_base_univariate(value):
        output = base_univariate(0)
        for monomial, coefficient in qring(value).dict().items():
            output += (
                QQ(coefficient)
                * prod(
                    generator ** exponent
                    for generator, exponent in zip(base.gens(), monomial[:3])
                )
                * base_w ** monomial[3]
            )
        return output

    U = branch["equations"]["U"]
    V = branch["equations"]["V"]
    j11_univariate = to_base_univariate(j11)
    j11_degree = int(j11_univariate.degree())
    transformed_j11 = base(
        sum(
            j11_univariate[index] * (-U) ** index * V ** (j11_degree - index)
            for index in range(j11_degree + 1)
        )
    )
    essential_j11 = base(1)
    for factor, exponent in transformed_j11.factor():
        if library["normalized_key"](factor) not in branch["unit_keys"]:
            essential_j11 *= factor ** exponent
    essential_j11 = base(essential_j11)

    field = GF(ZZ(args.prime))
    ring = PolynomialRing(field, names=("x", "s", "p"), order="degrevlex")

    def convert_base(value):
        output = ring(0)
        for monomial, coefficient in base(value).dict().items():
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += reduced * prod(
                generator ** exponent
                for generator, exponent in zip(ring.gens(), monomial)
            )
        return output

    route_generators = [
        convert_base(qslice_factor),
        convert_base(branch["essential"]["E2"]),
        convert_base(branch["essential"]["E3"]),
        convert_base(essential_j11),
    ]
    print(canonical_json({"phase": "BASE_GROEBNER_BEGIN"}), flush=True)
    route_basis = list(
        ring.ideal(route_generators).groebner_basis(algorithm="singular:slimgb")
    )
    assert route_basis != [ring(1)]
    assert int(ring.ideal(route_basis).dimension()) == 1
    route_hash = digest("\n".join(str(value) for value in route_basis))
    print(
        canonical_json(
            {
                "phase": "BASE_GROEBNER_DONE",
                "basis_size": len(route_basis),
                "basis_sha256": route_hash,
                "dimension": 1,
            }
        ),
        flush=True,
    )

    def normal(value):
        return ring(value).reduce(route_basis)

    numerator_univariate = to_base_univariate(descended)
    numerator_degree = int(numerator_univariate.degree())
    assert numerator_degree == 15
    coefficients = [
        normal(convert_base(numerator_univariate[index]))
        for index in range(numerator_degree + 1)
    ]
    reduced_u = normal(convert_base(U))
    reduced_v = normal(convert_base(V))
    value = coefficients[-1]
    v_power = ring(1)
    steps = []
    for index in reversed(range(numerator_degree)):
        v_power = normal(v_power * reduced_v)
        value = normal(value * (-reduced_u) + coefficients[index] * v_power)
        step = {
            "coefficient_index": index,
            "degree": int(value.total_degree()) if value else -1,
            "terms": int(len(value.monomials())) if value else 0,
            "sha256": digest(value),
            "zero": not bool(value),
        }
        steps.append(step)
        print(canonical_json({"phase": "HORNER_STEP", **step}), flush=True)

    reconstructed = value
    print(
        canonical_json(
            {
                "phase": "NUMERATOR_REDUCED",
                "numerator_w_degree": numerator_degree,
                "remainder": metric(reconstructed),
            }
        ),
        flush=True,
    )
    if reconstructed:
        final_basis = list(
            ring.ideal([*route_generators, reconstructed]).groebner_basis(
                algorithm="singular:slimgb"
            )
        )
    else:
        final_basis = route_basis
    unit_ideal = final_basis == [ring(1)]
    dimension = -1 if unit_ideal else int(ring.ideal(final_basis).dimension())
    localizer = ring(1)
    localizer_steps = []
    nilpotence_index = 1 if unit_ideal else None
    if not unit_ideal:
        for index, factor in enumerate(branch["unit_factors"], start=1):
            localizer = (localizer * convert_base(factor)).reduce(final_basis)
            step = {
                "index": index,
                "zero": not bool(localizer),
                "degree": int(localizer.total_degree()) if localizer else None,
                "terms": int(len(localizer.monomials())) if localizer else None,
                "sha256": digest(localizer),
            }
            localizer_steps.append(step)
            if not localizer:
                nilpotence_index = 1
                break
    result = {
        "phase": "DONE",
        "cell": cell,
        "numerator_w_degree": numerator_degree,
        "route_basis_size": len(route_basis),
        "route_basis_sha256": route_hash,
        "numerator_remainder": metric(reconstructed),
        "basis_size": len(final_basis),
        "basis_sha256": digest("\n".join(str(value) for value in final_basis)),
        "dimension": dimension,
        "unit_ideal": unit_ideal,
        "localizer_steps": localizer_steps,
        "localizer_nilpotence_index": nilpotence_index,
        "terminal": (
            "FULL_J_LOG_GUARDED_NUMERATOR_INTERSECTION_EMPTY"
            if nilpotence_index is not None
            else "FULL_J_LOG_GUARDED_NUMERATOR_INTERSECTION_SURVIVES"
        ),
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
