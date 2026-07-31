#!/usr/bin/env python3
"""Hash-pinned dispatcher for the near-negative q-slice certificate."""

from __future__ import annotations

import hashlib
import runpy
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NOTES = ROOT / "critical/nodes/rate_half_band_closure/notes"
HELPERS = {
    "aligned": NOTES / "kb_c2_112_negative_qslice_locus.py",
    "near": NOTES / "kb_c2_112_near_negative_qslice_locus.py",
    "audit_source": (
        ROOT
        / "background/nodes/"
        "rate_half_kb_m2_r4_diagonal_c2_112_source_line_"
        "aligned_negative_q_slice_exclusion/verify_audit.py"
    ),
}
EXPECTED = {
    "aligned": "bfc1404f30ee9a36b214baa71527fa48a837f0550842d26c1d7d63cca1523d66",
    "near": "1421ffa838e94a3613f997e9b23de0a95c0238ef29b90206422633fa3d89eeb9",
    "audit_source": "b7832cab560f9e8e39014327cd6196d1111f70bd164c6b0467212cc208f19e98",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_hashes() -> None:
    for name, path in HELPERS.items():
        if sha(path) != EXPECTED[name]:
            raise RuntimeError(f"helper hash: {name}")


def run(arguments: list[str]) -> None:
    check_hashes()
    sys.path.insert(0, str(NOTES))
    try:
        sys.argv = [str(HELPERS["near"]), *arguments]
        runpy.run_path(str(HELPERS["near"]), run_name="__main__")
    finally:
        sys.path.pop(0)


def template() -> None:
    run(["fixed-moving", "--compare-templates"])


def branch(name: str) -> None:
    if name not in ("a", "tau-a", "other"):
        raise RuntimeError("near-negative branch")
    run([
        "fixed-moving", "--xi", name,
        "--eliminate", "--fibers", "--modular-saturate",
    ])


if __name__ == "__main__":
    check_hashes()
    print("KB_C2_112_NEAR_NEGATIVE_DISPATCH_PASS")
