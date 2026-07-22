#!/usr/bin/env python3
"""Mutation audit for the exact unsafe-cell fiber-layout counterexample."""

from __future__ import annotations

import json
from copy import deepcopy

from verify import D, Q, ROOT, SELECTED_CLASSES, evaluate, evaluate_wiring


def trips(**changes: object) -> bool:
    return not all(evaluate(**changes).values())


def main() -> None:
    mutations = [
        {"q": Q + 2},
        {"d": D // 2},
        {"selected_classes": (2, 2, 3, 4, 5, 6)},
        {"selected_classes": SELECTED_CLASSES[:-1]},
        {"background_class": 0},
        {"core_class": 2},
        {"proth_base": 2},
        {"rate_denominator": 2},
    ]
    caught = sum(trips(**mutation) for mutation in mutations)

    dag = json.loads((ROOT / "dag.json").read_text())
    wiring_mutations = []

    changed = deepcopy(dag)
    next(node for node in changed["nodes"] if node["id"] == "ww_row_envelope_clause")["status"] = "REFUTED"
    wiring_mutations.append(changed)

    changed = deepcopy(dag)
    next(
        edge
        for edge in changed["edges"]
        if edge["from"] == "list_safe" and edge["to"] == "list_adjacency_closing"
    )["kind"] = "ev"
    wiring_mutations.append(changed)

    changed = deepcopy(dag)
    next(
        edge
        for edge in changed["edges"]
        if edge["from"] == "list_planted_arithmetic"
        and edge["to"] == "list_adjacency_closing"
    )["kind"] = "req"
    wiring_mutations.append(changed)

    changed = deepcopy(dag)
    changed["edges"] = [
        edge
        for edge in changed["edges"]
        if not (
            edge["from"] == "ww_spending_cell_fiber_layout_counterexample"
            and edge["to"] == "ww_row_envelope_clause"
        )
    ]
    wiring_mutations.append(changed)

    changed = deepcopy(dag)
    next(
        node for node in changed["nodes"] if node["id"] == "ww_row_envelope_clause"
    )["statement"] = next(
        node for node in changed["nodes"] if node["id"] == "ww_row_envelope_clause"
    )["statement"].replace("safe-side official-convention", "official-convention")
    wiring_mutations.append(changed)

    wiring_caught = sum(
        not all(evaluate_wiring(changed).values()) for changed in wiring_mutations
    )
    if caught != len(mutations) or wiring_caught != len(wiring_mutations):
        raise SystemExit(
            "WW_SPENDING_CELL_FIBER_LAYOUT_COUNTEREXAMPLE_AUDIT_FAIL "
            f"math={caught}/{len(mutations)} wiring={wiring_caught}/{len(wiring_mutations)}"
        )
    print(
        "WW_SPENDING_CELL_FIBER_LAYOUT_COUNTEREXAMPLE_AUDIT_PASS "
        f"math_mutations={caught}/{len(mutations)} "
        f"wiring_mutations={wiring_caught}/{len(wiring_mutations)}"
    )


if __name__ == "__main__":
    main()
