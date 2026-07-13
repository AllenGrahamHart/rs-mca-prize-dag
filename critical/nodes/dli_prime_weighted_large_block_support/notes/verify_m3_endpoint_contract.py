#!/usr/bin/env python3
"""Fail-closed static audit of the DLI endpoint-exception contract."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]


def main() -> None:
    contract = (
        ROOT
        / "critical/nodes/dli_prime_weighted_large_block_support/notes"
        / "M3_ENDPOINT_EXCEPTION_COVERAGE.md"
    ).read_text()
    sieve = (
        ROOT
        / "critical/nodes/dli_prime_weighted_large_block_support/notes"
        / "A1_PROD_NORM_SIEVE.md"
    ).read_text()
    source_warning = (
        ROOT / "critical/nodes/dli_prime_weighted_large_block_support/PRO_DLI_CLOSE_5.md"
    ).read_text()
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}

    checks = {
        "dli_stays_target": nodes["dli_prime_weighted_large_block_support"]["status"]
        == "TARGET",
        "universal_scope": "for every official row R" in contract,
        "soundness_implication": "VERIFY_ENDPOINT_EXC(R,pi_R)=ACCEPT  ==>" in contract,
        "binding_endpoint": "W_cen(R) <= 2^121" in contract,
        "coverage_named": "ENDPOINT-EXC-COVERAGE" in contract,
        "completeness_required": "checkable completeness proof" in contract,
        "residual_required": "residual near-peak upper certificate" in contract,
        "engineering_rejected": "PPT/engineering hardness are\nrejected" in contract,
        "density_is_not_individual": "density" in sieve and "Markov" in sieve,
        "source_denies_exhaustive_certificate": (
            "not computationally certifiable at production" in source_warning
        ),
        "no_endpoint_node_wired": "dli_endpoint_exception_coverage" not in nodes,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    print(json.dumps({"status": "PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
