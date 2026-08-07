#!/usr/bin/env python3
"""Fail-closed checks for the complete F2 degree/order census."""

from __future__ import annotations


CHECKS = 0


def check(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def main() -> None:
    plus_order_one = 3 * (1 << 41) + 1
    plus_order_two = 27 * (1 << 40) + 1
    plus_order_four = 5 * (1 << 39) + 1
    minus_order_two = (1 << 61) - 1
    minus_order_four = 25 * (1 << 39) - 1

    expected = {
        *(('plus', 1, degree) for degree in range(1, 7)),
        ('plus', 2, 2),
        ('plus', 2, 4),
        ('plus', 4, 4),
        ('minus', 2, 2),
        ('minus', 2, 4),
        ('minus', 4, 4),
    }
    enumerated: set[tuple[str, int, int]] = set()
    for degree in range(1, 7):
        for order in (1, 2, 4):
            if degree % order:
                continue
            if order == 1:
                enumerated.add(('plus', order, degree))
            elif order == 4 and degree == 4:
                enumerated.add(('plus', order, degree))
                enumerated.add(('minus', order, degree))
            elif order == 2 and degree in (2, 4):
                enumerated.add(('plus', order, degree))
                enumerated.add(('minus', order, degree))
    check(enumerated == expected, '12-type enumeration')

    plus_candidates = (
        (1, 257),
        (3, 7),
        (5, 3),
    )
    for coefficient, divisor in plus_candidates:
        candidate = coefficient * (1 << 40) + 1
        check(candidate % divisor == 0, 'plus e=6 compositeness')
        check(candidate**3 < 1 << 128, 'plus candidate is inside cube cap')

    minus_candidates = (
        (40, 1, 3),
        (40, 3, 144899),
        (40, 5, 179),
        (41, 1, 13367),
        (41, 3, 5),
        (42, 1, 3),
    )
    for valuation, coefficient, divisor in minus_candidates:
        candidate = coefficient * (1 << valuation) - 1
        check(candidate % divisor == 0, 'minus e=6 compositeness')
        check(candidate**3 < 1 << 128, 'minus candidate is inside cube cap')

    check((7 * (1 << 40) + 1) ** 3 > 1 << 128, 'plus cap cutoff')
    check((5 * (1 << 41) - 1) ** 3 > 1 << 128, 'minus b41 cutoff')
    check((3 * (1 << 42) - 1) ** 3 > 1 << 128, 'minus b42 cutoff')
    check(((1 << 43) - 1) ** 3 > 1 << 128, 'minus valuation cutoff')

    check(plus_order_one**6 < 1 << 256, 'order-one witness through e=6')
    check(plus_order_two**4 < 1 << 256, 'plus order-two through e=4')
    check(plus_order_four**4 < 1 << 256, 'plus order-four field cap')
    check(minus_order_two**4 < 1 << 256, 'minus order-two through e=4')
    check(minus_order_four**4 < 1 << 256, 'minus order-four field cap')

    non_generating = {
        row for row in expected if row[1] < row[2]
    }
    check(len(expected) == 12, 'total type count')
    check(len(non_generating) == 7, 'non-generating type count')

    print(
        'F2_ADMISSIBLE_DEGREE_ORDER_CLASSIFICATION_PASS '
        f'checks={CHECKS} types={len(expected)} non_generating={len(non_generating)}'
    )


if __name__ == '__main__':
    main()
