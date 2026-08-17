#!/usr/bin/env python3
"""Independent finite-field matrix audit and hostile controls."""

import importlib.util
import itertools
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (ROOT / "experiments/prize_resolution" /
          "rate_half_kb_positive_433_1b_o0b_split_bc_ef_involution.py")
PRIME = 2130706433
IOTA = 16711679
ROLE_PERMUTATION = (0, 2, 1, 3, 4)
FULL_PERMUTATION = (0, 2, 1, 3, 4, 6, 5, 9, 10, 7, 8, 11)
SUM_FACTORS = (1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1)
LANE_ACTION = {"S0": "S0", "SDE": "SDF", "SDF": "SDE"}


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


def cells():
    output = []
    for singleton in range(5):
        rest = tuple(index for index in range(5) if index != singleton)
        output.extend((singleton, matching) for matching in pairings(rest))
    return tuple(output)


def roots(cell, epsilon_1, epsilon_2, r, t):
    singleton, matching = cells()[cell]
    output = [None] * 5
    output[matching[0][0]] = 1
    output[matching[0][1]] = epsilon_1 * IOTA
    output[matching[1][0]] = r
    output[matching[1][1]] = epsilon_2 * IOTA * r
    output[singleton] = t
    return tuple(value % PRIME for value in output)


def action(cell, epsilon_1, epsilon_2, r, t):
    inverse_r = pow(r, PRIME - 2, PRIME)
    if cell == 0:
        scale = -epsilon_1 * IOTA
        return 0, -epsilon_1, -epsilon_2, scale, scale*r, scale*t
    if cell == 1:
        return 2, -epsilon_2, epsilon_1, inverse_r, inverse_r, t*inverse_r
    if cell == 2:
        return 1, epsilon_2, -epsilon_1, inverse_r, inverse_r, t*inverse_r
    if cell in (3, 4):
        return cell + 3, epsilon_1, -epsilon_2, 1, r, t
    if cell in (6, 7):
        return cell - 3, epsilon_1, -epsilon_2, 1, r, t
    if cell == 5:
        return 8, -epsilon_1, epsilon_2, 1, r, t
    if cell == 8:
        return 5, -epsilon_1, epsilon_2, 1, r, t
    if cell == 9:
        return 10, epsilon_1, -epsilon_2, 1, r, t
    if cell == 10:
        return 9, epsilon_1, -epsilon_2, 1, r, t
    if cell == 11:
        return 11, -epsilon_1, -epsilon_2, 1, epsilon_2*IOTA*r, t
    if cell == 12:
        return 13, epsilon_1, epsilon_2, 1, r, -t
    if cell == 13:
        return 12, epsilon_1, epsilon_2, 1, r, -t
    if cell == 14:
        return 14, epsilon_1, -epsilon_2, 1, epsilon_2*IOTA*r, -t
    raise RuntimeError("cell")


def edge(left, right, sign):
    return sign*left*right % PRIME, pow(left + sign*right, 2, PRIME)


def edge_pair(left, right, repeated):
    if repeated:
        row = edge(left, right, 1)
        return row, row
    return edge(left, right, 1), edge(left, right, -1)


def records(lane, sigma_o, values):
    a, b, c, d, e, f = values
    return (
        (-a*a % PRIME, 0),
        (a*b % PRIME, (a+b) % PRIME),
        (a*c % PRIME, (a+c) % PRIME),
        (b*c % PRIME, (b+c) % PRIME),
        (-b*c % PRIME, (b-c) % PRIME),
        edge(b, e, 1),
        edge(c, f, 1),
        *edge_pair(d, e, lane == "SDE"),
        *edge_pair(d, f, lane == "SDF"),
        edge(e, f, sigma_o),
    )


def product_row(product, label):
    return tuple(value % PRIME for value in (
        -product, -product*label, -product*label*label,
        1, label, label*label, 0, 0,
    ))


def sum_row(q_value, label):
    return tuple(value % PRIME for value in (
        q_value, q_value*label, q_value*label*label,
        0, 0, 0, label, label*label,
    ))


def scaled_row(row, columns, row_scale=1):
    return tuple(row_scale*value*column % PRIME
                 for value, column in zip(row, columns))


def direct_matrix_audit():
    require(IOTA*IOTA % PRIME == PRIME - 1, "deployed iota")
    target_values = (1, 2, 3, 5, 7, 11)
    transformed_values = (1, 3, 2, 5, 11, 7)
    r, t = 13, 17
    outside_roots = (19, 23, 29, 31, 37, 41, 43)
    checked = 0
    for lane, sigma_o, cell, epsilon_1, epsilon_2 in itertools.product(
            ("S0", "SDE", "SDF"), (-1, 1), range(15), (-1, 1), (-1, 1)):
        old_common = roots(cell, epsilon_1, epsilon_2, r, t)
        new_cell, new_epsilon_1, new_epsilon_2, scale, new_r, new_t = action(
            cell, epsilon_1, epsilon_2, r, t
        )
        scale %= PRIME
        new_common = roots(
            new_cell, new_epsilon_1, new_epsilon_2, new_r % PRIME, new_t % PRIME
        )
        old_roots = old_common + outside_roots
        new_roots = [None] * 12
        for old_index, new_index in enumerate(FULL_PERMUTATION):
            new_roots[new_index] = scale * SUM_FACTORS[old_index] * old_roots[old_index] % PRIME
        require(tuple(new_roots[:5]) == new_common, "independent common-root action")

        old_records = records(lane, sigma_o, target_values)
        new_records = records(LANE_ACTION[lane], sigma_o, transformed_values)
        mu = scale*scale % PRIME
        columns = (1, mu, mu*mu % PRIME, 1, mu, mu*mu % PRIME,
                   mu*pow(scale, PRIME - 2, PRIME) % PRIME,
                   mu*mu*pow(scale, PRIME - 2, PRIME) % PRIME)
        require(all(columns), "invertible matrix covariance")
        for old_index, new_index in enumerate(FULL_PERMUTATION):
            old_product, old_sum = old_records[old_index]
            new_product, new_sum = new_records[new_index]
            require(new_product == old_product, "independent target product")
            require(new_sum == SUM_FACTORS[old_index]*old_sum % PRIME,
                    "independent target sum")
            old_label = old_roots[old_index]**2 % PRIME
            new_label = new_roots[new_index]**2 % PRIME
            require(scaled_row(product_row(old_product, old_label), columns) ==
                    product_row(new_product, new_label), "product matrix covariance")
            old_q = old_roots[old_index]*old_sum % PRIME
            new_q = new_roots[new_index]*new_sum % PRIME
            require(scaled_row(sum_row(old_q, old_label), columns, scale) ==
                    sum_row(new_q, new_label), "sum matrix covariance")
            checked += 1
    require(checked == 360*12, "matrix audit census")
    return checked


def reject(module, permutation, factor, label):
    try:
        module.verify(permutation, factor)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def main():
    checked = direct_matrix_audit()
    spec = importlib.util.spec_from_file_location("split_involution", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    reject(module, (0, 1, 2, 3, 4, 5, 6), -1, "outside action")
    reject(module, module.OUTSIDE_PERMUTATION, 1, "BC-minus sign")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_BC_EF_QUOTIENT_AUDIT_PASS "
        f"matrix_rows={checked} mutations=2/2"
    )


if __name__ == "__main__":
    main()
