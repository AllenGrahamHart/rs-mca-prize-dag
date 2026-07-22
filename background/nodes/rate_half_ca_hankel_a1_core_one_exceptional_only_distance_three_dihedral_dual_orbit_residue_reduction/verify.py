#!/usr/bin/env python3
"""Exact controls for the dihedral dual orbit-residue formulas."""

from __future__ import annotations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return out


def locator(roots: list[int], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        out = multiply(out, [(-root) % prime, 1], prime)
    return out


def evaluate(poly: list[int], point: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % prime
    return value


def derivative(poly: list[int], prime: int) -> list[int]:
    return [index * coefficient % prime for index, coefficient in enumerate(poly)][1:]


def product(values: list[int], prime: int) -> int:
    out = 1
    for value in values:
        out = out * value % prime
    return out


def inverse(value: int, prime: int) -> int:
    require(value % prime != 0, "attempted to invert zero")
    return pow(value, prime - 2, prime)


def orbit_fixture(kind: str) -> tuple[int, int, list[tuple[int, int]], list[int], int, int]:
    prime = 97
    n = 24
    generator = pow(5, 4, prime)
    subgroup = sorted({pow(generator, index, prime) for index in range(n)})
    require(len(subgroup) == n, "toy subgroup has wrong order")

    if kind == "antipodal":
        c = -1 % prime
        involution = lambda value: -value % prime
    elif kind == "constant_product":
        c = pow(generator, 3, prime)
        involution = lambda value: c * inverse(value, prime) % prime
    else:
        raise ValueError(kind)

    orbits = sorted(
        {
            tuple(sorted((value, involution(value))))
            for value in subgroup
            if value != involution(value)
        }
    )
    pairs = orbits[:2]
    exceptional = {value for pair in pairs for value in pair}
    boundary = [value for value in subgroup if value not in exceptional][:5]
    s, x_zero = boundary[:2]
    triple = boundary[2:]
    require(len(set(boundary) | exceptional) == 9, "fixture roots are not disjoint")
    return prime, n, pairs, triple, s, x_zero


def check_branch(kind: str) -> None:
    prime, n, pairs, triple, s, x_zero = orbit_fixture(kind)
    e = len(pairs)
    subgroup = sorted({value for value in range(1, prime) if pow(value, n, prime) == 1})
    exceptional = [value for pair in pairs for value in pair]
    outside = [
        value
        for value in subgroup
        if value not in set(exceptional + triple + [s, x_zero])
    ]
    require(len(outside) == 6 * e + 3, "outside support has wrong size")

    b_poly = locator(triple, prime)
    c_poly = locator(outside, prime)
    c_triple_product = product([evaluate(c_poly, point, prime) for point in triple], prime)

    if kind == "antipodal":
        orbit_roots = [a * a % prime for a, _ in pairs]
        scale = 4 * c_triple_product * inverse(n * n % prime, prime) % prime

        def weight(u: int) -> int:
            values = [u * u, u - s * s, u - x_zero * x_zero]
            values.extend(u - point * point for point in triple)
            return product([value % prime for value in values], prime)

    else:
        a, b = pairs[0]
        c = a * b % prime
        require(all(left * right % prime == c for left, right in pairs), "product orbit changed")
        orbit_roots = [(left + right) % prime for left, right in pairs]
        scale = pow(c, e, prime) * c_triple_product * inverse(n * n % prime, prime) % prime

        def weight(u: int) -> int:
            values = [u * u - 4 * c, c + s * s - s * u, c + x_zero * x_zero - x_zero * u]
            values.extend(c + point * point - point * u for point in triple)
            return product([value % prime for value in values], prime)

    e_poly = locator(orbit_roots, prime)
    e_derivative = derivative(e_poly, prime)
    residues = []
    weights = []
    derivative_values = []

    for pair, orbit_root in zip(pairs, orbit_roots, strict=True):
        d_poly = locator(list(pair), prime)
        direct = product(
            [
                evaluate(b_poly, point, prime)
                * inverse(evaluate(d_poly, point, prime), prime)
                % prime
                for point in outside
            ],
            prime,
        )
        derivative_value = evaluate(e_derivative, orbit_root, prime)
        orbit_weight = weight(orbit_root)
        reduced = scale * orbit_weight * derivative_value * derivative_value % prime
        require(direct == reduced, f"{kind} orbit-residue formula failed")
        residues.append(direct)
        weights.append(orbit_weight)
        derivative_values.append(derivative_value)

    global_reduction = (
        pow(scale, e, prime)
        * product(weights, prime)
        * pow(product(derivative_values, prime), 2, prime)
        % prime
    )
    require(product(residues, prime) == global_reduction, f"{kind} global reduction failed")


def main() -> None:
    check_branch("antipodal")
    check_branch("constant_product")
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_DISTANCE_THREE_"
        "DIHEDRAL_DUAL_ORBIT_RESIDUE_REDUCTION_PASS branches=2 e=2 field=97"
    )


if __name__ == "__main__":
    main()
