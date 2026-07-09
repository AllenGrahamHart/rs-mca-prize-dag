#!/usr/bin/env python3
"""Payment compiler for a finite h=5 central slice."""

from __future__ import annotations

from math import prod

from f3_h5_central_slice_fixedpoint_skeleton import slice_fixedpoint_rows
from f3_h5_official_scaling_action import official_scaling_rows


def finite_scheme_payment_summary() -> dict[str, int]:
    degrees = tuple(row.slice_degree_bound for row in slice_fixedpoint_rows())
    if degrees != (81, 72, 63, 54):
        raise AssertionError(degrees)
    bezout_bound = prod(degrees)
    scaling_rows = official_scaling_rows()
    if scaling_rows[0].s != 13 or scaling_rows[-1].s != 41:
        raise AssertionError(scaling_rows)
    if any(row.central_weight_gcd != 1 for row in scaling_rows):
        raise AssertionError(scaling_rows)
    if any(row.central_orbit_size != row.n for row in scaling_rows):
        raise AssertionError(scaling_rows)

    first = scaling_rows[0]
    first_payment = bezout_bound * first.n
    first_budget = first.n**3
    if first_payment >= first_budget:
        raise AssertionError((bezout_bound, first_payment, first_budget))
    if any(bezout_bound * row.n >= row.n**3 for row in scaling_rows):
        raise AssertionError(("finite central payment exceeds n^3", bezout_bound))

    return {
        "degree_rows": len(degrees),
        "degree_product": bezout_bound,
        "max_degree": max(degrees),
        "first_s": first.s,
        "last_s": scaling_rows[-1].s,
        "official_rows": len(scaling_rows),
        "first_orbit_size": first.central_orbit_size,
        "last_orbit_size": scaling_rows[-1].central_orbit_size,
        "first_payment": first_payment,
        "first_budget": first_budget,
        "first_margin": first_budget - first_payment,
        "first_n_square": first.n**2,
    }


def main() -> None:
    summary = finite_scheme_payment_summary()
    print("h=5 central finite-scheme payment")
    print(
        f"slice degree bounds product K={summary['degree_product']} "
        f"(max_degree={summary['max_degree']})"
    )
    print(
        f"official rows s={summary['first_s']}..{summary['last_s']} "
        f"count={summary['official_rows']} "
        f"central_orbit_size={summary['first_orbit_size']}.."
        f"{summary['last_orbit_size']}"
    )
    print(
        "first official row: "
        f"K={summary['degree_product']} < n^2={summary['first_n_square']} "
        f"and K*n={summary['first_payment']} < n^3={summary['first_budget']}"
    )
    print(
        "conditional target: row-wise saturated zero-dimensional central slice "
        "is enough; emptiness is stronger than needed"
    )
    print("H5_CENTRAL_FINITE_SCHEME_PAYMENT_PASS")


if __name__ == "__main__":
    main()
