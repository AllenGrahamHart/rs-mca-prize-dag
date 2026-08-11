#!/usr/bin/env python3
"""Verify the explicit m=2 incidence-only rational-trace fence."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "experiments/prize_resolution/rh_bivariate_m2_rational_trace_fence_result.json"


def inverse(value: int, prime: int) -> int:
    return pow(value % prime, prime - 2, prime)


def matrix_rank(matrix: list[list[int]], prime: int) -> int:
    rows = [row[:] for row in matrix]
    output = 0
    for column in range(len(rows[0])):
        pivot = next(
            (row for row in range(output, len(rows)) if rows[row][column] % prime),
            None,
        )
        if pivot is None:
            continue
        rows[output], rows[pivot] = rows[pivot], rows[output]
        scale = inverse(rows[output][column], prime)
        rows[output] = [entry * scale % prime for entry in rows[output]]
        for row in range(len(rows)):
            if row == output or not rows[row][column] % prime:
                continue
            factor = rows[row][column]
            rows[row] = [
                (entry - factor * base) % prime
                for entry, base in zip(rows[row], rows[output])
            ]
        output += 1
    return output


def root_polynomial(roots: list[int], prime: int) -> list[int]:
    polynomial = [1]
    for root in roots:
        product = [0] * (len(polynomial) + 1)
        for degree, coefficient in enumerate(polynomial):
            product[degree] = (product[degree] - root * coefficient) % prime
            product[degree + 1] = (product[degree + 1] + coefficient) % prime
        polynomial = product
    return polynomial


def main() -> None:
    payload = json.loads(RESULT.read_text())
    assert payload["schema"] == "rate-half-bivariate-m2-rational-trace-fence-v1"
    assert payload["complete"] is True
    parameters = payload["parameters"]
    assert parameters == {
        "domain_size": 32,
        "field": 97,
        "m": 2,
        "rho": 7,
        "supported_slopes": 9,
    }
    prime = parameters["field"]
    m = parameters["m"]
    rho = parameters["rho"]
    domain = payload["domain"]
    assert len(domain) == len(set(domain)) == 32
    assert all(value and pow(value, 32, prime) == 1 for value in domain)

    selected = payload["slopes"]["selected"]
    residual = payload["slopes"]["residual"]
    slopes = selected + residual
    assert selected == [0, 1] and len(set(slopes)) == 9
    owners = payload["owners"]
    assert len(owners) == 32
    deficient = payload["deficient"]
    assert [index for index, values in enumerate(owners) if len(values) == 1] == [
        deficient
    ]
    assert all(len(values) in (1, 2) and len(values) == len(set(values)) for values in owners)
    assert sum(2 - len(values) for values in owners) == 1

    root_sets = {
        slope: {index for index, values in enumerate(owners) if slope in values}
        for slope in slopes
    }
    assert all(len(root_sets[slope]) == rho for slope in slopes)
    assert payload["row_sizes"] == {str(slope): rho for slope in slopes}
    support = sorted(root_sets[selected[0]] | root_sets[selected[1]])
    assert support == payload["support"] and len(support) == 12
    assert deficient not in support

    intersections = {}
    unions = {}
    for left_index, left in enumerate(slopes):
        for right in slopes[left_index + 1 :]:
            key = f"{left},{right}"
            intersections[key] = len(root_sets[left] & root_sets[right])
            unions[key] = len(root_sets[left] | root_sets[right])
    assert intersections == payload["pair_intersections"]
    assert unions == payload["pair_unions"]
    assert max(intersections.values()) == 2 and min(unions.values()) == 12

    support_set = set(support)
    residual_overlap = {
        str(slope): len(root_sets[slope] & support_set) for slope in residual
    }
    assert residual_overlap == payload["residual_overlap"]
    need_x = rho - (((32 - len(support)) * m) // (len(slopes) - 2) + 1)
    assert need_x == payload["bad_overlap_threshold"] == 1
    assert max(residual_overlap.values()) == 2

    for pair, trace in zip(payload["inverse_pairs"], payload["trace_values"]):
        assert pair[0] * pair[1] % prime == 1
        assert sum(pair) % prime == trace
    assert sorted(value for pair in payload["inverse_pairs"] for value in pair) == sorted(
        payload["support_values"]
    )

    mus = {int(column): value for column, value in payload["mus"].items()}
    assert set(mus) == support_set
    normalized = {}
    nu_values = {}
    for column in support:
        polynomial = root_polynomial(owners[column] + [mus[column]], prime)
        assert len(polynomial) == 4 and polynomial[-1] == 1
        assert all(
            sum(coefficient * pow(slope, degree, prime) for degree, coefficient in enumerate(polynomial))
            % prime
            == 0
            for slope in selected
        )
        normalized[column] = polynomial
        nu = (-polynomial[m] - sum(selected)) % prime
        x = domain[column]
        assert nu == (x * x + 1) * inverse(x, prime) % prime
        nu_values[str(column)] = nu
    certificate = payload["rational_certificate"]
    assert certificate["P_coefficients"] == [0, 1]
    assert certificate["Q_coefficients"] == [1, 0, 1]
    assert certificate["degree_bound"] == 3
    assert certificate["nu_values"] == nu_values

    full_matrix = [
        [
            normalized[column][parameter_degree] * pow(domain[column], moment, prime)
            % prime
            for column in support
        ]
        for moment in range(4 * m + 1)
        for parameter_degree in range(m + 2)
    ]
    trace_matrix = [
        [pow(domain[column], moment, prime) for column in support]
        for moment in range(4 * m + 1)
    ] + [
        [
            normalized[column][m] * pow(domain[column], moment, prime) % prime
            for column in support
        ]
        for moment in range(4 * m + 1)
    ]
    assert matrix_rank(full_matrix, prime) == 11
    assert matrix_rank(trace_matrix, prime) == 11

    kernel = payload["kernel"]
    assert len(kernel) == 12 and all(kernel)
    assert all(
        sum(entry * value for entry, value in zip(row, kernel)) % prime == 0
        for row in full_matrix
    )

    extension = []
    for moment in range(len(support) - rho - 1):
        for parameter_degree in range(m + 1):
            row = []
            for column in support:
                x = domain[column]
                derivative = 1
                for other in support:
                    if other != column:
                        derivative = derivative * (x - domain[other]) % prime
                locator = root_polynomial(owners[column], prime)
                row.append(
                    pow(x, moment, prime)
                    * inverse(derivative, prime)
                    * locator[parameter_degree]
                    % prime
                )
            extension.append(row)
    assert any(
        sum(entry * value for entry, value in zip(row, kernel)) % prime
        for row in extension
    )
    assert matrix_rank(full_matrix + extension, prime) == 12
    assert payload["ranks"] == {
        "columns": 12,
        "full_bivariate": 11,
        "top_plus_trace": 11,
        "with_locator_extension": 12,
    }
    assert payload["degree_rho_extension"]["exists"] is False

    print(
        "RATE_HALF_BIVARIATE_INCIDENCE_ONLY_RATIONAL_TRACE_ROUTE_FENCE_PASS "
        "rows=9 pair_unions=36 rank_old=11 rank_extended=12"
    )


if __name__ == "__main__":
    main()
