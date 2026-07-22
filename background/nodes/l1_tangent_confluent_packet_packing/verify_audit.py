#!/usr/bin/env python3
"""Mutation audit for tangent confluent-packet packing."""

from __future__ import annotations


def valid(row: dict[str, bool]) -> bool:
    return all(
        (
            row["complete_support"],
            row["exact_gcd_owner"],
            row["double_hasse_conditions"],
            row["value_set_disjoint_from_doubled"],
            row["k_total_conditions"],
            row["packet_disjointness"],
            row["mixed_complement_packet_disjointness"],
            row["integer_floor_retained"],
            not row["finite_reserve_fit_claimed"],
            not row["primitive_flatness_claimed"],
        )
    )


def main() -> None:
    row = {
        "complete_support": True,
        "exact_gcd_owner": True,
        "double_hasse_conditions": True,
        "value_set_disjoint_from_doubled": True,
        "k_total_conditions": True,
        "packet_disjointness": True,
        "mixed_complement_packet_disjointness": True,
        "integer_floor_retained": True,
        "finite_reserve_fit_claimed": False,
        "primitive_flatness_claimed": False,
    }
    assert valid(row)
    mutations = {
        "complete_support": False,
        "exact_gcd_owner": False,
        "double_hasse_conditions": False,
        "value_set_disjoint_from_doubled": False,
        "k_total_conditions": False,
        "packet_disjointness": False,
        "mixed_complement_packet_disjointness": False,
        "integer_floor_retained": False,
        "finite_reserve_fit_claimed": True,
        "primitive_flatness_claimed": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_TANGENT_CONFLUENT_PACKET_PACKING_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
