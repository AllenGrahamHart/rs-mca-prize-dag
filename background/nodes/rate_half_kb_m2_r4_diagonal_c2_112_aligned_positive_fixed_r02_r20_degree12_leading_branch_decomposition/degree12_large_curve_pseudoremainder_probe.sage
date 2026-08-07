#!/usr/bin/env sage
"""Pseudo-reduce E2/E3 in x modulo R12 on a large leading curve."""

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

    def x_leading(value):
        degree_x = int(value.degree(bx))
        return base(
            sum(
                QQ(coefficient) * bs ** monomial[1] * bp ** monomial[2]
                for monomial, coefficient in base(value).dict().items()
                if monomial[0] == degree_x
            )
        )

    r_factors = [
        record["factor"]
        for record in branch["factors"]["R"]
        if not record["named_unit_factor"]
    ]
    selected = r_factors[2]
    degree6_candidates = [
        factor for factor, _ in x_leading(selected).factor()
        if factor.total_degree() == 6
    ]
    assert len(degree6_candidates) == 1
    degree6 = degree6_candidates[0]
    target_row = branch["essential"][args.row]
    large_candidates = [
        factor
        for factor, _ in x_leading(target_row).factor()
        if factor.total_degree() >= 20
        and library["normalized_key"](factor) not in branch["unit_keys"]
    ]
    assert len(large_candidates) == 1
    large = large_candidates[0]

    field = GF(ZZ(args.prime))
    coefficients = PolynomialRing(field, names=("s", "p"), order="degrevlex")
    s, p = coefficients.gens()
    polynomial_x = PolynomialRing(coefficients, "x")
    x = polynomial_x.gen()

    def convert_coefficient(value):
        output = coefficients(0)
        for monomial, coefficient in base(value).dict().items():
            assert monomial[0] == 0
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += reduced * s ** monomial[1] * p ** monomial[2]
        return output

    def convert_x(value):
        output = polynomial_x(0)
        for monomial, coefficient in base(value).dict().items():
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += reduced * s ** monomial[1] * p ** monomial[2] * x ** monomial[0]
        return output

    def coefficient_metric(value):
        value = coefficients(value)
        return {
            "degree": int(value.total_degree()) if value else -1,
            "degrees": [int(value.degree(generator)) for generator in (s, p)],
            "terms": int(len(value.monomials())) if value else 0,
            "sha256": digest(value),
        }

    def x_metric(value):
        value = polynomial_x(value)
        nonzero = [coefficient for coefficient in value.list() if coefficient]
        return {
            "degree_x": int(value.degree()) if value else -1,
            "coefficients": len(nonzero),
            "terms": sum(len(coefficient.monomials()) for coefficient in nonzero),
            "max_coefficient_degree": max(
                (coefficient.total_degree() for coefficient in nonzero), default=-1
            ),
            "sha256": digest(value),
        }

    large_coefficient = convert_coefficient(large)
    degree6_coefficient = convert_coefficient(degree6)
    divisor = convert_x(selected)
    rows = {
        "E2": convert_x(branch["essential"]["E2"]),
        "E3": convert_x(branch["essential"]["E3"]),
    }
    leading = coefficients(divisor.leading_coefficient())
    assert leading.divides(degree6_coefficient) or degree6_coefficient.divides(leading)
    print(
        canonical_json(
            {
                "phase": "CONVERTED",
                "large": coefficient_metric(large_coefficient),
                "degree6": coefficient_metric(degree6_coefficient),
                "divisor": x_metric(divisor),
                "rows": {name: x_metric(value) for name, value in rows.items()},
            }
        ),
        flush=True,
    )

    def reduce_large(value):
        return coefficients(value).reduce([large_coefficient])

    def normalize_coefficients(value):
        return polynomial_x(
            sum(reduce_large(coefficient) * x ** index
                for index, coefficient in enumerate(polynomial_x(value).list()))
        )

    def pseudo_reduce(name, value):
        current = normalize_coefficients(value)
        divisor_degree = int(divisor.degree())
        step = 0
        while current and current.degree() >= divisor_degree:
            old_degree = int(current.degree())
            coefficient = coefficients(current[old_degree])
            shift = old_degree - divisor_degree
            current = normalize_coefficients(leading * current - coefficient * x ** shift * divisor)
            step += 1
            require_degree = int(current.degree()) if current else -1
            assert require_degree < old_degree
            print(
                canonical_json(
                    {
                        "phase": "PSEUDO_STEP",
                        "name": name,
                        "step": step,
                        "metric": x_metric(current),
                    }
                ),
                flush=True,
            )
        return current

    remainders = {}
    for name in ("E2", "E3"):
        print(canonical_json({"phase": "PSEUDO_BEGIN", "name": name}), flush=True)
        remainders[name] = pseudo_reduce(name, rows[name])
        print(
            canonical_json(
                {"phase": "PSEUDO_DONE", "name": name, "metric": x_metric(remainders[name])}
            ),
            flush=True,
        )

    ring = PolynomialRing(field, names=("x", "s", "p"), order="degrevlex")
    rx, rs, rp = ring.gens()

    def coefficient_to_ring(value):
        output = ring(0)
        for monomial, coefficient in coefficients(value).dict().items():
            output += field(coefficient) * rs ** monomial[0] * rp ** monomial[1]
        return output

    def x_to_ring(value):
        return ring(
            sum(coefficient_to_ring(coefficient) * rx ** index
                for index, coefficient in enumerate(polynomial_x(value).list()))
        )

    generators = [
        coefficient_to_ring(large_coefficient),
        x_to_ring(divisor),
        x_to_ring(remainders["E2"]),
        x_to_ring(remainders["E3"]),
    ]
    print(
        canonical_json(
            {
                "phase": "FINAL_GROEBNER_BEGIN",
                "generator_terms": [len(value.monomials()) for value in generators],
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
                "phase": "FINAL_GROEBNER_DONE",
                "unit_ideal": unit_ideal,
                "dimension": dimension,
                "basis_size": len(basis),
                "basis_sha256": digest("\n".join(str(value) for value in basis)),
            }
        ),
        flush=True,
    )

    def convert_unit(value):
        output = ring(0)
        for monomial, coefficient in base(value).dict().items():
            coefficient = QQ(coefficient)
            reduced = field(coefficient.numerator()) / field(coefficient.denominator())
            output += reduced * rx ** monomial[0] * rs ** monomial[1] * rp ** monomial[2]
        return output

    localizer_factors = [("prior_s", ring(rs)), ("prior_L6", coefficient_to_ring(degree6_coefficient))]
    localizer_factors.extend(
        (f"unit_{index}", convert_unit(factor))
        for index, factor in enumerate(branch["unit_factors"], start=1)
    )
    localizer = ring(1)
    steps = []
    nilpotence_index = 1 if unit_ideal else None
    if not unit_ideal:
        for index, (label, factor) in enumerate(localizer_factors, start=1):
            localizer = (localizer * factor).reduce(basis)
            steps.append(
                {
                    "index": index,
                    "label": label,
                    "zero": not bool(localizer),
                    "terms": len(localizer.monomials()) if localizer else 0,
                    "sha256": digest(localizer),
                }
            )
            if not localizer:
                nilpotence_index = 1
                break

    terminal = (
        "DEGREE12_LARGE_CURVE_PSEUDO_EMPTY"
        if nilpotence_index is not None
        else "DEGREE12_LARGE_CURVE_PSEUDO_SURVIVES"
    )
    print(
        canonical_json(
            {
                "phase": "DONE",
                "cell": args.cell,
                "row": args.row,
                "large_sha256": digest(large),
                "large_degree": int(large.total_degree()),
                "remainder_metrics": {
                    name: x_metric(value) for name, value in remainders.items()
                },
                "basis_size": len(basis),
                "basis_sha256": digest("\n".join(str(value) for value in basis)),
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
