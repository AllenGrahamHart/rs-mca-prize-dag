#!/usr/bin/env python3
"""Verify the cell-5 parallel-DE first-pair exclusion."""

import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell5_parallel_de_first_pair_residual_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell5_parallel_de_first_pair_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PRIMARY_SHA = "1abe858fb41a176baf59648a1be234b0a80ec749c5c9c5435ed7cfda6093fc41"
AUDIT_SHA = "4a3050677cb2568fc93dae6ffac33d06d3ee6682fd78bead7ddf84cbe4691dc6"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def terminal(payload, audit=False):
    expected = set(itertools.product(
        (-1, 1), (-1, 1), (-1, 1), (-1, 1)
    ))
    rows = {(*row["epsilon"], *row["sigma"]): row for row in payload["rows"]}
    require(set(rows) == expected and len(payload["rows"]) == 16,
            "case keys")
    total = 0
    for row in rows.values():
        require(row["status"] == "COMPLETE"
                and row["systems"] == 6
                and row["unit_systems"] == 6,
                "terminal system row")
        if audit:
            require(row["cut_kind"] == "equal_negative"
                    and not row["witnesses"] and not row["unresolved"]
                    and row["finite_systems"] == 0, "audit terminal")
        else:
            require(not row["nonunit_systems"], "primary terminal")
        total += row["systems"]
    require(total == 96, "system total")


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
    print("PASS cell-5 parallel-DE first-pair exclusion: systems=96 orbits=4 labels=9")


if __name__ == "__main__":
    main()
