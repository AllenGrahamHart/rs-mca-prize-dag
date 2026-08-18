#!/usr/bin/env python3
"""Verify the pole-simple small-owner payment arithmetic and source pins."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "02a025756473cfeac6a481f2bd933f152beace01589bbcadd10a1c1bf6798518"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-pole-simple-small-owner-atom-payment-import-v1",
        "schema",
    )
    require(data.get("upstream_sha") == "93fba1be3", "upstream pin")
    require(data.get("upstream_theorem") == "thm:owner-localization", "theorem pin")
    require(data.get("upstream_corollary") == "cor:small-owner", "corollary pin")
    n = data.get("domain_size")
    m = data.get("support_size")
    dimension = data.get("code_dimension")
    degree = data.get("denominator_degree_cap")
    require((n, m, dimension, degree) == (2097152, 1116048, 1048576, 67472), "row pins")
    small_owner = 2 * m - dimension
    require(data.get("small_owner_max") == small_owner == 1183520, "small owner")
    require(data.get("first_large_owner") == small_owner + 1 == 1183521, "large owner")
    require(data.get("sub_support_owner_cap") == n - m + 1 == 981105, "sub-support cap")
    require(data.get("small_owner_record_cap") == n == 2097152, "record cap")
    for rho in (0, 1, degree // 2, degree):
        n0 = n - rho
        require(rho + (n0 - m + 1) == n - m + 1, "small-g telescope")
        require(rho + n0 == n, "half-distance telescope")
    require("remains open" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_heavy_ruling_triple_owner_pole_simple_router",
        "rate_half_mca_rank11_cross_type_global_atom_record_extension",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"small_owner": small_owner, "record_cap": n}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("upstream_sha", "2788d5ec3"),
        lambda item: item.__setitem__("domain_size", 2097151),
        lambda item: item.__setitem__("support_size", 1116047),
        lambda item: item.__setitem__("denominator_degree_cap", 67471),
        lambda item: item.__setitem__("small_owner_max", 1183519),
        lambda item: item.__setitem__("first_large_owner", 1183520),
        lambda item: item.__setitem__("sub_support_owner_cap", 981104),
        lambda item: item.__setitem__("small_owner_record_cap", 2097153),
    )
    caught = 0
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutations")
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    checked = validate(data)
    if args.tamper_selftest:
        print(f"POLE_SIMPLE_SMALL_OWNER_PAYMENT_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "POLE_SIMPLE_SMALL_OWNER_PAYMENT_PASS "
        f"small_owner={checked['small_owner']} record_cap={checked['record_cap']}"
    )


if __name__ == "__main__":
    main()
