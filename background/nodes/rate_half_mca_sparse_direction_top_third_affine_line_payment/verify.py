#!/usr/bin/env python3
"""Verify the sparse-direction top-third affine-line payment."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "9132d3a2639804030b00e3f6d4c547ffd56430c0822b67cb318467c72e260b18"
PINNED = {
    "background/nodes/rate_half_mca_sparse_direction_terminal_deficit_line_payment/statement.md":
        "20787ec794b193f57a053f975c167c8e955e73e354cdac06f9697b6ed93f4960",
    "background/nodes/rate_half_mca_sparse_direction_terminal_deficit_line_payment/proof.md":
        "8fcd61a18f2855f8178e91e51be85b7eb6ed408c8de8d6b262989d0ed17733c5",
    "background/nodes/rate_half_mca_sparse_direction_punctured_johnson_profile/statement.md":
        "3cf121f53d306a72c6e624da54d7488a8036272e9013f54eceb87617923a2fdb",
    "background/nodes/rate_half_mca_sparse_direction_punctured_johnson_profile/proof.md":
        "109d04f93c9d4f0d506a5d5826f7a37241be174b96f8cb751dd3ca73e958092b",
}


class Reject(ValueError):
    pass


def endpoint(R: int, d: int, K: int) -> dict[str, int]:
    N = R + K
    m = d + K
    c = K - 1
    e = d - 1
    s = (e - K) // 3
    H = e - s - 1
    u = e // 2
    A_u = m - u
    A_H = m - H
    num_u = N * (A_u - c)
    den_u = A_u * A_u - N * c
    num_H = N * (A_H - c)
    den_H = A_H * A_H - N * c
    n = N - e
    A = m - e
    line_sum = sum((n - c) // (A + r - c) for r in range(s + 1))
    return {
        "endpoint_e": e,
        "s": s,
        "H": H,
        "u": u,
        "upper_n": N,
        "A_u_min": A_u,
        "J_u_numerator": num_u,
        "J_u_denominator": den_u,
        "A_H_min": A_H,
        "J_H_numerator": num_H,
        "J_H_denominator": den_H,
        "endpoint_punctured_length": n,
        "endpoint_terminal_agreement": A,
        "line_sum": line_sum,
        "uniform_total": (d - 2) * 31 + 47 + line_sum,
    }


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {
        "schema", "sources", "theorem", "uniform_caps", "rows"
    }:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-sparse-direction-top-third-affine-line-payment-v1":
        raise Reject("version")
    if contract["sources"] != {
        "terminal_line": "rate_half_mca_sparse_direction_terminal_deficit_line_payment",
        "johnson_profile": "rate_half_mca_sparse_direction_punctured_johnson_profile",
    }:
        raise Reject("sources")
    if contract["theorem"] != {
        "layer_range": "0<=r<=floor((e-K)/3)",
        "triple_overlap": "e-3r>=K",
        "outside_slack": "N-m>floor((e-K)/3)",
        "layer_cap": "floor((N-e-(K-1))/(m-e+r-(K-1)))",
        "coarse_profile": "(e-1)J_floor(e/2)+J_H+sum_r layer_cap",
    }:
        raise Reject("theorem")
    if contract["uniform_caps"] != {"J_floor_e_over_2": 31, "J_H": 47}:
        raise Reject("caps")

    bases = {
        "KoalaBear MCA": (1048576, 67472, 14, 274980728111395087, 67472, 1044238),
        "Mersenne-31 MCA": (1048576, 67448, 6, 16777215, 67448, 1044241),
    }
    if len(contract["rows"]) != 2:
        raise Reject("row count")
    checks = 0
    for row in contract["rows"]:
        name = row.get("name")
        if name not in bases:
            raise Reject("name")
        R, d, K, budget, floor, ceiling = bases[name]
        if tuple(row.get(key) for key in ("R", "d", "K", "budget")) != (R, d, K, budget):
            raise Reject("base")
        got = endpoint(R, d, K)
        if R - d <= got["s"]:
            raise Reject("outside slack")
        for key, value in got.items():
            if row.get(key) != value:
                raise Reject(key)
            checks += 1
        if got["J_u_denominator"] <= 0 or got["J_H_denominator"] <= 0:
            raise Reject("positive Johnson")
        if got["J_u_numerator"] // got["J_u_denominator"] > 31:
            raise Reject("J_u")
        if got["J_H_numerator"] // got["J_H_denominator"] > 47:
            raise Reject("J_H")
        if got["uniform_total"] > budget:
            raise Reject("budget")
        if (row["residual_floor"], row["residual_ceiling"]) != (floor, ceiling):
            raise Reject("residual")
        checks += 4
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
        (0, "line_sum", 1),
        (0, "J_H_denominator", 1),
        (1, "uniform_total", 1),
        (1, "residual_floor", 1),
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
        "RATE_HALF_MCA_SPARSE_DIRECTION_TOP_THIRD_AFFINE_LINE_PAYMENT_PASS "
        f"checks={result['checks']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
