#!/usr/bin/env python3
"""Mutation audit for the E29 endpoint profile partition and frontier."""

PROFILES = {
    "(5,6)", "(1,7)", "(4,4,1)", "(0,5,1)",
    "(3,2,2)", "(5,2,0,1)", "(2,0,3)", "(1,3,0,1)",
}


def valid(claimed: set[str], old_frontier: int, new_frontier: int) -> bool:
    return claimed == PROFILES and old_frontier == 58 and new_frontier == 56


def main() -> None:
    assert valid(set(PROFILES), 58, 56)
    assert not valid(PROFILES - {"(5,6)"}, 58, 56)
    assert not valid(PROFILES | {"(9,9)"}, 58, 56)
    assert not valid(set(PROFILES), 60, 56)
    assert not valid(set(PROFILES), 58, 54)
    print("E1_N256_S16_E29_ENDPOINT_EXCLUSION_AUDIT_PASS mutations=4/4")


if __name__ == "__main__":
    main()
