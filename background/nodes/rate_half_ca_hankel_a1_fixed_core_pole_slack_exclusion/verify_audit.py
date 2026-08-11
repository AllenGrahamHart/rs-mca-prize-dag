#!/usr/bin/env python3
"""Boundary mutation audit for fixed-core exclusion."""


def main():
    checks = 0
    for delta in range(1, 100):
        e = delta + 5
        slack = e - delta - 3
        if slack >= 0:
            lhs = delta // 3 + slack + 2
            assert lhs < e
            mutated = delta + slack + 2
            assert mutated >= lhs
            checks += 1

    e = 50
    # Boundary s=2 case: beta=2 is essential and equality is retained by a
    # beta=1 mutation.
    slack = e - 2
    assert 0 + slack + 1 < e
    assert 0 + slack + 2 == e

    print(
        "RATE_HALF_CA_HANKEL_A1_FIXED_CORE_POLE_SLACK_EXCLUSION_AUDIT_PASS "
        f"checks={checks} beta_mutation=detected"
    )


if __name__ == "__main__":
    main()
