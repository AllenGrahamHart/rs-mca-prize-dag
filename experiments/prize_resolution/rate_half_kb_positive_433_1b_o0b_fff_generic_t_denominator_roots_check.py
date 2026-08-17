#!/usr/bin/env python3
"""Hostile checker for the FFF generic-basis denominator root ledger."""

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "rate_half_kb_positive_433_1b_o0b_fff_generic_t_julia_result.json"
RESULT = HERE / (
    "rate_half_kb_positive_433_1b_o0b_fff_generic_t_denominator_roots_result.json"
)
PRIME = 2130706433
SOURCE_SHA256 = "c679e0c16cf2e64555c0c50a12eda54b8618e024563d7b6caabf5268bdaf518e"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def multiply(left, right):
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] = (output[i + j] + a * b) % PRIME
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def root_polynomial(roots):
    output = [1]
    for root in roots:
        output = multiply(output, [(-root) % PRIME, 1])
    return output


def evaluate(coefficients, value):
    output = 0
    for coefficient in reversed(coefficients):
        output = (output * value + coefficient) % PRIME
    return output


def verify(payload=None):
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "source custody")
    source = json.loads(SOURCE.read_text())
    denominators = source["row"]["unique_denominators"]
    payload = payload or json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-fff-denominator-roots-v1",
            "schema")
    require(payload["collection_complete"] is True and
            payload["field"] == PRIME and
            payload["source_sha256"] == SOURCE_SHA256, "envelope")
    row = payload["row"]
    require(row["status"] == "COMPLETE" and
            row["method"] ==
            "FLINT gcd(D,t^p-t), linear factorization, LCM union check" and
            row["denominator_count"] == len(denominators) == 44 and
            row["raw_degree_sum"] == sum(len(value) - 1 for value in denominators)
            and row["lcm_degree"] > 0, "result profile")
    require(row["roots"] == sorted(set(row["roots"])) and
            row["root_count"] == len(row["roots"]) and
            row["field_root_polynomial"] == root_polynomial(row["roots"]),
            "combined roots")
    require(len(row["rows"]) == len(denominators), "row count")
    union = set()
    for index, (entry, denominator) in enumerate(zip(row["rows"], denominators)):
        digest = hashlib.sha256(
            json.dumps(denominator, separators=(",", ":")).encode()
        ).hexdigest()
        require(entry["index"] == index and entry["degree"] == len(denominator) - 1
                and entry["denominator_sha256"] == digest, "row custody")
        require(entry["roots"] == sorted(set(entry["roots"])) and
                entry["field_root_polynomial"] == root_polynomial(entry["roots"]),
                "row roots")
        require(all(evaluate(denominator, root) == 0 for root in entry["roots"]),
                "claimed root")
        union.update(entry["roots"])
    require(sorted(union) == row["roots"] and
            all(any(evaluate(value, root) == 0 for value in denominators)
                for root in row["roots"]), "union")
    rows_text = json.dumps(row["rows"], separators=(",", ":"), sort_keys=True)
    require(row["rows_sha256"] == hashlib.sha256(rows_text.encode()).hexdigest(),
            "row hash")
    return row


def expect_rejected(payload, label):
    try:
        verify(payload)
    except RuntimeError:
        return
    raise RuntimeError(f"mutation survived: {label}")


def hostile_audit():
    payload = json.loads(RESULT.read_text())
    mutations = []
    mutation = deepcopy(payload)
    mutation["source_sha256"] = "0" * 64
    mutations.append((mutation, "source"))
    mutation = deepcopy(payload)
    mutation["row"]["root_count"] += 1
    mutations.append((mutation, "root count"))
    mutation = deepcopy(payload)
    mutation["row"]["rows"][0]["degree"] += 1
    mutations.append((mutation, "row"))
    if payload["row"]["roots"]:
        mutation = deepcopy(payload)
        mutation["row"]["roots"][0] = (mutation["row"]["roots"][0] + 1) % PRIME
        mutations.append((mutation, "root"))
    for mutation, label in mutations:
        expect_rejected(mutation, label)
    return len(mutations)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostile", action="store_true")
    args = parser.parse_args()
    row = verify()
    mutations = hostile_audit() if args.hostile else 0
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_DENOMINATOR_ROOTS_CHECK_PASS "
          f"roots={row['root_count']} mutations={mutations}/{mutations}")


if __name__ == "__main__":
    main()
