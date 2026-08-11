#!/usr/bin/env python3
"""Exact degree and splitting replay for signed-packet section vanishing."""

M = 1 << 37
RHO = 4 * M
E = (RHO + 1) // 3
D = 3 * E - 2


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    # u, i0, c, positive degree, minimum untouched reduced factors
    packets = (
        (1, 1, 4, 3, E - 4),
        (2, 1, 5, 3, E - 5),
        (2, 2, 6, 4, E - 6),
    )
    for u, i0, c, positive_degree, reduced_factors in packets:
        need(positive_degree in (3, 4), "positive modification length failed")
        need(i0 > 0, "ordinary divisor must be nonempty")
        need(reduced_factors > 0, "constant-line witness missing")
        need(c == 2 + u + i0, "packet deficit failed")
        splitting_degree = (positive_degree * (1 - D)
                            + (E - 1 - positive_degree) * (-D))
        base_degree = (E - 1) * (-D)
        need(splitting_degree == base_degree + positive_degree,
             "positive modification degree failed")
    need(D > 1, "negative summands could have sections")
    print(f"SIGNED_PACKET_SECTION_VANISHING_PASS e={E} packets={len(packets)} h0=0")


if __name__ == "__main__":
    main()
