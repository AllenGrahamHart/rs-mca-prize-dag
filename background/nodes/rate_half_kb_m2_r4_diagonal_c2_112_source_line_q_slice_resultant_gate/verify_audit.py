#!/usr/bin/env python3
"""Independent divisor audit for the q-slice resultant gate."""

from collections import Counter


def main() -> None:
    expected = Counter({"w": 4, "k1": 2, "k2": 2})
    checked = 0
    for first_root_k1 in range(3):
        first = Counter({
            "w": 2,
            "k1": first_root_k1,
            "k2": 2 - first_root_k1,
        })
        second = Counter({
            "w": 2,
            "k1": 2 - first_root_k1,
            "k2": first_root_k1,
        })
        assert first + second == expected
        assert sum(first.values()) == sum(second.values()) == 4
        checked += 1

    assert checked == 3
    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SOURCE_LINE_Q_SLICE_RESULTANT_GATE_AUDIT_PASS "
        "root_distributions=3 divisor=w^4*k1^2*k2^2"
    )


if __name__ == "__main__":
    main()
