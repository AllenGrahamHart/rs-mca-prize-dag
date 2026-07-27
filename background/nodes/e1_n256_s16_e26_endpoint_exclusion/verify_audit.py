#!/usr/bin/env python3
"""Mutation audit for the E26 endpoint profile partition and frontier."""

TWO_ODD = {
    "(2,6)", "(1,4,1)", "(0,2,2)",
    "(2,2,0,1)", "(1,0,1,1)", "(1,0,0,0,1)",
}
SIX_ODD = {"(6,5)", "(5,3,1)", "(4,1,2)", "(6,1,0,1)"}
PROFILES = TWO_ODD | SIX_ODD


def valid(two_odd: set[str], six_odd: set[str], old_frontier: int, new_frontier: int) -> bool:
    return (
        two_odd == TWO_ODD
        and six_odd == SIX_ODD
        and two_odd.isdisjoint(six_odd)
        and two_odd | six_odd == PROFILES
        and old_frontier == 52
        and new_frontier == 50
    )


def main() -> None:
    assert valid(set(TWO_ODD), set(SIX_ODD), 52, 50)
    assert not valid(TWO_ODD - {"(2,6)"}, set(SIX_ODD), 52, 50)
    assert not valid(set(TWO_ODD), SIX_ODD | {"(9,9)"}, 52, 50)
    assert not valid(set(TWO_ODD), SIX_ODD | {"(2,6)"}, 52, 50)
    assert not valid(set(TWO_ODD), set(SIX_ODD), 54, 50)
    assert not valid(set(TWO_ODD), set(SIX_ODD), 52, 48)
    assert not valid(set(TWO_ODD), set(SIX_ODD), 50, 50)
    print("E1_N256_S16_E26_ENDPOINT_EXCLUSION_AUDIT_PASS mutations=6/6")


if __name__ == "__main__":
    main()
