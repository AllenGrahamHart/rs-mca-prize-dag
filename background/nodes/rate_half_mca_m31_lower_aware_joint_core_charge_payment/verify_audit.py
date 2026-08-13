#!/usr/bin/env python3
"""Independent ledger audit for the M31 lower-aware line charge."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


N, M, C, BUDGET = 1048582, 67454, 5, 16777215
DATA = Path(__file__).with_name("source_contract.json")


def expand(runs: list[list[int]]) -> list[int]:
    return [value for value, count in runs for _ in range(count)]


def charge(e: int, lower: list[int]) -> tuple[int, list[int], int]:
    count = len(lower)
    if count == 0:
        return 0, [], 0
    budget = min(count * (M - 1), e + count * (count + 1) * C // 2)
    values = sorted(lower, reverse=True)
    excess = budget - sum(values)
    assert excess >= 0
    for index, value in enumerate(values):
        addition = min(excess, M - 1 - value)
        values[index] += addition
        excess -= addition
        if excess == 0:
            break
    assert excess == 0
    total = sum((Fraction(N - value, M - value) for value in values),
                Fraction())
    return total.numerator // total.denominator, values, budget


def audit_record(record: dict[str, object]) -> int:
    e = record["e"]
    thresholds = expand(record["threshold_runs"])
    printed_cores = expand(record["core_runs"])
    printed_insides = expand(record["inside_runs"])
    assert len(thresholds) == len(printed_cores) == len(printed_insides)
    cores: list[int] = []
    insides: list[int] = []
    checks = 4
    for threshold, printed_core, printed_inside in zip(
            thresholds, printed_cores, printed_insides):
        value = threshold * M - N
        core = (0 if value <= 0 else
                (value + threshold - 2) // (threshold - 1))
        inside = max(core - C, 0)
        assert (core, inside) == (printed_core, printed_inside)

        old_charge, _, _ = charge(e, cores)
        target = BUDGET - old_charge
        forced = ((target - record["base"] + 1 + record["groups"] - 1)
                  // record["groups"])
        assert forced == threshold
        cores.append(core)
        insides.append(inside)
        checks += 3

    positive = [value for value in insides if value > 0]
    packing = (sum(positive)
               - len(positive) * (len(positive) - 1) * C // 2)
    assert packing == record["packing"]

    if record["certificate"] == "core_packing":
        assert packing > e
        charged_lower = cores[:-1]
    else:
        assert record["certificate"] == "base_wall" and packing <= e
        charged_lower = cores
    final_charge, allocation, budget = charge(e, charged_lower)
    assert final_charge == record["charge"]
    assert budget == record["core_budget"]
    assert sum(charged_lower) == record["lower_sum"]
    assert allocation == expand(record["allocation_runs"])
    assert BUDGET - final_charge == record["target"]
    if record["certificate"] == "base_wall":
        assert record["base"] >= record["target"] + 1
    return checks + 8


def main() -> None:
    payload = json.loads(DATA.read_text())
    records = payload["records"]
    checks = sum(audit_record(records[name])
                 for name in ("first", "last", "adjacent"))

    first_allocation = expand(records["first"]["allocation_runs"])
    last_allocation = expand(records["last"]["allocation_runs"])
    wall_allocation = expand(records["adjacent"]["allocation_runs"])
    first_q = sum((Fraction(N - x, M - x) for x in first_allocation),
                  Fraction())
    last_q = sum((Fraction(N - x, M - x) for x in last_allocation),
                 Fraction())
    wall_q = sum((Fraction(N - x, M - x) for x in wall_allocation),
                 Fraction())
    assert (first_q.numerator, first_q.denominator) == (
        894348212835561, 1468173681520)
    assert (last_q.numerator, last_q.denominator) == (
        1565078288323625, 2569251168624)
    assert (wall_q.numerator, wall_q.denominator) == (
        379266425096056, 77242971)
    print("m31-lower-aware-joint-core-audit: PASS "
          f"({checks + 6} checks; exact rational replay)")


if __name__ == "__main__":
    main()
