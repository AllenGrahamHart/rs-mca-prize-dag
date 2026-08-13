#!/usr/bin/env python3
"""Verify selected exact records for recursive M31 line peeling."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "19a99d27b3618484d69670b2fe5c33f27a5737b1c0331c2a4b84e3be02b4b3d8"
PINS = {
    "background/nodes/rate_half_mca_m31_boundary_line_bank_absorption_payment/statement.md":
        "9a1227549c72e71a6f25a5f55d0ada3bff384ad7ecbc7f9c13d9a5d12ed7b7fa",
    "background/nodes/rate_half_mca_m31_boundary_line_bank_absorption_payment/proof.md":
        "84614d982caf4d828f7aecd450cb5cbc50948be27ec878a3b58ff56970baed21",
    "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/statement.md":
        "b1fa6c8ce0dfe3eca422dec52348346dae7d342a77c71ad685bcb88ef23f4632",
    "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/proof.md":
        "523c35fc8eefa4d8ea9612b2bc6ecd48373af2e9d09e5791eacc441309f2308b",
    "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/statement.md":
        "1b8ca277bfd1ac820e5cd0b9ee23a0087bed561b9d1d7ac97ad04bdd2d47974e",
    "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/proof.md":
        "f3ef385b9f247ad58a7fa3f4138960413075a1b9a41ecb4c461d6e58d1412800",
}


class Reject(ValueError):
    pass


def raw_cap(R: int, d: int, K: int, e: int, h: int) -> int:
    n, m, c = R + K - e, d + K, K - 1
    agreement = m - h
    if agreement <= c:
        raise Reject("prefix agreement")
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
    m = d + K
    if not 1 <= cutoff <= m:
        raise Reject("prefix cutoff")
    values = [0] + [raw_cap(R, d, K, e, h)
                    for h in range(1, cutoff + 1)]
    for h in range(cutoff - 1, 0, -1):
        values[h] = min(values[h], values[h + 1])
    return sum((values[h] - values[h - 1]) * (e // h)
               for h in range(1, cutoff + 1))


def choose_cutoff(e: int, m: int, c: int) -> int:
    initial = 65304
    cutoff = initial
    while cutoff < m:
        h = cutoff + 1
        agreement = 2 * h - e
        if (2 * h > e and agreement > c and
                agreement * agreement > e * c):
            break
        cutoff += 1
    if cutoff > initial and cutoff < m:
        cutoff += 2
    if cutoff >= m:
        raise Reject("no boundary bank")
    return cutoff


def record(R: int, d: int, K: int, budget: int, e: int) -> dict[str, object]:
    N, m, c = R + K, d + K, K - 1
    line_cap = N - m + 1
    H = e - (e - K) // 3 - 1
    if H < m:
        raise Reject("top slot scope")
    cutoff = choose_cutoff(e, m, c)
    bank_prefix = prefix(R, d, K, e, cutoff)
    upper = m
    steps: list[dict[str, int]] = []
    inside_sum = 0

    while len(steps) < 32:
        target = budget - len(steps) * line_cap
        if target < 0:
            raise Reject("negative residual budget")
        try:
            whole_prefix = prefix(R, d, K, e, upper)
        except Reject:
            whole_prefix = None
        if whole_prefix is not None and whole_prefix <= target:
            bound = len(steps) * line_cap + whole_prefix
            return {
                "e": e, "cutoff": cutoff, "certificate": "profile",
                "lines": len(steps), "final_upper": upper,
                "final_piece": whole_prefix, "bound": bound,
                "slack": budget - bound, "inside_sum": inside_sum,
                "packing_lhs": inside_sum - len(steps) * (len(steps) - 1) * c // 2,
                "steps": steps,
            }
        if upper <= cutoff:
            return {
                "e": e, "cutoff": cutoff, "certificate": "method_wall_prefix",
                "lines": len(steps), "final_upper": upper,
                "inside_sum": inside_sum, "steps": steps,
            }

        groups = 0
        for h in range(cutoff + 1, upper + 1):
            agreement = 2 * h - e
            denominator = agreement * agreement - e * c
            if (2 * h <= e or agreement <= c or denominator <= 0):
                raise Reject("line-bank guard")
            classes = e * (agreement - c) // denominator
            if classes < 1:
                raise Reject("class count")
            groups += classes
        base = bank_prefix + (upper - cutoff) - groups
        direct = base + groups * line_cap
        if direct <= target:
            bound = len(steps) * line_cap + direct
            return {
                "e": e, "cutoff": cutoff, "certificate": "direct_bank",
                "lines": len(steps), "final_upper": upper,
                "final_piece": direct, "bound": bound,
                "slack": budget - bound, "inside_sum": inside_sum,
                "packing_lhs": inside_sum - len(steps) * (len(steps) - 1) * c // 2,
                "steps": steps,
            }

        required = target - base + 1
        if required <= 0:
            return {
                "e": e, "cutoff": cutoff, "certificate": "method_wall_base",
                "lines": len(steps), "final_upper": upper,
                "target": target, "groups": groups, "base": base,
                "inside_sum": inside_sum,
                "packing_lhs": inside_sum - len(steps) * (len(steps) - 1) * c // 2,
                "steps": steps,
            }
        if groups < 1:
            raise Reject("empty line bank")
        threshold = (required + groups - 1) // groups
        if not 2 <= threshold <= line_cap:
            raise Reject("line threshold")
        numerator = threshold * m - N
        core = 0 if numerator <= 0 else (
            numerator + threshold - 2) // (threshold - 1)
        inside = max(core - c, 0)
        sync = e - inside + K
        inside_sum += inside
        line_number = len(steps) + 1
        packing_lhs = inside_sum - line_number * (line_number - 1) * c // 2
        steps.append({
            "upper": upper, "target": target, "groups": groups,
            "base": base, "threshold": threshold, "core": core,
            "inside": inside, "sync": sync, "packing_lhs": packing_lhs,
        })
        if packing_lhs > e:
            return {
                "e": e, "cutoff": cutoff,
                "certificate": "core_packing_contradiction",
                "lines": len(steps), "final_upper": upper,
                "inside_sum": inside_sum, "packing_lhs": packing_lhs,
                "steps": steps,
            }
        upper = min(upper, sync - 1)
    raise Reject("recursion limit")


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "theorem", "row", "census"}:
        raise Reject("schema keys")
    if payload["schema"] != (
            "rate-half-mca-m31-recursive-line-peeling-core-packing-v1"):
        raise Reject("schema")
    expected_sources = {
        "line_bank_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_boundary_line_bank_absorption_payment/statement.md"],
        "line_bank_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_boundary_line_bank_absorption_payment/proof.md"],
        "prefix_statement_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/statement.md"],
        "prefix_proof_sha256": PINS[
            "background/nodes/rate_half_mca_full_lift_mean_centered_global_line_profile/proof.md"],
        "absorption_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/statement.md"],
        "absorption_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/proof.md"],
    }
    if payload["sources"] != expected_sources:
        raise Reject("sources")
    if payload["theorem"] != (
            "recursive affine-line peeling plus distinct-line inside-core packing"):
        raise Reject("theorem")
    row = payload["row"]
    checks = 61
    for name in ("first", "first_packing", "last", "adjacent"):
        got = record(row["R"], row["d"], row["K"], row["budget"],
                     row[name]["e"])
        if row[name] != got:
            raise Reject(name)
        checks += 10 + 9 * len(got["steps"])
    census = payload["census"]
    if (census["first_e"] != row["first"]["e"] or
            census["last_e"] != row["last"]["e"] or
            census["adjacent_e"] != row["adjacent"]["e"] or
            census["paid"] != census["last_e"] - census["first_e"] + 1 or
            census["profile"] + census["direct_bank"] + census["packing"] !=
            census["paid"] or
            census["line_counts"] != {"1": 3534, "2": 397, "3": 1397,
                                      "4": 59, "5": 6} or
            census["max_lines"] != 5 or
            row["first"]["certificate"] != "profile" or
            row["first_packing"]["certificate"] != "core_packing_contradiction" or
            row["last"]["certificate"] != "core_packing_contradiction" or
            row["adjacent"]["certificate"] != "method_wall_base"):
        raise Reject("census")
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
    for name, section, key, delta in (
            ("first", None, "bound", 1),
            ("first_packing", 1, "threshold", 1),
            ("last", 4, "inside", 1),
            ("adjacent", None, "base", -1)):
        changed = copy.deepcopy(payload)
        target = changed["row"][name]
        if section is not None:
            target = target["steps"][section]
        target[key] += delta
        try:
            validate(changed)
        except Reject:
            mutations.append(True)
        else:
            mutations.append(False)
    changed = copy.deepcopy(payload)
    changed["census"]["paid"] += 1
    try:
        validate(changed)
    except Reject:
        mutations.append(True)
    else:
        mutations.append(False)
    if not all(mutations):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_M31_RECURSIVE_LINE_PEELING_CORE_PACKING_PASS "
        f"checks={checks} mutations={sum(mutations)}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
