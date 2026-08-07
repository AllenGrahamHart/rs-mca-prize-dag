#!/usr/bin/env sage
"""Compile the full-J logarithmic-derivative condition at W=0."""

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
        "--assignment",
        choices=("F04", "F05", "F06", "F07"),
        default="F04",
    )
    args = parser.parse_args()
    print(
        canonical_json({"phase": "START", "assignment": args.assignment}),
        flush=True,
    )

    library = load_library()
    frontier = library["load_frontier"]()
    parent = frontier["PARENT"]
    atlas = parent["ATLAS"]
    source_u, source_v, source_z = parent["build_source_R"](args.assignment)
    ring = parent["R"]
    field = parent["K"]
    polynomial_w = atlas["KW"]
    W = atlas["W"]
    b, c, d, w = map(field, ring.gens())

    def g_at(label):
        uu = sum(
            polynomial_w(source_u[index]) * field(label) ** index
            for index in range(3)
        )
        vv = sum(
            polynomial_w(source_v[index]) * field(label) ** index
            for index in range(3)
        )
        return polynomial_w(uu ** 2 - W * vv ** 2)

    observed_labels = (field(2), field(1) / 2, b, 1 / b, c, d)
    expected_labels = (w, source_z, 1 / source_z, 1 / c, 1 / d)
    observed_factors = [g_at(label) for label in observed_labels]

    observed_log = field(0)
    observed_metrics = []
    for factor in observed_factors:
        assert factor[0]
        contribution = field(factor[1]) / field(factor[0])
        observed_log += contribution
        observed_metrics.append(parent["metric"](contribution.numerator()))

    expected_log = -4 * sum(1 / field(label) for label in expected_labels)
    expected_log -= 2 / c + 2 / d
    mismatch = field(observed_log - expected_log)
    assert mismatch
    numerator = parent["primitive_R"](mismatch.numerator())
    denominator = parent["primitive_R"](mismatch.denominator())
    units = parent["named_units_R"](args.assignment)
    unit_keys = {
        str(factor / factor.lc())
        for value in units
        for factor, _ in ring(value).factor()
    }
    denominator_factors = []
    denominator_all_named = True
    for factor, exponent in denominator.factor():
        named = str(factor / factor.lc()) in unit_keys
        denominator_all_named = denominator_all_named and named
        factor_metric = parent["metric"](factor)
        denominator_factors.append(
            {
                "exponent": int(exponent),
                "metric": factor_metric,
                "named_unit": named,
                "polynomial": str(factor) if factor_metric["terms"] <= 500 else None,
            }
        )
    essential, dropped = parent["essential"](numerator, units)
    descended = parent["symmetric_cd_dict"](essential)

    def metric(value):
        value = value.parent()(value)
        return {
            "degree": int(value.total_degree()) if value else -1,
            "degrees": [int(value.degree(generator)) for generator in value.parent().gens()],
            "terms": int(len(value.monomials())) if value else 0,
            "sha256": digest(value),
        }

    print(
        canonical_json(
            {
                "phase": "LOG_DERIVATIVE_COMPILED",
                "observed_factor_count": len(observed_factors),
                "expected_linear_factor_count": 24,
                "observed_contribution_numerators": observed_metrics,
                "raw_numerator": parent["metric"](numerator),
                "denominator": parent["metric"](denominator),
                "denominator_factors": denominator_factors,
                "dropped_named_factors": dropped,
                "essential": parent["metric"](essential),
                "descended": metric(descended),
            }
        ),
        flush=True,
    )
    factors = []
    for factor, exponent in descended.factor():
        factor_metric = metric(factor)
        factors.append(
            {
                "exponent": int(exponent),
                "metric": factor_metric,
                "polynomial": str(factor) if factor_metric["terms"] <= 5000 else None,
            }
        )
    print(
        canonical_json(
            {
                "phase": "DONE",
                "assignment": args.assignment,
                "factors": factors,
                "denominator_all_named": denominator_all_named,
                "terminal": "FULL_J_LOG_DERIVATIVE_NECESSARY_CONDITION_COMPILED",
            }
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
