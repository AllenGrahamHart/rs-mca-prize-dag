#!/usr/bin/env python3
"""Small fixed-scale injectivity sanity check for E22 staircases."""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

CORE = Path(__file__).resolve().parents[1] / "worst_word_challenger_pricing" / "notes"
sys.path.insert(0, str(CORE))

from e22_core import P, locator, subgroup_domain  # noqa: E402


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
            seen: dict[tuple[int, ...], tuple[tuple[int, ...], tuple[int, ...]]] = {}
            for h in range(1, min(3, len(qs)) + 1):
                for H in itertools.combinations(qs, h):
                    full = {x for z in H for x in f[z]}
                    residual = [x for x in domain if x not in full]
                    for b in range(min(m - 1, 2) + 1):
                        for B in itertools.combinations(residual[: min(len(residual), 8)], b):
                            roots = tuple(sorted(full | set(B)))
                            poly = locator(list(roots), P)
                            params = (tuple(sorted(B)), tuple(sorted(H)))
                            old = seen.setdefault(poly, params)
                            assert old == params, (n, m, old, params)
                            checks += 1
    print(f"fixed-scale staircase injectivity checks passed: {checks}")


if __name__ == "__main__":
    main()
