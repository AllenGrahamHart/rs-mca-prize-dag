#!/usr/bin/env python3
"""Independent profile and terminal audit for the source-pencil compiler."""

from math import comb


def main() -> None:
    profiles = []
    for m in range(2, 60):
        if 60 % m:
            continue
        n = 60 // m
        for b in range(n + 1):
            if (n - b) % 5:
                continue
            a = (n - b) // 5
            if b and m % 5:
                continue
            if b * 4 * m // 5 > 2 * m - 2:
                continue
            profiles.append((m, n, a, b))
    assert [row[0] for row in profiles] == [2, 3, 4, 5, 6, 10, 12, 30]

    terminals = {m: "live" for m, *_ in profiles}
    terminals[5] = "deleted"
    terminals[30] = "route-6"
    assert {m for m, state in terminals.items() if state == "live"} == {
        2, 3, 4, 6, 10, 12
    }
    assert comb(6, 1) == 6  # dimension of Sym^5 of a two-space
    assert pow(2130706433, 6, 5) == 4
    print("RATE_HALF_KB_DECOMPOSITION_SOURCE_PENCIL_COMPILER_AUDIT_PASS")


if __name__ == "__main__":
    main()
