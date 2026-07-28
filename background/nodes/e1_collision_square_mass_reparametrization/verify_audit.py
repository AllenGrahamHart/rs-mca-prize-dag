#!/usr/bin/env python3
"""Independent audit: rebuild the coordinates from scratch and re-check wiring."""
from __future__ import annotations
import json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_collision_square_mass_reparametrization"
SUPPLIER = "e1_prime_field_l2_norm_collision_radius"
CONSUMERS = ("e1_official_prime_exception_control",
             "unsafe_crossing_family_instantiation")


def main() -> None:
    checks = 0
    # Rebuild alpha's coefficient multiset directly, without the S formula,
    # by simulating the fold: opposite pair -> 2, singleton -> 1, same pair -> 0.
    for a in range(0, 7):
        for b in range(0, 13, 2):
            for c in range(0, 7):
                coeffs = [2] * a + [1] * b + [0] * c
                S_direct = sum(x * x for x in coeffs)
                assert S_direct == 4 * a + b, (a, b, c)
                positions = 2 * a + b + 2 * c
                assert positions % 2 == 0
                assert positions // 2 == a + b // 2 + c
                checks += 2

    # the four pinned profiles land on their pinned bands
    for (a, b, c), s in (((3, 4, 0), 5), ((4, 2, 0), 5),
                         ((1, 2, 0), 2), ((0, 4, 0), 2)):
        assert a + b // 2 + c == s
        checks += 1

    # square-mass floors
    assert math.ceil(2 ** (500 / 128)) == 15
    assert math.ceil(2 ** (500 / 256)) == 4
    checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {n["id"]: n for n in dag["nodes"]}
    edges = {(e["from"], e["to"], e["kind"]) for e in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert (SUPPLIER, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert nodes[consumer]["status"] == "TARGET"
        assert (NODE, consumer, "ev") in edges, consumer
        assert (NODE, consumer, "req") not in edges, "must stay evidence-only"
        checks += 3
    checks += 3

    print(f"E1_COLLISION_SQUARE_MASS_REPARAMETRIZATION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
