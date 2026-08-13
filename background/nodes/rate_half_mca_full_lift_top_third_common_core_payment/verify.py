#!/usr/bin/env python3
"""Verify the full-lift top-third common-core payment."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "53abad99118d8c726d7d13edf5792d4e53c1bd22460623e2783a5e5a0795cc9a"
PINNED = {
    "background/nodes/rate_half_mca_full_lift_near_mds_extension_reduction/statement.md":
        "aa0fab1f4a1c31e7bc3bad3942d01d407a1a682d31431bc9964f9afce82f1a0b",
    "background/nodes/rate_half_mca_full_lift_near_mds_extension_reduction/proof.md":
        "2c60cbb8ebdeff0c31a4631f41d69b095c1599f33a26fa336410b57544198420",
    "background/nodes/rate_half_mca_sparse_direction_top_third_affine_line_payment/statement.md":
        "d076028804ae5734d589e824fa35f6b5c4db3dceed5e85db112d3d1228c50683",
    "background/nodes/rate_half_mca_sparse_direction_top_third_affine_line_payment/proof.md":
        "36615b434d592f9c68034de004fcb6f2199bb62efc9e1ec708edf3ba9f31f1e4",
}


class Reject(ValueError):
    pass


def grouped_floor_sum(numerator: int, first: int, last: int) -> int:
    if last < first:
        return 0
    total = 0
    x = first
    while x <= last:
        quotient = numerator // x
        end = min(last, numerator // quotient)
        total += quotient * (end - x + 1)
        x = end + 1
    return total


def profile(R: int, d: int, K: int, e: int) -> dict[str, int] | None:
    N, m, c = R + K, d + K, K - 1
    t = N - m
    s = (e - K) // 3
    H = e - s - 1
    u = e // 2
    r0 = max(0, e - m)
    if r0 > s or N - m <= s:
        return None

    n = N - e
    A_u = m - u
    A_H = m - H
    D_u = A_u * A_u - n * c
    D_H = A_H * A_H - n * c
    if D_u <= 0 or D_H <= 0:
        return None
    J_u = n * (A_u - c) // D_u
    J_H = n * (A_H - c) // D_H

    A0 = m - e + r0
    A1 = m - e + s
    low = max(0, min(A1, c) - A0 + 1)
    first_den = max(1, A0 - c)
    last_den = A1 - c
    outside = grouped_floor_sum(n - c, first_den, last_den)
    line = low * (t + 1) + outside
    prefix = (e - 1) * J_u + J_H
    return {
        "s": s, "H": H, "u": u,
        "A_u": A_u, "A_H": A_H,
        "J_u": J_u, "J_H": J_H,
        "H_denominator": D_H,
        "line_sum": line, "prefix": prefix, "total": prefix + line,
    }


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {
        "schema", "sources", "theorem", "rows"
    }:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-full-lift-top-third-common-core-payment-v1":
        raise Reject("version")
    if contract["sources"] != {
        "near_mds_reduction": "rate_half_mca_full_lift_near_mds_extension_reduction",
        "top_third_lines": "rate_half_mca_sparse_direction_top_third_affine_line_payment",
    }:
        raise Reject("sources")
    if contract["theorem"] != {
        "layer_range": "max(0,e-m)<=r<=floor((e-K)/3)",
        "total_core_cap": "N-m+1",
        "outside_cap": "floor((N-e-(K-1))/(m-e+r-(K-1))) when m-e+r>K-1",
        "profile": "(e-1)J_floor(e/2)+J_H+sum_r Q_r",
    }:
        raise Reject("theorem")

    bases = {
        "KoalaBear MCA": (1048576, 67472, 14, 274980728111395087, 95944, 1044238),
        "Mersenne-31 MCA": (1048576, 67448, 6, 16777215, 67453, 1044241),
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
        if first is None or last is None:
            raise Reject("endpoint availability")
        if first["total"] != row["first_total"]:
            raise Reject("first total")
        mapping = {
            "last_s": "s", "last_H": "H", "last_u": "u",
            "last_A_u": "A_u", "last_A_H": "A_H",
            "last_J_u": "J_u", "last_J_H": "J_H",
            "last_H_denominator": "H_denominator",
            "last_line_sum": "line_sum", "last_prefix": "prefix",
            "last_total": "total",
        }
        for target, source in mapping.items():
            if row[target] != last[source]:
                raise Reject(target)
            checks += 1

        max_line = (-1, -1)
        for e in range(row["first_new_e"], row["last_paid_e"] + 1):
            current = profile(R, d, K, e)
            if current is None or current["total"] > budget:
                raise Reject("strip")
            if current["line_sum"] > max_line[0]:
                max_line = (current["line_sum"], e)
            checks += 1
        if max_line != (row["max_line_sum"], row["max_line_sum_e"]):
            raise Reject("max line")

        adjacent = profile(R, d, K, row["adjacent_e"])
        if name == "KoalaBear MCA":
            e = row["adjacent_e"]
            s = (e - K) // 3
            H = e - s - 1
            n = R + K - e
            A = d + K - H
            denominator = A * A - n * (K - 1)
            if adjacent is not None or (
                H, denominator, row["adjacent_total"]
            ) != (
                row["adjacent_H"], row["adjacent_H_denominator"], None
            ):
                raise Reject("KoalaBear adjacent")
        elif adjacent is None or (
            adjacent["H"], adjacent["H_denominator"], adjacent["total"]
        ) != (
            row["adjacent_H"], row["adjacent_H_denominator"], row["adjacent_total"]
        ) or adjacent["total"] <= budget:
            raise Reject("Mersenne adjacent")
        if (row["residual_floor"], row["residual_ceiling"]) != (
            residual_floor, residual_ceiling
        ):
            raise Reject("residual")
        checks += 5
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
        (0, "last_line_sum", 1),
        (0, "adjacent_H_denominator", 1),
        (1, "last_total", 1),
        (1, "adjacent_total", -1),
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
        "RATE_HALF_MCA_FULL_LIFT_TOP_THIRD_COMMON_CORE_PAYMENT_PASS "
        f"checks={result['checks']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
