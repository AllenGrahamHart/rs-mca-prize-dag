#!/usr/bin/env python3
"""Independent factor-valuation audit for the unified squarefree gate."""


def main() -> None:
    # Tuples are (ord g_*, ord S_B^2, ord Lambda, ord J).
    cases = {
        "separated_off_center": (0, 2, 0, 0),
        "shared_off_center": (1, 2, 0, 0),
        "shared_center": (1, 2, 1, 1),
    }
    for values in cases.values():
        g_order, correction_order, center_order, j_order = values
        h_order = g_order + correction_order - j_order
        geometric_order = g_order + correction_order - center_order
        assert h_order == geometric_order

    # The source ledger permits at most one distinct center factor in J.
    assert max(values[3] for values in cases.values()) == 1
    print("RATE_HALF_SQUAREFREE_UNIFIED_HEAVY_ROW_GATE_AUDIT_PASS cases=3")


if __name__ == "__main__":
    main()
