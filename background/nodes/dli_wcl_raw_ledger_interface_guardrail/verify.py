#!/usr/bin/env python3
"""Verify the WCL raw-ledger interface and low-level quantization guardrail."""

from __future__ import annotations

import copy
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DAG = ROOT / "dag.json"
# w7-C5 retarget: master keeps the C1' pose in the dli node's notes
C1 = ROOT / ("critical/nodes/dli_prime_weighted_large_block_support/notes/C1PRIME_LEVEL_SCALED_POSE.md")
WCL = ROOT / "background/nodes/dli_wcl_zone_coverage/statement.md"
LATTICE = ROOT / "critical/nodes/dli_prime_weighted_large_block_support/PRO_DLI_CLOSE_6.md"
NODE = "dli_wcl_raw_ledger_interface_guardrail"
ZONE = "dli_wcl_zone_coverage"
LOW_LEVELS = (1, 2, 4, 8)


class Reject(ValueError):
    pass


def minimum_charge(level: int) -> Fraction:
    if not isinstance(level, int) or isinstance(level, bool) or level <= 0:
        raise Reject("level")
    return Fraction(2 * 256 * level, 2 ** (level + 5))


def compile_interface(payload: object) -> tuple[Fraction, Fraction]:
    if not isinstance(payload, dict) or set(payload) != {
        "consumer_ledger", "level", "orbits"
    }:
        raise Reject("payload schema")
    if payload["consumer_ledger"] != "raw":
        raise Reject("C1 consumer must use raw ledger")
    level = payload["level"]
    if not isinstance(level, int) or isinstance(level, bool) or level <= 0:
        raise Reject("level")
    orbits = payload["orbits"]
    if not isinstance(orbits, list) or not orbits:
        raise Reject("orbit ledger")
    raw = Fraction(0)
    owners = Fraction(0)
    seen_classes: set[str] = set()
    for row in orbits:
        if not isinstance(row, dict) or set(row) != {"class", "primitive", "weight"}:
            raise Reject("orbit schema")
        label = row["class"]
        primitive = row["primitive"]
        weight = row["weight"]
        if (
            not isinstance(label, str)
            or not label
            or primitive is not True
            or not isinstance(weight, int)
            or isinstance(weight, bool)
            or not level + 1 <= weight <= level + 5
        ):
            raise Reject("orbit row")
        mass = Fraction(2 * 256 * level, 2**weight)
        raw += mass
        if label not in seen_classes:
            owners += mass
            seen_classes.add(label)
    return raw, owners


def main() -> None:
    dag = json.loads(DAG.read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    c1 = C1.read_text()
    wcl = WCL.read_text()
    lattice = LATTICE.read_text()
    structural = {
        "guardrail_proved": nodes[NODE]["status"] == "PROVED",
        "zone_target": nodes[ZONE]["status"] == "TARGET",
        "evidence_edge": (NODE, ZONE, "ev") in edges,
        "c1_raw_sum": "sum_(primitive O" in c1 and "2N*2^-w(O)" in c1,
        "wcl_raw_pin": "RAW primitive signed-shift ledger" in " ".join(wcl.split()) and "no shadow/lift/cluster de-duplication" in " ".join(wcl.split()),
        "lattice_all_points": (
            "no independence convention anywhere" in lattice
            and "priced at their own weights" in lattice
        ),
    }
    if not all(structural.values()):
        raise AssertionError(structural)

    low = {level: minimum_charge(level) for level in LOW_LEVELS}
    if not all(value > Fraction(1, 32) for value in low.values()):
        raise AssertionError("low-level emptiness equivalence")
    if minimum_charge(16) != Fraction(1, 256):
        raise AssertionError("ell=16 boundary")

    payload = {
        "consumer_ledger": "raw",
        "level": 16,
        "orbits": [
            {"class": "one", "primitive": True, "weight": 21}
            for _ in range(9)
        ],
    }
    raw, owners = compile_interface(payload)
    if not (owners == Fraction(1, 256) <= Fraction(1, 32) < raw == Fraction(9, 256)):
        raise AssertionError("ownership countermodel")

    controls = []
    mutations = (
        lambda item: item.__setitem__("consumer_ledger", "owner"),
        lambda item: item.__setitem__("level", 0),
        lambda item: item["orbits"][0].__setitem__("primitive", False),
        lambda item: item["orbits"][0].__setitem__("weight", 22),
        lambda item: item["orbits"][0].__setitem__("class", ""),
    )
    for mutate in mutations:
        altered = copy.deepcopy(payload)
        mutate(altered)
        try:
            compile_interface(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError(f"negative controls caught {sum(controls)}/{len(controls)}")
    print(
        "DLI_WCL_RAW_LEDGER_INTERFACE_PASS "
        f"low_levels={','.join(map(str, LOW_LEVELS))} "
        f"owner_countermodel={owners} raw_countermodel={raw} "
        f"negative_controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
