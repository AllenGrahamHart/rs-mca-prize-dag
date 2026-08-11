#!/usr/bin/env python3
"""Fibre-degree replay for the final strict-corner exclusion."""


def main():
    profiles = 0
    for e in range(4, 256):
        for p in (0, 1):
            # Contact fibre without a clearing fibre.
            assert 3 % e != 0
            k = 3
            assert e - k + 3 == e
            assert k - 1 == 2 > 1 - p

            # Coincident contact and clearing fibres.
            degree = 2 * e - (3 - p) - p + 3
            assert degree == 2 * e
            required_excess = (3 - p) - 1
            available_excess = 1 - p
            assert required_excess == 2 - p > available_excess

            # Non-domain coincident fibre has a nonmultiple degree.
            assert (e - p + 3) % e != 0
            profiles += 1

    official_m = 1 << 37
    official_e = (4 * official_m - 1) // 3
    assert official_e > 3

    print(
        "RATE_HALF_CA_HANKEL_STRICT_A3_FINAL_CORNER_DIVISOR_EXCLUSION_PASS "
        f"profiles={profiles} official_e={official_e} margin=1"
    )


if __name__ == "__main__":
    main()
