#!/usr/bin/env python3
"""Mutation guards for the tame central-star necklace bound."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "tame_central_star_belyi_necklace_bound"
VERIFY = ROOT / "background/nodes" / NODE / "verify.py"


def load_verify():
    spec = importlib.util.spec_from_file_location("central_star_verify", VERIFY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    # Rotation quotient is load-bearing; labelled words overcount necklaces.
    assert verify.necklace_formula(12, 2) == 6
    assert verify.necklace_formula(14, 5) == 143
    assert verify.necklace_formula(24, 4) == 446
    assert verify.necklace_formula(12, 2) < 66

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    statement = (ROOT / "background/nodes" / NODE / "statement.md").read_text()
    for marker in (
        "source scalings", "characteristic `p>m`", "labelled polynomial covers",
        "not every necklace",
    ):
        assert marker in statement
    print(
        "TAME_CENTRAL_STAR_BELYI_NECKLACE_BOUND_AUDIT_PASS "
        "rotation_guard=1 reflection_guard=1 tame_guard=1"
    )


if __name__ == "__main__":
    main()
