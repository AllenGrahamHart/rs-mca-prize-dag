#!/usr/bin/env sage
"""Compress remaining rows through a quadratic pseudo-remainder in w."""

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
    parser.add_argument("--cell", default="F04-R02")
    parser.add_argument("--divisor", choices=("A0", "B0"), required=True)
    parser.add_argument("--groebner", action="store_true")
    parser.add_argument("--global-saturation", action="store_true")
    parser.add_argument("--skip-elimination", action="store_true")
    parser.add_argument("--fiber-search", action="store_true")
    parser.add_argument("--factor-fibers", action="store_true")
    parser.add_argument("--fiber-start", type=int, default=1)
    parser.add_argument("--fiber-limit", type=int, default=16)
    parser.add_argument("--field-degree", type=int, default=1)
    args = parser.parse_args()
    print(
        canonical_json(
            {"phase": "START", "cell": args.cell, "divisor": args.divisor}
        ),
        flush=True,
    )

    library = load_library()
    branch = library["build_branch"](args.cell)
    base = branch["base"]
    x, s, p = base.gens()
    rows = branch["converted"]
    divisor_index = 0 if args.divisor == "A0" else 1
    divisor = rows[divisor_index]
    remaining = {"A1": rows[2], "B1": rows[3]}
    U = branch["equations"]["U"]
    V = branch["equations"]["V"]

    def base_metric(value):
        value = base(value)
        return {
            "degree": int(value.total_degree()) if value else -1,
            "degrees": [int(value.degree(generator)) for generator in (x, s, p)],
            "terms": int(len(value.monomials())) if value else 0,
            "sha256": digest(value),
        }

    def w_metric(value):
        value = value.parent()(value)
        coefficients = [base(coefficient) for coefficient in value.list() if coefficient]
        return {
            "degree_w": int(value.degree()) if value else -1,
            "coefficients": len(coefficients),
            "terms": sum(len(coefficient.monomials()) for coefficient in coefficients),
            "max_coefficient_degree": max(
                (coefficient.total_degree() for coefficient in coefficients), default=-1
            ),
            "sha256": digest(value),
        }

    leading = base(divisor.leading_coefficient())
    leading_factors = []
    leading_nonnamed_keys = set()
    leading_nonnamed_values = []
    for factor, exponent in leading.factor():
        named = library["normalized_key"](factor) in branch["unit_keys"]
        if not named:
            leading_nonnamed_keys.add(library["normalized_key"](factor))
            leading_nonnamed_values.extend([factor] * int(exponent))
        leading_factors.append(
            {
                "degree": int(factor.total_degree()),
                "terms": int(len(factor.monomials())),
                "exponent": int(exponent),
                "sha256": digest(factor),
                "named_unit_factor": named,
            }
        )
    print(
        canonical_json(
            {
                "phase": "SOURCE",
                "divisor": w_metric(divisor),
                "divisor_leading": base_metric(leading),
                "divisor_leading_factors": leading_factors,
                "remaining": {name: w_metric(value) for name, value in remaining.items()},
                "blocks": {"U": base_metric(U), "V": base_metric(V)},
            }
        ),
        flush=True,
    )

    def pseudo_remainder(name, polynomial):
        current = polynomial.parent()(polynomial)
        quotient = polynomial.parent()(0)
        multiplier = base(1)
        divisor_degree = int(divisor.degree())
        steps = []
        while current and current.degree() >= divisor_degree:
            old_degree = int(current.degree())
            coefficient = base(current[old_degree])
            shift = old_degree - divisor_degree
            current = polynomial.parent()(leading * current - coefficient * polynomial.parent().gen() ** shift * divisor)
            quotient = polynomial.parent()(leading * quotient + coefficient * polynomial.parent().gen() ** shift)
            multiplier = base(multiplier * leading)
            assert not current or current.degree() < old_degree
            steps.append(w_metric(current))
            print(
                canonical_json(
                    {
                        "phase": "PSEUDO_STEP",
                        "name": name,
                        "step": len(steps),
                        "metric": steps[-1],
                    }
                ),
                flush=True,
            )
        assert polynomial.parent()(multiplier * polynomial - quotient * divisor) == current
        return current, multiplier, quotient, steps

    records = {}
    for name, polynomial in remaining.items():
        remainder, multiplier, quotient, steps = pseudo_remainder(name, polynomial)
        r0 = base(remainder[0]) if remainder else base(0)
        r1 = base(remainder[1]) if remainder.degree() >= 1 else base(0)
        determinant = base(V * r0 - U * r1)
        records[name] = {
            "input_degree": int(polynomial.degree()),
            "pseudo_exponent": len(steps),
            "remainder": w_metric(remainder),
            "multiplier": base_metric(multiplier),
            "quotient": w_metric(quotient),
            "determinant_value": determinant,
            "determinant": base_metric(determinant),
        }
        print(
            canonical_json(
                {
                    "phase": "DETERMINANT",
                    "name": name,
                    **{key: value for key, value in records[name].items() if key != "determinant_value"},
                }
            ),
            flush=True,
        )

    for name, record in records.items():
        print(canonical_json({"phase": "FACTOR_BEGIN", "name": name}), flush=True)
        factor_records = []
        essential = base(1)
        core = base(1)
        for factor, exponent in record["determinant_value"].factor():
            key = library["normalized_key"](factor)
            named = key in branch["unit_keys"]
            factor_records.append(
                {
                    "degree": int(factor.total_degree()),
                    "degrees": [int(factor.degree(generator)) for generator in (x, s, p)],
                    "terms": int(len(factor.monomials())),
                    "exponent": int(exponent),
                    "sha256": digest(factor),
                    "named_unit_factor": named,
                }
            )
            if not named:
                essential *= factor ** exponent
                if key not in leading_nonnamed_keys:
                    core *= factor ** exponent
        record["factors"] = factor_records
        record["essential"] = base_metric(essential)
        record["core_value"] = base(core)
        record["core"] = base_metric(core)
        print(
            canonical_json(
                {
                    "phase": "FACTOR_DONE",
                    "name": name,
                    "factors": factor_records,
                    "essential": record["essential"],
                    "core": record["core"],
                }
            ),
            flush=True,
        )

    groebner_record = None
    if args.groebner:
        assert leading_nonnamed_values
        r_factors = [
            record["factor"]
            for record in branch["factors"]["R"]
            if not record["named_unit_factor"]
        ]
        selected = r_factors[2]
        selected_degree_x = int(selected.degree(x))
        selected_leading = base(
            sum(
                QQ(coefficient) * s ** monomial[1] * p ** monomial[2]
                for monomial, coefficient in selected.dict().items()
                if monomial[0] == selected_degree_x
            )
        )
        degree6_values = [
            factor for factor, _ in selected_leading.factor()
            if factor.total_degree() == 6
        ]
        assert len(degree6_values) == 1
        degree6 = degree6_values[0]

        field = GF(2130706433)
        ring = PolynomialRing(field, names=("x", "s", "p"), order="degrevlex")
        rx, rs, rp = ring.gens()

        def convert(value):
            output = ring(0)
            for monomial, coefficient in base(value).dict().items():
                coefficient = QQ(coefficient)
                reduced = field(coefficient.numerator()) / field(coefficient.denominator())
                output += reduced * rx ** monomial[0] * rs ** monomial[1] * rp ** monomial[2]
            return output

        generators = [convert(selected), convert(records["A1"]["core_value"]), convert(records["B1"]["core_value"])]
        print(
            canonical_json(
                {
                    "phase": "GROEBNER_BEGIN",
                    "generators": [
                        {
                            "degree": int(value.total_degree()),
                            "degrees": [int(value.degree(generator)) for generator in (rx, rs, rp)],
                            "terms": int(len(value.monomials())),
                            "sha256": digest(value),
                        }
                        for value in generators
                    ],
                }
            ),
            flush=True,
        )
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
        localizer_factors = [("prior_s", ring(rs)), ("prior_L6", convert(degree6))]
        localizer_factors.extend(
            (f"chart_{index}", convert(value))
            for index, value in enumerate(leading_nonnamed_values, start=1)
        )
        localizer_factors.extend(
            (f"unit_{index}", convert(value))
            for index, value in enumerate(branch["unit_factors"], start=1)
        )
        localizer = ring(1)
        localizer_steps = []
        nilpotence_index = 1 if unit_ideal else None
        if not unit_ideal:
            for index, (label, factor) in enumerate(localizer_factors, start=1):
                localizer = (localizer * factor).reduce(basis)
                localizer_steps.append(
                    {
                        "index": index,
                        "label": label,
                        "zero": not bool(localizer),
                        "terms": int(len(localizer.monomials())) if localizer else 0,
                        "sha256": digest(localizer),
                    }
                )
                if not localizer:
                    nilpotence_index = 1
                    break
        chart_localizer_steps = []
        chart_nilpotence_index = 1 if unit_ideal else None
        if not unit_ideal:
            chart_localizer = convert(
                V * base.prod(leading_nonnamed_values)
            ).reduce(basis)
            chart_power = ring(1)
            for exponent in range(1, 17):
                chart_power = (chart_power * chart_localizer).reduce(basis)
                event = {
                    "exponent": exponent,
                    "zero": not bool(chart_power),
                    "terms": int(len(chart_power.monomials())) if chart_power else 0,
                    "sha256": digest(chart_power),
                }
                chart_localizer_steps.append(event)
                print(
                    canonical_json(
                        {"phase": "CHART_LOCALIZER_POWER", **event}
                    ),
                    flush=True,
                )
                if not chart_power:
                    chart_nilpotence_index = exponent
                    break
        groebner_record = {
            "basis_size": len(basis),
            "basis_sha256": digest("\n".join(str(value) for value in basis)),
            "dimension": dimension,
            "unit_ideal": unit_ideal,
            "localizer_steps": localizer_steps,
            "localizer_nilpotence_index": nilpotence_index,
            "chart_localizer": "V*K8",
            "chart_localizer_steps": chart_localizer_steps,
            "chart_localizer_nilpotence_index": chart_nilpotence_index,
            "terminal": (
                "QUADRATIC_PSEUDOREMAINDER_CORE_EMPTY"
                if nilpotence_index is not None
                or chart_nilpotence_index is not None
                else "QUADRATIC_PSEUDOREMAINDER_CORE_SURVIVES"
            ),
        }

    global_saturation_record = None
    if args.global_saturation:
        assert args.divisor == "B0"
        assert len(leading_nonnamed_values) == 1
        r_factors = [
            record["factor"]
            for record in branch["factors"]["R"]
            if not record["named_unit_factor"]
        ]
        selected = r_factors[2]
        field = GF(2130706433)
        ring = PolynomialRing(field, names=("x", "s", "pvar"), order="degrevlex")
        rx, rs, rp = ring.gens()

        def convert_global(value):
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

        global_generators = [
            convert_global(selected),
            convert_global(records["A1"]["core_value"]),
            convert_global(records["B1"]["core_value"]),
        ]
        print(canonical_json({"phase": "GLOBAL_BASIS_BEGIN"}), flush=True)
        global_basis = list(
            ring.ideal(global_generators).groebner_basis(
                algorithm="singular:slimgb"
            )
        )
        assert global_basis != [ring(1)]
        print(
            canonical_json(
                {
                    "phase": "GLOBAL_BASIS_DONE",
                    "basis_size": len(global_basis),
                    "dimension": int(ring.ideal(global_basis).dimension()),
                    "basis_sha256": digest(
                        "\n".join(str(value) for value in global_basis)
                    ),
                }
            ),
            flush=True,
        )
        boundary_localizer = convert_global(
            V * leading_nonnamed_values[0] * (s ** 2 - 4 * p)
        ).reduce(global_basis)
        print(
            canonical_json(
                {
                    "phase": "GLOBAL_LOCALIZER_REDUCED",
                    "metric": {
                        "degree": int(boundary_localizer.total_degree()),
                        "degrees": [
                            int(boundary_localizer.degree(generator))
                            for generator in (rx, rs, rp)
                        ],
                        "terms": int(len(boundary_localizer.monomials())),
                        "sha256": digest(boundary_localizer),
                    },
                }
            ),
            flush=True,
        )
        saturation_ring = PolynomialRing(
            field,
            names=("inverse", "x", "pvar", "svar"),
            order="degrevlex",
        )
        inverse, sx, sp, ss = saturation_ring.gens()

        def to_saturation_global(value):
            return saturation_ring(
                sum(
                    field(coefficient)
                    * sx ** monomial[0]
                    * ss ** monomial[1]
                    * sp ** monomial[2]
                    for monomial, coefficient in ring(value).dict().items()
                )
            )

        saturation_ideal = saturation_ring.ideal(
            [to_saturation_global(value) for value in global_basis]
            + [inverse * to_saturation_global(boundary_localizer) - 1]
        )
        print(canonical_json({"phase": "GLOBAL_SATURATION_BEGIN"}), flush=True)
        saturation_basis = list(
            saturation_ideal.groebner_basis(algorithm="singular:slimgb")
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
                    "phase": "GLOBAL_SATURATION_DONE",
                    "unit_ideal": saturation_unit,
                    "dimension": saturation_dimension,
                    "basis_size": len(saturation_basis),
                    "basis_sha256": digest(
                        "\n".join(str(value) for value in saturation_basis)
                    ),
                }
            ),
            flush=True,
        )
        field_basis = saturation_basis
        field_unit = saturation_unit
        field_steps = []
        full_open_steps = []
        full_open_product_zero = saturation_unit
        if not saturation_unit and saturation_dimension == 0:
            def saturation_metric(value):
                value = saturation_ring(value)
                return {
                    "degree": int(value.total_degree()) if value else -1,
                    "degrees": [
                        int(value.degree(generator))
                        for generator in (inverse, sx, sp, ss)
                    ],
                    "terms": int(len(value.monomials())) if value else 0,
                    "sha256": digest(value),
                }

            def saturation_power_reduce(value, exponent):
                result = saturation_ring(1)
                power = saturation_ring(value).reduce(saturation_basis)
                remaining = int(exponent)
                while remaining:
                    if remaining & 1:
                        result = (result * power).reduce(saturation_basis)
                    remaining >>= 1
                    if remaining:
                        power = (power * power).reduce(saturation_basis)
                return saturation_ring(result)

            q = int(field.cardinality())
            frobenius = []
            for name, generator in (("x", sx), ("s", ss), ("pvar", sp)):
                current = saturation_ring(generator)
                for iteration in range(1, 7):
                    current = saturation_power_reduce(current, q)
                    event = {
                        "name": name,
                        "iteration": iteration,
                        "metric": saturation_metric(current),
                    }
                    field_steps.append(event)
                    print(
                        canonical_json({"phase": "GLOBAL_FIELD_STEP", **event}),
                        flush=True,
                    )
                frobenius.append(
                    saturation_ring(current - generator).reduce(saturation_basis)
                )
            print(canonical_json({"phase": "GLOBAL_FIELD_BEGIN"}), flush=True)
            field_basis = list(
                saturation_ring.ideal(
                    saturation_basis + frobenius
                ).groebner_basis(algorithm="singular:slimgb")
            )
            field_unit = field_basis == [saturation_ring(1)]
            print(
                canonical_json(
                    {
                        "phase": "GLOBAL_FIELD_DONE",
                        "unit_ideal": field_unit,
                        "basis_size": len(field_basis),
                        "basis_sha256": digest(
                            "\n".join(str(value) for value in field_basis)
                        ),
                        "frobenius": [
                            saturation_metric(value) for value in frobenius
                        ],
                    }
                ),
                flush=True,
            )
            if not field_unit:
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
                full_open_values = [s, degree6_values[0], leading_nonnamed_values[0]]
                full_open_values.extend(branch["unit_factors"])
                full_open_product = saturation_ring(1)
                for index, value in enumerate(full_open_values, start=1):
                    full_open_product = (
                        full_open_product
                        * to_saturation_global(convert_global(value))
                    ).reduce(field_basis)
                    event = {
                        "index": index,
                        "zero": not bool(full_open_product),
                        "terms": (
                            int(len(full_open_product.monomials()))
                            if full_open_product
                            else 0
                        ),
                        "sha256": digest(full_open_product),
                    }
                    full_open_steps.append(event)
                    print(
                        canonical_json(
                            {"phase": "GLOBAL_FULL_OPEN_STEP", **event}
                        ),
                        flush=True,
                    )
                    if not full_open_product:
                        break
                full_open_product_zero = not bool(full_open_product)
        elimination_records = []
        if not saturation_unit and not args.skip_elimination:
            print(canonical_json({"phase": "GLOBAL_ELIMINATION_BEGIN"}), flush=True)
            elimination = saturation_ring.ideal(
                saturation_basis
            ).elimination_ideal([inverse, sx, sp])
            elimination_basis = list(elimination.groebner_basis())
            for value in elimination_basis:
                assert value.degree(inverse) == 0
                assert value.degree(sx) == 0
                assert value.degree(sp) == 0
                factors = []
                for factor, exponent in value.factor():
                    factor_record = {
                        "degree": int(factor.degree(ss)),
                        "terms": int(len(factor.monomials())),
                        "exponent": int(exponent),
                        "sha256": digest(factor),
                    }
                    if factor.degree(ss) == 1:
                        constant = field(0)
                        linear = field(0)
                        for monomial, coefficient in factor.dict().items():
                            if monomial[3] == 0:
                                constant += field(coefficient)
                            elif monomial[3] == 1:
                                linear += field(coefficient)
                            else:
                                raise AssertionError("nonlinear monomial in linear factor")
                        assert linear
                        factor_record["root"] = int(-constant / linear)
                    factors.append(factor_record)
                elimination_records.append(
                    {
                        "degree": int(value.degree(ss)),
                        "terms": int(len(value.monomials())),
                        "sha256": digest(value),
                        "factors": factors,
                    }
                )
            print(
                canonical_json(
                    {
                        "phase": "GLOBAL_ELIMINATION_DONE",
                        "basis_size": len(elimination_basis),
                        "records": elimination_records,
                    }
                ),
                flush=True,
            )
        global_saturation_record = {
            "global_basis_size": len(global_basis),
            "global_basis_sha256": digest(
                "\n".join(str(value) for value in global_basis)
            ),
            "saturation_unit_ideal": saturation_unit,
            "saturation_dimension": saturation_dimension,
            "saturation_basis_size": len(saturation_basis),
            "saturation_basis_sha256": digest(
                "\n".join(str(value) for value in saturation_basis)
            ),
            "field_extension_degree": 6,
            "field_unit_ideal": field_unit,
            "field_basis_size": len(field_basis),
            "field_basis_sha256": digest(
                "\n".join(str(value) for value in field_basis)
            ),
            "field_steps": field_steps,
            "full_open_steps": full_open_steps,
            "full_open_product_zero": full_open_product_zero,
            "elimination": elimination_records,
            "terminal": (
                "GLOBAL_OPEN_CHART_EMPTY"
                if saturation_unit
                else "GLOBAL_COMPLETE_OPEN_CHART_HAS_NO_F_P6_POINTS"
                if full_open_product_zero
                else "GLOBAL_OPEN_CHART_HAS_NO_F_P6_POINTS"
                if field_unit
                else "GLOBAL_OPEN_CHART_ELIMINATED_TO_S"
                if elimination_records
                else "GLOBAL_OPEN_CHART_DOMINATES_S"
            ),
        }

    fiber_search_record = None
    if args.fiber_search:
        r_factors = [
            record["factor"]
            for record in branch["factors"]["R"]
            if not record["named_unit_factor"]
        ]
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
        degree6 = base(degree6_values[0])
        assert len(leading_nonnamed_values) == 1
        chart_factor = base(leading_nonnamed_values[0])
        affine_source = [
            selected,
            base(records["A1"]["core_value"]),
            base(records["B1"]["core_value"]),
        ]
        field = GF(2130706433)
        fiber_ring = PolynomialRing(
            field, names=("x", "pvar"), order="degrevlex"
        )
        fx, fp = fiber_ring.gens()

        def specialize_s(value, s_value):
            output = fiber_ring(0)
            for monomial, coefficient in base(value).dict().items():
                coefficient = QQ(coefficient)
                reduced = field(coefficient.numerator()) / field(coefficient.denominator())
                output += (
                    reduced
                    * fx ** monomial[0]
                    * field(s_value) ** monomial[1]
                    * fp ** monomial[2]
                )
            return output

        def fiber_metric(value):
            value = fiber_ring(value)
            return {
                "degree": int(value.total_degree()) if value else -1,
                "degrees": [int(value.degree(generator)) for generator in (fx, fp)],
                "terms": int(len(value.monomials())) if value else 0,
                "sha256": digest(value),
            }

        def power_reduce(value, exponent, basis):
            result = fiber_ring(1)
            power = fiber_ring(value).reduce(basis)
            remaining = int(exponent)
            while remaining:
                if remaining & 1:
                    result = (result * power).reduce(basis)
                remaining >>= 1
                if remaining:
                    power = (power * power).reduce(basis)
            return fiber_ring(result)

        def evaluate_base(value, x_value, s_value, p_value):
            return field(
                sum(
                    field(QQ(coefficient).numerator())
                    / field(QQ(coefficient).denominator())
                    * x_value ** monomial[0]
                    * s_value ** monomial[1]
                    * p_value ** monomial[2]
                    for monomial, coefficient in base(value).dict().items()
                )
            )

        def evaluate_row(value, x_value, s_value, p_value, w_value):
            return field(
                sum(
                    evaluate_base(coefficient, x_value, s_value, p_value)
                    * w_value ** index
                    for index, coefficient in enumerate(value.list())
                )
            )

        fibers = []
        witness = None
        for s_integer in range(
            args.fiber_start, args.fiber_start + args.fiber_limit
        ):
            s_value = field(s_integer)
            generators = [specialize_s(value, s_value) for value in affine_source]
            print(
                canonical_json(
                    {
                        "phase": "FIBER_GROEBNER_BEGIN",
                        "s": s_integer,
                        "generators": [fiber_metric(value) for value in generators],
                    }
                ),
                flush=True,
            )
            basis = list(
                fiber_ring.ideal(generators).groebner_basis(
                    algorithm="singular:slimgb"
                )
            )
            unit_ideal = basis == [fiber_ring(1)]
            dimension = -1 if unit_ideal else int(fiber_ring.ideal(basis).dimension())
            record = {
                "s": s_integer,
                "basis_size": len(basis),
                "basis_sha256": digest("\n".join(str(value) for value in basis)),
                "dimension": dimension,
                "unit_ideal": unit_ideal,
            }
            if not unit_ideal and dimension == 0:
                if args.factor_fibers:
                    lex_ring = PolynomialRing(
                        field, names=("x", "pvar"), order="lex"
                    )
                    lx, lp = lex_ring.gens()

                    def to_lex(value):
                        return lex_ring(
                            sum(
                                field(coefficient)
                                * lx ** monomial[0]
                                * lp ** monomial[1]
                                for monomial, coefficient in fiber_ring(value).dict().items()
                            )
                        )

                    lex_basis = list(
                        lex_ring.ideal(
                            [to_lex(value) for value in generators]
                        ).groebner_basis(algorithm="singular:slimgb")
                    )
                    univariate = [
                        value for value in lex_basis
                        if value and value.degree(lx) == 0
                    ]

                    def lex_metric(value):
                        value = lex_ring(value)
                        return {
                            "degree": int(value.total_degree()) if value else -1,
                            "degrees": [
                                int(value.degree(generator))
                                for generator in (lx, lp)
                            ],
                            "terms": int(len(value.monomials())) if value else 0,
                            "sha256": digest(value),
                        }

                    record["lex_basis_size"] = len(lex_basis)
                    record["lex_basis_sha256"] = digest(
                        "\n".join(str(value) for value in lex_basis)
                    )
                    record["univariate_basis"] = [
                        {
                            **lex_metric(value),
                            "factors": [
                                {
                                    **lex_metric(factor),
                                    "exponent": int(exponent),
                                }
                                for factor, exponent in value.factor()
                            ],
                        }
                        for value in univariate
                    ]
                    assert len(univariate) == 1
                    component_records = []
                    component_open_values = [degree6, chart_factor]
                    component_open_values.extend(branch["transported_units"])
                    for factor, exponent in univariate[0].factor():
                        fiber_factor = fiber_ring(
                            sum(
                                field(coefficient)
                                * fx ** monomial[0]
                                * fp ** monomial[1]
                                for monomial, coefficient in factor.dict().items()
                            )
                        )
                        component_basis = list(
                            fiber_ring.ideal(
                                basis + [fiber_factor]
                            ).groebner_basis(algorithm="singular:slimgb")
                        )
                        component_unit = component_basis == [fiber_ring(1)]
                        component_localizer = fiber_ring(1)
                        component_open_steps = []
                        if not component_unit:
                            for index, value in enumerate(
                                component_open_values, start=1
                            ):
                                component_localizer = (
                                    component_localizer
                                    * specialize_s(value, s_value)
                                ).reduce(component_basis)
                                component_open_steps.append(
                                    {
                                        "index": index,
                                        "zero": not bool(component_localizer),
                                        **fiber_metric(component_localizer),
                                    }
                                )
                                if not component_localizer:
                                    break

                        saturation_unit = True
                        saturation_size = 1
                        saturation_sha256 = digest("1")
                        if not component_unit and component_localizer:
                            saturation_ring = PolynomialRing(
                                field,
                                names=("inverse", "x", "pvar"),
                                order="degrevlex",
                            )
                            inverse, sx, sp = saturation_ring.gens()

                            def to_saturation(value):
                                return saturation_ring(
                                    sum(
                                        field(coefficient)
                                        * sx ** monomial[0]
                                        * sp ** monomial[1]
                                        for monomial, coefficient in fiber_ring(value).dict().items()
                                    )
                                )

                            saturation_basis = list(
                                saturation_ring.ideal(
                                    [
                                        to_saturation(value)
                                        for value in component_basis
                                    ]
                                    + [
                                        inverse
                                        * to_saturation(component_localizer)
                                        - 1
                                    ]
                                ).groebner_basis(algorithm="singular:slimgb")
                            )
                            saturation_unit = saturation_basis == [
                                saturation_ring(1)
                            ]
                            saturation_size = len(saturation_basis)
                            saturation_sha256 = digest(
                                "\n".join(str(value) for value in saturation_basis)
                            )
                        component_records.append(
                            {
                                "factor": lex_metric(factor),
                                "exponent": int(exponent),
                                "component_basis_size": len(component_basis),
                                "component_unit_ideal": component_unit,
                                "open_product_zero": not bool(component_localizer),
                                "open_product_steps": component_open_steps,
                                "saturation_unit_ideal": saturation_unit,
                                "saturation_basis_size": saturation_size,
                                "saturation_basis_sha256": saturation_sha256,
                            }
                        )
                    record["factor_components"] = component_records
                q = int(field.cardinality())
                frobenius = []
                for generator in (fx, fp):
                    current = fiber_ring(generator)
                    for _ in range(args.field_degree):
                        current = power_reduce(current, q, basis)
                    frobenius.append(
                        fiber_ring(current - generator).reduce(basis)
                    )
                field_basis = list(
                    fiber_ring.ideal(basis + frobenius).groebner_basis(
                        algorithm="singular:slimgb"
                    )
                )
                field_unit = field_basis == [fiber_ring(1)]
                record.update(
                    {
                        "frobenius": [fiber_metric(value) for value in frobenius],
                        "field_basis_size": len(field_basis),
                        "field_basis_sha256": digest(
                            "\n".join(str(value) for value in field_basis)
                        ),
                        "field_unit_ideal": field_unit,
                        "field_extension_degree": args.field_degree,
                    }
                )
                open_values = [degree6, chart_factor]
                open_values.extend(branch["transported_units"])
                open_product = fiber_ring(1)
                open_steps = []
                if not field_unit:
                    for index, value in enumerate(open_values, start=1):
                        open_product = (
                            open_product * specialize_s(value, s_value)
                        ).reduce(field_basis)
                        open_steps.append(
                            {
                                "index": index,
                                "zero": not bool(open_product),
                                **fiber_metric(open_product),
                            }
                        )
                        if not open_product:
                            break
                record["open_product_steps"] = open_steps
                record["open_product_zero"] = not bool(open_product)
                if not field_unit and open_product:
                    record["open_finite_field_point_proved"] = True
                if not field_unit:
                    solutions = (
                        fiber_ring.ideal(field_basis).variety()
                        if args.field_degree == 1
                        else []
                    )
                    if args.field_degree == 1:
                        record["field_solutions"] = len(solutions)
                    rejection_signatures = {}
                    for solution in solutions:
                        x_value = field(solution[fx])
                        p_value = field(solution[fp])
                        u_value = evaluate_base(U, x_value, s_value, p_value)
                        v_value = evaluate_base(V, x_value, s_value, p_value)
                        open_records = [
                            (
                                "prior_L6",
                                evaluate_base(degree6, x_value, s_value, p_value),
                            ),
                            (
                                "chart_K8",
                                evaluate_base(
                                    chart_factor, x_value, s_value, p_value
                                ),
                            ),
                        ]
                        open_records.extend(
                            (
                                f"transported_{index}",
                                evaluate_base(value, x_value, s_value, p_value),
                            )
                            for index, value in enumerate(
                                branch["transported_units"], start=1
                            )
                        )
                        zero_open = [
                            label for label, value in open_records if not value
                        ]
                        row_values = None
                        w_value = None
                        nonzero_rows = []
                        if v_value:
                            w_value = -u_value / v_value
                            row_values = [
                                evaluate_row(
                                    value, x_value, s_value, p_value, w_value
                                )
                                for value in rows
                            ]
                            nonzero_rows = [
                                f"row_{index}"
                                for index, value in enumerate(row_values, start=1)
                                if value
                            ]
                        signature = tuple(zero_open + nonzero_rows)
                        signature_key = "|".join(signature) if signature else "ADMISSIBLE"
                        if signature_key not in rejection_signatures:
                            rejection_signatures[signature_key] = {
                                "count": 0,
                                "zero_open": zero_open,
                                "nonzero_rows": nonzero_rows,
                                "sample": {
                                    "x": int(x_value),
                                    "p": int(p_value),
                                    "w": int(w_value) if w_value is not None else None,
                                },
                            }
                        rejection_signatures[signature_key]["count"] += 1
                        if not zero_open and row_values is not None and not any(row_values):
                            witness = {
                                "x": int(x_value),
                                "s": int(s_value),
                                "p": int(p_value),
                                "w": int(w_value),
                                "row_values": [int(value) for value in row_values],
                                "open_factor_count": len(open_records),
                                "all_open": True,
                            }
                            break
                    record["rejection_signatures"] = sorted(
                        rejection_signatures.values(),
                        key=lambda item: (
                            item["zero_open"], item["nonzero_rows"], item["count"]
                        ),
                    )
            fibers.append(record)
            print(canonical_json({"phase": "FIBER_DONE", **record}), flush=True)
            if witness is not None:
                print(canonical_json({"phase": "WITNESS", **witness}), flush=True)
                break
            if record.get("open_finite_field_point_proved"):
                break
        fiber_search_record = {
            "fibers": fibers,
            "witness": witness,
            "terminal": (
                "DIRECT_F_P_WITNESS_FOUND"
                if witness is not None
                else "OPEN_F_P6_POINT_PROVED"
                if any(
                    record.get("open_finite_field_point_proved")
                    for record in fibers
                )
                else "NO_DIRECT_F_P_WITNESS_IN_TESTED_FIBERS"
            ),
        }

    result = {
        "phase": "DONE",
        "cell": args.cell,
        "divisor": args.divisor,
        "leading": base_metric(leading),
        "leading_factors": leading_factors,
        "records": {
            name: {
                key: value
                for key, value in record.items()
                if key not in ("determinant_value", "core_value")
            }
            for name, record in records.items()
        },
        "groebner": groebner_record,
        "global_saturation": global_saturation_record,
        "fiber_search": fiber_search_record,
        "terminal": "QUADRATIC_PSEUDOREMAINDER_DETERMINANTS_COMPILED",
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
