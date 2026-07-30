#!/usr/bin/env python3
"""Independent direct enumeration of the m4 A6/S6 passport frontier."""

from __future__ import annotations

import itertools
from collections import Counter, defaultdict, deque


IDENTITY = tuple(range(6))


def product(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(6))


def reciprocal(permutation: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * 6
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def signature(permutation: tuple[int, ...]) -> tuple[int, ...]:
    unused = set(range(6))
    answer = []
    while unused:
        start = min(unused)
        point = start
        orbit = []
        while point not in orbit:
            orbit.append(point)
            unused.remove(point)
            point = permutation[point]
        answer.append(len(orbit))
    return tuple(sorted(answer, reverse=True))


def pair_index(permutation: tuple[int, ...]) -> int:
    pairs = set(itertools.combinations(range(6), 2))
    cycles = 0
    while pairs:
        start = min(pairs)
        point = start
        orbit = set()
        while point not in orbit:
            orbit.add(point)
            point = tuple(sorted((permutation[point[0]], permutation[point[1]])))
        pairs -= orbit
        cycles += 1
    return 15 - cycles


def closure_order(generators: tuple[tuple[int, ...], ...]) -> int:
    steps = generators + tuple(reciprocal(generator) for generator in generators)
    found = {IDENTITY}
    pending = deque([IDENTITY])
    while pending:
        element = pending.popleft()
        for step in steps:
            candidate = product(element, step)
            if candidate not in found:
                found.add(candidate)
                pending.append(candidate)
    return len(found)


def main() -> None:
    classes: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for permutation in itertools.permutations(range(6)):
        classes[signature(permutation)].append(permutation)
    assert len(classes) == 11
    assert sum(map(len, classes.values())) == 720

    class_data = {
        kind: (pair_index(elements[0]), (6 - len(kind)) % 2)
        for kind, elements in classes.items()
        if kind != (1, 1, 1, 1, 1, 1)
    }
    assert {kind: data[0] for kind, data in class_data.items()} == {
        (2, 1, 1, 1, 1): 4,
        (2, 2, 1, 1): 6,
        (2, 2, 2): 6,
        (3, 1, 1, 1): 8,
        (3, 2, 1): 10,
        (3, 3): 10,
        (4, 1, 1): 10,
        (4, 2): 10,
        (5, 1): 12,
        (6,): 12,
    }

    kinds = sorted(class_data)
    necessary = set()
    for length in range(2, 5):
        for candidate in itertools.combinations_with_replacement(kinds, length):
            if sum(class_data[kind][0] for kind in candidate) != 16:
                continue
            odd_count = sum(class_data[kind][1] for kind in candidate)
            if odd_count % 2 == 0:
                necessary.add(candidate)
    assert len(necessary) == 9

    pole_5a = (1, 2, 3, 4, 0, 5)
    pole_5b = product(pole_5a, pole_5a)
    audit = {}
    for candidate in sorted(necessary):
        target = 360 if all(class_data[kind][1] == 0 for kind in candidate) else 720
        poles = (pole_5a, pole_5b) if target == 360 else (pole_5a,)
        pole_rows = []
        for pole in poles:
            orders: Counter[int] = Counter()
            for prefix in itertools.product(*(classes[kind] for kind in candidate[:-1])):
                running = pole
                for branch_cycle in prefix:
                    running = product(running, branch_cycle)
                final = reciprocal(running)
                if signature(final) != candidate[-1]:
                    continue
                orders[closure_order((pole,) + prefix + (final,))] += 1
            pole_rows.append(tuple(sorted(orders.items())))
        audit[candidate] = (target, tuple(pole_rows))

    expected = {
        ((2, 1, 1, 1, 1),) * 4: (720, (((120, 125),),)),
        ((2, 1, 1, 1, 1), (2, 1, 1, 1, 1), (3, 1, 1, 1)): (
            720,
            (((120, 25),),),
        ),
        ((2, 1, 1, 1, 1), (2, 2, 1, 1), (2, 2, 2)): (
            720,
            (((720, 25),),),
        ),
        ((2, 1, 1, 1, 1), (6,)): (720, (((720, 5),),)),
        ((2, 2, 1, 1), (3, 3)): (360, (((60, 5),), ((60, 5),))),
        ((2, 2, 1, 1), (4, 2)): (360, (((360, 10),), ((360, 10),))),
        ((2, 2, 2), (3, 2, 1)): (720, (((720, 5),),)),
        ((2, 2, 2), (4, 1, 1)): (720, (((120, 5),),)),
        ((3, 1, 1, 1), (3, 1, 1, 1)): (
            360,
            (((60, 5),), ((60, 5),)),
        ),
    }
    assert audit == expected
    retained = {
        candidate
        for candidate, (target, pole_rows) in audit.items()
        if any(dict(row).get(target, 0) for row in pole_rows)
    }
    assert retained == {
        ((2, 1, 1, 1, 1), (2, 2, 1, 1), (2, 2, 2)),
        ((2, 1, 1, 1, 1), (6,)),
        ((2, 2, 1, 1), (4, 2)),
        ((2, 2, 2), (3, 2, 1)),
    }
    print("RATE_HALF_KB_M4_A6S6_GENUS_ZERO_PASSPORT_REDUCTION_AUDIT_PASS")


if __name__ == "__main__":
    main()
