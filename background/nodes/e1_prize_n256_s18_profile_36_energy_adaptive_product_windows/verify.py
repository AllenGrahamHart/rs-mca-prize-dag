#!/usr/bin/env python3
"""Verify the profile-(3,6) energy-adaptive product windows."""

from __future__ import annotations

from fractions import Fraction
import hashlib
from math import isqrt
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_profile_36_energy_adaptive_product_windows"
PARENTS = {
    "e1_prize_n256_s18_profile_36_bounded_product_windows",
    "e1_prize_n256_s18_profile_36_m1538_exclusion",
}
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
COUNT = 64
MEAN = Fraction(18)
GLOBAL_CAP = Fraction(144)
DENOMINATOR = 2**192
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
WINDOWS = {256: (48, 60, 46), 514: (24, 34, 22)}
PARITY_L1 = {
    7: {3: 5, 7: 7},
    8: {4: 6, 8: 8},
    9: {1: 5, 5: 7, 9: 9},
    10: {2: 6, 6: 8, 10: 10},
    11: {3: 7, 7: 9, 11: 11},
}
PARITY_EXCLUDED = {(9, 1), (10, 2), (11, 3), (11, 7)}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sqrt_interval(value: Fraction) -> tuple[Fraction, Fraction]:
    scaled_square = value.numerator * DENOMINATOR**2 // value.denominator
    floor = isqrt(scaled_square)
    lower = Fraction(floor, DENOMINATOR)
    if floor * floor * value.denominator == value.numerator * DENOMINATOR**2:
        return lower, lower
    return lower, Fraction(floor + 1, DENOMINATOR)


def product_intervals(
    variance: int, cap_override: int | None = None
) -> list[tuple[Fraction, Fraction]]:
    cap = min(
        GLOBAL_CAP,
        Fraction(cap_override) if cap_override is not None else MEAN + variance,
    )
    rows = []
    total_sum = COUNT * MEAN
    total_square = COUNT * variance
    for capped_count in range(COUNT):
        residual_count = COUNT - capped_count
        residual_mean = (total_sum - capped_count * cap) / residual_count
        if residual_mean <= 0 or residual_mean > cap:
            continue
        residual_square = (
            total_square
            - capped_count * (cap - MEAN) ** 2
            - residual_count * (residual_mean - MEAN) ** 2
        )
        if residual_square < 0:
            continue
        residual_variance = residual_square / residual_count
        if residual_variance == 0:
            value = cap**capped_count * residual_mean**residual_count
            rows.append((value, value))
            continue
        for lower_count in range(1, residual_count):
            upper_count = residual_count - lower_count
            lower_square = residual_variance * upper_count / lower_count
            upper_square = residual_variance * lower_count / upper_count
            if lower_square >= residual_mean**2:
                continue
            if upper_square > (cap - residual_mean) ** 2:
                continue
            lower_delta = sqrt_interval(lower_square)
            upper_delta = sqrt_interval(upper_square)
            low_value = (
                residual_mean - lower_delta[1],
                residual_mean - lower_delta[0],
            )
            high_value = (
                residual_mean + upper_delta[0],
                residual_mean + upper_delta[1],
            )
            rows.append(
                (
                    cap**capped_count
                    * low_value[0] ** lower_count
                    * high_value[0] ** upper_count,
                    cap**capped_count
                    * low_value[1] ** lower_count
                    * high_value[1] ** upper_count,
                )
            )
    assert rows
    return rows


