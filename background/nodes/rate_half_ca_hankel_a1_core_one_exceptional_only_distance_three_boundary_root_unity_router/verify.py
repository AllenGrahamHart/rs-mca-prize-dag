#!/usr/bin/env python3
"""Boundary root-unity replay on the exact F_17 route fence."""

from __future__ import annotations


P = 17
E = 1
N = 16
CORE = 1
OMITTED = 14


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def locator(roots: tuple[int, ...], x: int) -> int:
    value = 1
    for root in roots:
        value = value * (x - root) % P
    return value


def p_x_derivative(x: int, omitted: int = OMITTED) -> int:
    return N * inv(x) * inv((x - CORE) * (x - omitted)) % P


def main() -> None:
    roots_a = (2, 5)
    triple = (3, 13, 15)
    a, b = roots_a

    u_ab = locator(triple, a) * inv(locator(triple, b)) % P
    zeta = (
        -p_x_derivative(a)
        * inv(p_x_derivative(b))
        * inv(pow(u_ab, 4, P))
    ) % P
    assert zeta == 1
    assert pow(zeta, E, P) == 1

    triple_gates = {}
    for index, t in enumerate(triple):
        for u in triple[index + 1 :]:
            v_tu = locator(roots_a, t) * inv(locator(roots_a, u)) % P
            b_prime_t = locator(tuple(x for x in triple if x != t), t)
            b_prime_u = locator(tuple(x for x in triple if x != u), u)
            w_tu = b_prime_t * inv(b_prime_u) % P
            eta = (
                p_x_derivative(t)
                * inv(p_x_derivative(u))
                * inv(pow(v_tu, 4, P) * w_tu)
            ) % P
            triple_gates[(t, u)] = eta
            assert eta == 1
            assert pow(eta, E, P) == 1

    # A false omitted row breaks the pair gate before any slope variables.
    mutated = (
        -p_x_derivative(a, omitted=4)
        * inv(p_x_derivative(b, omitted=4))
        * inv(pow(u_ab, 4, P))
    ) % P
    assert mutated == 5
    assert pow(mutated, E, P) != 1

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_BOUNDARY_ROOT_UNITY_ROUTER_PASS "
        f"field={P} pair_gate={zeta} triple_gates={triple_gates} mutation={mutated}"
    )


if __name__ == "__main__":
    main()
