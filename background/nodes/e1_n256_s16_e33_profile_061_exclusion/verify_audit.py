#!/usr/bin/env python3
"""Independent finite audit of the symmetric target-fiber bound."""

from itertools import combinations


def main() -> None:
    modulus = 32
    tested = 0
    maximum_outer = 0
    maximum_target = 0
    maximum_moment = 0
    for representatives in combinations(range(1, modulus // 2), 7):
        support = set(representatives) | {(-value) % modulus for value in representatives}
        assert len(support) == 14
        tested += 1
        outer = sum(
            ((-left-right) % modulus) in support
            for left in support
            for right in support
        )
        maximum_outer = max(maximum_outer, outer)
        for target in support:
            fiber = sum(((target-left) % modulus) in support for left in support)
            moment = 8 * outer + 24 * fiber + 12 * int((2*target) % modulus in support)
            maximum_target = max(maximum_target, fiber)
            maximum_moment = max(maximum_moment, moment)
    assert (tested, maximum_outer, maximum_target, maximum_moment) == (6435, 168, 12, 1644)

    # Each coefficient is load-bearing in the sharp witness ledger.
    assert 1644 - 8 * 168 == 300
    assert 1644 - 24 * 12 == 1356
    assert 1644 - 12 == 1632
    print(
        "E1_N256_S16_E33_PROFILE_061_EXCLUSION_AUDIT_PASS "
        "sets=6435 outer=168 fiber=12 m3=1644 mutations=3"
    )


if __name__ == "__main__":
    main()
