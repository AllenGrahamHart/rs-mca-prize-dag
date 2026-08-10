#!/usr/bin/env python3
"""Construct an m=2 incidence witness with a rational trace certificate."""

from __future__ import annotations

import json
from pathlib import Path

import modal


P = 97
M = 2
N = 32
RHO = 7
RESULT = Path(__file__).with_name("rh_bivariate_m2_rational_trace_fence_result.json")

APP = modal.App("rate-half-bivariate-m2-rational-trace-fence")
IMAGE = modal.Image.debian_slim()


def primitive_root() -> int:
    for candidate in range(2, P):
        if pow(candidate, 48, P) != 1 and pow(candidate, 32, P) != 1:
            return candidate
    raise AssertionError("no primitive root")


GENERATOR = primitive_root()
ZETA = pow(GENERATOR, 3, P)
DOMAIN = tuple(pow(ZETA, index, P) for index in range(N))


def inverse(value: int) -> int:
    return pow(value % P, P - 2, P)


def rank(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    output = 0
    for column in range(len(rows[0])):
        pivot = next(
            (row for row in range(output, len(rows)) if rows[row][column] % P),
            None,
        )
        if pivot is None:
            continue
        rows[output], rows[pivot] = rows[pivot], rows[output]
        scale = inverse(rows[output][column])
        rows[output] = [entry * scale % P for entry in rows[output]]
        for row in range(len(rows)):
            if row == output or not rows[row][column] % P:
                continue
            factor = rows[row][column]
            rows[row] = [
                (entry - factor * base) % P
                for entry, base in zip(rows[row], rows[output])
            ]
        output += 1
    return output


def solve_square(matrix: list[list[int]], target: list[int]) -> list[int] | None:
    size = len(matrix)
    rows = [matrix[row][:] + [target[row] % P] for row in range(size)]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if rows[row][column] % P),
            None,
        )
        if pivot is None:
            return None
        rows[column], rows[pivot] = rows[pivot], rows[column]
        scale = inverse(rows[column][column])
        rows[column] = [entry * scale % P for entry in rows[column]]
        for row in range(size):
            if row == column or not rows[row][column] % P:
                continue
            factor = rows[row][column]
            rows[row] = [
                (entry - factor * base) % P
                for entry, base in zip(rows[row], rows[column])
            ]
    return [rows[index][-1] for index in range(size)]


def root_polynomial(roots: tuple[int, ...]) -> list[int]:
    polynomial = [1]
    for root in roots:
        product = [0] * (len(polynomial) + 1)
        for degree, coefficient in enumerate(polynomial):
            product[degree] = (product[degree] - root * coefficient) % P
            product[degree + 1] = (product[degree + 1] + coefficient) % P
        polynomial = product
    return polynomial


