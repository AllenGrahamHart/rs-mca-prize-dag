#!/usr/bin/env python3
"""Hash-pinned dispatcher for the mixed other-xi certificate."""

from __future__ import annotations

import hashlib
import runpy
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
DATA = NODE / "data"
NOTES = ROOT / "critical/nodes/rate_half_band_closure/notes"
HELPERS = {
    "shared": NOTES / "kb_c2_112_near_moving_template_probe.py",
    "source": NOTES / "kb_c2_112_near_moving_other_probe.py",
    "ratio": NOTES / "kb_c2_112_near_moving_other_mixed_ratio.py",
    "flint": NOTES / "kb_c2_112_near_moving_other_mixed_flint.py",
    "classify": NOTES / "kb_c2_112_near_moving_other_cached_classify.py",
    "audit": NOTES / "kb_c2_112_near_moving_other_mixed_audit.py",
}
EXPECTED_HELPERS = {
    "shared": "deb385db95bf5737a7eef419af359714829c19b5a92a63d087f0fc3451afd32c",
    "source": "ef0ddd499a403abdc34b5fa6e83cbb38a444672c6e8fac7d59ea865d12ec19d1",
    "ratio": "8f0c8f827f657580ffae27c22096d4b0c2998a824d271f7b59be9868b12a9d84",
    "flint": "4c6915f9940d96324524f9691fa08580129a65b5eac7696e5a5e5ad1b24e02d8",
    "classify": "260b2431c04af60947232f8cd0c482ebbfc84440b40bf255b8b4a6b24f85e782",
    "audit": "ce96aa3e8a48c90cef9f5e921a691cba389905dd7aabee36d123457b850404af",
}
EXPECTED_DATA_COUNT = 26
EXPECTED_DATA_TREE = "5caec0e6c529230e847058357bd451730e7590a914cad0eba8e4dc628893314d"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def data_tree() -> tuple[int, str]:
    files = sorted(
        (path for path in DATA.iterdir() if path.is_file()),
        key=lambda path: path.name,
    )
    digest = hashlib.sha256()
    for path in files:
        digest.update(
            path.name.encode("ascii") + b"\0"
            + hashlib.sha256(path.read_bytes()).digest()
        )
    return len(files), digest.hexdigest()


def check_hashes() -> None:
    for name, path in HELPERS.items():
        if sha(path) != EXPECTED_HELPERS[name]:
            raise RuntimeError(f"helper hash: {name}")
    count, digest = data_tree()
    if count != EXPECTED_DATA_COUNT or digest != EXPECTED_DATA_TREE:
        raise RuntimeError("data tree")


def audit(mode: str) -> None:
    check_hashes()
    sys.argv = [
        str(HELPERS["audit"]), mode, "--data-dir", str(DATA),
    ]
    runpy.run_path(str(HELPERS["audit"]), run_name="__main__")


def classify(index: int) -> None:
    if not 0 <= index < 22:
        raise RuntimeError("classification shard")
    check_hashes()
    if index == 21:
        sys.argv = [
            str(HELPERS["ratio"]), "quadratic-sextic",
            "--cache-dir", str(DATA),
        ]
        runpy.run_path(str(HELPERS["ratio"]), run_name="__main__")
        print(
            "KB_C2_112_NEAR_MOVING_OTHER_MIXED_CLASSIFY_21_PASS",
            flush=True,
        )
        return
    sys.argv = [
        str(HELPERS["classify"]), "mixed", str(index),
        "--cache-dir", str(DATA),
    ]
    runpy.run_path(str(HELPERS["classify"]), run_name="__main__")
    print(
        f"KB_C2_112_NEAR_MOVING_OTHER_MIXED_CLASSIFY_{index}_PASS",
        flush=True,
    )


if __name__ == "__main__":
    check_hashes()
    print("KB_C2_112_NEAR_MOVING_OTHER_MIXED_DISPATCH_PASS")
