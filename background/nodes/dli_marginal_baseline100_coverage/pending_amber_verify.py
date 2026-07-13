# PARKED PENDING AMBER (w6-C10, 2026-07-13): becomes this node's
# verify.py VERBATIM at the maintainer's amber ceremony; its
# structural checks expect the amber wiring (req edges + status).
#!/usr/bin/env python3
"""Exact fail-closed audit of the 100-bit DLI marginal assembly."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
TARGET = "dli_marginal_baseline100_coverage"
C1 = "dli_dyadic_k_core"
ZONE = "dli_wcl_zone_coverage"


class Reject(ValueError):
    pass


def exact_fraction(value: object) -> Fraction:
    if (
        not isinstance(value, list)
        or len(value) != 2
        or any(not isinstance(part, int) or isinstance(part, bool) for part in value)
        or value[1] <= 0
    ):
        raise Reject("not an exact rational pair")
    return Fraction(value[0], value[1])


def exact_rows(value: object) -> frozenset[str]:
    if not isinstance(value, list) or not value:
        raise Reject("row set absent")
    if any(not isinstance(row, str) or not row for row in value):
        raise Reject("invalid row key")
    rows = frozenset(value)
    if len(rows) != len(value):
        raise Reject("duplicate row key")
    return rows


def compile_baseline(payload: object) -> Fraction:
    required = {
        "schema",
        "official_rows",
        "c1_rows",
        "zone_rows",
        "predicate_ids",
        "levels",
        "k_prime",
        "tau",
        "field_bits_strict",
        "N_rule",
        "baseline_endpoint",
    }
    if not isinstance(payload, dict) or set(payload) != required:
        raise Reject("schema keys do not match")
    if payload["schema"] != "dli-baseline100-assembly-v1":
        raise Reject("schema mismatch")
    if payload["predicate_ids"] != [C1, ZONE]:
        raise Reject("predicate identity/order mismatch")

    official = exact_rows(payload["official_rows"])
    if exact_rows(payload["c1_rows"]) != official:
        raise Reject("C1' row coverage gap")
    if exact_rows(payload["zone_rows"]) != official:
        raise Reject("W_cl zone coverage gap")
    if payload["levels"] != 34:
        raise Reject("production level count drift")
    if payload["field_bits_strict"] != 256 or payload["N_rule"] != "N_L=256L":
        raise Reject("balance pin drift")

    k_prime = exact_fraction(payload["k_prime"])
    tau = exact_fraction(payload["tau"])
    endpoint = exact_fraction(payload["baseline_endpoint"])
    if k_prime < 0 or tau < 0:
        raise Reject("negative premise bound")
    if k_prime > 4:
        raise Reject("C1' constant exceeds four")
    if tau > Fraction(1, 32):
        raise Reject("primitive-ledger zone exceeds 1/32")
    if endpoint != 2**100:
        raise Reject("100-bit endpoint drift")

    level_factor = 1 + k_prime * (1 + tau)
    aggregate = level_factor**payload["levels"]
    if aggregate > endpoint:
        raise Reject("marginal aggregate exceeds endpoint")
    return aggregate


def rejected(payload: dict) -> bool:
    try:
        compile_baseline(payload)
    except Reject:
        return True
    return False


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    proof = (ROOT / f"critical/nodes/{TARGET}/conditional.md").read_text()

    structural = {
        "baseline_conditional": nodes[TARGET]["status"] == "CONDITIONAL",
        "c1_target": nodes[C1]["status"] == "TARGET",
        "zone_target": nodes[ZONE]["status"] == "TARGET",
        "c1_req": (C1, TARGET, "req") in edges,
        "zone_req": (ZONE, TARGET, "req") in edges,
        "factor_pin": "E_L <= 41/8" in proof,
        "integer_pin": "41^34 < 2^202" in proof,
        "no_reserve_credit": "reserve credit" in proof,
    }
    if not all(structural.values()):
        raise AssertionError(structural)

    good = {
        "schema": "dli-baseline100-assembly-v1",
        "official_rows": ["official-row-A", "official-row-B"],
        "c1_rows": ["official-row-B", "official-row-A"],
        "zone_rows": ["official-row-A", "official-row-B"],
        "predicate_ids": [C1, ZONE],
        "levels": 34,
        "k_prime": [4, 1],
        "tau": [1, 32],
        "field_bits_strict": 256,
        "N_rule": "N_L=256L",
        "baseline_endpoint": [2**100, 1],
    }
    aggregate = compile_baseline(good)
    if aggregate != Fraction(41, 8) ** 34:
        raise AssertionError("41/8 boundary reconstruction failed")
    if not 2**80 < aggregate < 2**81:
        raise AssertionError("exact aggregate bit bracket drift")
    if not 41**34 < 2**202:
        raise AssertionError("integer endpoint inequality failed")

    mutations: list[dict] = []
    for mutate in (
        lambda p: p.pop("c1_rows"),
        lambda p: p["c1_rows"].pop(),
        lambda p: p["zone_rows"].pop(),
        lambda p: p.__setitem__("k_prime", [5, 1]),
        lambda p: p.__setitem__("tau", [1, 16]),
        lambda p: p.__setitem__("levels", 35),
        lambda p: p.__setitem__("field_bits_strict", 257),
        lambda p: p.__setitem__("N_rule", "N_L=255L"),
        lambda p: p.__setitem__("tau", 0.03125),
        lambda p: p.__setitem__("baseline_endpoint", [2**101, 1]),
        lambda p: p.__setitem__("predicate_ids", [ZONE, C1]),
    ):
        candidate = json.loads(json.dumps(good))
        mutate(candidate)
        mutations.append(candidate)
    caught = sum(rejected(candidate) for candidate in mutations)
    if caught != len(mutations):
        raise AssertionError(f"negative controls caught {caught}/{len(mutations)}")

    print(
        "DLI_BASELINE100_ASSEMBLY_PASS "
        f"factor=41/8 aggregate_bits=(80,81) negative_controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()

