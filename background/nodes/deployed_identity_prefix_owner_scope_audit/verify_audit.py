#!/usr/bin/env python3
"""Mutation audit for deployed identity-prefix ownership."""

from __future__ import annotations

import copy
import json
from pathlib import Path


def valid(row: dict) -> bool:
    expected_owner = "SIMPLE_POLE_LIST" if row["object"] == "MCA" else "Q_BOUNDARY"
    return (
        row["a_plus"] == row["a0"] + 1
        and row["attack_a0"] > row["B_star"]
        and row["attack_a_plus"] <= row["B_star"]
        and row["owner"] == expected_owner
    )


def main() -> None:
    rows = json.loads(Path(__file__).with_name("deployed_rows.json").read_text())["rows"]
    assert all(valid(row) for row in rows)
    mutations = []
    for key, value in (
        ("owner", "APERIODIC"),
        ("a_plus", rows[0]["a0"] + 2),
        ("attack_a0", rows[0]["B_star"]),
    ):
        row = copy.deepcopy(rows[0])
        row[key] = value
        mutations.append(not valid(row))
    assert all(mutations)
    print("DEPLOYED_IDENTITY_PREFIX_OWNER_SCOPE_AUDIT_MUTATION_PASS mutations=3/3")


if __name__ == "__main__":
    main()
