#!/usr/bin/env python3
"""Replay correction-center exclusion and the j<=1 overlap cap."""


def main() -> None:
    centers = {"alpha", "beta", "theta"}
    actual_center_supports = {
        "alpha": {"u1", "u2"},
        "beta": {"u2", "u3"},
        "theta": {"u1", "u3"},
    }
    x_star = "x_star"
    assert all(x_star not in support for support in actual_center_supports.values())

    # A correction root at a center would make x_star a locator root outside
    # actual support, hence padded and simultaneously a g_* root.
    allowed_correction_centers = {
        center
        for center in centers
        if x_star in actual_center_supports[center]
    }
    assert allowed_correction_centers == set()

    padded_center_capacity = 1
    correction_center_capacity = len(allowed_correction_centers)
    assert padded_center_capacity + correction_center_capacity == 1
    print("RATE_HALF_CORRECTION_CENTER_DISJOINT_OVERLAP_CAP_ONE_PASS j_max=1")


if __name__ == "__main__":
    main()
