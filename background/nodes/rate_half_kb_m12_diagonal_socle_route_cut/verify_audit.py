#!/usr/bin/env python3
"""Reconstruct the exceptional M12 degree-12 cross-action."""

from collections import deque
from pathlib import Path


NODE = Path(__file__).resolve().parent
DEGREE = 12


def permutation(cycles):
    result = list(range(DEGREE))
    for cycle in cycles:
        points = [point - 1 for point in cycle]
        for source, target in zip(points, points[1:] + points[:1]):
            result[source] = target
    return bytes(result)


def compose(left, right):
    return bytes(left[right[index]] for index in range(len(left)))


def paired(left, right):
    return left + right


def main() -> None:
    evidence = (NODE / "source_evidence.md").read_text()
    audit = (NODE / "audit.md").read_text()
    assert "5612e113d50ac23a7d10945383936e20440b4e14" in evidence
    assert "55af41251add2886aedb2ebf04dfb522776768a245dd9e6cd8369094cf84aa38" in evidence
    assert "twisted diagonals" in audit

    # ATLAS standard generators for M12G1-p12aB0.
    a1 = permutation(((1, 4), (3, 10), (5, 11), (6, 12)))
    a2 = permutation(((1, 8, 9), (2, 3, 4), (5, 12, 11), (6, 10, 7)))

    # The same abstract standard generators in M12G1-p12bB0.
    b1 = permutation(((2, 3), (5, 6), (8, 9), (11, 12)))
    b2 = permutation(((1, 2, 4), (3, 5, 7), (6, 8, 10), (9, 11, 12)))

    generators = (paired(a1, b1), paired(a2, b2))
    identity = bytes(range(DEGREE)) * 2
    group = {identity}
    queue = deque((identity,))
    while queue:
        element = queue.popleft()
        left, right = element[:DEGREE], element[DEGREE:]
        for generator in generators:
            candidate = paired(
                compose(generator[:DEGREE], left),
                compose(generator[DEGREE:], right),
            )
            if candidate not in group:
                group.add(candidate)
                queue.append(candidate)

    assert len(group) == 95_040
    stabilizer = tuple(element for element in group if element[0] == 0)
    assert len(stabilizer) == 7_920

    same_orbits = [len({element[point] for element in stabilizer})
                   for point in range(DEGREE)]
    cross_orbits = [len({element[DEGREE + point] for element in stabilizer})
                    for point in range(DEGREE)]
    assert sorted(same_orbits) == [1] + [11] * 11
    assert cross_orbits == [12] * 12
    print("RATE_HALF_KB_M12_DIAGONAL_SOCLE_ROUTE_CUT_AUDIT_PASS")


if __name__ == "__main__":
    main()
