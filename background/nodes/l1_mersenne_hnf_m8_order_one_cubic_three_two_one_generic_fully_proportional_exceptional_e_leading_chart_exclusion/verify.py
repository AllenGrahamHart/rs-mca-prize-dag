#!/usr/bin/env python3
"""Reconstruct the exact exceptional-E leading-chart contradiction."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_leading_chart_exclusion"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_quadratic_router"
CONSUMER = "l1_mixed_petal_amplification"
PRIMES = (8191, 131071, 524287, 2147483647)
EXPECTED = (6740, 100974, 284891, 1825899718)


def arithmetic_check() -> None:
    z = F(1575, 247)
    s = z + 27
    q = -F(10, 231) * s
    c_b = -720 * q**2 - 1902 * q - 40 * s
    c_0 = 240 * z * q + 240 * z - 630 * q

    assert s == F(8244, 247)
    assert c_b == -F(8244 * 3950060, 61009 * 5929)
    assert c_0 == F(3233714400, 61009 * 231)

    forced_b = -c_0 / c_b
    numerator = 115275930
    denominator = 45228187
    assert forced_b == F(numerator, denominator)
    assert denominator == 229 * 197503

    obstruction = 247 * numerator**2 - 1575 * denominator**2
    assert numerator**2 == 13288540037364900
    assert denominator**2 == 2045588899306969
    assert obstruction == 60466872820654125
    assert tuple(obstruction % p for p in PRIMES) == EXPECTED
    assert all(value != 0 for value in EXPECTED)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "lineage.md",
        "upstream_crosswalk.md",
        "verify.py",
        "verify_audit.py",
    }
    refs = set(nodes[NODE]["refs"])
    assert {str((base / name).relative_to(ROOT)) for name in required} <= refs
    packet = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in ("(FEL3)", "115275930/45228187", "60466872820654125", "1825899718"):
        assert marker in packet


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_321_EXCEPTIONAL_E_LEADING_CHART_EXCLUSION_PASS "
        "primes=4 obstruction=60466872820654125"
    )


if __name__ == "__main__":
    main()
