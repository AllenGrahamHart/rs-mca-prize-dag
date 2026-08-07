#!/usr/bin/env python3
"""Independent exact checks for the ideal/Galois multiplicity supplier."""

from __future__ import annotations

import argparse
import itertools
import json
from decimal import Decimal, getcontext
from math import comb


def bareiss_det(matrix: list[list[int]]) -> int:
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (
                    a[i][j] * pivot_value - a[i][k] * a[k][j]
                ) // previous
        previous = pivot_value
    return sign * a[-1][-1]


def cyclotomic_coordinates(n: int, subset: tuple[int, ...]) -> list[int]:
    h = n // 2
    coordinates = [0] * h
    for exponent in subset:
        exponent %= n
        if exponent < h:
            coordinates[exponent] += 1
        else:
            coordinates[exponent - h] -= 1
    return coordinates


def cyclotomic_norm(n: int, subset: tuple[int, ...]) -> int:
    h = n // 2
    coordinates = cyclotomic_coordinates(n, subset)
    multiplication = [[0] * h for _ in range(h)]
    for column in range(h):
        for basis_index, coefficient in enumerate(coordinates):
            exponent = basis_index + column
            if exponent < h:
                multiplication[exponent][column] += coefficient
            else:
                multiplication[exponent - h][column] -= coefficient
    return bareiss_det(multiplication)


def antipodal_count(n: int, subset: tuple[int, ...]) -> int:
    support = set(subset)
    h = n // 2
    return sum(1 for exponent in subset if (exponent + h) % n in support)


def odd_closure_size(n: int, p: int, w: int) -> int:
    closure: set[int] = set()
    for seed in range(1, w):
        value = seed % n
        while value not in closure:
            closure.add(value)
            value = value * p % n
    return sum(value % 2 for value in closure)


class FiniteField:
    def __init__(self, p: int, degree: int, nonsquare: int = 0) -> None:
        self.p = p
        self.degree = degree
        self.nonsquare = nonsquare

    def elements(self) -> list[tuple[int, int]]:
        if self.degree == 1:
            return [(a, 0) for a in range(self.p)]
        return [(a, b) for a in range(self.p) for b in range(self.p)]

    def add(
        self, left: tuple[int, int], right: tuple[int, int]
    ) -> tuple[int, int]:
        return ((left[0] + right[0]) % self.p, (left[1] + right[1]) % self.p)

    def mul(
        self, left: tuple[int, int], right: tuple[int, int]
    ) -> tuple[int, int]:
        if self.degree == 1:
            return (left[0] * right[0] % self.p, 0)
        return (
            (left[0] * right[0] + self.nonsquare * left[1] * right[1])
            % self.p,
            (left[0] * right[1] + left[1] * right[0]) % self.p,
        )

    def power(self, value: tuple[int, int], exponent: int) -> tuple[int, int]:
        answer = (1, 0)
        while exponent:
            if exponent & 1:
                answer = self.mul(answer, value)
            value = self.mul(value, value)
            exponent //= 2
        return answer

    def primitive_root(self, n: int) -> tuple[int, int]:
        for candidate in self.elements()[1:]:
            if self.power(candidate, n) == (1, 0) and self.power(
                candidate, n // 2
            ) != (1, 0):
                return candidate
        raise AssertionError(f"no primitive {n}-th root in registered field")


def moments_vanish(
    field: FiniteField,
    root: tuple[int, int],
    n: int,
    subset: tuple[int, ...],
    w: int,
) -> bool:
    for moment in range(1, w):
        total = (0, 0)
        for exponent in subset:
            total = field.add(
                total, field.power(root, moment * exponent % n)
            )
        if total != (0, 0):
            return False
    return True


def check_archimedean() -> dict[str, int]:
    checks = 0
    tight_nonzero = 0
    for n, sizes in ((8, range(0, 9)), (16, (3,))):
        h = n // 2
        for size in sizes:
            for subset in itertools.combinations(range(n), size):
                norm = cyclotomic_norm(n, subset)
                residual = size - antipodal_count(n, subset)
                assert norm * norm <= residual**h
                checks += 1
                if norm and norm * norm == residual**h:
                    tight_nonzero += 1
    assert checks == 2**8 + comb(16, 3)
    assert tight_nonzero > 0
    return {"checks": checks, "tight_nonzero": tight_nonzero}


