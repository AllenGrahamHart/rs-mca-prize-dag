#!/usr/bin/env python3
"""Verify the first Mersenne residue-zero core-absorption payment."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "c8c01775bd66dc3611867a3feb38280889a411788119b191bd7b5267516bdd8f"
PINS = {
    "background/nodes/rate_half_mca_m31_residue_zero_direction_class_router/statement.md":
        "ae7b4648a548b7e66e7d7b7a9d73f6ba428208faa20e569b9c732c0987e710b5",
    "background/nodes/rate_half_mca_m31_residue_zero_direction_class_router/proof.md":
        "11e5301a5cb5e6fefb7d21185e83260d644c56960edc2959033c3ff8cda45d49",
    "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/statement.md":
        "b1fa6c8ce0dfe3eca422dec52348346dae7d342a77c71ad685bcb88ef23f4632",
    "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/proof.md":
        "523c35fc8eefa4d8ea9612b2bc6ecd48373af2e9d09e5791eacc441309f2308b",
    "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/statement.md":
        "767b9a387abf3606d5ccb990846789b45afa92e3489a4c10169443a55a139edf",
    "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/proof.md":
        "677c8378f7bf2f87dfc10a5340e3a0861a1124a3cc68e460e61bd42dc9c32c1d",
}


class Reject(ValueError):
    pass


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "theorem", "row"}:
        raise Reject("schema keys")
    if payload["schema"] != (
            "rate-half-mca-m31-residue-zero-core-absorption-payment-v1"):
        raise Reject("schema")
    expected_sources = {
        "router_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_residue_zero_direction_class_router/statement.md"],
        "router_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_residue_zero_direction_class_router/proof.md"],
        "profile_statement_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/statement.md"],
        "profile_proof_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/proof.md"],
        "common_core_statement_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/statement.md"],
        "common_core_proof_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_top_third_common_core_payment/proof.md"],
    }
    if payload["sources"] != expected_sources:
        raise Reject("sources")
    if payload["theorem"] != (
            "unsafe=>large core=>high-layer absorption; low<=e*J"):
        raise Reject("theorem")

    r = payload["row"]
    R, d, K, e = r["R"], r["d"], r["K"], r["e"]
    N, m, c = R + K, d + K, K - 1
    inside = r["core_lower"] - c
    sync = e - inside + K
    low_end = sync - 1
    agreement = m - low_end
    n = N - e
    denominator = agreement * agreement - n * c
    numerator = n * (agreement - c)
    list_cap = numerator // denominator
    low_slopes = e * list_cap
    line = N - m + 1
    bound = low_slopes + line
    got = {
        "m": m, "N": N, "c": c, "inside_core_lower": inside,
        "sync_start": sync, "low_end": low_end,
        "low_agreement": agreement, "punctured_length": n,
        "johnson_denominator": denominator,
        "johnson_numerator": numerator, "low_list_cap": list_cap,
        "low_slope_cap": low_slopes, "line_cap": line,
        "contradiction_bound": bound, "slack": r["budget"] - bound,
    }
    for key, value in got.items():
        if r[key] != value:
            raise Reject(key)
    if (r["top_threshold"] < 2 or r["core_lower"] < m - 2 or
            denominator <= 0 or bound >= r["budget"] or
            r["adjacent_e"] != e + 1 or
            r["residual_ceiling"] < r["adjacent_e"]):
        raise Reject("guards")
    return 23


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINS.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {relative}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    controls = []
    for key, delta in (("inside_core_lower", 1), ("low_list_cap", -1),
                       ("contradiction_bound", -1), ("slack", 1)):
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
        "RATE_HALF_MCA_M31_RESIDUE_ZERO_CORE_ABSORPTION_PAYMENT_PASS "
        f"checks={checks} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
