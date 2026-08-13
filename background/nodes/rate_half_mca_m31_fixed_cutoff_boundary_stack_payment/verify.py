#!/usr/bin/env python3
"""Verify pinned endpoints of the M31 fixed-cutoff boundary stack."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
SCAN = HERE / "scan_result.json"
CONTRACT_SHA256 = "10810877e32279126306f7676ed749b515c9e73656a0de098b47e181d9dcabd0"
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
SCAN_SHA256 = "aae7db91708e1ace36fc6d8202dcc43d92a08c4999e5d3912535fd7616c3cb83"


class Reject(ValueError):
    pass


def cap(R: int, d: int, K: int, e: int, h: int) -> int:
    n, m, c = R + K - e, d + K, K - 1
    agreement = m - h
    johnson = agreement * agreement - n * c
    if johnson > 0:
        return n * (agreement - c) // johnson
    gap = -johnson
    balance = 2 * agreement * agreement - n * c
    tangent = (n - agreement) ** 2 - (n - 1) * gap
    if balance < 0 or tangent <= 0:
        raise Reject("undefined prefix cap")
    return ((n - 1) * n * n * (agreement - c)
            // (agreement * tangent))


def prefix(R: int, d: int, K: int, e: int, cutoff: int) -> int:
    values = [0] + [cap(R, d, K, e, h) for h in range(1, cutoff + 1)]
    for h in range(cutoff - 1, 0, -1):
        values[h] = min(values[h], values[h + 1])
    return sum((values[h] - values[h - 1]) * (e // h)
               for h in range(1, cutoff + 1))


def endpoint(R: int, d: int, K: int, budget: int,
             cutoff: int, e: int) -> dict[str, int | str]:
    N, m, c = R + K, d + K, K - 1
    s, residue = divmod(e - K, 3)
    H = e - s - 1
    p = prefix(R, d, K, e, cutoff)
    stack = 0
    for h in range(cutoff + 1, H + 1):
        A = 2 * h - e
        denominator = A * A - e * c
        outside = m - h
        n = N - e
        if (2 * h <= e or denominator <= 0 or not (n > outside > c)):
            raise Reject("boundary guard")
        classes = e * (A - c) // denominator
        line = (n - c) // (outside - c)
        stack += 1 + classes * (line - 1)
    forcing = p + stack
    threshold = budget - forcing + 1
    got: dict[str, int | str] = {
        "e": e, "H": H, "residue": residue,
        "boundary_layers": H - cutoff, "prefix": p,
        "boundary_charge": stack, "forcing_charge": forcing,
        "top_threshold": threshold,
    }
    if forcing + (N - m + 1) <= budget:
        got["branch"] = "direct"
        return got
    if threshold < 2:
        got["branch"] = "fixed_cutoff_wall"
        return got
    core = (threshold * m - N + threshold - 2) // (threshold - 1)
    inside = core - c
    sync = e - inside + K
    agreement = m - sync + 1
    n = N - e
    denominator = agreement * agreement - n * c
    if denominator <= 0:
        raise Reject("low Johnson")
    low = n * (agreement - c) // denominator
    bound = e * low + (N - m + 1)
    got.update({
        "branch": "absorption", "core": core,
        "inside_core": inside, "sync_start": sync,
        "low_agreement": agreement, "low_list_cap": low,
        "final_bound": bound, "slack": budget - bound,
    })
    return got


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "theorem", "row"}:
        raise Reject("schema keys")
    if payload["schema"] != (
            "rate-half-mca-m31-fixed-cutoff-boundary-stack-payment-v1"):
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
        "scan_result_sha256": SCAN_SHA256,
    }
    if payload["sources"] != expected_sources:
        raise Reject("sources")
    if payload["theorem"] != (
            "fixed prefix plus exact direction-class boundary stack plus unsafe-core absorption"):
        raise Reject("theorem")
    r = payload["row"]
    checkpoints = {
        r["first_e"]: json.loads(SCAN.read_text())["first_paid"],
        r["last_direct_e"]: json.loads(SCAN.read_text())["last_direct"],
        r["first_absorption_e"]: json.loads(SCAN.read_text())["first_absorption"],
        r["last_paid_e"]: json.loads(SCAN.read_text())["last_paid"],
        r["adjacent_e"]: json.loads(SCAN.read_text())["adjacent"],
    }
    for e, expected in checkpoints.items():
        got = endpoint(r["R"], r["d"], r["K"], r["budget"], r["cutoff"], e)
        for key, value in expected.items():
            if key in {"slack"} and "slack" not in got:
                raise Reject(f"checkpoint {e} {key}")
            if got.get(key) != value:
                raise Reject(f"checkpoint {e} {key}")
    if (r["paid_count"] != r["last_paid_e"] - r["first_e"] + 1 or
            r["direct_count"] != r["last_direct_e"] - r["first_e"] + 1 or
            r["absorption_count"] != r["last_paid_e"] - r["first_absorption_e"] + 1 or
            r["endpoint_forcing_charge"] != checkpoints[r["last_paid_e"]]["forcing_charge"] or
            r["endpoint_top_threshold"] != checkpoints[r["last_paid_e"]]["top_threshold"] or
            r["endpoint_core"] != checkpoints[r["last_paid_e"]]["core"] or
            r["endpoint_low_list_cap"] != checkpoints[r["last_paid_e"]]["low_list_cap"] or
            r["endpoint_bound"] != checkpoints[r["last_paid_e"]]["final_bound"] or
            r["endpoint_slack"] != checkpoints[r["last_paid_e"]]["slack"] or
            r["adjacent_forcing_charge"] != checkpoints[r["adjacent_e"]]["forcing_charge"] or
            r["adjacent_excess"] != r["adjacent_forcing_charge"] - r["budget"] or
            r["residual_ceiling"] < r["adjacent_e"]):
        raise Reject("summary")
    return 41


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    if hashlib.sha256(SCAN.read_bytes()).hexdigest() != SCAN_SHA256:
        raise Reject("scan hash")
    for relative, digest in PINS.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {relative}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    controls = []
    for key, delta in (("paid_count", 1), ("endpoint_bound", -1),
                       ("adjacent_excess", -1), ("endpoint_slack", 1)):
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
        "RATE_HALF_MCA_M31_FIXED_CUTOFF_BOUNDARY_STACK_PAYMENT_PASS "
        f"checks={checks} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
