#!/usr/bin/env python3
"""Verify direction-mismatch recursive shortening and deployed envelopes."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "d0354c1a0127c3527b405c3f57159e88624e4443439f29bce9e8ebec1a84514e"
PINNED = {
    "background/nodes/rate_half_mca_global_core_direction_distance_router/statement.md": "0bdbd9585b37372cd9ff4ccc708d28ad1e3c2d28dc45e93f151b934e99ada8df",
    "background/nodes/rate_half_mca_global_core_direction_distance_router/proof.md": "22844c8398ab217e5bf238be97edd64c9e939d7803c4a40b0e31b95176641196",
    "background/nodes/rate_half_kb_common_core_shortening_adapter_staircase_import/proof.md": "e6a338cd23adefb18fa73ddcda397f5e6f2eb30c313ff1b4f76446510adfce70",
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
    base, base_bound = (int(row[key]) for key in ("base_s", "base_bound"))
    last_dimensions: list[int] = []
    direct_dimensions: list[int] = []
    iterations = 0
    for j in range(d):
        direct = direct_bound(R, d, base, j)
        value = min(base_bound, direct) if direct is not None else base_bound
        s = base
        direct_last = base if direct is None or direct <= budget else base - 1
        while True:
            next_s = s + 1
            recursive = (R - j) * value // (d - j)
            direct = direct_bound(R, d, next_s, j)
            candidate = min(recursive, direct) if direct is not None else recursive
            if direct is not None and direct <= budget:
                direct_last = next_s
            iterations += 1
            if candidate > budget:
                break
            value = candidate
            s = next_s
        last_dimensions.append(s)
        direct_dimensions.append(max(base, direct_last))
    if any(left < right for left, right in zip(last_dimensions, last_dimensions[1:])):
        raise Reject("nonmonotone envelope")
    checkpoints = []
    for s, _ in row.get("checkpoints", []):
        frontier = next((j - 1 for j, last in enumerate(last_dimensions) if last < s), d - 1)
        checkpoints.append([s, frontier])
    return {
        "last_dimensions": last_dimensions,
        "checkpoints": checkpoints,
        "extended_defects": sum(last > base for last in last_dimensions),
        "maximum_extension": max(
            last - direct for last, direct in zip(last_dimensions, direct_dimensions)
        ),
        "rank_regular_last_s": last_dimensions[0],
        "iterations": iterations,
    }


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "recurrence", "rows"}:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-direction-mismatch-recursive-shortening-v1":
        raise Reject("version")
    if contract["sources"] != {
        "global_direction_router": "rate_half_mca_global_core_direction_distance_router",
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
        "KoalaBear MCA": (1048576, 67472, 274980728111395087, 13, 47876303026096432, 4331, 10, 4992),
        "Mersenne-31 MCA": (1048576, 67448, 16777215, 5, 14115447, 4335, 1, 4979),
    }
    rows = contract["rows"]
    if not isinstance(rows, list) or len(rows) != 2:
        raise Reject("rows")
    iterations = 0
    for row in rows:
        values = tuple(
            row.get(key)
            for key in (
                "R", "d", "budget", "base_s", "base_bound",
                "extended_defects", "maximum_extension", "rank_regular_last_s",
            )
        )
        if values != expected.get(row.get("name")):
            raise Reject("row constants")
        result = envelope(row)
        iterations += int(result["iterations"])
        for key in ("checkpoints", "extended_defects", "maximum_extension", "rank_regular_last_s"):
            if result[key] != row.get(key):
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
    for index, key in (
        (0, "maximum_extension"), (0, "rank_regular_last_s"),
        (1, "extended_defects"),
    ):
        changed = copy.deepcopy(contract)
        changed["rows"][index][key] += 1
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    changed = copy.deepcopy(contract)
    changed["rows"][1]["checkpoints"][0][1] -= 1
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
