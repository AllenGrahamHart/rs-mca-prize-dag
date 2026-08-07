#!/usr/bin/env python3
"""Finite-field rank replay for uniform guarded codimension."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HELPER = (
    Path(__file__).resolve().parents[1]
    / "l1_fpc5_ratehalf_m4_t2_sharp_projective_flat_descriptor"
    / "verify.py"
)


def load_helper():
    spec = importlib.util.spec_from_file_location("uniform_guard_helper", HELPER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_helper()
    cells = 0
    exact_boundary_cells = 0
    for ell in range(3, 10):
        l1 = module.locator(list(range(20, 20 + ell)))
        l2 = module.locator(list(range(50, 50 + ell)))
        c1, c2 = 2, 5
        for s in range(ell):
            variables_per_side = s + 1
            locator_degree = ell + s
            for r in range(s, ell):
                background = list(range(1, r + 1))
                rows = []
                for point in background:
                    row = [
                        c2
                        * module.evaluate(l1, point)
                        * pow(point, degree, module.P)
                        % module.P
                        for degree in range(variables_per_side)
                    ]
                    row += [
                        -c1
                        * module.evaluate(l2, point)
                        * pow(point, degree, module.P)
                        % module.P
                        for degree in range(variables_per_side)
                    ]
                    rows.append([value % module.P for value in row])

                constraint_rank = module.rank(rows)
                minimum_rank = min(r, s + 1)
                assert constraint_rank >= minimum_rank
                if r <= s + 1:
                    assert constraint_rank == r

                cofactor_basis = module.nullspace(rows, 2 * variables_per_side)
                expected_dimension = 2 * s + 2 - constraint_rank
                assert len(cofactor_basis) == expected_dimension

                inverse_gap = pow(c2 - c1, -1, module.P)
                f_basis = []
                for vector in cofactor_basis:
                    a1 = vector[:variables_per_side]
                    a2 = vector[variables_per_side:]
                    f_poly = module.scale(
                        module.add(
                            module.mul(l1, a1),
                            module.scale(module.mul(l2, a2), -1),
                        ),
                        inverse_gap,
                    )
                    assert len(f_poly) - 1 <= locator_degree
                    f_basis.append(f_poly)
                assert module.rank(f_basis) == expected_dimension

                codimension = locator_degree + 1 - expected_dimension
                assert codimension >= ell - 1
                if r == s:
                    assert expected_dimension == s + 2
                    assert codimension == ell - 1
                    exact_boundary_cells += 1
                else:
                    assert expected_dimension <= s + 1
                    assert codimension >= ell
                cells += 1

    official_k = 2**40
    official_ell = (official_k + 4) // 5
    assert 5 * official_ell == official_k + 4
    print(
        "L1_FPC5_UNIFORM_GUARDED_CODIMENSION_PASS "
        f"cells={cells} exact_boundary={exact_boundary_cells} "
        f"official_ell={official_ell}"
    )


if __name__ == "__main__":
    main()
