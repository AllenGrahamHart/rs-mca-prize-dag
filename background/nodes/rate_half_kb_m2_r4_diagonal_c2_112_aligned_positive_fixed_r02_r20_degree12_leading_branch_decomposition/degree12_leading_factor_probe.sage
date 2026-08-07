#!/usr/bin/env sage
"""Factor the initial x-leading coefficients on the degree-12 route."""

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
    args = parser.parse_args()
    print(canonical_json({"phase": "START", "cell": args.cell}), flush=True)

    library = load_library()
    branch = library["build_branch"](args.cell)
    base = branch["base"]
    x, s, p = base.gens()
    r_factors = [
        record["factor"]
        for record in branch["factors"]["R"]
        if not record["named_unit_factor"]
    ]
    values = {
        "R12": r_factors[2],
        "E2": branch["essential"]["E2"],
        "E3": branch["essential"]["E3"],
    }

    coefficient_ring = PolynomialRing(QQ, names=("s", "p"), order="degrevlex")
    cs, cp = coefficient_ring.gens()

    def coefficient_x(value, degree):
        output = coefficient_ring(0)
        for monomial, coefficient in base(value).dict().items():
            if monomial[0] == degree:
                output += QQ(coefficient) * cs ** monomial[1] * cp ** monomial[2]
        return output

    def lift(value):
        output = base(0)
        for monomial, coefficient in coefficient_ring(value).dict().items():
            output += QQ(coefficient) * s ** monomial[0] * p ** monomial[1]
        return output

    records = []
    for name, value in values.items():
        degree_x = int(value.degree(x))
        leading = coefficient_x(value, degree_x)
        factors = []
        for factor, exponent in leading.factor():
            lifted = lift(factor)
            terms = int(len(factor.monomials()))
            factors.append(
                {
                    "exponent": int(exponent),
                    "degree": int(factor.total_degree()),
                    "degrees": [int(factor.degree(generator)) for generator in (cs, cp)],
                    "terms": terms,
                    "sha256": digest(factor),
                    "polynomial": str(factor) if terms <= 100 else None,
                    "named_unit_factor": library["normalized_key"](lifted) in branch["unit_keys"],
                }
            )
        record = {
            "name": name,
            "degree_x": degree_x,
            "leading_degree": int(leading.total_degree()),
            "leading_terms": int(len(leading.monomials())),
            "leading_sha256": digest(leading),
            "factors": factors,
        }
        records.append(record)
        print(canonical_json({"phase": "LEADING", **record}), flush=True)

    result = {
        "phase": "DONE",
        "cell": args.cell,
        "records": records,
        "terminal": "DEGREE12_INITIAL_LEADING_FACTORS_COMPILED",
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
