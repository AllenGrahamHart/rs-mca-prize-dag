#!/usr/bin/env python3
"""Verify the cell-5 exceptional-fiber router census."""

import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
sys.path.insert(0, str(EXPERIMENTS))
import check_rate_half_kb_positive_433_1a_cell5_pair_guard_norms as guards
import check_rate_half_kb_positive_433_1a_cell5_specialization_poles as poles


guard_candidates = guards.verify()
pole_roots = poles.verify()
forbidden = {0, 1, poles.PRIME - 1, 16711679, poles.PRIME - 16711679}
candidates = sorted(guard_candidates | (pole_roots - forbidden))
assert len(guard_candidates) == 14
assert len(pole_roots - forbidden) == 56
assert len(candidates) == 69
digest = hashlib.sha256(",".join(map(str, candidates)).encode()).hexdigest()
assert digest == "bd64dc238bb3dcc4491d7d7b856078871336571cbdd5df3343014f8198cfe1d4"
print(
    "positive 433-1a cell-5 exceptional-fiber router verified "
    f"guard=14 poles=56 union=69 sha256={digest}"
)
