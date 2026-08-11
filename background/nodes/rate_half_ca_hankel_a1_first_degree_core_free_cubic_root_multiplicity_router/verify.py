#!/usr/bin/env python3
"""Exact arithmetic replay for the core-free cubic root router."""

M = 1 << 37
RHO = 4 * M
E = (RHO + 1) // 3
DELTA = 2 * E - 1


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    need(3 * E == RHO + 1, "first-degree identity failed")

    u_low = (E - 1) // 5
    need(5 * u_low < E, "low-gap endpoint failed")
    for i0 in (0, u_low):
        need(i0 <= u_low, "ordinary-incidence range failed")
        for r in (1, 2):
            need((3 - r) * E > 3 * u_low + 2 * i0,
                 "simple low-gap branch survived")

    u_first = (E + 4) // 5
    need(5 * u_first >= E, "first possible two-root boundary failed")
    need(E <= 5 * u_first, "simple-root capacity boundary failed")

    u_triple = (E + 1) // 2
    need(2 * (u_triple - 1) < E <= 2 * u_triple,
         "triple-root threshold failed")

    for u in (0, 1, u_low, u_first, u_triple):
        v = E + 1 - u
        i_h = DELTA - u
        omission = DELTA - v
        need(i_h + omission == 3 * E - 3,
             "cubic incidence identity failed")

    print(
        "CORE_FREE_CUBIC_ROOT_ROUTER_PASS "
        f"e={E} low_u_max={u_low} first_two_root_u={u_first}"
    )


if __name__ == "__main__":
    main()
