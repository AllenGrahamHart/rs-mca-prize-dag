#!/usr/bin/env python3
"""Formal isolation lemma for the h=5 central weighted-slice origin."""

from __future__ import annotations

from f3_h5_central_slice_tangent import slice_tangent_summary
from f3_h5_official_scaling_action import official_scaling_summary


def formal_isolation_summary() -> dict[str, int]:
    tangent = slice_tangent_summary()
    scaling = official_scaling_summary()
    if tangent["fixed_equation_diagonal_numerator"] != 3:
        raise AssertionError(tangent)
    if tangent["fixed_equation_diagonal_denominator"] != 4:
        raise AssertionError(tangent)
    if tangent["fixed_equation_det_numerator"] != 81:
        raise AssertionError(tangent)
    if tangent["fixed_equation_det_denominator"] != 256:
        raise AssertionError(tangent)
    # Official rows have n=2^s with s>=13.  Any row prime p satisfies
    # p == 1 mod n, so p is odd and p != 3; hence 81/256 is a unit.
    if scaling["first_s"] < 13 or scaling["central_stabilizer_size"] != 1:
        raise AssertionError(scaling)
    return {
        "variables": tangent["slice_tangent_rows"],
        "linear_num": tangent["fixed_equation_diagonal_numerator"],
        "linear_den": tangent["fixed_equation_diagonal_denominator"],
        "det_num": tangent["fixed_equation_det_numerator"],
        "det_den": tangent["fixed_equation_det_denominator"],
        "first_official_s": scaling["first_s"],
        "central_stabilizer_size": scaling["central_stabilizer_size"],
    }


def main() -> None:
    summary = formal_isolation_summary()
    print("h=5 central slice formal isolation")
    print(
        "fixed-equation linearization: "
        f"{summary['linear_num']}/{summary['linear_den']} times identity "
        f"on {summary['variables']} variables"
    )
    print(f"determinant={summary['det_num']}/{summary['det_den']}")
    print(
        "official rows have odd characteristic !=3, so the determinant is a unit"
    )
    print(
        "completed local fixed-point quotient at the normalized central origin "
        "is the residue field"
    )
    print("H5_CENTRAL_SLICE_FORMAL_ISOLATION_PASS")


if __name__ == "__main__":
    main()
