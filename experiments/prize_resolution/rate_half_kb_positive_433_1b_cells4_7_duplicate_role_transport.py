#!/usr/bin/env python3
"""Exact duplicate-common-role transport from complete cell 4 to cell 7."""

import itertools


ROLES = ("LA", "AB", "AC", "BC+", "BC-")
SOURCE_SIGNS = tuple(itertools.product((-1, 1), repeat=2))
TARGET_LANES = tuple(itertools.product((-1, 1), repeat=2))
OUTSIDE_PERMUTATION = (0, 1, 2, 3, 4, 6, 5)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


# Sparse integer polynomials in (a,b,c,d,e,f,r,t,i).
VARIABLE_COUNT = 9


def constant(value):
    return {} if value == 0 else {(0,) * VARIABLE_COUNT: value}


def variable(index):
    exponent = [0] * VARIABLE_COUNT
    exponent[index] = 1
    return {tuple(exponent): 1}


def add(left, right):
    output = dict(left)
    for exponent, coefficient in right.items():
        output[exponent] = output.get(exponent, 0) + coefficient
        if output[exponent] == 0:
            del output[exponent]
    return output


def scale(value, scalar):
    return {
        exponent: scalar * coefficient
        for exponent, coefficient in value.items()
        if scalar * coefficient
    }


def multiply(left, right):
    output = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = tuple(
                a + b for a, b in zip(left_exponent, right_exponent)
            )
            output[exponent] = (
                output.get(exponent, 0)
                + left_coefficient * right_coefficient
            )
    return {key: value for key, value in output.items() if value}


def square(value):
    return multiply(value, value)


def normalize_unit(value):
    if not value:
        return ()
    ordered = sorted(value.items())
    sign = 1 if ordered[0][1] > 0 else -1
    return tuple((exponent, sign * coefficient) for exponent, coefficient in ordered)


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
        for matching in pairings(rest):
            output.append((singleton, matching))
    return tuple(output)


def canonical_cell(cell):
    singleton, matching = cell
    return singleton, canonical_matching(matching)


def permute_cell(cell, permutation):
    singleton, matching = cell
    return canonical_cell((
        permutation[singleton],
        tuple(
            (permutation[left], permutation[right])
            for left, right in matching
        ),
    ))


def common_cell4_rows(epsilon_1, epsilon_2, values):
    _, b, c, _, _, _, r, t, iota = values
    one = constant(1)
    return {
        "LA": (constant(-1), constant(0), one),
        "AB": (b, multiply(t, add(one, b)), square(t)),
        "AC": (c, multiply(r, add(one, c)), square(r)),
        "BC+": (
            multiply(b, c),
            scale(multiply(iota, add(b, c)), epsilon_1),
            constant(-1),
        ),
        "BC-": (
            scale(multiply(b, c), -1),
            scale(multiply(multiply(iota, r), add(b, scale(c, -1))), epsilon_2),
            scale(square(r), -1),
        ),
    }


def common_cell7_rows(epsilon_1, epsilon_2, values):
    # values already contain the transformed targets B'=c, C'=b.
    _, b, c, _, _, _, r, t, iota = values
    one = constant(1)
    return {
        "LA": (constant(-1), constant(0), one),
        "AB": (b, multiply(r, add(one, b)), square(r)),
        "AC": (c, multiply(t, add(one, c)), square(t)),
        "BC+": (
            multiply(b, c),
            scale(multiply(iota, add(b, c)), epsilon_1),
            constant(-1),
        ),
        "BC-": (
            scale(multiply(b, c), -1),
            scale(multiply(multiply(iota, r), add(b, scale(c, -1))), epsilon_2),
            scale(square(r), -1),
        ),
    }


def outside_records(values, sigma_c, sigma_o):
    _, b, c, d, e, f, _, _, _ = values
    de = multiply(d, e)
    return (
        de, de, scale(de, -1), multiply(d, f),
        scale(multiply(e, f), sigma_o), multiply(b, f),
        scale(multiply(c, f), sigma_c),
    )


def squared_sum(left, right, sign=1):
    return square(add(left, scale(right, sign)))


def outside_sums(values, sigma_c, sigma_o):
    _, b, c, d, e, f, _, _, _ = values
    return (
        squared_sum(d, e), squared_sum(d, e), squared_sum(d, e, -1),
        squared_sum(d, f), squared_sum(e, f, sigma_o),
        squared_sum(b, f), squared_sum(c, f, sigma_c),
    )


def target_guards(values):
    coordinates = values[:6]
    guards = list(coordinates)
    for left, right in itertools.combinations(coordinates, 2):
        guards.append(add(left, scale(right, -1)))
        guards.append(add(left, right))
    return {normalize_unit(value) for value in guards}


def verify_role_cell_action():
    cells = role_cells()
    indexed = {canonical_cell(cell): index for index, cell in enumerate(cells)}
    bc_swap = {0: 0, 1: 2, 2: 1, 3: 3, 4: 4}
    require(indexed[permute_cell(cells[4], bc_swap)] == 7,
            "duplicate-role action cell 4 to cell 7")


