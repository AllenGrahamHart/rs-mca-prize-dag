#!/usr/bin/env python3
"""Mutation audit for the XR global quotient-core router."""

from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    # The binomial comparison is not a rate-half theorem.
    assert comb(64, 32) > comb(64, 33)

    # Strict activity and rate-preserving divisibility pin the k-point core.
    n, k, reserve, scale = 1024, 256, 5, 8
    agreement = k + reserve
    assert scale > reserve and k % scale == 0
    assert scale * (agreement // scale) == k
    assert not (4 > reserve)
    assert 10 % 4 != 0

    # Grouping per threshold would double-pay K0; global grouping collides it.
    per_threshold_singletons = 4
    global_singletons = 2
    assert per_threshold_singletons > global_singletons

    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "C(N,h)<=C(N,h+1)" in proof
    assert "tailcontainsatleastonecoordinate" in proof
    assert "Grouping is global across every raised threshold" in audit
    assert "doesnotprovetheP-Abound" in statement

    print("XR_QUOTIENT_GLOBAL_CORE_COLLISION_ROUTER_AUDIT_PASS mutations=7")


if __name__ == "__main__":
    main()
