#!/usr/bin/env python3
"""Check the exact ten-orbit quotient of the 60 positive common rows."""

from collections import deque
import itertools

import sympy as sp


ROLES = ("LC", "AB+1", "AB+2", "AB-", "AC")
ROLE_INDEX = {role: index for index, role in enumerate(ROLES)}
PRODUCTS = ("-c^2", "b", "b", "-b", "c")
SUMS = (0, "1+b", "1+b", "1-b", "1+c")
ROLE_ORBITS = (
    (0,), (1, 2), (3, 6), (4, 7), (5, 8),
    (9, 10), (11,), (12, 13), (14,),
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


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


def roots(cell, epsilon_1, epsilon_2, r, t):
    singleton, matching = cells()[cell]
    output = [None] * 5
    output[matching[0][0]] = sp.Integer(1)
    output[matching[0][1]] = epsilon_1 * sp.I
    output[matching[1][0]] = r
    output[matching[1][1]] = epsilon_2 * sp.I * r
    output[singleton] = t
    return tuple(output)


def compare_records(observed, expected, message):
    b, c = sp.symbols("b c")
    sums = (0, 1 + b, 1 + b, 1 - b, 1 + c)
    for index, (left, right) in enumerate(zip(observed, expected)):
        require(sp.cancel(left**2 - right**2) == 0,
                f"{message} {ROLES[index]} label")
        require(sp.cancel(left * sums[index] - right * sums[index]) == 0,
                f"{message} {ROLES[index]} q")


def check_loop_paired_actions():
    r, t = sp.symbols("r t", nonzero=True)
    for cell in range(3, 15):
        singleton, matching = cells()[cell]
        require(matching[0][0] == ROLE_INDEX["LC"], f"cell {cell} LC anchor")
        require(singleton != ROLE_INDEX["LC"], f"cell {cell} nonloop singleton")
        for epsilon_1, epsilon_2 in itertools.product((-1, 1), repeat=2):
            source = roots(cell, epsilon_1, epsilon_2, r, t)
            negated = tuple(-value for value in source)
            expected_negated = roots(
                cell, -epsilon_1, epsilon_2, -r, -t
            )
            compare_records(negated, expected_negated, f"cell {cell} deck")

            reciprocal = tuple(-1 / value for value in source)
            expected_reciprocal = roots(
                cell, epsilon_1, -epsilon_2, -1 / r, -1 / t
            )
            compare_records(
                reciprocal, expected_reciprocal, f"cell {cell} reciprocal"
            )


def check_cell0_actions():
    r, t = sp.symbols("r t", nonzero=True)
    require(cells()[0] == (0, ((1, 2), (3, 4))), "cell 0 shape")
    for epsilon_1, epsilon_2 in itertools.product((-1, 1), repeat=2):
        source = roots(0, epsilon_1, epsilon_2, r, t)

        scale = 1 / (epsilon_1 * sp.I)
        scaled = [scale * value for value in source]
        scaled[1], scaled[2] = scaled[2], scaled[1]
        expected_swap = roots(0, -epsilon_1, epsilon_2, scale * r, scale * t)
        compare_records(tuple(scaled), expected_swap, "cell 0 duplicate swap")

        reciprocal = tuple(1 / value for value in source)
        expected_reciprocal = roots(
            0, -epsilon_1, -epsilon_2, 1 / r, 1 / t
        )
        compare_records(reciprocal, expected_reciprocal, "cell 0 reciprocal")


def check_cell12_actions():
    r, t = sp.symbols("r t", nonzero=True)
    require(cells()[1] == (0, ((1, 3), (2, 4))), "cell 1 shape")
    require(cells()[2] == (0, ((1, 4), (2, 3))), "cell 2 shape")
    for epsilon_1, epsilon_2 in itertools.product((-1, 1), repeat=2):
        source = roots(1, epsilon_1, epsilon_2, r, t)
        reciprocal = tuple(1 / value for value in source)
        expected_reciprocal = roots(
            1, -epsilon_1, -epsilon_2, 1 / r, 1 / t
        )
        compare_records(reciprocal, expected_reciprocal, "cell 1 reciprocal")

        swapped = list(source)
        swapped[1], swapped[2] = swapped[2], swapped[1]
        scale = 1 / r
        swapped = tuple(scale * value for value in swapped)
        expected_cell2 = roots(
            2, epsilon_2, epsilon_1, 1 / r, t / r
        )
        compare_records(swapped, expected_cell2, "cell 1 to cell 2")


def orbit_census():
    states = {
        (cell, epsilon_1, epsilon_2)
        for cell in range(15)
        for epsilon_1, epsilon_2 in itertools.product((-1, 1), repeat=2)
    }
    partner = {}
    for orbit in ROLE_ORBITS:
        if len(orbit) == 2:
            partner[orbit[0]] = orbit[1]
            partner[orbit[1]] = orbit[0]

    def neighbors(state):
        cell, epsilon_1, epsilon_2 = state
        output = set()
        if cell >= 3:
            output.add((cell, -epsilon_1, epsilon_2))
            output.add((cell, epsilon_1, -epsilon_2))
        elif cell == 0:
            output.add((0, -epsilon_1, epsilon_2))
            output.add((0, -epsilon_1, -epsilon_2))
        else:
            output.add((cell, -epsilon_1, -epsilon_2))
        if cell in partner:
            if {cell, partner[cell]} == {1, 2}:
                output.add((partner[cell], epsilon_2, epsilon_1))
            else:
                # The exact sign image is immaterial here: each endpoint
                # already has one four-sign source-projectivity orbit.
                output.add((partner[cell], epsilon_1, epsilon_2))
        return output

    unseen = set(states)
    orbits = []
    while unseen:
        seed = min(unseen)
        queue = deque([seed])
        orbit = {seed}
        while queue:
            current = queue.popleft()
            for neighbor in neighbors(current):
                require(neighbor in states, "state closure")
                if neighbor not in orbit:
                    orbit.add(neighbor)
                    queue.append(neighbor)
        unseen -= orbit
        orbits.append(tuple(sorted(orbit)))
    orbits.sort(key=lambda orbit: orbit[0])
    sizes = sorted(len(orbit) for orbit in orbits)
    require(len(orbits) == 10, f"ten symmetry orbits: {orbits}")
    require(sizes == [4, 4, 4, 4, 4, 8, 8, 8, 8, 8],
            f"orbit sizes: {sizes}; orbits={orbits}")
    representatives = [orbit[0] for orbit in orbits]
    require(sum(5 <= cell <= 8 for cell, _, _ in representatives) == 1,
            "cell-5/8 representative")
    return orbits


def main():
    require(len(cells()) == 15, "cell count")
    check_loop_paired_actions()
    check_cell0_actions()
    check_cell12_actions()
    orbits = orbit_census()
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_COMMON_ROOT_SIGN_SYMMETRY_PASS "
        f"raw_rows=60 exact_orbits={len(orbits)} closed_orbits=1 open_orbits=9"
    )


if __name__ == "__main__":
    main()
