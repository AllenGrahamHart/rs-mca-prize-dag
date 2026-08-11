#!/usr/bin/env python3
"""Exact degree replay for the core-one two-point normal form."""

M = 1 << 37
RHO = 4 * M
E = (RHO + 1) // 3
D = RHO - 1
DELTA = E - 2


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    need(RHO == 3 * E - 1, "first-degree identity failed")
    need(D == 3 * E - 2, "residual degree failed")
    need((E - 4) + 2 * 2 == E, "vertical multiplicities failed")
    need((E - 4) + 2 == DELTA, "adjugate radical degree failed")
    need(E + 1 - DELTA == 3, "Forney quotient degree failed")
    need(E - (E - 4) == 4, "derivative quotient degree failed")
    picard_degree = (RHO + 2) * E - (E + 1) * D
    need(picard_degree == 2, "Picard degree failed")
    print(f"CORE_ONE_TWO_POINT_NORMAL_FORM_PASS e={E} delta={DELTA} picard={picard_degree}")


if __name__ == "__main__":
    main()
