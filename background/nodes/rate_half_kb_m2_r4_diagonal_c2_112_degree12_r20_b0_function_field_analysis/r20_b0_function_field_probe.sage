#!/usr/bin/env sage
"""Compile the complete-open R20 B0 generic fiber over Q(s)."""

import argparse
import hashlib
import json
from pathlib import Path


LIBRARY = Path("/branch_core.sage")


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
    parser.add_argument(
        "--cell",
        choices=("F04-R20", "F05-R20", "F06-R20", "F07-R20"),
        required=True,
    )
    parser.add_argument("--target-elimination", action="store_true")
    args = parser.parse_args()
    print(canonical_json({"phase": "START", "cell": args.cell}), flush=True)

    library = load_library()
    branch = library["build_branch"](args.cell)
    base = branch["base"]
    x, s, pvar = base.gens()
    rows = branch["converted"]
    U = base(branch["equations"]["U"])
    V = base(branch["equations"]["V"])

    def metric(value):
        value = value.parent()(value)
        return {
            "degree": int(value.total_degree()) if value else -1,
            "degrees": [int(value.degree(g)) for g in value.parent().gens()],
            "terms": int(len(value.monomials())) if value else 0,
            "sha256": digest(value),
        }

    def nonnamed_leading(divisor):
        leading = base(divisor.leading_coefficient())
        values = []
        for factor, exponent in leading.factor():
            if library["normalized_key"](factor) not in branch["unit_keys"]:
                values.extend([base(factor)] * int(exponent))
        assert len(values) == 1
        return leading, values[0]

    leading, K10 = nonnamed_leading(rows[1])

    def pseudo_core(polynomial):
        divisor = rows[1]
        current = polynomial.parent()(polynomial)
        quotient = polynomial.parent()(0)
        multiplier = base(1)
        steps = 0
        while current and current.degree() >= divisor.degree():
            old_degree = int(current.degree())
            coefficient = base(current[old_degree])
            shift = old_degree - int(divisor.degree())
            current = polynomial.parent()(
                leading * current
                - coefficient * polynomial.parent().gen() ** shift * divisor
            )
            quotient = polynomial.parent()(
                leading * quotient
                + coefficient * polynomial.parent().gen() ** shift
            )
            multiplier = base(multiplier * leading)
            steps += 1
        assert polynomial.parent()(multiplier * polynomial - quotient * divisor) == current
        assert steps == 3 and current.degree() <= 1
        determinant = base(V * base(current[0]) - U * base(current[1]))
        core = base(1)
        factor_records = []
        for factor, exponent in determinant.factor():
            key = library["normalized_key"](factor)
            is_named = key in branch["unit_keys"]
            is_leading = key == library["normalized_key"](K10)
            factor_records.append(
                {
                    **metric(factor),
                    "exponent": int(exponent),
                    "named_unit_factor": is_named,
                    "leading_factor": is_leading,
                }
            )
            if not is_named and not is_leading:
                core *= base(factor) ** int(exponent)
        assert core != 1
        return base(core), factor_records

    core_a, factors_a = pseudo_core(rows[2])
    core_b, factors_b = pseudo_core(rows[3])
    r_factors = [
        record["factor"]
        for record in branch["factors"]["R"]
        if not record["named_unit_factor"]
    ]
    selected = base(r_factors[2])
    selected_degree_x = int(selected.degree(x))
    selected_leading = base(
        sum(
            QQ(coefficient) * s ** monomial[1] * pvar ** monomial[2]
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
                "K10": metric(K10),
                "L6": metric(L6),
                "cores": {"A1": metric(core_a), "B1": metric(core_b)},
                "determinant_factors": {"A1": factors_a, "B1": factors_b},
            }
        ),
        flush=True,
    )

    if args.target_elimination:
        field = GF(2130706433)
        elimination_ring = PolynomialRing(
            field,
            names=("x", "pvar", "svar"),
            order="lex",
        )
        ex, ep, es = elimination_ring.gens()

        def convert_target(value):
            output = elimination_ring(0)
            for monomial, coefficient in base(value).dict().items():
                coefficient = QQ(coefficient)
                reduced = (
                    field(coefficient.numerator())
                    / field(coefficient.denominator())
                )
                output += (
                    reduced
                    * ex ** monomial[0]
                    * es ** monomial[1]
                    * ep ** monomial[2]
                )
            return output

        generators = [convert_target(selected), convert_target(core_a), convert_target(core_b)]
        print(
            canonical_json(
                {
                    "phase": "TARGET_ELIMINATION_BEGIN",
                    "generator_count": len(generators),
                }
            ),
            flush=True,
        )
        basis = list(
            elimination_ring.ideal(generators).groebner_basis(
                algorithm="singular:slimgb"
            )
        )
        unit_ideal = basis == [elimination_ring(1)]
        elimination = [
            value for value in basis if value and value.degree(ex) == 0
        ]

        def elimination_metric(value):
            value = elimination_ring(value)
            return {
                "degree": int(value.total_degree()) if value else -1,
                "degrees": [
                    int(value.degree(generator))
                    for generator in elimination_ring.gens()
                ],
                "terms": int(len(value.monomials())) if value else 0,
                "sha256": digest(value),
            }

        print(
            canonical_json(
                {
                    "phase": "TARGET_ELIMINATION_BASIS_DONE",
                    "basis_size": len(basis),
                    "basis_sha256": digest("\n".join(str(value) for value in basis)),
                    "dimension": -1 if unit_ideal else int(elimination_ring.ideal(basis).dimension()),
                    "elimination_count": len(elimination),
                    "elimination": [elimination_metric(value) for value in elimination],
                }
            ),
            flush=True,
        )
        boundary = ep + es + 1
        factor_records = []
        for value in elimination:
            factors = []
            for factor, exponent in value.factor():
                factors.append(
                    {
                        **elimination_metric(factor),
                        "exponent": int(exponent),
                        "boundary_p_plus_s_plus_1": (
                            factor.monic() == boundary.monic()
                        ),
                    }
                )
            factor_records.append(
                {"polynomial": elimination_metric(value), "factors": factors}
            )
        print(
            canonical_json(
                {
                    "phase": "DONE",
                    "cell": args.cell,
                    "basis_size": len(basis),
                    "basis_sha256": digest("\n".join(str(value) for value in basis)),
                    "dimension": -1 if unit_ideal else int(elimination_ring.ideal(basis).dimension()),
                    "unit_ideal": unit_ideal,
                    "elimination_factors": factor_records,
                    "terminal": "R20_TARGET_ELIMINATION_COMPILED",
                }
            ),
            flush=True,
        )
        return

    parameter_ring = PolynomialRing(QQ, "s")
    parameter = parameter_ring.gen()
    function_field = FractionField(parameter_ring)
    ring = PolynomialRing(
        function_field,
        names=("x", "pvar"),
        order="degrevlex",
    )
    fx, fp = ring.gens()

    def convert(value):
        output = ring(0)
        for monomial, coefficient in base(value).dict().items():
            output += (
                function_field(QQ(coefficient))
                * fx ** monomial[0]
                * function_field(parameter) ** monomial[1]
                * fp ** monomial[2]
            )
        return output

    open_values = [L6, K10]
    open_values.extend(branch["unit_factors"])
    generators = [convert(selected), convert(core_a), convert(core_b)]
    print(
        canonical_json(
            {
                "phase": "FUNCTION_FIELD_BEGIN",
                "generator_count": len(generators),
                "open_factor_count": len(open_values),
            }
        ),
        flush=True,
    )
    basis = list(ring.ideal(generators).groebner_basis(algorithm="singular:slimgb"))
    unit_ideal = basis == [ring(1)]
    dimension = -1 if unit_ideal else int(ring.ideal(basis).dimension())

    def polynomial_degree(value):
        return int(value.degree()) if value else -1

    def coefficient_degrees(value):
        numerator_degrees = []
        denominator_degrees = []
        for coefficient in ring(value).dict().values():
            numerator_degrees.append(polynomial_degree(coefficient.numerator()))
            denominator_degrees.append(polynomial_degree(coefficient.denominator()))
        return {
            "max_numerator_s_degree": max(numerator_degrees, default=-1),
            "max_denominator_s_degree": max(denominator_degrees, default=-1),
        }

    def ring_metric(value):
        value = ring(value)
        return {
            "degree": int(value.total_degree()) if value else -1,
            "degrees": [int(value.degree(g)) for g in ring.gens()],
            "terms": int(len(value.monomials())) if value else 0,
            "sha256": digest(value),
            **coefficient_degrees(value),
        }

    basis_records = [ring_metric(value) for value in basis]
    open_product = ring(1)
    open_steps = []
    if not unit_ideal:
        for index, value in enumerate(open_values, start=1):
            open_product = (open_product * convert(value)).reduce(basis)
            open_steps.append(
                {
                    "index": index,
                    "source": metric(value),
                    "reduced": ring_metric(open_product),
                    "zero": not bool(open_product),
                }
            )
            if not open_product:
                break
    open_nilpotence = None
    if unit_ideal or not open_product:
        open_nilpotence = 1
    elif dimension == 0:
        current = ring(open_product)
        for exponent in range(2, 9):
            current = (current * open_product).reduce(basis)
            if not current:
                open_nilpotence = exponent
                break

    univariate = [
        value
        for value in basis
        if value and value.degree(fx) == 0
    ]
    factor_records = []
    for value in univariate:
        factor_records.append({"polynomial": ring_metric(value)})

    result = {
        "phase": "DONE",
        "cell": args.cell,
        "basis_size": len(basis),
        "basis_sha256": digest("\n".join(str(value) for value in basis)),
        "dimension": dimension,
        "unit_ideal": unit_ideal,
        "basis": basis_records,
        "open_steps": open_steps,
        "open_product_nilpotence_index": open_nilpotence,
        "univariate_pvar": factor_records,
        "terminal": (
            "COMPLETE_OPEN_R20_GENERIC_FIBER_BOUNDARY_SUPPORTED"
            if open_nilpotence is not None
            else "COMPLETE_OPEN_R20_GENERIC_FIBER_SURVIVES"
        ),
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
