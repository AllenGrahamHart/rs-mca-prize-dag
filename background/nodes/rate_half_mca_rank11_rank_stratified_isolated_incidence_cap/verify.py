#!/usr/bin/env python3
"""Verify the rank-stratified isolated-incidence contract."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "25def3f3f47dedd1d7aeb704c24dd28c00b507fda019bd72e9240ed6bcbd123c"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate(data: object) -> None:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-rank-stratified-isolated-incidence-cap-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_rank11_dense_locator_component_incidence_dichotomy"],
        "dependency",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("correction_dimension") == 10, "dimension")
    require(p.get("tuple_size") == 11, "tuple")
    require(p.get("dense_locator_degree") == 18, "locator")
    require(p.get("retained_slopes_are_distinct") is True, "distinct slopes")
    require(p.get("retained_slopes_avoid_locator_roots") is True, "nonroots")
    require(p.get("old_generic_isolated_cap_per_tuple") == 198, "old cap")
    require(p.get("new_record_isolated_cap_per_tuple") == 1, "new cap")
    require(
        p.get("component_lower_bound") == "N*C(m_prime,11)-C(n_prime,11)",
        "lower bound",
    )
    pins = data.get("logical_pins")
    require(isinstance(pins, list) and len(pins) == 5, "pins")


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("correction_dimension", 9),
        lambda item: item["parameters"].__setitem__("tuple_size", 10),
        lambda item: item["parameters"].__setitem__("new_record_isolated_cap_per_tuple", 2),
        lambda item: item["parameters"].__setitem__("retained_slopes_avoid_locator_roots", False),
        lambda item: item.__setitem__("logical_pins", []),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (AssertionError, KeyError, TypeError):
            rejected += 1
    require(rejected == len(mutations), "tamper controls")
    return rejected


def main() -> None:
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    validate(data)
    controls = tamper_selftest(data)
    print(
        "RATE_HALF_MCA_RANK11_RANK_STRATIFIED_ISOLATED_INCIDENCE_CAP_PASS "
        f"isolated_per_tuple=1 controls={controls}"
    )


if __name__ == "__main__":
    main()
