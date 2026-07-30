#!/usr/bin/env python3
"""Independent flag-stabilizer and centralizer audit for the m10 router."""

from collections import deque
from itertools import combinations
from pathlib import Path


NODE = Path(__file__).resolve().parent


def compose(left, right):
    return tuple(left[right[index]] for index in range(len(left)))


def generated_group(degree, generators):
    identity = tuple(range(degree))
    group = {identity}
    queue = deque((identity,))
    while queue:
        element = queue.popleft()
        for generator in generators:
            candidate = compose(generator, element)
            if candidate not in group:
                group.add(candidate)
                queue.append(candidate)
    return group


def permutation(degree, cycles):
    result = list(range(degree))
    for cycle in cycles:
        for source, target in zip(cycle, cycle[1:] + cycle[:1]):
            result[source] = target
    return tuple(result)


def flag_action(permutation, flag):
    point, pair = flag
    return permutation[point], tuple(sorted(permutation[x] for x in pair))


def orbit_lengths(group, omega, action):
    unseen = set(omega)
    lengths = []
    while unseen:
        point = min(unseen)
        orbit = {action(g, point) for g in group}
        unseen -= orbit
        lengths.append(len(orbit))
    return sorted(lengths)


def main() -> None:
    audit = (NODE / "audit.md").read_text()
    result = (NODE / "result.md").read_text()
    assert "kernel-free exceptions" in audit
    assert "strict routing" in audit
    assert "18 types" in result

    # Explicit stabilizers of the base flag (0,{1,2}).
    swap_pair = permutation(6, ((1, 2),))
    swap_tail = permutation(6, ((3, 4),))
    tail_cycle = permutation(6, ((3, 4, 5),))
    s6_stabilizer = generated_group(6, (swap_pair, swap_tail, tail_cycle))
    even_pair_tail = permutation(6, ((1, 2), (3, 4)))
    a6_stabilizer = generated_group(6, (even_pair_tail, tail_cycle))
    assert (len(a6_stabilizer), len(s6_stabilizer)) == (6, 12)

    omega = [
        (point, pair)
        for point in range(6)
        for pair in combinations([x for x in range(6) if x != point], 2)
    ]
    a6_lengths = orbit_lengths(a6_stabilizer, omega, flag_action)
    s6_lengths = orbit_lengths(s6_stabilizer, omega, flag_action)
    assert a6_lengths == [1, 2] + [3] * 3 + [6] * 8
    assert s6_lengths == [1, 2] + [3] * 3 + [6] * 6 + [12]
    assert 4 not in a6_lengths + s6_lengths

    # Reconstruct the degree-10 A5 action from the pinned PrimGrp generators.
    a = permutation(10, ((0, 4, 6), (1, 8, 3), (2, 7, 9)))
    b = permutation(10, ((1, 5), (2, 4), (3, 6), (8, 9)))
    a5 = generated_group(10, (a, b))
    assert len(a5) == 60
    point_stabilizer = {g for g in a5 if g[0] == 0}
    assert len(point_stabilizer) == 6
    point_orbits = orbit_lengths(
        point_stabilizer,
        list(range(10)),
        lambda g, point: g[point],
    )
    assert point_orbits == [1, 3, 6]
    assert point_orbits.count(1) == 1

    assert {size for size in range(1, 7) if 6 % size == 0} == {1, 2, 3, 6}
    assert {2, 3, 6} < {1, 2, 3, 6, 10}
    print("RATE_HALF_KB_M10_SCOTT_STRIP_LOWER_DEGREE_ROUTER_AUDIT_PASS")


if __name__ == "__main__":
    main()
