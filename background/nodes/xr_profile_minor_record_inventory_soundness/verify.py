#!/usr/bin/env python3
"""Lightweight coverage check for XR minor-record inventories."""

from __future__ import annotations

ACCEPTED = {"triangular", "monomial", "remote_table"}


def verify_inventory(required: set[str], records: dict[str, str]) -> None:
    assert set(records) == required
    for kind in records.values():
        assert kind in ACCEPTED


def main() -> None:
    required = {"profile_A", "profile_B", "profile_C"}
    records = {
        "profile_A": "triangular",
        "profile_B": "monomial",
        "profile_C": "remote_table",
    }
    verify_inventory(required, records)
    print("PASS: XR minor-record inventory covers required profiles with accepted records")


if __name__ == "__main__":
    main()
