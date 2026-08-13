#!/usr/bin/env python3
"""Verify the full-lift top-third global-line payment."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "e769fbff60173dc27ab951c03627eb627c4835ad5cb057bb80c66f3ec677be79"
PINNED = {
    "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/statement.md":
        "767b9a387abf3606d5ccb990846789b45afa92e3489a4c10169443a55a139edf",
    "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/proof.md":
        "677c8378f7bf2f87dfc10a5340e3a0861a1124a3cc68e460e61bd42dc9c32c1d",
}


class Reject(ValueError):
    pass


def profile(R: int, d: int, K: int, e: int) -> dict[str, int] | None:
    N, m, c = R + K, d + K, K - 1
    n = N - e
    s = (e - K) // 3
    H = e - s - 1
    u = e // 2
    values = []
    denominators = []
    for h in (u, H):
        A = m - h
        denominator = A * A - n * c
        denominators.append(denominator)
        if denominator <= 0:
            return None
        values.append(n * (A - c) // denominator)
    prefix = (e - 1) * values[0] + values[1]
    return {
        "s": s, "H": H, "u": u,
        "J_u": values[0], "J_H": values[1],
        "H_denominator": denominators[1],
        "global_line_cap": N - m + 1,
        "prefix": prefix,
        "total": prefix + N - m + 1,
    }


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {
        "schema", "sources", "theorem", "rows"
    }:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-full-lift-top-third-global-line-payment-v1":
        raise Reject("version")
    if contract["sources"] != {
        "per_layer_common_core": "rate_half_mca_full_lift_top_third_common_core_payment"
    }:
        raise Reject("sources")
    if contract["theorem"] != {
        "cross_layer_threshold": "r_i+r_j+r_k<=3*floor((e-K)/3)<=e-K",
        "global_line_cap": "N-m+1",
        "profile": "(e-1)J_floor(e/2)+J_H+(N-m+1)",
    }:
        raise Reject("theorem")

    bases = {
        "KoalaBear MCA": (1048576, 67472, 14, 274980728111395087, 95944, 1044238),
        "Mersenne-31 MCA": (1048576, 67448, 6, 16777215, 97909, 1044241),
    }
    checks = 0
    for row in contract["rows"]:
        name = row.get("name")
        if name not in bases:
            raise Reject("name")
        R, d, K, budget, residual_floor, residual_ceiling = bases[name]
        if tuple(row.get(key) for key in ("R", "d", "K", "budget")) != (R, d, K, budget):
            raise Reject("base")
        first = profile(R, d, K, row["first_new_e"])
        last = profile(R, d, K, row["last_paid_e"])
        if first is None or last is None or first["total"] != row["first_total"]:
            raise Reject("endpoints")
        mapping = {
            "last_s": "s", "last_H": "H", "last_u": "u",
            "last_J_u": "J_u", "last_J_H": "J_H",
            "last_H_denominator": "H_denominator",
            "global_line_cap": "global_line_cap",
            "last_prefix": "prefix", "last_total": "total",
        }
        for target, source in mapping.items():
            if row[target] != last[source]:
                raise Reject(target)
            checks += 1

        maximum = (-1, -1)
        for e in range(row["first_new_e"], row["last_paid_e"] + 1):
            current = profile(R, d, K, e)
            if current is None or current["total"] > budget:
                raise Reject("strip")
            if current["total"] > maximum[0]:
                maximum = (current["total"], e)
            checks += 1
        if maximum != (row["max_total"], row["max_total_e"]):
            raise Reject("maximum")

        adjacent = row["adjacent_e"]
        if profile(R, d, K, adjacent) is not None:
            raise Reject("adjacent available")
        s = (adjacent - K) // 3
        H = adjacent - s - 1
        n = R + K - adjacent
        A = d + K - H
        denominator = A * A - n * (K - 1)
        if (H, denominator) != (
            row["adjacent_H"], row["adjacent_H_denominator"]
        ):
            raise Reject("adjacent record")
        if (row["residual_floor"], row["residual_ceiling"]) != (
            residual_floor, residual_ceiling
        ):
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
        (0, "last_total", 1),
        (0, "adjacent_H_denominator", 1),
        (1, "max_total", -1),
        (1, "global_line_cap", 1),
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
        "RATE_HALF_MCA_FULL_LIFT_TOP_THIRD_GLOBAL_LINE_PAYMENT_PASS "
        f"checks={result['checks']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
