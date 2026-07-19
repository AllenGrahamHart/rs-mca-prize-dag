#!/usr/bin/env python3
"""Small coverage check for Petal squarefree classification ledgers."""

from __future__ import annotations


def verify_ledger(universe: set[str], charged: dict[str, str], uncharged: dict[str, int], max_uncharged: int) -> None:
    covered = set(charged) | set(uncharged)
    assert covered == universe
    assert set(charged).isdisjoint(uncharged)
    for citation in charged.values():
        assert citation
    for exponent in uncharged.values():
        assert exponent >= 0
    assert len(uncharged) <= max_uncharged


def main() -> None:
    universe = {"k0", "k1", "k2", "k3"}
    charged = {"k0": "paid_tail", "k1": "paid_norm"}
    uncharged = {"k2": 3, "k3": 4}
    verify_ledger(universe, charged, uncharged, max_uncharged=2)
    print("PASS: Petal squarefree classification ledger covers with bounded uncharged classes")


if __name__ == "__main__":
    main()
