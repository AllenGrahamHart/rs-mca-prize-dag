#!/usr/bin/env python3
"""Verify finite algebra behind the PMA diffuse hyperplane reduction."""

from __future__ import annotations

from itertools import combinations, product


CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def inv(value: int, p: int) -> int:
    return pow(value % p, p - 2, p)


def hyperplane_coefficients(xs: tuple[int, ...], cs: tuple[int, ...], p: int) -> tuple[int, ...]:
    lambdas = []
    for j, x in enumerate(xs):
        denominator = 1
        for m, y in enumerate(xs):
            if m != j:
                denominator = denominator * (x - y) % p
        lambdas.append(inv(denominator, p))
    return tuple(sum(lambdas[j] * cs[j] * pow(xs[j], t, p) for j in range(5)) % p for t in range(4))


for p in (7, 11, 17):
    xs = tuple(range(1, 6))
    for cs in combinations(range(1, p), 5):
        coeff = hyperplane_coefficients(xs, cs, p)
        check(any(coeff), f"nonzero divided difference p={p}, cs={cs}")
    equal = hyperplane_coefficients(xs, (1, 1, 1, 1, 1), p)
    check(not any(equal), f"equal-scalar negative control p={p}")


# Exhaust every nonzero symmetric multi-affine hyperplane over F_7 on a
# six-point core and check the strict K^2/2 split-locator bound directly.
p = 7
core = tuple(range(6))
K = len(core)
for alpha, beta, gamma, delta in product(range(p), repeat=4):
    if alpha == beta == gamma == delta == 0:
        continue
    count = 0
    for a, b, c in combinations(core, 3):
        value = (
            alpha
            + beta * (a + b + c)
            + gamma * (a * b + a * c + b * c)
            + delta * a * b * c
        ) % p
        count += value == 0
    check(2 * count < K * K, f"split bound coeff={(alpha,beta,gamma,delta)} count={count}")

print(f"PMA diffuse d3 hyperplane reduction: PASS ({CHECKS} checks)")
