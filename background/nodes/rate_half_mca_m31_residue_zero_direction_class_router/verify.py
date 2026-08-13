#!/usr/bin/env python3
"""Verify the Mersenne residue-zero direction-class router."""

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "c75223d3f1a6fba4e56a5e0c419a9ffe946805566d26757441af0b66f1d5c152"
PINS = {
    "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/statement.md":
        "b1fa6c8ce0dfe3eca422dec52348346dae7d342a77c71ad685bcb88ef23f4632",
    "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/proof.md":
        "523c35fc8eefa4d8ea9612b2bc6ecd48373af2e9d09e5791eacc441309f2308b",
    "background/nodes/rate_half_mca_full_lift_top_third_global_line_payment/statement.md":
        "8d103c4c092961387fa02ee18ff851a084c0f7774c0b4b238d1e7fba42dbe02d",
    "background/nodes/rate_half_mca_full_lift_top_third_global_line_payment/proof.md":
        "5abca3dd268f99b38c483fb12b22c9c7d91e0908b5a4ef389195b648651e3cb2",
    "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/statement.md":
        "767b9a387abf3606d5ccb990846789b45afa92e3489a4c10169443a55a139edf",
    "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/proof.md":
        "677c8378f7bf2f87dfc10a5340e3a0861a1124a3cc68e460e61bd42dc9c32c1d",
}


class Reject(ValueError):
    pass


def cap(R, d, K, e, h):
    n, m, c = R + K - e, d + K, K - 1
    a = m - h
    den = a * a - n * c
    if den > 0:
        return n * (a - c) // den
    gap = -den
    tangent = (n - a) ** 2 - (n - 1) * gap
    if 2 * a * a < n * c or tangent <= 0:
        raise Reject("undefined cap")
    return (n - 1) * n * n * (a - c) // (a * tangent)


def prefix(R, d, K, e, end):
    values = [0] + [cap(R, d, K, e, h) for h in range(1, end + 1)]
    for h in range(end - 1, 0, -1):
        values[h] = min(values[h], values[h + 1])
    return sum((values[h] - values[h - 1]) * (e // h)
               for h in range(1, end + 1))


def validate(payload):
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "theorem", "row"}:
        raise Reject("schema keys")
    if payload.get("schema") != "rate-half-mca-m31-residue-zero-direction-class-router-v1":
        raise Reject("schema")
    expected_sources = {
        "mean_centered_statement_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/statement.md"],
        "mean_centered_proof_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/proof.md"],
        "global_line_statement_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_top_third_global_line_payment/statement.md"],
        "global_line_proof_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_top_third_global_line_payment/proof.md"],
        "common_core_statement_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/statement.md"],
        "common_core_proof_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/proof.md"],
    }
    if payload["sources"] != expected_sources:
        raise Reject("sources")
    if payload["theorem"] != (
            "boundary<=1+J(Q-1); unsafe=>top>=343071=>core>=m-2"):
        raise Reject("theorem")
    r = payload["row"]
    R, d, K, e = r["R"], r["d"], r["K"], r["e"]
    N, m, c = R + K, d + K, K - 1
    s, q = divmod(e - K, 3)
    H = e - s - 1
    A = 2 * H - e
    den = A * A - e * c
    classes = e * (A - c) // den
    line = (N - e - c) // (m - H - c)
    boundary = 1 + classes * (line - 1)
    p = prefix(R, d, K, e, H - 1)
    threshold = r["budget"] - (p + boundary) + 1
    core = (threshold * m - N + threshold - 2) // (threshold - 1)
    got = {
        "s": s, "q": q, "H": H, "pair_agreement": A,
        "direction_classes": classes, "outside_line_cap": line,
        "boundary_cap": boundary, "P_H_minus_1": p,
        "prefix_plus_boundary": p + boundary,
        "top_threshold": threshold, "line_cap": N - m + 1,
        "forced_common_core": core, "m": m, "N": N,
    }
    for key, value in got.items():
        if r[key] != value:
            raise Reject(key)
    if den <= 0 or threshold > r["line_cap"] or core != m - 2:
        raise Reject("guards")
    return 19


def main():
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINS.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {relative}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    controls = []
    for key, delta in (("direction_classes", 1), ("boundary_cap", -1),
                       ("top_threshold", -1), ("forced_common_core", 1)):
        changed = copy.deepcopy(payload)
        changed["row"][key] += delta
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    assert all(controls)
    print("RATE_HALF_MCA_M31_RESIDUE_ZERO_DIRECTION_CLASS_ROUTER_PASS "
          f"checks={checks} mutations={sum(controls)}/{len(controls)}")


if __name__ == "__main__":
    main()
