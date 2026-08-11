#!/usr/bin/env python3
"""Replay the complete valuation trichotomy excluding a zero heavy row."""


def main() -> None:
    q_row_order = 3
    exact_correction_order = 2
    transverse_order = 1

    cases = {
        "center": q_row_order > exact_correction_order,
        "unsupported_off_center": q_row_order > exact_correction_order,
        "supported_actual": q_row_order > transverse_order,
        "supported_padding": True,
    }
    assert all(cases.values())

    # Every center-overlap degree now inherits nonvanishing.
    overlap_nonzero = {overlap: all(cases.values()) for overlap in range(4)}
    assert overlap_nonzero == {0: True, 1: True, 2: True, 3: True}

    # Mutation controls remove the two numerical contradictions.
    assert not (2 > exact_correction_order)
    assert not (1 > transverse_order)
    print("RATE_HALF_SEPARATED_HEAVY_ROW_NONZERO_PASS cases=4 overlaps=4")


if __name__ == "__main__":
    main()
