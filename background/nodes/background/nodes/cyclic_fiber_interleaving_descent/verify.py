#!/usr/bin/env python3
"""Replay cyclic-fiber Fourier descent on an exact finite-field model."""

from __future__ import annotations

from itertools import product


P = 17
N = 8
K_DIM = 4
GEN = 3
H = tuple(pow(GEN, 2 * i, P) for i in range(N))
WORD = tuple((3 * i * i + 5 * i + 7) % P for i in range(N))


def ev(coeffs: tuple[int, ...], x: int) -> int:
    value = 0
    for coefficient in reversed(coeffs):
        value = (value * x + coefficient) % P
    return value


def check(modulus: int) -> None:
    assert N % modulus == 0 and K_DIM % modulus == 0
    zeta = pow(GEN, (P - 1) // modulus, P)
    image = tuple(dict.fromkeys(pow(x, modulus, P) for x in H))
    representatives = {y: next(x for x in H if pow(x, modulus, P) == y) for y in image}
    inv_m = pow(modulus, -1, P)

    transformed: dict[int, tuple[int, ...]] = {}
    mutated: dict[int, tuple[int, ...]] = {}
    for y, x in representatives.items():
        fiber_values = tuple(WORD[H.index((pow(zeta, j, P) * x) % P)] for j in range(modulus))
        transformed[y] = tuple(
            pow(x, -r, P)
            * inv_m
            * sum(pow(zeta, -j * r, P) * fiber_values[j] for j in range(modulus))
            % P
            for r in range(modulus)
        )
        mutated[y] = tuple(
            inv_m
            * sum(pow(zeta, -j * r, P) * fiber_values[j] for j in range(modulus))
            % P
            for r in range(modulus)
        )

    if transformed == mutated:
        raise AssertionError((modulus, "missing representative normalization was not detected"))

    seen = set()
    for coeffs in product(range(P), repeat=K_DIM):
        components = tuple(tuple(coeffs[r + modulus * j] for j in range(K_DIM // modulus)) for r in range(modulus))
        seen.add(components)
        full_fibers = 0
        component_agreements = 0
        for y, x in representatives.items():
            full = all(
                ev(coeffs, (pow(zeta, j, P) * x) % P)
                == WORD[H.index((pow(zeta, j, P) * x) % P)]
                for j in range(modulus)
            )
            component = all(ev(components[r], y) == transformed[y][r] for r in range(modulus))
            if full != component:
                raise AssertionError((modulus, coeffs, y, full, component))
            full_fibers += full
            component_agreements += component
        if full_fibers != component_agreements:
            raise AssertionError((modulus, coeffs))

    if len(seen) != P**K_DIM:
        raise AssertionError((modulus, "decomposition is not injective"))


def main() -> None:
    check(2)
    check(4)
    print("CYCLIC_FIBER_INTERLEAVING_DESCENT_PASS models=2 polynomials=167042")


if __name__ == "__main__":
    main()
