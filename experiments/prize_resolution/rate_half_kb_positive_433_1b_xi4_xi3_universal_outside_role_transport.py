#!/usr/bin/env python3
"""Verify the universal xi4/xi3 outside-role transport."""

import itertools


ROLES = ("LA", "AB", "AC", "BC+", "BC-")
XI3 = 3
XI4 = 4
SOURCE_SIGNS = tuple(itertools.product((-1, 1), repeat=2))
TARGET_LANES = tuple(itertools.product((-1, 1), repeat=2))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


# Sparse integer polynomials in (a,b,c,d,e,f).
def constant(value):
    return {} if value == 0 else {(0, 0, 0, 0, 0, 0): value}


def variable(index):
    exponent = [0] * 6
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
    """Identify guard polynomials that differ by the unit -1."""
    if not value:
        return ()
    ordered = sorted(value.items())
    sign = 1 if ordered[0][1] > 0 else -1
    return tuple((exponent, sign * coefficient) for exponent, coefficient in ordered)


def signed_sum(left, right, sign=1):
    return square(add(left, scale(right, sign)))


def atlas_records(coordinates, sigma_c, sigma_o):
    _, b, c, d, e, f = coordinates
    de = multiply(d, e)
    return (
        de,
        de,
        scale(de, -1),
        multiply(d, f),
        scale(multiply(e, f), sigma_o),
        multiply(b, f),
        scale(multiply(c, f), sigma_c),
    )


def atlas_sums(coordinates, sigma_c, sigma_o):
    _, b, c, d, e, f = coordinates
    return (
        signed_sum(d, e),
        signed_sum(d, e),
        signed_sum(d, e, -1),
        signed_sum(d, f),
        signed_sum(e, f, sigma_o),
        signed_sum(b, f),
        signed_sum(c, f, sigma_c),
    )


def target_guards(coordinates):
    guards = list(coordinates)
    for left, right in itertools.combinations(coordinates, 2):
        guards.append(add(left, scale(right, -1)))
        guards.append(add(left, right))
    return {normalize_unit(value) for value in guards}


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


def role_cells():
    output = []
    for singleton in range(5):
        rest = tuple(index for index in range(5) if index != singleton)
        for matching in pairings(rest):
            output.append((singleton, matching))
    return tuple(output)


def canonical_cell(cell):
    singleton, matching = cell
    return singleton, tuple(sorted(tuple(sorted(pair)) for pair in matching))


def permute_cell(cell, permutation):
    singleton, matching = cell
    return canonical_cell((
        permutation[singleton],
        tuple(
            (permutation[left], permutation[right])
            for left, right in matching
        ),
    ))


def verify_role_cell_action():
    cells = role_cells()
    require(len(cells) == 15, "15 role cells")
    indexed = {canonical_cell(cell): index for index, cell in enumerate(cells)}
    require(len(indexed) == 15, "15 distinct role cells")

    # The D/E transport acts only on outside coordinates, so its induced
    # permutation on the five common roles is the identity.
    outside_swap = {index: index for index in range(5)}
    for cell_index, cell in enumerate(cells):
        require(
            indexed[permute_cell(cell, outside_swap)] == cell_index,
            f"D/E outside transport fixes source role cell {cell_index}",
        )

    bc_swap = {0: 0, 1: 2, 2: 1, 3: 3, 4: 4}
    require(indexed[permute_cell(cells[3], bc_swap)] == 6,
            "B/C exchange sends cell 3 to cell 6")


def verify_lane_action(sigma_c, sigma_o):
    # Canonical active-edge signs are AB,AC,BF,CF,DE,DF,EF.
    original = {
        "AB": 1, "AC": 1, "BF": 1, "CF": sigma_c,
        "DE": 1, "DF": 1, "EF": sigma_o,
    }
    # Swap D and E, then gauge both new outside vertices by sigma_o.
    transported = {
        "AB": original["AB"],
        "AC": original["AC"],
        "BF": original["BF"],
        "CF": original["CF"],
        "DE": original["DE"] * sigma_o * sigma_o,
        "DF": original["EF"] * sigma_o,
        "EF": original["DF"] * sigma_o,
    }
    require(transported == original, "canonical lane fixed")
    require(
        transported["AB"] * transported["BF"]
        * transported["CF"] * transported["AC"] == sigma_c,
        "common cycle invariant",
    )
    require(
        transported["DE"] * transported["DF"] * transported["EF"]
        == sigma_o,
        "outside cycle invariant",
    )


