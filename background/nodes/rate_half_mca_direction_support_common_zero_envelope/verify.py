#!/usr/bin/env python3
"""Verify the common-zero envelope refutation."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
REFUTER = HERE.parent / "rate_half_mca_affine_span_incidence_counterexample" / "source_contract.json"
if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != "17bab359e18267cb3721b4809d5c6df9ddc033ebb076bcebe3a22f28bf077513":
    raise ValueError("contract hash")
if hashlib.sha256(REFUTER.read_bytes()).hexdigest() != "7c0d75814b99fa6272e8c005ee93fd78220bb5717ea9211a84dec67c0bcd9f8a":
    raise ValueError("refuter hash")
contract = json.loads(CONTRACT.read_text())
p = contract["parameters"]
values = []
for x in range(p["R"] + p["r"], p["R"] + p["K"] + 1):
    numerator = x * (x - 1) - (x - p["e"]) * (x - p["e"] - 1)
    denominator = (x - p["R"] + p["d"]) * p["d"]
    values.append(numerator // denominator)
bound = max(values)
if bound != contract["claimed_bound"] or not contract["slopes"] > bound:
    raise ValueError("refutation")
print("RATE_HALF_MCA_DIRECTION_SUPPORT_COMMON_ZERO_REFUTED_PASS slopes=31 bound=22")
