#!/usr/bin/env python3
"""Verify the exact X4 d=1 high-width Johnson sum."""


N = 1 << 41
E0 = N // 4 + 1


def bound(e: int) -> int:
    denominator = 4 * e * e - N * (e + 1)
    assert denominator > 0
    return N * (e - 1) // denominator


def main() -> None:
    assert 4 * E0 * E0 - N * (E0 + 1) == 4
    assert bound(E0) == N * N // 16

    samples = (E0, E0 + 1, E0 + 17, 3 * N // 8, N // 2)
    for e in samples:
        assert bound(e) <= N * N // 16

    widths = N // 2 - E0 + 1
    assert widths == N // 4
    aggregate = widths * (N * N // 16)
    assert aggregate == N**3 // 64

    # Exact coefficient check for the multiplied inequality at e=E0+x.
    assert N * N + 8 * N - 16 > 0
    print(
        "X4_LOW_DIFFERENCE_JOHNSON_HIGHWIDTH_PASS "
        f"first_width={E0} widths={widths} aggregate={aggregate}"
    )


if __name__ == "__main__":
    main()