def check_finite_fields() -> dict[str, object]:
    cases = (
        (8, FiniteField(3, 2, 2), range(1, 8), range(2, 6)),
        (16, FiniteField(17, 1), range(1, 7), range(2, 6)),
        (16, FiniteField(7, 2, 3), range(1, 7), range(2, 6)),
    )
    records: list[dict[str, object]] = []
    bad_solutions = 0
    divisibility_checks = 0
    exact_exponent_witnesses = 0
    for n, field, sizes, windows in cases:
        root = field.primitive_root(n)
        case_bad = 0
        for size in sizes:
            for subset in itertools.combinations(range(n), size):
                norm = cyclotomic_norm(n, subset)
                if norm == 0:
                    continue
                residual = size - antipodal_count(n, subset)
                for w in windows:
                    if not moments_vanish(field, root, n, subset, w):
                        continue
                    exponent = odd_closure_size(n, field.p, w)
                    divisor = field.p**exponent
                    assert norm % divisor == 0
                    assert norm * norm <= residual ** (n // 2)
                    assert divisor * divisor <= residual ** (n // 2)
                    bad_solutions += 1
                    case_bad += 1
                    divisibility_checks += 1
                    if norm % (divisor * field.p):
                        exact_exponent_witnesses += 1
        records.append(
            {
                "n": n,
                "p": field.p,
                "degree": field.degree,
                "root": list(root),
                "bad_solutions": case_bad,
            }
        )
    assert bad_solutions > 0
    assert exact_exponent_witnesses > 0
    return {
        "cases": records,
        "bad_solutions": bad_solutions,
        "divisibility_checks": divisibility_checks,
        "exact_exponent_witnesses": exact_exponent_witnesses,
    }


def log2_decimal(value: int) -> Decimal:
    return Decimal(value).ln() / Decimal(2).ln()


def crossing_margin(w: int, characteristic_bits: int) -> Decimal:
    n = 2**41
    r_prime = 2**40 - w
    coefficient = (w - 1 + 1) // 2
    return Decimal(coefficient * characteristic_bits) - Decimal(n // 4) * log2_decimal(
        r_prime
    )


def last_unexcluded(characteristic_bits: int) -> int:
    low = 2**34
    high = 2**39
    if crossing_margin(high, characteristic_bits) <= 0:
        return high
    while low < high:
        middle = (low + high + 1) // 2
        if crossing_margin(middle, characteristic_bits) <= 0:
            low = middle
        else:
            high = middle - 1
    return low


def check_threshold_and_tower() -> dict[str, object]:
    getcontext().prec = 80
    last_safe_256 = last_unexcluded(256)
    last_safe_128 = last_unexcluded(128)
    last_safe_64 = last_unexcluded(64)
    assert last_safe_256 == 170_752_922_587
    assert crossing_margin(last_safe_256, 256) <= 0
    assert crossing_margin(last_safe_256 + 1, 256) > 0
    assert last_safe_128 > last_safe_256
    assert last_safe_64 == 2**39

    tower_checks = 0
    for v in range(2, 12):
        w = 2**v
        base = (w - 1 + 1) // 2
        for a in range(v):
            reduced = (w - 1) // 2**a
            coefficient = (reduced + 1) // 2
            assert 2**a * coefficient == base
            tower_checks += 1

    w = 6
    base = (w - 1 + 1) // 2
    reduced = (w - 1) // 2
    deeper_scaled = 2 * ((reduced + 1) // 2)
    assert deeper_scaled < base

    bracket_size = 2**39 - 2**34 + 1
    excluded = 2**39 - last_safe_256
    percentage = Decimal(100 * excluded) / Decimal(bracket_size)
    return {
        "last_unexcluded_256": last_safe_256,
        "first_excluded_256": last_safe_256 + 1,
        "excluded_percentage_256": str(percentage.quantize(Decimal("0.0001"))),
        "last_unexcluded_128": last_safe_128,
        "last_unexcluded_64": last_safe_64,
        "power_two_tower_checks": tower_checks,
        "arbitrary_window_counterexample": {
            "w": w,
            "base_scaled_coefficient": base,
            "a1_scaled_coefficient": deeper_scaled,
        },
    }


def run_audit() -> dict[str, object]:
    archimedean = check_archimedean()
    finite_fields = check_finite_fields()
    threshold_and_tower = check_threshold_and_tower()
    return {
        "schema": "cs-independent-transport-audit-v1",
        "status": "PASS",
        "archimedean": archimedean,
        "finite_fields": finite_fields,
        "threshold_and_tower": threshold_and_tower,
        "tamper_selftests": {
            "stronger_divisibility_rejected": finite_fields[
                "exact_exponent_witnesses"
            ]
            > 0,
            "stronger_archimedean_ceiling_rejected": archimedean[
                "tight_nonzero"
            ]
            > 0,
            "floor_free_tower_shortcut_rejected": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = run_audit()
    if args.tamper_selftest:
        assert all(result["tamper_selftests"].values())
    if args.json:
        print(json.dumps(result, sort_keys=True))
    else:
        print("CS_INDEPENDENT_AUDIT_PASS")
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
