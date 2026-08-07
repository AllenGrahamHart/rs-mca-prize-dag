"""Block-order localization analysis for a one-parameter saturated ideal."""


def analyze_generic_block(
    field,
    source_ring,
    source_basis,
    parameter_index,
    digest,
    canonical_json,
):
    source_generators = source_ring.gens()
    variable_indices = tuple(
        index for index in range(len(source_generators)) if index != parameter_index
    )
    assert len(variable_indices) == 3

    block_order = TermOrder("degrevlex", 3) + TermOrder("degrevlex", 1)
    block_ring = PolynomialRing(
        field,
        names=("inverse", "x", "pvar", "svar"),
        order=block_order,
    )
    block_generators = block_ring.gens()

    def to_block(value):
        output = block_ring(0)
        for monomial, coefficient in source_ring(value).dict().items():
            reordered = tuple(monomial[index] for index in variable_indices) + (
                monomial[parameter_index],
            )
            term = field(coefficient)
            for generator, exponent in zip(block_generators, reordered):
                term *= generator ** exponent
            output += term
        return block_ring(output)

    print(
        canonical_json(
            {
                "phase": "K10_GENERIC_BLOCK_BEGIN",
                "generator_count": len(source_basis),
            }
        ),
        flush=True,
    )
    block_basis = list(
        block_ring.ideal([to_block(value) for value in source_basis]).groebner_basis(
            algorithm="singular:slimgb"
        )
    )
    block_sha256 = digest("\n".join(str(value) for value in block_basis))
    print(
        canonical_json(
            {
                "phase": "K10_GENERIC_BLOCK_DONE",
                "basis_size": len(block_basis),
                "basis_sha256": block_sha256,
            }
        ),
        flush=True,
    )

    parameter_ring = PolynomialRing(field, "sparam")
    sparam = parameter_ring.gen()
    function_field = parameter_ring.fraction_field()
    generic_ring = PolynomialRing(
        function_field,
        names=("inverse", "x", "pvar"),
        order="degrevlex",
        implementation="generic",
    )
    generic_generators = generic_ring.gens()

    def to_generic(value):
        output = generic_ring(0)
        for monomial, coefficient in block_ring(value).dict().items():
            term = function_field(coefficient) * function_field(sparam) ** monomial[3]
            for generator, exponent in zip(generic_generators, monomial[:3]):
                term *= generator ** exponent
            output += term
        return generic_ring(output)

    def leading_monomial(value):
        return max(
            value.dict(),
            key=lambda monomial: (
                sum(monomial),
                tuple(-entry for entry in reversed(monomial)),
            ),
        )

    def monomial_value(exponents):
        output = generic_ring(1)
        for generator, exponent in zip(generic_generators, exponents):
            output *= generator ** exponent
        return generic_ring(output)

    def normal_form(value, reducers):
        current = generic_ring(value)
        remainder = generic_ring(0)
        reducer_data = []
        for reducer in reducers:
            if not reducer:
                continue
            reducer = generic_ring(reducer)
            reducer_monomial = leading_monomial(reducer)
            reducer_data.append(
                (reducer, reducer_monomial, reducer.dict()[reducer_monomial])
            )
        while current:
            current_monomial = leading_monomial(current)
            current_coefficient = current.dict()[current_monomial]
            for reducer, reducer_monomial, reducer_coefficient in reducer_data:
                if all(
                    current_monomial[index] >= reducer_monomial[index]
                    for index in range(3)
                ):
                    quotient_monomial = tuple(
                        current_monomial[index] - reducer_monomial[index]
                        for index in range(3)
                    )
                    current -= (
                        current_coefficient
                        / reducer_coefficient
                        * monomial_value(quotient_monomial)
                        * reducer
                    )
                    break
            else:
                leading_term = current_coefficient * monomial_value(current_monomial)
                remainder += leading_term
                current -= leading_term
        return generic_ring(remainder)

    generic_basis = [to_generic(value) for value in block_basis if value]
    reduced_basis = []
    for index, value in enumerate(generic_basis):
        reduced = normal_form(
            value,
            generic_basis[:index] + generic_basis[index + 1 :],
        )
        if reduced:
            leading = leading_monomial(reduced)
            reduced_basis.append(
                generic_ring(reduced.dict()[leading] ** (-1) * reduced)
            )
    reduced_basis.sort(
        key=lambda value: (
            sum(leading_monomial(value)),
            tuple(-entry for entry in reversed(leading_monomial(value))),
        ),
        reverse=True,
    )

    denominator_factors = {}
    reduced_records = []
    for value in reduced_basis:
        coefficients = []
        for monomial, coefficient in sorted(value.dict().items(), reverse=True):
            numerator = parameter_ring(coefficient.numerator())
            denominator = parameter_ring(coefficient.denominator())
            factors = []
            for factor, exponent in denominator.factor():
                if factor.degree() <= 0:
                    continue
                normalized = factor.monic()
                key = str(normalized)
                denominator_factors[key] = normalized
                factors.append(
                    {
                        "polynomial": key,
                        "degree": int(normalized.degree()),
                        "exponent": int(exponent),
                        "sha256": digest(normalized),
                    }
                )
            coefficients.append(
                {
                    "monomial": monomial,
                    "numerator": str(numerator),
                    "numerator_degree": int(numerator.degree()),
                    "numerator_sha256": digest(numerator),
                    "denominator": str(denominator),
                    "denominator_degree": int(denominator.degree()),
                    "denominator_sha256": digest(denominator),
                    "denominator_factors": factors,
                }
            )
        reduced_records.append(
            {
                "leading_monomial": leading_monomial(value),
                "degree": int(value.total_degree()),
                "degrees": [
                    int(value.degree(generator)) for generator in generic_generators
                ],
                "terms": int(len(value.monomials())),
                "sha256": digest(value),
                "coefficients": coefficients,
            }
        )

    generic_inverse, generic_x, generic_p = generic_generators
    expected_boundary_square = generic_ring(
        (generic_p + function_field(sparam) + 1) ** 2
    )
    boundary_square_present = any(
        value == expected_boundary_square for value in reduced_basis
    )

    exceptional_records = []
    source_parameter = source_generators[parameter_index]
    for name, factor in sorted(denominator_factors.items()):
        source_factor = source_ring(
            sum(
                field(coefficient) * source_parameter ** exponent
                for exponent, coefficient in enumerate(factor.list())
            )
        )
        print(
            canonical_json(
                {
                    "phase": "K10_GENERIC_EXCEPTION_BEGIN",
                    "factor": name,
                    "degree": int(factor.degree()),
                    "sha256": digest(factor),
                }
            ),
            flush=True,
        )
        exceptional_basis = list(
            source_ring.ideal(source_basis + [source_factor]).groebner_basis(
                algorithm="singular:slimgb"
            )
        )
        unit_ideal = exceptional_basis == [source_ring(1)]
        record = {
            "factor": name,
            "degree": int(factor.degree()),
            "sha256": digest(factor),
            "basis_size": len(exceptional_basis),
            "basis_sha256": digest(
                "\n".join(str(value) for value in exceptional_basis)
            ),
            "unit_ideal": unit_ideal,
            "dimension": (
                -1
                if unit_ideal
                else int(source_ring.ideal(exceptional_basis).dimension())
            ),
        }
        exceptional_records.append(record)
        print(
            canonical_json({"phase": "K10_GENERIC_EXCEPTION_DONE", **record}),
            flush=True,
        )

    result = {
        "block_basis_size": len(block_basis),
        "block_basis_sha256": block_sha256,
        "generic_basis_size": len(generic_basis),
        "generic_basis_sha256": digest(
            "\n".join(str(value) for value in generic_basis)
        ),
        "reduced_basis_size": len(reduced_basis),
        "reduced_basis_sha256": digest(
            "\n".join(str(value) for value in reduced_basis)
        ),
        "reduced_basis": reduced_records,
        "boundary_square_present": boundary_square_present,
        "denominator_factors": sorted(denominator_factors),
        "exceptional_records": exceptional_records,
        "boundary_support_proved": (
            boundary_square_present
            and all(record["unit_ideal"] for record in exceptional_records)
        ),
    }
    print(
        canonical_json({"phase": "K10_GENERIC_ANALYSIS_DONE", **result}),
        flush=True,
    )
    return result
