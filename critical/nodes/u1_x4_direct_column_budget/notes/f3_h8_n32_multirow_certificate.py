#!/usr/bin/env python3
"""Run complete n=32,h=8 anchored certificates at several boundary primes."""

from __future__ import annotations

import json

from f3_h8_n32_full_certificate import ROOT, run_certificate


OUT = (
    ROOT
    / "critical/nodes/u1_x4_direct_column_budget/notes"
    / "f3_h8_n32_multirow_certificate.json"
)

PRIMES = (1153, 3137, 12289)


def main() -> None:
    rows = []
    for p in PRIMES:
        row = run_certificate(p)
        expected = {
            "n": 32,
            "h": 8,
            "p": p,
            "W": 32,
            "hashed": 2629575,
            "probed": 7888725,
            "anchored_toral_trades": 3,
            "anchored_nontoral_trades": 0,
            "partial": False,
            "complete": True,
            "direct_n3_exceeded": False,
        }
        for key, value in expected.items():
            if row.get(key) != value:
                raise AssertionError((p, key, row.get(key), value, row))
        rows.append(row)

    OUT.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    for row in rows:
        print(json.dumps(row, sort_keys=True))
    print("H8_N32_MULTIROW_CERTIFICATE_PASS")


if __name__ == "__main__":
    main()
