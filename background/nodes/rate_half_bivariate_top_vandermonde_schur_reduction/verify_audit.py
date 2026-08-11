#!/usr/bin/env python3
"""Audit the Schur reduction on all ten published m=1 matrices."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PROBE = ROOT / "experiments/prize_resolution/rh_bivariate_m1_rank_probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("m1_probe_for_schur", PROBE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    probe = load_probe()
    representatives = {}
    for slope, support in probe.SUPPORTS.items():
        target = tuple(
            (a + slope * b) % probe.PRIME for a, b in zip(probe.Y0, probe.Y1)
        )
        representatives[slope] = probe.solve_support(support, target)

    checks = 0
    slopes = tuple(probe.SUPPORTS)
    for first_index, first in enumerate(slopes):
        for second in slopes[first_index + 1 :]:
            matrix, _, _ = probe.pair_matrix(first, second, representatives)
            top_rows = [2, 5, 8, 11, 14]
            top_slice = [matrix[row] for row in top_rows]
            assert probe.matrix_rank(top_slice) == 5
            assert probe.matrix_rank(matrix) == 5
            assert len(matrix[0]) - 5 == 1
            checks += 1

    print(
        "RATE_HALF_BIVARIATE_TOP_VANDERMONDE_SCHUR_REDUCTION_AUDIT_PASS "
        f"m1_pairs={checks} residual_width=1 residual_rank=0"
    )


if __name__ == "__main__":
    main()
