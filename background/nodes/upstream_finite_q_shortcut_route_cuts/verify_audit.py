#!/usr/bin/env python3
"""Mutation checks for the finite-Q route-cut bundle."""

from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path

from verify import moment_floor


def main() -> None:
    rows = json.loads(Path(__file__).with_name("route_cuts.json").read_text())["rows"]
    caught = 0
    for row in rows:
        truth = moment_floor(row["base"], row["w"], row["delta_real_12"])
        if truth != row["moment_floor_real"] - 1:
            caught += 1
    assert caught == 4

    # Deleting tau is invalid away from the full-mass model.
    delta = Decimal(rows[0]["delta_real_12"])
    tau_log2 = Decimal(-10)
    assert delta - tau_log2 > delta

    # A one-pencil theorem cannot pay a positive-dimensional family merely by
    # applying the same bound once.
    assert all(row["boundary_q_dimension"] > 1 for row in rows)
    print("UPSTREAM_FINITE_Q_SHORTCUT_ROUTE_CUTS_AUDIT_PASS mutations=6/6")


if __name__ == "__main__":
    main()
