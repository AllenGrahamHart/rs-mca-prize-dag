#!/usr/bin/env python3
"""Light verifier for affine character cancellation over prime fields."""

from cmath import exp, pi


def char(p: int, x: int) -> complex:
    return exp(2j * pi * (x % p) / p)


def dot(a: tuple[int, ...], x: tuple[int, ...], p: int) -> int:
    return sum(ai * xi for ai, xi in zip(a, x)) % p


def points(p: int, dim: int):
    if dim == 0:
        yield ()
        return
    for tail in points(p, dim - 1):
        for x in range(p):
            yield tail + (x,)


def main() -> None:
    for p in (3, 5, 7):
        for dim in range(1, 4):
            for coeff in points(p, dim):
                if all(c == 0 for c in coeff):
                    continue
                for offset in range(p):
                    for xi in range(1, p):
                        total = sum(char(p, xi * (dot(coeff, x, p) + offset)) for x in points(p, dim))
                        assert abs(total) < 1e-8, (p, dim, coeff, offset, xi, total)

    print("PASS: nonconstant affine maps have zero nontrivial character sums")


if __name__ == "__main__":
    main()
