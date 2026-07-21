#!/usr/bin/env python3
"""Verify the prize primitive rank-two shell band."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_primitive_rank_two_shell_band"
PARENT = "xr_higher_rank_rank_two_shell_maxwell_router"
CONSUMER = "xr_highcore_collision_count"
ROWS = (
    ("prize-1/4", 3 * 2**39, 2**33 + 1, 384, 22_428_333, 34_135_455_048, 95_708, -51_362),
    ("prize-1/8", 7 * 2**38, 2**33 + 1, 448, 19_217_048, 34_167_567_898, 166_834, -33_420),
    ("prize-1/16", 15 * 2**37, 2**32 + 1, 960, 4_478_600, 17_135_083_194, 177_042, -743_596),
)


def bound(h: int, d: int, t: int) -> int:
    return t * h + (1 - d) * t * t + (d - 3) * t + 2 * (d + 1)


def arithmetic_checks() -> int:
    checked = 0
    for _, r, h, expected_l, d_max, b4, bl, next_bl in ROWS:
        l_max = (2 * r + h - 1) // h
        assert l_max == expected_l
        assert bound(h, d_max, 4) == b4 > 0
        assert bound(h, d_max, l_max) == bl > 0
        assert bound(h, d_max + 1, l_max) == next_bl < 0
        for t in range(4, l_max + 1):
            assert bound(h, d_max, t) > 0
            assert bound(h, d_max, t + 1) - 2 * bound(h, d_max, t) + bound(h, d_max, t - 1) == 2 * (1 - d_max)
            assert bound(h, d_max + 1, t) - bound(h, d_max, t) == -(t - 2) * (t + 1)
            checked += 1
    return checked


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARENT]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "L_max=floor((2R+h-1)/h)",
        "22,428,333",
        "19,217,048",
        "4,478,600",
        "concavein`t`",
        "2<=d<=D_row",
        "doesnotremoveproperlocal",
    ):
        assert marker in statement


def main() -> None:
    checked = arithmetic_checks()
    packet_check()
    print(f"XR_PRIZE_PRIMITIVE_RANK_TWO_SHELL_BAND_PASS cells={checked}")


if __name__ == "__main__":
    main()
