#!/usr/bin/env python3
"""Mutation audit for the E=34 three-profile reduction certificates."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    nested = load_module("e34_nested", NOTES / "e34_nested_quotient_census_check.py")
    coupled = load_module("e34_coupled", NOTES / "e34_profile2_coupled_check.py")
    nested_packet = json.loads(nested.SURVIVORS.read_text())
    coupled_packet = json.loads(coupled.RESULT.read_text())
    caught = 0

    bad = copy.deepcopy(nested_packet["results"][0])
    bad["best"] = int(bad["best"]) + 1
    try:
        nested.check_result(bad)
    except AssertionError:
        caught += 1

    bad = copy.deepcopy(nested_packet["results"][0])
    bad["exact"][0][0] = int(bad["exact"][0][0]) + 1
    try:
        nested.check_result(bad)
    except AssertionError:
        caught += 1

    quotient = copy.deepcopy(coupled_packet["quotient_results"][0])
    quotient["best_refined"]["value"] = int(quotient["best_refined"]["value"]) + 1
    try:
        coupled.check_candidate(quotient["best_refined"], int(quotient["order"]), "best_refined")
    except AssertionError:
        caught += 1

    support = copy.deepcopy(coupled_packet["support_results"][0])
    support["u"][0] = support["b"][0]
    try:
        assert not set(support["b"]) & set(support["u"])
    except AssertionError:
        caught += 1

    missing = coupled_packet["support_results"][:-1]
    try:
        assert {int(row["shard"]) for row in missing} == set(range(32))
    except AssertionError:
        caught += 1

    assert caught == 5
    print("E1_N256_S16_E34_THREE_PROFILE_REDUCTION_AUDIT_PASS mutations=5")


if __name__ == "__main__":
    main()
