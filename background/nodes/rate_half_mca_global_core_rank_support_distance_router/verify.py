#!/usr/bin/env python3
"""Verify the rank/support router regression and surviving gates."""

import copy
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "779e1498f5a47b0900e10ae001f2575d8050d70961b04dc5a58de3216375b257"


class Reject(ValueError):
    pass


def validate(contract: object) -> int:
    if not isinstance(contract, dict) or contract.get("schema") != "rate-half-mca-global-core-rank-support-replacement-target-v2":
        raise Reject("schema")
    if contract.get("status") != "TARGET" or contract.get("refuter") != "rate_half_mca_affine_span_incidence_counterexample":
        raise Reject("status")
    if contract.get("retracted") != ["affine-rank gate", "direction-support affine-basis gate", "common-zero gate"]:
        raise Reject("retracted")
    expected = {
        "KoalaBear MCA": (14, 1048576, 5, 4337, 1044239),
        "Mersenne-31 MCA": (6, 1048576, 1, 4334, 1044242),
    }
    checks = 0
    for row in contract["first_gates"]:
        values = tuple(row[key] for key in ("s", "R", "low_e", "frontier_j", "high_e"))
        if values != expected.get(row["row"]):
            raise Reject("row")
        if row["high_e"] != row["R"] - row["frontier_j"]:
            raise Reject("conversion")
        checks += 1
    return checks


if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
    raise Reject("contract hash")
contract = json.loads(CONTRACT.read_text())
checks = validate(contract)
changed = copy.deepcopy(contract)
changed["first_gates"][0]["high_e"] += 1
try:
    validate(changed)
except Reject:
    mutation = 1
else:
    raise AssertionError("mutation")
print(f"RATE_HALF_MCA_GLOBAL_CORE_RANK_SUPPORT_REPLACEMENT_TARGET_PASS gates={checks} mutations={mutation}/1")
