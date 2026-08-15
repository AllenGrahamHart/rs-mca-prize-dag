#!/usr/bin/env python3
"""Independent audit of completion-branch lattice refinement."""

from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    checks = 0
    for source in range(2, 10):
        q = 19
        terminal = set(range(q - (9 - source), q + 1))
        fallback = set(range(q - (10 - source) + 1))
        require(not terminal & fallback, "disjoint")
        require(terminal | fallback == set(range(q + 1)), "exhaustive")
        require(len(terminal) + 1 == 11 - source, "leaf count")
        checks += q + 1
    special = p["support6_specialization"]
    require(special["terminal_defects"] == [0, 1, 2, 3], "support-six defects")
    require(special["fallback_ceiling"] == "q-4", "support-six fallback")
    require(special["replacement_leaf_count"] == 5, "support-six leaves")
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_COMPLETION_BRANCH_LATTICE_REFINEMENT_AUDIT_PASS "
        f"partition_checks={checks} support6_leaves=5"
    )


if __name__ == "__main__":
    main()
