#!/usr/bin/env python3
"""Independent GF(5), K=2 audit of the lifted-rank gauge dichotomy."""

from itertools import product


P = 5


def rank(vectors: list[tuple[int, ...]]) -> int:
    if not vectors:
        return 0
    if any(any(value % P for value in vector) for vector in vectors):
        if len(vectors[0]) == 1:
            return 1
    if len(vectors[0]) == 2:
        nonzero = [vector for vector in vectors if vector != (0, 0)]
        if not nonzero:
            return 0
        first = nonzero[0]
        return 2 if any(
            (first[0] * other[1] - first[1] * other[0]) % P
            for other in nonzero[1:]
        ) else 1
    # The audit uses dimensions three only for lifted/error vectors.
    for left in range(len(vectors)):
        for middle in range(left + 1, len(vectors)):
            for right in range(middle + 1, len(vectors)):
                a, b, c = vectors[left], vectors[middle], vectors[right]
                determinant = (
                    a[0] * (b[1] * c[2] - b[2] * c[1])
                    - a[1] * (b[0] * c[2] - b[2] * c[0])
                    + a[2] * (b[0] * c[1] - b[1] * c[0])
                ) % P
                if determinant:
                    return 3
    return 2 if any(
        any((a[i] * b[j] - a[j] * b[i]) % P
            for i in range(3) for j in range(i + 1, 3))
        for a in vectors for b in vectors
    ) else int(any(any(value % P for value in vector) for vector in vectors))


def gauge_histogram(points: list[tuple[int, tuple[int, int]]]) -> dict[int, int]:
    histogram: dict[int, int] = {}
    for gauge in product(range(P), repeat=2):
        transformed = [
            ((word[0] - slope * gauge[0]) % P,
             (word[1] - slope * gauge[1]) % P)
            for slope, word in points
        ]
        value = rank(transformed)
        histogram[value] = histogram.get(value, 0) + 1
    return histogram


def main() -> None:
    drop = [(1, (1, 0)), (2, (2, 1))]
    full = [(1, (1, 0)), (2, (0, 1)), (3, (0, 0))]
    if rank([(slope, *word) for slope, word in drop]) != 2:
        raise ValueError("drop lifted rank")
    if rank([(slope, *word) for slope, word in full]) != 3:
        raise ValueError("full lifted rank")
    if gauge_histogram(drop) != {1: 5, 2: 20}:
        raise ValueError("drop gauge histogram")
    if gauge_histogram(full) != {2: 25}:
        raise ValueError("full gauge histogram")
    drop_errors = [(-word[0] % P, -word[1] % P, slope) for slope, word in drop]
    full_errors = [(-word[0] % P, -word[1] % P, slope) for slope, word in full]
    if rank(drop_errors) != 2 or rank(full_errors) != 3:
        raise ValueError("error rank")

    perturbed = drop + [(3, (0, 0))]
    if rank([(slope, *word) for slope, word in perturbed]) != 3:
        raise ValueError("hostile lifted perturbation")
    if gauge_histogram(perturbed) != {2: 25}:
        raise ValueError("hostile gauge perturbation")
    print(
        "RATE_HALF_MCA_FULL_EXPLANATION_LIFTED_RANK_GAUGE_DICHOTOMY_AUDIT_PASS "
        "gauges=50 hostile=1"
    )


if __name__ == "__main__":
    main()
