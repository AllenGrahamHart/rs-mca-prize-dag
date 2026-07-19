#!/usr/bin/env python3
"""Independent audit of the exceptional-only infinity chain."""

from __future__ import annotations

from pathlib import Path
from random import Random


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_infinity_coefficient_rigidity"


def randomized_chain() -> None:
    p = 1013
    rng = Random(20260720)
    for _ in range(64):
        exceptional = rng.randrange(1, p)
        q_bar = rng.randrange(1, p)
        j_inf = rng.randrange(1, p)
        v_inf = rng.randrange(0, p)
        p_cl = rng.randrange(1, p)
        q_inf = exceptional * q_bar % p
        a_inf = p_cl * j_inf % p
        b_inf = -j_inf * q_bar % p
        w_inf = -exceptional * q_bar * v_inf % p
        k_inf = j_inf * q_bar * v_inf % p
        product = p_cl * exceptional % p
        assert (q_inf * a_inf + product * b_inf) % p == 0
        assert (q_inf * v_inf + w_inf) % p == 0
        assert (w_inf * b_inf - q_inf * k_inf) % p == 0

        wrong_k = -k_inf % p
        if k_inf:
            assert (w_inf * b_inf - q_inf * wrong_k) % p != 0


def scope_check() -> None:
    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    contract = (here / "claim_contract.md").read_text()
    audit = (here / "audit.md").read_text()
    assert "If it vanishes" in statement
    assert "no exact degree claim for" in contract
    assert "coverage" in audit and "failure" in audit


def main() -> None:
    randomized_chain()
    scope_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_INFINITY_RIGIDITY_AUDIT_PASS "
        "fixtures=64 mutation=sign zero_v=allowed"
    )


if __name__ == "__main__":
    main()
