#!/usr/bin/env python3
"""Exact B/C--E/F involution on the O0b split-principal ledger."""

import itertools


ROLES = ("LA", "AB", "AC", "BC+", "BC-")
LANES = tuple(itertools.product(("S0", "SDE", "SDF"), (-1, 1)))
SOURCE_SIGNS = tuple(itertools.product((-1, 1), repeat=2))
ROLE_PERMUTATION = (0, 2, 1, 3, 4)
OUTSIDE_PERMUTATION = (1, 0, 4, 5, 2, 3, 6)
FULL_PERMUTATION = (0, 2, 1, 3, 4, 6, 5, 9, 10, 7, 8, 11)
SUM_FACTORS = (1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


# Laurent monomials coefficient*i^i*r^r*t^t with i^2=-1.
def monomial(coefficient=1, i_power=0, r_power=0, t_power=0):
    quotient, remainder = divmod(i_power, 2)
    if quotient % 2:
        coefficient = -coefficient
    return coefficient, remainder, r_power, t_power


ONE = monomial()
IOTA = monomial(i_power=1)
R = monomial(r_power=1)
T = monomial(t_power=1)


def mmul(left, right):
    return monomial(
        left[0] * right[0],
        left[1] + right[1],
        left[2] + right[2],
        left[3] + right[3],
    )


def mscale(value, scalar):
    return monomial(scalar * value[0], value[1], value[2], value[3])


def minverse(value):
    require(value[0] in (-1, 1), "unit monomial")
    return monomial(value[0], -value[1], -value[2], -value[3])


def mpower(value, exponent):
    if exponent < 0:
        return mpower(minverse(value), -exponent)
    output = ONE
    for _ in range(exponent):
        output = mmul(output, value)
    return output


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


def canonical_matching(matching):
    return tuple(sorted(tuple(sorted(pair)) for pair in matching))


def role_cells():
    output = []
    for singleton in range(5):
        rest = tuple(index for index in range(5) if index != singleton)
        output.extend((singleton, matching) for matching in pairings(rest))
    return tuple(output)


def canonical_cell(cell):
    return cell[0], canonical_matching(cell[1])


def permute_cell(cell, permutation=ROLE_PERMUTATION):
    singleton, matching = cell
    return canonical_cell((
        permutation[singleton],
        tuple((permutation[left], permutation[right]) for left, right in matching),
    ))


def source_roots(cell_index, epsilon_1, epsilon_2, r_value=R, t_value=T):
    singleton, matching = role_cells()[cell_index]
    roots = [None] * 5
    roots[matching[0][0]] = ONE
    roots[matching[0][1]] = mscale(IOTA, epsilon_1)
    roots[matching[1][0]] = r_value
    roots[matching[1][1]] = mscale(mmul(IOTA, r_value), epsilon_2)
    roots[singleton] = t_value
    require(all(value is not None for value in roots), "source root cover")
    return tuple(roots)


def source_action(cell, epsilon_1, epsilon_2):
    """Return destination cell/signs, global root scale, and new r,t."""
    if cell == 0:
        scale = mscale(IOTA, -epsilon_1)
        return 0, -epsilon_1, -epsilon_2, scale, mmul(scale, R), mmul(scale, T)
    if cell == 1:
        scale = minverse(R)
        return 2, -epsilon_2, epsilon_1, scale, scale, mmul(T, scale)
    if cell == 2:
        scale = minverse(R)
        return 1, epsilon_2, -epsilon_1, scale, scale, mmul(T, scale)
    if cell in (3, 4):
        return cell + 3, epsilon_1, -epsilon_2, ONE, R, T
    if cell in (6, 7):
        return cell - 3, epsilon_1, -epsilon_2, ONE, R, T
    if cell == 5:
        return 8, -epsilon_1, epsilon_2, ONE, R, T
    if cell == 8:
        return 5, -epsilon_1, epsilon_2, ONE, R, T
    if cell == 9:
        return 10, epsilon_1, -epsilon_2, ONE, R, T
    if cell == 10:
        return 9, epsilon_1, -epsilon_2, ONE, R, T
    if cell == 11:
        return 11, -epsilon_1, -epsilon_2, ONE, mscale(mmul(IOTA, R), epsilon_2), T
    if cell == 12:
        return 13, epsilon_1, epsilon_2, ONE, R, mscale(T, -1)
    if cell == 13:
        return 12, epsilon_1, epsilon_2, ONE, R, mscale(T, -1)
    if cell == 14:
        return 14, epsilon_1, -epsilon_2, ONE, mscale(mmul(IOTA, R), epsilon_2), mscale(T, -1)
    raise RuntimeError(f"unknown cell {cell}")


def substitute(value, r_value, t_value):
    coefficient, i_power, r_power, t_power = value
    output = monomial(coefficient, i_power)
    output = mmul(output, mpower(r_value, r_power))
    return mmul(output, mpower(t_value, t_power))


def verify_source_action():
    cells = role_cells()
    indexed = {canonical_cell(cell): index for index, cell in enumerate(cells)}
    expected_cell_action = (0, 2, 1, 6, 7, 8, 3, 4, 5, 10, 9, 11, 13, 12, 14)
    require(tuple(indexed[permute_cell(cell)] for cell in cells) == expected_cell_action,
            "fifteen-cell B/C action")

    state_rows = []
    scaling_profile = {"minus_one": 0, "r_inverse_square": 0, "identity": 0}
    for cell in range(15):
        for epsilon_1, epsilon_2 in SOURCE_SIGNS:
            roots = source_roots(cell, epsilon_1, epsilon_2)
            destination = source_action(cell, epsilon_1, epsilon_2)
            new_cell, new_epsilon_1, new_epsilon_2, scale, new_r, new_t = destination
            require(new_cell == expected_cell_action[cell], "source destination cell")
            new_roots = source_roots(
                new_cell, new_epsilon_1, new_epsilon_2, new_r, new_t
            )
            desired = tuple(
                mmul(scale, mscale(roots[old], SUM_FACTORS[old]))
                for old in (0, 2, 1, 3, 4)
            )
            require(new_roots == desired, f"common root action cell={cell}")

            image = source_action(new_cell, new_epsilon_1, new_epsilon_2)
            _, final_epsilon_1, final_epsilon_2, second_scale, second_r, second_t = image
            require(image[0] == cell and (final_epsilon_1, final_epsilon_2) ==
                    (epsilon_1, epsilon_2), "source state involution")
            require(mmul(scale, substitute(second_scale, new_r, new_t)) == ONE,
                    "global root scale involution")
            require(substitute(second_r, new_r, new_t) == R and
                    substitute(second_t, new_r, new_t) == T,
                    "source parameter involution")

            mu = mpower(scale, 2)
            if cell == 0:
                require(mu == monomial(-1), "cell-0 domain multiplier")
                scaling_profile["minus_one"] += 1
            elif cell in (1, 2):
                require(mu == monomial(r_power=-2), "cell-1/2 domain multiplier")
                scaling_profile["r_inverse_square"] += 1
            else:
                require(mu == ONE, "unit source multiplier")
                scaling_profile["identity"] += 1

            # Right-column scaling plus one row scaling gives exact covariance
            # of the eight-column product/sum incidence matrix.
            product_columns = (ONE, mu, mpower(mu, 2), ONE, mu, mpower(mu, 2))
            require(product_columns[:3] == product_columns[3:], "product row covariance")
            sum_tail_columns = (mmul(mu, minverse(scale)),
                                mmul(mpower(mu, 2), minverse(scale)))
            require(tuple(mmul(scale, value) for value in sum_tail_columns) ==
                    (mu, mpower(mu, 2)), "sum row covariance")
            state_rows.append((cell, epsilon_1, epsilon_2, new_cell,
                               new_epsilon_1, new_epsilon_2))
    require(len(state_rows) == 60, "common source-state census")
    return scaling_profile


# Sparse integer polynomials in target coordinates (a,b,c,d,e,f).
VARIABLE_COUNT = 6


def constant(value):
    return {} if value == 0 else {(0,) * VARIABLE_COUNT: value}


def variable(index):
    exponent = [0] * VARIABLE_COUNT
    exponent[index] = 1
    return {tuple(exponent): 1}


def padd(left, right):
    output = dict(left)
    for exponent, coefficient in right.items():
        output[exponent] = output.get(exponent, 0) + coefficient
        if output[exponent] == 0:
            del output[exponent]
    return output


def pscale(value, scalar):
    return {key: scalar * coefficient for key, coefficient in value.items()
            if scalar * coefficient}


def pmul(left, right):
    output = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = tuple(a + b for a, b in zip(left_exponent, right_exponent))
            output[exponent] = output.get(exponent, 0) + left_coefficient * right_coefficient
    return {key: value for key, value in output.items() if value}


def psquare(value):
    return pmul(value, value)


def edge_record(left, right, sign):
    return pscale(pmul(left, right), sign), psquare(padd(left, pscale(right, sign)))


def pair_records(left, right, repeated):
    if repeated:
        row = edge_record(left, right, 1)
        return row, row
    return edge_record(left, right, 1), edge_record(left, right, -1)


def target_records(lane, sigma_o, values):
    a, b, c, d, e, f = values
    common = (
        (pscale(psquare(a), -1), constant(0)),
        (pmul(a, b), padd(a, b)),
        (pmul(a, c), padd(a, c)),
        (pmul(b, c), padd(b, c)),
        (pscale(pmul(b, c), -1), padd(b, pscale(c, -1))),
    )
    outside = (
        edge_record(b, e, 1),
        edge_record(c, f, 1),
        *pair_records(d, e, lane == "SDE"),
        *pair_records(d, f, lane == "SDF"),
        edge_record(e, f, sigma_o),
    )
    return common + outside


def target_guards(values):
    guards = list(values)
    for left, right in itertools.combinations(values, 2):
        guards.extend((padd(left, right), padd(left, pscale(right, -1))))
    output = set()
    for row in guards:
        ordered = sorted(row.items())
        sign = 1 if ordered[0][1] > 0 else -1
        output.add(tuple((exponent, sign * coefficient)
                         for exponent, coefficient in ordered))
    return output


def lane_action(lane):
    return {"S0": "S0", "SDE": "SDF", "SDF": "SDE"}[lane]


def verify_target_action(outside_permutation=OUTSIDE_PERMUTATION,
                         bc_minus_factor=-1):
    require(tuple(FULL_PERMUTATION[5:]) == tuple(value + 5 for value in outside_permutation),
            "outside/full permutation agreement")
    values = tuple(variable(index) for index in range(VARIABLE_COUNT))
    transformed = (values[0], values[2], values[1], values[3], values[5], values[4])
    require(target_guards(values) == target_guards(transformed), "target guard action")
    sum_factors = tuple(
        bc_minus_factor if index == 4 else 1 for index in range(12)
    )
    for lane, sigma_o in LANES:
        old = target_records(lane, sigma_o, values)
        new = target_records(lane_action(lane), sigma_o, transformed)
        for old_index, new_index in enumerate(FULL_PERMUTATION):
            require(new[new_index][0] == old[old_index][0], "target product action")
            require(new[new_index][1] == pscale(old[old_index][1], sum_factors[old_index]),
                    "target sum action")
    return len(LANES)


def case_transport(xi, matching_index, matching_rows,
                   permutation=OUTSIDE_PERMUTATION):
    new_xi = permutation[xi]
    old_residual = tuple(index for index in range(7) if index != xi)
    new_residual = tuple(index for index in range(7) if index != new_xi)
    new_compact = {full: compact for compact, full in enumerate(new_residual)}
    old_matching = matching_rows[matching_index]
    new_matching = canonical_matching(tuple(
        (
            new_compact[permutation[old_residual[left]]],
            new_compact[permutation[old_residual[right]]],
        )
        for left, right in old_matching
    ))
    lookup = {canonical_matching(value): index for index, value in enumerate(matching_rows)}
    return new_xi, lookup[new_matching]


def state_action(state):
    lane, sigma_o, cell, epsilon_1, epsilon_2 = state
    source = source_action(cell, epsilon_1, epsilon_2)
    return lane_action(lane), sigma_o, source[0], source[1], source[2]


def verify_quotient(outside_permutation=OUTSIDE_PERMUTATION):
    matching_rows = tuple(pairings(range(6)))
    require(len(matching_rows) == 15, "outside matching census")
    label_cases = tuple(itertools.product(range(7), range(15)))
    case_images = {
        case_transport(xi, matching, matching_rows, outside_permutation)
        for xi, matching in label_cases
    }
    require(case_images == set(label_cases), "105-case bijection")

    states = tuple(
        (lane, sigma_o, cell, epsilon_1, epsilon_2)
        for lane, sigma_o in LANES
        for cell in range(15)
        for epsilon_1, epsilon_2 in SOURCE_SIGNS
    )
    state_set = set(states)
    require(len(states) == 360, "raw split state census")
    require({state_action(state) for state in states} == state_set, "state action bijection")
    require(all(state_action(state_action(state)) == state for state in states),
            "state action involution")
    require(all(state_action(state) != state for state in states),
            "state action fixed-point free")
    state_orbits = {min(state, state_action(state)) for state in states}
    require(len(state_orbits) == 180, "state quotient census")

    raw_cases = {
        (*state, xi, matching)
        for state in states
        for xi, matching in label_cases
    }

    def action(row):
        state = row[:5]
        xi, matching = case_transport(
            row[5], row[6], matching_rows, outside_permutation
        )
        return (*state_action(state), xi, matching)

    require(len(raw_cases) == 37800, "raw formal-row census")
    require({action(row) for row in raw_cases} == raw_cases, "formal-row bijection")
    require(all(action(action(row)) == row for row in raw_cases), "formal-row involution")
    formal_orbits = {min(row, action(row)) for row in raw_cases}
    require(len(formal_orbits) == 18900, "formal-row quotient census")
    return len(states), len(state_orbits), len(raw_cases), len(formal_orbits)


def verify(outside_permutation=OUTSIDE_PERMUTATION, bc_minus_factor=-1):
    scaling = verify_source_action()
    lanes = verify_target_action(outside_permutation, bc_minus_factor)
    raw_states, state_orbits, raw_rows, row_orbits = verify_quotient(outside_permutation)
    return {
        "lanes": lanes,
        "raw_states": raw_states,
        "state_orbits": state_orbits,
        "raw_rows": raw_rows,
        "row_orbits": row_orbits,
        "source_scaling": scaling,
    }


def main():
    result = verify()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_BC_EF_INVOLUTION_PASS "
        f"lanes={result['lanes']} raw_states={result['raw_states']} "
        f"state_orbits={result['state_orbits']} raw_rows={result['raw_rows']} "
        f"row_orbits={result['row_orbits']}"
    )


if __name__ == "__main__":
    main()
