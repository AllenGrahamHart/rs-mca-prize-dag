#!/usr/bin/env python3
"""Replay the exact center-deficit/overlap ledger."""

from itertools import product


def main() -> None:
    cases = 0
    for deficits in product((0, 1), repeat=3):
        d_a = sum(deficits)
        if d_a > 1:
            continue
        for corrections in product((0, 1), repeat=3):
            # A correction center must already be a padded-heavy center.
            if any(correction and not deficit for correction, deficit in zip(corrections, deficits)):
                continue
            g_centers = {i for i, value in enumerate(deficits) if value}
            correction_centers = {i for i, value in enumerate(corrections) if value}
            j_centers = g_centers | correction_centers
            assert correction_centers <= g_centers
            assert len(j_centers) == d_a
            assert (d_a == 0 and len(j_centers) == 0) or d_a == 1
            cases += 1

    assert cases == 7
    print("RATE_HALF_SQUAREFREE_EXACT_DEFICIT_LEDGER_PASS cases=7 j=d_A")


if __name__ == "__main__":
    main()
