#!/usr/bin/env python3
"""Verify the official-rate source-scale and rate-quarter boundary sieve."""

from __future__ import annotations


NODE = "pma_official_rate_small_source_degree_sieve"


def main() -> None:
    rows = 0
    sieved = 0
    quarter_rows = 0
    quarter_upper = 0
    quarter_paid = 0
    equality_seen = False
    endpoint_scale_seen = False

    mutation_m_endpoint = False
    mutation_background_shift = False
    mutation_defect_cap = False
    mutation_strict_half = False
    mutation_core_size = False

    for r in (2, 4, 8, 16):
        for k in range(1, 401):
            total = (r - 1) * k + 1
            for ell in range(1, total + 1):
                rows += 1
                m, b = divmod(total, ell)
                assert total == m * ell + b
                assert 0 <= b < ell

                if m <= r - 2:
                    sieved += 1
                    assert ell >= k + 1
                    assert k - 1 < ell

                if m == r - 2 and r > 2:
                    endpoint_scale_seen = True
                    assert ell >= k + 1

                if m == r - 1 and ell <= k:
                    mutation_m_endpoint = True

                if r != 4 or m != 4:
                    continue

                quarter_rows += 1
                d0 = (3 * ell + 1) // 2
                upper_exists = ell < d0 < 2 * ell and d0 <= k - 1
                threshold = 2 * b >= ell + 8
                assert upper_exists == threshold
                assert (3 * ell <= 2 * (k - 1)) == threshold
                if upper_exists:
                    quarter_upper += 1
                else:
                    quarter_paid += 1
                    assert 4 * k >= 4

                equality_seen |= 2 * b == ell + 8 and upper_exists

                # Valid rows have a congruence gap below the equality endpoint;
                # ell+7 and ell+6 are equivalent to ell+8.  Ell+5 is the first
                # weakening that admits a false row.
                wrong_background = 2 * b >= ell + 5
                mutation_background_shift |= wrong_background != upper_exists

                wrong_cap = ell < d0 < 2 * ell and d0 <= k
                mutation_defect_cap |= wrong_cap != upper_exists

                wrong_d0 = 3 * ell // 2 + 1
                wrong_strict = ell < wrong_d0 < 2 * ell and wrong_d0 <= k - 1
                mutation_strict_half |= wrong_strict != upper_exists

                # Replacing the physical (k-1)-core by a k-core would lead to
                # the spurious threshold 2b>=ell on the same printed row.
                wrong_core = 2 * b >= ell
                mutation_core_size |= wrong_core != upper_exists

    assert rows > 2_000_000
    assert sieved > 1_000_000
    assert quarter_rows > 5_000
    assert quarter_upper > 0 and quarter_paid > 0
    assert equality_seen
    assert endpoint_scale_seen
    mutations = (
        mutation_m_endpoint
        + mutation_background_shift
        + mutation_defect_cap
        + mutation_strict_half
        + mutation_core_size
    )
    assert mutations == 5, {
        "m_endpoint": mutation_m_endpoint,
        "background_shift": mutation_background_shift,
        "defect_cap": mutation_defect_cap,
        "strict_half": mutation_strict_half,
        "core_size": mutation_core_size,
    }

    print(
        f"{NODE}_PASS rows={rows} sieved={sieved} "
        f"quarter_rows={quarter_rows} quarter_upper={quarter_upper} "
        f"quarter_paid={quarter_paid} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
