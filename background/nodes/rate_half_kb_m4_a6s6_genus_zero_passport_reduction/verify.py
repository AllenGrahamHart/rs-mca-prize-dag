#!/usr/bin/env python3
"""Verify the KoalaBear m4 genus-zero passport certificate."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PRODUCER = ROOT / "experiments/prize_resolution/rate_half_kb_m4_degree15_passport_budget.py"
CERTIFICATE = ROOT / "experiments/prize_resolution/rate_half_kb_m4_degree15_passport_budget_result.json"
TOP_KEYS = {
    "schema",
    "payload_sha256",
    "producer",
    "input",
    "class_rows",
    "necessary_passports",
    "tuple_audit",
    "conclusion",
    "scope_fence",
}


class VerificationError(RuntimeError):
    pass


def canonical_payload(data: dict[str, object]) -> str:
    payload = copy.deepcopy(data)
    payload.pop("payload_sha256", None)
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def load_producer():
    spec = importlib.util.spec_from_file_location("kb_m4_passport_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise VerificationError("cannot load producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expected_sections(module) -> tuple[list, list, list]:
    table = module.class_table()
    passports = module.residual_passports(table)
    audits = module.tuple_audit(passports)
    class_rows = [
        [
            module.label(tuple(row["letter_cycle_type"])),
            row["class_size"],
            row["letter_parity"],
            module.label(tuple(row["pair_cycle_type"])),
            row["pair_index"],
        ]
        for row in table
    ]
    necessary = [
        [
            row["ambient_candidates"][0],
            row["residual_classes"],
            row["residual_indices"],
            row["odd_class_count"],
        ]
        for row in passports
    ]
    tuple_rows = [
        [
            row["residual_classes"],
            row["target_order"],
            [
                [
                    pole["pole_class"],
                    pole["product_one_tuple_count"],
                    pole["generated_order_counts"],
                    pole["generating_tuple_count"],
                ]
                for pole in row["pole_class_audits"]
            ],
            row["realized"],
        ]
        for row in audits
    ]
    return class_rows, necessary, tuple_rows


def validate(data: dict[str, object], expected: tuple[list, list, list]) -> None:
    if set(data) != TOP_KEYS:
        raise VerificationError("top-level schema mismatch")
    if data["schema"] != "rate_half_kb_m4_degree15_passport_budget_v1":
        raise VerificationError("schema mismatch")
    if data["payload_sha256"] != canonical_payload(data):
        raise VerificationError("payload mismatch")
    producer = data["producer"]
    if set(producer) != {"path", "sha256"}:
        raise VerificationError("producer schema mismatch")
    if producer["path"] != str(PRODUCER.relative_to(ROOT)):
        raise VerificationError("producer path mismatch")
    if producer["sha256"] != hashlib.sha256(PRODUCER.read_bytes()).hexdigest():
        raise VerificationError("producer hash mismatch")
    if data["input"] != {
        "degree": 15,
        "genus_zero_total_index": 28,
        "mandatory_letter_class": "5.1",
        "mandatory_pair_cycle_type": "5.5.5",
        "mandatory_index": 12,
        "residual_index_budget": 16,
    }:
        raise VerificationError("input mismatch")
    class_rows, necessary, tuple_rows = expected
    if data["class_rows"] != class_rows:
        raise VerificationError("class table mismatch")
    if data["necessary_passports"] != necessary:
        raise VerificationError("necessary passport mismatch")
    if data["tuple_audit"] != tuple_rows:
        raise VerificationError("tuple audit mismatch")
    if data["conclusion"] != {
        "necessary_passport_count": 9,
        "realized_passport_count": 4,
        "retained": [
            ["A6", ["5.1", "2.2.1.1", "4.2"]],
            ["S6", ["5.1", "2.1.1.1.1", "2.2.1.1", "2.2.2"]],
            ["S6", ["5.1", "2.1.1.1.1", "6"]],
            ["S6", ["5.1", "2.2.2", "3.2.1"]],
        ],
        "three_point_count": 3,
        "four_point_count": 1,
        "terminal": "M4_A6S6_GEOMETRIC_FRONTIER_FOUR_PASSPORTS",
    }:
        raise VerificationError("conclusion mismatch")
    required_fences = {
        "no challenge-field descent",
        "no split-zero or split-pole payment",
        "no quartic source-star incidence",
        "no surviving m4 type deletion",
        "no KoalaBear row or ledger closure",
    }
    if set(data["scope_fence"]) != required_fences:
        raise VerificationError("scope fence mismatch")


def hostile_mutations(data: dict[str, object]) -> list[dict[str, object]]:
    mutations: list[dict[str, object]] = []

    def changed(mutator) -> None:
        mutation = copy.deepcopy(data)
        mutator(mutation)
        mutation["payload_sha256"] = canonical_payload(mutation)
        mutations.append(mutation)

    changed(lambda row: row["input"].__setitem__("residual_index_budget", 15))
    changed(lambda row: row["class_rows"][1].__setitem__(4, 5))
    changed(lambda row: row["class_rows"][9].__setitem__(3, "5.5.1.1.1.1.1"))
    changed(lambda row: row["necessary_passports"].pop())
    changed(lambda row: row["necessary_passports"][0][1].pop())
    changed(lambda row: row["tuple_audit"][0][2][0].__setitem__(3, 1))
    changed(lambda row: row["tuple_audit"][2].__setitem__(3, False))
    changed(lambda row: row["tuple_audit"][5][2].pop())
    changed(lambda row: row["conclusion"].__setitem__("realized_passport_count", 5))
    changed(lambda row: row["conclusion"]["retained"].pop())
    changed(lambda row: row["scope_fence"].pop())
    changed(lambda row: row.__setitem__("extra", 1))
    return mutations


def main() -> None:
    data = json.loads(CERTIFICATE.read_text())
    module = load_producer()
    expected = expected_sections(module)
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
    if "No challenge-field model" not in contract:
        raise VerificationError("scope fence missing from contract")
    print("RATE_HALF_KB_M4_A6S6_GENUS_ZERO_PASSPORT_REDUCTION_PASS")
    print("RATE_HALF_KB_M4_A6S6_GENUS_ZERO_PASSPORT_MUTATIONS_12_OF_12_REJECTED")


if __name__ == "__main__":
    main()
