#!/usr/bin/env python3
"""Verify the exact K'=45 full completion-product payment."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import itertools
import json
import sys
from functools import lru_cache
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "f935bbbc6266e4df746a0b9f4d4d53a0afef01a5fa5a384199f682bee8018c6f"
PARENT_VERIFY = ROOT / "background/nodes/rate_half_mca_rank11_k44_branch_lattice_payment/verify.py"
JOINT_VERIFY = ROOT / "background/nodes/rate_half_mca_sparse_circuit_support4_external_charge/verify.py"
SUPPORTS = tuple(range(2, 10))


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"module {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PARENT = load_module("k44_parent_for_k45", PARENT_VERIFY)
JOINT = load_module("joint_support4_for_k45", JOINT_VERIFY)
LEDGER = PARENT.LEDGER
CAPS = PARENT.CAPS


def source_options(kprime: int, support: int, baseline: dict[int, int]):
    q = kprime - 10
    m = 67472 + kprime
    options = [
        (f"c{support}d{defect}", defect, PARENT.terminal_caps(q, m, support, defect, baseline))
        for defect in range(10 - support)
    ]
    fallback = dict(baseline)
    fallback[support] = min(
        fallback[support], CAPS.deletion_cap(m, support, q - (10 - support))
    )
    options.append((f"c{support}F", None, fallback))
    return options


@lru_cache(maxsize=None)
def branch_summary(kprime: int) -> dict[str, Any]:
    q = kprime - 10
    m = 67472 + kprime
    baseline = CAPS.baseline_caps(q, m)
    options = {support: source_options(kprime, support, baseline) for support in SUPPORTS}
    digest = hashlib.sha256()
    premium_sum = 0
    leaf_count = 0
    joint_count = 0
    tightened_count = 0
    maximum = (-1, "")
    maximum_before = (-1, "")
    maximum_joint = (-1, "")
    maximum_nonjoint = (-1, "")

    for choices in itertools.product(*(options[support] for support in SUPPORTS)):
        caps = dict(baseline)
        defects: dict[int, int | None] = {}
        labels = []
        for support, (label, defect, option_caps) in zip(SUPPORTS, choices):
            labels.append(label)
            defects[support] = defect
            for target in SUPPORTS:
                caps[target] = min(caps[target], option_caps[target])
        label = "/".join(labels)
        before = sum(LEDGER.DEFICITS[target] * caps[target] for target in SUPPORTS)
        if before > maximum_before[0]:
            maximum_before = (before, label)

        joint = defects[4] is not None and defects[5] is not None
        if joint:
            joint_count += 1
            require(q > int(defects[4]) + int(defects[5]), "joint overlap condition")
            joint_cap = JOINT.cap_for_defects(
                kprime, m, int(defects[4]), int(defects[5])
            )[0]
            if joint_cap < caps[4]:
                tightened_count += 1
            caps[4] = min(caps[4], joint_cap)
        premium = sum(LEDGER.DEFICITS[target] * caps[target] for target in SUPPORTS)
        if premium > maximum[0]:
            maximum = (premium, label)
        if joint and premium > maximum_joint[0]:
            maximum_joint = (premium, label)
        if not joint and premium > maximum_nonjoint[0]:
            maximum_nonjoint = (premium, label)
        digest.update(f"{label}:{premium}\n".encode())
        premium_sum += premium
        leaf_count += 1

    return {
        "option_counts": {str(support): len(options[support]) for support in SUPPORTS},
        "leaf_count": leaf_count,
        "joint_branch_count": joint_count,
        "nonjoint_branch_count": leaf_count - joint_count,
        "joint_tightened_count": tightened_count,
        "maximum_before_joint": maximum_before[0],
        "maximum_before_joint_branch": maximum_before[1],
        "maximum_joint_premium": maximum_joint[0],
        "maximum_joint_branch": maximum_joint[1],
        "maximum_nonjoint_premium": maximum_nonjoint[0],
        "maximum_nonjoint_branch": maximum_nonjoint[1],
        "active_branch": maximum[1],
        "completion_premium": maximum[0],
        "premium_sum": premium_sum,
        "branch_digest_sha256": digest.hexdigest(),
    }


@lru_cache(maxsize=None)
def expected(kprime: int) -> dict[str, Any]:
    old = LEDGER.row(kprime)
    n = 1048576 + kprime
    m = 67472 + kprime
    summary = branch_summary(kprime)
    premium = int(summary["completion_premium"])
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
    ceiling = (
        LEDGER.RECORD_FLOOR * 55 * comb(m, 11)
        - 55 * comb(n, 11)
        - 55 * kernel
        - marks
        - 1
    ) // LEDGER.RECORD_FLOOR
    return {
        "n": n,
        "m": m,
        "q": kprime - 10,
        "max_core": int(old["max_core"]),
        "chart": int(old["chart"]),
        "kernel_capacity": kernel,
        "rank_nine_marks": marks,
        **summary,
        "safe_premium_ceiling": ceiling,
        "premium_ceiling_margin": ceiling - premium,
        "full_rank_capacity": full_rank,
        "total_capacity": total,
        "required_component_incidence": demand,
        "gap": demand - total,
        "record_coefficient_cross": coefficient,
        "floor_record_raw_cross": raw,
    }


def contract() -> dict[str, object]:
    row45 = expected(45)
    row46 = dict(expected(46))
    row46["capacity_excess"] = -row46.pop("gap")
    return {
        "schema": "rate-half-mca-rank11-k45-full-completion-product-payment-v1",
        "dependencies": [
            "rate_half_mca_rank11_k44_branch_lattice_payment",
            "rate_half_mca_sparse_circuit_support4_external_charge",
        ],
        "parameters": {
            "closed_row": 45,
            "new_closed_prefix": [10, 45],
            "first_method_wall": 46,
            "residual_record_floor": LEDGER.RECORD_FLOOR,
            "source_support_order": list(SUPPORTS),
            "branch_stream_format": "c2*/c3*/c4*/c5*/c6*/c7*/c8*/c9*:premium\\n",
            "joint_cap_condition": "support4 and support5 both terminal",
            "deficit_weights": {
                str(support): LEDGER.DEFICITS[support] for support in SUPPORTS
            },
            "K45": row45,
            "K46_method_wall": row46,
            "remaining_rank9_interval": [46, 15528],
        },
        "claim": (
            "The full completion product plus the joint support-four charge "
            "closes the rank-nine component target at K'=45."
        ),
        "nonclaim": (
            "The same payment fails at K'=46. No rank-eight, rank-eleven, "
            "active-v4, KoalaBear, or prize closure is asserted."
        ),
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-k45-full-completion-product-payment-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_rank11_k44_branch_lattice_payment",
            "rate_half_mca_sparse_circuit_support4_external_charge",
        ],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("closed_row") == 45, "closed row")
    require(p.get("new_closed_prefix") == [10, 45], "prefix")
    require(p.get("first_method_wall") == 46, "wall")
    require(p.get("residual_record_floor") == LEDGER.RECORD_FLOOR, "record floor")
    require(p.get("source_support_order") == list(SUPPORTS), "source order")
    require(
        p.get("branch_stream_format")
        == "c2*/c3*/c4*/c5*/c6*/c7*/c8*/c9*:premium\\n",
        "stream format",
    )
    require(
        p.get("joint_cap_condition") == "support4 and support5 both terminal",
        "joint condition",
    )
    require(
        p.get("deficit_weights")
        == {str(support): LEDGER.DEFICITS[support] for support in SUPPORTS},
        "deficits",
    )

    row45 = p.get("K45")
    require(isinstance(row45, dict), "K45")
    require(row45 == expected(45), "K45 exact replay")
    require(row45["leaf_count"] == 362880, "leaf count")
    require(row45["joint_branch_count"] == 259200, "joint count")
    require(row45["nonjoint_branch_count"] == 103680, "nonjoint count")
    require(row45["active_branch"] == "c2F/c3F/c4F/c5F/c6F/c7F/c8F/c9F", "active")
    require(row45["gap"] > 0 and row45["floor_record_raw_cross"] > 0, "K45 sign")
    require(row45["premium_ceiling_margin"] > 0, "K45 ceiling")
    require(row45["maximum_before_joint"] > row45["safe_premium_ceiling"], "joint needed")

    wall = p.get("K46_method_wall")
    require(isinstance(wall, dict), "K46")
    expected_wall = dict(expected(46))
    expected_wall["capacity_excess"] = -expected_wall.pop("gap")
    require(wall == expected_wall, "K46 exact replay")
    require(wall["active_branch"] == "c2F/c3F/c4F/c5F/c6F/c7F/c8F/c9F", "K46 active")
    require(wall["capacity_excess"] > 0 and wall["floor_record_raw_cross"] < 0, "K46 sign")
    require(wall["premium_ceiling_margin"] < 0, "K46 ceiling")
    require(p.get("remaining_rank9_interval") == [46, 15528], "remaining")
    require("fails at K'=46" in str(data.get("nonclaim")), "nonclaim")
    return {
        "gap": int(row45["gap"]),
        "wall": int(wall["capacity_excess"]),
        "leaves": int(row45["leaf_count"]),
    }


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("closed_row", 44),
        lambda item: item["parameters"].__setitem__("source_support_order", [5, 4, 3, 2]),
        lambda item: item["parameters"]["K45"].__setitem__("leaf_count", 362879),
        lambda item: item["parameters"]["K45"].__setitem__("joint_branch_count", 0),
        lambda item: item["parameters"]["K45"].__setitem__("branch_digest_sha256", "0" * 64),
        lambda item: item["parameters"]["K45"].__setitem__("completion_premium", 0),
        lambda item: item["parameters"]["K45"].__setitem__("gap", 0),
        lambda item: item["parameters"]["K46_method_wall"].__setitem__("capacity_excess", 0),
        lambda item: item["parameters"].__setitem__("remaining_rank9_interval", [45, 15528]),
        lambda item: item.__setitem__("nonclaim", "K'=46 closed"),
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
        "RATE_HALF_MCA_RANK11_K45_FULL_COMPLETION_PRODUCT_PAYMENT_PASS "
        f"leaves={result['leaves']} gap={result['gap']} "
        f"wall={result['wall']} controls={controls}"
    )


if __name__ == "__main__":
    main()
