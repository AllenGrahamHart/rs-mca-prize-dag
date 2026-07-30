#!/usr/bin/env python3
"""Verify the KoalaBear m4 adjacency-genus exclusion certificate."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PRODUCER = (
    ROOT
    / "experiments/prize_resolution/rate_half_kb_m4_adjacency_genus_exclusion.py"
)
CERTIFICATE = (
    ROOT
    / "experiments/prize_resolution/rate_half_kb_m4_adjacency_genus_exclusion_result.json"
)


class VerificationError(RuntimeError):
    pass


def canonical_hash(data: dict[str, object]) -> str:
    payload = copy.deepcopy(data)
    payload.pop("payload_sha256", None)
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def load_producer():
    spec = importlib.util.spec_from_file_location("kb_m4_adjacency_genus", PRODUCER)
    if spec is None or spec.loader is None:
        raise VerificationError("cannot load producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(data: dict[str, object], expected: dict[str, object]) -> None:
    if data.get("schema") != "rate_half_kb_m4_adjacency_genus_exclusion_v1":
        raise VerificationError("schema mismatch")
    if data.get("payload_sha256") != canonical_hash(data):
        raise VerificationError("payload mismatch")
    producer = data.get("producer")
    if not isinstance(producer, dict):
        raise VerificationError("producer missing")
    if producer.get("path") != str(PRODUCER.relative_to(ROOT)):
        raise VerificationError("producer path mismatch")
    if producer.get("sha256") != hashlib.sha256(PRODUCER.read_bytes()).hexdigest():
        raise VerificationError("producer hash mismatch")
    if data != expected:
        raise VerificationError("certificate reconstruction mismatch")


def hostile_mutations(data: dict[str, object]) -> list[dict[str, object]]:
    mutations: list[dict[str, object]] = []

    def changed(mutator) -> None:
        mutation = copy.deepcopy(data)
        mutator(mutation)
        mutation["payload_sha256"] = canonical_hash(mutation)
        mutations.append(mutation)

    changed(lambda row: row["group_actions"]["A6"].__setitem__("order", 720))
    changed(
        lambda row: row["group_actions"]["S6"].__setitem__(
            "ordered_adjacency_orbit", 60
        )
    )
    changed(lambda row: row["passports"][0].__setitem__("adjacency_genus", 2))
    changed(
        lambda row: row["passports"][1].__setitem__("total_branch_index", 248)
    )
    changed(
        lambda row: row["passports"][2]["adjacency_branch_rows"][1].__setitem__(
            "cycle_count", 31
        )
    )
    changed(lambda row: row["passports"][3]["letter_cycle_types"].pop())
    changed(lambda row: row["passports"].pop())
    changed(
        lambda row: row["imported_geometry"].__setitem__(
            "actual_component_arithmetic_genus", 4
        )
    )
    changed(
        lambda row: row["imported_geometry"].__setitem__(
            "component_to_outer_image_degree", 1
        )
    )
    changed(
        lambda row: row["conclusion"].__setitem__(
            "remaining_independent_inner_degrees", [2, 3, 4]
        )
    )
    changed(lambda row: row["scope_fence"].pop())
    changed(lambda row: row.__setitem__("extra", True))
    return mutations


def require_parent_contracts() -> None:
    route = (
        ROOT
        / "background/nodes/rate_half_kb_q6_u2_primitive_subdegree4_route_cut/proof.md"
    ).read_text()
    transverse = (
        ROOT
        / "background/nodes/rate_half_kb_source_pencil_rank_transverse_compiler/proof.md"
    ).read_text()
    passports = (
        ROOT
        / "background/nodes/rate_half_kb_m4_a6s6_genus_zero_passport_reduction/statement.md"
    ).read_text()
    required = (
        (route, "An actual outgoing component of bidegree `(u,2u)`"),
        (route, "The map is birational and its image has bidegree `(2u,2u)`"),
        (transverse, "delta*r_Y=4m=delta*r_Z"),
        (passports, "exactly\nfour letter-cycle class multisets"),
        (passports, "A6:  5.1, 2.2.1.1, 4.2"),
        (passports, "S6:  5.1, 2.2.2, 3.2.1"),
    )
    for content, needle in required:
        if needle not in content:
            raise VerificationError(f"parent contract missing: {needle}")


def main() -> None:
    data = json.loads(CERTIFICATE.read_text())
    expected = load_producer().build()
    validate(data, expected)
    require_parent_contracts()
    for number, mutation in enumerate(hostile_mutations(data), start=1):
        try:
            validate(mutation, expected)
        except VerificationError:
            continue
        raise VerificationError(f"hostile mutation {number} accepted")
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    if "- **status:** PROVED" not in statement:
        raise VerificationError("status missing")
    if "No `m=2` or `m=3` type is deleted" not in contract:
        raise VerificationError("scope fence missing")
    print("RATE_HALF_KB_M4_ADJACENCY_GENUS_EXCLUSION_PASS")
    print("RATE_HALF_KB_M4_ADJACENCY_GENUS_MUTATIONS_12_OF_12_REJECTED")


if __name__ == "__main__":
    main()
