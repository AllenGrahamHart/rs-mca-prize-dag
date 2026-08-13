#!/usr/bin/env python3
"""Verify the M31 exact-layer slot-core packing payment."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "66cb4092487bbbdb9f9f2bf3f69b5aa672ce5c4e6b0f92e9652c315e1d7d0aef"
PINS = {
    "background/nodes/rate_half_mca_m31_core_dichotomy_capped_charge_payment/statement.md":
        "2b3f5b24ad800aac4dba4896181b832ea43c1376791b1310eec9fbdeacf2647e",
    "background/nodes/rate_half_mca_m31_core_dichotomy_capped_charge_payment/proof.md":
        "ebfb312ad8d7b97df1af97169560f42f4b24e990b6b3d81a2816cec2347dca5a",
    "background/nodes/rate_half_mca_m31_recursive_line_peeling_core_packing_payment/statement.md":
        "53db2ab106c93d6e21e2b7ac5673509a099d36262478144616946b5eb630784e",
    "background/nodes/rate_half_mca_m31_recursive_line_peeling_core_packing_payment/proof.md":
        "1b9f6621104164183d6b83815f9e4c9766c36e7b212c51faba36ce2ad95dce1b",
}

N, M, C = 1048582, 67454, 5
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


def bank(e: int, cutoff: int) -> tuple[int, int, int]:
    weighted_prefix = prefix(e, cutoff)
    groups = 0
    for h in range(cutoff + 1, M + 1):
        overlap = 2 * h - e
        denominator = overlap * overlap - e * C
        if 2 * h <= e or overlap <= C or denominator <= 0:
            raise Reject("bank guard")
        groups += e * (overlap - C) // denominator
    return weighted_prefix, groups, weighted_prefix + M - cutoff - groups


def capped_charge(e: int, lower: list[int], cap: int) -> tuple[int, int]:
    count = len(lower)
    if count == 0:
        return 0, 0
    budget = min(count * cap, e + count * (count + 1) * C // 2)
    values = sorted(lower, reverse=True)
    excess = budget - sum(values)
    if excess < 0:
        raise Reject("packing before charge")
    for index, value in enumerate(values):
        addition = min(excess, cap - value)
        values[index] += addition
        excess -= addition
        if excess == 0:
            break
    if excess:
        raise Reject("allocation")
    rational = sum((Fraction(N - value, M - value) for value in values),
                   Fraction())
    return rational.numerator // rational.denominator, budget


def paid_row(e: int, cutoff: int) -> dict[str, int]:
    weighted_prefix, groups, base = bank(e, cutoff)
    cap = e + 9 - ABSORPTION_CUTOFF
    absorption_bound = prefix(e, ABSORPTION_CUTOFF) + LINE
    lowers: list[int] = []
    threshold = inside_core = charge = target = core_budget = 0
    for _ in range(3):
        charge, core_budget = capped_charge(e, lowers, cap)
        target = BUDGET - charge
        threshold = (target - base + 1 + groups - 1) // groups
        if threshold < 2:
            raise Reject("paid threshold")
        numerator = threshold * (cutoff + 1) - e
        inside_core = max(0, (numerator + threshold - 2) // (threshold - 1))
        lowers.append(inside_core)
    packing = sum(lowers) - len(lowers) * (len(lowers) - 1) * C // 2
    if packing <= e:
        raise Reject("paid packing")
    return {
        "e": e, "cutoff": cutoff, "prefix": weighted_prefix,
        "groups": groups, "base": base, "core_cap": cap,
        "absorption_bound": absorption_bound, "threshold": threshold,
        "inside_core": inside_core, "charge": charge, "target": target,
        "core_budget": core_budget, "packing": packing,
    }


def uniform_charge(e: int, lines: int, lower: int, cap: int) -> tuple[int, int, int, int, int]:
    budget = min(lines * cap, e + lines * (lines + 1) * C // 2)
    lower_sum = lines * lower
    excess = budget - lower_sum
    if excess < 0:
        raise Reject("uniform packing")
    full, remainder = divmod(excess, cap - lower)
    full = min(full, lines)
    rational = full * Fraction(N - cap, M - cap)
    if full < lines:
        if remainder:
            rational += Fraction(N - (lower + remainder),
                                 M - (lower + remainder))
            residual = lines - full - 1
        else:
            residual = lines - full
        rational += residual * Fraction(N - lower, M - lower)
    return (rational.numerator // rational.denominator, budget,
            lower_sum, full, remainder)


def adjacent_row(e: int, cutoff: int) -> dict[str, int]:
    weighted_prefix, groups, base = bank(e, cutoff)
    cap = e + 9 - ABSORPTION_CUTOFF
    absorption_bound = prefix(e, ABSORPTION_CUTOFF) + LINE
    first_threshold = (BUDGET - base + 1 + groups - 1) // groups
    inside_core = ((first_threshold * (cutoff + 1) - e
                    + first_threshold - 2) // (first_threshold - 1))
    max_packing = max(
        lines * inside_core - lines * (lines - 1) * C // 2
        for lines in range(1, 1000))
    for lines in range(1, 10000):
        charge, budget, lower_sum, full, remainder = uniform_charge(
            e, lines, inside_core, cap)
        target = BUDGET - charge
        threshold = (target - base + 1 + groups - 1) // groups
        if threshold < 2:
            return {
                "e": e, "cutoff": cutoff, "prefix": weighted_prefix,
                "groups": groups, "base": base, "core_cap": cap,
                "absorption_bound": absorption_bound,
                "first_threshold": first_threshold,
                "inside_core": inside_core, "max_packing": max_packing,
                "wall_lines": lines, "core_budget": budget,
                "lower_sum": lower_sum, "full_caps": full,
                "remainder": remainder, "charge": charge,
                "target": target, "next_threshold": threshold,
            }
    raise Reject("adjacent limit")


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "theorem", "absorption_cutoff",
            "rows", "adjacent", "census"}:
        raise Reject("schema keys")
    if payload["schema"] != (
            "rate-half-mca-m31-exact-layer-slot-core-packing-v1"):
        raise Reject("schema")
    expected_sources = {
        "dichotomy_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_core_dichotomy_capped_charge_payment/statement.md"],
        "dichotomy_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_core_dichotomy_capped_charge_payment/proof.md"],
        "recursive_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_recursive_line_peeling_core_packing_payment/statement.md"],
        "recursive_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_recursive_line_peeling_core_packing_payment/proof.md"],
    }
    if payload["sources"] != expected_sources:
        raise Reject("sources")
    if payload["theorem"] != (
            "exact-layer line-slot incidence forces inside common core"):
        raise Reject("theorem")
    if payload["absorption_cutoff"] != ABSORPTION_CUTOFF:
        raise Reject("absorption cutoff")
    checks = 31
    rows = payload["rows"]
    if len(rows) != 11:
        raise Reject("row count")
    for row in rows:
        if paid_row(row["e"], row["cutoff"]) != row:
            raise Reject(f"row {row['e']}")
        checks += 17
    if adjacent_row(130237, 65521) != payload["adjacent"]:
        raise Reject("adjacent")
    checks += 19
    if payload["census"] != {
            "first_e": 130226, "last_e": 130236,
            "adjacent_e": 130237, "paid": 11,
            "lines_per_paid_row": 3, "residual_ceiling": 1044241}:
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
    for index, key, delta in (
            (0, "inside_core", -1),
            (10, "charge", 1)):
        mutant = copy.deepcopy(payload)
        mutant["rows"][index][key] += delta
        try:
            validate(mutant)
        except Reject:
            mutations.append(True)
        else:
            mutations.append(False)
    for key, delta in (("max_packing", 1), ("wall_lines", -1)):
        mutant = copy.deepcopy(payload)
        mutant["adjacent"][key] += delta
        try:
            validate(mutant)
        except Reject:
            mutations.append(True)
        else:
            mutations.append(False)
    if not all(mutations):
        raise Reject("mutations")
    print("m31-exact-layer-slot-core-packing: PASS "
          f"({checks} checks; mutations={sum(mutations)}/{len(mutations)}; "
          "paid=130226..130236; wall=130237)")


if __name__ == "__main__":
    main()
