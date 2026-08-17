#!/usr/bin/env python3
"""Verify the first basis-fed outside orbit exclusion."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_diagnostic_result.json"
QUOTIENT = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_quotient.py"
RESULT_SHA256 = "e7ea616f603636f8286225e5cd851cdacd8ea1a32e56ba87825a9a2c9e46898d"
CASE = (3, "S0", -1, -1, -1, 0, 0)
EXPECTED_ORBIT = {
    (3, "S0", -1, -1, -1, 0, 0),
    (3, "S0", -1, -1, -1, 0, 4),
    (6, "S0", -1, -1, 1, 1, 7),
    (6, "S0", -1, -1, 1, 1, 11),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_quotient():
    spec = importlib.util.spec_from_file_location("cells3_6_quotient", QUOTIENT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify(payload=None, expected_orbit=EXPECTED_ORBIT):
    require(hashlib.sha256(RESULT.read_bytes()).hexdigest() == RESULT_SHA256,
            "result custody")
    payload = payload or json.loads(RESULT.read_text())
    row = payload["row"]
    require(payload["complete"] is True and tuple(payload["case"]) == CASE,
            "complete canonical case")
    require(row["status"] == "COMPLETE" and row["unit"] is True and
            row["dimension"] == -1 and row["basis_size"] == 1,
            "unit result")
    require(row["common_basis_size"] == 21 and
            row["outside_equation_count"] == 5 and row["guard_count"] == 40 and
            row["rank_cofactor_count"] == 6, "input ledger")
    stdout = row["stdout"]
    require("INITIAL_DIM=3,INITIAL_SIZE=108" in stdout and
            "SAT=4,DIM=3,SIZE=82\nSAT=5,DIM=-1,SIZE=1" in stdout and
            "BEGIN\nDIM=-1\nSIZE=1\nUNIT=1\nEND" in stdout,
            "boundary transcript")
    quotient = load_quotient()
    matchings = tuple(quotient.BC.pairings(range(6)))
    first = quotient.bc_action(CASE, matchings)
    second = quotient.secondary_action(CASE)
    orbit = {CASE, first, second, quotient.bc_action(second, matchings)}
    require(orbit == expected_orbit, "four-case orbit")
    return {"raw": len(orbit), "representatives": 1}


def main():
    result = verify()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_CASE0_VERIFY_PASS "
          f"raw={result['raw']} representatives={result['representatives']}")


if __name__ == "__main__":
    main()
