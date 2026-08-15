#!/usr/bin/env python3
"""Verify the uniform corank-two projective-basis cap."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "0eefc50e8452fb30d8dba4cf94ecfc639ae618dba34a1662ef9decf7de4f2cfd"
ROOT = Path(__file__).resolve().parents[3]


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def row(t: int, r: int, w: int, target: int) -> dict[str, int]:
    resource = (r + t) * (r + t + 1) * (r + t + 2)
    basis = 3 * w * (w + t + 1)
    cap, remainder = divmod(resource, basis)
    return {
        "t": t,
        "resource": resource,
        "ordered_basis_floor": basis,
        "record_cap": cap,
        "division_remainder": remainder,
        "next_integer_gap": (target + 1) * basis - resource,
    }


def validate(data: object, files: bool) -> int:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-corank2-uniform-projective-basis-cap-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_corank2_projective_basis_cap",
        "rate_half_mca_rank11_kernel_projective_paving_integer_gap_fence",
        "rate_half_mca_support_local_transversality_compiler",
        "matroid_rank3_bounded_parallel_basis_floor",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["R"], p["w"], p["dimension"]) == (1048576, 67472, 2), "base parameters")
    require((p["t_minimum"], p["t_maximum"]) == (0, 1048566), "t range")
    require(p["parallel_class_ceiling"] == "t+1", "parallel ceiling")
    require(p["ordered_basis_floor"] == "3*w*(w+t+1)", "basis floor")
    require(p["ratio_step_sign"] == "2*t+3*w+3-R", "ratio sign")
    target = int(p["uniform_record_cap"])
    require(target == 84416263, "target cap")
    expected_rows = (
        ("complete_row", 0),
        ("adjacent_row", 1),
        ("official_endpoint", int(p["t_maximum"])),
    )
    for name, t in expected_rows:
        require(p[name] == row(t, int(p["R"]), int(p["w"]), target), name)
        require(p[name]["record_cap"] <= target, f"{name} cap")
        require(p[name]["next_integer_gap"] > 0, f"{name} next integer")
    require((p["turn_left"], p["turn_right"]) == (423078, 423079), "turn")
    require(2 * p["turn_left"] + 3 * p["w"] + 3 - p["R"] == -1, "left sign")
    require(2 * p["turn_right"] + 3 * p["w"] + 3 - p["R"] == 1, "right sign")
    require(p["complete_row"]["record_cap"] > p["official_endpoint"]["record_cap"], "endpoint maximum")
    require("does not select" in str(data.get("nonclaim")), "nonclaim")
    evidence = data.get("evidence")
    require(isinstance(evidence, dict), "evidence")
    require((evidence["checked_rows"], evidence["worker_timeout_seconds"], evidence["worker_memory_mb"], evidence["max_containers"]) == (
        1048567, 60, 512, 1
    ), "evidence limits")

    if files:
        script = ROOT / evidence["script"]
        result = ROOT / evidence["result"]
        require(hashlib.sha256(script.read_bytes()).hexdigest() == evidence["script_sha256"], "script hash")
        require(hashlib.sha256(result.read_bytes()).hexdigest() == evidence["result_sha256"], "result hash")
        payload = json.loads(result.read_text())
        require(payload["complete"] is True, "completion")
        require(payload["schema"] == evidence["result_schema"], "result schema")
        require(payload["scan"] == {
            "checked_rows": 1048567,
            "first_excess": None,
            "first_maximizer": 0,
            "maximum_record_cap": target,
        }, "scan custody")
        require(payload["rows"]["complete"] == {**p["complete_row"], "ratio_step_sign": -846157}, "complete custody")
        require(payload["rows"]["adjacent"] == {**p["adjacent_row"], "ratio_step_sign": -846155}, "adjacent custody")
        require(payload["rows"]["official_endpoint"] == {**p["official_endpoint"], "ratio_step_sign": 1250975}, "endpoint custody")
    return len(expected_rows)


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    rows = validate(data, True)
    mutations = (
        lambda item: item["parameters"].__setitem__("uniform_record_cap", 84416262),
        lambda item: item["parameters"].__setitem__("parallel_class_ceiling", "t+2"),
        lambda item: item["parameters"].__setitem__("ratio_step_sign", "t+3*w-R"),
        lambda item: item["parameters"]["adjacent_row"].__setitem__("record_cap", 84416264),
        lambda item: item["parameters"].__setitem__("turn_left", 423077),
        lambda item: item["evidence"].__setitem__("checked_rows", 1),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered, False)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_CORANK2_UNIFORM_PROJECTIVE_BASIS_CAP_PASS "
        f"cap=84416263 endpoints={rows} controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
