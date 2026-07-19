#!/usr/bin/env python3
"""Verify the multideletion multifiber independence thresholds."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_multideletion_multifiber_exclusion"
DEPENDENCY = "rate_half_list_budget_three_multifiber_vandermonde_exclusion"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 1_000_003
PROFILES = {
    "cycle": ((1, 1, 1, 1), 4),
    "path": ((1, 1, 1), 3),
    "linear-k4e": ((2, 2, 1, 1), 6),
    "k4": ((2, 2, 2, 2), 7),
    "triangle-singleton": ((1, 1, 1, 2), 5),
}


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    return answer


def divide_exact(dividend: list[int], divisor: list[int]) -> list[int]:
    work = dividend[:]
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    inverse = pow(divisor[-1], PRIME - 2, PRIME)
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient = work[shift + len(divisor) - 1] * inverse % PRIME
        quotient[shift] = coefficient
        for j, value in enumerate(divisor):
            work[shift + j] = (work[shift + j] - coefficient * value) % PRIME
    assert not any(work)
    return quotient


def full_block(values: set[int], m: int) -> list[int]:
    answer = [1]
    for value in values:
        factor = [-value % PRIME] + [0] * (m - 1) + [1]
        answer = multiply(answer, factor)
    return answer


def root_locator(roots: list[int]) -> list[int]:
    answer = [1]
    for root in roots:
        answer = multiply(answer, [-root % PRIME, 1])
    return answer


def rank(columns: list[list[int]]) -> int:
    height = max(len(column) for column in columns)
    rows = [
        [column[i] if i < len(column) else 0 for column in columns]
        for i in range(height)
    ]
    answer = 0
    for column in range(len(columns)):
        pivot = next((i for i in range(answer, height) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[answer], rows[pivot] = rows[pivot], rows[answer]
        inverse = pow(rows[answer][column], PRIME - 2, PRIME)
        rows[answer] = [entry * inverse % PRIME for entry in rows[answer]]
        for row in range(height):
            if row != answer and rows[row][column]:
                factor = rows[row][column]
                rows[row] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(rows[row], rows[answer], strict=True)
                ]
        answer += 1
    return answer


def profile_check() -> int:
    checked = 0
    for profile, (deletions, threshold) in PROFILES.items():
        assert threshold == sum(deletions) - min(deletions) + 1
        for m in range(threshold, threshold + 4):
            root_sets = []
            cursor = 2
            for size in deletions:
                roots = list(range(cursor, cursor + size))
                cursor += size
                root_sets.append(roots)
            all_values = {pow(root, m, PRIME) for roots in root_sets for root in roots}
            s = len(all_values) + 1
            locators = []
            for index, roots in enumerate(root_sets):
                values = {pow(root, m, PRIME) for root in roots}
                extra = 1000 + 97 * index
                while len(values) < s:
                    values.add(extra % PRIME)
                    extra += 1
                block = full_block(values, m)
                locators.append(divide_exact(block, root_locator(roots)))
            assert rank(locators) == len(deletions), profile
            checked += 1
    return checked


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    checked = profile_check()
    assert all(8 >= threshold for _, threshold in PROFILES.values())
    packet_check()
    print(
        "RATE_HALF_LIST_B3_MULTIDELETION_MULTIFIBER_EXCLUSION_PASS "
        f"profiles={checked} official_uniform_threshold=8"
    )


if __name__ == "__main__":
    main()
