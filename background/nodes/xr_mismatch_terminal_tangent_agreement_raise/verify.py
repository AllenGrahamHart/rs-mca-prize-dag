#!/usr/bin/env python3
"""Verify the XR terminal-tangent agreement raise."""

from __future__ import annotations

from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_mismatch_terminal_tangent_agreement_raise"
DEPENDENCIES = {
    "xr_mismatch_accumulated_locator_flag_normal_form",
    "xr_true_tangent_coordinate_injection",
}
CONSUMER = "xr_tangent_support_mismatch_bridge"


def finite_error_check() -> int:
    prime = 3
    length = 4
    checked = 0
    vectors = tuple(product(range(prime), repeat=length))
    for error_0 in vectors:
        for error_1 in vectors:
            common = sum(
                left == 0 and right == 0
                for left, right in zip(error_0, error_1)
            )
            if common == 0:
                continue
            for slope in range(prime):
                extra = sum(
                    (left != 0 or right != 0)
                    and (left + slope * right) % prime == 0
                    for left, right in zip(error_0, error_1)
                )
                if extra:
                    line_agreement = sum(
                        (left + slope * right) % prime == 0
                        for left, right in zip(error_0, error_1)
                    )
                    assert line_agreement >= common + 1
                    checked += 1
    return checked


def nesting_check() -> None:
    for length in range(1, 50):
        sizes = tuple(length - agreement + 1 for agreement in range(1, length + 2))
        assert all(left >= right for left, right in zip(sizes, sizes[1:]))
        assert sizes[-1] == 0


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "zinB_(A+1)(u,v)",
        "Z_tansubseteqB_(A+1)(u,v)",
        "Repeatingthisroutingcanraiseagreementatmost`n-A`times",
        "doesnotbound`B_(A+1)`",
    ):
        assert marker in statement


def main() -> None:
    checked = finite_error_check()
    nesting_check()
    packet_check()
    print(f"XR_MISMATCH_TERMINAL_TANGENT_AGREEMENT_RAISE_PASS cases={checked}")


if __name__ == "__main__":
    main()
