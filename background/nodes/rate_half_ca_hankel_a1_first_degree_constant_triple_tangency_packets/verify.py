#!/usr/bin/env python3
"""Exact arithmetic replay for the constant-residual tangency packets."""

M = 1 << 37
RHO = 4 * M
E = (RHO + 1) // 3


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    need(3 * E == RHO + 1, "wrong first live degree")

    # Core zero, residual degree two.
    delta0 = 2 * E - 1
    packets0 = []
    for u in range(2):
        v = 1 - u
        i_h = delta0 - u
        omission = delta0 - v
        for i0 in range(u + 1):
            i_e = i_h - i0
            if i_e <= 2 * (E - 1) and i_e > E - 1:
                packets0.append((u, v, i0, 2 * E - i_e, omission))
    need(packets0 == [(1, 0, 0, 2, delta0), (1, 0, 1, 3, delta0)],
         "wrong core-zero packets")

    # Core one, residual degree one.
    delta1 = E - 2
    packets1 = []
    for u in range(3):
        v = 2 - u
        i_h = delta1 - u
        for i0 in range(u + 1):
            deficit = E - (i_h - i0)
            packets1.append((u, v, i0, deficit))
    expected1 = [
        (0, 2, 0, 2),
        (1, 1, 0, 3), (1, 1, 1, 4),
        (2, 0, 0, 4), (2, 0, 1, 5), (2, 0, 2, 6),
    ]
    need(packets1 == expected1, "wrong core-one packets")
    need(all((delta1 - u) + (delta1 - v) == 2 * E - 6
             for u, v, _, _ in packets1), "core-one balance failed")

    print(f"CONSTANT_TRIPLE_PACKETS_PASS e={E} core0={len(packets0)} core1={len(packets1)}")


if __name__ == "__main__":
    main()