def verify_lane_action(sigma_c, sigma_o):
    original = {
        "AB": 1, "AC": 1, "BF": 1, "CF": sigma_c,
        "DE": 1, "DF": 1, "EF": sigma_o,
    }
    # B/C are exchanged. Gauging D,E,F by sigma_c restores canonical signs.
    transported = {
        "AB": original["AC"],
        "AC": original["AB"],
        "BF": original["CF"] * sigma_c,
        "CF": original["BF"] * sigma_c,
        "DE": original["DE"] * sigma_c * sigma_c,
        "DF": original["DF"] * sigma_c * sigma_c,
        "EF": original["EF"] * sigma_c * sigma_c,
    }
    require(transported == original, "canonical target lane fixed")


def case_transport(xi, matching_index, matching_rows):
    new_xi = OUTSIDE_PERMUTATION[xi]
    old_residual = tuple(index for index in range(7) if index != xi)
    new_residual = tuple(index for index in range(7) if index != new_xi)
    new_compact = {full: compact for compact, full in enumerate(new_residual)}
    old_matching = matching_rows[matching_index]
    new_matching = canonical_matching(tuple(
        (
            new_compact[OUTSIDE_PERMUTATION[old_residual[left]]],
            new_compact[OUTSIDE_PERMUTATION[old_residual[right]]],
        )
        for left, right in old_matching
    ))
    matching_lookup = {
        canonical_matching(value): index
        for index, value in enumerate(matching_rows)
    }
    return new_xi, matching_lookup[new_matching]


def verify_transport():
    values = tuple(variable(index) for index in range(VARIABLE_COUNT))
    a, b, c, d, e, f, r, t, iota = values
    matching_rows = tuple(pairings(range(6)))
    require(len(matching_rows) == 15, "15 matchings")
    verify_role_cell_action()

    for epsilon_1, epsilon_2 in SOURCE_SIGNS:
        transformed_common_values = (a, c, b, d, e, f, r, t, iota)
        cell4 = common_cell4_rows(epsilon_1, epsilon_2, values)
        cell7 = common_cell7_rows(
            epsilon_1, -epsilon_2, transformed_common_values
        )
        role_map = {
            "LA": "LA", "AB": "AC", "AC": "AB",
            "BC+": "BC+", "BC-": "BC-",
        }
        require(
            all(cell7[new_role] == cell4[old_role]
                for new_role, old_role in role_map.items()),
            "complete common Vieta-row transport",
        )

    for sigma_c, sigma_o in TARGET_LANES:
        transformed = (
            a, c, b, scale(d, sigma_c), scale(e, sigma_c),
            scale(f, sigma_c), r, t, iota,
        )
        original_records = outside_records(values, sigma_c, sigma_o)
        original_sums = outside_sums(values, sigma_c, sigma_o)
        transported_records = outside_records(transformed, sigma_c, sigma_o)
        transported_sums = outside_sums(transformed, sigma_c, sigma_o)
        require(
            all(transported_records[OUTSIDE_PERMUTATION[index]]
                == original_records[index] for index in range(7)),
            "outside product transport",
        )
        require(
            all(transported_sums[OUTSIDE_PERMUTATION[index]]
                == original_sums[index] for index in range(7)),
            "outside squared-sum transport",
        )
        require(target_guards(values) == target_guards(transformed),
                "target guard divisor fixed")
        verify_lane_action(sigma_c, sigma_o)

    case_images = set()
    for xi in range(7):
        for matching_index in range(15):
            new_xi, new_matching = case_transport(
                xi, matching_index, matching_rows
            )
            case_images.add((new_xi, new_matching))
    require(case_images == set(itertools.product(range(7), range(15))),
            "105-case missing/matching bijection")

    raw_images = {
        (
            *case_transport(xi, matching, matching_rows),
            epsilon_1, -epsilon_2, sigma_c, sigma_o,
        )
        for xi in range(7)
        for matching in range(15)
        for epsilon_1, epsilon_2 in SOURCE_SIGNS
        for sigma_c, sigma_o in TARGET_LANES
    }
    expected = set(itertools.product(
        range(7), range(15), (-1, 1), (-1, 1), (-1, 1), (-1, 1)
    ))
    require(raw_images == expected, "1680-case principal bijection")
    return {
        "source_signs": 4,
        "target_lanes": 4,
        "missing_matching_cases": len(case_images),
        "raw_cases": len(raw_images),
    }


def main():
    census = verify_transport()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_CELLS4_7_TRANSPORT_PASS "
        f"source_signs={census['source_signs']} "
        f"target_lanes={census['target_lanes']} "
        f"missing_matching_cases={census['missing_matching_cases']} "
        f"raw_cases={census['raw_cases']}"
    )


if __name__ == "__main__":
    main()
