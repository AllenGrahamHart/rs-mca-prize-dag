#!/usr/bin/env python3
"""Mutation checks for the arbitrary-line syndrome criterion."""

from verify import bad_slopes, error_spaces


def main() -> None:
    prime, n, redundancy, radius = 7, 6, 3, 2
    _, spaces = error_spaces(prime, n, redundancy, radius)
    first, second = (0, 1, 0), (0, 0, 1)
    truth = bad_slopes(first, second, prime, spaces)
    assert truth == tuple(range(prime))

    # Removing the non-mutuality clause turns every jointly correctable pair
    # into a false MCA witness. The zero syndrome pair exposes the mutation.
    zero = (0,) * redundancy
    mutated = []
    for slope in range(prime):
        combined = tuple((x + slope * y) % prime for x, y in zip(zero, zero, strict=True))
        if any(combined in space for _, space in spaces):
            mutated.append(slope)
    assert mutated == list(range(prime))
    assert bad_slopes(zero, zero, prime, spaces) == ()

    print("RATE_HALF_ARBITRARY_LINE_SYNDROME_ROUTER_AUDIT_PASS mutations=1/1")


if __name__ == "__main__":
    main()
