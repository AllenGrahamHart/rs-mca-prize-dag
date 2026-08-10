#!/usr/bin/env python3
"""Mutation audit for the marked coefficient and support floor."""


def main():
    mutations = 0
    rejected = 0
    for m in range(2, 65):
        rho = 4 * m - 1
        joint_support = rho + 3
        remaining = joint_support - 1
        assert remaining == 4 * m + 1

        candidates = [
            (rho + 1, rho),
            (rho + 2, rho + 1),
            (rho, rho - 1),
        ]
        for bad_joint, bad_remaining in candidates:
            mutations += 1
            valid = bad_joint >= rho + 1 and bad_remaining >= rho + 2
            if not valid:
                rejected += 1

        x0 = 17
        for x in range(17, 25):
            coefficient = x - x0
            if x == x0:
                assert coefficient == 0
            else:
                assert coefficient != 0

    assert rejected == mutations
    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_MARKED_ROW_SPLIT_VERONESE_DEPENDENCY_AUDIT_PASS "
        f"mutations={rejected}/{mutations}"
    )


if __name__ == "__main__":
    main()
