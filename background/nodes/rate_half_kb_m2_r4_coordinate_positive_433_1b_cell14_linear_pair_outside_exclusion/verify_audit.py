#!/usr/bin/env python3
"""Independent audit for the cell-14 linear-pair exclusion."""

import copy
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, values[index]),) + tail


def main():
    script = (EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_generic_fiber_modal.py").read_text()
    for snippet in (
        "records = (\n        a_pair, a_pair, -a_pair",
        "primary = (a, a, a, u, v, f, f)[xi_index]",
        "coefficient_a*constant*constant",
        "boundary = constant.numer.gcd(linear.numer)",
        '"t2_plus_r2": t_pair*t_pair+r_common*r_common',
    ):
        require(snippet in script, f"source construction: {snippet}")

    matchings = tuple(pairings(range(6)))
    require(len(matchings) == 15 and
            all((0, 1) in matchings[index] for index in range(3)) and
            all((0, 1) not in matchings[index] for index in range(3, 15)),
            "three residual-de matchings")

    aggregate = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_linear_pair_census_result.json").read_text())
    open_payload = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_linear_pair_pairings1_2_open_result.json").read_text())
    profiles = {}
    for row in open_payload["rows"]:
        cut = row["parameter_cuts"][0]
        profile = tuple((factor["degree"], factor["multiplicity"])
                        for factor in cut["boundary_factors"])
        profiles.setdefault(row["xi_index"], set()).add(
            (cut["degree"], cut["terms"], cut["boundary_degree"], profile)
        )
    require(profiles[0] == profiles[1] and len(profiles[0]) == 1 and
            next(iter(profiles[0]))[:3] == (0, 1, 60), "role-0/1 profile")
    require(len(profiles[2]) == 1 and
            next(iter(profiles[2]))[:3] == (0, 1, 82), "role-2 profile")

    spec = importlib.util.spec_from_file_location("primary", NODE / "verify.py")
    primary = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(primary)
    primary.verify_payload(aggregate)
    for field, value in (("unit_ideal_count", 1775),
                         ("retained_outside_case_count", 1535)):
        mutant = copy.deepcopy(aggregate)
        mutant[field] = value
        try:
            primary.verify_payload(mutant)
        except RuntimeError:
            pass
        else:
            raise RuntimeError(f"mutation survived: {field}")
    mutant = copy.deepcopy(aggregate)
    mutant["rows"][0]["boundary_factor_count"] -= 1
    try:
        primary.verify_payload(mutant)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("boundary-count mutation survived")
    print("audit=ok cases=144 matching_indices=3 boundary_profiles=2 mutations=3")


if __name__ == "__main__":
    main()
