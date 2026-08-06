#!/usr/bin/env python3
"""h=2 affine-coset cap for the h=3 lambda=1 scale branch."""

from __future__ import annotations

from dataclasses import dataclass
from math import comb

from f3_h2_rich_coset_optimized import K_RICH
from f3_h3_repeat_boundary_q0_cell import ceil_cuberoot
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_lambda_one_scale_compiler import lambda_one_scale_edges
from f3_h3_repeat_same_lambda_scale_count import scale_orbit_bound
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


OFFICIAL_EXPONENTS = tuple(range(13, 42))


@dataclass(frozen=True)
class ScaleCapRow:
    s: int
    n: int
    trivial_orbit_bound: int
    h2_orbit_bound: int
    combined_orbit_bound: int
    combined_pair_bound: int


def h2_affine_count_bound(n: int) -> int:
    return ceil_cuberoot((K_RICH**3) * (n**2))


def h2_scale_orbit_bound(n: int) -> int:
    # Each admissible scale orbit contributes three x-values, and the first two
    # affine membership conditions are bounded by the h=2 affine-coset pair cap.
    return h2_affine_count_bound(n) // 3


def combined_scale_orbit_bound(n: int) -> int:
    return min(scale_orbit_bound(n), h2_scale_orbit_bound(n))


def combined_scale_pair_bound(n: int) -> int:
    return comb(combined_scale_orbit_bound(n), 2)


def official_scale_cap_rows() -> tuple[ScaleCapRow, ...]:
    rows = []
    for s in OFFICIAL_EXPONENTS:
        n = 2**s
        trivial = scale_orbit_bound(n)
        h2 = h2_scale_orbit_bound(n)
        combined = min(trivial, h2)
        rows.append(
            ScaleCapRow(
                s=s,
                n=n,
                trivial_orbit_bound=trivial,
                h2_orbit_bound=h2,
                combined_orbit_bound=combined,
                combined_pair_bound=comb(combined, 2),
            )
        )
    return tuple(rows)


def verify_sample_rows() -> tuple[tuple[int, int, int, int], ...]:
    rows = []
    for p, n in (*WITNESS_ROWS, *CONTRAST_ROWS):
        actual = len(set(lambda_one_scale_edges(p, n).values()))
        combined = combined_scale_orbit_bound(n)
        if actual > combined:
            raise AssertionError((p, n, actual, combined))
        rows.append((p, n, actual, combined))
    return tuple(rows)


def scale_h2_cap_summary() -> dict[str, int]:
    samples = verify_sample_rows()
    official = official_scale_cap_rows()
    first_h2_better = next(row.s for row in official if row.h2_orbit_bound < row.trivial_orbit_bound)
    first = official[0]
    last = official[-1]
    if first.combined_orbit_bound != first.trivial_orbit_bound:
        raise AssertionError(first)
    if first_h2_better != 19:
        raise AssertionError(first_h2_better)
    if last.combined_orbit_bound != last.h2_orbit_bound:
        raise AssertionError(last)
    if any(row.combined_pair_bound >= row.n * row.n for row in official):
        raise AssertionError("combined pair bound should remain below n^2")
    return {
        "sample_rows": len(samples),
        "first_s": first.s,
        "last_s": last.s,
        "first_h2_better_s": first_h2_better,
        "first_combined_orbit_bound": first.combined_orbit_bound,
        "first_combined_pair_bound": first.combined_pair_bound,
        "last_combined_orbit_bound": last.combined_orbit_bound,
        "last_combined_pair_bound": last.combined_pair_bound,
    }


def main() -> None:
    summary = scale_h2_cap_summary()
    print("h=3 lambda=1 scale h=2 affine cap")
    print("scale branch uses forms 1+x and 1+omega*x as an h=2 affine-coset pair")
    for p, n, actual, combined in verify_sample_rows():
        print(f"  sample p={p} n={n}: actual_orbits={actual} combined_bound={combined}")
    print(
        "official summary: "
        f"s={summary['first_s']}..{summary['last_s']} "
        f"first_h2_better=2^{summary['first_h2_better_s']} "
        f"first_bound={summary['first_combined_orbit_bound']} "
        f"first_pair_bound={summary['first_combined_pair_bound']} "
        f"last_bound={summary['last_combined_orbit_bound']} "
        f"last_pair_bound={summary['last_combined_pair_bound']}"
    )
    print("H3_REPEAT_LAMBDA_ONE_SCALE_H2_CAP_PASS")


if __name__ == "__main__":
    main()
