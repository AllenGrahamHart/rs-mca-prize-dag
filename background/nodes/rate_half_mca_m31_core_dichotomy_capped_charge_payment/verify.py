#!/usr/bin/env python3
"""Verify the M31 core-dichotomy capped-charge payment."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "d73e5d313c3fdd19a532effc923d5199e7540731d80a15d1c8da6d39217efc3f"
PINS = {
    "background/nodes/rate_half_mca_m31_lower_aware_joint_core_charge_payment/statement.md":
        "7d2635c9b16ad58c20047d42ebb2ae765358649afd63ffd7641b4bb0e1874a4a",
    "background/nodes/rate_half_mca_m31_lower_aware_joint_core_charge_payment/proof.md":
        "57598ac57b7d7dfee9d4bc808435a364ed2675bf4888ed6cd47a606246a445c1",
    "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/statement.md":
        "1b8ca277bfd1ac820e5cd0b9ee23a0087bed561b9d1d7ac97ad04bdd2d47974e",
    "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/proof.md":
        "f3ef385b9f247ad58a7fa3f4138960413075a1b9a41ecb4c461d6e58d1412800",
}

R, D, K = 1048576, 67448, 6
N, M, C = R + K, D + K, K - 1
BUDGET, LINE, ABSORPTION_CUTOFF = 16777215, N - M + 1, 65450


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


def bank(e: int) -> tuple[int, int, int, int]:
    cutoff = choose_cutoff(e)
    weighted_prefix = prefix(e, cutoff)
    groups = 0
    for h in range(cutoff + 1, M + 1):
        overlap = 2 * h - e
        denominator = overlap * overlap - e * C
        if 2 * h <= e or overlap <= C or denominator <= 0:
            raise Reject("bank guard")
        groups += e * (overlap - C) // denominator
    return cutoff, weighted_prefix, groups, weighted_prefix + M - cutoff - groups


def runs(values: list[int]) -> list[list[int]]:
    answer: list[list[int]] = []
    for value in values:
        if answer and answer[-1][0] == value:
            answer[-1][1] += 1
        else:
            answer.append([value, 1])
    return answer


def capped_charge(e: int, lower: list[int], cap: int) -> tuple[int, int, list[list[int]]]:
    count = len(lower)
    if count == 0:
        return 0, 0, []
    core_budget = min(count * cap, e + count * (count + 1) * C // 2)
    allocation = sorted(lower, reverse=True)
    excess = core_budget - sum(allocation)
    if excess < 0:
        raise Reject("infeasible lower bounds")
    for index in range(count):
        addition = min(excess, cap - allocation[index])
        allocation[index] += addition
        excess -= addition
        if excess == 0:
            break
    if excess:
        raise Reject("allocation")
    rational = sum((Fraction(N - value, M - value)
                    for value in allocation), Fraction())
    return rational.numerator // rational.denominator, core_budget, runs(allocation)


def zero_lower_charge(e: int, lines: int, cap: int) -> tuple[int, int, int, int]:
    if lines == 0:
        return 0, 0, 0, 0
    core_budget = min(lines * cap, e + lines * (lines + 1) * C // 2)
    full, remainder = divmod(core_budget, cap)
    if full == lines:
        rational = lines * Fraction(N - cap, M - cap)
    else:
        rational = full * Fraction(N - cap, M - cap)
        rational += Fraction(N - remainder, M - remainder)
        rational += (lines - full - 1) * Fraction(N, M)
    return rational.numerator // rational.denominator, core_budget, full, remainder


def paid_record(e: int) -> dict[str, object]:
    core_cap = e + 9 - ABSORPTION_CUTOFF
    absorption_prefix = prefix(e, ABSORPTION_CUTOFF)
    cutoff, weighted_prefix, groups, base = bank(e)
    thresholds: list[int] = []
    cores: list[int] = []
    insides: list[int] = []
    for removed in range(256):
        charge, core_budget, allocation_runs = capped_charge(e, cores, core_cap)
        target = BUDGET - charge
        required = target - base + 1
        if required <= 0:
            raise Reject("premature base wall")
        threshold = (required + groups - 1) // groups
        if threshold < 2:
            raise Reject("premature threshold wall")
        numerator = threshold * M - N
        core = (0 if numerator <= 0 else
                (numerator + threshold - 2) // (threshold - 1))
        inside = max(core - C, 0)
        thresholds.append(threshold)
        cores.append(core)
        insides.append(inside)
        positive = [value for value in insides if value > 0]
        packing = (sum(positive)
                   - len(positive) * (len(positive) - 1) * C // 2)
        if packing > e:
            return {
                "e": e, "core_cap": core_cap,
                "absorption_prefix": absorption_prefix,
                "absorption_bound": absorption_prefix + LINE,
                "cutoff": cutoff, "prefix": weighted_prefix,
                "groups": groups, "base": base,
                "certificate": "core_packing", "lines": removed + 1,
                "target": target, "charge": charge,
                "core_budget": core_budget,
                "allocation_runs": allocation_runs,
                "threshold_runs": runs(thresholds),
                "core_runs": runs(cores), "inside_runs": runs(insides),
                "packing": packing,
            }
    raise Reject("recursion limit")


def adjacent_record(e: int) -> dict[str, object]:
    core_cap = e + 9 - ABSORPTION_CUTOFF
    absorption_prefix = prefix(e, ABSORPTION_CUTOFF)
    cutoff, weighted_prefix, groups, base = bank(e)
    first_required = BUDGET - base + 1
    first_threshold = (first_required + groups - 1) // groups
    first_numerator = first_threshold * M - N
    if first_numerator > 0:
        raise Reject("positive adjacent core")
    for lines in range(20000):
        charge, core_budget, full, remainder = zero_lower_charge(
            e, lines, core_cap)
        target = BUDGET - charge
        threshold = (target - base + 1 + groups - 1) // groups
        if threshold < 2:
            return {
                "e": e, "core_cap": core_cap,
                "absorption_prefix": absorption_prefix,
                "absorption_bound": absorption_prefix + LINE,
                "cutoff": cutoff, "prefix": weighted_prefix,
                "groups": groups, "base": base,
                "certificate": "threshold_one_wall", "lines": lines,
                "target": target, "charge": charge,
                "core_budget": core_budget, "full_caps": full,
                "remainder": remainder,
                "first_threshold": first_threshold,
                "next_threshold": threshold, "packing": 0,
            }
        if threshold > first_threshold:
            raise Reject("threshold monotonicity")
    raise Reject("adjacent recursion limit")


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "theorem", "absorption_cutoff",
            "records", "census"}:
        raise Reject("schema keys")
    if payload["schema"] != "rate-half-mca-m31-core-dichotomy-capped-charge-v1":
        raise Reject("schema")
    expected_sources = {
        "lower_aware_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_lower_aware_joint_core_charge_payment/statement.md"],
        "lower_aware_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_lower_aware_joint_core_charge_payment/proof.md"],
        "absorption_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/statement.md"],
        "absorption_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_residue_zero_core_absorption_payment/proof.md"],
    }
    if payload["sources"] != expected_sources:
        raise Reject("sources")
    if payload["theorem"] != (
            "high-core absorption or capped lower-aware convex peeling"):
        raise Reject("theorem")
    if payload["absorption_cutoff"] != ABSORPTION_CUTOFF:
        raise Reject("absorption cutoff")
    checks = 37
    for e in range(130222, 130226):
        name = f"e{e}"
        if paid_record(e) != payload["records"][name]:
            raise Reject(name)
        checks += 21
    if adjacent_record(130226) != payload["records"]["adjacent"]:
        raise Reject("adjacent")
    checks += 21
    if payload["census"] != {
            "first_e": 130222, "last_e": 130225,
            "adjacent_e": 130226, "paid": 4,
            "line_counts": {"14": 2, "70": 2},
            "max_lines": 70, "residual_ceiling": 1044241}:
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
            ("e130222", "packing", -1),
            ("e130225", "charge", 1),
            ("adjacent", "target", -1),
            ("adjacent", "full_caps", 1)):
        mutant = copy.deepcopy(payload)
        mutant["records"][name][key] += delta
        try:
            validate(mutant)
        except Reject:
            mutations.append(True)
        else:
            mutations.append(False)
    if not all(mutations):
        raise Reject("mutation controls")
    print("m31-core-dichotomy-capped-charge: PASS "
          f"({checks} checks; mutations={sum(mutations)}/{len(mutations)}; "
          "paid=130222..130225; wall=130226)")


if __name__ == "__main__":
    main()
