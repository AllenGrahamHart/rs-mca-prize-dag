#!/usr/bin/env python3
"""Verify the KoalaBear v4 tangent-source atom and frozen partition."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_kb_v4_tangent_source_atom"
SOURCE = "rate_half_mca_sparse_layer_reduction"
CONSUMER = "rate_half_band_closure"
ARCH = "GRANDE_FINALE_V4_KB_MCA_TANGENT_SOURCE_ADAPTER_V1"
DIGEST = "4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc"
P = 2_130_706_433
N = 2_097_152
A = 1_116_048
B_STAR = 274_980_728_111_395_087
U_PAID = 981_104
RESERVE = 274_980_728_110_413_983


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def canonical(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def cells(
    bad: set[int], tangent: set[int], q_set: set[int], bc_set: set[int]
) -> tuple[set[int], set[int], set[int], set[int]]:
    paid = bad & tangent
    residual_1 = bad - paid
    q_cell = residual_1 & q_set
    residual_2 = residual_1 - q_cell
    bc_cell = residual_2 & bc_set
    return paid, q_cell, bc_cell, residual_2 - bc_cell


def main() -> None:
    contract_path = Path(__file__).with_name("partition_contract.json")
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    body = copy.deepcopy(contract)
    claimed = body.pop("partition_sha256")
    method = body.pop("partition_digest_method")
    actual = hashlib.sha256(canonical(body)).hexdigest()
    require(contract["architecture_id"] == ARCH, "architecture")
    require(
        method == "SHA256_CANONICAL_JSON_WITHOUT_PARTITION_SHA256_AND_METHOD",
        "digest method",
    )
    require(claimed == actual == DIGEST, "partition digest")
    require(
        contract["atom_order"] == ["U_paid", "U_Q", "U_BC", "U_new"],
        "atom order",
    )
    require(contract["residual_rule"] == "ITERATED_EXACT_SET_DIFFERENCE", "rule")
    require(contract["unresolved_cells"] == [
        "ACTIVE_V4_BOUNDARY_PREFIX_Q",
        "ACTIVE_V4_BALANCED_CORE",
        "UNPAID_V4_COMPLEMENT",
    ], "unpaid cells")

    require(N - A == U_PAID, "source support charge")
    require((P**6) // (2**128) == B_STAR, "field budget")
    require(B_STAR - U_PAID == RESERVE, "remaining reserve")

    incoming = {0, 1, 2, 3, 4, 5, 6}
    parts = cells(incoming, {1, 2, 8}, {2, 3, 4, 9}, {4, 5, 10})
    require(parts == ({1, 2}, {3, 4}, {5}, {0, 6}), "fixture cells")
    require(set().union(*parts) == incoming, "fixture exhaustion")
    require(all(
        left.isdisjoint(right)
        for index, left in enumerate(parts)
        for right in parts[index + 1:]
    ), "fixture disjointness")

    dag = json.loads((ROOT / "dag.json").read_text(encoding="utf-8"))
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    require(nodes[NODE]["status"] == "PROVED", "DAG status")
    require((SOURCE, NODE, "req") in edges, "required source edge")
    require((NODE, CONSUMER, "ev") in edges, "evidence consumer edge")

    print(
        "RATE_HALF_KB_V4_TANGENT_SOURCE_ATOM_PASS "
        f"U_paid={U_PAID} reserve={RESERVE} partition={DIGEST}"
    )


if __name__ == "__main__":
    main()