def parity_l1_bounds(energy: int) -> dict[int, int]:
    bounds: dict[int, int] = {}
    for threes in range(energy // 9 + 1):
        for twos in range((energy - 9 * threes) // 4 + 1):
            ones = energy - 9 * threes - 4 * twos
            odd_weight = ones + threes
            l1_norm = ones + 2 * twos + 3 * threes
            if odd_weight:
                bounds[odd_weight] = max(bounds.get(odd_weight, 0), l1_norm)
    return bounds


def multiplicity(state: tuple[tuple[int, int], ...]) -> int:
    support = [position for position, value in state if abs(value) == 1]
    for derivative in range(16):
        if sum((derivative & ~position) == 0 for position in support) % 2:
            return derivative
    return 16


def energy(state: tuple[tuple[int, int], ...]) -> int:
    values = [0] * 64
    for index, (left, left_value) in enumerate(state):
        for right, right_value in state[index + 1 :]:
            delta = right - left
            if delta < 64:
                values[delta] += left_value * right_value
            elif delta > 64:
                values[128 - delta] -= left_value * right_value
    return sum(value * value for value in values)


def main() -> None:
    node_dir = ROOT / "background/nodes" / NODE
    pin = json.loads((node_dir / "source_pin.json").read_text())
    for key in (
        "parent_statement", "parent_proof", "mu1_statement", "mu1_proof",
        "certificate", "search", "search_result", "norm", "norm_result",
        "chord_count",
    ):
        assert sha256(ROOT / pin[f"{key}_file"]) == pin[f"{key}_sha256"]

    comparisons = 0
    for cofactor, (onset, old_upper, boundary) in WINDOWS.items():
        target = cofactor * P_MIN
        for variance in range(onset, old_upper + 1, 2):
            rows = product_intervals(variance)
            assert all(upper < target for _, upper in rows)
            comparisons += len(rows)
        boundary_rows = product_intervals(boundary)
        assert any(lower > target for lower, _ in boundary_rows)
        comparisons += len(boundary_rows)

    assert {energy_value: parity_l1_bounds(energy_value) for energy_value in range(7, 12)} == PARITY_L1
    for energy_value, rows_by_q in PARITY_L1.items():
        for odd_weight, l1_bound in rows_by_q.items():
            rows = product_intervals(2 * energy_value, 18 + 2 * l1_bound)
            target = 514 * P_MIN
            excluded = all(upper < target for _, upper in rows)
            survives = any(lower > target for lower, _ in rows)
            assert excluded != survives
            assert excluded == ((energy_value, odd_weight) in PARITY_EXCLUDED)
            comparisons += len(rows)
    assert comparisons == 6273

    search = json.loads((ROOT / pin["search_result_file"]).read_text())
    assert search["source_sha256"] == pin["search_sha256"]
    assert search["shards"] == 64 and search["seconds"] == 60.0
    found_states = []
    for row in search["rows"]:
        if not row["found"]:
            continue
        state = tuple((int(position), int(value)) for position, value in row["state"])
        assert sum(abs(value) == 1 for _, value in state) == 6
        assert sum(abs(value) == 2 for _, value in state) == 3
        assert multiplicity(state) == 1
        assert energy(state) == row["energy"] in (15, 17)
        assert sum(value * pow(3, position, 257) for position, value in state) % 257 == 0
        found_states.append(state)
    assert len(found_states) == 5 and min(energy(state) for state in found_states) == 15

    norms = json.loads((ROOT / pin["norm_result_file"]).read_text())
    assert norms["source_sha256"] == pin["norm_sha256"]
    assert norms["search_sha256"] == pin["search_result_sha256"]
    assert norms["complete"] is True and norms["agreement"] is True
    norm_states = []
    for row in norms["rows"]:
        state = tuple((int(position), int(value)) for position, value in row["state"])
        norm = int(row["norm"])
        assert row["flint_pari_agree"] is True and row["valuation"] == 1
        assert norm % 514 == 0 and int(row["quotient"]) == norm // 514
        assert row["quotient_relation"] == "below" and norm // 514 < P_MIN
        norm_states.append(state)
    assert sorted(norm_states) == sorted(found_states)

    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("m=256: V<=46", "m=514: V<=22", "(11,11)"):
        assert text in statement
    for text in ("6273", "18+V", "(9,1),(10,2),(11,3),(11,7)"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert all((parent, NODE, "req") in edges for parent in PARENTS)
    assert all((NODE, target, "ev") in edges for target in TARGETS)

    print(
        "E1_PRIZE_N256_S18_PROFILE_36_ENERGY_ADAPTIVE_PRODUCT_WINDOWS_PASS "
        f"comparisons={comparisons} live_m514_strata=9 witnesses={len(found_states)}"
    )


if __name__ == "__main__":
    main()
