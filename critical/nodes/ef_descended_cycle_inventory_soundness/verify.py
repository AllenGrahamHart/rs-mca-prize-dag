#!/usr/bin/env python3
"""Small coverage check for EF descended-cycle inventories."""

from __future__ import annotations

ALLOWED = {"base_descended", "tower_confined", "noncontainment_degenerate"}


def verify_inventory(cycles: set[str], labels: dict[str, str]) -> None:
    assert set(labels) == cycles
    for label in labels.values():
        assert label in ALLOWED


def main() -> None:
    cycles = {"C0", "C1", "C2"}
    labels = {
        "C0": "base_descended",
        "C1": "tower_confined",
        "C2": "noncontainment_degenerate",
    }
    verify_inventory(cycles, labels)
    print("PASS: EF descended-cycle inventory covers all cycles with allowed labels")


if __name__ == "__main__":
    main()
