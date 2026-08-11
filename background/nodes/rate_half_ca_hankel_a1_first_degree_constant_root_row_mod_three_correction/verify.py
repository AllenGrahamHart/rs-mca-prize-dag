#!/usr/bin/env python3
"""Exact residue replay for the scalar root-row correction law."""

M = 1 << 37
RHO = 4 * M
E = (RHO + 1) // 3


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def correction(c: int, t: int) -> int:
    return (t - c) % 3


def main() -> None:
    need(E % 3 == 0, "official e must be divisible by three")
    need([correction(c, 0) for c in range(3)] == [0, 2, 1],
         "full-overlap correction table failed")

    exact_packets = (
        # c, t, epsilon
        (2, 2, 0),
        (4, 1, 0),
        (5, 0, 1),
        (6, 0, 0),
    )
    for c, t, epsilon in exact_packets:
        need((c + epsilon - t) % 3 == 0,
             "known packet violates correction law")
        need(epsilon >= correction(c, t),
             "known packet misses minimum correction")

    for c in range(9):
        for t in range(9):
            eps = correction(c, t)
            need((c + eps - t) % 3 == 0, "residue solver failed")
            need(all((c + j - t) % 3 for j in range(eps)),
                 "correction was not minimal")
    print(f"ROOT_ROW_MOD_THREE_CORRECTION_PASS e={E} packets={len(exact_packets)}")


if __name__ == "__main__":
    main()
