#!/usr/bin/env python3
"""Focused arithmetic replay for the affine-span list compiler."""

from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "upstream_gfv4_affine_span_list_compiler"


def falling(x: int, s: int) -> int:
    out = 1
    for j in range(s):
        out *= x - j
    return out


def rising(x: int, s: int) -> int:
    out = 1
    for j in range(s):
        out *= x + j
    return out


def main() -> None:
    checks = 0
    for n in range(2, 25):
        for k in range(1, n + 1):
            for w in range(n - k + 1):
                for s in range(k + 1):
                    lhs = falling(n - k + s, s) * comb(w + s, s)
                    rhs = rising(w + 1, s) * comb(n - k + s, s)
                    assert lhs == rhs
                    checks += 1

    for n in range(2, 18):
        for k in range(1, n + 1):
            for s in range(1, k + 1):
                for z in range(k - s + 1):
                    for g in range(z + 1):
                        for m in range(k, n + 1):
                            w = m - k
                            b = z - g
                            q = k - s - z
                            left = (m - g) * (n - k + s) - (n - z) * (w + s)
                            right = b * (n - k + s) + q * (n - m)
                            assert left == right and right >= 0
                            checks += 1

    for d in (3, 4, 7, 31, 2**10, 2**20, 2**39):
        n, k, w = 4 * d, 2 * d, d - 1
        assert (n - k + 1) // (w + 1) == 2
        rank_two_num = comb(n - k + 2, 2)
        rank_two_den = comb(w + 2, 2)
        assert rank_two_num // rank_two_den == 4
        checks += 2

    dag = (ROOT / "dag.json").read_text()
    proof = (ROOT / "background" / "nodes" / NODE / "proof.md").read_text()
    assert f'"id": "{NODE}"' in dag
    assert "b(n-K+s)+q(n-m)>=0" in proof
    print(f"UPSTREAM_GFV4_AFFINE_SPAN_LIST_COMPILER_PASS checks={checks}")


if __name__ == "__main__":
    main()
