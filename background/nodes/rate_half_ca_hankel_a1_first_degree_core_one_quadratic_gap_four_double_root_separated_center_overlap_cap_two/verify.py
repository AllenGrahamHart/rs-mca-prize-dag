#!/usr/bin/env python3
"""Replay the disjoint center-overlap capacity bound."""


def main() -> None:
    centers = {"alpha", "beta", "theta"}
    endpoint_centers = {"alpha", "beta"}

    correction_center_sets = [set(), {"theta"}]
    padded_center_sets = [set()] + [{center} for center in centers]

    cases = 0
    for correction in correction_center_sets:
        assert not (correction & endpoint_centers)
        for padded in padded_center_sets:
            if correction & padded:
                continue
            assert len(correction) <= 1
            assert len(padded) <= 1
            assert len(correction | padded) <= 2
            cases += 1

    assert cases == 7
    print("RATE_HALF_SEPARATED_CENTER_OVERLAP_CAP_TWO_PASS cases=7")


if __name__ == "__main__":
    main()
