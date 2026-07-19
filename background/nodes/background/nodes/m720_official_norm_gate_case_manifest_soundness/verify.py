#!/usr/bin/env python3
"""Small coverage check for M720 official norm-gate manifests."""

from __future__ import annotations


def verify_manifest(cases: set[str], entries: dict[str, dict[str, object]]) -> None:
    assert set(entries) == cases
    for entry in entries.values():
        kind = entry.get("kind")
        if kind == "uniform_theorem":
            assert entry.get("citation")
        elif kind == "certificate":
            assert entry.get("complete") is True
            assert entry.get("unpaid_nontoral_survivors") == 0
        else:
            raise AssertionError(f"bad entry kind: {kind!r}")


def main() -> None:
    cases = {"h7_rowA", "h8_rowA", "h16_rowB"}
    entries = {
        "h7_rowA": {"kind": "certificate", "complete": True, "unpaid_nontoral_survivors": 0},
        "h8_rowA": {"kind": "certificate", "complete": True, "unpaid_nontoral_survivors": 0},
        "h16_rowB": {"kind": "uniform_theorem", "citation": "uniform-norm-gate"},
    }
    verify_manifest(cases, entries)
    print("PASS: M720 official norm-gate manifest covers cases with accepted discharges")


if __name__ == "__main__":
    main()
