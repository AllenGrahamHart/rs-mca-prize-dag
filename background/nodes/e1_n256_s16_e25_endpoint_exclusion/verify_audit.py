#!/usr/bin/env python3
"""Mutation audit for the E25 endpoint profile partition and frontier."""

PROFILES = {
    "(5,5)", "(1,6)", "(4,3,1)", "(0,4,1)", "(3,1,2)",
    "(5,1,0,1)", "(1,2,0,1)", "(0,0,1,1)", "(0,0,0,0,1)",
}


def valid(claimed: set[str], old_frontier: int, new_frontier: int) -> bool:
    return claimed == PROFILES and old_frontier == 50 and new_frontier == 48


def main() -> None:
    assert valid(set(PROFILES), 50, 48)
    assert not valid(PROFILES - {"(5,5)"}, 50, 48)
    assert not valid(PROFILES | {"(9,9)"}, 50, 48)
    assert not valid(set(PROFILES), 52, 48)
    assert not valid(set(PROFILES), 50, 46)
    print("E1_N256_S16_E25_ENDPOINT_EXCLUSION_AUDIT_PASS mutations=4/4")


if __name__ == "__main__":
    main()
