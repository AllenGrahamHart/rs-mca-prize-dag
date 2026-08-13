#!/usr/bin/env python3
"""Verify repaired direction-mismatch shortening envelopes."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "610813bd58e34e4c0e5892eb51011eab23b566c8859e5a58065744734f7e0c15"
PINNED = {
    "background/nodes/rate_half_mca_global_core_direction_distance_router/statement.md": "15bc1a798db19d80b025e4e16e758e6d8e932992873f1b306513525deb996bb2",
    "background/nodes/rate_half_mca_global_core_direction_distance_router/proof.md": "0f3ddfff5acd7c6d54af7e5347a8dccf614784c358b293263ed6164c90115b2b",
    "background/nodes/rate_half_kb_common_core_shortening_adapter_staircase_import/proof.md": "8cd269f1274bfb0d540e5c0bf54f1686149d031f8cd4628e007be57cd62c02a2",
}


class Reject(ValueError):
    pass


def direct_bound(R: int, d: int, s: int, j: int) -> int | None:
    n = R + s
    denominator = d * d - (R - 2 * d) * s - n * j
    if denominator <= 0 or j >= d:
        return None
    return n * (d - j) // denominator


def envelope(row: dict[str, object]) -> dict[str, object]:
    R, d, budget = (int(row[key]) for key in ("R", "d", "budget"))
    base = int(row["base_s"])
    base_max = int(row["base_max_j"])
    last_dimensions: list[int] = []
    direct_dimensions: list[int] = []
    iterations = 0
    for j in range(base_max + 1):
        value = direct_bound(R, d, base, j)
        if value is None or value > budget:
            raise Reject("base")
        s = base
        direct_last = base
        while True:
            next_s = s + 1
            recursive = (R - j) * value // (d - j)
            direct = direct_bound(R, d, next_s, j)
            if direct is not None and direct <= budget:
                direct_last = next_s
            candidate = min(recursive, direct) if direct is not None else recursive
            iterations += 1
            if candidate > budget:
                break
            value = candidate
            s = next_s
        last_dimensions.append(s)
        direct_dimensions.append(direct_last)
    next_base = direct_bound(R, d, base, base_max + 1)
    if next_base is not None and next_base <= budget:
        raise Reject("base adjacency")
    checkpoints = []
    for s, _ in row["checkpoints"]:
        frontier = max((j for j, last in enumerate(last_dimensions) if last >= s), default=-1)
        checkpoints.append([s, frontier])
    return {
        "checkpoints": checkpoints,
        "extended_defects": sum(left > right for left, right in zip(last_dimensions, direct_dimensions)),
        "maximum_extension": max(left - right for left, right in zip(last_dimensions, direct_dimensions)),
        "rank_regular_last_s": last_dimensions[0],
        "iterations": iterations,
    }


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "recurrence", "rows"}:
        raise Reject("shape")
    if contract["schema"] != "rate-half-mca-direction-mismatch-recursive-shortening-v2":
        raise Reject("schema")
    if contract["sources"] != {
        "global_direction_gate": "rate_half_mca_global_core_direction_distance_router",
        "cancellation_adapter": "rate_half_kb_common_core_shortening_adapter_staircase_import",
    }:
        raise Reject("sources")
    if contract["recurrence"] != {
        "minimum_lift_support": "|E|=R-j",
        "witness_incidence_floor": "|S_gamma intersect E|>=d-j",
        "child_parameters": "(R+s-1,s-1,d+s-1)",
        "child_defect": "j_x<=j",
        "step": "M_s(j)<=floor((R-j)M_(s-1)(j)/(d-j)) for 0<=j<d",
    }:
        raise Reject("recurrence")
    expected = {
        "KoalaBear MCA": (1048576,67472,274980728111395087,1,4340,4341,10,4992),
        "Mersenne-31 MCA": (1048576,67448,16777215,1,4337,4044,1,4979),
    }
    iterations = 0
    for row in contract["rows"]:
        values = tuple(row.get(key) for key in (
            "R", "d", "budget", "base_s", "base_max_j",
            "extended_defects", "maximum_extension", "rank_regular_last_s"
        ))
        if values != expected.get(row.get("name")):
            raise Reject("row")
        result = envelope(row)
        iterations += result["iterations"]
        for key in ("checkpoints", "extended_defects", "maximum_extension", "rank_regular_last_s"):
            if result[key] != row[key]:
                raise Reject(key)
    return {"iterations": iterations}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINNED.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"source pin: {relative}")
    contract = json.loads(CONTRACT.read_text())
    result = validate(contract)
    controls = []
    for index, key in ((0, "base_max_j"), (0, "maximum_extension"), (1, "extended_defects")):
        changed = copy.deepcopy(contract)
        changed["rows"][index][key] += 1
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_DIRECTION_MISMATCH_RECURSIVE_SHORTENING_PASS "
        f"iterations={result['iterations']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
