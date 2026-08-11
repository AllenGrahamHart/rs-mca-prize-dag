#!/usr/bin/env python3
"""Check the exact bidirectional packing and heavy-localization bounds."""

import json
from pathlib import Path


def ceil_div(a, b):
    return -((-a) // b)


def bounds(e, arm, R):
    generic = ceil_div((R + 3) * e - 2, R + 5)
    if arm == "double":
        localized = ceil_div((R + 1) * e - 6, R + 2)
    else:
        localized = ceil_div(2 * (R + 2) * e - 8, 2 * R + 7)
    return generic, localized, max(generic, localized)


def check(e, arm, R):
    generic, localized, g = bounds(e, arm, R)
    s = (R + 5) * g - (R + 3) * e + 2
    assert s >= 0
    assert (R + 5) * (generic - 1) < (R + 3) * e - 2

    if arm == "double":
        assert (R + 2) * localized >= (R + 1) * e - 6
        assert (R + 2) * (localized - 1) < (R + 1) * e - 6
    else:
        assert (2 * R + 7) * localized >= 2 * (R + 2) * e - 8
        assert (2 * R + 7) * (localized - 1) < 2 * (R + 2) * e - 8
    return g


for test_e in (13, 101, 1009):
    for test_R in range(3):
        check(test_e, "double", test_R)
    for test_R in range(5):
        check(test_e, "two", test_R)

e = 183251937963
official_double = tuple(check(e, "double", R) for R in range(3))
official_two = tuple(check(e, "two", R) for R in range(5))
assert official_double == (109951162778, 122167958642, 137438953471)
assert official_two == (
    109951162778,
    122167958642,
    133274136700,
    140963029202,
    146601550370,
)

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
node_id = (
    "rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_"
    "minimum_pair_bidirectional_heavy_incidence_localization"
)
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[node_id]["status"] == "PROVED"

print(
    "RATE_HALF_QUADRATIC_MINIMUM_PAIR_BIDIRECTIONAL_HEAVY_"
    "INCIDENCE_LOCALIZATION_PASS",
    official_double,
    official_two,
)
