#!/usr/bin/env python3
"""Verify the exact O0b matching-resultant projective-chart split."""

import hashlib
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_o0b_resultant_projective_charts.py"
)
COMPILER = (
    ROOT / "experiments/prize_resolution" /
    "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
)
SCRIPT_SHA256 = "fed6f3746dc7ca34db12b19a9b2b06330d15655ede9b4e14cffab88aaf8d99e6"
COMPILER_SHA256 = "048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_script():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "identity-script custody")
    require(hashlib.sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256,
            "compiler custody")
    spec = importlib.util.spec_from_file_location("resultant_charts", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    module = load_script()
    module.verify_resultant_identity()
    module.verify_chart_implications()
    masks = module.verify_chart_cover()
    count = module.verify_compiler_resultants()
    require(count == 3 and len(masks) == 8, "resultant/chart census")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_RESULTANT_PROJECTIVE_CHARTS_VERIFY_PASS "
          "resultants=3 charts=8")


if __name__ == "__main__":
    main()
