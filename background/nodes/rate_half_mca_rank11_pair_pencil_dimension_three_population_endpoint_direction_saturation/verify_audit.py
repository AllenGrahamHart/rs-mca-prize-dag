#!/usr/bin/env python3
"""Independent audit of the q=3170 direction-saturation bank."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "ffbc2eaed1d0d6d1a495ba685ed7bce7d0ad87e8de4864dfe31ff63aa99ec260"


def c2(value: int) -> int:
    return value * (value - 1) // 2


def ceil_ratio(a: int, b: int) -> int:
    value = a // b
    return value if value * b == a else value + 1


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    direction_max = c2(3170) // c2(15)
    assert direction_max == data["direction_population_ceiling"] == 47836
    rows = []
    for kprime in range(4960, 4983):
        full = -13661092 + 2953 * kprime
        roots = 210 * full
        directions = ceil_ratio(roots, kprime - 1)
        deficit = direction_max * (kprime - 1) - roots
        rows.append((directions, deficit, roots))
    assert rows[0] == (41746, 30203244, 207015480)
    assert rows[-1] == (44301, 17612776, 220658340)
    assert min(item[0] for item in rows) == data["direction_population_floor"]
    assert max(item[1] for item in rows) == data["aggregate_degree_deficit_ceiling"]
    assert Fraction(rows[0][2], direction_max * 4959) == \
        Fraction(data["saturation_numerator"], data["saturation_denominator"])
    assert 4960 - 2609 == data["individual_direction_root_floor"] == 2351

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pair_pencil_dimension_three_population_endpoint_plane_line_design"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().lower().split())
    assert "R<=floor(C(3170,2)/105)=47836" in proof
    assert "aggregate" in audit
    print("RANK11_D3_DIRECTION_SAT_AUDIT_PASS rows=23 directions=41746..47836 saturation=5750430/6589409")


if __name__ == "__main__":
    main()
