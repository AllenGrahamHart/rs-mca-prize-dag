#!/usr/bin/env python3
"""Verify the exact K'=42 cross-support completion-defect payment."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "db90a48687728e7e6490e5ee976b54b3eda5b35b7184be7fc4a98e82c3a635b8"
PARENT_VERIFY = (
    ROOT
    / "background/nodes/rate_half_mca_rank11_k24_k40_full_deficit_shadow_payment/verify.py"
)


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def load_parent():
    spec = importlib.util.spec_from_file_location("full_deficit_parent_k42", PARENT_VERIFY)
    require(spec is not None and spec.loader is not None, "parent module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PARENT = load_parent()


def deletion_cap(m: int, support: int, ceiling: int) -> int:
    values = [PARENT.completion_value(m, support, b) for b in range(ceiling + 1)]
    return comb(m, support - 1) * max(values) // support


def carrier_cap(q: int, m: int, defect: int, target: int) -> int:
    carrier = q + 4 + defect * (target - 1)
    return comb(carrier, target) * comb(m - target, 11 - target)


def carrier_valid(defect: int, target: int) -> bool:
    return 5 + (defect + 1) * target - defect - 1 <= 10


def baseline_caps(q: int, m: int) -> dict[int, int]:
    return {
        support: (
            PARENT.defect_cap(q, m, support)[0]
            if support <= 5
            else PARENT.universal_cap(q, m, support)[0]
        )
        for support in range(2, 10)
    }


def branch_premiums(kprime: int) -> dict[str, int]:
    q = kprime - 10
    m = 67472 + kprime
    base = baseline_caps(q, m)
    branches: dict[str, int] = {}
    for defect in range(5):
        caps = dict(base)
        caps[5] = min(caps[5], deletion_cap(m, 5, q - defect))
        for target in range(2, 10):
            if carrier_valid(defect, target):
                caps[target] = min(caps[target], carrier_cap(q, m, defect, target))
        branches[f"defect_{defect}"] = sum(
            PARENT.DEFICITS[support] * caps[support] for support in range(2, 10)
        )
    caps = dict(base)
    caps[5] = min(caps[5], deletion_cap(m, 5, q - 5))
    branches["fallback"] = sum(
        PARENT.DEFICITS[support] * caps[support] for support in range(2, 10)
    )
    return branches


def expected(kprime: int) -> dict[str, object]:
    old = PARENT.row(kprime)
    n = 1048576 + kprime
    m = 67472 + kprime
    branches = branch_premiums(kprime)
    premium = max(branches.values())
    marks = int(old["marks"])
    kernel = int(old["kernel"])
    full_rank = (marks + PARENT.RECORD_FLOOR * premium) // 55
    total = kernel + full_rank
    demand = PARENT.RECORD_FLOOR * comb(m, 11) - comb(n, 11)
    coefficient = 55 * comb(m, 11) - premium
    raw = (
        PARENT.RECORD_FLOOR * coefficient
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
        "completion_premium": premium,
        "premium_saving": int(old["premium"]) - premium,
        "full_rank_capacity": full_rank,
        "total_capacity": total,
        "required_component_incidence": demand,
        "gap": demand - total,
        "record_coefficient_cross": coefficient,
        "floor_record_raw_cross": raw,
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-k42-cross-support-defect-payment-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_rank11_k41_sharp_isolated_payment",
            "rate_half_mca_sparse_circuit_cross_support_defect_carrier",
        ],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("closed_row") == 42, "closed row")
    require(p.get("new_closed_prefix") == [10, 42], "prefix")
    require(p.get("first_method_wall") == 43, "wall row")
    require(p.get("residual_record_floor") == PARENT.RECORD_FLOOR, "record floor")
    require(
        p.get("deficit_weights")
        == {str(support): PARENT.DEFICITS[support] for support in range(2, 10)},
        "deficit weights",
    )
    require(p.get("source_support") == 5, "source support")
    require(p.get("carrier_defects") == list(range(5)), "carrier defects")
    require(
        p.get("branch_partition")
        == "s=q-max_A b_A for s=0..4, otherwise max_A b_A<=q-5",
        "branch partition",
    )
    require(p.get("fallback_completion_ceiling") == "q-5", "fallback")

    row42 = expected(42)
    for key, value in row42.items():
        require(p.get(key) == value, f"K42 {key}")
    require(row42["completion_premium"] == row42["branch_premiums"]["fallback"], "K42 active")
    require(row42["gap"] > 0, "K42 gap")
    require(row42["record_coefficient_cross"] > 0, "K42 coefficient")
    require(row42["floor_record_raw_cross"] > 0, "K42 raw")

    row43 = expected(43)
    wall = p.get("K43_method_wall")
    require(isinstance(wall, dict), "K43 wall")
    expected_wall = dict(row43)
    expected_wall.pop("isolated_global_cap")
    expected_wall.pop("uncoupled_completion_premium")
    expected_wall.pop("premium_saving")
    expected_wall["capacity_excess"] = -expected_wall.pop("gap")
    require(wall == expected_wall, "K43 exact wall")
    require(row43["gap"] < 0, "K43 wall sign")
    require(row43["floor_record_raw_cross"] < 0, "K43 raw sign")
    require(p.get("remaining_rank9_interval") == [43, 15528], "remaining")
    require("fails at K'=43" in str(data.get("nonclaim")), "nonclaim")
    return {
        "gap": int(row42["gap"]),
        "wall": -int(row43["gap"]),
        "branches": len(row42["branch_premiums"]),
    }


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("closed_row", 41),
        lambda item: item["parameters"].__setitem__("branch_partition", "overlapping"),
        lambda item: item["parameters"]["deficit_weights"].__setitem__("2", 35),
        lambda item: item["parameters"]["branch_premiums"].__setitem__("defect_0", 0),
        lambda item: item["parameters"].__setitem__("completion_premium", 0),
        lambda item: item["parameters"].__setitem__("gap", 0),
        lambda item: item["parameters"].__setitem__("floor_record_raw_cross", 0),
        lambda item: item["parameters"]["K43_method_wall"].__setitem__("capacity_excess", 0),
        lambda item: item["parameters"].__setitem__("remaining_rank9_interval", [42, 15528]),
        lambda item: item.__setitem__("nonclaim", "K'=43 closed"),
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
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    controls = tamper_selftest(data)
    print(
        "RATE_HALF_MCA_RANK11_K42_CROSS_SUPPORT_DEFECT_PAYMENT_PASS "
        f"branches={result['branches']} gap={result['gap']} "
        f"wall={result['wall']} controls={controls}"
    )


if __name__ == "__main__":
    main()
