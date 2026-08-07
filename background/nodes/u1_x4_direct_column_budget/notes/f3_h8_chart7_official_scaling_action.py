#!/usr/bin/env python3
"""Official root-scaling action for the h=8 chart-7 reciprocal target."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from math import gcd

from f3_h8_weighted_homogeneity import weighted_homogeneity_summary


OFFICIAL_EXPONENTS = tuple(range(13, 42))
CHART7_WEIGHT = 7


@dataclass(frozen=True)
class ScalingRow:
    exponent: int
    n: int
    gcd_weight_n: int
    orbit_size: int
    stabilizer_size: int


@lru_cache(maxsize=1)
def official_scaling_rows() -> tuple[ScalingRow, ...]:
    rows = []
    for exponent in OFFICIAL_EXPONENTS:
        n = 2**exponent
        g = gcd(CHART7_WEIGHT, n)
        stabilizer_size = g
        rows.append(
            ScalingRow(
                exponent=exponent,
                n=n,
                gcd_weight_n=g,
                orbit_size=n // stabilizer_size,
                stabilizer_size=stabilizer_size,
            )
        )
    return tuple(rows)


@lru_cache(maxsize=1)
def official_scaling_summary() -> dict[str, int]:
    weighted = weighted_homogeneity_summary()
    rows = official_scaling_rows()
    if weighted["chart7_numerator_weight"] != CHART7_WEIGHT:
        raise AssertionError(weighted)
    if weighted["chart7_denominator_weight"] != -CHART7_WEIGHT:
        raise AssertionError(weighted)
    if any(row.gcd_weight_n != 1 for row in rows):
        raise AssertionError(rows)
    if any(row.orbit_size != row.n or row.stabilizer_size != 1 for row in rows):
        raise AssertionError(rows)
    return {
        "rows": len(rows),
        "first_s": rows[0].exponent,
        "last_s": rows[-1].exponent,
        "chart7_weight": CHART7_WEIGHT,
        "max_gcd": max(row.gcd_weight_n for row in rows),
        "min_orbit_size": min(row.orbit_size for row in rows),
        "max_orbit_size": max(row.orbit_size for row in rows),
        "max_stabilizer_size": max(row.stabilizer_size for row in rows),
    }


def main() -> None:
    summary = official_scaling_summary()
    print("h=8 chart-7 official scaling action")
    print("support scaling by gamma in mu_n sends c_i -> gamma^(16-i)c_i")
    print("chart denominator bar_c9 has weight -7")
    for row in official_scaling_rows():
        if row.exponent in (summary["first_s"], 16, 32, summary["last_s"]):
            print(
                f"  s={row.exponent}: n={row.n} gcd(7,n)={row.gcd_weight_n} "
                f"orbit_size={row.orbit_size} stabilizer={row.stabilizer_size}"
            )
    print(
        "summary: "
        f"rows={summary['rows']} "
        f"s_range={summary['first_s']}..{summary['last_s']} "
        f"chart7_weight={summary['chart7_weight']} "
        f"max_gcd={summary['max_gcd']} "
        f"orbit_size_range={summary['min_orbit_size']}..{summary['max_orbit_size']} "
        f"max_stabilizer_size={summary['max_stabilizer_size']}"
    )
    print("H8_CHART7_OFFICIAL_SCALING_ACTION_PASS")


if __name__ == "__main__":
    main()
