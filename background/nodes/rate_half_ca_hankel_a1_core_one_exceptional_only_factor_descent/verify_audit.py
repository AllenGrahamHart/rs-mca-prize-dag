#!/usr/bin/env python3
"""Independent audit of the exceptional-only descent identities."""

from __future__ import annotations

from pathlib import Path
from random import Random


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_factor_descent"


def randomized_identity_audit() -> None:
    p = 1009
    rng = Random(20260719)
    for _ in range(64):
        q = rng.randrange(1, p)
        exceptional = rng.randrange(1, p)
        w = rng.randrange(1, p)
        b_1 = rng.randrange(1, p)
        j = rng.randrange(1, p)
        p_cl = rng.randrange(1, p)
        p_x = rng.randrange(1, p)
        inv_q = pow(q, -1, p)

        k_1 = (w * b_1 - 1) * inv_q % p
        a_1 = (p_x - p_cl * exceptional * b_1) * inv_q % p
        b = (q * j + exceptional * b_1) % p
        a = (a_1 - p_cl * j) % p
        k = (w * j + exceptional * k_1) % p
        product = p_cl * exceptional % p
        v = (product - p_x * w) * inv_q % p

        assert (q * a + p_cl * b) % p == p_x
        assert (w * b - exceptional) % p == q * k % p
        assert (q * a_1 + product * b_1) % p == p_x
        assert (w * b_1 - 1) % p == q * k_1 % p
        assert (v * b_1 + a_1 + p_x * k_1) % p == 0

        mutated_k = (w * j - exceptional * k_1) % p
        if k_1:
            assert (w * b - exceptional) % p != q * mutated_k % p


def scope_audit() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "c=z=1" in statement
    assert "one-degree relaxation" in statement
    assert "no exclusion of the exceptional-only profile" in contract
    assert "not asserted on the" in audit and "`c=2` profile" in audit


def main() -> None:
    randomized_identity_audit()
    scope_audit()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_FACTOR_DESCENT_AUDIT_PASS "
        "fixtures=64 mutation=sign scope=guarded"
    )


if __name__ == "__main__":
    main()
