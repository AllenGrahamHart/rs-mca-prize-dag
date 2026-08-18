#!/usr/bin/env python3
"""Verify the scalar-dimension-three common-core shortening."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "67fc4bda1f106e0701e6801e4f654330d66dec03181a4a2374d57c5d80bb2b9a"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-pair-pencil-dimension-three-common-core-shortening-v1",
        "schema",
    )
    n, m, K = data.get("n"), data.get("m"), data.get("K")
    q = data.get("selected_types")
    s = data.get("pair_core_size")
    line = data.get("affine_line_cap")
    require((n, m, K, q, s, line) == (2097152, 1116048, 1048576, 520, m - 2, 15), "pins")
    plane = line * (n - (K - 1)) // (s - (K - 1))
    require(data.get("affine_plane_cap") == plane == 233, "plane cap")
    core = math.ceil((q * s - plane * n) / (q - plane))
    require(data.get("common_core_floor") == core == 319539, "core floor")
    n1, K1, m1, s1 = n - core, K - core, m - core, s - core
    require(data.get("shortened_n_at_floor") == n1 == 1777613, "n1")
    require(data.get("shortened_K_at_floor") == K1 == 729037, "K1")
    require(data.get("shortened_m_at_floor") == m1 == 796509, "m1")
    require(data.get("shortened_pair_core_at_floor") == s1 == 796507, "s1")
    slack = plane * n1 - q * s1
    require(data.get("incidence_slack_at_floor") == slack == 189, "slack")
    require(data.get("preserved_excess") == m1 - K1 == 67472, "excess")
    require("not paid" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_pair_pencil_dimension_two_incidence_exclusion",
        "rate_half_mca_rank11_pair_pencil_dimension_two_common_core_shortening",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"plane": plane, "core": core, "slack": slack}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("n", 2097151),
        lambda item: item.__setitem__("selected_types", 519),
        lambda item: item.__setitem__("affine_line_cap", 16),
        lambda item: item.__setitem__("affine_plane_cap", 234),
        lambda item: item.__setitem__("common_core_floor", 319538),
        lambda item: item.__setitem__("shortened_K_at_floor", 729038),
        lambda item: item.__setitem__("incidence_slack_at_floor", 188),
        lambda item: item.__setitem__("preserved_excess", 67471),
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
        print(f"PAIR_PENCIL_DIM3_COMMON_CORE_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "PAIR_PENCIL_DIM3_COMMON_CORE_PASS "
        f"plane={checked['plane']} core={checked['core']} slack={checked['slack']}"
    )


if __name__ == "__main__":
    main()
