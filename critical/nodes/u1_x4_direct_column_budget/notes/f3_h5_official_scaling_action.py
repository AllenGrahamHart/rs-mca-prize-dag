#!/usr/bin/env python3
"""Compile the official mu_n scaling action on the h=5 reciprocal system."""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from f3_h5_weighted_homogeneity import WEIGHTS, weighted_homogeneity_summary
from f3_h5_reciprocal_compatibility_compiler import TOP
from f3_h5_basefree_reciprocal_system import ALL_BARS


OFFICIAL_EXPONENTS = tuple(range(13, 42))


@dataclass(frozen=True)
class OfficialScalingRow:
    s: int
    n: int
    central_weight_gcd: int
    central_orbit_size: int


def official_scaling_rows() -> tuple[OfficialScalingRow, ...]:
    rows: list[OfficialScalingRow] = []
    central_weight = abs(WEIGHTS[ALL_BARS[0]])
    if central_weight != 5:
        raise AssertionError((ALL_BARS[0], central_weight))
    for s in OFFICIAL_EXPONENTS:
        n = 2**s
        stabilizer = gcd(n, central_weight)
        rows.append(
            OfficialScalingRow(
                s=s,
                n=n,
                central_weight_gcd=stabilizer,
                central_orbit_size=n // stabilizer,
            )
        )
    return tuple(rows)


def coefficient_weight_table() -> dict[str, int]:
    table = {str(variable): WEIGHTS[variable] for variable in TOP + ALL_BARS}
    expected = {
        "l5": 5,
        "l6": 4,
        "l7": 3,
        "l8": 2,
        "l9": 1,
        "bar_l5": -5,
        "bar_l6": -4,
        "bar_l7": -3,
        "bar_l8": -2,
        "bar_l9": -1,
    }
    if table != expected:
        raise AssertionError(table)
    return table


def official_scaling_summary() -> dict[str, int]:
    weighted = weighted_homogeneity_summary()
    rows = official_scaling_rows()
    if any(row.central_weight_gcd != 1 for row in rows):
        raise AssertionError(rows)
    if any(row.central_orbit_size != row.n for row in rows):
        raise AssertionError(rows)
    return {
        "first_s": rows[0].s,
        "last_s": rows[-1].s,
        "official_rows": len(rows),
        "central_stabilizer_size": rows[0].central_weight_gcd,
        "first_central_orbit_size": rows[0].central_orbit_size,
        "last_central_orbit_size": rows[-1].central_orbit_size,
        "weighted_pairwise_rows": weighted["pairwise_rows"],
        "weighted_unit_rows": weighted["unit_rows"],
    }


def main() -> None:
    summary = official_scaling_summary()
    print("h=5 official mu_n scaling action")
    print("coefficient weights:")
    for name, weight in coefficient_weight_table().items():
        print(f"  {name}: {weight}")
    print(
        "central chart bar_l5 != 0 has trivial stabilizer on official rows "
        "because gcd(5,2^s)=1"
    )
    print(
        "summary: "
        f"s={summary['first_s']}..{summary['last_s']} "
        f"rows={summary['official_rows']} "
        f"central_stabilizer={summary['central_stabilizer_size']} "
        f"central_orbit_size={summary['first_central_orbit_size']}.."
        f"{summary['last_central_orbit_size']} "
        f"weighted_rows={summary['weighted_pairwise_rows']}+"
        f"{summary['weighted_unit_rows']}"
    )
    print("H5_OFFICIAL_SCALING_ACTION_PASS")


if __name__ == "__main__":
    main()
