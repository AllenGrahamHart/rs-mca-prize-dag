#!/usr/bin/env python3
"""Verify the exact official fixed affine-reflection pencil cap."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "ad63a47a7e9a528e1379d3c42cad6781a3be64dafbeaa4c643b180c6c21096eb"
RESULT = ROOT / "experiments/prize_resolution/rate_half_mca_rank11_affine_reflection_cyclotomic_census_result.json"
SOURCE = ROOT / "experiments/prize_resolution/rate_half_mca_rank11_affine_reflection_cyclotomic_census.cpp"
DISPATCHER = ROOT / "experiments/prize_resolution/rate_half_mca_rank11_affine_reflection_cyclotomic_census_modal.py"
CHECKER = ROOT / "experiments/prize_resolution/verify_rate_half_mca_rank11_affine_reflection_cyclotomic_census.py"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def validate(contract: object, result: object) -> dict[str, int]:
    require(isinstance(contract, dict) and isinstance(result, dict), "objects")
    require(
        contract.get("schema")
        == "rate-half-mca-rank11-exception-spi-affine-reflection-fixed-pencil-cap-v1",
        "schema",
    )
    p, n, index, generator = (
        contract.get("official_base_prime"),
        contract.get("official_domain_order"),
        contract.get("cyclotomic_index"),
        contract.get("primitive_generator"),
    )
    require((p, n, index, generator) == (2130706433, 2**21, 1016, 3), "pins")
    require(is_prime(p), "official prime")
    require(p - 1 == index * n, "index")
    require(pow(generator, p - 1, p) == 1, "Fermat")
    require(pow(generator, (p - 1) // 2, p) != 1, "2-primary order")
    require(pow(generator, (p - 1) // 127, p) != 1, "127-primary order")
    require(contract.get("coset_representatives") == index, "representatives")
    require(contract.get("completed_shards") == 93, "shards")

    for key, path in (
        ("source_sha256", SOURCE),
        ("dispatcher_sha256", DISPATCHER),
        ("outcome_neutral_checker_sha256", CHECKER),
        ("result_sha256", RESULT),
    ):
        require(contract.get(key) == sha256(path), key)

    require(result.get("status") == "COMPLETE" and result.get("failures") == [], "complete")
    require(result.get("p") == p and result.get("domain_order") == n, "result field")
    require(result.get("index") == index and result.get("primitive_generator") == generator, "result quotient")
    require(result.get("completed_shards") == 93, "result shards")
    rows = result.get("rows")
    require(isinstance(rows, list) and len(rows) == index, "rows")

    inverse_two = pow(2, p - 2, p)
    counts: list[int] = []
    fibers: list[int] = []
    fixed_cosets = 0
    expected_c = 1
    for expected_index, row in enumerate(rows):
        require(
            isinstance(row, list)
            and len(row) == 4
            and all(isinstance(value, int) for value in row),
            "row shape",
        )
        row_index, c, production, audit = row
        require((row_index, c) == (expected_index, expected_c), "row identity")
        require(production == audit and 0 <= production <= n, "paired count")
        fixed = int(pow(c * inverse_two % p, n, p) == 1)
        require(production % 2 == fixed, "reflection parity")
        fixed_cosets += fixed
        counts.append(production)
        fibers.append((production - fixed) // 2)
        expected_c = expected_c * generator % p

    maximum = max(counts)
    maximizers = [j for j, count in enumerate(counts) if count == maximum]
    maximum_fibers = max(fibers)
    require(sum(counts) == n - 1 == result.get("count_sum"), "first moment")
    require(maximum == result.get("maximum_reflection_points"), "result maximum")
    require(maximizers == result.get("maximizing_indices"), "result maximizers")
    require(maximum == contract.get("maximum_reflection_points") == 2308, "maximum")
    require(maximum_fibers == contract.get("maximum_nonfixed_fibers") == 1154, "fiber cap")
    require(maximizers == contract.get("maximizing_indices") == [74], "maximizer")
    require(rows[74][1] == contract.get("maximizing_representative") == 1177199610, "representative")
    require(fibers[74] == 1154 and counts[74] == 2308, "sharp row")
    require(not contract.get("maximizer_has_fixed_point"), "sharp fixed point")
    require(fixed_cosets == contract.get("fixed_point_cosets") == 1, "fixed cosets")
    require(sum(fibers) == contract.get("nonfixed_fiber_sum_over_cosets") == n // 2 - 1, "fiber sum")
    require(
        contract.get("hypothetical_pair_type_count") * maximum_fibers
        == contract.get("hypothetical_synchronized_cap")
        == 67348594,
        "hypothetical cap",
    )
    require("not an aggregate" in str(contract.get("nonclaim")).lower(), "nonclaim")
    return {"maximum": maximum, "fibers": maximum_fibers, "fixed_cosets": fixed_cosets}


def tamper_selftest(contract: dict[str, object], result: dict[str, object]) -> int:
    mutations = (
        lambda c, r: c.__setitem__("official_base_prime", 2130706431),
        lambda c, r: c.__setitem__("completed_shards", 92),
        lambda c, r: c.__setitem__("maximum_reflection_points", 2307),
        lambda c, r: c.__setitem__("maximum_nonfixed_fibers", 1153),
        lambda c, r: c.__setitem__("maximizing_indices", [75]),
        lambda c, r: c.__setitem__("maximizing_representative", 1),
        lambda c, r: r["rows"][0].__setitem__(3, r["rows"][0][3] + 1),
        lambda c, r: r["rows"][74].__setitem__(2, 2310),
        lambda c, r: c.__setitem__("nonclaim", "aggregate payment"),
    )
    caught = 0
    for mutate in mutations:
        altered_contract = copy.deepcopy(contract)
        altered_result = copy.deepcopy(result)
        mutate(altered_contract, altered_result)
        try:
            validate(altered_contract, altered_result)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutations")
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    require(sha256(CONTRACT) == CONTRACT_SHA256, "contract hash")
    contract = json.loads(CONTRACT.read_text())
    result = json.loads(RESULT.read_text())
    checked = validate(contract, result)
    if args.tamper_selftest:
        print(f"RANK11_AFFINE_FIXED_PENCIL_CAP_TAMPER_PASS mutations={tamper_selftest(contract, result)}/9")
        return
    print(
        "RANK11_AFFINE_FIXED_PENCIL_CAP_PASS "
        f"maximum={checked['maximum']} fibers={checked['fibers']} "
        f"fixed_cosets={checked['fixed_cosets']}"
    )


if __name__ == "__main__":
    main()
