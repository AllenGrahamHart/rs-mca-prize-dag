#!/usr/bin/env python3
"""Verify the atom-weld gauge dichotomy contract and finite controls."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "c977c422ea2be541bc0475a7b215ba311e45f0ad8e92cfa79dd162a3987a6120"
PRIME = 101


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def determinant(left: tuple[int, int], middle: tuple[int, int], right: tuple[int, int]) -> int:
    a0, b0 = left
    a1, b1 = middle
    a2, b2 = right
    return ((a1 - a0) * (b2 - b0) - (a2 - a0) * (b1 - b0)) % PRIME


def finite_controls() -> int:
    controls = 0
    generic = [(0, 0), (1, 0), (0, 1), (2, 3), (7, 9)]
    require(determinant(*generic[:3]) != 0, "generic basis")
    for s in generic[3:]:
        require(determinant(generic[0], generic[2], s) != 0 or determinant(generic[1], generic[2], s) != 0, "vertex propagation")
        controls += 1
    for s, t in itertools.combinations(generic, 2):
        require(any(determinant(x, s, t) != 0 for x in generic[:3] if x not in (s, t)), "edge propagation")
        controls += 1
    pencil = [(x, (3 * x + 4) % PRIME) for x in range(9)]
    require(all(determinant(*triple) == 0 for triple in itertools.combinations(pencil, 3)), "rank-two pencil")
    controls += 84
    return controls


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-cross-type-atom-weld-gauge-dichotomy-v1",
        "schema",
    )
    require(data.get("canonical_anchor_records") == 18, "anchor")
    require(data.get("shared_locator_points_for_projective_identity") == 3, "projective points")
    require(data.get("pair_type_vector") == "(1,a_p,b_p)", "pair vector")
    require(data.get("edge_gauge") == "C_pq-C_pr=D_p(1,a_p,b_p)", "gauge")
    require(data.get("triangle_cocycle") == "D_q T_q=D_p T_p+D_r T_r", "cocycle")
    require(data.get("generic_output") == "one globally identical normalized edge atom", "generic")
    require(data.get("degenerate_output") == "pair-type rank at most two over F(X)", "degenerate")
    require("not yet extended" in str(data.get("nonclaim")).lower(), "nonclaim")
    controls = finite_controls()

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_cross_type_degree18_atom_weld_compiler",
        "rate_half_mca_rank11_multi_anchor_exchange_split_pencil_synchronization",
        "rate_half_mca_rank11_heavy_ruling_exception_split_pencil_normal_form",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"controls": controls}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("canonical_anchor_records", 17),
        lambda item: item.__setitem__("shared_locator_points_for_projective_identity", 2),
        lambda item: item.__setitem__("pair_type_vector", "(a_p,b_p)"),
        lambda item: item.__setitem__("edge_gauge", "C_pq-C_pr=D_p"),
        lambda item: item.__setitem__("triangle_cocycle", "D_q T_q=D_p T_p-D_r T_r"),
        lambda item: item.__setitem__("generic_output", "one atom per triangle"),
        lambda item: item.__setitem__("degenerate_output", "pair-type rank at most three over F(X)"),
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
        print(f"CROSS_TYPE_ATOM_WELD_GAUGE_TAMPER_PASS mutations={tamper_selftest(data)}/7")
        return
    print(f"CROSS_TYPE_ATOM_WELD_GAUGE_PASS controls={checked['controls']}")


if __name__ == "__main__":
    main()
