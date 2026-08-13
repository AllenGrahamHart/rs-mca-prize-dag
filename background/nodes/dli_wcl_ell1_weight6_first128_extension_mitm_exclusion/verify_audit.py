#!/usr/bin/env python3
"""Independent artifact audit for the extension-row MITM packet."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "experiments/prize_resolution"
PRIMARY = BASE / "dli_wcl_ell1_weight6_extension_row_mitm_result.json"
SOURCE = BASE / "dli_wcl_ell1_weight6_extension_row_mitm_audit.cpp"
RESULT = BASE / "dli_wcl_ell1_weight6_extension_row_mitm_audit_result.json"
PAIR_COUNT = 129_540
TRIPLE_COUNT = 21_849_080
INDICES = [0, 63, 64, 127]


class Reject(ValueError):
    pass


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(data: object, primary: list[dict[str, object]]) -> None:
    if not isinstance(data, dict):
        raise Reject("audit object")
    if (
        set(data) != {"schema", "status", "indices", "rows", "worker_errors"}
        or data["schema"] != "dli-wcl-ell1-weight6-extension-row-mitm-audit-v1"
        or data["status"] != "COMPLETE"
        or data["indices"] != INDICES
        or data["worker_errors"] != []
        or not isinstance(data["rows"], list)
        or len(data["rows"]) != 4
    ):
        raise Reject("audit header")
    for index, row in zip(INDICES, data["rows"]):
        expected = primary[index]
        p = row.get("p")
        omega = row.get("omega")
        if (
            row.get("index") != index
            or row.get("status") != "EXHAUSTED"
            or row.get("pair_count") != PAIR_COUNT
            or row.get("triples_scanned") != TRIPLE_COUNT
            or row.get("seed") != expected["seed"]
            or p != expected["p"]
            or omega != expected["omega"]
            or not isinstance(p, int)
            or not isinstance(omega, int)
            or pow(omega, 512, p) != 1
            or pow(omega, 256, p) != p - 1
        ):
            raise Reject(f"audit row {index}")


def main() -> None:
    if digest(SOURCE) != "c2b877ded7e60ed347fbdb925306b581c1e9e60b9e41f4d9f092a0d350a045ea":
        raise Reject("independent source hash")
    if digest(RESULT) != "b99d200e4457b89ed27c83d977647ef3df540a8389c2c45302df5880b7f887c6":
        raise Reject("audit result hash")
    if PAIR_COUNT != math.comb(510, 2) - 255:
        raise Reject("pair ledger")
    if TRIPLE_COUNT != math.comb(510, 3) - 255 * 508:
        raise Reject("triple ledger")
    primary_data = json.loads(PRIMARY.read_text())
    primary = primary_data.get("rows")
    if not isinstance(primary, list) or len(primary) != 128:
        raise Reject("primary dependency")
    data = json.loads(RESULT.read_text())
    validate(data, primary)

    controls = []
    for key, value in (
        ("status", "FOUND"),
        ("pair_count", PAIR_COUNT - 1),
        ("triples_scanned", TRIPLE_COUNT - 1),
        ("omega", 1),
    ):
        altered = copy.deepcopy(data)
        altered["rows"][0][key] = value
        try:
            validate(altered, primary)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("audit mutation control")
    print(
        "DLI_WCL_ELL1_WEIGHT6_FIRST128_EXTENSION_AUDIT_PASS "
        f"rows=128 independent_replays=4 controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
