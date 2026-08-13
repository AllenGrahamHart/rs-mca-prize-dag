#!/usr/bin/env python3
"""Verify the direction-support affine-basis refutation."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
REFUTER = HERE.parent / "rate_half_mca_affine_span_incidence_counterexample" / "source_contract.json"
if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != "ea3cabe68da8fe5f7fc08f5e9591c32b08738e69b502a0c6493282ab9d9cf37d":
    raise ValueError("contract hash")
if hashlib.sha256(REFUTER.read_bytes()).hexdigest() != "7c0d75814b99fa6272e8c005ee93fd78220bb5717ea9211a84dec67c0bcd9f8a":
    raise ValueError("refuter hash")
contract = json.loads(CONTRACT.read_text())
refuter = json.loads(REFUTER.read_text())
p = contract["parameters"]
bound = ((p["R"] + p["K"]) * (p["R"] + p["K"] - 1) - (p["R"] + p["K"] - p["e"]) * (p["R"] + p["K"] - p["e"] - 1)) // ((p["d"] + p["K"]) * p["d"])
if bound != contract["claimed_bound"] or bound != refuter["expected"]["support_bound"] or not contract["slopes"] > bound:
    raise ValueError("refutation")
print("RATE_HALF_MCA_DIRECTION_SUPPORT_AFFINE_BASIS_REFUTED_PASS slopes=31 bound=22")
