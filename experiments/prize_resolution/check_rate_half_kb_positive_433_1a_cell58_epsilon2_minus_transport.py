#!/usr/bin/env python3
"""Check the exact cell-5/8 and first-root-sign transports."""

import itertools

import sympy as sp


ROLES = ("LC", "AB+1", "AB+2", "AB-", "AC")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def matrix_equal(left, right):
    return all(sp.expand(value) == 0 for value in (left - right))


def pairings(values):
    values = tuple(values)
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        yield ((first, second), (rest[0], rest[1]))


def cells():
    output = []
    for singleton in range(5):
        rest = tuple(index for index in range(5) if index != singleton)
        for matching in pairings(rest):
            output.append((singleton, matching))
    return tuple(output)


def common_records(cell, epsilon_1, epsilon_2, r, t):
    iota, b, c = sp.symbols("iota b c", nonzero=True)
    singleton, matching = cells()[cell]
    roots = [None] * 5
    roots[matching[0][0]] = sp.Integer(1)
    roots[matching[0][1]] = epsilon_1 * iota
    roots[matching[1][0]] = r
    roots[matching[1][1]] = epsilon_2 * iota * r
    roots[singleton] = t
    products = (-c**2, b, b, -b, c)
    sums = (0, 1 + b, 1 + b, 1 - b, 1 + c)
    return {
        role: {
            "root": sp.expand(roots[index]),
            "label": sp.expand(roots[index] ** 2),
            "product": products[index],
            "sum": sums[index],
            "q": sp.expand(roots[index] * sums[index]),
        }
        for index, role in enumerate(ROLES)
    }


def duplicate_role_transport(records):
    swap = {"AB+1": "AB+2", "AB+2": "AB+1"}
    return {swap.get(role, role): record for role, record in records.items()}


def product_row(record):
    label = record["label"]
    product = record["product"]
    return sp.Matrix([[
        -product, -product * label, -product * label**2,
        1, label, label**2, 0, 0,
    ]])


def sum_row(record):
    label = record["label"]
    q_value = record["q"]
    return sp.Matrix([[
        q_value, q_value * label, q_value * label**2,
        0, 0, 0, label, label**2,
    ]])


def check_duplicate_transport(epsilon_1, epsilon_2):
    r, t = sp.symbols("r t", nonzero=True)
    cell8 = duplicate_role_transport(
        common_records(8, epsilon_1, epsilon_2, r, t)
    )
    cell5 = common_records(5, epsilon_1, epsilon_2, r, t)
    require(cell8 == cell5, "duplicate AB+ transport 8 -> 5")


def check_first_sign_transport(cell, epsilon_1, epsilon_2):
    require(cell in (5, 8), "transport only covers cells 5 and 8")
    require(epsilon_1 in (-1, 1), "epsilon_1")
    require(epsilon_2 == -1, "epsilon_2=-1 is essential")
    r, t = sp.symbols("r t", nonzero=True)

    source = common_records(cell, epsilon_1, epsilon_2, r, t)
    if epsilon_1 == -1:
        base = common_records(cell, -1, -1, r, t)
        q_scale = 1
    else:
        base = common_records(cell, -1, -1, -r, -t)
        q_scale = -1

    for role in ROLES:
        for key in ("label", "product", "sum"):
            require(
                sp.expand(base[role][key] - source[role][key]) == 0,
                f"{role} {key}",
            )
        if role == "LC":
            require(base[role]["q"] == source[role]["q"] == 0, "loop q")
        else:
            require(
                sp.expand(base[role]["q"] - q_scale * source[role]["q"])
                == 0,
                f"{role} q scale",
            )

    beta_involution = sp.diag(1, 1, 1, 1, 1, 1, -1, -1)
    column_involution = (
        sp.eye(8) if q_scale == 1 else beta_involution
    )
    for role in ROLES:
        require(
            matrix_equal(
                product_row(base[role]) * column_involution,
                product_row(source[role]),
            ),
            f"{role} product matrix",
        )
        expected_scale = 1 if q_scale == 1 else -1
        require(
            matrix_equal(
                sum_row(base[role]) * column_involution,
                expected_scale * sum_row(source[role]),
            ),
            f"{role} full sum matrix",
        )

    source_labels = [source[role]["label"] for role in ROLES]
    base_labels = [base[role]["label"] for role in ROLES]
    for left, right in itertools.combinations(range(5), 2):
        require(
            sp.expand(
                (source_labels[left] - source_labels[right])
                - (base_labels[left] - base_labels[right])
            )
            == 0,
            "source guard",
        )

    z, product, edge_sum = sp.symbols("z product edge_sum")
    outside_source = {
        "label": z**2,
        "product": product,
        "q": z * edge_sum,
    }
    outside_base = {
        "label": (-z) ** 2,
        "product": product,
        "q": (-z) * edge_sum,
    }
    require(
        matrix_equal(
            product_row(outside_base) * beta_involution,
            product_row(outside_source),
        ),
        "outside product matrix",
    )
    require(
        matrix_equal(
            sum_row(outside_base) * beta_involution,
            -sum_row(outside_source),
        ),
        "outside full sum matrix",
    )
    return q_scale


def main():
    require(len(cells()) == 15, "matching cell count")
    require(
        cells()[5] == (1, ((0, 4), (2, 3))),
        "cell 5 role shape",
    )
    require(
        cells()[8] == (2, ((0, 4), (1, 3))),
        "cell 8 role shape",
    )
    rows = []
    for epsilon_1 in (-1, 1):
        check_duplicate_transport(epsilon_1, -1)
        for cell in (5, 8):
            rows.append((cell, epsilon_1, -1,
                         check_first_sign_transport(cell, epsilon_1, -1)))
    require(len(rows) == 4, "transport orbit size")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL58_EPSILON2_MINUS_TRANSPORT_PASS "
        "rows=4 cells=5,8 epsilon1=-1,+1 epsilon2=-1"
    )


if __name__ == "__main__":
    main()
