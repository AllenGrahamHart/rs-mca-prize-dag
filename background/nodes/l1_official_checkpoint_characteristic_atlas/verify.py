#!/usr/bin/env python3
"""Verify the exhaustive official checkpoint characteristic atlas."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_checkpoint_characteristic_atlas"
ROUTER = "l1_official_frobenius_checkpoint_q_router"
CAPACITY = "l1_official_split_pencil_value_capacity"
CONSUMER = "l1_mixed_petal_amplification"
ATLAS = Path(__file__).with_name("checkpoint_atlas.tsv")
MR_BASES = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % prime == 0:
            return value == prime
    odd = value - 1
    twos = 0
    while odd % 2 == 0:
        twos += 1
        odd //= 2
    for base in MR_BASES:
        if base % value == 0:
            continue
        witness = pow(base, odd, value)
        if witness in (1, value - 1):
            continue
        for _ in range(twos - 1):
            witness = witness * witness % value
            if witness == value - 1:
                break
        else:
            return False
    return True


def order_at_most_16(value: int, modulus: int) -> int | None:
    for order in (1, 2, 4, 8, 16):
        if pow(value, order, modulus) == 1:
            return order
    return None


def generate_atlas() -> list[tuple[int, int, int, int, int, int]]:
    rows: list[tuple[int, int, int, int, int, int]] = []
    for exponent in range(13, 45):
        n = 1 << exponent
        step = 1 << (exponent - 6)
        residues = {
            sign * pow(5, index * step, n) % n
            for sign in (1, -1)
            for index in range(16)
        }
        assert len(residues) == 32
        for characteristic in sorted(residues):
            order = order_at_most_16(characteristic, n)
            if (
                characteristic >= 3583
                and characteristic < n
                and order is not None
                and characteristic**order < 1 << 256
                and is_prime(characteristic)
            ):
                multiplicity, remainder = divmod(n, characteristic)
                rows.append(
                    (exponent, n, characteristic, order, multiplicity, remainder)
                )
    return rows


def read_atlas() -> list[tuple[int, int, int, int, int, int]]:
    with ATLAS.open(newline="") as source:
        reader = csv.DictReader(source, delimiter="\t")
        assert reader.fieldnames == ["s", "n", "p", "ord", "m", "remainder"]
        return [
            tuple(int(row[key]) for key in reader.fieldnames)
            for row in reader
        ]


def main() -> None:
    checks = 0
    generated = generate_atlas()
    recorded = read_atlas()
    assert generated == recorded
    assert len(recorded) == 59
    checks += 2

    histogram = Counter(row[4] for row in recorded)
    assert histogram == Counter({1: 33, 2: 10, 3: 4, 4: 4, 5: 2, 7: 1, 8: 4, 16: 1})
    assert sum(count for multiplicity, count in histogram.items() if multiplicity >= 3) == 16
    checks += 2

    two_point = [(row[1], row[2]) for row in recorded if row[4] == 2 and row[5] == 2]
    assert two_point == [
        (1 << 14, 8191),
        (1 << 18, 131071),
        (1 << 20, 524287),
        (1 << 32, 2147483647),
    ]
    assert [row[5] for row in recorded if row[4] == 2 and row[5] != 2] == [
        1026,
        4098,
        8190,
        524290,
        524286,
        2147483646,
    ]
    checks += 2

    for exponent, n, characteristic, order, multiplicity, remainder in recorded:
        assert n == 1 << exponent
        assert 13 <= exponent <= 44
        assert 3583 <= characteristic < n < 1 << 45
        assert is_prime(characteristic)
        assert order in (1, 2, 4, 8, 16)
        assert pow(characteristic, order, n) == 1
        assert characteristic**order < 1 << 256
        assert divmod(n, characteristic) == (multiplicity, remainder)
        checks += 8

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[ROUTER]["status"] == "PROVED"
    assert nodes[CAPACITY]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (ROUTER, NODE, "req") in edges
    assert (CAPACITY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    checks += 7

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "ord_n(p) in {1,2,4,8,16}",
        "exactly the 59 rows",
        "| rows | 33 | 10 | 4 | 4 | 2 | 1 | 4 | 1 |",
        "16 rows: m>=3",
        "exactly four have the two-point complement",
        "precisely `n/2`",
        "39 theorem-empty at t=p",
        "No `m<=2` minimum-width computation remains",
        "Rows with `p>=n`",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_OFFICIAL_CHECKPOINT_CHARACTERISTIC_ATLAS_PASS checks={checks}")


if __name__ == "__main__":
    main()
