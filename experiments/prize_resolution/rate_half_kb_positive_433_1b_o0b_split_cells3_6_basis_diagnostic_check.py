#!/usr/bin/env python3
"""Check a complete unit cells-3/6 global-basis diagnostic."""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CACHE = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
BASIS = HERE / "rate_half_kb_positive_433_1b_cell3_global_common_basis_result.json"
CORE = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_cached_outside_core.py"
RESULT = HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_basis_diagnostic_result.json"
CACHE_SHA256 = "28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8"
BASIS_SHA256 = "bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e"
CASE = [3, "S0", -1, -1, -1, 0, 0]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    require(hashlib.sha256(CACHE.read_bytes()).hexdigest() == CACHE_SHA256,
            "cache custody")
    require(hashlib.sha256(BASIS.read_bytes()).hexdigest() == BASIS_SHA256,
            "basis custody")
    cache = json.loads(CACHE.read_text())
    basis = json.loads(BASIS.read_text())
    payload = json.loads(RESULT.read_text())
    row = payload["row"]
    packet_row = next(value for value in cache["rows"] if value["epsilon"] == [-1, -1])
    basis_row = next(value for value in basis["rows"] if value["epsilon"] == [-1, -1])
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-split-cells3-6-basis-diagnostic-v1",
            "schema")
    require(payload["complete"] is True and payload["field"] == 2130706433 and
            payload["case"] == CASE, "complete case")
    require(payload["source_cache_sha256"] == CACHE_SHA256 and
            payload["source_basis_sha256"] == BASIS_SHA256 and
            payload["source_core_sha256"] ==
            hashlib.sha256(CORE.read_bytes()).hexdigest(), "source fields")
    require(row["status"] == "COMPLETE" and row["unit"] is True and
            row["dimension"] == -1 and row["basis_size"] == 1,
            "unit result")
    require(row["common_basis_size"] == 21 and
            row["outside_equation_count"] == 5 and
            row["guard_count"] == 40 and row["rank_cofactor_count"] == 6,
            "input ledger")
    require(row["packet_sha256"] == packet_row["packet_sha256"] and
            row["basis_sha256"] == basis_row["basis_sha256"],
            "sign input custody")
    require(row["input_program"] == "" and row["stderr"] == "",
            "compact clean output")
    require("INITIAL_DIM=" in row["stdout"] and
            "COFACTOR_DIM=-1,COFACTOR_SIZE=1" in row["stdout"] and
            "BEGIN\nDIM=-1\nSIZE=1\nUNIT=1\nEND" in row["stdout"] and
            "?" not in row["stdout"], "complete transcript")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_BASIS_DIAGNOSTIC_CHECK_PASS "
          "case=1 unit=1 common_basis=21 outside_equations=5")


if __name__ == "__main__":
    main()
