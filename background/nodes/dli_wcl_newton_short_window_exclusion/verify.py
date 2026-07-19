#!/usr/bin/env python3
"""Verify the Newton short-window algebra, cutoff, and DAG interface."""

from __future__ import annotations

import copy
import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DAG = ROOT / "dag.json"
PIN = ROOT / "critical/nodes/dli_prime_weighted_large_block_support/DLI_CLOSE_PINNED.md"
NODE = "dli_wcl_newton_short_window_exclusion"
ZONE = "dli_wcl_zone_coverage"
TEST_PRIMES = (5, 7, 11, 13, 17, 19)
ACTUAL_LEVELS = tuple(2**power for power in range(33))  # w7-C6: tuple, not a one-shot generator
EXPECTED_RESIDUAL = ((1, 5), (1, 6), (2, 5), (2, 6), (2, 7), (4, 9))


class Reject(ValueError):
    pass


def trial_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, math.isqrt(value) + 1))


def elementary(roots: tuple[int, ...], prime: int) -> list[int]:
    return [1] + [
        sum(math.prod(part) for part in itertools.combinations(roots, size)) % prime
        for size in range(1, len(roots) + 1)
    ]


def compile_short(payload: object) -> dict[str, object]:
    if not isinstance(payload, dict) or set(payload) != {"level", "prime", "roots"}:
        raise Reject("payload schema")
    level = payload["level"]
    prime = payload["prime"]
    roots = payload["roots"]
    if not isinstance(level, int) or isinstance(level, bool) or level <= 0:
        raise Reject("level")
    if not isinstance(prime, int) or isinstance(prime, bool) or not trial_prime(prime):
        raise Reject("field")
    if (
        not isinstance(roots, list)
        or not roots
        or any(not isinstance(root, int) or isinstance(root, bool) for root in roots)
    ):
        raise Reject("roots")
    reduced = tuple(root % prime for root in roots)
    weight = len(reduced)
    if prime <= weight:
        raise Reject("characteristic")
    if weight > 2 * level:
        raise Reject("weight cutoff")
    if 0 in reduced or len(set(reduced)) != weight:
        raise Reject("distinct nonzero roots")

    powers = [0] + [sum(root**index for root in reduced) % prime for index in range(1, weight + 1)]
    for index in range(1, 2 * level, 2):
        if sum(pow(root, index, prime) for root in reduced) % prime:
            raise Reject("odd-power hypotheses")
    coefficients = elementary(reduced, prime)
    for index in range(1, weight + 1):
        right = sum(
            (-1) ** (part - 1) * coefficients[index - part] * powers[part]
            for part in range(1, index + 1)
        )
        if (index * coefficients[index] - right) % prime:
            raise Reject("Newton identity")
    if any(coefficients[index] for index in range(1, weight + 1, 2)):
        raise Reject("odd elementary coefficient")
    if weight % 2:
        raise Reject("odd nonzero product contradiction")

    antipodal = all((-root) % prime in reduced for root in reduced)
    if not antipodal:
        raise Reject("even polynomial did not pair roots")
    return {"antipodal": antipodal, "weight": weight}


def residual_slots() -> tuple[tuple[int, int], ...]:
    residual = []
    for level in ACTUAL_LEVELS:
        for weight in range(level + 1, level + 6):
            newton_excludes = weight <= 2 * level
            earlier_excludes = level == 1 and weight in (3, 4)
            if not (newton_excludes or earlier_excludes):
                residual.append((level, weight))
    return tuple(residual)


def main() -> None:
    dag = json.loads(DAG.read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    pin = PIN.read_text()
    structural = {
        "node_proved": nodes[NODE]["status"] == "PROVED",
        "proof_closure": nodes[NODE]["closure"] == "proof",
        "zone_target": nodes[ZONE]["status"] in ("TARGET", "CONDITIONAL")  # 2026-07-19 amber re-pose,
        "evidence_edge": (NODE, ZONE, "ev") in edges,
        "odd_power_matrix": "A_{l,y} = x_y^{2l-1}" in pin,
        "residual_slots": residual_slots() == EXPECTED_RESIDUAL,
    }
    if not all(structural.values()):
        raise AssertionError(structural)

    checked = 0
    paired_hits = 0
    for prime in TEST_PRIMES:
        for level in range(1, 5):
            for weight in range(2, min(2 * level, prime - 1) + 1):
                for roots in itertools.combinations(range(1, prime), weight):
                    checked += 1
                    if any(
                        sum(pow(root, index, prime) for root in roots) % prime
                        for index in range(1, 2 * level, 2)
                    ):
                        continue
                    result = compile_short(
                        {"level": level, "prime": prime, "roots": list(roots)}
                    )
                    if not result["antipodal"]:
                        raise AssertionError("non-antipodal short relation")
                    paired_hits += 1
    if paired_hits == 0:
        raise AssertionError("vacuous finite replay")

    boundary = (
        {"level": 1, "prime": 7, "roots": [1, 2, 4]},
        {"level": 2, "prime": 11, "roots": [1, 3, 4, 5, 9]},
        {"level": 4, "prime": 19, "roots": [pow(4, exponent, 19) for exponent in range(9)]},
    )
    for row in boundary:
        roots = tuple(row["roots"])
        if len(set(roots)) != 2 * row["level"] + 1:
            raise AssertionError("boundary subgroup size")
        if any(
            sum(pow(root, index, row["prime"]) for root in roots) % row["prime"]
            for index in range(1, 2 * row["level"], 2)
        ):
            raise AssertionError("boundary moments")
        if any((-root) % row["prime"] in roots for root in roots):
            raise AssertionError("boundary antipode")
        try:
            compile_short(row)
        except Reject as error:
            if str(error) != "weight cutoff":
                raise
        else:
            raise AssertionError("cutoff mutation accepted")

    valid = {"level": 2, "prime": 13, "roots": [1, 12, 2, 11]}
    if not compile_short(valid)["antipodal"]:
        raise AssertionError("positive control")
    controls = 0
    mutations = (
        lambda item: item.__setitem__("level", 0),
        lambda item: item.__setitem__("prime", 4),
        lambda item: item["roots"].__setitem__(1, item["roots"][0]),
        lambda item: item["roots"].__setitem__(0, 0),
        lambda item: item["roots"].pop(),
        lambda item: item.__setitem__("extra", True),
    )
    for mutate in mutations:
        altered = copy.deepcopy(valid)
        mutate(altered)
        try:
            compile_short(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls += 1
    if controls != len(mutations):
        raise AssertionError(f"negative controls caught {controls}/{len(mutations)}")

    print(
        "DLI_WCL_NEWTON_SHORT_WINDOW_PASS "
        f"finite_sets={checked} paired_hits={paired_hits} "
        f"residual_slots={len(EXPECTED_RESIDUAL)} boundary_controls={len(boundary)} "
        f"negative_controls={controls}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
