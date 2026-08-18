#!/usr/bin/env python3
"""Verify global-atom one-record extension packet arithmetic."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "7d899ce39d8cdb167353728a6ac3511de2fa10d1bea0a3bb712d1f7093cdd42f"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-cross-type-global-atom-record-extension-v1",
        "schema",
    )
    size = data.get("packet_size")
    anchor = data.get("anchor_records_after_replacement")
    shared = data.get("shared_records")
    shared_anchor = data.get("shared_anchor_type_records")
    counterpart = data.get("minimum_shared_counterpart_records")
    threshold = data.get("atom_identity_threshold")
    require((size, anchor, shared, shared_anchor) == (32, 18, 31, 17), "packet pins")
    require(shared == size - 1, "one replacement")
    require(shared_anchor == anchor - 1, "anchor overlap")
    require(counterpart == 5, "counterpart")
    require(shared >= threshold == 16, "identity threshold")
    require(shared_anchor >= 3 and counterpart >= 3, "two-type multiplicity")
    require(data.get("high_complexity_floor") == 2299571, "complexity")
    require(data.get("output") == "one atom certifies every large-type record", "output")
    require("not yet bounded" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_cross_type_atom_weld_gauge_dichotomy",
        "rate_half_mca_rank11_cross_type_degree18_atom_weld_compiler",
        "rate_half_mca_rank11_cross_type_pole_simple_atom_identity",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"shared": shared, "anchor": shared_anchor, "counterpart": counterpart}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("packet_size", 31),
        lambda item: item.__setitem__("anchor_records_after_replacement", 17),
        lambda item: item.__setitem__("shared_records", 30),
        lambda item: item.__setitem__("shared_anchor_type_records", 16),
        lambda item: item.__setitem__("minimum_shared_counterpart_records", 4),
        lambda item: item.__setitem__("atom_identity_threshold", 17),
        lambda item: item.__setitem__("high_complexity_floor", 2299570),
        lambda item: item.__setitem__("output", "one atom per pair type"),
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
        print(f"CROSS_TYPE_GLOBAL_ATOM_EXTENSION_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "CROSS_TYPE_GLOBAL_ATOM_EXTENSION_PASS "
        f"shared={checked['shared']} types={checked['anchor']}+{checked['counterpart']}"
    )


if __name__ == "__main__":
    main()
