#!/usr/bin/env python3
"""Audit the antipodal distance-six router on an exact small row."""

from __future__ import annotations

from itertools import combinations, combinations_with_replacement


PRIME = 1_153
ORDER = 32
HALF = ORDER // 2


def coefficient_vector(left: int, right: int) -> tuple[int, ...]:
    answer = [0] * HALF
    for exponent, coefficient in ((left + right, 1), (left, -1), (right, -1)):
        exponent %= ORDER
        answer[exponent % HALF] += coefficient * (1 if exponent < HALF else -1)
    return tuple(answer)


def norm(vector: tuple[int, ...]) -> int:
    return sum(value * value for value in vector)


def distance(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum((a - b) ** 2 for a, b in zip(left, right, strict=True))


def main() -> None:
    generator = next(
        value
        for value in range(2, PRIME)
        if pow(value, ORDER, PRIME) == 1
        and pow(value, HALF, PRIME) != 1
    )
    subgroup = tuple(pow(generator, exponent, PRIME) for exponent in range(ORDER))
    exponent_of = {value: exponent for exponent, value in enumerate(subgroup)}

    by_target: dict[int, list[tuple[int, int, tuple[int, ...], bool]]] = {}
    selected_pairs = set()
    for left, right in combinations_with_replacement(range(1, ORDER), 2):
        vector = coefficient_vector(left, right)
        if norm(vector) > 3:
            continue
        target = (1 - subgroup[left]) * (1 - subgroup[right]) % PRIME
        record = (left, right, vector, (right - left) % ORDER == HALF)
        by_target.setdefault(target, []).append(record)
        selected_pairs.add((left, right))

    direct = 0
    antipodal_targets = {}
    for target, records in by_target.items():
        antipodal = [record for record in records if record[3]]
        if not antipodal:
            continue
        assert len(antipodal) == 1
        edge_count = sum(
            distance(left[2], right[2]) == 6
            for left, right in combinations(records, 2)
        )
        quotient_count = sum(
            (1 - subgroup[w]) % PRIME == target * (1 - subgroup[z]) % PRIME
            for z in range(1, ORDER)
            for w in range(1, ORDER)
        )
        direct += edge_count * quotient_count
        antipodal_targets[target] = antipodal[0][0]

    routed = 0
    for target, x_exponent in antipodal_targets.items():
        square = subgroup[x_exponent] ** 2 % PRIME
        assert target == (1 - square) % PRIME
        for u_exponent in range(1, ORDER):
            denominator = (1 - subgroup[u_exponent]) % PRIME
            v_value = (square - subgroup[u_exponent]) * pow(
                denominator, -1, PRIME
            ) % PRIME
            v_exponent = exponent_of.get(v_value, 0)
            first_pair = tuple(sorted((u_exponent, v_exponent)))
            if not v_exponent or first_pair not in selected_pairs or u_exponent != first_pair[0]:
                continue
            for a_exponent in range(1, ORDER):
                denominator = (1 - subgroup[a_exponent]) % PRIME
                b_value = (square - subgroup[a_exponent]) * pow(
                    denominator, -1, PRIME
                ) % PRIME
                b_exponent = exponent_of.get(b_value, 0)
                second_pair = tuple(sorted((a_exponent, b_exponent)))
                if (
                    not b_exponent
                    or second_pair not in selected_pairs
                    or a_exponent != second_pair[0]
                    or first_pair >= second_pair
                ):
                    continue
                if distance(
                    coefficient_vector(*first_pair),
                    coefficient_vector(*second_pair),
                ) != 6:
                    continue
                for z_exponent in range(1, ORDER):
                    w_value = (
                        square + (1 - square) * subgroup[z_exponent]
                    ) % PRIME
                    if exponent_of.get(w_value, 0):
                        routed += 1

    assert direct == routed == 6
    print(
        "AUDIT_F3_H3_ANTIPODAL_TAIL_DISTANCE_SIX_SPLIT_PASS "
        "order=32 prime=1153 direct=6 routed=6 high_tail_filter=omitted"
    )


if __name__ == "__main__":
    main()
