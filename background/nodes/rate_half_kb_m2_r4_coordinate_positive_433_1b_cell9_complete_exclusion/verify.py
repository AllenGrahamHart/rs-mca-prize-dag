#!/usr/bin/env python3
"""Verify complete exclusion of all 105 cell-9 labels."""

import collections
import importlib.util
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
ROUTER = (
    ROOT / "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
)
ENDPOINT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell9_endpoint_roles_complete_exclusion"
)
QUOTIENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell9_remaining_generic_label_orbit_quotient"
)
OWNERS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_parallel_de_first_pair_complete_exclusion": (
        (0, 0), (0, 1), (2, 0), (2, 1),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_parallel_de_pairing11_14_common_f_exclusion": (
        (0, 11), (2, 11),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_parallel_de_pairing3_6_nested_quadratic_exclusion": (
        (0, 3), (2, 3),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_parallel_de_pairing4_7_9_10_nested_quadratic_exclusion": (
        (0, 4), (2, 4),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_parallel_de_pairing5_8_12_13_nested_quadratic_exclusion": (
        (0, 5), (2, 5),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_positive_de_pairing9_10_nested_quadratic_exclusion": (
        (0, 9),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_positive_de_pairing12_13_nested_quadratic_exclusion": (
        (0, 12),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_positive_de_pairing14_common_f_resultant_exclusion": (
        (0, 14),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_xi3_pairing0_reciprocal_square_exclusion": (
        (3, 0),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_xi3_pairing1_reciprocal_linear_exclusion": (
        (3, 1),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_xi3_pairing2_reciprocal_linear_exclusion": (
        (3, 2),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_xi3_pairing3_reciprocal_square_exclusion": (
        (3, 3),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_xi3_pairing4_nested_signfree_exclusion": (
        (3, 4),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_xi3_pairing5_nested_signfree_exclusion": (
        (3, 5),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_xi3_pairing7_quadratic_resultant_signfree_exclusion": (
        (3, 7),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_xi3_pairing8_quadratic_resultant_signfree_exclusion": (
        (3, 8),
    ),
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_xi3_pairing11_quadratic_resultant_signfree_exclusion": (
        (3, 11),
    ),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_statuses():
    identifiers = {ENDPOINT, QUOTIENT, *OWNERS}
    statuses = {}
    for identifier in identifiers:
        path = ROOT / "background/nodes" / identifier / "node.json"
        payload = json.loads(path.read_text())
        require(payload["node"]["id"] == identifier, f"node identity: {identifier}")
        statuses[identifier] = payload["node"]["status"]
    return statuses


def compile_active_orbits():
    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    return [
        tuple(tuple(label) for label in orbit)
        for orbit in router.compile_orbits()
        if all(label[0] <= 4 for label in orbit)
    ]


def validate(owners, statuses):
    require(len(owners) == 17, "owner packet count")
    require(
        set(statuses) == {ENDPOINT, QUOTIENT, *owners}
        and all(status == "PROVED" for status in statuses.values()),
        "proved dependency cover",
    )
    orbits = compile_active_orbits()
    require(len(orbits) == 24, "active orbit count")
    size_profile = collections.Counter(map(len, orbits))
    require(size_profile == {1: 1, 2: 9, 4: 14}, "orbit size profile")
    active_labels = {label for orbit in orbits for label in orbit}
    require(
        active_labels == {(xi, pairing) for xi in range(5) for pairing in range(15)}
        and len(active_labels) == 75,
        "active raw-label cover",
    )
    representatives = {orbit[0] for orbit in orbits}
    paid = [representative for values in owners.values() for representative in values]
    require(
        len(paid) == len(set(paid)) == 24
        and set(paid) == representatives,
        "exact representative ownership",
    )
    orbit_by_representative = {orbit[0]: orbit for orbit in orbits}
    paid_labels = {
        label
        for representative in paid
        for label in orbit_by_representative[representative]
    }
    require(paid_labels == active_labels, "transported label cover")
    endpoint_labels = {(xi, pairing) for xi in (5, 6) for pairing in range(15)}
    require(
        len(endpoint_labels) == 30
        and not endpoint_labels & active_labels
        and len(endpoint_labels | paid_labels) == 105,
        "105-label terminal cover",
    )
    return {
        "owners": len(owners),
        "orbits": len(orbits),
        "active_labels": len(active_labels),
        "endpoint_labels": len(endpoint_labels),
        "total_labels": len(endpoint_labels | paid_labels),
    }


def main():
    result = validate(OWNERS, load_statuses())
    print(
        "PASS cell-9 complete exclusion: "
        f"owners={result['owners']} orbits={result['orbits']} "
        f"labels={result['endpoint_labels']}+{result['active_labels']}="
        f"{result['total_labels']}"
    )


if __name__ == "__main__":
    main()
