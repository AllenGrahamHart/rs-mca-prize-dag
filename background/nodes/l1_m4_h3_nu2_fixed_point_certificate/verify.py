#!/usr/bin/env python3
"""Verify the nu=2 fixed-point certificate and DAG wiring."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_nu2_fixed_point_certificate"
SUPPLIER = "l1_m4_h3_nu2_base_field_normalization"
CONSUMER = "l1_mixed_petal_amplification"


def multiplicative_order(a: int, modulus: int) -> int:
    value = 1
    for order in range(1, 5):
        value = value * a % modulus
        if value == 1:
            return order
    raise AssertionError("order exceeds four")


def main() -> None:
    checks = 0
    for p in (524287, 2147483647):
        r = (p + 1).bit_length() - 1
        assert p + 1 == 1 << r
        n = 4 * (p + 1)
        assert multiplicative_order(p, n) == 4
        assert math.gcd(n, p - 1) == 2
        checks += 3

    # Check the compressed sign equation against direct product evaluation
    # on every pairwise-distinct passport at two small Mersenne analogues.
    for p in (7, 31):
        for e1 in range(1, p):
            for e2 in range(1, p - e1):
                e3 = p - e1 - e2
                if e3 <= 0 or len({e1, e2, e3}) < 3:
                    continue
                ds = ((e2 - e3) % p, (e3 - e1) % p, (e1 - e2) % p)
                w = 1
                for d, e in zip(ds, (e1, e2, e3)):
                    assert d
                    w = w * pow(d, e, p) % p
                c = 4 * pow(3 * w, -1, p) % p
                s0 = -pow(w, -1, p) % p
                for epsilon in (1, -1):
                    x = epsilon * c % p
                    sx = 1
                    compressed = 1
                    for d, e in zip(ds, (e1, e2, e3)):
                        sx = sx * pow((x - pow(d, -1, p)) % p, e, p) % p
                        compressed = compressed * pow(
                            (3 * w - 4 * epsilon * d) % p, e, p
                        ) % p
                    direct_pass = (sx - s0 - c) % p == 0
                    compressed_pass = (compressed + w) % p == 0
                    assert direct_pass == compressed_pass
                    checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (SUPPLIER, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    checks += 5

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(FPC2)", "(FPC3)", "(FPC4)", "(FPC6)", "A=c^n",
                   "F_e(W)^3-2F_e(W)+1",
                   "necessary certificate"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_NU2_FIXED_POINT_CERTIFICATE_PASS checks={checks}")


if __name__ == "__main__":
    main()
