#!/usr/bin/env python3
"""Independent direct scan and mutation for the rank-flat fence."""


def cap(d: int, d1: int, d2: int, d3: int) -> int:
    t = d + 1
    return d3 * (d3 - 1) * (d3 - 2) // (
        (d1 - t) * (d2 - t) * (d3 - t)
    )


def main() -> None:
    checked = 0
    for d in range(3, 129):
        for d3 in range(2 * d + 3, 4 * d + 1):
            for d2 in range(2 * d + 2, min(3 * d + 1, d3 - 1) + 1):
                assert cap(d, 2 * d + 1, d2, d3) >= 4
                checked += 1

    # Losing the exact d1 pin admits a synthetic cap-three tuple.
    assert cap(10, 30, 31, 32) == 3

    print(
        "RATE_HALF_LIST_CHAMBER_RANK_FLAT_FENCE_AUDIT_PASS "
        f"tuples={checked} mutation=lost_d1_pin"
    )


if __name__ == "__main__":
    main()
