#!/usr/bin/env python3
"""Verify the Mersenne residue-two boundary-layer case split."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "f3891ed7a69bcc33b8df02186d59ecdc99563be7d3efe4f977ee256a8be60c1b"
PINS = {
    "background/nodes/rate_half_mca_m31_boundary_anchor_case_split/statement.md":
        "8376a7b148ec4d7f8ee99bc0dbb41e5961a404184a8bced1eeff1c54c8822d8d",
    "background/nodes/rate_half_mca_m31_boundary_anchor_case_split/proof.md":
        "6fefba234c0ef750ac2e85c19559d9ca9c2de3a748772fd79e226af7c465c977",
    "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/statement.md":
        "767b9a387abf3606d5ccb990846789b45afa92e3489a4c10169443a55a139edf",
    "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/proof.md":
        "677c8378f7bf2f87dfc10a5340e3a0861a1124a3cc68e460e61bd42dc9c32c1d",
}


class Reject(ValueError):
    pass


def cumulative_cap(R: int, d: int, K: int, e: int, h: int) -> int | None:
    n, m, c = R + K - e, d + K, K - 1
    agreement = m - h
    johnson = agreement * agreement - n * c
    if johnson > 0:
        return n * (agreement - c) // johnson
    gap = -johnson
    balance = 2 * agreement * agreement - n * c
    tangent = (n - agreement) ** 2 - (n - 1) * gap
    if gap < 0 or balance < 0 or tangent <= 0:
        return None
    return ((n - 1) * n * n * (agreement - c)
            // (agreement * tangent))


def prefix(R: int, d: int, K: int, e: int, end: int) -> tuple[int, int, int]:
    caps = [0]
    for h in range(1, end + 1):
        value = cumulative_cap(R, d, K, e, h)
        if value is None:
            raise Reject("undefined cap")
        caps.append(value)
    for h in range(end - 1, 0, -1):
        caps[h] = min(caps[h], caps[h + 1])
    total = sum((caps[h] - caps[h - 1]) * (e // h)
                for h in range(1, end + 1))
    breaks = sum(caps[h] != caps[h - 1] for h in range(1, end + 1))
    return total, breaks, caps[end]


def record(R: int, d: int, K: int, e: int) -> dict[str, object]:
    N, m, c = R + K, d + K, K - 1
    s, q = divmod(e - K, 3)
    H = e - s - 1
    n = N - e
    if q != 2 or H < 3 or 2 * (s + 2) >= e or m - H <= c:
        raise Reject("theorem hypotheses")
    # The source theorem requires every cap through H to exist.
    prefix(R, d, K, e, H)
    p2, b2, z2 = prefix(R, d, K, e, H - 2)
    p1, b1, z1 = prefix(R, d, K, e, H - 1)
    line = N - m + 1
    outside = (n - c) // (m - H - c)
    disjoint = e // (s + 1)
    cases = {
        "two_top_anchors": p2 + line,
        "one_top_boundary_line": p1 + outside + 1,
        "one_top_small_boundary": p1 + 2,
        "no_top_boundary_line": p1 + outside,
        "no_top_disjoint_boundary": p1 + disjoint,
    }
    return {
        "s": s,
        "q": q,
        "H": H,
        "line_cap": line,
        "outside_line_cap": outside,
        "disjoint_cap": disjoint,
        "P_H_minus_2": p2,
        "P_H_minus_2_breaks": b2,
        "B_H_minus_2": z2,
        "P_H_minus_1": p1,
        "P_H_minus_1_breaks": b1,
        "B_H_minus_1": z1,
        "cases": cases,
        "bound": max(cases.values()),
    }


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
        "schema", "sources", "theorem", "row"
    }:
        raise Reject("schema keys")
    if payload["schema"] != "rate-half-mca-m31-two-boundary-layer-case-split-v1":
        raise Reject("schema")
    if payload["theorem"] != (
        "max(P_(H-2)+(t+1),P_(H-1)+Q+1,P_(H-1)+2,"
        "P_(H-1)+Q,P_(H-1)+D)"
    ):
        raise Reject("theorem")
    expected_sources = {
        "one_boundary_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_boundary_anchor_case_split/statement.md"
        ],
        "one_boundary_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_boundary_anchor_case_split/proof.md"
        ],
        "common_core_statement_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/statement.md"
        ],
        "common_core_proof_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/proof.md"
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
    if row["e"] - 3 * row["s"] - 2 != row["K"]:
        raise Reject("mixed triple equality")
    adjacent_q = (row["adjacent_e"] - row["K"]) % 3
    if adjacent_q != row["adjacent_q"] or adjacent_q != 0:
        raise Reject("adjacent residue")
    try:
        record(row["R"], row["d"], row["K"], row["adjacent_e"])
    except Reject:
        pass
    else:
        raise Reject("adjacent theorem unexpectedly legal")
    if row["residual_ceiling"] < row["adjacent_e"]:
        raise Reject("residual")
    return 31


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINS.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {relative}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    controls = []
    for path, delta in (
        (("outside_line_cap",), 1),
        (("cases", "two_top_anchors"), -1),
        (("bound",), -1),
        (("slack",), 1),
    ):
        changed = copy.deepcopy(payload)
        target = changed["row"]
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] += delta
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_M31_TWO_BOUNDARY_LAYER_CASE_SPLIT_PASS "
        f"checks={checks} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
