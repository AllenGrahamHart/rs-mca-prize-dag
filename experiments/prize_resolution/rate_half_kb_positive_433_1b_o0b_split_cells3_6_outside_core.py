#!/usr/bin/env python3
"""Pure symbolic compiler for O0b split cells-3/6 outside ideals."""

import functools


PRIME = 2130706433
IOTA = 16711679

# Target coordinates are indexed as (b,c,d,e,f). A sign of zero means the
# lane's free outside EF sign.
EDGE_SPECS = {
    "S0": (
        (0, 3, 1), (1, 4, 1),
        (2, 3, 1), (2, 3, -1),
        (2, 4, 1), (2, 4, -1),
        (3, 4, 0),
    ),
    "SDE": (
        (0, 3, 1), (1, 4, 1),
        (2, 3, 1), (2, 3, 1),
        (2, 4, 1), (2, 4, -1),
        (3, 4, 0),
    ),
    "SDF": (
        (0, 3, 1), (1, 4, 1),
        (2, 3, 1), (2, 3, -1),
        (2, 4, 1), (2, 4, 1),
        (3, 4, 0),
    ),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, values[index]),) + tail


def verify_edge_table(edge_table=EDGE_SPECS):
    expected = {
        "S0": (
            (0, 3, 1), (1, 4, 1), (2, 3, 1), (2, 3, -1),
            (2, 4, 1), (2, 4, -1), (3, 4, 0),
        ),
        "SDE": (
            (0, 3, 1), (1, 4, 1), (2, 3, 1), (2, 3, 1),
            (2, 4, 1), (2, 4, -1), (3, 4, 0),
        ),
        "SDF": (
            (0, 3, 1), (1, 4, 1), (2, 3, 1), (2, 3, -1),
            (2, 4, 1), (2, 4, 1), (3, 4, 0),
        ),
    }
    require(edge_table == expected, "O0b signed-edge table")
    require(len(tuple(pairings(range(6)))) == 15, "matching census")
    return 3, 21, 15


