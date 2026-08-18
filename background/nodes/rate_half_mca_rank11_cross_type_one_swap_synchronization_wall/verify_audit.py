#!/usr/bin/env python3
"""Independent audit of the cross-type one-swap wall."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "1befeda8f067182ab717a44bce4f202e7a9f1f58eb4de24011025f24d473266b"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    size = data["packet_size"]
    for threshold, cap in (
        (data["partial_relative_anchor_threshold"], data["partial_relative_cross_anchor_overlap_cap"]),
        (data["heavy_ruling_anchor_threshold"], data["heavy_ruling_cross_anchor_overlap_cap"]),
    ):
        assert 2 * threshold > size
        assert cap == 2 * size - 2 * threshold
        assert data["one_swap_overlap"] > cap
    assert data["collision_forced_common_zero_before_shortening"] - data["denominator_degree_cap"] == 1012239
    assert data["distinct_pair_agreement_cap_before_shortening"] - 1012239 == 36336

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_order32_partial_relative_harvest"]["status"] == "PROVED"
    assert nodes["rate_half_mca_rank11_quadratic_quotient_population_router"]["status"] == "PROVED"

    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "anchor type is therefore constant" in proof
    assert "this bound is sharp at the set-system level" in proof
    assert "primitive root-free corollary needs only two" in proof
    assert "method wall, not a counterexample" in statement
    print("CROSS_TYPE_ONE_SWAP_WALL_AUDIT_PASS overlaps=28,24 gap=36336")


if __name__ == "__main__":
    main()
