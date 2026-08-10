#!/usr/bin/env python3
"""Verify locator-extension parity checks and the genuine m=1 control."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
M1_PROBE = ROOT / "experiments/prize_resolution/rh_bivariate_m1_rank_probe.py"


def inverse(value: int, prime: int) -> int:
    return pow(value % prime, prime - 2, prime)


def matrix_rank(matrix: list[list[int]], prime: int) -> int:
    if not matrix:
        return 0
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


def extension_checks(points: list[int], rho: int, prime: int) -> list[list[int]]:
    rows = []
    for moment in range(max(0, len(points) - rho - 1)):
        row = []
        for x in points:
            sigma_derivative = 1
            for value in points:
                if value != x:
                    sigma_derivative = sigma_derivative * (x - value) % prime
            row.append(pow(x, moment, prime) * inverse(sigma_derivative, prime) % prime)
        rows.append(row)
    return rows


def load_m1_probe():
    spec = importlib.util.spec_from_file_location("rh_bivariate_m1_probe", M1_PROBE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    prime = 101
    generic_cases = 0
    for size, rho in ((5, 4), (6, 3), (9, 4), (12, 7)):
        points = list(range(1, size + 1))
        checks = extension_checks(points, rho, prime)
        assert matrix_rank(checks, prime) == max(0, size - rho - 1)
        for shift in range(3):
            coefficients = [shift + 2 * degree + 1 for degree in range(rho + 1)]
            values = [
                sum(
                    coefficient * pow(x, degree, prime)
                    for degree, coefficient in enumerate(coefficients)
                )
                % prime
                for x in points
            ]
            assert all(
                sum(entry * value for entry, value in zip(row, values)) % prime == 0
                for row in checks
            )
            generic_cases += 1
        if checks:
            too_large = [pow(x, rho + 1, prime) for x in points]
            assert any(
                sum(entry * value for entry, value in zip(row, too_large)) % prime
                for row in checks
            )

    probe = load_m1_probe()
    representatives = {}
    for slope, support in probe.SUPPORTS.items():
        target = tuple(
            (a + slope * b) % probe.PRIME for a, b in zip(probe.Y0, probe.Y1)
        )
        representatives[slope] = probe.solve_support(support, target)
    owner = {
        point: slope for slope, points in probe.SUPPORTS.items() for point in points
    }

    m1_pairs = 0
    slopes = list(probe.SUPPORTS)
    for first_index, first in enumerate(slopes):
        for second in slopes[first_index + 1 :]:
            matrix, kernel, support = probe.pair_matrix(first, second, representatives)
            checks = extension_checks(list(support), rho=3, prime=probe.PRIME)
            extension = []
            for check in checks:
                extension.append(
                    [
                        check[index] * (-owner[x]) % probe.PRIME
                        for index, x in enumerate(support)
                    ]
                )
                extension.append(check[:])
            assert all(
                sum(entry * value for entry, value in zip(row, kernel)) % probe.PRIME
                == 0
                for row in extension
            )
            assert probe.matrix_rank(matrix + extension) == 5 < len(support)
            m1_pairs += 1

    assert m1_pairs == 10
    print(
        "RATE_HALF_BIVARIATE_LOCATOR_EXTENSION_KERNEL_REDUCTION_PASS "
        f"generic_cases={generic_cases} m1_pairs={m1_pairs}"
    )


if __name__ == "__main__":
    main()
