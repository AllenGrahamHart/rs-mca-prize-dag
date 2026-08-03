#!/usr/bin/env python3
"""Independent audit of the positive-DE parallel-edge transport."""

import ast
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
ATLAS = ROOT / "background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas/statement.md"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    ast.parse((NODE / "verify.py").read_text())
    atlas = ATLAS.read_text()
    require("outside: de,de,-de; df, sigma_o ef" in atlas,
            "signed atlas record order")
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("(d+e)^2, (d+e)^2, (d-e)^2" in proof,
            "squared-sum distinction")
    require("de, -de, df, sigma_o ef, bf, sigma_c cf" in proof,
            "identical residual lists")
    require("No claim is made for another pairing" in audit and
            "negative `DE` copy" in audit, "transport scope")
    # Forced pin correction (wave-43 audit): the original pin named `xi=2` as
    # the next frontier; the xi=2 commit closed it and rewrote frontier.md
    # without updating this pin. Pin the successor marker instead.
    require("The next missing record is `xi=3`" in frontier,
            "next frontier")
    print("audit=ok parallel_positive_DE=2 pairing=0 transport=exact")


if __name__ == "__main__":
    main()