def verify_transport():
    coordinates = tuple(variable(index) for index in range(6))
    a, b, c, d, e, f = coordinates
    compact_xi4 = (0, 1, 2, 3, 5, 6)
    compact_xi3 = (0, 1, 2, 4, 5, 6)
    matching_rows = tuple(pairings(range(6)))
    require(len(matching_rows) == 15, "15 canonical residual matchings")
    require(len(set(matching_rows)) == 15, "distinct canonical matchings")

    for sigma_c, sigma_o in TARGET_LANES:
        transformed = (a, b, c, scale(e, sigma_o), scale(d, sigma_o), f)
        original_products = atlas_records(coordinates, sigma_c, sigma_o)
        original_sums = atlas_sums(coordinates, sigma_c, sigma_o)
        xi3_products = atlas_records(transformed, sigma_c, sigma_o)
        xi3_sums = atlas_sums(transformed, sigma_c, sigma_o)

        # The full atlas transposition is xi3 <-> xi4 and fixes all other rows.
        permutation = (0, 1, 2, 4, 3, 5, 6)
        require(
            tuple(xi3_products[index] for index in permutation)
            == original_products,
            "product-record transport",
        )
        require(
            tuple(xi3_sums[index] for index in permutation) == original_sums,
            "squared-sum transport",
        )
        require(
            original_products[XI4] == xi3_products[XI3]
            and original_sums[XI4] == xi3_sums[XI3],
            "missing-record transport",
        )
        require(
            tuple(original_products[index] for index in compact_xi4)
            == tuple(xi3_products[index] for index in compact_xi3),
            "compact residual product order",
        )
        require(
            tuple(original_sums[index] for index in compact_xi4)
            == tuple(xi3_sums[index] for index in compact_xi3),
            "compact residual squared-sum order",
        )
        require(
            target_guards(coordinates) == target_guards(transformed),
            "target guard divisor fixed",
        )
        verify_lane_action(sigma_c, sigma_o)

        for matching_index, matching in enumerate(matching_rows):
            left_products = tuple(
                (original_products[compact_xi4[left]],
                 original_products[compact_xi4[right]])
                for left, right in matching
            )
            right_products = tuple(
                (xi3_products[compact_xi3[left]],
                 xi3_products[compact_xi3[right]])
                for left, right in matching
            )
            left_sums = tuple(
                (original_sums[compact_xi4[left]],
                 original_sums[compact_xi4[right]])
                for left, right in matching
            )
            right_sums = tuple(
                (xi3_sums[compact_xi3[left]],
                 xi3_sums[compact_xi3[right]])
                for left, right in matching
            )
            require(left_products == right_products,
                    f"matching {matching_index} product equations")
            require(left_sums == right_sums,
                    f"matching {matching_index} sum equations")

    verify_role_cell_action()
    return {
        "role_cells": len(role_cells()),
        "source_signs": len(SOURCE_SIGNS),
        "target_lanes": len(TARGET_LANES),
        "matchings": len(matching_rows),
        "system_bijections": (
            len(role_cells()) * len(SOURCE_SIGNS)
            * len(TARGET_LANES) * len(matching_rows)
        ),
    }


def main():
    census = verify_transport()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_UNIVERSAL_XI4_XI3_TRANSPORT_PASS "
        f"role_cells={census['role_cells']} "
        f"source_signs={census['source_signs']} "
        f"target_lanes={census['target_lanes']} "
        f"matchings={census['matchings']} "
        f"system_bijections={census['system_bijections']}"
    )


if __name__ == "__main__":
    main()
