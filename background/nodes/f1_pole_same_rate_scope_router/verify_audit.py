#!/usr/bin/env python3
"""Mutation audit for the F1 same-rate scope router."""

from verify import same_rate


def main() -> None:
    assert same_rate(64, 16, 64, 16)
    caught = 0
    for args in ((64, 16, 64, 17), (64, 16, 63, 16), (64, 32, 64, 31)):
        if not same_rate(*args):
            caught += 1
    assert caught == 3
    print("F1_POLE_SAME_RATE_SCOPE_ROUTER_AUDIT_PASS mutations=3/3")


if __name__ == "__main__":
    main()
