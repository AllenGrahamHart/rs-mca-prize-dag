#!/usr/bin/env python3
"""Hostile mutations for the raw-basis fiber exclusion."""

import json
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
sys.path.insert(0, str(EXPERIMENTS))
import check_rate_half_kb_positive_433_1a_cell5_raw_fiber_replay as checker


def rejected(payload, kind):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as handle:
        json.dump(payload, handle)
        handle.flush()
        try:
            if kind == "replay":
                checker.verify(replay_path=Path(handle.name))
            else:
                checker.verify(profile_path=Path(handle.name))
        except checker.CertificateError:
            return True
    return False


replay = json.loads(checker.REPLAY.read_text())
replay["results"][0]["matrices"]["b"][0][0] = (
    replay["results"][0]["matrices"]["b"][0][0] + 1
) % checker.PRIME
assert rejected(replay, "replay")

profile = json.loads(checker.PROFILE.read_text())
profile[3]["quotient_dimension"] = 24
assert rejected(profile, "profile")

print("positive 433-1a cell-5 raw-basis exclusion audit verified mutations=2")
