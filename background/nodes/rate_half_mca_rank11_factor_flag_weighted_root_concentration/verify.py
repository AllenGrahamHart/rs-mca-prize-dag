#!/usr/bin/env python3
"""Exact verifier for factor-flag weighted root concentration."""

from __future__ import annotations

import argparse
import copy
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
RANK1_FIELD = 2_130_706_433**6


def build(data: dict[str, object]) -> dict[str, object]:
    row = data["row"]
    expected = data["selection"]
    n, k, m, agreement = (row[x] for x in ("n", "k", "anchor_good_universe", "A"))
    multiplicity = n - agreement
    caps = {
        d: multiplicity * (comb(n - k + d, d) // comb(agreement - k + d, d))
        for d in (4, 5, 6)
    }
    assert caps == {4: 63_397_365_764, 5: 1_010_335_321_405, 6: 16_100_859_197_492}
    assert all((caps[d] // multiplicity) ** 2 < RANK1_FIELD for d in caps)

    def cell(cutoff: int) -> dict[str, int]:
        h = expected["residual_h"]
        residual_roots = row["H"] - cutoff + 1
        gap = residual_roots - h
        assert gap > 0
        factor_classes = m // cutoff
        dim2_classes = (m * (m - 1) * (m - 2)) // gap**3
        dim3_classes = (m * (m - 1)) // gap**2
        factor_cost = factor_classes * caps[5]
        dim2_cost = dim2_classes * caps[4]
        dim3_cost = dim3_classes * caps[6]
        union_cost = factor_cost + dim2_cost + dim3_cost
        paid_total = row["transverse"] + union_cost
        flag_mass = row["budget"] + 1 - paid_total
        output = h + 1
        return {
            "factor_cutoff": cutoff,
            "residual_h": h,
            "residual_zero_output": output,
            "residual_roots": residual_roots,
            "gap": gap,
            "factor_classes": factor_classes,
            "residual_dim2_classes": dim2_classes,
            "residual_dim3_classes": dim3_classes,
            "factor_cost": factor_cost,
            "dim2_cost": dim2_cost,
            "dim3_cost": dim3_cost,
            "union_cost": union_cost,
            "paid_total": paid_total,
            "flag_mass": flag_mass,
            "minimum_flag_classes": (flag_mass + caps[6] - 1) // caps[6],
            "coordinate_mass": (output * flag_mass + m - 1) // m,
        }

    selected = cell(expected["factor_cutoff"])
    assert selected == expected
    candidates = [cell(cutoff) for cutoff in range(1, row["H"] - expected["residual_h"] + 1)]
    best = min(candidates, key=lambda entry: (entry["union_cost"], entry["factor_cutoff"]))
    assert best["factor_cutoff"] == 650
    return {"selected": selected, "best_cutoff": best["factor_cutoff"]}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = []
    for key, delta in (
        ("flag_mass", 1),
        ("minimum_flag_classes", -1),
        ("coordinate_mass", -1),
        ("union_cost", 1),
    ):
        changed = copy.deepcopy(data)
        changed["selection"][key] += delta
        mutations.append(changed)
    caught = 0
    for mutation in mutations:
        try:
            build(mutation)
        except AssertionError:
            caught += 1
    assert caught == len(mutations)
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(CONTRACT.read_text())
    result = build(data)
    if args.tamper_selftest:
        print(f"RANK11_WEIGHTED_ROOT_TAMPER_PASS mutations={tamper_selftest(data)}/4")
        return
    selected = result["selected"]
    print(
        "RANK11_WEIGHTED_ROOT_PASS "
        f"flag_mass={selected['flag_mass']} classes={selected['minimum_flag_classes']} "
        f"coordinate_mass={selected['coordinate_mass']}"
    )


if __name__ == "__main__":
    main()
