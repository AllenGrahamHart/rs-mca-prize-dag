#!/usr/bin/env python3
"""Verify the direction-support affine-basis MCA payment."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "876a14f1386caafd12c5227cbb88be352eb05fc7d9ca9d26c55b75eb68e7d6e0"
PINNED = {
    "background/nodes/rate_half_mca_codeword_direction_gauge_rank_router/statement.md": "4e8bbe3ba4bda528d2dc88c071704379d6f3647928376df35c1927fbab30185e",
    "background/nodes/rate_half_mca_codeword_direction_gauge_rank_router/proof.md": "7af81043ed3fc0b17a672cb4f323f1c1bb8fb6d4bc08562ac36d5f35d01cd5d5",
    "background/nodes/rate_half_mca_supportwise_affine_span_compiler/statement.md": "08bd599c71cf40b4ee53a7eb7483f0b16f99f77616234ceb737ce08301922190",
    "background/nodes/rate_half_mca_supportwise_affine_span_compiler/proof.md": "97915ef59268ab5c1eb64e31b6947c6380ce2ee9cebbd95b61f66153d18e9ae3",
}


class Reject(ValueError):
    pass


def falling(x: int, length: int) -> int:
    return math.prod(range(x - length + 1, x + 1))


def rising(x: int, length: int) -> int:
    return math.prod(range(x, x + length))


def envelope(R: int, d: int, K: int, rank: int) -> tuple[int, int, str]:
    ambient = (falling(R + K, rank + 1), (d + K) * rising(d, rank))
    rank_endpoint = (falling(R + rank, rank + 1), rising(d, rank + 1))
    if ambient[0] * rank_endpoint[1] >= rank_endpoint[0] * ambient[1]:
        return ambient[0], ambient[1], "ambient_cap"
    return rank_endpoint[0], rank_endpoint[1], "rank_endpoint"


def support_bound(R: int, d: int, K: int, rank: int, e: int) -> int:
    numerator, denominator, _ = envelope(R, d, K, rank)
    base = falling(R + rank, rank + 1)
    support_numerator = base - falling(R + rank - e, rank + 1)
    return (numerator * support_numerator) // (denominator * base)


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "theorem", "rows"}:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-direction-support-affine-basis-payment-v1":
        raise Reject("version")
    if contract["sources"] != {
        "gauge_rank_router": "rate_half_mca_codeword_direction_gauge_rank_router",
        "supportwise_incidence": "rate_half_mca_supportwise_affine_span_compiler",
    }:
        raise Reject("sources")
    if contract["theorem"] != {
        "minimum_lift_support": "1<=e=|supp(r_1-b)|<=R",
        "active_basis_numerator": "(n-z)_fall_(r+1)-(n-e-z)_fall_(r+1)",
        "support_factor": "P(R,r,e)=1-(R+r-e)_fall_(r+1)/(R+r)_fall_(r+1)",
        "bound": "floor(P(R,r,e)*max((R+K)_fall_(r+1)/((d+K)d_rise_r),(R+r)_fall_(r+1)/d_rise_(r+1)))",
    }:
        raise Reject("theorem")
    expected = {
        "KoalaBear MCA": (
            1048576, 67472, 274980728111395087, 1048576,
            [(11, 1048576, 49107626893329409, None, None),
             (12, 15903, 274972626068661685, 15904, 274988375895649069),
             (13, 435, 274696020639658311, 436, 275325800101492947),
             (14, 13, 274045236375554780, 14, 295123669059482852),
             (15, 0, 0, 1, 698803577325965886)],
        ),
        "Mersenne-31 MCA": (
            1048576, 67448, 16777215, 1048576,
            [(4, 1048576, 1756139, None, None),
             (5, 62235, 16777006, 62236, 16777236),
             (6, 1486, 16768344, 1487, 16779580),
             (7, 41, 16506471, 42, 16909011),
             (8, 1, 14082980, 2, 28165853),
             (9, 0, 0, 1, 486473420)],
        ),
    }
    if len(contract["rows"]) != len(expected):
        raise Reject("row count")
    checks = 0
    for row in contract["rows"]:
        walls = [
            (item.get("rank"), item.get("last_paid_e"), item.get("bound_last"),
             item.get("first_unpaid_e"), item.get("bound_first_unpaid"))
            for item in row.get("rank_support_walls", ())
        ]
        values = (row.get("R"), row.get("d"), row.get("budget"), row.get("K_cap"), walls)
        if values != expected.get(row.get("name")):
            raise Reject("row constants")
        R, d, budget, K_cap, _ = values
        for rank, last, last_value, first, first_value in walls:
            _, _, owner = envelope(R, d, K_cap, rank)
            checks += 1
            if owner != "ambient_cap":
                raise Reject("uniform endpoint owner")
            observed_last = 0 if last == 0 else support_bound(R, d, K_cap, rank, last)
            checks += 1
            if observed_last != last_value or observed_last > budget:
                raise Reject("last value")
            if first is None:
                if last != R or first_value is not None:
                    raise Reject("full support wall")
            else:
                if first != last + 1:
                    raise Reject("adjacency")
                observed_first = support_bound(R, d, K_cap, rank, first)
                checks += 1
                if observed_first != first_value or observed_first <= budget:
                    raise Reject("first value")
            for e in {1, max(1, last), min(R, last + 1), R}:
                x = R + rank - e
                difference = falling(x, rank + 1) - falling(x - 1, rank + 1)
                expected_difference = (rank + 1) * falling(x - 1, rank)
                checks += 1
                if e < R and (difference != expected_difference or difference <= 0):
                    raise Reject("support monotonicity")
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
        (0, 1, "last_paid_e"),
        (0, 3, "bound_first_unpaid"),
        (1, 1, "bound_last"),
        (1, 4, "first_unpaid_e"),
    ):
        changed = copy.deepcopy(contract)
        changed["rows"][row_index]["rank_support_walls"][wall_index][key] += 1
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_DIRECTION_SUPPORT_AFFINE_BASIS_PAYMENT_PASS "
        f"checks={result['checks']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
