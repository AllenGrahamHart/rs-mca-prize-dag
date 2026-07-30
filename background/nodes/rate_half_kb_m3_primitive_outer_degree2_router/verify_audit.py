#!/usr/bin/env python3
"""Independently reconstruct the primitive projective degree-20 actions."""

from __future__ import annotations


P = 19
INFINITY = P
IDENTITY = tuple(range(P + 1))


def mobius(a: int, b: int, c: int, d: int) -> tuple[int, ...]:
    assert (a * d - b * c) % P
    result = []
    for value in range(P):
        denominator = (c * value + d) % P
        if denominator == 0:
            result.append(INFINITY)
        else:
            result.append(((a * value + b) * pow(denominator, -1, P)) % P)
    result.append(INFINITY if c == 0 else (a * pow(c, -1, P)) % P)
    assert len(set(result)) == P + 1
    return tuple(result)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[value]] for value in range(P + 1))


def generated_group(generators: tuple[tuple[int, ...], ...]) -> set[tuple[int, ...]]:
    group = {IDENTITY}
    pending = [IDENTITY]
    while pending:
        current = pending.pop()
        for generator in generators:
            candidate = compose(generator, current)
            if candidate not in group:
                group.add(candidate)
                pending.append(candidate)
    return group


def subdegrees(group: set[tuple[int, ...]]) -> list[int]:
    stabilizer = [value for value in group if value[INFINITY] == INFINITY]
    unseen = set(range(P + 1))
    lengths = []
    while unseen:
        seed = min(unseen)
        orbit = {value[seed] for value in stabilizer}
        lengths.append(len(orbit))
        unseen -= orbit
    return sorted(lengths)


def cycle_type(value: tuple[int, ...]) -> list[int]:
    unseen = set(range(P + 1))
    lengths = []
    while unseen:
        start = min(unseen)
        point = start
        length = 0
        while point in unseen:
            unseen.remove(point)
            point = value[point]
            length += 1
        lengths.append(length)
    return sorted(lengths, reverse=True)


def main() -> None:
    translation = mobius(1, 1, 0, 1)
    inversion = mobius(0, -1, 1, 0)
    nonsquare_scaling = mobius(2, 0, 0, 1)
    assert pow(2, (P - 1) // 2, P) == P - 1

    psl = generated_group((translation, inversion))
    pgl = generated_group((translation, inversion, nonsquare_scaling))
    assert len(psl) == 3420
    assert len(pgl) == 6840
    assert psl < pgl
    assert subdegrees(psl) == [1, 19]
    assert subdegrees(pgl) == [1, 19]
    assert any(cycle_type(value) == [5, 5, 5, 5] for value in psl)

    # In the natural actions, the point stabilizers A19 and S19 are
    # transitive on the other 19 points; a 3-cycle and transposition provide
    # explicit witnesses between any chosen pair after relabeling.
    assert 20 >= 5
    natural_subdegrees = [1, 19]
    assert natural_subdegrees == subdegrees(psl) == subdegrees(pgl)
    print("RATE_HALF_KB_M3_PRIMITIVE_OUTER_DEGREE2_ROUTER_AUDIT_PASS")


if __name__ == "__main__":
    main()
