#!/usr/bin/env python3
"""Mutation audit for the Mersenne checkpoint chamber formula."""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("primary", HERE / "verify.py")
primary = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(primary)


def mutated(m: int, nbase: int, mode: str) -> set[int]:
    out = set()
    for q in range(m):
        for b in range(nbase):
            if b == 0:
                hit = q == (1 if mode == "move_zero" else 0)
            else:
                g = __import__("math").gcd(2 * b, m)
                second = b + 1 if mode == "plus_one" else b - 1
                hit = q % g == 0
                if mode != "drop_second":
                    hit = hit or (q - second) % g == 0
            if hit:
                out.add(q * nbase + b)
    return out


def main() -> None:
    caught = 0
    for mode in ("move_zero", "plus_one", "drop_second"):
        bad = mutated(8, 32, mode)
        good = primary.direct_closure(8 * 32, 31)
        assert bad != good
        caught += 1

    statement = (HERE / "statement.md").read_text()
    assert "evidence only" in statement
    assert "does not" in statement and "close L1" in statement
    caught += 2
    print(f"L1_MERSENNE_CHECKPOINT_CYCLOTOMIC_NORMAL_FORM_AUDIT_PASS checks={caught}")


if __name__ == "__main__":
    main()
