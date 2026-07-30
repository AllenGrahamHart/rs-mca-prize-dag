#!/usr/bin/env python3
"""Independently enumerate aligned and near saturated matching rows."""


I = frozenset(range(6))
K = frozenset(range(5))
XI = 5
ETA = 6
LABELS = tuple(range(12))


def matchings(vertices):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for index in range(1, len(vertices)):
        second = vertices[index]
        rest = vertices[1:index] + vertices[index + 1:]
        for tail in matchings(rest):
            yield ((first, second),) + tail


def main() -> None:
    aligned = 0
    near = 0
    for edges in matchings(LABELS):
        mate = {}
        for left, right in edges:
            mate[left] = right
            mate[right] = left
        crossing = sum(mate[label] not in I for label in I)
        a = sum(left in K and right in K for left, right in edges)
        b = int(mate[XI] in K)
        if (a, b, crossing) != (1, 1, 2):
            continue

        Lc_aligned = set(range(6, 12))
        omega_aligned = {mate[k] for k in K if mate[k] in Lc_aligned}
        J1 = {mate[i] for i in I if mate[i] not in I}
        assert omega_aligned == J1 and len(omega_aligned) == 2
        aligned += 1

        if mate[ETA] in K:
            Lc_near = set(LABELS) - (set(K) | {ETA})
            omega_near = {mate[k] for k in K if mate[k] in Lc_near}
            assert XI in omega_near and len(omega_near) == 2
            assert next(label for label in omega_near if label != XI) in J1
            near += 1

    assert aligned == 2700
    assert near == 900
    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SOURCE_LINE_COLORED_QUOTIENT_COMPILER_AUDIT_PASS "
        "aligned_matchings=2700 near_saturated_matchings=900 Omega_size=2"
    )


if __name__ == "__main__":
    main()
