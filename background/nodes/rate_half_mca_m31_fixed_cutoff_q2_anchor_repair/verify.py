#!/usr/bin/env python3
"""Verify the M31 fixed-cutoff residue-two anchor repair."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "7f15aaaaa74be977c2b7de99aa559d3759f84910893d7e86100c485a4440e68d"
PINS = {
    "background/nodes/rate_half_mca_m31_fixed_cutoff_boundary_stack_payment/statement.md":
        "6b21c262941ed2dfb2dcb6e5ec8147906e4938b323baaa6891d423775df34d3c",
    "background/nodes/rate_half_mca_m31_fixed_cutoff_boundary_stack_payment/proof.md":
        "a4ab9148bd31f304d5139c3b29fb68feb538fe70f282370edc7e567e9dcc8999",
    "background/nodes/rate_half_mca_m31_two_boundary_layer_case_split/statement.md":
        "2d4c7e74136249fc69bee869452aa04163ec539c9cf8ece79928888d843ec6e1",
    "background/nodes/rate_half_mca_m31_two_boundary_layer_case_split/proof.md":
        "4a6d9d39ac6249811bac009de8b587a37cbb2b288c87cd46862e91cf7b56b832",
    "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/statement.md":
        "1b8ca277bfd1ac820e5cd0b9ee23a0087bed561b9d1d7ac97ad04bdd2d47974e",
    "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/proof.md":
        "f3ef385b9f247ad58a7fa3f4138960413075a1b9a41ecb4c461d6e58d1412800",
}


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


def layer_charge(R: int, d: int, K: int, e: int, h: int) -> int:
    N, m, c = R + K, d + K, K - 1
    A = 2 * h - e
    denominator = A * A - e * c
    outside = m - h
    n = N - e
    if 2 * h <= e or denominator <= 0 or not (n > outside > c):
        raise Reject("boundary guard")
    classes = e * (A - c) // denominator
    line = (n - c) // (outside - c)
    return 1 + classes * (line - 1)


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "theorem", "row"}:
        raise Reject("schema keys")
    if payload["schema"] != "rate-half-mca-m31-fixed-cutoff-q2-anchor-repair-v1":
        raise Reject("schema")
    expected_sources = {
        "stack_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_fixed_cutoff_boundary_stack_payment/statement.md"],
        "stack_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_fixed_cutoff_boundary_stack_payment/proof.md"],
        "q2_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_two_boundary_layer_case_split/statement.md"],
        "q2_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_two_boundary_layer_case_split/proof.md"],
        "absorption_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/statement.md"],
        "absorption_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/proof.md"],
    }
    if payload["sources"] != expected_sources:
        raise Reject("sources")
    if payload["theorem"] != "five-case residue-two repair at the fixed-cutoff wall":
        raise Reject("theorem")
    r = payload["row"]
    R, d, K, e = r["R"], r["d"], r["K"], r["e"]
    N, m, c = R + K, d + K, K - 1
    s, q = divmod(e - K, 3)
    H = e - s - 1
    p = prefix(R, d, K, e, r["cutoff"])
    layers = [layer_charge(R, d, K, e, h)
              for h in range(r["cutoff"] + 1, H + 1)]
    boundary = sum(layers)
    forcing = p + boundary
    d1, d2 = layers[-1], layers[-2]
    lower = forcing - d1 - d2
    threshold = r["budget"] - lower + 1
    core = (threshold * m - N + threshold - 2) // (threshold - 1)
    inside = core - c
    sync = e - inside + K
    agreement = m - sync + 1
    n = N - e
    denominator = agreement * agreement - n * c
    low = n * (agreement - c) // denominator
    two_top = e * low + (N - m + 1)
    outside = (n - c) // (m - H - c)
    disjoint = e // (s + 1)
    cases = {
        "two_top": two_top,
        "one_top_boundary_line": forcing - d1 + outside + 1,
        "one_top_small_boundary": forcing - d1 + 2,
        "no_top_boundary_line": forcing - d1 + outside,
        "no_top_disjoint_boundary": forcing - d1 + disjoint,
    }
    got = {
        "s": s, "q": q, "H": H, "prefix": p,
        "boundary_charge": boundary, "forcing_charge": forcing,
        "D1": d1, "D2": d2, "lower_charge": lower,
        "line_cap": N - m + 1, "unsafe_line_threshold": threshold,
        "forced_core": core, "inside_core": inside,
        "sync_start": sync, "low_agreement": agreement,
        "low_list_cap": low, "two_top_absorption": two_top,
        "outside_line_cap": outside, "disjoint_cap": disjoint,
        "cases": cases, "bound": max(cases.values()),
    }
    for key, value in got.items():
        if r[key] != value:
            raise Reject(key)
    if (q != 2 or e - 2 * s - (s + 2) != K or
            denominator <= 0 or r["bound"] >= r["budget"] or
            r["slack"] != r["budget"] - r["bound"] or
            r["adjacent_e"] != e + 1 or
            (r["adjacent_e"] - K) % 3 != r["adjacent_q"] or
            r["adjacent_q"] != 0 or
            r["residual_ceiling"] < r["adjacent_e"]):
        raise Reject("guards")
    return 37 + len(layers)


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINS.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {relative}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    controls = []
    for key, delta in (("prefix", 1), ("D1", 1),
                       ("two_top_absorption", -1), ("bound", -1),
                       ("slack", 1)):
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
        "RATE_HALF_MCA_M31_FIXED_CUTOFF_Q2_ANCHOR_REPAIR_PASS "
        f"checks={checks} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
