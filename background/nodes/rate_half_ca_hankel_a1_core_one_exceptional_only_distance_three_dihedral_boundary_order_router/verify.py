#!/usr/bin/env python3
"""Exact checks for the distance-three dihedral boundary-order router."""

from __future__ import annotations

from itertools import combinations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return out


def locator(roots: list[int], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % prime, 1], prime)
    return out


def power(poly: list[int], exponent: int, prime: int) -> list[int]:
    out = [1]
    for _ in range(exponent):
        out = mul(out, poly, prime)
    return out


def proportional(left: list[int], right: list[int], prime: int) -> bool:
    scale = None
    for a, b in zip(left, right, strict=True):
        if b % prime:
            scale = a * pow(b, prime - 2, prime) % prime
            break
        if a % prime:
            return False
    if scale is None:
        return not any(value % prime for value in left)
    return all((a - scale * b) % prime == 0 for a, b in zip(left, right, strict=True))


def evaluate(poly: list[int], point: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % prime
    return value


def derivative(poly: list[int], prime: int) -> list[int]:
    return [index * coefficient % prime for index, coefficient in enumerate(poly)][1:]


def main() -> None:
    e = (1 << 38) - 1
    n = 1 << 41
    require(e == 3 * 174763 * 524287, "factorization of e failed")
    require(n == 8 * e + 8, "reciprocal exponent does not equal N")

    prime_factors = (3, 174763, 524287)
    divisors = {1}
    for factor in prime_factors:
        divisors |= {value * factor for value in tuple(divisors)}
    large = sorted(value for value in divisors if 14 * value >= e)
    require(large == [e // 3, e], "large divisor classification failed")

    prime = 17
    nonzero = set(range(1, prime))
    stable_triples = [
        triple
        for triple in combinations(nonzero, 3)
        if {(-value) % prime for value in triple} == set(triple)
    ]
    require(not stable_triples, "nonzero negation-stable triple exists")

    c = 4
    s, x_zero = 3, 7
    triple = [1, 2, 4]
    require({c * pow(value, prime - 2, prime) % prime for value in (s, x_zero)} == {s, x_zero}, "simple roots are not inversion-stable")
    require({c * pow(value, prime - 2, prime) % prime for value in triple} == set(triple), "triple is not inversion-stable")
    require(c == s * x_zero % prime, "simple roots do not form one two-cycle")
    fixed_triple = [value for value in triple if value * value % prime == c]
    require(fixed_triple == [2], "triple does not have one fixed point")

    fixed_points = {value for value in nonzero if value * value % prime == c}
    require(len(fixed_points) == 2, "toy inversion does not have two fixed points")
    disjoint_stable_triples = [
        candidate
        for candidate in combinations(nonzero - fixed_points, 3)
        if {c * pow(value, prime - 2, prime) % prime for value in candidate}
        == set(candidate)
    ]
    require(not disjoint_stable_triples, "a stable odd set avoided all fixed points")

    b_poly = locator(triple, prime)
    f_poly = mul(locator([s, x_zero], prime), power(b_poly, 4, prime), prime)
    require(len(f_poly) == 15, "boundary polynomial has wrong degree")
    reciprocal = [
        f_poly[14 - index] * pow(c, 14 - index, prime) % prime
        for index in range(15)
    ]
    require(proportional(f_poly, reciprocal, prime), "reciprocal control is not proportional")

    # The divisor symmetry is real, but it fails the independent triple gate.
    toy_e = 1
    toy_n = 16
    a_poly = locator([5, 11], prime)
    b_derivative = derivative(b_poly, prime)

    def p_derivative(point: int) -> int:
        denominator = point * (point - s) * (point - x_zero) % prime
        return toy_n * pow(denominator, prime - 2, prime) % prime

    def k_b(point: int) -> int:
        denominator = pow(evaluate(a_poly, point, prime), 4, prime)
        denominator = denominator * evaluate(b_derivative, point, prime) % prime
        return p_derivative(point) * pow(denominator, prime - 2, prime) % prime

    u, t, mate = 2, 1, 4
    triple_ratio = k_b(mate) * pow(k_b(t), prime - 2, prime) % prime
    require(triple_ratio == pow(u * pow(t, prime - 2, prime) % prime, 3, prime), "triple ratio formula failed")
    require(pow(triple_ratio, toy_e, prime) != 1, "reciprocal toy packet passed the triple gate")

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_DIHEDRAL_BOUNDARY_ORDER_ROUTER_PASS "
        f"large_gcds={large} reciprocal_rejected=1 triple_ratio={triple_ratio} "
        "orbit_normal_form=1 "
        "antipodal_constant=0"
    )


if __name__ == "__main__":
    main()
