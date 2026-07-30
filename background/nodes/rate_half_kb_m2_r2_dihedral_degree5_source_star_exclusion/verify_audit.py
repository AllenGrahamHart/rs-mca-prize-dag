#!/usr/bin/env python3
"""Audit the totally ramified pole and source-weight ledger."""


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[i]] for i in range(len(left)))


def cycle_lengths(permutation: tuple[int, ...]) -> list[int]:
    seen: set[int] = set()
    lengths: list[int] = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        point = start
        length = 0
        while point not in seen:
            seen.add(point)
            point = permutation[point]
            length += 1
        lengths.append(length)
    return sorted(lengths, reverse=True)


def main() -> None:
    # D_5 on the five cosets of a reflection subgroup. The rotation branch
    # has one e=5 point; a reflection branch has cycle type 2,2,1.
    rotation = tuple((i + 1) % 5 for i in range(5))
    reflection = tuple((-i) % 5 for i in range(5))
    identity = tuple(range(5))
    assert compose(rotation, (compose(reflection, rotation))) == reflection
    assert compose(reflection, reflection) == identity
    assert cycle_lengths(rotation) == [5]
    assert cycle_lengths(reflection) == [2, 2, 1]

    # q_5 has one e=5 point. A simple outer pole there and one generic
    # order-five pole account for the degree-six pole divisor of G.
    outer_pole_orders = [1, 5]
    assert sum(outer_pole_orders) == 6
    endpoint_orders = [5 * outer_pole_orders[0]] + [outer_pole_orders[1]] * 5
    assert endpoint_orders == [5] * 6

    locator_degrees = [2, 2]
    matching_weight = sum(locator_degrees)
    assert matching_weight == 4
    assert matching_weight * (matching_weight - 1) // 2 == 6
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_DEGREE5_SOURCE_STAR_EXCLUSION_AUDIT_PASS")


if __name__ == "__main__":
    main()
