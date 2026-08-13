#!/usr/bin/env python3
"""Independent exhaustive GF(5) audit of codimension-one RS extensions."""

from itertools import product


P = 5
N = 5


def weight(word: tuple[int, ...]) -> int:
    return sum(value != 0 for value in word)


def span_word(
    codeword: tuple[int, ...], scalar: int, direction: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple((value + scalar * extra) % P
                 for value, extra in zip(codeword, direction))


def dependent(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    return any(
        all((b - scalar * a) % P == 0 for a, b in zip(left, right))
        for scalar in range(P)
    )


def weights(words: frozenset[tuple[int, ...]]) -> tuple[int, int, int]:
    nonzero = [word for word in words if any(word)]
    first = min(map(weight, nonzero))
    second = N
    for index, left in enumerate(nonzero):
        for right in nonzero[index + 1:]:
            if dependent(left, right):
                continue
            union = sum(a != 0 or b != 0 for a, b in zip(left, right))
            second = min(second, union)
    full = sum(any(word[index] for word in words) for index in range(N))
    return first, second, full


def main() -> None:
    code = [
        tuple((constant + slope * x) % P for x in range(N))
        for constant, slope in product(range(P), repeat=2)
    ]
    code_set = frozenset(code)
    extensions: dict[frozenset[tuple[int, ...]], int] = {}
    for direction in product(range(P), repeat=N):
        if direction in code_set:
            continue
        extension = frozenset(
            span_word(codeword, scalar, direction)
            for codeword in code
            for scalar in range(P)
        )
        distance = min(
            weight(tuple((a - b) % P for a, b in zip(direction, codeword)))
            for codeword in code
        )
        if extension in extensions and extensions[extension] != distance:
            raise ValueError("coset distance invariance")
        extensions[extension] = distance

    if len(extensions) != 31:
        raise ValueError("extension census")
    profile: dict[int, int] = {}
    for extension, distance in extensions.items():
        observed = weights(extension)
        if observed != (distance, 4, 5):
            raise ValueError("near-MDS hierarchy")
        profile[distance] = profile.get(distance, 0) + 1
    if sum(profile.values()) != 31 or set(profile) != {1, 2, 3}:
        raise ValueError("distance profile")
    print(
        "RATE_HALF_MCA_FULL_LIFT_NEAR_MDS_EXTENSION_REDUCTION_AUDIT_PASS "
        f"extensions={len(extensions)} profile={sorted(profile.items())}"
    )


if __name__ == "__main__":
    main()
