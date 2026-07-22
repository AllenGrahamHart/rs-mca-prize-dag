#!/usr/bin/env python3
"""Verify broad-checkpoint Frobenius orbit closures and DAG wiring."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_broad_checkpoint_frobenius_periodicity_exclusion"
SUPPLIER = "l1_official_first_checkpoint_split_pencil_reduction"
ATLAS = "l1_official_checkpoint_characteristic_atlas"
CONSUMER = "l1_mixed_petal_amplification"


def read_tsv(path: Path) -> list[dict[str, int]]:
    with path.open(newline="") as handle:
        return [
            {key: int(value) for key, value in row.items()}
            for row in csv.DictReader(handle, delimiter="\t")
        ]


def orbit_record(n: int, p: int, order: int) -> tuple[int, int, int]:
    seen = bytearray(n)
    for start in range(p):
        value = start
        for _ in range(order):
            seen[value] = 1
            value = value * p % n
    closure = sum(seen)
    divisor = 0
    for frequency, present in enumerate(seen):
        if not present:
            divisor = math.gcd(divisor, frequency)
    return closure, n - closure, divisor


def main() -> None:
    checks = 0
    atlas = read_tsv(
        ROOT
        / "background"
        / "nodes"
        / ATLAS
        / "checkpoint_atlas.tsv"
    )
    table = read_tsv(Path(__file__).with_name("broad_orbit_closure.tsv"))
    broad = [
        row for row in atlas
        if row["m"] >= 3 and row["remainder"] > 16
    ]
    assert len(broad) == len(table) == 7
    checks += 1

    table_by_key = {(row["n"], row["p"]): row for row in table}
    assert {(row["n"], row["p"]) for row in broad} == set(table_by_key)
    checks += 1

    for source in broad:
        row = table_by_key[(source["n"], source["p"])]
        assert row["ord"] == source["ord"]
        assert row["m"] == source["m"]
        assert row["remainder"] == source["remainder"]
        closure, missing, divisor = orbit_record(
            row["n"], row["p"], row["ord"]
        )
        assert (closure, missing, divisor) == (
            row["closure"], row["missing"], row["gcd"]
        )
        assert closure + missing == row["n"]
        assert divisor > 0 and divisor % 2 == 0
        assert row["p"] % divisor != 0
        checks += 7

    residual = [
        row for row in atlas
        if row["m"] >= 3 and row["remainder"] <= 16
    ]
    assert len(residual) == 9
    assert all(row["remainder"] == row["m"] for row in residual)
    assert {row["m"] for row in residual} == {4, 8, 16}
    assert all(row["n"] == row["m"] * (row["p"] + 1) for row in residual)
    checks += 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert nodes[ATLAS]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (SUPPLIER, NODE, "req") in edges
    assert (ATLAS, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    checks += 7

    statement = Path(__file__).with_name("statement.md").read_text()
    for anchor in (
        "A(T)=sum_(i in I) T^i-sum_(j in J) T^j",
        "S_(n,p)=union_(r>=0)",
        "gcd(M)",
        "periodic with period `n/g`",
        "no two complete p-point fibers",
        "Only the nine rows",
        "s=m in {4,8,16}",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_BROAD_CHECKPOINT_FROBENIUS_PERIODICITY_PASS checks={checks}")


if __name__ == "__main__":
    main()