def compile_case(case, product_payload, kernel_payload, sp):
    """Return exact polynomial equations, guards, and rank-five cofactors."""
    cell, lane, sigma_o, epsilon_1, epsilon_2, xi_index, pairing_index = case
    require(cell == 3, "canonical cells-3/6 representative")
    require(lane in EDGE_SPECS and sigma_o in (-1, 1), "lane/sign domain")
    require(epsilon_1 in (-1, 1) and epsilon_2 in (-1, 1), "source signs")
    require(0 <= xi_index < 7 and 0 <= pairing_index < 15, "outside label")

    t, r, c, b, d, e, f = sp.symbols("t r c b d e f")
    variables = (t, r, c, b, d, e, f)
    common_variables = (t, r, c, b)
    roots = (1, t, epsilon_1 * IOTA, r, epsilon_2 * IOTA * r)
    labels = tuple(sp.expand(root * root) for root in roots)
    products = (-1, b, c, b * c, -b * c)
    sums = (0, 1 + b, 1 + c, b + c, b - c)
    q_values = tuple(
        sp.expand(root * edge_sum) for root, edge_sum in zip(roots, sums)
    )

    product_row = next(
        row for row in product_payload["rows"] if row["cell"] == 3
    )
    raw_cofactors = tuple(
        sp.Poly(sp.sympify(value), *common_variables, modulus=PRIME)
        for value in product_row["kernel_cofactor_expressions"]
    )
    common_gcd = functools.reduce(sp.gcd, raw_cofactors)
    cofactors = []
    for value in raw_cofactors:
        quotient, remainder = sp.div(value, common_gcd)
        require(remainder.is_zero, "product-kernel gcd division")
        cofactors.append(quotient.as_expr())

    product_rows = [
        [-product, -product * label, -product * label**2,
         1, label, label**2, 0]
        for label, product in zip(labels, products)
    ]
    sum_rows = [
        [q_value, q_value * label, q_value * label**2,
         0, 0, 0, -label * (1 - label)]
        for label, q_value in zip(labels, q_values)
    ]
    base_rows = [*product_rows, sum_rows[1]]
    common_equations = [
        sp.expand(
            sp.Matrix([*base_rows, sum_rows[index]]).det(method="domain-ge")
        )
        for index in (2, 3, 4)
    ]
    route_guards = [
        b, c, r, t,
        b - 1, b + 1, c - 1, c + 1, b - c, b + c,
        r * r - 1, r * r + 1, t * t - 1, t * t + 1,
        t * t - r * r, t * t + r * r,
    ]

    def strip_factors(expression):
        value = sp.Poly(expression, *common_variables, modulus=PRIME)
        for factor in route_guards:
            divisor = sp.Poly(factor, *common_variables, modulus=PRIME)
            while True:
                quotient, remainder = sp.div(value, divisor)
                if not remainder.is_zero:
                    break
                value = quotient
        return value.monic().as_expr()

    common_equations = [strip_factors(value) for value in common_equations]
    kernel_row = next(
        row for row in kernel_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
    )
    require(kernel_row["status"] == "COMPLETE", "kernel-row custody")
    kernel = tuple(sp.sympify(value["expression"]) for value in kernel_row["kernel"])
    require(len(kernel) == 8, "coefficient-kernel width")
    a2 = kernel[:3]
    a0 = kernel[3:6]
    beta = kernel[6:]

    def evaluate(coefficients, value):
        return sp.expand(sum(
            coefficient * value**index
            for index, coefficient in enumerate(coefficients)
        ))

    def edge(left, right, sign):
        return sign * left * right, (left + sign * right) ** 2

    target_outside = (b, c, d, e, f)
    signed_edges = tuple(
        edge(
            target_outside[left],
            target_outside[right],
            sigma_o if sign == 0 else sign,
        )
        for left, right, sign in EDGE_SPECS[lane]
    )
    records = tuple(row[0] for row in signed_edges)
    squared_sums = tuple(row[1] for row in signed_edges)
    missing_label = -t * t
    a2_missing = evaluate(a2, missing_label)
    a0_missing = evaluate(a0, missing_label)
    beta_missing = evaluate(beta, missing_label)

    y, z = sp.symbols("y z")
    p0, p1, p2 = (a0[index] - y * a2[index] for index in range(3))
    q0 = a0[0] - z * a2[0]
    q1 = -a0[1] + z * a2[1]
    q2 = a0[2] - z * a2[2]
    paired = sp.expand(
        (p2 * q0 - p0 * q2) ** 2
        - (p2 * q1 - p1 * q2) * (p1 * q0 - p0 * q1)
    )
    residual = tuple(index for index in range(7) if index != xi_index)
    matching = tuple(pairings(range(6)))[pairing_index]
    outside_equations = [records[xi_index] * a2_missing - a0_missing]
    outside_equations.extend(
        paired.subs({y: records[residual[left]], z: records[residual[right]]})
        for left, right in matching
    )
    outside_equations.append(
        missing_label * beta_missing**2
        - squared_sums[xi_index] * a2_missing**2
    )

    target_values = (sp.Integer(1), b, c, d, e, f)
    guards = [*route_guards]
    guards.extend(target_values[1:])
    guards.extend(
        target_values[left] ** 2 - target_values[right] ** 2
        for left in range(6) for right in range(left + 1, 6)
    )
    common_labels = (t * t, 1, -1, r * r, -r * r)
    guards.extend(evaluate(a2, label) for label in common_labels)
    guards.append(a2_missing)

    normalized_guards = []
    seen = set()
    for expression in guards:
        polynomial = sp.Poly(expression, *variables, modulus=PRIME)
        if polynomial.total_degree() == 0:
            continue
        normalized = polynomial.monic().as_expr()
        key = str(normalized)
        if key not in seen:
            seen.add(key)
            normalized_guards.append(normalized)

    rank_cofactors = []
    seen = set()
    for expression in product_row["stripped_expressions"]:
        polynomial = sp.Poly(sp.sympify(expression), *variables, modulus=PRIME)
        if polynomial.is_zero:
            continue
        normalized = polynomial.monic().as_expr()
        key = str(normalized)
        if key not in seen:
            seen.add(key)
            rank_cofactors.append(normalized)
    require(len(rank_cofactors) == 6, "six product-rank charts")
    return {
        "variables": variables,
        "equations": tuple(common_equations + outside_equations),
        "guards": tuple(normalized_guards),
        "rank_cofactors": tuple(rank_cofactors),
        "common_equation_count": len(common_equations),
        "outside_equation_count": len(outside_equations),
    }


def singular(expression, variables, sp):
    return str(
        sp.Poly(expression, *variables, modulus=PRIME).as_expr()
    ).replace("**", "^")


if __name__ == "__main__":
    lanes, records, matchings = verify_edge_table()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_OUTSIDE_CORE_PASS "
        f"lanes={lanes} signed_records={records} matchings={matchings}"
    )
