#!/usr/bin/env python3
"""Exact cap-row replay for the rate-half multiplicative no-go fence."""

from math import ceil, comb, log2


N = 1 << 41
K = 1 << 40
SIGMA = 8_592_912_738
CHARGE_BITS = 256
TRIGGER_BITS = 216


def main() -> None:
    if SIGMA != (1 << 33) + 2_978_146:
        raise AssertionError("sigma decomposition changed")

    entropy_rows = 0
    exact_rows: list[tuple[int, int]] = []
    for e in range(1, 41):
        c = 1 << e
        quotient_n = N // c
        d = ceil(SIGMA / c)
        if e <= 33:
            r = 1 << (33 - e)
            if quotient_n != CHARGE_BITS * r or d < r + 1:
                raise AssertionError((e, quotient_n, d, r))
            if quotient_n - CHARGE_BITS * (d - 1) > 0:
                raise AssertionError((e, "entropy fence failed"))
            entropy_rows += 1
        else:
            if d != 1:
                raise AssertionError((e, d))
            value = comb(quotient_n, quotient_n // 2 + 1)
            exact_rows.append((e, value))

    maximum_scale, maximum = max(exact_rows, key=lambda row: row[1])
    expected = comb(128, 65)
    if maximum_scale != 34 or maximum != expected or expected <= 1:
        raise AssertionError((maximum_scale, maximum, expected))

    minimum_multiplier = (1 << TRIGGER_BITS) // maximum + 1
    if not (minimum_multiplier * maximum > (1 << TRIGGER_BITS)):
        raise AssertionError("strict trigger not crossed")
    if not ((minimum_multiplier - 1) * maximum <= (1 << TRIGGER_BITS)):
        raise AssertionError("multiplier is not minimal")

    # Removing the positive cap gap destroys the small-scale <=1 argument.
    mutated_d = ceil((1 << 33) / (1 << 33))
    if (1 << 8) - CHARGE_BITS * (mutated_d - 1) <= 0:
        raise AssertionError("endpoint mutation was not detected")

    print(
        "RATE_HALF_MULTIPLICATIVE_FLOOR_PASS "
        f"entropy_rows={entropy_rows} exact_rows={len(exact_rows)} "
        f"max_scale=2^34 max_bits={maximum.bit_length()} "
        f"minimum_multiplier={minimum_multiplier} "
        f"log2_min={log2(minimum_multiplier):.6f}"
    )


if __name__ == "__main__":
    main()
