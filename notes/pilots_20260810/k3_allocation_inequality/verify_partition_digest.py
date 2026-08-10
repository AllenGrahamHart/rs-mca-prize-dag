#!/usr/bin/env python3
"""Scratch re-verification of the frozen K3 partition manifest digest.

Derived from background/nodes/rate_half_kb_v4_tangent_source_atom/verify.py
but with the dag.json read REMOVED (RAM law: never open dag.json).  Stdlib
only, exact integers only.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = (
    ROOT
    / "background/nodes/rate_half_kb_v4_tangent_source_atom/partition_contract.json"
)
DIGEST = "4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc"


def canonical(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    body = copy.deepcopy(contract)
    claimed = body.pop("partition_sha256")
    method = body.pop("partition_digest_method")
    actual = hashlib.sha256(canonical(body)).hexdigest()
    print("file_sha256      =",
          hashlib.sha256(CONTRACT.read_bytes()).hexdigest())
    print("digest_method    =", method)
    print("claimed          =", claimed)
    print("recomputed       =", actual)
    print("pinned in node   =", DIGEST)
    print("MATCH            =", claimed == actual == DIGEST)
    print("atom_order       =", contract["atom_order"])
    print("owner_order      =", contract["owner_order"])
    print("unit             =", contract["unit"])
    print("quantifier       =", contract["quantifier"])
    print("residual_rule    =", contract["residual_rule"])
    print("unresolved_cells =", contract["unresolved_cells"])
    print("first_match      =", contract["first_match"],
          contract["first_match_disjoint"])
    print("same_partition   =", contract["same_partition_for_all_atoms"])

    # Which atom index is the balanced-core cell?
    bc = [s for s in contract["chronology_stages"]
          if s["owner_id"] == "ACTIVE_V4_BALANCED_CORE"]
    print("balanced_core stage =", bc)


if __name__ == "__main__":
    main()
