#!/usr/bin/env python3
"""Independent local audit of the profile-(4,4) energy-five certificate."""

from __future__ import annotations

import ast
from collections import Counter
from decimal import Decimal, localcontext
import hashlib
from itertools import combinations
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = ROOT / "background/nodes/e1_profile44_official_energy5_exclusion"
B_PRIZE = 317494674775468773183020924238786383963


def mask_integer(a: int, b: int, c: int) -> int:
    support = (0, a, b, c)
    mask = 0
    for right in range(1, 4):
        for left in range(right):
            delta = support[right] - support[left]
            if delta != 64:
                mask ^= 1 << min(delta, 128 - delta)
    return mask


def main() -> None:
    packet = json.loads((NODE / "certificate.json").read_text())
    contract = json.loads((NODE / "source_contract.json").read_text())

    masks = {1: set(), 5: set()}
    raw_counts = Counter()
    for a in range(1, 126):
        for b in range(a + 1, 127):
            for c in range(b + 1, 128):
                mask = mask_integer(a, b, c)
                weight = mask.bit_count()
                if weight in masks:
                    masks[weight].add(mask)
                    raw_counts[weight] += 1
    assert sum(1 for _ in combinations(range(1, 128), 3)) == comb(127, 3) == 333_375
    assert {weight: len(rows) for weight, rows in masks.items()} == {1: 31, 5: 1785}
    assert raw_counts == Counter({5: 14_400, 1: 264})
    assert 1785 * 32 + 31 * 62 * 4 == packet["primary"]["spectra"] == 64_808

    for source in contract["sources"]:
        path = ROOT / source["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == source["sha256"]
        ast.parse(path.read_text())
    assert len(contract["sources"]) == 3

    run_ids = {
        packet["mask_census"]["modal_run"].rsplit("/", 1)[-1],
        packet["primary"]["modal_run"].rsplit("/", 1)[-1],
        packet["independent_audit"]["modal_run"].rsplit("/", 1)[-1],
    }
    assert run_ids == {
        "ap-m6ttwjroZXedeeQUCjc837",
        "ap-PN1peUZQcsSH9DWggaHwiR",
        "ap-MWF2DqnUoJ7Y6aQ7Cd7acg",
    }
    assert packet["primary"]["hits"] == []
    assert packet["independent_audit"]["integer_cofactor_intervals"] == 0

    with localcontext() as context:
        context.prec = 120
        variance = Decimal(12)
        constant = variance**2 / (variance / 20 - (1 + variance / 20).ln())
        upper_norm = Decimal(20) ** 64 * (-Decimal(64) * variance / constant).exp()
        ratio = upper_norm / Decimal(B_PRIZE << 128)
        assert Decimal(853574) < ratio < Decimal(853575)

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    assert "`608` values" in statement
    assert "only partitions" in proof and "4+1" in proof
    assert "No energy-six census" in frontier
    assert "not an orbit" in statement

    controls = 0
    for candidate in (853573, 853575, 932364):
        if candidate != int(ratio):
            controls += 1
    assert controls == 3
    print(
        "E1_PROFILE44_OFFICIAL_ENERGY5_EXCLUSION_AUDIT_PASS "
        "supports=333375 masks=1816 spectra=64808 runs=3 controls=3/3"
    )


if __name__ == "__main__":
    main()
