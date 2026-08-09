#!/usr/bin/env python3
"""Verify the cell-9 parallel-DE first-pair exclusion."""

import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_parallel_de_first_pair_residual_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_parallel_de_first_pair_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PRIMARY_SHA = "87002be22b20a3676311fb7a6a86bc143bdbb6122bf218cafe808db904562cbe"
AUDIT_SHA = "50daa9cdccf0a7941e723efc4558d7de211a35d67f8da41ccce5300cf8f5cf9e"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def terminal(payload, audit=False):
    expected = set(itertools.product(
        (-1, 1), (-1, 1), (-1, 1), (-1, 1), ("positive", "negative")
    ))
    rows = {(*row["epsilon"], *row["sigma"], row["cut_kind"]): row
            for row in payload["rows"]}
    require(set(rows) == expected and len(payload["rows"]) == 32,
            "case keys")
    total = 0
    for row in rows.values():
        expected_systems = 12 if row["cut_kind"] == "positive" else 6
        require(row["status"] == "COMPLETE"
                and row["systems"] == expected_systems
                and row["unit_systems"] == expected_systems,
                "terminal system row")
        if audit:
            require(not row["witnesses"] and not row["unresolved"]
                    and row["finite_systems"] == 0, "audit terminal")
        else:
            require(not row["nonunit_systems"], "primary terminal")
        total += row["systems"]
    require(total == 288, "system total")


def main():
    require(hashlib.sha256(PRIMARY.read_bytes()).hexdigest() == PRIMARY_SHA,
            "primary hash")
    require(hashlib.sha256(AUDIT.read_bytes()).hexdigest() == AUDIT_SHA,
            "audit hash")
    terminal(json.loads(PRIMARY.read_text()))
    terminal(json.loads(AUDIT.read_text()), audit=True)

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    direct = {(xi, matching) for xi in (0, 2) for matching in (0, 1, 2)}
    selected = [orbit for orbit in router.compile_orbits()
                if direct & set(orbit)]
    expected = [
        [(0, 0), (1, 0)],
        [(0, 1), (0, 2), (1, 1), (1, 2)],
        [(2, 0)],
        [(2, 1), (2, 2)],
    ]
    require(selected == expected and len(set().union(*map(set, selected))) == 9,
            "nine-label orbit transport")
    print("PASS cell-9 parallel-DE first-pair exclusion: systems=288 orbits=4 labels=9")


if __name__ == "__main__":
    main()
