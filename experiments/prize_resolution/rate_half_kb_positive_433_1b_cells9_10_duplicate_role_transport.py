#!/usr/bin/env python3
"""Verify exact B/C duplicate-role transport from cell 9 to cell 10."""

import itertools

import sympy as sp


ROLES = ("LA", "AB", "AC", "BC+", "BC-")
OUTSIDE_PERMUTATION = (0, 1, 2, 3, 4, 6, 5)


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
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, second),) + tail


def common_cell9(b, c, r, t, iota, epsilon_1, epsilon_2):
    roots = (1, epsilon_1*iota, r, t, epsilon_2*iota*r)
    products = (-1, b, c, b*c, -b*c)
    sums = (0, 1+b, 1+c, b+c, b-c)
    return {
        role: (sp.expand(product), sp.expand(root*edge_sum), sp.expand(root**2))
        for role, root, product, edge_sum in zip(ROLES, roots, products, sums)
    }


def common_cell10(b, c, r, t, iota, epsilon_1, epsilon_2):
    roots = (1, r, epsilon_1*iota, t, epsilon_2*iota*r)
    products = (-1, b, c, b*c, -b*c)
    sums = (0, 1+b, 1+c, b+c, b-c)
    return {
        role: (sp.expand(product), sp.expand(root*edge_sum), sp.expand(root**2))
        for role, root, product, edge_sum in zip(ROLES, roots, products, sums)
    }


def outside(b, c, d, e, f, sigma_c, sigma_o):
    products = (
        d*e, d*e, -d*e, d*f, sigma_o*e*f, b*f, sigma_c*c*f,
    )
    sums = (
        (d+e)**2, (d+e)**2, (d-e)**2, (d+f)**2,
        (e+sigma_o*f)**2, (b+f)**2, (c+sigma_c*f)**2,
    )
    return tuple(map(sp.expand, products)), tuple(map(sp.expand, sums))


def normalized(expression, variables):
    return sp.Poly(expression, *variables).monic().as_expr()


def target_guards(coordinates, variables):
    guards = list(coordinates)
    for left, right in itertools.combinations(coordinates, 2):
        guards.extend((left-right, left+right))
    return {normalized(value, variables) for value in guards
            if sp.Poly(value, *variables).total_degree() > 0}


def canonical(matching):
    return tuple(sorted(tuple(sorted(edge)) for edge in matching))


def main():
    b, c, d, e, f, r, t, iota = sp.symbols("b c d e f r t iota")
    role_map = {"LA": "LA", "AB": "AC", "AC": "AB",
                "BC+": "BC+", "BC-": "BC-"}
    common_checks = 0
    outside_checks = 0
    matching_checks = 0
    matching_rows = tuple(pairings(range(6)))
    matching_index = {canonical(row): index
                      for index, row in enumerate(matching_rows)}
    for epsilon_1, epsilon_2 in itertools.product((-1, 1), repeat=2):
        left = common_cell9(b, c, r, t, iota, epsilon_1, epsilon_2)
        right = common_cell10(c, b, r, t, iota, epsilon_1, -epsilon_2)
        for new_role, old_role in role_map.items():
            require(all(sp.expand(a-b_value) == 0
                        for a, b_value in zip(right[new_role], left[old_role])),
                    "common role transport")
            common_checks += 1

    coordinates = (sp.Integer(1), b, c, d, e, f)
    variables = (b, c, d, e, f)
    for sigma_c, sigma_o in itertools.product((-1, 1), repeat=2):
        left_products, left_sums = outside(b, c, d, e, f, sigma_c, sigma_o)
        right_products, right_sums = outside(
            c, b, sigma_c*d, sigma_c*e, sigma_c*f, sigma_c, sigma_o
        )
        require(all(sp.expand(right_products[OUTSIDE_PERMUTATION[index]]
                              - left_products[index]) == 0
                    for index in range(7)), "outside product transport")
        require(all(sp.expand(right_sums[OUTSIDE_PERMUTATION[index]]
                              - left_sums[index]) == 0
                    for index in range(7)), "outside sum transport")
        transformed = (sp.Integer(1), c, b, sigma_c*d, sigma_c*e, sigma_c*f)
        require(target_guards(coordinates, variables) ==
                target_guards(transformed, variables),
                "target guard transport")
        outside_checks += 1

        for xi_index in range(7):
            old_residual = tuple(index for index in range(7)
                                 if index != xi_index)
            new_xi = OUTSIDE_PERMUTATION[xi_index]
            new_residual = tuple(index for index in range(7)
                                 if index != new_xi)
            compact = {value: index for index, value in enumerate(new_residual)}
            images = set()
            for matching in matching_rows:
                image = canonical(tuple(
                    (compact[OUTSIDE_PERMUTATION[old_residual[left]]],
                     compact[OUTSIDE_PERMUTATION[old_residual[right]]])
                    for left, right in matching
                ))
                images.add(matching_index[image])
            require(images == set(range(15)), "matching bijection")
            matching_checks += 15

    require(common_checks == 20 and outside_checks == 4
            and matching_checks == 420, "transport totals")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_CELLS9_10_TRANSPORT_PASS "
        "common_rows=20 target_lanes=4 labels=420 systems=1680"
    )


if __name__ == "__main__":
    main()
