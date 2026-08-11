#!/usr/bin/env python3
"""Replay all ten m=1 bivariate matrix rank certificates."""

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CERTIFICATE = Path(__file__).with_name("certificate.json")
PROBE = ROOT / "experiments/prize_resolution/rh_bivariate_m1_rank_probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("rh_bivariate_m1_rank_probe", PROBE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    probe = load_probe()
    payload = json.loads(CERTIFICATE.read_text())
    assert payload["schema"] == "rate-half-bivariate-m1-rank-v1"
    assert payload["field"] == probe.PRIME == 17

    representatives = {}
    for slope, support in probe.SUPPORTS.items():
        target = tuple(
            (a + slope * b) % probe.PRIME for a, b in zip(probe.Y0, probe.Y1)
        )
        representatives[slope] = probe.solve_support(support, target)

    for record in payload["pairs"]:
        first, second = record["slopes"]
        matrix, kernel, support = probe.pair_matrix(first, second, representatives)
        assert list(support) == record["support"]
        assert probe.matrix_rank(matrix) == payload["rank"] == 5
        certificate = probe.rank_five_certificate(matrix)
        expected = (
            tuple(record["rows"]),
            record["omitted_column"],
            record["determinant"],
        )
        assert certificate == expected
        assert all(kernel)

    assert len(payload["pairs"]) == 10
    print("RATE_HALF_BIVARIATE_ROW_SURPLUS_ROUTE_FENCE_PASS pairs=10 rank=5")


if __name__ == "__main__":
    main()
