#!/usr/bin/env python3
"""Test fixed-mixed degree-five q-slice survivors against full quotients."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import flint


HERE = Path(__file__).resolve().parent
BASE = (
    HERE / "kb_c2_112_aligned_positive_unramified_fixed_swap_full_quotient_probe.py"
)
BASE_SHA256 = "0f750b5486a32db2df33c56b41c80d99d3c67eee21f0a74e8507159166efb775"
SURVIVORS = (
    HERE / "kb_c2_112_aligned_positive_unramified_fixed_mixed_degree5_survivors.json"
)
SURVIVORS_SHA256 = "8ec4e97be7cf2adebe40a450ada0b385268686f44566ca520c964896e53fffe9"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_module(path: Path, digest: str, name: str):
    require(hashlib.sha256(path.read_bytes()).hexdigest() == digest, f"{name} hash")
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"{name} loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    require(flint.__version__ == "0.9.0", "python-flint version")
    require(
        hashlib.sha256(SURVIVORS.read_bytes()).hexdigest() == SURVIVORS_SHA256,
        "survivor hash",
    )
    base = load_module(BASE, BASE_SHA256, "fixed_full_quotient")
    common = base.load_module(base.BASE, base.BASE_SHA256, "fixed_common")
    source = common.load_module(
        common.SOURCE, common.SOURCE_SHA256, "positive_qslice"
    )
    helpers = common.load_module(
        common.HELPERS, common.HELPERS_SHA256, "full_quotient_helpers"
    )
    payload = json.loads(SURVIVORS.read_text(encoding="ascii"))
    require(payload["allocation"] == "mixed", "allocation")
    require(len(payload["survivors"]) == 4, "survivor count")
    outcomes = [
        base.run_record(
            common, source, helpers, record, allocation="mixed"
        )
        for record in payload["survivors"]
    ]
    rejected = sum(not (first and second) for first, second in outcomes)
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_MIXED_DEGREE5_"
        f"FULL_QUOTIENT_PROBE_PASS tested=4 rejected={rejected} "
        f"survived={len(outcomes) - rejected}",
        flush=True,
    )


if __name__ == "__main__":
    main()
