#!/usr/bin/env python3
"""Adapt the exact support-disjoint witness analyzer to K'=87."""

from __future__ import annotations

import importlib.util
from pathlib import Path


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_module(
    "k87_residual_witness_base",
    Path(__file__).with_name(
        "rate_half_mca_rank11_k85_residual_witness_adjacent_payment.py"
    ),
)
BASE.KPRIME, BASE.Q, BASE.M = 87, 77, 67559
BASE.LEADER = 41460899125475443837881046685022762331499044695
BASE.CEILING = 41460914669043067085305042221812436226076443389


if __name__ == "__main__":
    BASE.main()
