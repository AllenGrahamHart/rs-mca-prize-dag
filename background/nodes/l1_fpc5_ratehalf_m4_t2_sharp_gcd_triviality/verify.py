#!/usr/bin/env python3
"""Finite-field replay of sharp guarded-flat gcd triviality."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HELPER = (
    Path(__file__).resolve().parents[1]
    / "l1_fpc5_ratehalf_m4_t2_sharp_projective_flat_descriptor"
    / "verify.py"
)


def load_helper():
    spec = importlib.util.spec_from_file_location("sharp_flat_helper", HELPER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def interpolate(module, points: list[int], values: list[int]) -> list[int]:
    assert len(points) == len(values)
    out = [0]
    for index, point in enumerate(points):
        numerator = [1]
        denominator = 1
        for other_index, other in enumerate(points):
            if other_index == index:
                continue
            numerator = module.mul(numerator, [(-other) % module.P, 1])
            denominator = denominator * (point - other) % module.P
        term = module.scale(
            numerator, values[index] * pow(denominator, -1, module.P)
        )
        out = module.add(out, term)
    return out


def main() -> None:
    module = load_helper()
    checked_roots = 0
    for ell in range(3, 11):
        m = ell - 3
        background = list(range(1, m + 1))
        petal_1 = list(range(20, 20 + ell))
        petal_2 = list(range(50, 50 + ell))
        l0 = module.locator(background)
        l1 = module.locator(petal_1)
        l2 = module.locator(petal_2)
        c1, c2 = 2, 5

        variables_per_side = m + 1
        rows = []
        for point in background:
            row = [
                c2 * module.evaluate(l1, point) * pow(point, degree, module.P)
                % module.P
                for degree in range(variables_per_side)
            ]
            row += [
                -c1 * module.evaluate(l2, point) * pow(point, degree, module.P)
                % module.P
                for degree in range(variables_per_side)
            ]
            rows.append([value % module.P for value in row])
        cofactor_basis = module.nullspace(rows, 2 * variables_per_side)
        assert len(cofactor_basis) == ell - 1

        inverse_gap = pow(c2 - c1, -1, module.P)
        f_basis = []
        for vector in cofactor_basis:
            a1 = vector[:variables_per_side]
            a2 = vector[variables_per_side:]
            f_poly = module.scale(
                module.add(
                    module.mul(l1, a1), module.scale(module.mul(l2, a2), -1)
                ),
                inverse_gap,
            )
            f_basis.append(f_poly)
        assert module.rank(f_basis) == ell - 1

        easy_1 = module.scale(module.mul(l0, l1), inverse_gap)
        easy_2 = module.scale(module.mul(l0, l2), -inverse_gap)
        assert module.in_span(easy_1, f_basis, 2 * ell - 2)
        assert module.in_span(easy_2, f_basis, 2 * ell - 2)
        assert module.monic_gcd(easy_1, easy_2) == l0

        for selected in background:
            values = [
                c2
                * module.evaluate(l1, point)
                * pow(c1 * module.evaluate(l2, point), -1, module.P)
                % module.P
                for point in background
            ]
            a1 = [1]
            a2 = interpolate(module, background, values)
            assert len(a2) - 1 <= m - 1
            for point in background:
                assert (
                    c2 * module.evaluate(l1, point) * module.evaluate(a1, point)
                    - c1 * module.evaluate(l2, point) * module.evaluate(a2, point)
                ) % module.P == 0
            f_poly = module.scale(
                module.add(
                    module.mul(l1, a1), module.scale(module.mul(l2, a2), -1)
                ),
                inverse_gap,
            )
            assert module.evaluate(f_poly, selected) == (
                -module.evaluate(l1, selected) * pow(c1, -1, module.P)
            ) % module.P
            assert module.evaluate(f_poly, selected) != 0
            checked_roots += 1

        assert module.gcd_basis(f_basis) == [1]

    official_k = 2**40
    official_ell = (official_k + 4) // 5
    assert 5 * official_ell == official_k + 4
    print(
        "L1_FPC5_SHARP_GCD_TRIVIALITY_PASS "
        f"cells=8 avoided_background_roots={checked_roots} "
        f"official_ell={official_ell}"
    )


if __name__ == "__main__":
    main()
