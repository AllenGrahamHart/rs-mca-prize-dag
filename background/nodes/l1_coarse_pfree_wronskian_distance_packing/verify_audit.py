#!/usr/bin/env python3
"""Mutation audit for coarse p-free Wronskian distance packing."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_coarse_pfree_wronskian_distance_packing"


def main() -> None:
    checks = 0

    # The F_4 boundary fixture has t=2 at d=2, refuting a mutated t>=3.
    depth = 2
    tail = 2
    assert tail == math.ceil((depth + 2) / 2)
    assert not tail >= math.ceil((depth + 2) / 2) + 1
    checks += 2

    # Dropping the extra order in the Laurent expansion would give the false
    # degree -1 on the same nonzero constant Wronskian.
    assert 2 * tail - depth - 2 == 0
    assert 2 * tail - depth - 3 == -1
    checks += 2

    # Scalar specialization is floor, not ceiling, when d is odd.
    k = 3
    d = 3
    a = k + d
    s = a - math.ceil((d + 2) / 2) + 1
    assert s == (a + k) // 2 == 4
    assert s != math.ceil((a + k) / 2)
    checks += 2

    # The cap lower bound diagnoses the route only; it is not a lower bound
    # on the true maximum fiber. At this small boundary it is attained by the
    # integer floor of the packing ratio.
    n = 8
    a = 6
    k = 2
    s = (a + k) // 2
    cap = math.comb(n, s) // math.comb(a, s)
    assert s == n // 2
    assert cap == 2 ** (n - a)
    checks += 2

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    audit = (ROOT / "background" / "nodes" / NODE / "audit.md").read_text()
    assert "F_4" in statement
    assert "simple zero/pole valuations" in audit
    assert "may be exponentially above" in audit
    assert "bound on any actual fiber" in audit
    assert "stronger tail" in audit
    checks += 5

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["l1_mixed_petal_amplification"]["status"] == "TARGET"
    checks += 2

    print(f"AUDIT_L1_COARSE_PFREE_WRONSKIAN_DISTANCE_PACKING_PASS checks={checks}")


if __name__ == "__main__":
    main()
