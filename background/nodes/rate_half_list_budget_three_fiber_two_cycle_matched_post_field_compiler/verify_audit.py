#!/usr/bin/env python3
"""Independent quartic-class audit for the corrected final gate."""

from __future__ import annotations


P = 17
N = 8


def is_square(value: int) -> bool:
    value %= P
    return value == 0 or pow(value, (P - 1) // 2, P) == 1


def is_fourth(value: int) -> bool:
    value %= P
    return any(pow(root, 4, P) == value for root in range(P))


def order(value: int) -> int:
    current = 1
    for exponent in range(1, P):
        current = current * value % P
        if current == 1:
            return exponent
    raise AssertionError("nonzero field element has no order")


def main() -> None:
    assert P % (4 * N) == 1 + 2 * N
    ratios = [q for q in range(1, P) if pow(q, N, P) == 1 and q not in (1, P - 1)]
    assert ratios
    assert all(is_square(q) for q in ratios)

    checked = 0
    reciprocal_checks = 0
    old_gate_false_rejections = 0
    for q in ratios:
        inverse = pow(q, -1, P)
        for z in range(1, P):
            t = q * z * z % P
            direct = is_square(z)
            corrected = is_fourth(t * inverse % P)
            reciprocal = is_fourth(t * q % P)
            assert corrected == direct
            assert reciprocal == corrected
            checked += 1
            reciprocal_checks += 1
            if order(q) == N and direct and not is_fourth(t):
                old_gate_false_rejections += 1

    assert old_gate_false_rejections > 0
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_MATCHED_POST_FIELD_COMPILER_AUDIT_PASS "
        f"p={P} N={N} scalar_cases={checked} reciprocal={reciprocal_checks} "
        f"old_gate_false_rejections={old_gate_false_rejections}"
    )


if __name__ == "__main__":
    main()
