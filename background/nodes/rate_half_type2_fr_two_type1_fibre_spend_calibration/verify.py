#!/usr/bin/env python3
"""Exact replay of the two-type-1 fibre spend calibration."""

from __future__ import annotations


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def profile(m: int) -> dict[str, int]:
    n = 16 * m
    rho = 4 * m - 1
    a = 7 * m - 1
    capacity = (n - a) * m
    baseline_fibre_sum = 2 * (a - rho)
    baseline_spend = baseline_fibre_sum - rho
    required_spend = capacity // (4 * m - 1) + 1
    required_fibre_sum = rho + required_spend
    baseline_type2_cap = capacity // baseline_spend
    return {
        "rho": rho,
        "a": a,
        "capacity": capacity,
        "baseline_fibre_sum": baseline_fibre_sum,
        "baseline_spend": baseline_spend,
        "required_spend": required_spend,
        "required_fibre_sum": required_fibre_sum,
        "baseline_type2_cap": baseline_type2_cap,
    }


def check_projective_support_identity() -> None:
    # A concrete partition checks the support-complement bookkeeping in TFC1.
    fibres = [set(range(0, 12)), set(range(12, 24)), set(range(24, 27))]
    w = set().union(*fibres)
    supports = [w - fibre for fibre in fibres]
    check(len(w) == 27, "fixture joint support")
    check(supports[0] | supports[1] == w, "two projective supports cover W")
    check(supports[0] & fibres[0] == set(), "support is fibre complement")
    check(sum(len(fibre) for fibre in fibres) == len(w), "fibre partition")


def main() -> None:
    check_projective_support_identity()

    for m in (4, 8, 16, 64, 1024, 2**20, 2**37):
        row = profile(m)
        check(row["baseline_fibre_sum"] == 6 * m, f"baseline fibres m={m}")
        check(row["baseline_spend"] == 2 * m + 1, f"baseline spend m={m}")
        check(row["required_spend"] == 9 * m // 4 + 1, f"required spend m={m}")
        check(row["required_fibre_sum"] == 25 * m // 4, f"required fibres m={m}")
        check(
            row["required_fibre_sum"] - row["baseline_fibre_sum"] == m // 4,
            f"fibre gap m={m}",
        )
        check(
            row["baseline_type2_cap"] == 9 * m // 2 - 2,
            f"baseline type2 cap m={m}",
        )
        check(2 + row["baseline_type2_cap"] == 9 * m // 2, f"total cap m={m}")
        check(row["a"] - row["required_fibre_sum"] == 3 * m // 4 - 1, "tail")

    m = 2**37
    row = profile(m)
    total = 2 + row["baseline_type2_cap"]
    check(row["baseline_spend"] == 274877906945, "official baseline spend")
    check(row["required_spend"] == 309237645313, "official required spend")
    check(row["required_fibre_sum"] == 858993459200, "official fibre threshold")
    check(total == 618475290624, "official total cap")
    check(total - 4 * m == 68719476736, "official cap residual")
    check(row["required_spend"] - row["baseline_spend"] == 34359738368, "gap")

    print(
        "RH_TYPE2_FR_TWO_TYPE1_FIBRE_SPEND_PASS "
        f"m={m} baseline_spend={row['baseline_spend']} "
        f"required_spend={row['required_spend']} total_cap={total}"
    )


if __name__ == "__main__":
    main()
