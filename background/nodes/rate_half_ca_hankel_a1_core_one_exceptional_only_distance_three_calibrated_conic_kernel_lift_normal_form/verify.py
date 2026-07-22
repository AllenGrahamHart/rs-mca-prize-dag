#!/usr/bin/env python3
"""Exact regression checks for the calibrated conic kernel-lift normal form."""

from __future__ import annotations


P = 1009


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % P == 0:
        poly.pop()
    return [value % P for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % P
    return trim(out)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([(scalar * value) % P for value in poly])


def mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    return trim(out)


def power(poly: list[int], exponent: int) -> list[int]:
    out = [1]
    base = poly
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        base = mul(base, base)
        exponent >>= 1
    return out


def evaluate(poly: list[int], point: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * point + coefficient) % P
    return out


def locator(roots: list[int]) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % P, 1])
    return out


def divide_exact(numerator: list[int], denominator: list[int]) -> list[int]:
    work = numerator[:] + [0]
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse_lead = pow(denominator[-1], P - 2, P)
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient = work[shift + len(denominator) - 1] * inverse_lead % P
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            work[shift + index] = (work[shift + index] - coefficient * value) % P
    require(not any(work[: len(denominator) - 1]), "nonexact division")
    return trim(quotient)


def interpolate(points: list[int], values: list[int]) -> list[int]:
    out = [0]
    for index, point in enumerate(points):
        basis = [1]
        denominator = 1
        for other_index, other in enumerate(points):
            if other_index == index:
                continue
            basis = mul(basis, [(-other) % P, 1])
            denominator = denominator * (point - other) % P
        out = add(out, scale(basis, values[index] * pow(denominator, P - 2, P)))
    return out


def check_conic_lifts() -> tuple[int, int]:
    e = 4
    internal = [2, 3, 5, 7]
    lambdas = [11, 13, 17, 19]
    pair_roots = [(40, 41), (43, 47), (53, 59), (61, 67)]
    p_z = locator(list(range(20, 32)))
    i_poly = locator(internal)

    constants = [
        evaluate(p_z, xi) * pow(lam, P - 2, P) % P
        for xi, lam in zip(internal, lambdas, strict=True)
    ]
    sigmas = [(left + right) % P for left, right in pair_roots]
    products = [(left * right) % P for left, right in pair_roots]
    r_0 = interpolate(internal, [c * product % P for c, product in zip(constants, products, strict=True)])
    r_1 = interpolate(internal, [(-c * sigma) % P for c, sigma in zip(constants, sigmas, strict=True)])
    r_2 = interpolate(internal, constants)

    checked = 0
    for row, leading in zip((101, 103, 107, 109, 113), (23, 29, 31, 37, 41), strict=True):
        residue = add(add(r_0, scale(r_1, row)), scale(r_2, row * row))
        j_poly = [row + 1, 2 * row + 3, row * row + 5, 7, leading]
        scaled_complement = add(residue, mul(i_poly, j_poly))
        recovered = divide_exact(add(scaled_complement, scale(residue, -1)), i_poly)
        require(recovered == trim(j_poly), "kernel lift recovery mismatch")
        require(len(recovered) - 1 == e and recovered[-1] == leading, "lift leading coefficient mismatch")
        for index, xi in enumerate(internal):
            d_value = (row * row - sigmas[index] * row + products[index]) % P
            require(
                evaluate(scaled_complement, xi) == constants[index] * d_value % P,
                "calibrated conic value mismatch",
            )
        checked += 1
    return checked, len(r_0) + len(r_1) + len(r_2)


def check_design_product() -> tuple[int, int]:
    e = 4
    roots = list(range(1, 3 * e + 1))
    p_z = locator(roots)
    blocks: list[tuple[int, ...]] = []
    for base in ({0, 1, 2, 3}, {0, 1, 3, 6}):
        for shift in range(3 * e):
            blocks.append(tuple(sorted({(index + shift) % (3 * e) for index in base})))
    blocks.extend(((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11)))

    require(len(blocks) == len(set(blocks)) == 6 * e + 3, "design blocks repeat")
    replication = [sum(index in block for block in blocks) for index in range(3 * e)]
    require(replication == [2 * e + 1] * (3 * e), "wrong design replication")

    product = [1]
    for block in blocks:
        g_x = locator([roots[index] for index in block])
        product = mul(product, divide_exact(p_z, g_x))
    expected_exponent = (6 * e + 3) - (2 * e + 1)
    require(product == power(p_z, expected_exponent), "complement product mismatch")
    return len(blocks), expected_exponent


def main() -> None:
    lifts, interpolation_size = check_conic_lifts()
    blocks, exponent = check_design_product()
    print(
        "RATE_HALF_DISTANCE_THREE_CALIBRATED_CONIC_KERNEL_LIFT_NORMAL_FORM_PASS "
        f"lifts={lifts} interpolation_size={interpolation_size} "
        f"blocks={blocks} product_exponent={exponent}"
    )


if __name__ == "__main__":
    main()
