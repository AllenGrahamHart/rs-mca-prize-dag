#!/usr/bin/env python3
"""Focused arithmetic replay for the fixed-union compilers."""

from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "upstream_gfv4_fixed_union_johnson"


def main() -> None:
    checks = 0
    for r in range(2, 30):
        for nu in range(1, 8):
            n = r + nu
            for t in range(r):
                h = n - t
                assert h - (nu + 1) + 1 == r - t
                ray = comb(n, nu + 1) // (r - t)
                assert ray >= 1
                if nu == 1:
                    assert ray == (r * (r + 1)) // (2 * (r - t))
                denom = h * h - n * (nu - 1)
                if denom > 0:
                    johnson = n * (h - nu + 1) // denom
                    assert johnson >= 1
                checks += 1

    dag = (ROOT / "dag.json").read_text()
    proof = (ROOT / "background" / "nodes" / NODE / "proof.md").read_text()
    assert f'"id": "{NODE}"' in dag
    assert "L(h^2-N(nu-1))<=N(h-nu+1)" in proof
    print(f"UPSTREAM_GFV4_FIXED_UNION_JOHNSON_PASS checks={checks}")


if __name__ == "__main__":
    main()
