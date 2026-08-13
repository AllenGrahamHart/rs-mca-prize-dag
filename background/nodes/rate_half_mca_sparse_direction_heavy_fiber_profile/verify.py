#!/usr/bin/env python3
"""Verify the sparse-direction heavy-fiber profile compiler."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "11c2587813b0f6973198fc3c0c772c0193e43c7b4c099c05e1b5c79b9ef1d636"
PINNED = {
    "background/nodes/rate_half_mca_sparse_direction_affine_rank_payment/statement.md": "70eaf116e9934cf31a8e5e3ead007ab3da94a81dad38867705d6e3693dd76d49",
    "background/nodes/rate_half_mca_sparse_direction_affine_rank_payment/proof.md": "aa9a46a6902de83b96d5fff1db1815f4deb150fcbeb3cdf69de03a200abb6f6e",
    "background/nodes/upstream_gfv4_affine_span_list_compiler/statement.md": "b3be423dd1f85fff8811c98e7da41c03194b38975d89b1f860943e71334e3a31",
    "background/nodes/upstream_gfv4_affine_span_list_compiler/proof.md": "bc36d7a54e91ad5f82d14249b7e1e5c8270fc7c547ca8c37015f04997af01236",
}


class Reject(ValueError):
    pass


def profile_bound(R: int, d: int, rank: int, e: int) -> int:
    numerator = math.comb(R - e + rank, rank)
    previous = 0
    total = 0
    for h in range(1, e + 1):
        current = numerator // math.comb(d - h + rank, rank)
        total += (current - previous) * (e // h)
        previous = current
    return total


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "theorem", "rows"}:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-sparse-direction-heavy-fiber-profile-v1":
        raise Reject("version")
    if contract["sources"] != {
        "rank_payment": "rate_half_mca_sparse_direction_affine_rank_payment",
        "affine_list_compiler": "upstream_gfv4_affine_span_list_compiler",
    }:
        raise Reject("sources")
    if contract["theorem"] != {
        "outside_deficit": "h_a=m-|{x outside E:a(x)=r_0(x)}| with 1<=h_a<=e",
        "cumulative_explanation_cap": "B_h=floor(binomial(R-e+r,r)/binomial(d-h+r,r))",
        "slope_fiber_cap": "floor(e/h_a)",
        "profile_bound": "P(R,d,r,e)=sum_(h=1)^e (B_h-B_(h-1))*floor(e/h), with B_0=0",
        "ambient_dimension_independent": True,
    }:
        raise Reject("theorem")
    expected = {
        "KoalaBear MCA": (
            1048576, 67472, 274980728111395087,
            [(12, 1407, 274873552279452282, 1408, 275066073832310863),
             (13, 89, 274122309183156532, 90, 277203280658362178),
             (14, 5, 239418412614265435, 6, 287318134677474348),
             (15, 0, 0, 1, 743896698428332665)],
        ),
        "Mersenne-31 MCA": (
            1048576, 67448, 16777215,
            [(4, 287, 16750063, 288, 16808423),
             (5, 18, 16345664, 19, 17253587),
             (6, 1, 14115447, 2, 28231988),
             (7, 0, 0, 1, 219426634)],
        ),
    }
    checks = 0
    if len(contract["rows"]) != len(expected):
        raise Reject("row count")
    for row in contract["rows"]:
        walls = [
            (item.get("rank"), item.get("paid_prefix_end"), item.get("bound_at_end"),
             item.get("adjacent_first_unpaid"), item.get("bound_at_first_unpaid"))
            for item in row.get("rank_support_prefixes", ())
        ]
        values = (row.get("R"), row.get("d"), row.get("budget"), walls)
        if values != expected.get(row.get("name")):
            raise Reject("row constants")
        R, d, budget, _ = values
        for rank, end, end_value, first, first_value in walls:
            previous = -1
            for e in range(1, first + 1):
                value = profile_bound(R, d, rank, e)
                checks += 1
                if value < previous:
                    raise Reject("prefix monotonicity")
                previous = value
                if e <= end and value > budget:
                    raise Reject("unpaid prefix")
            if first != end + 1:
                raise Reject("adjacency")
            if end == 0:
                if end_value != 0:
                    raise Reject("empty end")
            elif profile_bound(R, d, rank, end) != end_value:
                raise Reject("end value")
            if profile_bound(R, d, rank, first) != first_value:
                raise Reject("first value")
            if not end_value <= budget < first_value:
                raise Reject("budget boundary")
    return {"checks": checks}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINNED.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"source pin: {relative}")
    contract = json.loads(CONTRACT.read_text())
    result = validate(contract)
    controls = []
    for row_index, wall_index, key in (
        (0, 0, "paid_prefix_end"),
        (0, 1, "bound_at_first_unpaid"),
        (1, 0, "bound_at_end"),
        (1, 2, "adjacent_first_unpaid"),
    ):
        changed = copy.deepcopy(contract)
        changed["rows"][row_index]["rank_support_prefixes"][wall_index][key] += 1
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_SPARSE_DIRECTION_HEAVY_FIBER_PROFILE_PASS "
        f"checks={result['checks']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
