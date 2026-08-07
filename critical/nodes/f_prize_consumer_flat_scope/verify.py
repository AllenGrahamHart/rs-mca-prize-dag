#!/usr/bin/env python3
"""Verify the strict Conjecture-F caller inventory and interface split."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def load_node(node_id: str) -> dict:
    paths = list((ROOT / "critical" / "nodes" / node_id).glob("node.json"))
    paths += list((ROOT / "background" / "nodes" / node_id).glob("node.json"))
    assert len(paths) == 1, (node_id, paths)
    return json.loads(paths[0].read_text())


def main() -> None:
    callers: set[str] = set()
    for base in (ROOT / "critical" / "nodes", ROOT / "background" / "nodes"):
        for path in base.glob("*/node.json"):
            data = json.loads(path.read_text())
            if any(edge.get("from") == "conj_f" for edge in data.get("requires", [])):
                callers.add(data["node"]["id"])

    assert callers == {"imgfib", "spi_point_counting"}, callers

    scope = load_node("f_prize_consumer_flat_scope")
    scope_parents = {edge["from"] for edge in scope["requires"]}
    assert scope_parents == {
        "f_imgfib_consumer_descriptor",
        "f_spi_hankel_consumer_descriptor",
    }

    imgfib = load_node("imgfib")
    imgfib_parents = {edge["from"] for edge in imgfib["requires"]}
    assert {"conj_f", "l1_mixed_petal_amplification"} <= imgfib_parents

    pade = load_node("l1_full_locator_pade_section_all_cofactors")
    rootfree = load_node("l1_rootfree_rational_q_projective_packing")
    assert pade["node"]["status"] == "PROVED"
    assert rootfree["node"]["status"] == "PROVED"
    assert "no cardinality" in pade["node"]["statement"].lower()
    assert "projective split-locator intersection" in rootfree["node"]["statement"].lower()

    print("F_PRIZE_CONSUMER_SCOPE_PASS callers=2 list=target spi=proved")


if __name__ == "__main__":
    main()
