#!/usr/bin/env python3
"""Verify the rigid S6 [6,5,2] pair-quotient certificate."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PRODUCER = ROOT / "experiments/prize_resolution/rate_half_kb_m4_s6_652_pair_quotient.py"
CERTIFICATE = ROOT / "experiments/prize_resolution/rate_half_kb_m4_s6_652_pair_quotient_result.json"


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
    spec = importlib.util.spec_from_file_location("kb_m4_s6_652", PRODUCER)
    if spec is None or spec.loader is None:
        raise VerificationError("cannot load producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(data: dict[str, object], expected: dict[str, object]) -> None:
    if data.get("schema") != "rate_half_kb_m4_s6_652_pair_quotient_v1":
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

    changed(lambda row: row["companion"].__setitem__("degree", 5))
    changed(lambda row: row["pair_curve"].__setitem__("projected_degree", 3))
    changed(lambda row: row["pair_curve"].__setitem__("m_of_u", "0"))
    changed(lambda row: row["quotient"].__setitem__("degree", 14))
    changed(lambda row: row["quotient"]["fiber_zero"].pop())
    changed(lambda row: row["quotient"]["fiber_one"].__setitem__(0, 4))
    changed(lambda row: row["quotient"].__setitem__("total_branch_index", 27))
    changed(lambda row: row["challenge_field"].__setitem__("pole_fiber_splits", False))
    changed(lambda row: row["challenge_field"].__setitem__("extension_degree", 5))
    changed(lambda row: row["conclusion"].__setitem__("passport", "A6"))
    changed(lambda row: row["scope_fence"].pop())
    changed(lambda row: row.__setitem__("extra", 1))
    return mutations


def main() -> None:
    data = json.loads(CERTIFICATE.read_text())
    expected = load_producer().build()
    validate(data, expected)
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
    if "No completely split unramified 15-point active fiber" not in contract:
        raise VerificationError("scope fence missing")
    print("RATE_HALF_KB_M4_S6_652_PAIR_QUOTIENT_NORMAL_FORM_PASS")
    print("RATE_HALF_KB_M4_S6_652_PAIR_QUOTIENT_MUTATIONS_12_OF_12_REJECTED")


if __name__ == "__main__":
    main()
