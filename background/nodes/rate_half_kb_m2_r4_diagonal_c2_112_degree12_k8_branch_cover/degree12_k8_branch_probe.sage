#!/usr/bin/env sage
"""Test the two exhaustive K8=0 branches of the F04-R02 degree-12 cell."""

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
    parser.add_argument("--mode", choices=("a0_k10_nonzero", "k8_k10_zero"), required=True)
    args = parser.parse_args()
    print(canonical_json({"phase": "START", "mode": args.mode}), flush=True)

    library = load_library()
    branch = library["build_branch"]("F04-R02")
    base = branch["base"]
    x, s, p = base.gens()
    rows = branch["converted"]
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

    def leading_factor(divisor):
        leading = base(divisor.leading_coefficient())
        named = []
        nonnamed = []
        records = []
        for factor, exponent in leading.factor():
            is_named = library["normalized_key"](factor) in branch["unit_keys"]
            records.append(
                {
                    **metric(factor),
                    "exponent": int(exponent),
                    "named_unit_factor": is_named,
                }
            )
            target = named if is_named else nonnamed
            target.extend([base(factor)] * int(exponent))
        assert len(nonnamed) == 1
        return leading, nonnamed[0], records

    a_leading, K10, a_leading_records = leading_factor(rows[0])
    b_leading, K8, b_leading_records = leading_factor(rows[1])
    assert K10.total_degree() == 10
    assert K8.total_degree() == 8

    def pseudo_core(polynomial):
        divisor = rows[0]
        leading = a_leading
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
        r0 = base(current[0])
        r1 = base(current[1])
        determinant = base(V * r0 - U * r1)
        core = base(1)
        factors = []
        for factor, exponent in determinant.factor():
            key = library["normalized_key"](factor)
            is_named = key in branch["unit_keys"]
            is_leading = key == library["normalized_key"](K10)
            factors.append(
                {
                    **metric(factor),
                    "exponent": int(exponent),
                    "named_unit_factor": is_named,
                    "leading_factor": is_leading,
                }
            )
            if not is_named and not is_leading:
                core *= base(factor) ** int(exponent)
        assert core.total_degree() == 37
        return base(core), metric(determinant), factors

    core_a, determinant_a, factors_a = pseudo_core(rows[2])
    core_b, determinant_b, factors_b = pseudo_core(rows[3])
    print(
        canonical_json(
            {
                "phase": "SOURCE_COMPILED",
                "K8": metric(K8),
                "K10": metric(K10),
                "A0_leading": metric(a_leading),
                "B0_leading": metric(b_leading),
                "A0_leading_factors": a_leading_records,
                "B0_leading_factors": b_leading_records,
                "cores": {"A1": metric(core_a), "B1": metric(core_b)},
                "determinants": {"A1": determinant_a, "B1": determinant_b},
                "determinant_factors": {"A1": factors_a, "B1": factors_b},
            }
        ),
        flush=True,
    )

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
    L6 = base(degree6_values[0])

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

    if args.mode == "a0_k10_nonzero":
        generator_values = [selected, K8, core_a, core_b]
        open_values = [("prior_s", s), ("prior_L6", L6), ("chart_K10", K10)]
    else:
        generator_values = [selected, K8, K10]
        open_values = [("prior_s", s), ("prior_L6", L6)]
    open_values.extend(
        (f"unit_{index}", value)
        for index, value in enumerate(branch["unit_factors"], start=1)
    )
    generators = [convert(value) for value in generator_values]
    print(
        canonical_json(
            {
                "phase": "GROEBNER_BEGIN",
                "generators": [metric(value) for value in generator_values],
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
    saturation_size = 1 if saturation_unit else None
    saturation_dimension = -1 if saturation_unit else None
    saturation_sha256 = digest("1") if saturation_unit else None
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
        saturation_size = len(saturation_basis)
        saturation_dimension = (
            -1
            if saturation_unit
            else int(saturation_ring.ideal(saturation_basis).dimension())
        )
        saturation_sha256 = digest(
            "\n".join(str(value) for value in saturation_basis)
        )
        print(
            canonical_json(
                {
                    "phase": "SATURATION_DONE",
                    "unit_ideal": saturation_unit,
                    "basis_size": saturation_size,
                    "basis_sha256": saturation_sha256,
                    "dimension": saturation_dimension,
                }
            ),
            flush=True,
        )

    result = {
        "phase": "DONE",
        "mode": args.mode,
        "basis_size": len(basis),
        "basis_sha256": digest("\n".join(str(value) for value in basis)),
        "dimension": dimension,
        "unit_ideal": unit_ideal,
        "localizer_steps": localizer_steps,
        "saturation_unit_ideal": saturation_unit,
        "saturation_basis_size": saturation_size,
        "saturation_basis_sha256": saturation_sha256,
        "saturation_dimension": saturation_dimension,
        "terminal": (
            "K8_BRANCH_EMPTY"
            if saturation_unit
            else "K8_BRANCH_SURVIVES"
        ),
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
