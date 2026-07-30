#!/usr/bin/env python3
"""Verify the m12 r4 low-genus branch-profile reduction."""

from collections import defaultdict
from itertools import permutations, product
from pathlib import Path


NODE = Path(__file__).resolve().parent
IDENTITY = tuple(range(5))
S5 = list(permutations(range(5)))
INFINITY = (1, 2, 3, 4, 0)


def compose(left, right):
    """Return left after right."""

    return tuple(left[right[index]] for index in range(5))


def inverse(permutation):
    result = [0] * 5
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def cycles(permutation):
    seen = set()
    result = []
    for start in range(5):
        if start in seen:
            continue
        cycle = []
        point = start
        while point not in seen:
            seen.add(point)
            cycle.append(point)
            point = permutation[point]
        result.append(tuple(cycle))
    return result


def index(permutation):
    return 5 - len(cycles(permutation))


def cycle_type(permutation):
    nontrivial = sorted(
        (len(cycle) for cycle in cycles(permutation) if len(cycle) > 1),
        reverse=True,
    )
    return tuple(nontrivial) if nontrivial else (1,)


def generated_group(generators):
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
    return group


def point_stabilizer_subdegrees(group):
    stabilizer = [item for item in group if item[0] == 0]
    unseen = set(range(5))
    subdegrees = []
    while unseen:
        seed = min(unseen)
        orbit = {item[seed] for item in stabilizer}
        subdegrees.append(len(orbit))
        unseen -= orbit
    return tuple(sorted(subdegrees))


def ordered_pair_index(permutation):
    unseen = {
        (left, right)
        for left in range(5)
        for right in range(5)
        if left != right
    }
    cycle_count = 0
    while unseen:
        current = next(iter(unseen))
        cycle_count += 1
        while current in unseen:
            unseen.remove(current)
            current = (permutation[current[0]], permutation[current[1]])
    return 20 - cycle_count


def compositions(total, prefix=()):
    if total == 0:
        yield prefix
        return
    if len(prefix) == 4:
        return
    for part in range(1, total + 1):
        yield from compositions(total - part, prefix + (part,))


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "genus(C)<=1" in statement
    assert "`AGL(1,5)` does not occur" in contract
    assert "No profile is yet deleted" in (NODE / "result.md").read_text()

    # The bidegree-(2,4) actual model has arithmetic genus three. If the
    # degree-12 target had genus at least two, RH would force 2g-2 >= 24.
    assert (2 - 1) * (4 - 1) == 3
    assert 2 * 3 - 2 < 12 * (2 * 2 - 2)

    by_index = {
        value: [item for item in S5 if index(item) == value]
        for value in range(1, 5)
    }
    target = inverse(INFINITY)
    summary = defaultdict(int)

    for index_composition in compositions(4):
        pools = [by_index[value] for value in index_composition]
        for finite_tuple in product(*pools):
            finite_product = IDENTITY
            for branch_cycle in finite_tuple:
                finite_product = compose(finite_product, branch_cycle)
            if finite_product != target:
                continue

            group = generated_group([INFINITY, *finite_tuple])
            if point_stabilizer_subdegrees(group) != (1, 4):
                continue

            induced_index_sum = sum(
                ordered_pair_index(item) for item in (INFINITY, *finite_tuple)
            )
            assert induced_index_sum % 2 == 0
            genus = 1 - 20 + induced_index_sum // 2
            profile = tuple(sorted(cycle_type(item) for item in finite_tuple))
            summary[(len(group), profile, genus)] += 1

    expected = {
        (60, ((2, 2), (3,)), 0): 10,
        (60, ((3,), (3,)), 1): 5,
        (120, ((2,), (3, 2)), 0): 10,
        (120, ((2,), (4,)), 0): 10,
        (120, ((2,), (2,), (2, 2)), 1): 75,
        (120, ((2,), (2,), (3,)), 2): 75,
        (120, ((2,), (2,), (2,), (2,)), 3): 125,
    }
    assert dict(summary) == expected
    assert sum(summary.values()) == 310
    assert all(group_order != 20 for group_order, _, _ in summary)

    low_genus = {
        key: count for key, count in summary.items() if key[2] <= 1
    }
    assert len(low_genus) == 5
    assert sum(low_genus.values()) == 110
    print("RATE_HALF_KB_M12_R4_LOW_GENUS_BRANCH_PROFILE_REDUCTION_PASS")


if __name__ == "__main__":
    main()
