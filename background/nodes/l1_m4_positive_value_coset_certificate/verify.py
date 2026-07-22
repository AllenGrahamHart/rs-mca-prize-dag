#!/usr/bin/env python3
"""Verify the 16-case value-coset certificate and DAG wiring."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_positive_value_coset_certificate"
SUPPLIERS = {
    "l1_m4_h3_colored_cyclic_equivalence",
    "l1_m4_h3_tangent_radical_exclusion",
}
CONSUMER = "l1_mixed_petal_amplification"


def load_checker():
    path = ROOT / "experiments" / "prize_resolution" / "l1_m4_depressed_value_coset_check.py"
    spec = importlib.util.spec_from_file_location("value_coset_check", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    checks = 0
    checker = load_checker()
    primes = (8191, 131071, 524287, 2147483647)
    expected_counts = {8191: 0, 131071: 0, 524287: 3, 2147483647: 3}
    for p in primes:
        one, minus_one = (1, 0), (-1 % p, 0)
        quarters = (one, minus_one, (0, 1), (0, -1 % p))
        survivors = []
        for epsilon in quarters:
            for eta in quarters:
                outcome = checker.classify(p, epsilon, eta)
                if outcome != "NONE":
                    survivors.append((epsilon, eta, outcome))
        assert len(survivors) == expected_counts[p]
        if survivors:
            assert {(epsilon, eta) for epsilon, eta, _ in survivors} == {
                (one, minus_one), (minus_one, one), (minus_one, minus_one)
            }
            assert all(outcome == "ALL_QUADRATIC_ROOTS"
                       for _epsilon, _eta, outcome in survivors)
            assert p != 5
            checks += 4
        else:
            checks += 1

    # The surviving normalized triple has outer coefficients a=-2, b=1.
    for p in primes[2:]:
        a, b = -2 % p, 1
        assert (pow(a, 3, p) + 8 * b * b) % p == 0
        assert (-4 * pow(a, 3, p) - 27 * b * b) % p == 5 % p
        checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in SUPPLIERS:
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (NODE, CONSUMER, "ev") in edges
    checks += 3

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(VCC3)", "(VCC4)", "(VCC5)", "(VCC6)",
                   "a^3+8b^2=0", "does not exclude"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_POSITIVE_VALUE_COSET_CERTIFICATE_PASS checks={checks}")


if __name__ == "__main__":
    main()
