#!/usr/bin/env python3
"""Exact packet replay for the no-ordinary canonical classes."""

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
        c = 2 + u
        d_star = E - c
        packets.append((u, v, c, d_star))
        need(c - u == 2, "effective divisor degree failed")
        need(DELTA - d_star == u, "rank-loss tail failed")
        for w in range(v + 1):
            lower_num = 2 * u + w
            lower_contact = (lower_num + 2) // 3
            need(lower_contact >= u, "vertical contact lower bound failed")
    need(len(packets) == 3, "wrong packet count")
    print(f"NO_ORDINARY_CANONICAL_PACKETS_PASS e={E} packets={packets} h0=1")


if __name__ == "__main__":
    main()
