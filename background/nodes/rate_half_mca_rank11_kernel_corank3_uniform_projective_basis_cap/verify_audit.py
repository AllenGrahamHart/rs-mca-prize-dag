#!/usr/bin/env python3
"""Independent endpoint and recurrence audit for uniform corank three."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "598eb55c00ce2778fa57b185360f80208b5ae34b418a001bd5293b55d6669a7d"
R = 1048576
RANK_GAP = 67474
T_MAX = R - 10
TARGET = 983902549


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def h_value(a: int, r: int) -> int:
    return min((a + 1) // 2, (a + r) // 4)


def direct_floor6(a: int, r: int = RANK_GAP) -> int:
    value = 6
    for current in range(4, r + 1):
        coloop = (a + current - 1) * (current - 1) * (current - 2)
        increment = 3 * (a + current - h_value(a, current) - 1) * (current - 2)
        value = min(coloop, value + increment)
    return value


def direct_row(t: int) -> dict[str, int]:
    floor6 = direct_floor6(t + 1)
    n = R + t + 3
    resource = n * (n - 1) * (n - 2) * (n - 3)
    ordered = 4 * floor6
    cap, remainder = divmod(resource, ordered)
    return {
        "t": t,
        "basis_floor_times_6": floor6,
        "ordered_basis_floor": ordered,
        "record_cap": cap,
        "division_remainder": remainder,
        "next_integer_gap": (TARGET + 1) * ordered - resource,
    }


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    contract = json.loads(CONTRACT.read_text())
    evidence = contract["evidence"]
    result_path = ROOT / evidence["result"]
    require(hashlib.sha256(result_path.read_bytes()).hexdigest() == evidence["result_sha256"], "result hash")
    result = json.loads(result_path.read_text())
    samples = {
        "complete": 0,
        "adjacent": 1,
        "first_nontrivial": 2,
        "middle": T_MAX // 2,
        "official_endpoint": T_MAX,
    }
    checks = 0
    for key, t in samples.items():
        expected = direct_row(t)
        actual = result["rows"][key]
        for field, value in expected.items():
            require(actual[field] == value, f"{key} {field}")
            checks += 1
        require(expected["next_integer_gap"] > 0, f"{key} gap")
    scan = result["scan"]
    require(scan["checked_rows"] == T_MAX + 1, "scan rows")
    require((scan["maximum_record_cap"], scan["first_maximizer"]) == (TARGET, 0), "scan maximum")
    require(scan["first_excess"] is None, "scan excess")
    require(scan["branch_counts"] == {"base": 7, "reset": 1048560}, "branch census")
    require((scan["recurrence_checks"], scan["residue_checks"]) == (9440, 2240), "audit grids")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_CORANK3_UNIFORM_PROJECTIVE_BASIS_CAP_AUDIT_PASS "
        f"sample_checks={checks} rows={scan['checked_rows']} branches=7/1048560"
    )


if __name__ == "__main__":
    main()
