#!/usr/bin/env python3
"""Mutation audit for the E30 endpoint profile partition."""

PROFILES = {
    "(6,6)", "(2,7)", "(5,4,1)", "(1,5,1)",
    "(4,2,2)", "(0,3,2)", "(6,2,0,1)", "(3,0,3)",
}
GROUPS = [
    {"(0,3,2)", "(6,2,0,1)", "(3,0,3)"},
    {"(2,7)", "(1,5,1)"},
    {"(4,2,2)"},
    {"(5,4,1)"},
    {"(6,6)"},
]


def valid(groups: list[set[str]]) -> bool:
    flat = [profile for group in groups for profile in group]
    return set(flat) == PROFILES and len(flat) == len(PROFILES)


def main() -> None:
    assert valid(GROUPS)
    dropped = [set(group) for group in GROUPS]
    dropped[-1].clear()
    duplicated = [set(group) for group in GROUPS]
    duplicated[-1].add("(5,4,1)")
    invented = [set(group) for group in GROUPS]
    invented[-1].add("(9,9)")
    assert not valid(dropped)
    assert not valid(duplicated)
    assert not valid(invented)
    print("E1_N256_S16_E30_ENDPOINT_EXCLUSION_AUDIT_PASS mutations=3/3")


if __name__ == "__main__":
    main()
