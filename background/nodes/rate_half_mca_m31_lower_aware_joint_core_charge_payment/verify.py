#!/usr/bin/env python3
"""Verify the M31 lower-aware joint-core charge payment."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "c5406fb12ad6d251d9d3e8c969febffe2cc5c72dd8689cb82e685ba17eb81266"
PINS = {
    "background/nodes/rate_half_mca_m31_joint_core_charge_peeling_payment/statement.md":
        "5016cdb04352b5bcefa7cacdfd4fad9004a16a54357d6d2596a18f3af66a0be9",
    "background/nodes/rate_half_mca_m31_joint_core_charge_peeling_payment/proof.md":
        "3b40867beaf471b8fbd4c02f82d819355c745d67f80c439a427716b2bc87b03f",
    "background/nodes/rate_half_mca_m31_recursive_line_peeling_core_packing_payment/statement.md":
        "53db2ab106c93d6e21e2b7ac5673509a099d36262478144616946b5eb630784e",
    "background/nodes/rate_half_mca_m31_recursive_line_peeling_core_packing_payment/proof.md":
        "1b9f6621104164183d6b83815f9e4c9766c36e7b212c51faba36ce2ad95dce1b",
}

R, D, K = 1048576, 67448, 6
N, M, C = R + K, D + K, K - 1
BUDGET = 16777215


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


def runs(values: list[int]) -> list[list[int]]:
    answer: list[list[int]] = []
    for value in values:
        if answer and answer[-1][0] == value:
            answer[-1][1] += 1
        else:
            answer.append([value, 1])
    return answer


def lower_aware_charge(e: int, lower: list[int]) -> tuple[int, int, int, list[list[int]]]:
    count = len(lower)
    if count == 0:
        return 0, 0, 0, []
    core_budget = min(count * (M - 1),
                      e + count * (count + 1) * C // 2)
    lower_sum = sum(lower)
    if lower_sum > core_budget:
        raise Reject("infeasible lower bounds")
    allocation = sorted(lower, reverse=True)
    excess = core_budget - lower_sum
    for index in range(count):
        addition = min(excess, M - 1 - allocation[index])
        allocation[index] += addition
        excess -= addition
        if excess == 0:
            break
    if excess != 0:
        raise Reject("allocation")
    rational = sum((Fraction(N - value, M - value)
                    for value in allocation), Fraction())
    return (rational.numerator // rational.denominator, core_budget,
            lower_sum, runs(allocation))


def record(e: int) -> dict[str, object]:
    cutoff = choose_cutoff(e)
    weighted_prefix = prefix(e, cutoff)
    groups = 0
    for h in range(cutoff + 1, M + 1):
        overlap = 2 * h - e
        denominator = overlap * overlap - e * C
        if 2 * h <= e or overlap <= C or denominator <= 0:
            raise Reject("bank guard")
        groups += e * (overlap - C) // denominator
    base = weighted_prefix + M - cutoff - groups
    thresholds: list[int] = []
    cores: list[int] = []
    insides: list[int] = []

    for removed in range(512):
        charge, core_budget, lower_sum, allocation_runs = (
            lower_aware_charge(e, cores))
        target = BUDGET - charge
        required = target - base + 1
        positive = [value for value in insides if value > 0]
        packing = (sum(positive)
                   - len(positive) * (len(positive) - 1) * C // 2)
        common = {
            "e": e, "cutoff": cutoff, "prefix": weighted_prefix,
            "groups": groups, "base": base, "lines": removed,
            "target": target, "charge": charge,
            "core_budget": core_budget, "lower_sum": lower_sum,
            "allocation_runs": allocation_runs,
            "threshold_runs": runs(thresholds),
            "core_runs": runs(cores), "inside_runs": runs(insides),
            "packing": packing,
        }
        if required <= 0:
            common["certificate"] = "base_wall"
            return common
        threshold = (required + groups - 1) // groups
        if threshold < 2:
            raise Reject("threshold wall")
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
            common.update({
                "certificate": "core_packing", "lines": removed + 1,
                "threshold_runs": runs(thresholds),
                "core_runs": runs(cores), "inside_runs": runs(insides),
                "packing": packing,
            })
            return common
    raise Reject("recursion limit")


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "theorem", "records", "census"}:
        raise Reject("schema keys")
    if payload["schema"] != (
            "rate-half-mca-m31-lower-aware-joint-core-charge-v1"):
        raise Reject("schema")
    expected_sources = {
        "joint_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_joint_core_charge_peeling_payment/statement.md"],
        "joint_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_joint_core_charge_peeling_payment/proof.md"],
        "recursive_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_recursive_line_peeling_core_packing_payment/statement.md"],
        "recursive_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_recursive_line_peeling_core_packing_payment/proof.md"],
    }
    if payload["sources"] != expected_sources:
        raise Reject("sources")
    if payload["theorem"] != (
            "lower-bound-aware convex core charge for recursive affine-line peeling"):
        raise Reject("theorem")
    checks = 31
    for name in ("first", "last", "adjacent"):
        expected = payload["records"][name]
        if record(expected["e"]) != expected:
            raise Reject(name)
        checks += 17 + sum(len(expected[key]) for key in (
            "allocation_runs", "threshold_runs", "core_runs", "inside_runs"))
    census = payload["census"]
    if (census != {
            "first_e": 130220, "last_e": 130221,
            "adjacent_e": 130222, "paid": 2,
            "line_counts": {"38": 2}, "max_lines": 38,
            "residual_ceiling": 1044241} or
            payload["records"]["first"]["certificate"] != "core_packing" or
            payload["records"]["last"]["certificate"] != "core_packing" or
            payload["records"]["adjacent"]["certificate"] != "base_wall"):
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
            ("adjacent", "target", -1),
            ("adjacent", "lower_sum", 1)):
        mutant = copy.deepcopy(payload)
        mutant["records"][name][key] += delta
        try:
            validate(mutant)
        except Reject:
            mutations.append(True)
        else:
            mutations.append(False)
    if not all(mutations):
        raise Reject("mutation")
    print("m31-lower-aware-joint-core: PASS "
          f"({checks} checks; mutations={sum(mutations)}/{len(mutations)}; "
          "paid=130220..130221; wall=130222)")


if __name__ == "__main__":
    main()
