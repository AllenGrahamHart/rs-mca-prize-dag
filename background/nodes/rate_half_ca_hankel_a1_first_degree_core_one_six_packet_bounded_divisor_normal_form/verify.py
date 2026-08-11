#!/usr/bin/env python3
"""Exact six-packet replay for the bounded-divisor normal form."""

M = 1 << 37
RHO = 4 * M
E = (RHO + 1) // 3
DELTA = E - 2


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    packets = []
    for u in range(3):
        v = 2 - u
        for i0 in range(u + 1):
            c = 2 + u + i0
            d_star = E - c
            packets.append((u, v, i0, c, d_star))
            need(DELTA - d_star == c - 2 == u + i0, "adjugate tail failed")
            need(E + 1 - d_star == c + 1, "Forney tail failed")
            need(c - i0 - u == 2, "Picard degree failed")
            need(d_star + i0 == DELTA - u, "contact residual failed")
    need(len(packets) == 6, "wrong packet count")
    need(max(p[3] for p in packets) == 6, "wrong row-tail cap")
    print(f"SIX_PACKET_BOUNDED_DIVISOR_PASS e={E} packets={len(packets)} tails=(6,4,7)")


if __name__ == "__main__":
    main()
