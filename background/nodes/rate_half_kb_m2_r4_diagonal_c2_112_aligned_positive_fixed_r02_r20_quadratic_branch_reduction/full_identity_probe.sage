#!/usr/bin/env sage
"""Compile symbolic full J/I mismatch coefficients for fixed assignments."""

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


def metric(value):
    value = value.parent()(value)
    return {
        "degree": int(value.total_degree()),
        "degrees": [int(value.degree(g)) for g in value.parent().gens()],
        "terms": int(len(value.monomials())),
        "sha256": digest(value),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--assignment", choices=("F04", "F05", "F06", "F07"), required=True)
    parser.add_argument("--identity", choices=("J", "I"), default="J")
    parser.add_argument("--coefficient-index", type=int, choices=(0, 1, 2), default=0)
    args = parser.parse_args()
    print(canonical_json({"phase": "START", "assignment": args.assignment}), flush=True)

    library = load_library()
    frontier = library["load_frontier"]()
    parent = frontier["PARENT"]
    atlas = parent["ATLAS"]
    source_u, source_v, source_z = parent["build_source_R"](args.assignment)
    print(canonical_json({"phase": "SOURCE_BUILT"}), flush=True)
    ring = parent["R"]
    field = parent["K"]
    polynomial_w = atlas["KW"]
    W = atlas["W"]
    b, c, d, w = map(field, ring.gens())
    def g_at(label):
        uu = sum(polynomial_w(source_u[index]) * field(label) ** index for index in range(3))
        vv = sum(polynomial_w(source_v[index]) * field(label) ** index for index in range(3))
        return polynomial_w(uu ** 2 - W * vv ** 2)

    j_labels = (field(2), field(1) / 2, b, 1 / b, c, d)
    i_labels = (1 / c, 1 / d, w, 1 / w, source_z, 1 / source_z)
    k_labels = (w, source_z, 1 / source_z, 1 / c, 1 / d)
    r_labels = (1 / w, *j_labels)

    def linear(label):
        return polynomial_w(W - field(label))

    def truncated_product(factors, maximum_index=2):
        coefficients = [field(1)] + [field(0)] * maximum_index
        leading = field(1)
        for factor in factors:
            factor = polynomial_w(factor)
            available = [
                field(factor[index]) if index <= factor.degree() else field(0)
                for index in range(maximum_index + 1)
            ]
            updated = [field(0)] * (maximum_index + 1)
            for left_index in range(maximum_index + 1):
                for right_index in range(maximum_index + 1 - left_index):
                    updated[left_index + right_index] += (
                        coefficients[left_index] * available[right_index]
                    )
            coefficients = updated
            leading *= field(factor.leading_coefficient())
        return coefficients, leading

    q_factors = [linear(c), linear(c), linear(d), linear(d)]
    if args.identity == "J":
        observed_factors = [g_at(label) for label in j_labels]
        expected_factors = [linear(label) for label in k_labels for _ in range(4)]
        expected_factors.extend(q_factors)
    else:
        observed_factors = [*q_factors, *(g_at(label) for label in i_labels)]
        expected_factors = [linear(label) for label in r_labels for _ in range(4)]
    print(
        canonical_json(
            {
                "phase": "FACTORS_BUILT",
                "identity": args.identity,
                "observed_factor_count": len(observed_factors),
                "expected_factor_count": len(expected_factors),
            }
        ),
        flush=True,
    )
    observed_truncated = truncated_product(observed_factors)
    expected_truncated = truncated_product(expected_factors)

    units = parent["named_units_R"](args.assignment)
    observed, observed_leading = observed_truncated
    expected, expected_leading = expected_truncated
    mismatch = [
        observed[index] * expected_leading
        - expected[index] * observed_leading
        for index in range(len(observed))
    ]
    coefficient_index = int(args.coefficient_index)
    assert mismatch[coefficient_index]
    coefficient = field(mismatch[coefficient_index])
    print(canonical_json({"phase": "COEFFICIENT", "index": coefficient_index}), flush=True)
    numerator = parent["primitive_R"](coefficient.numerator())
    denominator = parent["primitive_R"](coefficient.denominator())
    print(canonical_json({"phase": "NUMERATOR", "metric": parent["metric"](numerator)}), flush=True)
    denominator_support = parent["denominator_support_R"](denominator, units)
    essential, dropped = parent["essential"](numerator, units)
    print(canonical_json({"phase": "ESSENTIAL", "metric": parent["metric"](essential)}), flush=True)
    descended = parent["symmetric_cd_dict"](essential)
    print(canonical_json({"phase": "DESCENDED", "metric": metric(descended)}), flush=True)
    factor_records = []
    for factor, exponent in descended.factor():
        factor_metric = metric(factor)
        factor_records.append(
            {
                "exponent": int(exponent),
                "metric": factor_metric,
                "polynomial": str(factor) if factor_metric["terms"] <= 500 else None,
            }
        )
    record = {
        "first_nonzero_coefficient_index": int(coefficient_index),
        "raw_numerator_metric": parent["metric"](numerator),
        "denominator_support": denominator_support,
        "dropped_named_factors": dropped,
        "essential_metric": parent["metric"](essential),
        "descended_metric": metric(descended),
        "descended_factors": factor_records,
    }
    print(
        canonical_json(
            {"phase": "IDENTITY", "identity": args.identity, "record": record}
        ),
        flush=True,
    )

    result = {
        "phase": "DONE",
        "assignment": args.assignment,
        "identities": {args.identity: record},
        "terminal": "FULL_IDENTITY_NECESSARY_COEFFICIENTS_COMPILED",
    }
    print(canonical_json(result), flush=True)


if __name__ == "__main__":
    main()
