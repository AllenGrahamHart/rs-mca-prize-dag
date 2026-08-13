#!/usr/bin/env python3
"""Verify the affine-span compiler's refuted status."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
REFUTER = HERE.parent / "rate_half_mca_affine_span_incidence_counterexample" / "source_contract.json"

if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != "33353099a9eaeee37856c6cfd04fcf302cdcb05f5d2ad061d2e76174d129f74f":
    raise ValueError("contract hash")
if hashlib.sha256(REFUTER.read_bytes()).hexdigest() != "7c0d75814b99fa6272e8c005ee93fd78220bb5717ea9211a84dec67c0bcd9f8a":
    raise ValueError("refuter hash")
contract = json.loads(CONTRACT.read_text())
refuter = json.loads(REFUTER.read_text())
n, K, m, w, rank = contract["row"]
bound = max(n * (n - 1) // (m * w), n * (n - 1) // (w * (w + 1)))
if (
    contract["schema"] != "rate-half-mca-supportwise-affine-span-compiler-refuted-v2"
    or (n, K, m, w, rank) != (100, 1, 21, 20, 1)
    or bound != contract["claimed_bound"]
    or bound != refuter["expected"]["affine_span_bound"]
    or contract["slopes"] != refuter["selected"]["count"]
    or not contract["slopes"] > bound
):
    raise ValueError("refutation")
print("RATE_HALF_MCA_SUPPORTWISE_AFFINE_SPAN_COMPILER_REFUTED_PASS slopes=31 bound=23")
