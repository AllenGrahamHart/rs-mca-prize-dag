#!/usr/bin/env python3
"""Hash-pinned dispatcher for one projective-boundary saturation shard."""

import hashlib
import runpy
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SOURCE = (
    ROOT
    / "critical/nodes/rate_half_band_closure/notes/"
    "kb_c2_112_near_positive_projective_boundary.py"
)
EXPECTED = "34159386a24e7ae1a6bd62a75f4654a9de81a49d2a1beda2d03f5dbf9b23eaeb"


def check_hash():
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != EXPECTED:
        raise RuntimeError("projective helper hash")


def run(arguments):
    check_hash()
    sys.argv = [str(SOURCE), *arguments]
    runpy.run_path(str(SOURCE), run_name="__main__")


if __name__ == "__main__":
    check_hash()
    print("KB_C2_112_NEAR_POSITIVE_PROJECTIVE_DISPATCH_PASS")
