#!/usr/bin/env sage
"""Reduce the degree-12 resultant route over F_p(s,p)[x]."""

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
    parser.add_argument("--cell", choices=("F04-R02", "F04-R20"), required=True)
    parser.add_argument("--prime", type=int, default=2130706433)
    args = parser.parse_args()
    print(canonical_json({"phase": "START", "cell": args.cell}), flush=True)

    library = load_library()
    branch = library["build_branch"](args.cell)
    base = branch["base"]
    r_factors = [
        record["factor"]
        for record in branch["factors"]["R"]
        if not record["named_unit_factor"]
    ]
    assert len(r_factors) == 3
    selected = r_factors[2]
    assert selected.total_degree() == 12 and selected.degree(base.gen(0)) == 6
    e2 = branch["essential"]["E2"]
    e3 = branch["essential"]["E3"]

    field = GF(ZZ(args.prime))
    coefficient_ring = PolynomialRing(field, names=("s", "p"), order="degrevlex")
    s, p = coefficient_ring.gens()
    coefficient_field = FractionField(coefficient_ring)
    polynomial_x = PolynomialRing(coefficient_field, "x")
    x = polynomial_x.gen()

    def convert(value):
        output = polynomial_x(0)
        for monomial, coefficient in base(value).dict().items():
            ex, es, ep = monomial
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += coefficient_field(reduced * s ** es * p ** ep) * x ** ex
        return output

    def coefficient_metric(value):
        value = coefficient_ring(value)
        return {
            "degree": int(value.total_degree()) if value else -1,
            "degrees": [int(value.degree(generator)) for generator in (s, p)],
            "terms": int(len(value.monomials())) if value else 0,
            "sha256": digest(value),
        }

    def rational_metric(value):
        value = coefficient_field(value)
        return {
            "numerator": coefficient_metric(value.numerator()),
            "denominator": coefficient_metric(value.denominator()),
        }

    def polynomial_metric(value):
        value = polynomial_x(value)
        coefficient_metrics = [rational_metric(coefficient) for coefficient in value.list()]
        return {
            "degree_x": int(value.degree()) if value else -1,
            "nonzero_coefficients": sum(bool(coefficient) for coefficient in value.list()),
            "coefficient_metrics": coefficient_metrics,
            "sha256": digest(value),
        }

    f = convert(selected)
    g2 = convert(e2)
    g3 = convert(e3)
    print(
        canonical_json(
            {
                "phase": "CONVERTED",
                "degrees_x": [int(value.degree()) for value in (f, g2, g3)],
                "f_leading": rational_metric(f.leading_coefficient()),
            }
        ),
        flush=True,
    )
    remainder2 = g2.mod(f)
    remainder3 = g3.mod(f)
    print(
        canonical_json(
            {
                "phase": "REMAINDERS",
                "E2": polynomial_metric(remainder2),
                "E3": polynomial_metric(remainder3),
            }
        ),
        flush=True,
    )

    print(canonical_json({"phase": "RESULTANT_E2_BEGIN"}), flush=True)
    resultant2 = coefficient_field(f.resultant(remainder2))
    print(
        canonical_json(
            {"phase": "RESULTANT_E2_DONE", "metric": rational_metric(resultant2)}
        ),
        flush=True,
    )
    print(canonical_json({"phase": "RESULTANT_E3_BEGIN"}), flush=True)
    resultant3 = coefficient_field(f.resultant(remainder3))
    print(
        canonical_json(
            {"phase": "RESULTANT_E3_DONE", "metric": rational_metric(resultant3)}
        ),
        flush=True,
    )

    numerator2 = coefficient_ring(resultant2.numerator())
    numerator3 = coefficient_ring(resultant3.numerator())
    denominator2 = coefficient_ring(resultant2.denominator())
    denominator3 = coefficient_ring(resultant3.denominator())
    gcd = coefficient_ring(numerator2.gcd(numerator3))
    print(
        canonical_json(
            {
                "phase": "BASE_GCD",
                "metric": coefficient_metric(gcd),
                "polynomial": str(gcd) if len(gcd.monomials()) <= 300 else None,
            }
        ),
        flush=True,
    )

    print(canonical_json({"phase": "BASE_GROEBNER_BEGIN"}), flush=True)
    base_basis = list(
        coefficient_ring.ideal([numerator2, numerator3]).groebner_basis(
            algorithm="singular:slimgb"
        )
    )
    unit_ideal = base_basis == [coefficient_ring(1)]
    dimension = -1 if unit_ideal else int(coefficient_ring.ideal(base_basis).dimension())
    print(
        canonical_json(
            {
                "phase": "BASE_GROEBNER_DONE",
                "unit_ideal": unit_ideal,
                "dimension": dimension,
                "basis_size": len(base_basis),
                "basis_sha256": digest("\n".join(str(value) for value in base_basis)),
            }
        ),
        flush=True,
    )

    leading_numerator = coefficient_ring(f.leading_coefficient().numerator())
    leading_denominator = coefficient_ring(f.leading_coefficient().denominator())
    denominator_product = coefficient_ring(denominator2 * denominator3 * leading_denominator)
    result = {
        "phase": "DONE",
        "cell": args.cell,
        "selected_sha256": digest(selected),
        "remainder_metrics": {
            "E2": polynomial_metric(remainder2),
            "E3": polynomial_metric(remainder3),
        },
        "resultant_metrics": {
            "E2": rational_metric(resultant2),
            "E3": rational_metric(resultant3),
        },
        "base_gcd": {
            "metric": coefficient_metric(gcd),
            "polynomial": str(gcd) if len(gcd.monomials()) <= 300 else None,
        },
        "base_basis_size": len(base_basis),
        "base_basis_sha256": digest("\n".join(str(value) for value in base_basis)),
        "base_dimension": dimension,
        "base_unit_ideal": unit_ideal,
        "leading_numerator": coefficient_metric(leading_numerator),
        "denominator_product": coefficient_metric(denominator_product),
        "terminal": "DEGREE12_FUNCTION_FIELD_BASE_REDUCTION_COMPILED",
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
