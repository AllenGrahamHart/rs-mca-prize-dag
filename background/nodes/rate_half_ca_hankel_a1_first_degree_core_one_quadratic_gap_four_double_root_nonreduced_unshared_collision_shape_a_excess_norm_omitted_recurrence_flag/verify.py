#!/usr/bin/env python3
"""Replay the shape-A omitted-recurrence degree-drop flag."""

import argparse


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def poly_mul(left, right, prime):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return out


def locator(points, prime):
    out = [1]
    for point in points:
        out = poly_mul(out, [-point % prime, 1], prime)
    return out


def quotient_by_linear(poly, point, prime):
    # Coefficients are low to high; synthetic division returns L/(X-point).
    degree = len(poly) - 1
    out = [0] * degree
    carry = poly[-1]
    out[-1] = carry
    for index in range(degree - 1, 0, -1):
        carry = (poly[index] + point * carry) % prime
        out[index - 1] = carry
    require((poly[0] + point * carry) % prime == 0, "synthetic remainder")
    return out


def inverse(value, prime):
    return pow(value, prime - 2, prime)


def replay(mutation=None):
    mutation = mutation or {}
    e = mutation.get("e", (2**39 + 1) // 3)
    p_official = mutation.get("p_official", (3 * e - 1) // 2)
    d_official = mutation.get("d_official", 2 * p_official - 1)
    n_official = mutation.get("n_official", p_official - 3)
    rows_official = mutation.get("rows_official", 3 * p_official - 2)

    require(e == 183251937963, "official e")
    require(p_official == 274877906944, "official p")
    require(d_official == 549755813887, "official locator degree")
    require(n_official == 274877906941, "official biform row degree")
    require(rows_official - d_official - 2 == n_official, "index weld")

    # Small exact interpolation fixture with R-d-2=n.
    prime = 101
    points = list(range(1, 9))
    R = len(points)
    d = 3
    n = R - d - 2
    L = locator(points, prime)
    derivatives = []
    quotients = []
    for point in points:
        quotient = quotient_by_linear(L, point, prime)
        quotients.append(quotient)
        value = sum(coef * pow(point, i, prime) for i, coef in enumerate(quotient))
        derivatives.append(value % prime)
        require(value % prime != 0, "distinct interpolation points")

    # Coefficients are polynomials in a symbolic parameter evaluated at the
    # three test slopes. Their top-degree drops are 2, 1, and 0.
    slopes = [10, 11, 12]
    expected_drops = [2, 1, 0]
    for slope, expected_drop in zip(slopes, expected_drops):
        top = (slope - 10) * (slope - 11) % prime
        middle = (slope - 10) % prime
        G = [7, 5, middle, top]  # degree n=3, low to high
        while len(G) > 1 and G[-1] == 0:
            G.pop()
        drop = n - (len(G) - 1)
        require(drop == expected_drop, "fixture degree drop")

        H = []
        for point, derivative in zip(points, derivatives):
            value = sum(coef * pow(point, i, prime) for i, coef in enumerate(G))
            H.append(value * inverse(derivative, prime) % prime)
        moments = [
            sum(weight * pow(point, j, prime) for weight, point in zip(H, points))
            % prime
            for j in range(d + 1 + n)
        ]
        require(all(value == 0 for value in moments[: d + 1]), "forced moments")
        initial_zeros = 0
        for value in moments[d + 1 :]:
            if value != 0:
                break
            initial_zeros += 1
        require(initial_zeros == drop, "omitted-moment zero run")

    layer_cake = sum(1 for q in expected_drops for level in range(1, n + 1) if q >= level)
    require(layer_cake == sum(expected_drops) == 3, "nested gcd layer cake")
    return d_official, n_official, layer_cake


def tamper_selftest():
    mutations = [
        {"e": (2**39 + 1) // 3 + 1},
        {"p_official": 274877906943},
        {"d_official": 549755813886},
        {"n_official": 274877906940},
        {"rows_official": 824633720829},
    ]
    rejected = 0
    for mutation in mutations:
        try:
            replay(mutation)
        except AssertionError:
            rejected += 1
    require(rejected == len(mutations), "hostile mutation rejection")
    return rejected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()

    d, n, layer_cake = replay()
    suffix = ""
    if args.tamper_selftest:
        suffix = f" mutations={tamper_selftest()}/5"
    print(
        "RATE_HALF_SHAPE_A_OMITTED_RECURRENCE_FLAG_PASS "
        f"d={d} n={n} fixture_layer_cake={layer_cake}{suffix}"
    )


if __name__ == "__main__":
    main()
