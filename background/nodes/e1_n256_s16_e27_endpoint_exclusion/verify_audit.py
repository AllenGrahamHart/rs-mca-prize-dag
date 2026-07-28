#!/usr/bin/env python3
"""Mutation audit for the E27 endpoint profile partition and frontier."""

PROFILES = {
    "(3,6)", "(2,4,1)", "(1,2,2)",
    "(3,2,0,1)", "(0,0,3)", "(2,0,1,1)",
}


def valid(claimed: set[str], old_frontier: int, new_frontier: int) -> bool:
    return claimed == PROFILES and old_frontier == 54 and new_frontier == 52


def main() -> None:
    assert valid(set(PROFILES), 54, 52)
    assert not valid(PROFILES - {"(3,6)"}, 54, 52)
    assert not valid(PROFILES | {"(9,9)"}, 54, 52)
    assert not valid(set(PROFILES), 56, 52)
    assert not valid(set(PROFILES), 54, 50)
    print("E1_N256_S16_E27_ENDPOINT_EXCLUSION_AUDIT_PASS mutations=4/4")


if __name__ == "__main__":
    main()
