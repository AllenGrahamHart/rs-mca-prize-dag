#!/usr/bin/env python3
"""Check the reusable cell-3 common polynomial packets."""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PRODUCT = HERE / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
STRUCTURE = HERE / "rate_half_kb_positive_433_1b_cell3_compact_structure_result.json"
KERNEL = HERE / "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
RESULT = HERE / "rate_half_kb_positive_433_1b_cell3_cached_common_input_result.json"
PRODUCT_SHA256 = "ee4dcb25877e9101a544ee5896b9bf6890059d6398c78d7562127b0d1c53c293"
STRUCTURE_SHA256 = "2f8712f2a942bb46f153d5204c4f4c8f9bff08336c295db4f31aef10fb5d22b7"
KERNEL_SHA256 = "e20ccb714b252f00ee3ce877ee68eff032f43deb877e2097919151436ddcf789"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    require(hashlib.sha256(PRODUCT.read_bytes()).hexdigest() == PRODUCT_SHA256,
            "product custody")
    require(hashlib.sha256(STRUCTURE.read_bytes()).hexdigest() == STRUCTURE_SHA256,
            "structure custody")
    require(hashlib.sha256(KERNEL.read_bytes()).hexdigest() == KERNEL_SHA256,
            "kernel custody")
    payload = json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell3-cached-common-input-v1",
            "schema")
    require(payload["complete"] is True and payload["field"] == 2130706433,
            "complete field result")
    require(payload["source_product_sha256"] == PRODUCT_SHA256 and
            payload["source_structure_sha256"] == STRUCTURE_SHA256 and
            payload["source_kernel_sha256"] == KERNEL_SHA256,
            "source fields")
    require(payload["expected_row_count"] == 4 and
            payload["processed_row_count"] == 4 and len(payload["rows"]) == 4,
            "row census")
    expected_signs = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    require([row["epsilon"] for row in payload["rows"]] == expected_signs,
            "ordered sign cover")
    packet_hashes = []
    for row in payload["rows"]:
        require(row["status"] == "COMPLETE", "complete row")
        packet = row["packet"]
        require(packet["variables"] == ["t", "r", "c", "b"], "variable order")
        require(len(packet["common_equations"]) == 3 and
                len(packet["kernel"]) == 8 and
                len(packet["route_guards"]) == 16 and
                len(packet["rank_cofactors"]) == 6,
                "packet shape")
        encoded = json.dumps(packet, separators=(",", ":"), sort_keys=True)
        digest = hashlib.sha256(encoded.encode()).hexdigest()
        require(row["packet_sha256"] == digest, "packet hash")
        require(len(row["equation_hashes"]) == 3 and
                len(row["kernel_hashes"]) == 8, "source hash vectors")
        packet_hashes.append(digest)
    require(len(set(packet_hashes)) == 4, "distinct sign packets")
    print("RATE_HALF_KB_POSITIVE_433_1B_CELL3_CACHED_COMMON_INPUT_CHECK_PASS "
          "rows=4 equations=12 kernel_entries=32 rank_charts=24")


if __name__ == "__main__":
    main()
