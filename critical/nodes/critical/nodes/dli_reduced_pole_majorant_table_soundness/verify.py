#!/usr/bin/env python3
"""Tiny coverage/domination check for DLI reduced-pole majorant tables."""

from __future__ import annotations


def verify_majorant_table(universe: set[str], true_degrees: dict[str, int], majorants: dict[str, int], budget: int) -> None:
    assert set(true_degrees) == universe
    assert set(majorants) == universe
    for key in universe:
        assert 0 <= true_degrees[key] <= majorants[key]
    assert sum(majorants.values()) < budget


def main() -> None:
    universe = {"tau0", "tau1", "tau2"}
    true_degrees = {"tau0": 2, "tau1": 0, "tau2": 3}
    majorants = {"tau0": 2, "tau1": 1, "tau2": 4}
    verify_majorant_table(universe, true_degrees, majorants, budget=8)
    print("PASS: DLI reduced-pole majorant table covers and dominates below budget")


if __name__ == "__main__":
    main()
