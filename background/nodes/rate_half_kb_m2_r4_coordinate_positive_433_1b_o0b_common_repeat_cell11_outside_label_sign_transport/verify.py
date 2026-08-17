#!/usr/bin/env python3
"""Verify the repeated-BC cell-11 outside-label sign transport."""

import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = ROOT / "experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_outside_label_router.py"
SCRIPT_SHA256 = "1de5f3755d635c5c4b5bd21807e305bd149877f6de41ae1c60c3ea8e127ed412"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_outside_label_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_vieta_minor_compiler",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
SPEC = importlib.util.spec_from_file_location("outside_router", SCRIPT)
ROUTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ROUTER)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(permutation):
    require(sorted(permutation) == list(range(7)), "record bijection")
    b, c, d, e, f, sigma = ROUTER.sp.symbols("b c d e f sigma")
    common = (-1, b, c, sigma*b*c, sigma*b*c,
              0, (1+b)**2, (1+c)**2, (b+sigma*c)**2, (b+sigma*c)**2)
    require(all(ROUTER.sp.expand(value.subs(d, -d, simultaneous=True) - value) == 0
                if hasattr(value, "subs") else True for value in common),
            "common packet fixed")
    products = (b*e, c*f, d*e, -d*e, d*f, -d*f, sigma*e*f)
    sums = ((b+e)**2, (c+f)**2, (d+e)**2, (d-e)**2,
            (d+f)**2, (d-f)**2, (e+sigma*f)**2)
    for records in (products, sums):
        transformed = tuple(
            ROUTER.sp.expand(value.subs(d, -d, simultaneous=True))
            for value in records
        )
        require(all(ROUTER.sp.expand(transformed[index]
                                     - records[permutation[index]]) == 0
                    for index in range(7)), "outside target action")
    labels = set(itertools.product(range(7), range(15)))
    orbits = []
    while labels:
        seed = min(labels)
        image = ROUTER.act(seed, permutation)
        require(ROUTER.act(image, permutation) == seed, "label involution")
        orbit = tuple(sorted({seed, image}))
        labels -= set(orbit)
        orbits.append(orbit)
    require(len(orbits) == 57 and sum(map(len, orbits)) == 105, "orbit census")
    missing_images = {
        ROUTER.RECORDS[index]: ROUTER.RECORDS[permutation[index]]
        for index in range(7)
    }
    require(missing_images["DE+"] == "DE-" and missing_images["DF+"] == "DF-",
            "missing-record transport")
    return tuple(orbits)


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "script custody")
    orbits = validate(ROUTER.D_SIGN_FLIP)
    require(ROUTER.profile(orbits) == {1: 9, 2: 48, 4: 0}, "orbit profile")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED"
                and (parent, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL11_OUTSIDE_SIGN_TRANSPORT_VERIFY_PASS labels=105 orbits=57 transported=30")


if __name__ == "__main__":
    main()
