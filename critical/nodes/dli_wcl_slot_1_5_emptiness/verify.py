#!/usr/bin/env python3
"""Verify compact custody for the complete WCL `(1,5)` certificate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKET_ROOT = ROOT / "notes/pilots_20260806/wcl15_finish"
EXPECTED_SHA256 = {
    "prime_vocabulary_inventory.json": (
        "25597e973edb63c822af4a8b8b71506e4ecf68f629046aabcdda19ea6d535a31"
    ),
    "full_batch_replay.json": (
        "04dc6160585c122a9022b922d867bde6d64967a16a41359d6c327c4f03dd5c6c"
    ),
    "tail_independent_cert.json": (
        "2292b2a5fccc61fba288dc8566904237b2ce4db05a0c7a83587720512d94c5ba"
    ),
    "tail191_factor_cert.json": (
        "37fc520d9f5e2f34da0e6e8e5bed3e5ed8e735258f88fc8f29c509b266517271"
    ),
}


def fail(label: str, value: object = None) -> None:
    raise AssertionError((label, value))


def check_embedded_digest(packet: dict[str, object], field: str) -> None:
    expected = packet.get(field)
    body = {key: value for key, value in packet.items() if key != field}
    actual = hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if actual != expected:
        fail(field, (actual, expected))


def load_packets() -> dict[str, dict[str, object]]:
    packets = {}
    for name, expected in EXPECTED_SHA256.items():
        raw = (PACKET_ROOT / name).read_bytes()
        actual = hashlib.sha256(raw).hexdigest()
        if actual != expected:
            fail(name + " SHA-256", actual)
        packets[name] = json.loads(raw)
    return packets


def validate(packets: dict[str, dict[str, object]]) -> None:
    vocabulary = packets["prime_vocabulary_inventory.json"]
    if (
        vocabulary.get("schema") != "wcl15-prime-vocabulary-inventory-v1"
        or vocabulary.get("status") != "COMPLETE"
        or vocabulary.get("validated_batches") != 35_890
        or vocabulary.get("class_count") != 2_296_920
        or vocabulary.get("factor_records") != 6_528_119
        or vocabulary.get("shard_prime_records") != 6_177_403
        or vocabulary.get("distinct_easy_primes") != 4_443_651
        or vocabulary.get("maximum_v2_prime_minus_1") != 30
        or vocabulary.get("high_gate_factors") != []
        or vocabulary.get("representative_sha256")
        != "9ac0ca650e704a13514180fe2d8bcea94943c771f125b3942888a6aba8c87f00"
    ):
        fail("easy vocabulary")
    check_embedded_digest(vocabulary, "result_digest")

    replay = packets["full_batch_replay.json"]
    if (
        replay.get("schema") != "wcl15-full-batch-replay-v1"
        or replay.get("status") != "COMPLETE"
        or replay.get("complete_groups") != 100
        or replay.get("expected_groups") != 100
        or replay.get("missing_groups") != []
        or replay.get("incomplete_groups") != []
        or replay.get("missing_batches") != 0
        or replay.get("duplicate_batches") != 0
    ):
        fail("full replay envelope")
    expected_counts = {
        "checked_batches": 35_890,
        "checked_rows": 2_296_920,
        "checked_primes": 6_177_403,
        "checked_factor_records": 6_528_119,
        "unresolved_rows": 194,
    }
    if any(replay.get(key) != value for key, value in expected_counts.items()):
        fail("full replay counts")
    groups = replay.get("groups")
    if not isinstance(groups, list) or len(groups) != 100:
        fail("group count")
    cursor = 0
    sums = {key: 0 for key in expected_counts}
    for index, group in enumerate(groups):
        if (
            group.get("group_index") != index
            or group.get("start_batch") != cursor
            or group.get("status") != "COMPLETE"
            or group.get("error") is not None
        ):
            fail("group custody", index)
        end = group.get("end_batch")
        if not isinstance(end, int) or end <= cursor:
            fail("group interval", index)
        if group.get("checked_batches") != end - cursor:
            fail("group batch count", index)
        cursor = end
        for key in sums:
            sums[key] += int(group[key])
    if cursor != 35_890 or sums != expected_counts:
        fail("group partition", (cursor, sums))
    if replay.get("custody_digest") != (
        "975220600606e8f9fac4de09d7d350121ea04ea3de23b9e492fb0651b331e033"
    ):
        fail("replay custody digest")
    check_embedded_digest(replay, "result_digest")

    tails = packets["tail_independent_cert.json"]
    if (
        tails.get("schema") != "wcl15-independent-hard-tail-cert-v1"
        or tails.get("status") != "COMPLETE_193_PENDING_191"
        or tails.get("manifest_rows") != 194
        or tails.get("certified_tail_rows") != 193
        or tails.get("pending_tail_indices") != [191]
        or tails.get("primality_checks") != 400
        or tails.get("distinct_primes") != 399
        or tails.get("maximum_v2_prime_minus_1") != 17
        or tails.get("high_gate_factors") != []
    ):
        fail("193-tail certificate")
    check_embedded_digest(tails, "certificate_digest")

    final = packets["tail191_factor_cert.json"]
    if (
        final.get("schema") != "wcl15-tail191-independent-factor-cert-v1"
        or final.get("status") != "COMPLETE"
        or final.get("norm_bits") != 269
        or final.get("factor_product_exact") is not True
        or final.get("primality_checks") != 2
        or final.get("maximum_v2_prime_minus_1") != 12
        or final.get("high_gate_factors") != []
    ):
        fail("tail-191 envelope")
    rows = final.get("factors")
    if not isinstance(rows, list) or len(rows) != 2:
        fail("tail-191 factor rows")
    factors = [int(row["prime"]) for row in rows]
    if math.prod(factors) != int(final["norm"]):
        fail("tail-191 factor product")
    if [row["bits"] for row in rows] != [112, 158]:
        fail("tail-191 bits")
    if [row["v2_prime_minus_1"] for row in rows] != [9, 12]:
        fail("tail-191 valuations")
    if any(row["official_gate"] or not row["below_2_256"] for row in rows):
        fail("tail-191 gate")
    check_embedded_digest(final, "certificate_digest")

    if max(
        int(vocabulary["maximum_v2_prime_minus_1"]),
        int(tails["maximum_v2_prime_minus_1"]),
        int(final["maximum_v2_prime_minus_1"]),
    ) != 30:
        fail("global maximum depth")


def tamper_selftest(packets: dict[str, dict[str, object]]) -> int:
    mutations = [
        ("full_batch_replay.json", "checked_rows", 2_296_921),
        ("full_batch_replay.json", "missing_batches", 1),
        ("tail_independent_cert.json", "pending_tail_indices", []),
        ("tail191_factor_cert.json", "maximum_v2_prime_minus_1", 41),
        ("prime_vocabulary_inventory.json", "high_gate_factors", ["x"]),
    ]
    rejected = 0
    for name, key, value in mutations:
        altered = copy.deepcopy(packets)
        altered[name][key] = value
        try:
            validate(altered)
        except AssertionError:
            rejected += 1
        else:
            fail("accepted hostile mutation", (name, key))
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    packets = load_packets()
    validate(packets)
    rejected = tamper_selftest(packets) if args.tamper_selftest else 0
    print(
        "WCL15_CERTIFICATE_PASS "
        f"rows=2296920 easy=2296726 tails=194 max_v2=30 "
        f"tamper_rejected={rejected}"
    )


if __name__ == "__main__":
    main()
