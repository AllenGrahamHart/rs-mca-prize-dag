#!/usr/bin/env python3
"""Verify the F02 mixed collision-exclusion proof packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
HASHES = {
    "f02_mixed_collision_primary.sage":
        "0af9ac23b992663b905002ed3af0fc1d21f456cee4de37769f50cafe4b7bb9a8",
    "f02_mixed_collision_audit.sage":
        "6c970e9cd05d1ddb9279085fca09576b890f62177c43dac74bbe1bcae9b492f9",
    "f02_mixed_collision_modal.py":
        "147572c07817d1d9bb4249ae76f30c4f2676b168edf6ce05ccc797fa0d738fb6",
    "f02_mixed_collision_output.json":
        "e3746c39c21ac49e5e1201029f36abfddd684c5d318c8f75f38bc545f84cfbbf",
}
CELLS = {"F02-A-RM", "F02-OB-RM"}
PRIMARY_BASES = {"F02-A-RM": 6, "F02-OB-RM": 7}
PRIMARY_DIGESTS = {
    "F02-A-RM":
        "31bb6f848859550aae71774f255ad7b58163e88d7a484902355809626448021a",
    "F02-OB-RM":
        "a0683962d17548fa21fbd1b081ff98120158c40bb4dedf6aa5ee0de9c5cb3c89",
}
LOCALIZER_DIGEST = (
    "2810dcb8ddd37f7c87082bcc957d85dbe117697890ad674eea68546fac5bb51a"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


for name, expected in HASHES.items():
    actual = hashlib.sha256((NODE / name).read_bytes()).hexdigest()
    require(actual == expected, f"hash: {name}")

payload = json.loads((NODE / "f02_mixed_collision_output.json").read_text())
require(
    payload["schema"] == "kb-c2-112-near-positive-f02-mixed-collision-modal-v1",
    "schema",
)
results = payload["results"]
require(set(results) == {"primary", "audit"}, "methods")

for cell, row in results["primary"].items():
    require(cell in CELLS, f"primary cell: {cell}")
    require(row["status"] == "PASS" and row["returncode"] == 0, f"primary: {cell}")
    result = row["payload"]
    require(result["collision_remainder"] == "0", f"collision remainder: {cell}")
    require(result["pre_collision_basis_size"] == PRIMARY_BASES[cell], f"basis: {cell}")
    require(
        result["pre_collision_basis_sha256"] == PRIMARY_DIGESTS[cell],
        f"basis digest: {cell}",
    )
    require(result["unit_ideal"] is True, f"primary unit: {cell}")
    require(result["terminal"] == "COLLISION_SATURATED_UNIT_IDEAL", f"terminal: {cell}")

for cell, row in results["audit"].items():
    require(cell in CELLS, f"audit cell: {cell}")
    require(row["status"] == "PASS" and row["returncode"] == 0, f"audit: {cell}")
    result = row["payload"]
    require(result["localizer_count"] == 14, f"localizers: {cell}")
    require(result["localizer_product_degree"] == 18, f"degree: {cell}")
    require(result["localizer_product_terms"] == 132, f"terms: {cell}")
    require(result["localizer_product_sha256"] == LOCALIZER_DIGEST, f"localizer digest: {cell}")
    require(result["basis_size"] == 1 and result["unit_ideal"] is True, f"audit unit: {cell}")
    require(result["terminal"] == "RABINOWITSCH_UNIT_IDEAL", f"audit terminal: {cell}")

print(
    "KB_C2_112_NEAR_POSITIVE_F02_MIXED_COLLISION_EXCLUSIONS_PASS "
    "cells=2 primary=collision_saturation audit=rabinowitsch frontier=24"
)
