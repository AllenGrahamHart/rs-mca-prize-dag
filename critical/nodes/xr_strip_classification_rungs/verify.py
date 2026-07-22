#!/usr/bin/env python3
"""Replay the two independent XR strip/classification audits."""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
AUDITS = (
    (
        ROOT / "critical/nodes/xr_smallcore_spread_count/notes/"
        "audit_consumption_replay_20260710.py",
        "c39442d16fcbe86bbfd97f245de970dc729d0e257514c6d4f9f74c9a8c7fac56",
        69,
        "XR_CONSUMPTION_REPLAY_PASS",
        10,
    ),
    (
        ROOT / "critical/nodes/xr_smallcore_spread_count/notes/"
        "audit_p8p9_local_20260710.py",
        "e34e926087feebbb07c719bf877633f50d158843f8e74fb628e4695d701940af",
        88,
        "XR_P8P9_LOCAL_PASS",
        45,
    ),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    for path, expected_hash, expected_passes, tail, timeout in AUDITS:
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        require(actual_hash == expected_hash, f"hash drift: {path.name}")
        completed = subprocess.run(
            [sys.executable, str(path)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        require(completed.returncode == 0, completed.stdout + completed.stderr)
        require(completed.stderr == "", f"unexpected stderr: {path.name}")
        lines = completed.stdout.splitlines()
        require(
            sum(line.startswith("PASS ") for line in lines) == expected_passes,
            f"PASS count drift: {path.name}",
        )
        require(
            not any(line.startswith("FAIL ") for line in lines),
            f"failed audit: {path.name}",
        )
        require(completed.stdout.rstrip().endswith(tail), f"bad tail: {path.name}")
    print(
        "XR_STRIP_CLASSIFICATION_RUNGS_PASS "
        "official_checks=69 toy_checks=88 forced_pairs=4662 pinned_audits=2"
    )


if __name__ == "__main__":
    main()
