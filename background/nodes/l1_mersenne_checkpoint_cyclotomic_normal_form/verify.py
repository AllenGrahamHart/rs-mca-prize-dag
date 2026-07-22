#!/usr/bin/env python3
"""Verify the exact Mersenne checkpoint cyclotomic chambers."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_checkpoint_cyclotomic_normal_form"
SUPPLIER = "l1_official_broad_checkpoint_frobenius_periodicity_exclusion"
CONSUMER = "l1_mixed_petal_amplification"


def direct_closure(n: int, p: int) -> set[int]:
    seen = set(range(p))
    stack = list(seen)
    while stack:
        value = stack.pop()
        nxt = value * p % n
        if nxt not in seen:
            seen.add(nxt)
            stack.append(nxt)
    return seen


def formula_closure(m: int, nbase: int) -> set[int]:
    out = set()
    for q in range(m):
        for b in range(nbase):
            if b == 0:
                hit = q == 0
            else:
                g = math.gcd(2 * b, m)
                hit = q % g == 0 or (q - (b - 1)) % g == 0
            if hit:
                out.add(q * nbase + b)
    return out


def expected_complement(m: int, nbase: int) -> int:
    return {4: 2 * nbase + 1,
            8: 9 * nbase // 2 + 1,
            16: 37 * nbase // 4 + 1}[m]


def main() -> None:
    checks = 0
    for m in (4, 8, 16):
        for nbase in (m, 2 * m, 4 * m, 8 * m):
            p = nbase - 1
            n = m * nbase
            actual = direct_closure(n, p)
            predicted = formula_closure(m, nbase)
            assert actual == predicted
            assert set(range(nbase)) <= actual
            assert n - len(actual) == expected_complement(m, nbase)
            checks += 3

    atlas_path = (ROOT / "background" / "nodes" /
                  "l1_official_checkpoint_characteristic_atlas" /
                  "checkpoint_atlas.tsv")
    with atlas_path.open() as handle:
        rows = [{key: int(value) for key, value in row.items()}
                for row in csv.DictReader(handle, delimiter="\t")]
    survivors = [(row["n"], row["p"], row["m"]) for row in rows
                 if row["m"] in (4, 8, 16)
                 and row["n"] == row["m"] * (row["p"] + 1)]
    expected_rows = [
        (32768, 8191, 4),
        (65536, 8191, 8),
        (131072, 8191, 16),
        (524288, 131071, 4),
        (1048576, 131071, 8),
        (2097152, 524287, 4),
        (4194304, 524287, 8),
        (8589934592, 2147483647, 4),
        (17179869184, 2147483647, 8),
    ]
    assert survivors == expected_rows
    checks += len(survivors)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (SUPPLIER, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    checks += 5

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(MCN2)", "(MCN3)", "(MCN4)", "(MCN5)",
                   "This is an exact normal form", "close L1"):
        assert anchor in statement
        checks += 1

    print(f"L1_MERSENNE_CHECKPOINT_CYCLOTOMIC_NORMAL_FORM_PASS checks={checks}")


if __name__ == "__main__":
    main()
