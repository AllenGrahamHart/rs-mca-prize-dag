#!/usr/bin/env python3
"""Hash-pinned dispatcher for one ramified saturation shard."""

from __future__ import annotations

import hashlib
import runpy
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NOTES = ROOT / "critical/nodes/rate_half_band_closure/notes"
SOURCES = {
    "generator": NOTES / "kb_c2_112_positive_qslice_symmetric.py",
    "saturation": NOTES / "kb_c2_112_aligned_positive_ramified_saturation.py",
}
EXPECTED = {
    "generator": "bc5f958f834d978b2bb2e054cafd8ee47f46469b26c9798257f10436cc8eb45d",
    "saturation": "bf420a62be9df72dd52f81ff7bc8052f322f22ff3008b33b29548a076a13409d",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_hashes():
    for name, path in SOURCES.items():
        if digest(path) != EXPECTED[name]:
            raise RuntimeError(f"source hash: {name}")


def run(template, allocation):
    if template not in ("fixed-moving", "moving-moving"):
        raise RuntimeError("template")
    if allocation not in ("same", "swap", "mixed"):
        raise RuntimeError("allocation")
    check_hashes()
    sys.argv = [str(SOURCES["saturation"]), template, allocation]
    runpy.run_path(str(SOURCES["saturation"]), run_name="__main__")


if __name__ == "__main__":
    check_hashes()
    print("KB_C2_112_ALIGNED_POSITIVE_RAMIFIED_DISPATCH_PASS")