def construct() -> dict:
    assert len(set(DOMAIN)) == N and pow(ZETA, N, P) == 1
    index_of = {value: index for index, value in enumerate(DOMAIN)}

    inverse_pairs = []
    seen = set()
    for value in DOMAIN:
        partner = inverse(value)
        key = tuple(sorted((value, partner)))
        if value == partner or key in seen:
            continue
        seen.add(key)
        inverse_pairs.append(key)
    chosen_pairs = inverse_pairs[:6]
    traces = [(first + second) % P for first, second in chosen_pairs]
    assert len(set(traces)) == 6

    free = [value for value in range(P) if value not in traces]
    first_slope, second_slope, extra_slope = free[:3]
    residual_slopes = traces + [extra_slope]
    slopes = [first_slope, second_slope] + residual_slopes
    assert len(set(slopes)) == 9

    owners: list[list[int]] = [[] for _ in range(N)]
    mus: dict[int, int] = {}

    # One inverse pair is the selected-pair intersection. The other five
    # contribute one exclusive point to each selected support.
    intersection_pair = chosen_pairs[0]
    for value in intersection_pair:
        column = index_of[value]
        owners[column] = [first_slope, second_slope]
        mus[column] = traces[0]

    for pair_index, pair in enumerate(chosen_pairs[1:], start=1):
        first_value, second_value = pair
        first_column = index_of[first_value]
        second_column = index_of[second_value]
        owners[first_column] = [first_slope, traces[pair_index]]
        owners[second_column] = [second_slope, traces[pair_index]]
        mus[first_column] = second_slope
        mus[second_column] = first_slope

    support = sorted(column for column, values in enumerate(owners) if values)
    assert len(support) == 12
    outside = [column for column in range(N) if column not in support]
    assert len(outside) == 20

    # Start from K_7, remove three edges, and duplicate (0,6). Together
    # with one singleton at vertex 1 this realizes outside degrees
    # (7,5,5,5,5,5,7) with pair multiplicity at most two.
    removed = {(1, 2), (1, 3), (4, 5)}
    edges = [
        (left, right)
        for left in range(7)
        for right in range(left + 1, 7)
        if (left, right) not in removed
    ]
    edges.append((0, 6))
    assert len(edges) == 19
    for column, (left, right) in zip(outside[:19], edges):
        owners[column] = [residual_slopes[left], residual_slopes[right]]
    deficient = outside[-1]
    owners[deficient] = [residual_slopes[1]]

    root_sets = {
        slope: {column for column, values in enumerate(owners) if slope in values}
        for slope in slopes
    }
    assert all(len(root_sets[slope]) == RHO for slope in slopes)
    assert sum(2 - len(values) for values in owners) == 1
    assert deficient not in support

    intersections = {
        f"{left},{right}": len(root_sets[left] & root_sets[right])
        for left_index, left in enumerate(slopes)
        for right in slopes[left_index + 1 :]
    }
    pair_unions = {
        key: 2 * RHO - value for key, value in intersections.items()
    }
    selected_key = f"{first_slope},{second_slope}"
    assert pair_unions[selected_key] == 12
    assert min(pair_unions.values()) == 12
    assert max(intersections.values()) == 2

    residual_overlap = {
        slope: len(root_sets[slope] & set(support)) for slope in residual_slopes
    }
    need_x = RHO - (((N - len(support)) * M) // (len(slopes) - 2) + 1)
    assert need_x == 1 and max(residual_overlap.values()) == 2

    normalized_polynomials = {}
    nu_values = {}
    matrix_columns = []
    for column in support:
        roots = tuple(owners[column] + [mus[column]])
        polynomial = root_polynomial(roots)
        assert len(polynomial) == M + 2 and polynomial[-1] == 1
        normalized_polynomials[column] = polynomial
        nu = (-polynomial[M] - first_slope - second_slope) % P
        nu_values[column] = nu
        x = DOMAIN[column]
        rational_value = (x * x + 1) * inverse(x) % P
        assert nu == rational_value
        matrix_columns.append((column, polynomial))

    full_matrix = [
        [
            polynomial[parameter_degree] * pow(DOMAIN[column], moment, P) % P
            for column, polynomial in matrix_columns
        ]
        for moment in range(4 * M + 1)
        for parameter_degree in range(M + 2)
    ]
    trace_matrix = [
        [pow(DOMAIN[column], moment, P) for column in support]
        for moment in range(4 * M + 1)
    ] + [
        [
            normalized_polynomials[column][M]
            * pow(DOMAIN[column], moment, P)
            % P
            for column in support
        ]
        for moment in range(4 * M + 1)
    ]
    full_rank = rank(full_matrix)
    trace_rank = rank(trace_matrix)
    assert trace_rank < len(support)

    extension_matrix = []
    extension_checks = len(support) - (RHO + 1)
    for moment in range(extension_checks):
        for parameter_degree in range(M + 1):
            row = []
            for column in support:
                x = DOMAIN[column]
                sigma_derivative = 1
                for other_column in support:
                    if other_column != column:
                        sigma_derivative = (
                            sigma_derivative * (x - DOMAIN[other_column])
                        ) % P
                locator = root_polynomial(tuple(owners[column]))
                row.append(
                    pow(x, moment, P)
                    * inverse(sigma_derivative)
                    * locator[parameter_degree]
                    % P
                )
            extension_matrix.append(row)
    combined_rank = rank(full_matrix + extension_matrix)
    assert combined_rank == len(support)

    # The rational certificate gives the explicit all-nonzero kernel
    # lambda_x=P(x)/sigma'_W(x), with P(X)=X.
    support_values = [DOMAIN[column] for column in support]
    kernel = []
    for x in support_values:
        sigma_derivative = 1
        for value in support_values:
            if value != x:
                sigma_derivative = sigma_derivative * (x - value) % P
        kernel.append(x * inverse(sigma_derivative) % P)
    assert all(kernel)
    assert all(
        sum(entry * coefficient for entry, coefficient in zip(row, kernel)) % P
        == 0
        for row in full_matrix
    )

    # Check the next necessary gate: can Q_Y(x)=lambda_x*A_x(Y) on W be
    # interpolated coefficientwise by polynomials of X-degree <=rho?
    q_values = [[] for _ in range(M + 1)]
    for coefficient, column in zip(kernel, support):
        locator = root_polynomial(tuple(owners[column]))
        for degree in range(M + 1):
            q_values[degree].append(coefficient * locator[degree] % P)
    sample_size = RHO + 1
    vandermonde = [
        [pow(DOMAIN[column], degree, P) for degree in range(sample_size)]
        for column in support[:sample_size]
    ]
    coefficient_polynomials = []
    degree_extension = True
    for parameter_degree in range(M + 1):
        coefficients = solve_square(
            vandermonde,
            q_values[parameter_degree][:sample_size],
        )
        if coefficients is None or any(
            sum(
                coefficient * pow(DOMAIN[column], degree, P)
                for degree, coefficient in enumerate(coefficients)
            )
            % P
            != q_values[parameter_degree][support_index]
            for support_index, column in enumerate(support)
        ):
            degree_extension = False
            coefficient_polynomials = []
            break
        coefficient_polynomials.append(coefficients)

    owner_match = False
    supported_parameters = []
    if degree_extension:
        owner_match = True
        for slope in slopes:
            roots = {
                column
                for column in range(N)
                if sum(
                    pow(slope, parameter_degree, P)
                    * sum(
                        coefficient * pow(DOMAIN[column], degree, P)
                        for degree, coefficient in enumerate(
                            coefficient_polynomials[parameter_degree]
                        )
                    )
                    for parameter_degree in range(M + 1)
                )
                % P
                == 0
            }
            if roots != root_sets[slope]:
                owner_match = False
            if len(roots) == RHO:
                supported_parameters.append(slope)

    return {
        "schema": "rate-half-bivariate-m2-rational-trace-fence-v1",
        "complete": True,
        "parameters": {
            "field": P,
            "m": M,
            "domain_size": N,
            "rho": RHO,
            "supported_slopes": len(slopes),
        },
        "slopes": {
            "selected": [first_slope, second_slope],
            "residual": residual_slopes,
        },
        "domain": list(DOMAIN),
        "inverse_pairs": [list(pair) for pair in chosen_pairs],
        "trace_values": traces,
        "owners": owners,
        "mus": {str(column): value for column, value in sorted(mus.items())},
        "support": support,
        "support_values": [DOMAIN[column] for column in support],
        "deficient": deficient,
        "row_sizes": {str(slope): len(root_sets[slope]) for slope in slopes},
        "pair_intersections": intersections,
        "pair_unions": pair_unions,
        "residual_overlap": {
            str(slope): value for slope, value in residual_overlap.items()
        },
        "bad_overlap_threshold": need_x,
        "rational_certificate": {
            "P_coefficients": [0, 1],
            "Q_coefficients": [1, 0, 1],
            "degree_bound": 3,
            "nu_values": {str(column): value for column, value in nu_values.items()},
        },
        "kernel": kernel,
        "degree_rho_extension": {
            "exists": degree_extension,
            "owner_match": owner_match,
            "coefficient_polynomials": coefficient_polynomials,
            "supported_parameters": supported_parameters,
        },
        "ranks": {
            "columns": len(support),
            "full_bivariate": full_rank,
            "with_locator_extension": combined_rank,
            "top_plus_trace": trace_rank,
        },
    }


@APP.function(image=IMAGE, cpu=1.0, memory=256, timeout=30)
def remote_construct() -> dict:
    return construct()


@APP.local_entrypoint()
def main() -> None:
    result = remote_construct.remote()
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    ranks = result["ranks"]
    print(
        "RH_BIVARIATE_M2_RATIONAL_TRACE_FENCE_COMPLETE "
        f"trace_rank={ranks['top_plus_trace']}/{ranks['columns']} "
        f"full_rank={ranks['full_bivariate']}/{ranks['columns']}"
    )
