#!/usr/bin/env python3
"""Verify the exact E1 class counts and clean-anchor loss allowances."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_clean_anchor_exact_collision_allowance"
TARGET = "unsafe_crossing_family_instantiation"
E1_TARGET = "e1_official_prime_exception_control"
ROWC_BUDGET = 1 << 122
PRIZE_BUDGET = 317494674775468773183020924238786383963

EXPECTED_PIN = {
    "upstream_commit": "b13de8113a03f06b6fc22bbd2f289a8abcdf7e95",
    "count_file": "tex/slackMCA_v4.tex",
    "count_file_sha256": "810ac469b8a8a8ba4638d882ec8426be95ffddf0f8888b83315afb4d60e990b4",
    "count_label": "thm:exactcount",
    "locator_label": "prop:qfloor",
    "budget_file": "tex/cs25_cap_v13_2.tex",
    "budget_file_sha256": "356f1ad4b972746b664260191387b25a89a2e10fcc61962a49dc8282412f93ce",
    "budget_label": "thm:capf-windows",
}


def a2_count(order: int, ell: int) -> int:
    half = order // 2
    total = 0
    for full_pairs in range(ell // 2 + 1):
        singleton_pairs = ell - 2 * full_pairs
        if singleton_pairs <= half and full_pairs <= half - singleton_pairs:
            total += math.comb(half, singleton_pairs) * 2**singleton_pairs
    return total


def minimum_pair_collisions(class_count: int, field_size: int) -> int:
    quotient, remainder = divmod(class_count, field_size)
    return field_size * quotient * (quotient - 1) // 2 + remainder * quotient


def subset_class_count(order: int, ell: int) -> int:
    """Count signed antipodal keys from all subsets, independently of formula."""
    half = order // 2
    keys = set()
    for subset in itertools.combinations(range(order), ell):
        selected = set(subset)
        key = tuple(
            int(index in selected) - int(index + half in selected)
            for index in range(half)
        )
        keys.add(key)
    return len(keys)


def integer_partitions(total: int, minimum: int = 1):
    if total == 0:
        yield ()
        return
    for first in range(minimum, total + 1):
        for tail in integer_partitions(total - first, first):
            yield (first,) + tail


def main() -> None:
    pin = json.loads((Path(__file__).with_name("source_pin.json")).read_text())
    assert pin == EXPECTED_PIN

    # Complete subset-to-class checks through order sixteen.
    small_checks = 0
    for order in range(2, 18, 2):
        for ell in range(order + 1):
            assert subset_class_count(order, ell) == a2_count(order, ell)
            small_checks += 1
    assert a2_count(16, 9) == 3280

    rows = (
        ("RowC-1/4", 1024, 256, 260, ROWC_BUDGET, 256, 65,
         1146852336572689151906730465296195854216377730651578907904,
         1146852336572689151901413553313056190724762502410457529599,
         382284112190896383970682459093111839235997652964233428737),
        ("RowC-1/8", 1024, 128, 132, ROWC_BUDGET, 256, 33,
         38001322036274275320505631960233903602944,
         37996005124291135657014016731992782224639,
         12668879649419138327999082396158341660417),
        ("RowC-1/16", 1024, 64, 66, ROWC_BUDGET, 512, 33,
         3413962861332812601133559951042096138635313539480064,
         3413962861332807284221576811378604523407072418101759,
         1137987620444272639348514363568529251287851553619457),
        ("prize-1/4", 1 << 41, 1 << 39, 558345748480, PRIZE_BUDGET, 256, 65,
         1146852336572689151906730465296195854216377730651578907904,
         1146852336572689151589235790520727081033356806412792523940,
         382284112190896384074741713357221542466466218296788430623),
        ("prize-1/8", 1 << 41, 1 << 38, 283467841536, PRIZE_BUDGET, 256, 33,
         38001322036274275320505631960233903602944,
         37683827361498806547322611035995117218980,
         12772938903683248031229550961490896662303),
        ("prize-1/16", 1 << 41, 1 << 37, 141733920768, PRIZE_BUDGET, 512, 33,
         3413962861332812601133559951042096138635313539480064,
         3413962861332495106458784482268913117711074753096100,
         1137987620444376698602778473271759719853184108621343),
    )
    for row in rows:
        (_, n, k, agreement, budget, expected_order, expected_ell,
         expected_k, expected_g, expected_b_min) = row
        assert n % (agreement - k) == 0
        order = n // (agreement - k)
        assert order == expected_order
        assert order % 2 == 0
        assert k * order % n == 0
        ell = k * order // n + 1
        assert ell == expected_ell
        class_count = a2_count(order, ell)
        assert class_count == expected_k
        assert class_count - budget - 1 == expected_g
        assert expected_g >= 0
        assert expected_b_min == (class_count + budget + 3) // 3
        assert minimum_pair_collisions(class_count, expected_b_min) <= expected_g
        assert minimum_pair_collisions(class_count, expected_b_min - 1) > expected_g

    # Every possible integer fiber profile at small K satisfies loss <= pairs.
    profile_checks = 0
    for class_count in range(1, 15):
        for profile in integer_partitions(class_count):
            image_size = len(profile)
            pair_count = sum(size * (size - 1) // 2 for size in profile)
            assert class_count - image_size <= pair_count
            profile_checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[E1_TARGET] == "TARGET"
    assert statuses[TARGET] == "TARGET"
    assert ("acl_count", NODE, "req") in edges
    assert ("qfloor_clean_anchor_norm_threshold_route_cut", NODE, "req") in edges
    assert ("v13_base_field_normalization_guard", NODE, "req") in edges
    assert (NODE, "e1_fullness", "req") in edges
    assert (NODE, E1_TARGET, "ev") in edges
    assert (NODE, TARGET, "ev") in edges
    assert "P <= K-B*-1" in statements[NODE]
    assert "b<=B* rules out direct E1" in statements[NODE]
    assert "b_pair_min=ceil((K+B*+1)/3)" in statements[NODE]
    assert "quotient orders N in {256,512}" in statements[E1_TARGET]

    print(
        "E1_CLEAN_ANCHOR_EXACT_COLLISION_ALLOWANCE_PASS "
        f"rows={len(rows)} small_checks={small_checks} profile_checks={profile_checks}"
    )


if __name__ == "__main__":
    main()
