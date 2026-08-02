#!/usr/bin/env python3
"""Hostile mutations for the dynamic map-pole exclusion packet."""

import json
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
sys.path.insert(0, str(EXPERIMENTS))
import check_rate_half_kb_positive_433_1a_cell5_dynamic_fiber_replay as checker


def rejected(payload, kind):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
        json.dump(payload, handle)
        handle.flush()
        try:
            if kind == "replay":
                checker.verify(replay_path=Path(handle.name))
            else:
                checker.verify(regularized_path=Path(handle.name))
        except checker.CertificateError:
            return True
    return False


replay = json.loads(checker.REPLAY.read_text())
replay["results"][0]["rows"][0]["gcd"] = [[1], [1]]
assert rejected(replay, "replay")

regularized = json.loads(checker.REGULARIZED.read_text())
regularized[0]["entries"][0]["numerator"][0] = (
    regularized[0]["entries"][0]["numerator"][0] + 1
) % checker.PRIME
assert rejected(regularized, "regularized")

print("positive 433-1a cell-5 dynamic map-pole exclusion audit verified mutations=2")
