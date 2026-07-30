#!/usr/bin/env python3
"""Recompute the A6 pair curve's two adjoint resultants."""

from __future__ import annotations

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PRODUCER = ROOT / "experiments/prize_resolution/rate_half_kb_m4_a6_542_pair_quotient.py"


def main() -> None:
    spec = importlib.util.spec_from_file_location("kb_m4_a6_542_elimination", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.derive_coordinates()
    print("RATE_HALF_KB_M4_A6_542_PAIR_QUOTIENT_ELIMINATION_PASS")


if __name__ == "__main__":
    main()
