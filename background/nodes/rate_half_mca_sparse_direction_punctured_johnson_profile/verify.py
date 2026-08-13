#!/usr/bin/env python3
"""Verify the sparse-direction punctured Johnson profile."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "f485ce789dccf03b4767e63281bc404ba4529a750c8243e56b4946da484eeb08"
PINNED = {
    "background/nodes/rate_half_mca_sparse_direction_heavy_fiber_profile/statement.md": "b953ec015b2f4180e1086de29983cbd2d4aff2c3e67066493edc368af07891be",
    "background/nodes/rate_half_mca_sparse_direction_heavy_fiber_profile/proof.md": "28978c430f5d8159948a864e0e2c4a5ab3c12bfb7a5e727c5e73073c020a5465",
    "background/nodes/rate_half_mca_sparse_direction_punctured_list_payment/statement.md": "42bf5bc5ea77d245c56b45e19a94f862bf3596b490ecda17fe88fc01596775b6",
    "background/nodes/rate_half_mca_sparse_direction_punctured_list_payment/proof.md": "2ff6f0fc1accd77ac2a3bceeaf375f099605b654765d274ff2049dae241b2676",
}


class Reject(ValueError):
    pass


def denominator(R: int, d: int, K: int, e: int, h: int | None = None) -> int:
    if h is None:
        h = e
    return (d + K - h) ** 2 - (R + K - e) * (K - 1)


def johnson(R: int, d: int, K: int, e: int, h: int) -> int:
    if h == 0:
        return 0
    den = denominator(R, d, K, e, h)
    if den <= 0:
        raise Reject("nonpositive Johnson denominator")
    return (R + K - e) * (d - h + 1) // den


def coarse(R: int, d: int, K: int, e: int) -> int:
    return (e - 1) * johnson(R, d, K, e, e // 2) + johnson(R, d, K, e, e)


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "theorem", "rows"}:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-sparse-direction-punctured-johnson-profile-v1":
        raise Reject("version")
    if contract["sources"] != {
        "punctured_list_payment": "rate_half_mca_sparse_direction_punctured_list_payment",
        "heavy_fiber_profile": "rate_half_mca_sparse_direction_heavy_fiber_profile",
    }:
        raise Reject("sources")
    if contract["theorem"] != {
        "johnson_denominator": "D_e=(m-e)^2-(N-e)(K-1)>0",
        "cumulative_cap": "J_h=floor((N-e)(m-h-K+1)/((m-h)^2-(N-e)(K-1)))",
        "profile": "sum_(h=1)^e (J_h-J_(h-1))*floor(e/h), with J_0=0",
        "coarse_bound": "(e-1)J_floor(e/2)+J_e",
    }:
        raise Reject("theorem")

    expected = {
        "KoalaBear MCA": (
            1048576, 67472, 14, 274980728111395087, 63908, 984668,
            1218, -5924, 31954, 27, 2882094, 4607583, 63908,
        ),
        "Mersenne-31 MCA": (
            1048576, 67448, 6, 16777215, 65236, 983340,
            2794, -1636, 32618, 28, 778863, 2605443, 65236,
        ),
    }
    keys = (
        "R", "d", "K", "budget", "last_paid_e", "equivalent_defect_floor",
        "denominator_at_last", "denominator_at_next", "half_index",
        "johnson_at_half", "johnson_at_last", "coarse_bound_at_last",
        "coarse_maximizer",
    )
    if len(contract["rows"]) != 2:
        raise Reject("row count")

    checks = 0
    for row in contract["rows"]:
        values = tuple(row.get(key) for key in keys)
        if values != expected.get(row.get("name")):
            raise Reject("row constants")
        R, d, K, budget, last, defect, dlast, dnext, half, jhalf, jlast, qlast, maximizer = values
        if defect != R - last or half != last // 2:
            raise Reject("coordinate conversion")
        if denominator(R, d, K, last) != dlast or denominator(R, d, K, last + 1) != dnext:
            raise Reject("boundary denominators")
        if not dlast > 0 >= dnext:
            raise Reject("strict boundary")
        if johnson(R, d, K, last, half) != jhalf or johnson(R, d, K, last, last) != jlast:
            raise Reject("Johnson endpoint")
        if coarse(R, d, K, last) != qlast or qlast > budget:
            raise Reject("coarse endpoint")

        best = (-1, -1)
        previous_den = None
        for e in range(1, last + 1):
            den = denominator(R, d, K, e)
            if den <= 0:
                raise Reject("prefix positivity")
            if previous_den is not None and den >= previous_den:
                raise Reject("denominator descent")
            previous_den = den
            value = coarse(R, d, K, e)
            if value > budget:
                raise Reject("unpaid prefix")
            if value > best[1]:
                best = (e, value)
            checks += 1
        if best != (maximizer, qlast):
            raise Reject("coarse maximum")
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
    for row_index, key, delta in (
        (0, "last_paid_e", 1),
        (0, "johnson_at_last", 1),
        (1, "denominator_at_next", 1),
        (1, "coarse_maximizer", -1),
    ):
        changed = copy.deepcopy(contract)
        changed["rows"][row_index][key] += delta
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_SPARSE_DIRECTION_PUNCTURED_JOHNSON_PROFILE_PASS "
        f"checks={result['checks']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
