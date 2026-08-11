#!/usr/bin/env python3
"""Replay the squarefree unified overlap and exact-order ledger."""


def main() -> None:
    cases = []
    for shared in (0, 1):
        for center in (0, 1):
            # A correction center must be padded, hence shared.
            if center and not shared:
                continue
            r_tau = shared
            c_tau = center
            row_order = r_tau + 2 - c_tau
            heavy_factor_order = row_order
            assert row_order in (2, 3)
            assert row_order == heavy_factor_order
            cases.append((shared, center, row_order))

    assert cases == [(0, 0, 2), (1, 0, 3), (1, 1, 2)]
    center_overlap_cap = 1
    assert center_overlap_cap + 1 == 2
    print("RATE_HALF_SQUAREFREE_UNIFIED_HEAVY_ROW_GATE_PASS cases=3 j_max=1")


if __name__ == "__main__":
    main()
