# PARKED PENDING AMBER (w6-C10, 2026-07-13): becomes
# critical/nodes/dli_prime_weighted_large_block_support/verify.py
# VERBATIM at the maintainer's amber ceremony; its structural checks
# expect the amber wiring (req edges {baseline,c2pp} -> dli + dli
# status CONDITIONAL), which master has NOT executed.
#!/usr/bin/env python3
"""Fail-closed exact audit of the DLI M4 assembly implication."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BASELINE_ID = "dli_marginal_baseline100_coverage"
JOINT_ID = "dli_c2pp_joint_reserve"
TARGET_ID = "dli_prime_weighted_large_block_support"


class Reject(ValueError):
    pass


def exact_fraction(value: object) -> Fraction:
    if (
        not isinstance(value, list)
        or len(value) != 2
        or any(not isinstance(part, int) or isinstance(part, bool) for part in value)
        or value[1] <= 0
    ):
        raise Reject("not an exact positive-denominator rational pair")
    return Fraction(value[0], value[1])


def row_set(value: object) -> frozenset[str]:
    if not isinstance(value, list) or not value:
        raise Reject("row list absent")
    if any(not isinstance(row, str) or not row for row in value):
        raise Reject("invalid row key")
    rows = frozenset(value)
    if len(rows) != len(value):
        raise Reject("duplicate row key")
    return rows


def compile_endpoint(payload: object) -> Fraction:
    required = {
        "schema",
        "official_rows",
        "baseline_rows",
        "c2pp_instance_rows",
        "baseline_upper",
        "joint_factor_upper",
        "endpoint",
        "predicate_ids",
    }
    if not isinstance(payload, dict) or set(payload) != required:
        raise Reject("schema keys do not match")
    if payload["schema"] != "dli-m4-assembly-v1":
        raise Reject("schema mismatch")
    if payload["predicate_ids"] != [BASELINE_ID, JOINT_ID]:
        raise Reject("predicate identity/order mismatch")

    official = row_set(payload["official_rows"])
    if row_set(payload["baseline_rows"]) != official:
        raise Reject("baseline theorem row gap")
    if row_set(payload["c2pp_instance_rows"]) != official:
        raise Reject("C2'' instance gap")

    baseline = exact_fraction(payload["baseline_upper"])
    joint = exact_fraction(payload["joint_factor_upper"])
    endpoint = exact_fraction(payload["endpoint"])
    if baseline < 0 or joint < 0:
        raise Reject("negative upper bound")
    if baseline > 2**100:
        raise Reject("marginal baseline exceeds 100 bits")
    if joint > 2**21:
        raise Reject("joint reserve exceeds 21 bits")
    if endpoint != 2**121:
        raise Reject("consumer endpoint drift")
    result = baseline * joint
    if result > endpoint:
        raise Reject("assembled endpoint exceeded")
    return result


def rejected(payload: dict) -> bool:
    try:
        compile_endpoint(payload)
    except Reject:
        return True
    return False


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    conditional = (ROOT / f"critical/nodes/{TARGET_ID}/conditional.md").read_text()
    baseline_statement = (
        ROOT / f"critical/nodes/{BASELINE_ID}/statement.md"
    ).read_text()
    joint_statement = (ROOT / f"critical/nodes/{JOINT_ID}/statement.md").read_text()

    structural = {
        "target_conditional": nodes[TARGET_ID]["status"] == "CONDITIONAL",
        "baseline_conditional": nodes[BASELINE_ID]["status"] == "CONDITIONAL",
        "joint_target": nodes[JOINT_ID]["status"] == "TARGET",
        "baseline_req": (BASELINE_ID, TARGET_ID, "req") in edges,
        "joint_req": (JOINT_ID, TARGET_ID, "req") in edges,
        "baseline_100": "(41/8)^34 < 2^100" in baseline_statement,
        "joint_21": "X(R) <= 2^21 A(R)" in joint_statement,
        "endpoint_121": "2^21 2^100 = 2^121" in conditional,
        "no_certificate_interface_in_baseline": (
            "no endpoint certificate" in baseline_statement
            and "reserve credit" in baseline_statement
        ),
    }
    if not all(structural.values()):
        raise AssertionError(structural)

    good = {
        "schema": "dli-m4-assembly-v1",
        "official_rows": ["official-row-A", "official-row-B"],
        "baseline_rows": ["official-row-B", "official-row-A"],
        "c2pp_instance_rows": ["official-row-A", "official-row-B"],
        "baseline_upper": [2**100, 1],
        "joint_factor_upper": [2**21, 1],
        "endpoint": [2**121, 1],
        "predicate_ids": [BASELINE_ID, JOINT_ID],
    }
    if compile_endpoint(good) != 2**121:
        raise AssertionError("exact boundary assembly failed")

    mutations: list[dict] = []
    for mutate in (
        lambda p: p.pop("baseline_rows"),
        lambda p: p["baseline_rows"].pop(),
        lambda p: p["c2pp_instance_rows"].pop(),
        lambda p: p.__setitem__("baseline_upper", [2**100 + 1, 1]),
        lambda p: p.__setitem__("joint_factor_upper", [2**21 + 1, 1]),
        lambda p: p.__setitem__("endpoint", [2**122, 1]),
        lambda p: p.__setitem__("baseline_upper", 2.0**100),
        lambda p: p.__setitem__("predicate_ids", [JOINT_ID, BASELINE_ID]),
        lambda p: p["official_rows"].append("official-row-A"),
    ):
        candidate = json.loads(json.dumps(good))
        mutate(candidate)
        mutations.append(candidate)
    caught = sum(rejected(candidate) for candidate in mutations)
    if caught != len(mutations):
        raise AssertionError(f"negative controls caught {caught}/{len(mutations)}")

    print(
        "DLI_M4_ASSEMBLY_PASS "
        f"boundary=2^121 negative_controls={caught}/{len(mutations)} "
        "premises=baseline100+C2pp21"
    )


if __name__ == "__main__":
    main()
