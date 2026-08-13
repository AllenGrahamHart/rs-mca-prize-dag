#!/usr/bin/env python3
"""Verify pinned endpoints of the M31 boundary-line-bank payment."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "df160963ae6ba4908a35a41a56ce73563b9b24127867f7ec96b822e025ff3fac"
PINS = {
    "background/nodes/rate_half_mca_m31_fixed_cutoff_boundary_stack_payment/statement.md":
        "6b21c262941ed2dfb2dcb6e5ec8147906e4938b323baaa6891d423775df34d3c",
    "background/nodes/rate_half_mca_m31_fixed_cutoff_boundary_stack_payment/proof.md":
        "a4ab9148bd31f304d5139c3b29fb68feb538fe70f282370edc7e567e9dcc8999",
    "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/statement.md":
        "1b8ca277bfd1ac820e5cd0b9ee23a0087bed561b9d1d7ac97ad04bdd2d47974e",
    "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/proof.md":
        "f3ef385b9f247ad58a7fa3f4138960413075a1b9a41ecb4c461d6e58d1412800",
    "background/nodes/rate_half_mca_m31_fixed_cutoff_q2_anchor_repair/statement.md":
        "0bbcd5431c16a6c99ca3ca6d7b577f0187bb8e1ced7406afe24fde4114a48bfb",
    "background/nodes/rate_half_mca_m31_fixed_cutoff_q2_anchor_repair/proof.md":
        "614080531515fbf9f558318e2fd47c923b11af76415e010d54d47cdf5243fa3e",
}


class Reject(ValueError):
    pass


def raw_cap(R: int, d: int, K: int, e: int, h: int) -> int:
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
    values = [0] + [
        raw_cap(R, d, K, e, h) for h in range(1, cutoff + 1)]
    for h in range(cutoff - 1, 0, -1):
        values[h] = min(values[h], values[h + 1])
    return sum((values[h] - values[h - 1]) * (e // h)
               for h in range(1, cutoff + 1))


def endpoint(R: int, d: int, K: int, budget: int,
             cutoff: int, e: int) -> tuple[dict[str, int], int]:
    N, m, c = R + K, d + K, K - 1
    s, q = divmod(e - K, 3)
    H = e - s - 1
    upper = min(H, m)
    p = prefix(R, d, K, e, cutoff)
    class_sum = 0
    layers = 0
    for h in range(cutoff + 1, upper + 1):
        A = 2 * h - e
        denominator = A * A - e * c
        if 2 * h <= e or A <= c or denominator <= 0:
            raise Reject("line-bank guard")
        classes = e * (A - c) // denominator
        if classes < 1:
            raise Reject("class count")
        class_sum += classes
        layers += 1
    top = int(H < m)
    groups = top + class_sum
    base = p + layers - class_sum
    direct = base + groups * (N - m + 1)
    required = budget - base + 1
    if required <= 0 or groups < 1:
        raise Reject("pigeonhole")
    threshold = (required + groups - 1) // groups
    if threshold < 2:
        raise Reject("two anchors")
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
    return {
        "e": e, "q": q, "H": H, "prefix": p, "layers": layers,
        "groups": groups, "base": base, "direct": direct,
        "threshold": threshold, "core": core, "inside": inside,
        "sync": sync, "agreement": agreement, "low": low,
        "bound": bound, "slack": budget - bound,
    }, layers


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "theorem", "row"}:
        raise Reject("schema keys")
    if payload["schema"] != (
            "rate-half-mca-m31-boundary-line-bank-absorption-v1"):
        raise Reject("schema")
    expected_sources = {
        "stack_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_fixed_cutoff_boundary_stack_payment/statement.md"],
        "stack_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_fixed_cutoff_boundary_stack_payment/proof.md"],
        "absorption_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/statement.md"],
        "absorption_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/proof.md"],
        "q2_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_fixed_cutoff_q2_anchor_repair/statement.md"],
        "q2_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_fixed_cutoff_q2_anchor_repair/proof.md"],
    }
    if payload["sources"] != expected_sources:
        raise Reject("sources")
    if payload["theorem"] != (
            "boundary direction-class affine-line bank plus unsafe-core absorption"):
        raise Reject("theorem")
    row = payload["row"]
    checks = 47
    for name in ("first", "last", "adjacent"):
        got, layers = endpoint(
            row["R"], row["d"], row["K"], row["budget"],
            row["cutoff"], row[name]["e"])
        if row[name] != got:
            raise Reject(name)
        checks += layers
    if (row["paid_count"] != row["last"]["e"] - row["first"]["e"] + 1 or
            row["adjacent"]["e"] != row["last"]["e"] + 1 or
            row["first"]["bound"] > row["budget"] or
            row["last"]["bound"] > row["budget"] or
            row["adjacent"]["bound"] <= row["budget"] or
            row["residual_ceiling"] < row["adjacent"]["e"]):
        raise Reject("summary")
    return checks


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINS.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {relative}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    mutations = []
    for section, key, delta in (
            ("last", "prefix", 1), ("last", "groups", 1),
            ("last", "bound", -1), ("adjacent", "bound", -1),
            (None, "paid_count", 1)):
        changed = copy.deepcopy(payload)
        target = changed["row"] if section is None else changed["row"][section]
        target[key] += delta
        try:
            validate(changed)
        except Reject:
            mutations.append(True)
        else:
            mutations.append(False)
    if not all(mutations):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_M31_BOUNDARY_LINE_BANK_ABSORPTION_PASS "
        f"checks={checks} mutations={sum(mutations)}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
