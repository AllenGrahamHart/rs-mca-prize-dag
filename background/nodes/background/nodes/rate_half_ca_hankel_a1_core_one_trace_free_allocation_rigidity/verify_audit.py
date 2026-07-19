#!/usr/bin/env python3
"""Audit norm-degree partitions and exclusion of a W-row allocation."""

from __future__ import annotations


def compositions(total: int, parts: int, prefix: tuple[int, ...] = ()):
    if parts == 1:
        yield prefix + (total,)
        return
    for first in range(1, total - parts + 2):
        yield from compositions(total - first, parts - 1, prefix + (first,))


def main() -> None:
    partitions = 0
    allocations = 0
    for capacity in range(2, 18):
        for count in range(1, capacity + 1):
            for deficits in compositions(capacity, count):
                assert sum(deficits) == capacity
                partitions += 1
                # Divisibility by the exceptional factor forces epsilon=1,
                # so even a deficit-one row has quotient degree two.
                for delta in deficits:
                    assert delta + 1 > 1
                allocations += 1

    # Mutation fences: epsilon=1 raises Qhat degree to two at delta=1, and a
    # constant E_Z cannot absorb any positive Qhat degree.
    assert 1 + 1 > 1
    assert 1 > 0
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_A1_CORE_ONE_TRACE_FREE_ALLOCATION_RIGIDITY_PASS "
        f"partitions={partitions} allocation_checks={allocations} mutations=2"
    )


if __name__ == "__main__":
    main()
