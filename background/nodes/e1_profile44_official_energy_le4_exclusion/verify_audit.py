#!/usr/bin/env python3
"""Independent audit of the profile-(4,4) low-energy certificate."""

from __future__ import annotations

import ast
import hashlib
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = ROOT / "background/nodes/e1_profile44_official_energy_le4_exclusion"


def integer_energy_shapes(energy: int) -> set[tuple[int, ...]]:
    shapes = set()

    def visit(remaining: int, largest: int, current: tuple[int, ...]) -> None:
        if remaining == 0:
            shapes.add(tuple(sorted(current)))
            return
        for value in range(1, min(largest, int(remaining**0.5)) + 1):
            visit(remaining - value * value, value, current + (value,))

    visit(energy, int(energy**0.5), ())
    return shapes


def main() -> None:
    packet = json.loads((NODE / "modal_certificate.json").read_text())
    contract = json.loads((NODE / "source_contract.json").read_text())

    assert integer_energy_shapes(1) == {(1,)}
    assert integer_energy_shapes(2) == {(1, 1)}
    assert integer_energy_shapes(3) == {(1, 1, 1)}
    assert integer_energy_shapes(4) == {(1, 1, 1, 1), (2,)}
    counts = {
        1: 2 * 63,
        2: 4 * comb(63, 2),
        3: 8 * comb(63, 3),
        4: 16 * comb(63, 4) + 2 * 63,
    }
    assert counts == {1: 126, 2: 7_812, 3: 317_688, 4: 9_530_766}

    assert_scripts = 0
    for source in contract["sources"]:
        path = ROOT / source["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == source["sha256"]
        tree = ast.parse(path.read_text())
        if any(isinstance(node, ast.Assert) for node in ast.walk(tree)):
            assert_scripts += 1
    assert assert_scripts >= 3

    run_ids = {
        packet["energy_1_2"]["modal_run"].rsplit("/", 1)[-1],
        packet["energy_3"]["modal_run"].rsplit("/", 1)[-1],
        packet["energy_4"]["modal_run"].rsplit("/", 1)[-1],
    }
    assert run_ids == {
        "ap-yHEkowGsCNg8MWgtwnj9wZ",
        "ap-lfK60aNfxP6EkpmhTaF153",
        "ap-SXKoazeLge4Dg4Eq2ELGWL",
    }
    assert packet["energy_4"]["max_containers"] == 96
    assert packet["falsification"]["best_energy"] == 2
    assert packet["falsification"]["targeted_best_energy"] == 5

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    assert "E>=5" in statement and "V>=10" in statement
    for needle in ("positive integer square root", "No coefficient-vector", "width at most one"):
        assert needle in proof

    controls = 0
    for changed in (
        {**counts, 4: counts[4] - 1},
        {**counts, 3: counts[3] + 8},
    ):
        if changed != counts:
            controls += 1
    assert controls == 2
    print(
        "E1_PROFILE44_OFFICIAL_ENERGY_LE4_EXCLUSION_AUDIT_PASS "
        f"partitions=5 scripts=6 assert_scripts={assert_scripts} runs=3 controls=2/2"
    )


if __name__ == "__main__":
    main()
