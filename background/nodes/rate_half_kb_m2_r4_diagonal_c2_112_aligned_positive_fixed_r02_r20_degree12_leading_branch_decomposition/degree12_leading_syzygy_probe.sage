#!/usr/bin/env sage
"""Compile bounded content-primitive pseudo-remainder steps for degree 12."""

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
    parser.add_argument("--steps", type=int, choices=tuple(range(1, 7)), default=3)
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
    assert len(r_factors) == 3
    selected = r_factors[2]
    left = branch["essential"]["E2"]
    right = branch["essential"]["E3"]

    coefficient_ring = PolynomialRing(QQ, names=("s", "p"), order="degrevlex")
    cs, cp = coefficient_ring.gens()

    def coefficient_x(value, degree):
        output = coefficient_ring(0)
        for monomial, coefficient in base(value).dict().items():
            if monomial[0] == degree:
                output += QQ(coefficient) * cs ** monomial[1] * cp ** monomial[2]
        return output

    def coefficient_metric(value):
        value = coefficient_ring(value)
        return {
            "degree": int(value.total_degree()) if value else -1,
            "degrees": [int(value.degree(generator)) for generator in (cs, cp)],
            "terms": int(len(value.monomials())) if value else 0,
            "sha256": digest(value),
            "polynomial": str(value) if value and len(value.monomials()) <= 100 else None,
        }

    def polynomial_metric(value):
        value = base(value)
        return {
            "degree": int(value.total_degree()) if value else -1,
            "degrees": [int(value.degree(generator)) for generator in (x, s, p)],
            "terms": int(len(value.monomials())) if value else 0,
            "sha256": digest(value),
        }

    def content_x(value):
        value = base(value)
        coefficients = [
            coefficient_x(value, degree)
            for degree in range(int(value.degree(x)) + 1)
        ]
        nonzero = [coefficient for coefficient in coefficients if coefficient]
        content = nonzero[0]
        for coefficient in nonzero[1:]:
            content = content.gcd(coefficient)
            if content.is_constant():
                break
        if content and content.lc() != 1:
            content /= content.lc()
        return coefficient_ring(content)

    def lift_coefficient(value):
        output = base(0)
        for monomial, coefficient in coefficient_ring(value).dict().items():
            output += QQ(coefficient) * s ** monomial[0] * p ** monomial[1]
        return output

    def primitive_x(value):
        value = base(value)
        content = content_x(value)
        if content.is_constant():
            return value, content
        quotient, remainder = value.quo_rem(lift_coefficient(content))
        assert not remainder
        return base(quotient), content

    print(
        canonical_json(
            {
                "phase": "INPUTS",
                "selected": polynomial_metric(selected),
                "left": polynomial_metric(left),
                "right": polynomial_metric(right),
            }
        ),
        flush=True,
    )

    records = []
    a = base(left)
    b = base(right)
    for index in range(1, args.steps + 1):
        degree_a = int(a.degree(x))
        degree_b = int(b.degree(x))
        if degree_a < degree_b:
            a, b = b, a
            degree_a, degree_b = degree_b, degree_a
        leading_a = coefficient_x(a, degree_a)
        leading_b = coefficient_x(b, degree_b)
        shift = degree_a - degree_b
        raw = base(
            lift_coefficient(leading_b) * a
            - lift_coefficient(leading_a) * x ** shift * b
        )
        assert not raw or raw.degree(x) < degree_a
        primitive, content = primitive_x(raw)
        record = {
            "index": index,
            "input_degrees_x": [degree_a, degree_b],
            "shift": shift,
            "leading_a": coefficient_metric(leading_a),
            "leading_b": coefficient_metric(leading_b),
            "raw": polynomial_metric(raw),
            "content": coefficient_metric(content),
            "primitive": polynomial_metric(primitive),
        }
        records.append(record)
        print(canonical_json({"phase": "STEP", **record}), flush=True)
        if not primitive or primitive == 1:
            break
        a, b = b, primitive
        if len(primitive.monomials()) > 100000:
            break

    result = {
        "phase": "DONE",
        "cell": args.cell,
        "selected_sha256": digest(selected),
        "steps": records,
        "terminal": "DEGREE12_LEADING_SYZYGY_PREFIX_COMPILED",
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
