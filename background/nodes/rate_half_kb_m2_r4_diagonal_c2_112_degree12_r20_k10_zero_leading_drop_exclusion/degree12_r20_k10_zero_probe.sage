#!/usr/bin/env sage
"""Test the R20 degree-12 K10-zero leading-drop branch."""

import argparse
import hashlib
import json
from pathlib import Path


LIBRARY = Path("/branch_core.sage")
GENERIC_HELPER = Path("/generic_block_analysis.sage")


def load_library():
    namespace = dict(globals())
    namespace.update({"__name__": "branch_core_library", "__file__": str(LIBRARY)})
    raw = LIBRARY.read_text()
    exec(compile(raw, str(LIBRARY), "exec"), namespace)
    return namespace


def load_generic_helper():
    namespace = dict(globals())
    namespace.update(
        {"__name__": "generic_block_analysis", "__file__": str(GENERIC_HELPER)}
    )
    raw = GENERIC_HELPER.read_text()
    exec(compile(raw, str(GENERIC_HELPER), "exec"), namespace)
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
        choices=("F04-R20", "F05-R20", "F06-R20", "F07-R20"),
        required=True,
    )
    parser.add_argument("--generic-block", action="store_true")
    parser.add_argument("--linear-drop", action="store_true")
    parser.add_argument("--linear-source", action="store_true")
    args = parser.parse_args()
    print(canonical_json({"phase": "START", "cell": args.cell}), flush=True)

    library = load_library()
    branch = library["build_branch"](args.cell)
    base = branch["base"]
    x, s, p = base.gens()
    b0 = branch["converted"][1]
    U = base(branch["equations"]["U"])
    V = base(branch["equations"]["V"])

    def metric(value):
        value = value.parent()(value)
        generators = value.parent().gens()
        return {
            "degree": int(value.total_degree()) if value else -1,
            "degrees": [int(value.degree(generator)) for generator in generators],
            "terms": int(len(value.monomials())) if value else 0,
            "sha256": digest(value),
        }

    b0_leading = base(b0.leading_coefficient())
    leading_records = []
    nonnamed = []
    for factor, exponent in b0_leading.factor():
        is_named = library["normalized_key"](factor) in branch["unit_keys"]
        leading_records.append(
            {
                **metric(factor),
                "exponent": int(exponent),
                "named_unit_factor": is_named,
            }
        )
        if not is_named:
            nonnamed.extend([base(factor)] * int(exponent))
    assert len(nonnamed) == 1
    K10 = nonnamed[0]
    assert K10.total_degree() == 10

    r_factors = [
        record["factor"]
        for record in branch["factors"]["R"]
        if not record["named_unit_factor"]
    ]
    assert [factor.total_degree() for factor in r_factors] == [3, 3, 12]
    selected = base(r_factors[2])
    selected_degree_x = int(selected.degree(x))
    selected_leading = base(
        sum(
            QQ(coefficient) * s ** monomial[1] * p ** monomial[2]
            for monomial, coefficient in selected.dict().items()
            if monomial[0] == selected_degree_x
        )
    )
    degree6_values = [
        factor
        for factor, _ in selected_leading.factor()
        if factor.total_degree() == 6
    ]
    assert len(degree6_values) == 1
    L6 = base(degree6_values[0])
    print(
        canonical_json(
            {
                "phase": "SOURCE_COMPILED",
                "selected": metric(selected),
                "L6": metric(L6),
                "K10": metric(K10),
                "B0_leading": metric(b0_leading),
                "B0_leading_factors": leading_records,
                "unit_factor_count": len(branch["unit_factors"]),
            }
        ),
        flush=True,
    )

    b0_coefficients = [base(value) for value in b0.list()]
    assert len(b0_coefficients) == 3
    linear_drop_determinant = base(
        V * b0_coefficients[0] - U * b0_coefficients[1]
    )

    field = GF(2130706433)
    ring = PolynomialRing(field, names=("x", "s", "pvar"), order="degrevlex")
    rx, rs, rp = ring.gens()

    def convert(value):
        output = ring(0)
        for monomial, coefficient in base(value).dict().items():
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += (
                reduced
                * rx ** monomial[0]
                * rs ** monomial[1]
                * rp ** monomial[2]
            )
        return output

    converted_selected = convert(selected)
    converted_k10 = convert(K10)
    converted_linear_drop = convert(linear_drop_determinant).reduce(
        [converted_k10]
    )
    linear_source_records = {}
    linear_source_cores = []
    for name, row in zip(("A1", "B1"), branch["converted"][2:]):
        degree = int(row.degree())
        cleared_rational = base(
            sum(
                base(row[index])
                * (-b0_coefficients[0]) ** index
                * b0_coefficients[1] ** (degree - index)
                for index in range(degree + 1)
            )
        ).reduce([K10])
        core_rational = base(cleared_rational)
        removed_units = []
        for unit_index, unit in enumerate(branch["unit_factors"], start=1):
            exponent = 0
            while core_rational:
                quotient, remainder = core_rational.quo_rem(base(unit))
                if remainder:
                    break
                core_rational = base(quotient)
                exponent += 1
            if exponent:
                removed_units.append(
                    {"index": unit_index, "exponent": exponent, "unit": metric(unit)}
                )
        cleared = convert(cleared_rational)
        core = convert(core_rational)
        linear_source_records[name] = {
            "degree_w": degree,
            "cleared_reduced": metric(cleared_rational),
            "core": metric(core_rational),
            "removed_units": removed_units,
        }
        if core:
            linear_source_cores.append(core)

    generators = [converted_selected, converted_k10]
    if args.linear_drop:
        assert converted_linear_drop
        generators.append(converted_linear_drop)
    if args.linear_source:
        assert len(linear_source_cores) == 2
        generators.extend(linear_source_cores)
    print(
        canonical_json(
            {
                "phase": "GROEBNER_BEGIN",
                "generators": [
                    {
                        "degree": int(value.total_degree()) if value else -1,
                        "degrees": [
                            int(value.degree(generator))
                            for generator in ring.gens()
                        ],
                        "terms": int(len(value.monomials())) if value else 0,
                        "sha256": digest(value),
                    }
                    for value in generators
                ],
                "linear_drop_source": metric(linear_drop_determinant),
                "linear_drop_reduced": {
                    "degree": int(converted_linear_drop.total_degree()),
                    "degrees": [
                        int(converted_linear_drop.degree(generator))
                        for generator in ring.gens()
                    ],
                    "terms": int(len(converted_linear_drop.monomials())),
                    "sha256": digest(converted_linear_drop),
                },
                "linear_source": linear_source_records,
            }
        ),
        flush=True,
    )
    basis = list(
        ring.ideal(generators).groebner_basis(algorithm="singular:slimgb")
    )
    unit_ideal = basis == [ring(1)]
    dimension = -1 if unit_ideal else int(ring.ideal(basis).dimension())
    print(
        canonical_json(
            {
                "phase": "GROEBNER_DONE",
                "basis_size": len(basis),
                "basis_sha256": digest("\n".join(str(value) for value in basis)),
                "dimension": dimension,
                "unit_ideal": unit_ideal,
            }
        ),
        flush=True,
    )

    open_values = [("prior_s", s), ("prior_L6", L6)]
    open_values.extend(
        (f"unit_{index}", value)
        for index, value in enumerate(branch["unit_factors"], start=1)
    )
    localizer = ring(1)
    localizer_steps = []
    if not unit_ideal:
        for index, (label, value) in enumerate(open_values, start=1):
            localizer = (localizer * convert(value)).reduce(basis)
            event = {
                "index": index,
                "label": label,
                "zero": not bool(localizer),
                "terms": int(len(localizer.monomials())) if localizer else 0,
                "sha256": digest(localizer),
            }
            localizer_steps.append(event)
            print(canonical_json({"phase": "LOCALIZER_STEP", **event}), flush=True)
            if not localizer:
                break

    saturation_unit = unit_ideal or not bool(localizer)
    saturation_basis = [ring(1)] if saturation_unit else []
    saturation_dimension = -1 if saturation_unit else None
    if not saturation_unit:
        saturation_ring = PolynomialRing(
            field,
            names=("inverse", "x", "s", "pvar"),
            order="degrevlex",
        )
        inverse, sx, ss, sp = saturation_ring.gens()

        def to_saturation(value):
            return saturation_ring(
                sum(
                    field(coefficient)
                    * sx ** monomial[0]
                    * ss ** monomial[1]
                    * sp ** monomial[2]
                    for monomial, coefficient in ring(value).dict().items()
                )
            )

        print(canonical_json({"phase": "SATURATION_BEGIN"}), flush=True)
        saturation_basis = list(
            saturation_ring.ideal(
                [to_saturation(value) for value in basis]
                + [inverse * to_saturation(localizer) - 1]
            ).groebner_basis(algorithm="singular:slimgb")
        )
        saturation_unit = saturation_basis == [saturation_ring(1)]
        saturation_dimension = (
            -1
            if saturation_unit
            else int(saturation_ring.ideal(saturation_basis).dimension())
        )
        print(
            canonical_json(
                {
                    "phase": "SATURATION_DONE",
                    "unit_ideal": saturation_unit,
                    "basis_size": len(saturation_basis),
                    "basis_sha256": digest(
                        "\n".join(str(value) for value in saturation_basis)
                    ),
                    "dimension": saturation_dimension,
                }
            ),
            flush=True,
        )

    generic_record = None
    if not saturation_unit and args.generic_block:
        helper = load_generic_helper()
        generic_record = helper["analyze_generic_block"](
            field,
            saturation_ring,
            saturation_basis,
            2,
            digest,
            canonical_json,
        )

    result = {
        "phase": "DONE",
        "cell": args.cell,
        "linear_drop": args.linear_drop,
        "linear_source": args.linear_source,
        "basis_size": len(basis),
        "basis_sha256": digest("\n".join(str(value) for value in basis)),
        "dimension": dimension,
        "unit_ideal": unit_ideal,
        "localizer_steps": localizer_steps,
        "saturation_unit_ideal": saturation_unit,
        "saturation_basis_size": len(saturation_basis),
        "saturation_basis_sha256": digest(
            "\n".join(str(value) for value in saturation_basis)
        ),
        "saturation_dimension": saturation_dimension,
        "generic_block": generic_record,
        "terminal": "K10_ZERO_BRANCH_EMPTY" if saturation_unit else "K10_ZERO_BRANCH_SURVIVES",
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
