#!/usr/bin/env python3
"""Independent representative and ordered-pair genus audit."""


IDENTITY = tuple(range(5))
INFINITY = (1, 2, 3, 4, 0)


def compose(left, right):
    return tuple(left[right[index]] for index in range(5))


def inverse(permutation):
    result = [0] * 5
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def from_cycles(*cycle_list):
    result = list(range(5))
    for cycle in cycle_list:
        zero_based = [value - 1 for value in cycle]
        for source, target in zip(zero_based, zero_based[1:] + zero_based[:1]):
            result[source] = target
    return tuple(result)


def cycle_type(permutation):
    seen = set()
    lengths = []
    for start in range(5):
        if start in seen:
            continue
        point = start
        length = 0
        while point not in seen:
            seen.add(point)
            length += 1
            point = permutation[point]
        if length > 1:
            lengths.append(length)
    return tuple(sorted(lengths, reverse=True)) or (1,)


def ordered_pair_index(permutation):
    unseen = {(i, j) for i in range(5) for j in range(5) if i != j}
    cycles = 0
    while unseen:
        point = next(iter(unseen))
        cycles += 1
        while point in unseen:
            unseen.remove(point)
            point = (permutation[point[0]], permutation[point[1]])
    return 20 - cycles


def group_order(generators):
    generators = [*generators, *(inverse(item) for item in generators)]
    group = {IDENTITY}
    frontier = [IDENTITY]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = compose(generator, current)
            if candidate not in group:
                group.add(candidate)
                frontier.append(candidate)
    return len(group)


def main() -> None:
    type_representatives = {
        (2,): from_cycles((1, 2)),
        (2, 2): from_cycles((1, 2), (3, 4)),
        (3,): from_cycles((1, 2, 3)),
        (3, 2): from_cycles((1, 2, 3), (4, 5)),
        (4,): from_cycles((1, 2, 3, 4)),
        (5,): INFINITY,
    }
    expected_indices = {
        (2,): 7,
        (2, 2): 10,
        (3,): 12,
        (3, 2): 15,
        (4,): 15,
        (5,): 16,
    }
    assert {
        kind: ordered_pair_index(permutation)
        for kind, permutation in type_representatives.items()
    } == expected_indices

    # Explicit tuples are independent witnesses for each retained row.
    rows = [
        (
            60,
            0,
            [from_cycles((2, 3), (4, 5)), from_cycles((1, 4, 2))],
        ),
        (60, 1, [from_cycles((3, 5, 4)), from_cycles((1, 3, 2))]),
        (
            120,
            0,
            [from_cycles((3, 5)), from_cycles((1, 3, 2), (4, 5))],
        ),
        (120, 0, [from_cycles((4, 5)), from_cycles((1, 4, 3, 2))]),
        (
            120,
            1,
            [
                from_cycles((4, 5)),
                from_cycles((2, 4)),
                from_cycles((1, 2), (3, 4)),
            ],
        ),
    ]
    retained_profiles = set()
    for expected_order, expected_genus, finite_tuple in rows:
        product_value = IDENTITY
        for branch_cycle in finite_tuple:
            product_value = compose(product_value, branch_cycle)
        assert product_value == inverse(INFINITY)
        assert group_order([INFINITY, *finite_tuple]) == expected_order
        genus = 1 - 20 + sum(
            ordered_pair_index(item) for item in [INFINITY, *finite_tuple]
        ) // 2
        assert genus == expected_genus
        retained_profiles.add(tuple(sorted(cycle_type(item) for item in finite_tuple)))

    assert retained_profiles == {
        ((2, 2), (3,)),
        ((3,), (3,)),
        ((2,), (3, 2)),
        ((2,), (4,)),
        ((2,), (2,), (2, 2)),
    }
    print("RATE_HALF_KB_M12_R4_LOW_GENUS_BRANCH_PROFILE_REDUCTION_AUDIT_PASS")


if __name__ == "__main__":
    main()
