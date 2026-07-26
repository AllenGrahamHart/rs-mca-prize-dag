#!/usr/bin/env python3
"""Mutation audit for the endpoint and rank-two capacity argument."""


def main() -> None:
    checks = 0
    for d in range(3, 1000):
        z = 2 * d - 2
        endpoint_lower = 4 * (3 * d - 1)
        capacity = 4 * z + 2 * (4 * d - z)
        assert endpoint_lower == capacity

        mutated_lower = 4 * (3 * d - 2)
        assert mutated_lower < capacity
        assert 2 * d + 2 > 6
        checks += 3
    print(f"AUDIT_RATE_HALF_LIST_BUDGET_THREE_AFFINE_RANK_RIGIDITY_PASS checks={checks}")


if __name__ == "__main__":
    main()
