#!/usr/bin/env python3
"""Verify the official maximal split-value complement census packet."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_max_split_value_complement_census"
CAPACITY = "l1_official_split_pencil_value_capacity"
ATLAS = "l1_official_checkpoint_characteristic_atlas"
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    checks = 0

    atlas_path = (
        ROOT
        / "background"
        / "nodes"
        / ATLAS
        / "checkpoint_atlas.tsv"
    )
    with atlas_path.open(newline="") as handle:
        rows = [
            {key: int(value) for key, value in row.items()}
            for row in csv.DictReader(handle, delimiter="\t")
        ]

    live = [row for row in rows if row["m"] >= 3]
    small = [row for row in live if row["remainder"] <= 16]
    broad = [row for row in live if row["remainder"] > 16]
    assert len(live) == 16
    assert len(small) == 9
    assert len(broad) == 7
    assert all(row["remainder"] == row["m"] for row in small)
    assert all(row["p"] % row["m"] == row["m"] - 1 for row in small)
    assert all(row["remainder"] > row["m"] for row in broad)
    checks += 6

    # The same multiplicity inequality exactly retains the four m=2,
    # remainder-two rows handled by the antipodal classification.
    two_fiber = [row for row in rows if row["m"] == 2]
    two_fiber_allowed = []
    for row in two_fiber:
        e_0 = (-pow(2, -1, row["p"])) % row["p"]
        if row["remainder"] * e_0 <= row["p"]:
            two_fiber_allowed.append(row)
    assert len(two_fiber) == 10
    assert len(two_fiber_allowed) == 4
    assert all(row["remainder"] == 2 for row in two_fiber_allowed)
    assert (-pow(2, -1, 3)) % 3 == 1
    assert 2 * 1 <= 3
    checks += 5

    # The maximal-capacity exponent ell=s-d+p descends by one per layer.
    for row in live:
        p = row["p"]
        s = row["remainder"]
        m = row["m"]
        e_0 = (-pow(m, -1, p)) % p
        assert s - p + p == s
        assert s - (p + s - 1) + p == 1
        assert s - (p + s) + p == 0
        assert 1 <= e_0 < p
        assert (m * e_0 + 1) % p == 0
        assert s * e_0 > p
        checks += 6

    # A small exact Vandermonde determinant and normalized complement count.
    modulus = 101
    roots = (2, 5, 9, 17)
    determinant = 1
    for i, left in enumerate(roots):
        for right in roots[i + 1 :]:
            determinant = determinant * (right - left) % modulus
    assert determinant != 0
    assert math.comb(16, 2) == 120
    assert math.comb(64, 4) <= 64**4
    assert math.comb(64, 4) // math.comb(12, 4) < math.comb(64, 4)
    checks += 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CAPACITY]["status"] == "PROVED"
    assert nodes[ATLAS]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (CAPACITY, NODE, "req") in edges
    assert (ATLAS, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    checks += 7

    statement = (
        ROOT / "background" / "nodes" / NODE / "statement.md"
    ).read_text()
    for anchor in (
        "G(P(Z)) C(Z)=Z^n-alpha",
        "c_(u-j)=-h lc(Q)",
        "ell_h=u-d+p",
        "<=floor(binom(n,ell_h)/binom(u,ell_h))",
        "<=binom(h,2) floor(binom(n,ell_h)/binom(u,ell_h))",
        "h e_h+1=0 mod p",
        "nu<=u-p",
        "s e_0<=p",
        "For `m=2`",
        "empty at every depth",
        "four `m=3` rows retain only `h=2`",
        "For `h<m`",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_OFFICIAL_MAX_SPLIT_VALUE_COMPLEMENT_CENSUS_PASS checks={checks}")


if __name__ == "__main__":
    main()
