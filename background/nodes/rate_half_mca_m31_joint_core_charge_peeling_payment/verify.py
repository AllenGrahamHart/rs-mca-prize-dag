#!/usr/bin/env python3
"""Verify endpoints of the M31 joint-core charge peeling payment."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "2d5005cc27a3ee7dfa858d7bd3f57209d416d61e31f4dece0b13603d9bcae015"
PINS = {
    "background/nodes/rate_half_mca_m31_recursive_line_peeling_core_packing_payment/statement.md":
        "53db2ab106c93d6e21e2b7ac5673509a099d36262478144616946b5eb630784e",
    "background/nodes/rate_half_mca_m31_recursive_line_peeling_core_packing_payment/proof.md":
        "1b9f6621104164183d6b83815f9e4c9766c36e7b212c51faba36ce2ad95dce1b",
    "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/statement.md":
        "1b8ca277bfd1ac820e5cd0b9ee23a0087bed561b9d1d7ac97ad04bdd2d47974e",
    "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/proof.md":
        "f3ef385b9f247ad58a7fa3f4138960413075a1b9a41ecb4c461d6e58d1412800",
}

R, D, K = 1048576, 67448, 6
N, M, C = R + K, D + K, K - 1
BUDGET, LINE = 16777215, N - M + 1


class Reject(ValueError):
    pass


def raw_cap(e: int, h: int) -> int:
    shortened, agreement = N - e, M - h
    if agreement <= C:
        raise Reject("prefix agreement")
    johnson = agreement * agreement - shortened * C
    if johnson > 0:
        return shortened * (agreement - C) // johnson
    gap = -johnson
    balance = 2 * agreement * agreement - shortened * C
    tangent = (shortened - agreement) ** 2 - (shortened - 1) * gap
    if balance < 0 or tangent <= 0:
        raise Reject("prefix cap")
    return ((shortened - 1) * shortened * shortened * (agreement - C)
            // (agreement * tangent))


def prefix(e: int, cutoff: int) -> int:
    if not 1 <= cutoff <= M:
        raise Reject("cutoff")
    values = [0] + [raw_cap(e, h) for h in range(1, cutoff + 1)]
    for h in range(cutoff - 1, 0, -1):
        values[h] = min(values[h], values[h + 1])
    return sum((values[h] - values[h - 1]) * (e // h)
               for h in range(1, cutoff + 1))


def choose_cutoff(e: int) -> int:
    initial = 65304
    cutoff = initial
    while cutoff < M:
        h = cutoff + 1
        overlap = 2 * h - e
        if (2 * h > e and overlap > C and
                overlap * overlap > e * C):
            break
        cutoff += 1
    if cutoff > initial and cutoff < M:
        cutoff += 2
    if cutoff >= M:
        raise Reject("no bank")
    return cutoff


def joint_charge(e: int, lines: int) -> tuple[int, int, int, int]:
    if lines == 0:
        return 0, 0, 0, 0
    core_budget = min(
        lines * (M - 1), e + lines * (lines + 1) * C // 2)
    full, remainder = divmod(core_budget, M - 1)
    full = min(full, lines)
    if full == lines:
        charge = lines * LINE
    else:
        left = lines - full
        rational = Fraction(full * LINE, 1)
        rational += Fraction(N - remainder, M - remainder)
        rational += (left - 1) * Fraction(N, M)
        charge = rational.numerator // rational.denominator
    return charge, core_budget, full, remainder


def runs(values: list[int]) -> list[list[int]]:
    answer: list[list[int]] = []
    for value in values:
        if answer and answer[-1][0] == value:
            answer[-1][1] += 1
        else:
            answer.append([value, 1])
    return answer


def record(e: int) -> dict[str, object]:
    cutoff = choose_cutoff(e)
    p = prefix(e, cutoff)
    groups = 0
    for h in range(cutoff + 1, M + 1):
        overlap = 2 * h - e
        denominator = overlap * overlap - e * C
        if 2 * h <= e or overlap <= C or denominator <= 0:
            raise Reject("bank guard")
        groups += e * (overlap - C) // denominator
    base = p + M - cutoff - groups
    thresholds: list[int] = []
    insides: list[int] = []

    for removed in range(256):
        charge, core_budget, full, remainder = joint_charge(e, removed)
        target = BUDGET - charge
        required = target - base + 1
        if required <= 0:
            return {
                "e": e, "cutoff": cutoff, "prefix": p,
                "groups": groups, "base": base,
                "certificate": "base_wall", "lines": removed,
                "target": target, "charge": charge,
                "core_budget": core_budget, "full": full,
                "remainder": remainder,
                "threshold_runs": runs(thresholds),
                "inside_runs": runs(insides),
            }
        threshold = (required + groups - 1) // groups
        if threshold < 2:
            raise Reject("threshold")
        numerator = threshold * M - N
        core = 0 if numerator <= 0 else (
            numerator + threshold - 2) // (threshold - 1)
        inside = max(core - C, 0)
        thresholds.append(threshold)
        insides.append(inside)
        positive = [value for value in insides if value > 0]
        packing = (sum(positive)
                   - len(positive) * (len(positive) - 1) * C // 2)
        if packing > e:
            return {
                "e": e, "cutoff": cutoff, "prefix": p,
                "groups": groups, "base": base,
                "certificate": "core_packing", "lines": removed + 1,
                "target": target, "charge": charge,
                "core_budget": core_budget, "full": full,
                "remainder": remainder, "packing": packing,
                "threshold_runs": runs(thresholds),
                "inside_runs": runs(insides),
            }
        if inside == 0:
            return {
                "e": e, "cutoff": cutoff, "prefix": p,
                "groups": groups, "base": base,
                "certificate": "zero_core_wall", "lines": removed + 1,
                "target": target, "charge": charge,
                "core_budget": core_budget, "full": full,
                "remainder": remainder, "packing": packing,
                "threshold_runs": runs(thresholds),
                "inside_runs": runs(insides),
            }
    raise Reject("recursion")


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "theorem", "records", "census"}:
        raise Reject("schema keys")
    if payload["schema"] != (
            "rate-half-mca-m31-joint-core-charge-peeling-v1"):
        raise Reject("schema")
    expected_sources = {
        "recursive_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_recursive_line_peeling_core_packing_payment/statement.md"],
        "recursive_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_recursive_line_peeling_core_packing_payment/proof.md"],
        "absorption_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/statement.md"],
        "absorption_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/proof.md"],
    }
    if payload["sources"] != expected_sources:
        raise Reject("sources")
    if payload["theorem"] != (
            "joint convex core charge for recursive affine-line peeling"):
        raise Reject("theorem")
    checks = 37
    for name in ("first", "last", "adjacent"):
        got = record(payload["records"][name]["e"])
        if got != payload["records"][name]:
            raise Reject(name)
        checks += 14 + len(got["threshold_runs"]) + len(got["inside_runs"])
    census = payload["census"]
    if (census["paid"] != census["last_e"] - census["first_e"] + 1 or
            census["adjacent_e"] != census["last_e"] + 1 or
            sum(census["line_counts"].values()) != census["paid"] or
            census["line_counts"] != {
                "4": 2, "5": 10, "6": 3, "7": 2,
                "8": 1, "10": 1, "13": 2} or
            census["max_lines"] != 13 or
            payload["records"]["first"]["certificate"] != "core_packing" or
            payload["records"]["last"]["certificate"] != "core_packing" or
            payload["records"]["adjacent"]["certificate"] != "zero_core_wall"):
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
    for name, key, delta in (
            ("first", "packing", -1),
            ("last", "charge", 1),
            ("adjacent", "packing", 1),
            ("adjacent", "target", -1)):
        changed = copy.deepcopy(payload)
        changed["records"][name][key] += delta
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
        "RATE_HALF_MCA_M31_JOINT_CORE_CHARGE_PEELING_PASS "
        f"checks={checks} mutations={sum(mutations)}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
