#!/usr/bin/env python3
"""Pin LIST's direct residual partition and absence of a Conjecture-F call."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def load(node_id: str) -> dict:
    paths = list((ROOT / "critical" / "nodes" / node_id).glob("node.json"))
    paths += list((ROOT / "background" / "nodes" / node_id).glob("node.json"))
    assert len(paths) == 1, (node_id, paths)
    return json.loads(paths[0].read_text())


def parents(node_id: str) -> set[str]:
    return {edge["from"] for edge in load(node_id).get("requires", [])}


def main() -> None:
    imgfib = load("imgfib")
    imgfib_parents = parents("imgfib")
    assert "conj_f" not in imgfib_parents
    assert {
        "petal_growth",
        "l1_full_petal_fpc5_payment",
        "l1_mixed_petal_amplification",
        "l1_program_frontier",
        "pma_exact_periodic_owner",
        "dyadic_profile_evaluation",
        "payment_completeness",
    } <= imgfib_parents

    fpc5 = load("l1_full_petal_fpc5_payment")
    # wave-48 repin (coordinator): the FPC5 leaf became a CONDITIONAL router over
    # three payment leaves at the official-cell decomposition; the open-leaf intent
    # is preserved by pinning the red child below.
    assert fpc5["node"]["status"] == "CONDITIONAL"
    req_ids = {r.get("from") for r in fpc5.get("requires", [])}
    assert {"l1_fpc5_ratehalf_m4_t3_split_slice_payment", "l1_fpc5_m4_t2_payment",
            "l1_fpc5_large_source_payment"} <= req_ids
    red_child = load("l1_fpc5_ratehalf_m4_t2_payment")
    assert red_child["node"]["status"] == "TARGET"
    fpc5_text = fpc5["node"]["statement"]
    for token in ("FPC5", "exactly three residual routers", "rate-quarter branch is proved"):
        assert token in fpc5_text, token

    composition = load("pma_full_petal_band_composition")
    assert composition["node"]["status"] == "PROVED"
    assert "remaining full-petal family" in composition["node"]["statement"]

    mixed = load("l1_mixed_petal_amplification")
    assert mixed["node"]["status"] == "TARGET"
    assert "mixed-petal or diffuse partial-petal" in mixed["node"]["statement"]

    callers = set()
    for base in (ROOT / "critical" / "nodes", ROOT / "background" / "nodes"):
        for path in base.glob("*/node.json"):
            data = json.loads(path.read_text())
            if any(edge.get("from") == "conj_f" for edge in data.get("requires", [])):
                callers.add(data["node"]["id"])
    assert callers == {"spi_point_counting"}, callers

    assert imgfib["node"]["status"] == "CONDITIONAL"
    print("F_IMGFIB_ROUTE_RETIREMENT_PASS callers=0 direct_reds=2 fpc5=exact")


if __name__ == "__main__":
    main()
