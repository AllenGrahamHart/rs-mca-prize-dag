#!/usr/bin/env python3
"""Independent audit for the cell-14 rank-one target projection."""

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
        rest = values[1:index]+values[index+1:]
        for tail in pairings(rest):
            yield ((first, values[index]),)+tail


def load_module(name, path):
    specification = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def main():
    projection = (EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_target_projection_modal.py").read_text()
    for snippet in (
        "target[a]*target[f]**2*lift(common_replacement.inverse())",
        "target[u]*target[v]",
        "equation.constant*cutter.linear",
        "pow(variable_univariate, PRIME, polynomial)",
        '"rankone_targetfree"',
    ):
        require(snippet in projection, f"projection construction: {snippet}")
    require(len(tuple(pairings(range(6)))) == 15, "perfect-matching census")

    census = load_module("rankone_census", EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_rankone_census.py")
    projection_hash = census.sha256_file(census.PROJECTION_SCRIPT)
    curve_hash = census.sha256_file(EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_curve_kernel_result.json")
    audited = [
        census.audit_shard(specification, projection_hash, curve_hash)
        for specification in census.SHARDS
    ]
    require(sum(row["case_count"] for row in audited) == 960, "audited cases")
    boundary = census.audit_boundary(curve_hash)
    require(boundary["case_count"] == boundary["unit_count"] == 4,
            "audited boundary")
    replay = census.audit_root_replay()
    require(replay["case_count"] == replay["pass_count"] == 960 and
            replay["field_root_count"] == 12880, "audited root replay")

    aggregate = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_rankone_census_result.json").read_text())
    primary = load_module("primary", NODE / "verify.py")
    primary.verify_payload(aggregate)
    for field, value in (("rankone_excluded_count", 959),
                         ("retained_case_count", 575)):
        mutant = copy.deepcopy(aggregate)
        mutant[field] = value
        try:
            primary.verify_payload(mutant)
        except RuntimeError:
            pass
        else:
            raise RuntimeError(f"mutation survived: {field}")
    mutant = copy.deepcopy(aggregate)
    mutant["shards"][0]["checked_field_roots"] -= 1
    try:
        primary.verify_payload(mutant)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("root-count mutation survived")
    print("audit=ok cases=960 field_roots=12880 direct=2848 mutations=3")


if __name__ == "__main__":
    main()
