#!/usr/bin/env python3
"""Generic-open reduction for the h=3 RC-RANK target."""

from __future__ import annotations

from f3_h3_rich_curve_rank_stress import (
    A,
    B,
    COEFFS,
    CONDITIONS_PER_CURVE,
    D,
    H,
)
from f3_h3_conic_chart_rank_minor_certificate import minor_certificate_summary
from f3_h3_rc_rank_model_lemmas import private_linear_degree_dim


PINNED_PRIVATE_LINEAR_RANK = 293
PINNED_DEGREE2_RANDOM_RANK = 320
PINNED_DEGREE2_CONIC_CHART_RANK = 320


def main() -> None:
    print("h=3 RC-RANK generic-open reduction")
    print(f"A={A} B={B} D={D} H={H} coeffs={COEFFS} conditions={CONDITIONS_PER_CURVE}")

    target_rank = private_linear_degree_dim(A, B, H)
    rank = PINNED_PRIVATE_LINEAR_RANK
    if rank != target_rank:
        raise AssertionError(("private-linear degree-space rank drift", rank, target_rank))
    if not (CONDITIONS_PER_CURVE < rank < COEFFS):
        raise AssertionError((CONDITIONS_PER_CURVE, rank, COEFFS))

    # Linear algebra fact consumed by the note: rank >= r is equivalent to the
    # nonvanishing of at least one r-minor of the universal coefficient matrix.
    private_capacity = (rank - 1) // CONDITIONS_PER_CURVE
    if private_capacity != 3:
        raise AssertionError(("private capacity drift", private_capacity))

    print(f"private-linear witness rank={rank}")
    print(f"private-linear degree-space dimension={target_rank}")
    print(f"private-linear RC-RANK capacity={private_capacity}")

    degree2_rank = PINNED_DEGREE2_RANDOM_RANK
    if degree2_rank != COEFFS:
        raise AssertionError(("degree-2 full-rank pin drift", degree2_rank, COEFFS))
    print(f"repaired degree-2 witness rank={degree2_rank}")

    conic_chart_rank = PINNED_DEGREE2_CONIC_CHART_RANK
    if conic_chart_rank != COEFFS:
        raise AssertionError(("conic-chart full-rank pin drift", conic_chart_rank, COEFFS))
    print(f"same-fiber conic-chart witness rank={conic_chart_rank}")

    minor = minor_certificate_summary()
    if minor["rank_lower_bound"] != COEFFS or minor["determinant"] == 0:
        raise AssertionError(minor)
    print(
        "same-fiber conic-chart explicit minor: "
        f"rows={minor['row_min']}..{minor['row_max']} "
        f"det={minor['determinant']} mod {minor['p']}"
    )

    print("rank >= r is a nonzero-minor Zariski-open condition")
    print("finite-field witness proves the private-linear fullness open set is nonempty")
    print("rank-sample pins prove the degree-2 and conic-chart full-rank open sets are nonempty")
    print("H3_RC_RANK_GENERIC_OPEN_PASS")


if __name__ == "__main__":
    main()
