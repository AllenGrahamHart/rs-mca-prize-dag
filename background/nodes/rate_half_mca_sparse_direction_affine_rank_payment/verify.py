#!/usr/bin/env python3
"""Verify the sparse-direction affine-rank MCA payment."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "4067e90440ab4d8640074a9c1583a2fba162221956821e329d35dcfbc3e4315d"
PINNED = {
    "background/nodes/rate_half_mca_codeword_direction_gauge_rank_router/statement.md": "e2d58d0cdc4b958c996f27b383ebca65a377387aceb1fdf908d416c2815daa40",
    "background/nodes/rate_half_mca_codeword_direction_gauge_rank_router/proof.md": "f4a78a4eb5f397c9bade1a2b54689d31259a47be55ad20c3bd04e8c9037db564",
    "background/nodes/rate_half_mca_sparse_direction_punctured_list_payment/statement.md": "42bf5bc5ea77d245c56b45e19a94f862bf3596b490ecda17fe88fc01596775b6",
    "background/nodes/rate_half_mca_sparse_direction_punctured_list_payment/proof.md": "2ff6f0fc1accd77ac2a3bceeaf375f099605b654765d274ff2049dae241b2676",
}


class Reject(ValueError):
    pass


def bound(R: int, d: int, rank: int, e: int) -> int:
    quotient = math.comb(R - e + rank, rank) // math.comb(d - e + rank, rank)
    return e * quotient


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "theorem", "rows"}:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-sparse-direction-affine-rank-payment-v1":
        raise Reject("version")
    if contract["sources"] != {
        "gauge_rank_router": "rate_half_mca_codeword_direction_gauge_rank_router",
        "full_code_special_case": "rate_half_mca_sparse_direction_punctured_list_payment",
    }:
        raise Reject("sources")
    if contract["theorem"] != {
        "transformed_rank": "r=rank_aff(c_gamma-gamma b)",
        "direction_support": "e=|supp(r_1-b)| with 1<=e<d",
        "bound": "e*floor(binomial(R-e+r,r)/binomial(d-e+r,r))",
        "ambient_dimension_independent": True,
    }:
        raise Reject("theorem")
    expected = {
        "KoalaBear MCA": (
            1048576, 67472, 274980728111395087,
            [(12, 1144, 274849472034465328, 1145, 275136341921843765),
             (13, 87, 272256895343216442, 88, 275435997743171320),
             (14, 5, 239567470186217925, 6, 287536780021025682),
             (15, 0, 0, 1, 743896698428332665)],
        ),
        "Mersenne-31 MCA": (
            1048576, 67448, 16777215,
            [(4, 282, 16730778, 283, 16791239),
             (5, 18, 16363584, 19, 17273869),
             (6, 1, 14115447, 2, 28233244),
             (7, 0, 0, 1, 219426634)],
        ),
    }
    checks = 0
    for row in contract["rows"]:
        walls = [
            (item.get("rank"), item.get("last_paid_e"), item.get("bound_last"),
             item.get("first_unpaid_e"), item.get("bound_first_unpaid"))
            for item in row.get("rank_support_walls", ())
        ]
        values = (row.get("R"), row.get("d"), row.get("budget"), walls)
        if values != expected.get(row.get("name")):
            raise Reject("row constants")
        R, d, budget, _ = values
        for rank, last, last_value, first, first_value in walls:
            observed = 0
            previous = -1
            for e in range(1, d):
                value = bound(R, d, rank, e)
                checks += 1
                if value < previous:
                    raise Reject("monotonicity")
                previous = value
                if value <= budget:
                    observed = e
            if observed != last or first != last + 1:
                raise Reject("boundary")
            if last == 0:
                if last_value != 0:
                    raise Reject("empty last")
            elif bound(R, d, rank, last) != last_value:
                raise Reject("last value")
            if bound(R, d, rank, first) != first_value or not last_value <= budget < first_value:
                raise Reject("first value")
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
        (0, 0, "last_paid_e"), (0, 1, "bound_first_unpaid"),
        (1, 2, "bound_last"),
    ):
        changed = copy.deepcopy(contract)
        changed["rows"][row_index]["rank_support_walls"][wall_index][key] += 1
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    changed = copy.deepcopy(contract)
    changed["rows"][1]["rank_support_walls"][3]["last_paid_e"] = 1
    try:
        validate(changed)
    except Reject:
        controls.append(True)
    else:
        controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_SPARSE_DIRECTION_AFFINE_RANK_PAYMENT_PASS "
        f"checks={result['checks']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
