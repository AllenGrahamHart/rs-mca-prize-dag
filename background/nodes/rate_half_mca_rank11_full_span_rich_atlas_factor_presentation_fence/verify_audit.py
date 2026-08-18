#!/usr/bin/env python3
"""Independent dimension and Gaussian-count audit."""


def qbinom_5_2(q: int) -> int:
    return ((q**5 - 1) * (q**4 - 1)) // ((q**2 - 1) * (q - 1))


def main() -> None:
    h = 38_385
    d = h + 4
    ambient = h + d
    family = 10 * (d - 4)
    product = max(
        2 * (a - 1) + 5 * (b - 4)
        for a in range(1, ambient - 3)
        for b in (ambient - a,)
        if b >= 4
    )
    assert (ambient, family, product, family - product) == (
        76_774,
        383_850,
        383_845,
        5,
    )
    assert 4 * qbinom_5_2(16) == 71_862_340
    assert 2_097_152**5 > 32 * (ambient + 1) ** 2
    assert ambient < 1_048_576
    print("RANK11_RICH_ATLAS_FACTOR_FENCE_AUDIT_PASS gap=5 q16=71862340")


if __name__ == "__main__":
    main()
