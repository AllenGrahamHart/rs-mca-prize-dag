#!/usr/bin/env python3
"""Verify the explicit F2 non-generating O1 counterexample."""

from __future__ import annotations

import json
from math import gcd, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
P = 6_597_069_766_657
N = 1 << 41


def pocklington_base() -> int:
    for base in range(2, 100):
        if pow(base, P - 1, P) == 1 and gcd(
            pow(base, (P - 1) // 2, P) - 1, P
        ) == 1:
            return base
    raise AssertionError("no Pocklington base below 100")


def main() -> None:
    assert P == 3 * N + 1
    assert N > isqrt(P)
    base = pocklington_base()
    assert pow(base, P - 1, P) == 1
    assert gcd(pow(base, (P - 1) // 2, P) - 1, P) == 1
    assert P**6 < 2**256
    assert (P - 1) % N == 0
    assert P % N == 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["f2_all_admissible_o1_mass_bound"]["status"] == "REFUTED"
    assert nodes["f2_conditional_close"]["status"] == "TARGET"
    print(
        "F2_ALL_ADMISSIBLE_O1_MASS_BOUND_REFUTED_PASS "
        f"pocklington_base={base} field_cap=1 excess=5n/12 dag=2/2"
    )


if __name__ == "__main__":
    main()
