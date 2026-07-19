#!/usr/bin/env python3
"""Independent finite-field audit of the bi-Mobius graph identity."""

from __future__ import annotations


P = 101


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % P
    return tuple(answer)


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return tuple(
        ((left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)) % P
        for i in range(size)
    )


def evaluate(poly: tuple[int, ...], x: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % P
    return value


def main() -> None:
    b02 = (P - 2, 1)
    b03 = (P - 3, 1)
    b12 = (P - 5, 1)
    b13 = (P - 7, 1)
    b01 = (1,)
    b23 = add(multiply(b02, b13), tuple(-value % P for value in multiply(b03, b12)))
    assert b23[:2] == (P - 1, P - 1) and all(value == 0 for value in b23[2:])

    checked = 0
    m2_values = []
    m3_values = []
    for x in range(P):
        if x not in (2, 3):
            m2 = evaluate(b12, x) * pow(evaluate(b02, x), -1, P) % P
            m3 = evaluate(b13, x) * pow(evaluate(b03, x), -1, P) % P
            left = (m3 - m2) % P
            right = evaluate(b01, x) * evaluate(b23, x) * pow(
                evaluate(b02, x) * evaluate(b03, x), -1, P
            ) % P
            assert left == right
            checked += 1
        if x != 2:
            m2_values.append(evaluate(b12, x) * pow(evaluate(b02, x), -1, P) % P)
        if x != 3:
            m3_values.append(evaluate(b13, x) * pow(evaluate(b03, x), -1, P) % P)
    assert len(m2_values) == len(set(m2_values)) == P - 1
    assert len(m3_values) == len(set(m3_values)) == P - 1

    constant_mutation = tuple(range(3, 11))
    mutated_values = [(x - 2) * pow(x - 2, -1, P) % P for x in constant_mutation]
    assert len(set(mutated_values)) == 1
    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_CYCLE_BIMOBIUS_TRANSVERSAL_PASS "
        f"graph_identity_points={checked} injections=2 mutation_constant=1"
    )


if __name__ == "__main__":
    main()
