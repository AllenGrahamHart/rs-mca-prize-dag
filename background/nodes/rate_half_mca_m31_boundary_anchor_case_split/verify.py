#!/usr/bin/env python3
"""Verify the Mersenne boundary-anchor case split."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "f3b0dec86cd2d5fe518793ce10e42f7493e5b8b66d5dd5641704b7e1440af3cd"
PINS = {
    "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/statement.md":
        "b1fa6c8ce0dfe3eca422dec52348346dae7d342a77c71ad685bcb88ef23f4632",
    "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/proof.md":
        "523c35fc8eefa4d8ea9612b2bc6ecd48373af2e9d09e5791eacc441309f2308b",
    "background/nodes/rate_half_mca_full_lift_top_third_global_line_payment/statement.md":
        "8d103c4c092961387fa02ee18ff851a084c0f7774c0b4b238d1e7fba42dbe02d",
    "background/nodes/rate_half_mca_full_lift_top_third_global_line_payment/proof.md":
        "5abca3dd268f99b38c483fb12b22c9c7d91e0908b5a4ef389195b648651e3cb2",
}


class Reject(ValueError):
    pass


def cumulative_cap(R: int, d: int, K: int, e: int, h: int) -> int | None:
    n, m, c = R + K - e, d + K, K - 1
    A = m - h
    D = A * A - n * c
    if D > 0:
        return n * (A - c) // D
    g = -D
    balance = 2 * A * A - n * c
    T = (n - A) ** 2 - (n - 1) * g
    if g < 0 or balance < 0 or T <= 0:
        return None
    return (n - 1) * n * n * (A - c) // (A * T)


def prefix(R: int, d: int, K: int, e: int, J: int) -> tuple[int, int, int]:
    caps = [0]
    for h in range(1, J + 1):
        value = cumulative_cap(R, d, K, e, h)
        if value is None:
            raise Reject("undefined cap")
        caps.append(value)
    for h in range(J - 1, 0, -1):
        caps[h] = min(caps[h], caps[h + 1])
    total = sum(
        (caps[h] - caps[h - 1]) * (e // h) for h in range(1, J + 1)
    )
    breaks = sum(caps[h] != caps[h - 1] for h in range(1, J + 1))
    return total, breaks, caps[J]


def record(R: int, d: int, K: int, e: int) -> dict[str, int]:
    N, m = R + K, d + K
    s, q = divmod(e - K, 3)
    H = e - s - 1
    if H < 2 or q < 1 or 2 * (s + 1) >= e or m - H <= K - 1:
        raise Reject("theorem hypotheses")
    P_H, breaks_H, B_H = prefix(R, d, K, e, H)
    P_previous, breaks_previous, B_previous = prefix(R, d, K, e, H - 1)
    line_cap = N - m + 1
    small = P_H + 1
    anchors = P_previous + line_cap
    return {
        "s": s, "q": q, "H": H, "line_cap": line_cap,
        "P_H": P_H, "P_H_breaks": breaks_H, "B_H": B_H,
        "P_previous": P_previous,
        "P_previous_breaks": breaks_previous,
        "B_previous": B_previous,
        "small_tail_case": small, "two_anchor_case": anchors,
        "bound": max(small, anchors),
    }


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
        "schema", "sources", "theorem", "row"
    }:
        raise Reject("schema keys")
    if payload["schema"] != "rate-half-mca-m31-boundary-anchor-case-split-v1":
        raise Reject("schema")
    if payload["theorem"] != "max(P_H+1,P_(H-1)+(N-m+1))":
        raise Reject("theorem")
    expected_sources = {
        "mean_global_statement_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/statement.md"
        ],
        "mean_global_proof_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/proof.md"
        ],
        "top_third_statement_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_top_third_global_line_payment/statement.md"
        ],
        "top_third_proof_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_top_third_global_line_payment/proof.md"
        ],
    }
    if payload["sources"] != expected_sources:
        raise Reject("sources")
    row = payload["row"]
    got = record(row["R"], row["d"], row["K"], row["e"])
    for key, value in got.items():
        if row[key] != value:
            raise Reject(f"endpoint {key}")
    if row["slack"] != row["budget"] - got["bound"] or row["slack"] <= 0:
        raise Reject("slack")
    if row["e"] - 3 * row["s"] - 1 != row["K"] + row["q"] - 1:
        raise Reject("mixed triple")
    adjacent = record(row["R"], row["d"], row["K"], row["adjacent_e"])
    adjacent_keys = {
        "q": "adjacent_q", "P_H": "adjacent_P_H",
        "P_previous": "adjacent_P_previous",
        "small_tail_case": "adjacent_small_tail_case",
        "two_anchor_case": "adjacent_two_anchor_case",
        "bound": "adjacent_bound",
    }
    for key, contract_key in adjacent_keys.items():
        if adjacent[key] != row[contract_key]:
            raise Reject(f"adjacent {key}")
    if row["adjacent_excess"] != adjacent["bound"] - row["budget"]:
        raise Reject("adjacent excess")
    if row["adjacent_excess"] <= 0 or row["residual_ceiling"] < row["adjacent_e"]:
        raise Reject("residual")
    return 28


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINS.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {relative}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    controls = []
    for key, delta in (("P_H", 1), ("two_anchor_case", -1),
                       ("adjacent_bound", -1), ("slack", 1)):
        changed = copy.deepcopy(payload)
        changed["row"][key] += delta
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_M31_BOUNDARY_ANCHOR_CASE_SPLIT_PASS "
        f"checks={checks} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
