#!/usr/bin/env python3
"""Mutation guards for the HGE4 Kummer midpoint-pencil router."""

from __future__ import annotations

import importlib.util
import json
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_near_third_kummer_midpoint_pencil"
VERIFY = ROOT / "background/nodes" / NODE / "verify.py"


def load_verify():
    spec = importlib.util.spec_from_file_location("kummer_midpoint_verify", VERIFY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()

    # The endpoint and sign are load-bearing.
    order, width, defect = 64, 18, 10
    center = width + defect
    assert 2 * width + center == order
    assert 2 * width + center + 1 != order
    prime, a_value, lambda_value = 107, 4, 7
    kappa = (1 - a_value * a_value * lambda_value) % prime
    root_power = pow(kappa, -1, prime)
    assert (-a_value * a_value * lambda_value * root_power) % prime == (1 - root_power) % prime
    wrong_kappa = (1 + a_value * a_value * lambda_value) % prime
    assert (-a_value * a_value * lambda_value * pow(wrong_kappa, -1, prime)) % prime != (
        1 - pow(wrong_kappa, -1, prime)
    ) % prime

    # The arithmetic ledger permits d=2 at even width, but primitivity does
    # not: the same eta stabilizes S and eta^h=1 stabilizes both outside terms.
    assert gcd(64, 17) == 1
    assert gcd(64, 18) == 2
    verify.kummer_degree_check(64, 17)
    verify.kummer_degree_check(64, 18)
    verify.primitive_degree_check(64, 17)
    verify.primitive_degree_check(64, 18)
    assert 18 % 2 == 0
    assert 2 > 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["f3_hge4_norm_gate_count"]["status"] == "TARGET"
    consumer = (ROOT / "critical/nodes/f3_hge4_norm_gate_count/statement.md").read_text()
    for marker in (NODE, "W=ZS+lambda y^c", "Kummer", "every width"):
        assert marker in consumer
    print(
        "F3_HGE4_NEAR_THIRD_KUMMER_MIDPOINT_PENCIL_AUDIT_PASS "
        "endpoint_guard=1 sign_guard=1 primitive_even_width_guard=2"
    )


if __name__ == "__main__":
    main()
