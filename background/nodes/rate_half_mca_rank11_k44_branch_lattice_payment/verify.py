#!/usr/bin/env python3
"""Verify the exact K'=44 completion branch-lattice payment."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "fb48b423a9f8b9aa11be869b91ed7edb21332feb48cfb4f9eec7070264661cc2"
PARENT_VERIFY = (
    ROOT
    / "background/nodes/rate_half_mca_rank11_k43_descending_support_ladder_payment/verify.py"
)
SOURCE_ORDER = (5, 4, 3, 2)
REFINED_PARENTS = ("c5_defect_2", "c5_defect_3")


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def load_parent():
    spec = importlib.util.spec_from_file_location("k43_parent_for_k44", PARENT_VERIFY)
    require(spec is not None and spec.loader is not None, "parent module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PARENT = load_parent()
LEDGER = PARENT.LEDGER
CAPS = PARENT.PARENT


def terminal_caps(
    q: int, m: int, source: int, defect: int, inherited: dict[int, int]
) -> dict[int, int]:
    caps = dict(inherited)
    caps[source] = min(caps[source], CAPS.deletion_cap(m, source, q - defect))
    for target in range(2, 10):
        if source + (defect + 1) * target - defect - 1 <= 10:
            carrier = q + source - 1 + defect * (target - 1)
            caps[target] = min(
                caps[target],
                comb(carrier, target) * comb(m - target, 11 - target),
            )
    return caps


def parent_leaf_caps(kprime: int) -> dict[str, dict[int, int]]:
    q = kprime - 10
    m = 67472 + kprime
    inherited = CAPS.baseline_caps(q, m)
    prefixes: list[str] = []
    leaves: dict[str, dict[int, int]] = {}
    for source in SOURCE_ORDER:
        for defect in range(10 - source):
            label = "__".join(prefixes + [f"c{source}_defect_{defect}"])
            leaves[label] = terminal_caps(q, m, source, defect, inherited)
        inherited = dict(inherited)
        inherited[source] = min(
            inherited[source],
            CAPS.deletion_cap(m, source, q - (10 - source)),
        )
        prefixes.append(f"c{source}_fallback")
    leaves["__".join(prefixes)] = inherited
    return leaves


def branch_premiums(kprime: int) -> dict[str, int]:
    q = kprime - 10
    m = 67472 + kprime
    parents = parent_leaf_caps(kprime)
    leaves: dict[str, dict[int, int]] = {}
    for label, inherited in parents.items():
        if label not in REFINED_PARENTS:
            leaves[label] = inherited
            continue
        for defect in range(4):
            leaves[f"{label}__c6_defect_{defect}"] = terminal_caps(
                q, m, 6, defect, inherited
            )
        fallback = dict(inherited)
        fallback[6] = min(fallback[6], CAPS.deletion_cap(m, 6, q - 4))
        leaves[f"{label}__c6_fallback"] = fallback
    return {
        label: sum(
            LEDGER.DEFICITS[support] * caps[support]
            for support in range(2, 10)
        )
        for label, caps in leaves.items()
    }


def expected(kprime: int) -> dict[str, Any]:
    old = LEDGER.row(kprime)
    n = 1048576 + kprime
    m = 67472 + kprime
    branches = branch_premiums(kprime)
    active = max(branches, key=branches.get)
    premium = branches[active]
    marks = int(old["marks"])
    kernel = int(old["kernel"])
    full_rank = (marks + LEDGER.RECORD_FLOOR * premium) // 55
    total = kernel + full_rank
    demand = LEDGER.RECORD_FLOOR * comb(m, 11) - comb(n, 11)
    coefficient = 55 * comb(m, 11) - premium
    raw = (
        LEDGER.RECORD_FLOOR * coefficient
        - 55 * comb(n, 11)
        - 55 * kernel
        - marks
    )
    return {
        "n": n,
        "m": m,
        "q": kprime - 10,
        "isolated_global_cap": comb(n, 11),
        "max_core": int(old["max_core"]),
        "chart": int(old["chart"]),
        "kernel_capacity": kernel,
        "rank_nine_marks": marks,
        "uncoupled_completion_premium": int(old["premium"]),
        "branch_premiums": branches,
        "active_branch": active,
        "completion_premium": premium,
        "premium_saving": int(old["premium"]) - premium,
        "full_rank_capacity": full_rank,
        "total_capacity": total,
        "required_component_incidence": demand,
        "gap": demand - total,
        "record_coefficient_cross": coefficient,
        "floor_record_raw_cross": raw,
    }


def contract() -> dict[str, object]:
    row44 = expected(44)
    row45 = expected(45)
    wall = dict(row45)
    for key in ("isolated_global_cap", "uncoupled_completion_premium", "premium_saving"):
        wall.pop(key)
    wall["capacity_excess"] = -wall.pop("gap")
    return {
        "schema": "rate-half-mca-rank11-k44-branch-lattice-payment-v1",
        "dependencies": [
            "rate_half_mca_rank11_k43_descending_support_ladder_payment",
            "rate_half_mca_sparse_circuit_completion_branch_lattice_refinement",
        ],
        "parameters": {
            "closed_row": 44,
            "new_closed_prefix": [10, 44],
            "first_method_wall": 45,
            "residual_record_floor": LEDGER.RECORD_FLOOR,
            "deficit_weights": {
                str(support): LEDGER.DEFICITS[support] for support in range(2, 10)
            },
            "parent_source_order": list(SOURCE_ORDER),
            "refined_parent_leaves": list(REFINED_PARENTS),
            "refinement_source_support": 6,
            "parent_branch_count": 27,
            "refined_branch_count": 35,
            **row44,
            "K45_method_wall": wall,
            "remaining_rank9_interval": [45, 15528],
        },
        "claim": (
            "The exhaustive completion branch-lattice payment closes the "
            "rank-nine component target at K'=44."
        ),
        "nonclaim": (
            "The same payment fails at K'=45. No rank-eight, chronology, active-v4, "
            "KoalaBear, or prize closure is asserted."
        ),
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-k44-branch-lattice-payment-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_rank11_k43_descending_support_ladder_payment",
            "rate_half_mca_sparse_circuit_completion_branch_lattice_refinement",
        ],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("closed_row") == 44, "closed row")
    require(p.get("new_closed_prefix") == [10, 44], "prefix")
    require(p.get("first_method_wall") == 45, "wall row")
    require(p.get("residual_record_floor") == LEDGER.RECORD_FLOOR, "record floor")
    require(p.get("parent_source_order") == list(SOURCE_ORDER), "source order")
    require(p.get("refined_parent_leaves") == list(REFINED_PARENTS), "parents")
    require(p.get("refinement_source_support") == 6, "refinement source")
    require(p.get("parent_branch_count") == 27, "parent count")
    require(p.get("refined_branch_count") == 35, "refined count")
    require(
        p.get("deficit_weights")
        == {str(support): LEDGER.DEFICITS[support] for support in range(2, 10)},
        "deficit weights",
    )

    row44 = expected(44)
    for key, value in row44.items():
        require(p.get(key) == value, f"K44 {key}")
    require(len(row44["branch_premiums"]) == 35, "K44 leaves")
    require(row44["active_branch"] == "c5_defect_2__c6_defect_2", "K44 active")
    require(row44["gap"] > 0, "K44 gap")
    require(row44["record_coefficient_cross"] > 0, "K44 coefficient")
    require(row44["floor_record_raw_cross"] > 0, "K44 raw")

    row45 = expected(45)
    wall = p.get("K45_method_wall")
    require(isinstance(wall, dict), "K45 wall")
    wanted_wall = dict(row45)
    for key in ("isolated_global_cap", "uncoupled_completion_premium", "premium_saving"):
        wanted_wall.pop(key)
    wanted_wall["capacity_excess"] = -wanted_wall.pop("gap")
    require(wall == wanted_wall, "K45 exact wall")
    require(row45["active_branch"] == "c5_defect_2__c6_defect_2", "K45 active")
    require(row45["gap"] < 0 and row45["floor_record_raw_cross"] < 0, "K45 sign")
    require(p.get("remaining_rank9_interval") == [45, 15528], "remaining")
    require("fails at K'=45" in str(data.get("nonclaim")), "nonclaim")
    return {
        "gap": int(row44["gap"]),
        "wall": -int(row45["gap"]),
        "branches": len(row44["branch_premiums"]),
    }


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("closed_row", 43),
        lambda item: item["parameters"].__setitem__("refined_parent_leaves", ["c5_defect_2"]),
        lambda item: item["parameters"].__setitem__("refined_branch_count", 34),
        lambda item: item["parameters"]["branch_premiums"].__setitem__("c5_defect_2__c6_defect_2", 0),
        lambda item: item["parameters"].__setitem__("active_branch", "c5_defect_4"),
        lambda item: item["parameters"].__setitem__("completion_premium", 0),
        lambda item: item["parameters"].__setitem__("gap", 0),
        lambda item: item["parameters"].__setitem__("floor_record_raw_cross", 0),
        lambda item: item["parameters"]["K45_method_wall"].__setitem__("capacity_excess", 0),
        lambda item: item["parameters"].__setitem__("remaining_rank9_interval", [44, 15528]),
        lambda item: item.__setitem__("nonclaim", "K'=45 closed"),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (Reject, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "tamper controls")
    return rejected


def main() -> None:
    if sys.argv[1:] == ["--write"]:
        CONTRACT.write_text(json.dumps(contract(), indent=2) + "\n")
        print(f"WROTE {CONTRACT}")
        return
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    controls = tamper_selftest(data)
    print(
        "RATE_HALF_MCA_RANK11_K44_BRANCH_LATTICE_PAYMENT_PASS "
        f"branches={result['branches']} gap={result['gap']} "
        f"wall={result['wall']} controls={controls}"
    )


if __name__ == "__main__":
    main()
