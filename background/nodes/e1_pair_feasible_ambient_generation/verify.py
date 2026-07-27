#!/usr/bin/env python3
"""Verify that pair-feasible clean-anchor E1 rows generate the ambient field."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_pair_feasible_ambient_generation"
PARENT = "e1_clean_anchor_exact_collision_allowance"
E1_TARGET = "e1_official_prime_exception_control"
UNIVERSAL_TARGET = "unsafe_crossing_family_instantiation"

EXPECTED_PIN = {
    "file": "background/nodes/e1_clean_anchor_exact_collision_allowance/statement.md",
    "file_sha256": "1380aed931775cb434e67586f0346b470afca4d19b52985f037a64793a26068a",
    "field_cap_bits": 256,
}


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    source = ROOT / pin["file"]
    assert hashlib.sha256(source.read_bytes()).hexdigest() == pin["file_sha256"]

    thresholds = (
        ("RowC-1/4", 382284112190896383970682459093111839235997652964233428737, 188),
        ("RowC-1/8", 12668879649419138327999082396158341660417, 134),
        ("RowC-1/16", 1137987620444272639348514363568529251287851553619457, 170),
        ("prize-1/4", 382284112190896384074741713357221542466466218296788430623, 188),
        ("prize-1/8", 12772938903683248031229550961490896662303, 134),
        ("prize-1/16", 1137987620444376698602778473271759719853184108621343, 170),
    )
    proper_subfield_ceiling = 1 << (pin["field_cap_bits"] // 2)
    for name, threshold, expected_bits in thresholds:
        assert threshold.bit_length() == expected_bits, name
        assert threshold > proper_subfield_ceiling, name

    # Exhaust small field towers: a proper subfield under a strict 2^C cap
    # is always below 2^(C/2).
    tower_checks = 0
    for cap_bits in range(4, 17):
        for base_size in range(2, 1 << (cap_bits // 2 + 1)):
            for degree in range(2, cap_bits + 1):
                q = base_size**degree
                if q < 1 << cap_bits:
                    assert base_size**2 < 1 << cap_bits
                    if cap_bits % 2 == 0:
                        assert base_size < 1 << (cap_bits // 2)
                    tower_checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[PARENT] == "PROVED"
    assert statuses[E1_TARGET] == "TARGET"
    assert statuses[UNIVERSAL_TARGET] == "TARGET"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, UNIVERSAL_TARGET, "ev") in edges
    assert "F_p(Q)=F_q" in statements[NODE]
    assert "b_pair_min>2^128" in statements[NODE]

    print(
        "E1_PAIR_FEASIBLE_AMBIENT_GENERATION_PASS "
        f"rows={len(thresholds)} tower_checks={tower_checks}"
    )


if __name__ == "__main__":
    main()
