#!/usr/bin/env python3
"""Shared exact checker for residual zero-loop complete-Vieta lanes."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_zero_loop_433_complete_vieta_probe.py"
)
SPEC = importlib.util.spec_from_file_location("router", SCRIPT)
ROUTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ROUTER)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_rows(cell, name, packet_indices, expected_assignments,
                expected_unresolved, expected_kill_row):
    comparisons = family_tests = 0
    for packet in packet_indices:
        result = ROUTER.probe(cell, packet, name)
        require(len(result["assignments"]) == expected_assignments[packet],
                f"{cell}/{packet}/{name} assignment census")
        require(len(result["unresolved_families"]) == expected_unresolved[packet],
                f"{cell}/{packet}/{name} family census")
        require(not result["survivors"], f"{cell}/{packet}/{name} finite survivor")
        family = ROUTER.family_vieta_cut(
            cell, packet, name, result["families"]
        )
        require(not family["survivors"], f"{cell}/{packet}/{name} family survivor")
        expected_tests = 2 * expected_unresolved[packet]
        require(family["tests"] == expected_tests,
                f"{cell}/{packet}/{name} family tests")
        expected_histogram = (
            {} if expected_tests == 0 else {expected_kill_row: expected_tests}
        )
        require(family["kill_rows"] == expected_histogram,
                f"{cell}/{packet}/{name} kill rows")
        comparisons += len(result["records"]) * len(result["assignments"])
        family_tests += family["tests"]
    return comparisons, family_tests
