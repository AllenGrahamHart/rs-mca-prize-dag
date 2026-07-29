#!/usr/bin/env python3
"""Verify the cofactor-514 Hermite exclusion of two magnitude profiles."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


sys.set_int_max_str_digits(100_000)


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_s18_m514_hermite_two_profile_exclusion"
PARENTS = {
    "e1_profile210_m514_parity_trace_cap",
    "e1_prize_field_floor_even_norm_exclusion",
}
TARGETS = {
    "e1_profile018_m514_five_ideal_occupancy",
    "e1_official_low_square_mass_pair_budget",
}
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
COFACTOR = 514
ROWS = (
    {
        "profile": (9, 1, 2, 0),
        "v": 18,
        "M": 10,
        "a": (-9, 5),
        "weights": (50, 9, 59),
        "values": ((81, 5), (28, 1)),
        "margin_bits": 23060,
        "margin_sha256": "4c4dd3fc2f0c3320e89234a2567c3fc49427e4c3dbedad23bf7934b6c7000043",
    },
    {
        "profile": (11, 7, 1, 0),
        "v": 22,
        "M": 18,
        "a": (-11, 9),
        "weights": (162, 11, 173),
        "values": ((151, 9), (36, 1)),
        "margin_bits": 78695,
        "margin_sha256": "7006de3798e0eee8522b6e414d94945a8075c4d5a480692bc9a3da6d9d856602",
    },
)


def check_row(row: dict[str, object]) -> None:
    energy, n1, n2, n3 = row["profile"]
    assert energy == n1 + 4 * n2 + 9 * n3
    l1 = n1 + 2 * n2 + 3 * n3
    assert row["v"] == 2 * energy and row["M"] == 2 * l1

    a_num, a_den = row["a"]
    assert a_num * row["M"] == -row["v"] * a_den
    weight_a, weight_m, denominator = row["weights"]
    assert weight_a + weight_m == denominator
    assert weight_a * a_num + weight_m * row["M"] * a_den == 0
    assert weight_a * a_num**2 + weight_m * (row["M"] * a_den) ** 2 == (
        denominator * row["v"] * a_den**2
    )

    (low_num, low_den), (high_num, high_den) = row["values"]
    assert low_num * a_den == 18 * low_den * a_den + a_num * low_den
    assert high_num == (18 + row["M"]) * high_den

    left = low_num ** (64 * weight_a) * high_num ** (64 * weight_m)
    right = (
        low_den ** (64 * weight_a)
        * high_den ** (64 * weight_m)
        * (COFACTOR * P_MIN) ** denominator
    )
    assert left < right
    margin = right - left
    assert margin.bit_length() == row["margin_bits"]
    assert hashlib.sha256(str(margin).encode("ascii")).hexdigest() == row["margin_sha256"]


def main() -> None:
    for row in ROWS:
        check_row(row)

    node_dir = ROOT / "background/nodes" / NODE
    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("(9;1,2,0)", "(11;7,1,0)", "13"):
        assert text in statement
    for text in ("23060", "78695", "Hermite"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    for target in TARGETS:
        assert nodes[target]["status"] == "TARGET"
        assert (NODE, target, "ev") in edges

    print(
        "E1_S18_M514_HERMITE_TWO_PROFILE_EXCLUSION_PASS "
        "profiles=2 survivors=13 margin_bits=23060,78695"
    )


if __name__ == "__main__":
    main()
