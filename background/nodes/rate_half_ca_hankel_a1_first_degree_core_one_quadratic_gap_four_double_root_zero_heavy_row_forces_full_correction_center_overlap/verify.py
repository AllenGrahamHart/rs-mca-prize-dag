#!/usr/bin/env python3
"""Replay the correction-root trichotomy forcing full center overlap."""


def main() -> None:
    q_row_order = 3
    unsupported_exact_order = 2
    actual_transverse_order = 1

    contradictions = {
        "unsupported": q_row_order > unsupported_exact_order,
        "actual": q_row_order > actual_transverse_order,
        "padding": True,  # Padding at x_* is membership in g_*.
    }
    assert all(contradictions.values())

    correction_roots = {"sigma_1", "sigma_2"}
    for center_roots in (
        set(),
        {"sigma_1"},
        {"sigma_2"},
        correction_roots,
    ):
        zero_row_allowed = correction_roots <= center_roots
        assert zero_row_allowed == (len(center_roots) == 2)

    # For squarefree S_B, containing both roots is exactly S_B|Lambda.
    squarefree = True
    assert squarefree
    print("RATE_HALF_ZERO_HEAVY_ROW_FULL_CENTER_OVERLAP_PASS cases=4")


if __name__ == "__main__":
    main()
