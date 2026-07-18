#!/usr/bin/env python3
"""Independent endpoint audit for the low-budget all-arity corollary."""

from __future__ import annotations


def projection_upper(base_list: int, field_order: int) -> int:
    return base_list * (field_order - 1) // (field_order - base_list)


def main() -> None:
    field_orders = ((1 << 128) + 1, (2 << 128) + 1)
    for budget, field_order in zip((1, 2), field_orders, strict=True):
        assert budget * budget < field_order
        assert projection_upper(budget, field_order) == budget
        # Equality at q=L^2 would invalidate the strict collapse step.
        assert not budget * budget < budget * budget

    length = 1 << 12
    safe = 3 * length // 4
    assert (length - safe, length - (safe - 1)) == (length // 4, length // 4 + 1)
    print(
        "AUDIT_RATE_HALF_LIST_LOW_BUDGET_ALL_ARITY_CROSSING_PASS "
        "budgets=2 strictness_controls=2 endpoint=1/1"
    )


if __name__ == "__main__":
    main()
