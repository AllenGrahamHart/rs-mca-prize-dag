#!/usr/bin/env python3
"""Exact arithmetic replay for the three signed tangent packets."""

M = 1 << 37
RHO = 4 * M
E = (RHO + 1) // 3
DELTA = E - 2


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    need(E % 3 == 0, "official e must be divisible by three")

    packets = (
        # u, v, i0, c, new roots, spare rank, deg A, deg B
        (1, 1, 1, 4, 1, 0, 1, 1),
        (2, 0, 1, 5, 0, 1, 1, 1),
        (2, 0, 2, 6, 0, 0, 0, 2),
    )
    for u, v, i0, c, new_roots, spare, deg_a, deg_b in packets:
        d_star = E - c
        omission = DELTA - v
        baseline_rank = d_star + 2 * i0
        need(DELTA - baseline_rank == spare, "wrong spare rank degree")
        need(DELTA - omission == new_roots, "wrong new-root count")
        need(c == 2 + u + i0, "wrong row deficit")

        if (u, i0) == (1, 1):
            vertical_base = d_star + deg_a
            residual_contact = deg_b
            signed_degree = deg_a + 2 * deg_b - i0
        elif (u, i0) == (2, 1):
            vertical_base = d_star + 2 * deg_a
            residual_contact = deg_a + deg_b
            signed_degree = deg_a + 2 * deg_b - i0
        else:
            vertical_base = d_star
            residual_contact = deg_b
            signed_degree = 2 * deg_b - i0

        need(vertical_base + 3 * deg_b == E, "vertical degree failed")
        need(residual_contact == u, "contact residual failed")
        need(signed_degree == 2, "signed Picard degree failed")

    print(f"SIGNED_PACKET_LOCAL_NORMAL_FORMS_PASS e={E} packets={len(packets)}")


if __name__ == "__main__":
    main()
