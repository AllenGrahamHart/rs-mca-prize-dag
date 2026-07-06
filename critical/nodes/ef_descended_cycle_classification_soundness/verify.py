#!/usr/bin/env python3
"""Tiny check for exhaustive EF descended-cycle classifications."""

from __future__ import annotations

ALLOWED = {"base_descended", "tower_confined", "noncontainment_degenerate"}


def uncovered(cycles: list[str], classification: dict[str, str]) -> list[str]:
    return [
        c
        for c in cycles
        if c not in classification or classification[c] not in ALLOWED
    ]


def main() -> None:
    cycles = ["C0", "C1", "C2"]
    classification = {
        "C0": "base_descended",
        "C1": "tower_confined",
        "C2": "noncontainment_degenerate",
    }
    assert uncovered(cycles, classification) == []
    assert uncovered(cycles + ["C3"], classification) == ["C3"]
    print("PASS: exhaustive EF descended-cycle classification excludes leakage")


if __name__ == "__main__":
    main()
