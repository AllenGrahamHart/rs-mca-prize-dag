#!/usr/bin/env python3
"""Replay the two-branch tangent-profile product rule."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def multiply(left, right, prime):
    product = {}
    for (z_left, y_left), left_value in left.items():
        for (z_right, y_right), right_value in right.items():
            z_degree = z_left + z_right
            y_degree = y_left + y_right
            if z_degree > 2 or y_degree > 2:
                continue
            key = (z_degree, y_degree)
            product[key] = (
                product.get(key, 0) + left_value * right_value
            ) % prime
    return product


def derivative_y(polynomial, prime):
    derivative = {}
    for (z_degree, y_degree), value in polynomial.items():
        if y_degree:
            derivative[(z_degree, y_degree - 1)] = (
                y_degree * value
            ) % prime
    return derivative


shape_orders = {
    "A": (2,),
    "B": (1, 1),
    "C": (2,),
    "D": (1, 1),
}
require(
    tuple(name for name, orders in shape_orders.items() if orders == (1, 1))
    == ("B", "D"),
    "two-branch shape ledger",
)

checks = 1
for prime in (101, 127):
    for a_1 in range(1, 6):
        for a_2 in range(1, 6):
            for v_1 in range(6):
                for v_2 in range(6):
                    u_0 = (2 * a_1 + 3 * a_2 + 1) % prime
                    require(u_0 != 0, "unit fixture")
                    f_1 = {
                        (1, 0): a_1,
                        (0, 1): v_1,
                        (2, 0): 7,
                        (1, 1): 11,
                        (0, 2): 13,
                    }
                    f_2 = {
                        (1, 0): a_2,
                        (0, 1): v_2,
                        (2, 0): 17,
                        (1, 1): 19,
                        (0, 2): 23,
                    }
                    unit = {(0, 0): u_0, (1, 0): 29, (0, 1): 31}
                    product = multiply(multiply(unit, f_1, prime), f_2, prime)
                    g_x = derivative_y(product, prime)
                    expected = u_0 * (a_1 * v_2 + a_2 * v_1) % prime
                    require(g_x.get((0, 0), 0) == 0, "profile-four exclusion")
                    require(g_x.get((1, 0), 0) == expected, "tangent sum")
                    require(
                        (expected == 0)
                        == ((v_1 * a_2 + v_2 * a_1) % prime == 0),
                        "profile router",
                    )
                    checks += 4

print(f"RATE_HALF_COLLISION_TWO_BRANCH_TANGENT_PASS checks={checks}")
