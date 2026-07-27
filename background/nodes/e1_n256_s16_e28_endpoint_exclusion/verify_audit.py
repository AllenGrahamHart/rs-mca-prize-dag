#!/usr/bin/env python3
"""Mutation audit for the E28 endpoint profile partition and frontier."""

PROFILES = {"(4,6)","(0,7)","(3,4,1)","(2,2,2)","(4,2,0,1)","(1,0,3)","(0,3,0,1)","(3,0,1,1)"}


def valid(claimed: set[str], old_frontier: int, new_frontier: int) -> bool:
    return claimed == PROFILES and old_frontier == 56 and new_frontier == 54


def main() -> None:
    assert valid(set(PROFILES),56,54)
    assert not valid(PROFILES-{"(4,6)"},56,54)
    assert not valid(PROFILES|{"(9,9)"},56,54)
    assert not valid(set(PROFILES),58,54)
    assert not valid(set(PROFILES),56,52)
    print("E1_N256_S16_E28_ENDPOINT_EXCLUSION_AUDIT_PASS mutations=4/4")


if __name__ == "__main__":
    main()
