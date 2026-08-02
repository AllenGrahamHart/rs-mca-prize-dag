#!/usr/bin/env python3
"""Node verifier for the signed-pair primitive residue ledger."""

import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
for script in (
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization.py",
):
    runpy.run_path(
        str(ROOT / "experiments/prize_resolution" / script),
        run_name="__main__",
    )
