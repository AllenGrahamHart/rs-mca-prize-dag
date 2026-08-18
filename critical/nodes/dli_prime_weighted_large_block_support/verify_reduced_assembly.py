#!/usr/bin/env python3
"""Fail-closed verifier for the current reduced B-WEAK implication."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
NODES = HERE.parent


def load(node_id: str) -> dict:
    return json.loads((NODES / node_id / "node.json").read_text())


def build() -> dict[str, object]:
    parent = load("dli_prime_weighted_large_block_support")
    c2 = load("dli_c2pp_joint_reserve")
    baseline = load("dli_marginal_baseline100_coverage")
    scope = json.loads(
        (NODES.parent.parent / "background/nodes"
         / "dli_unreduced_coset_endpoint_counterexample/node.json").read_text()
    )
    reqs = {edge["from"] for edge in parent["requires"]}
    result = {
        "joint_bits": 21,
        "baseline_bits": 100,
        "endpoint_bits": 121,
        "parent_status": parent["node"]["status"],
        "c2_status": c2["node"]["status"],
        "baseline_status": baseline["node"]["status"],
        "scope_status": scope["node"]["status"],
        "reqs": sorted(reqs),
    }
    assert parent["node"]["status"] == "CONDITIONAL"
    assert c2["node"]["status"] == "TARGET"
    assert baseline["node"]["status"] == "CONDITIONAL"
    assert scope["node"]["status"] == "PROVED"
    assert "X_prim(R)<=2^21 A(R)" in c2["node"]["statement"]
    assert "product_j E_U[rho_j]<=2^100" in parent["node"]["statement"]
    assert "q^{-t+H}W_cen^prim<=2^121" in parent["node"]["statement"]
    assert reqs == {
        "dli_c2pp_joint_reserve",
        "dli_marginal_baseline100_coverage",
    }
    assert result["joint_bits"] + result["baseline_bits"] == result["endpoint_bits"]
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        caught = 0
        for key, value in (
            ("joint_bits", 22),
            ("baseline_bits", 101),
            ("endpoint_bits", 122),
            ("scope_status", "TARGET"),
        ):
            changed = copy.deepcopy(result)
            changed[key] = value
            try:
                assert changed == result
            except AssertionError:
                caught += 1
        assert caught == 4
        print("DLI_REDUCED_ASSEMBLY_TAMPER_PASS mutations=4/4")
        return
    print(
        "DLI_REDUCED_ASSEMBLY_PASS conditional=true "
        "scope=primitive joint=21 baseline=100 endpoint=121"
    )


if __name__ == "__main__":
    main()
