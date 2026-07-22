#!/usr/bin/env python3
"""Mutation audit for the official-reserve tame-refinement router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_reserve_tame_refinement_router"


def main() -> None:
    checks = 0

    # A larger field cap admits the characteristic-three boundary fixture;
    # its canonical upper bound is not below p.
    n = 1 << 13
    p = 3
    f = n // 4
    assert p**f < 1 << 4096
    log_floor = (p**f).bit_length() - 1
    trial = (5 * n + 4 * log_floor - 1) // (4 * log_floor)
    assert trial + 1 >= p
    checks += 2

    # Without eta<=1/4, a large epsilon destroys the p-independent cutoff.
    assert 5 * (7 + 1) <= 4 * (7 - 2) * 3
    assert 101 * (7 + 1) > (7 - 2) * 3
    checks += 2

    # A noncanonical larger threshold need not have petal size below p.
    assert n // 2 + 1 > p
    checks += 1

    # ell<=p is insufficient: s=1 leaves the wild outer degree r=p.
    ell = p
    refinement_degree = 1
    assert (ell // refinement_degree) % p == 0
    checks += 1

    # Ambient-field normalization is forbidden by the claim contract.
    contract = (ROOT / "background" / "nodes" / NODE / "claim_contract.md").read_text()
    assert "generated field `F_(p^f)`, not an unrelated ambient field" in contract
    checks += 1

    audit = (ROOT / "background" / "nodes" / NODE / "audit.md").read_text()
    for anchor in (
        "n|p^f-1",
        "strict conclusion is `ell_0<p`",
        "Only fixed-petal map supply is removed",
        "No computation or probabilistic evidence is load-bearing",
    ):
        assert anchor in audit
        checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["l1_mixed_petal_amplification"]["status"] == "TARGET"
    checks += 2

    print(f"AUDIT_L1_OFFICIAL_RESERVE_TAME_REFINEMENT_ROUTER_PASS checks={checks}")


if __name__ == "__main__":
    main()
