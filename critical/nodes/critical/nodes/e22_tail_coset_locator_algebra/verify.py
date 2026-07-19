#!/usr/bin/env python3
"""Small sanity verifier for e22_tail_coset_locator_algebra.

The proof is symbolic; this script checks representative subgroup rows in
F_193 using the same polynomial routines as the E22 local model.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

CORE = Path(__file__).resolve().parents[1] / "worst_word_challenger_pricing" / "notes"
sys.path.insert(0, str(CORE))

from e22_core import P, locator, poly_mul, subgroup_domain, trim  # noqa: E402


def compose_xm(poly: tuple[int, ...], m: int) -> tuple[int, ...]:
    out = [0] * ((len(poly) - 1) * m + 1)
    for i, coeff in enumerate(poly):
        out[i * m] = coeff
    return trim(out, P)


def top_subleading(poly: tuple[int, ...], t: int) -> tuple[int, ...]:
    d = len(poly) - 1
    return tuple(poly[d - i] if d - i >= 0 else 0 for i in range(1, t + 1))


def fibers(domain: list[int], m: int) -> dict[int, list[int]]:
    out: dict[int, list[int]] = {}
    for x in domain:
        out.setdefault(pow(x, m, P), []).append(x)
    return out


def main() -> None:
    checks = 0
    for n in (16, 32):
        domain = subgroup_domain(n, P)
        for m in (d for d in range(2, n + 1) if n % d == 0):
            f = fibers(domain, m)
            qs = sorted(f)
            if len(qs) < 3:
                continue
            tail_q = qs[0]
            candidates = qs[1:]
            for b in range(min(m - 1, 3) + 1):
                B = f[tail_q][:b]
                LB = locator(B, P)
                for h in range(1, min(3, len(candidates)) + 1):
                    signatures = set()
                    for H in itertools.combinations(candidates, h):
                        roots = list(B)
                        for z in H:
                            roots.extend(f[z])
                        direct = locator(roots, P)
                        G = locator(list(H), P)
                        staircase = poly_mul(LB, compose_xm(G, m), P)
                        assert direct == staircase, (n, m, b, h, H)
                        signatures.add(top_subleading(staircase, m - 1))
                        checks += 1
                    assert len(signatures) == 1, (n, m, b, h)
    print(f"tail-coset locator checks passed: {checks}")


if __name__ == "__main__":
    main()
