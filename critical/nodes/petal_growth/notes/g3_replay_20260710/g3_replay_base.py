#!/usr/bin/env python3
"""Fresh verifier, part 1: the four structural nodes of the fifth E22 branch.

Covers (against direct enumeration ground truth):
  - e22_dyadic_minimal_scale_selector   (unique minimal admissible modulus)
  - e22_minimal_scale_tail_criterion    (criterion <=> selected minimum)
  - e22_minimal_scale_partition         (exactly one tail-minimal cell)
  - e22_overlap_nested_fiber_residual_identity (|B_j| = |B_i| + M_i r_{i,j})

Exhaustive for n in {8, 16} (all 2^n supports), sampled for n = 32.
"""

from __future__ import annotations

import random
import sys

sys.path.insert(0, "/tmp/claude-1000/-home-u2470931-smooth-read-solomin/d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad")
from g3_lib import (
    admissible,
    admissible_set,
    eligible_scales,
    minimal_scale,
    residual_stats,
    tail_criterion,
    tail_size,
)

MUTATE = "--mutate" in sys.argv  # negative control: deliberately break the criterion


def check_mask(n: int, t: int, mask: int) -> None:
    elig = eligible_scales(n, t)
    a = admissible_set(n, t, mask)
    # selector: nonempty (top scale n always admissible for t < n) and unique min
    assert a, (n, t, mask)
    mmin = min(a)
    assert a == sorted(a) and len(set(a)) == len(a)
    # tail criterion == "is the selected minimum", for every eligible scale
    for M in elig:
        crit = tail_criterion(n, t, mask, M)
        if MUTATE:
            crit = admissible(n, M, mask)  # broken criterion: raw admissibility
        assert crit == (M == mmin), (n, t, mask, M, crit, mmin)
    # partition: exactly one tail-minimal cell
    cells = [M for M in elig if tail_criterion(n, t, mask, M)]
    assert cells == [mmin], (n, t, mask, cells)
    # nested-fiber residual identity, all eligible pairs, unconditional in R
    for i, Mi in enumerate(elig):
        for Mj in elig[i + 1:]:
            c, r, b = residual_stats(n, Mi, Mj, mask)
            assert tail_size(n, Mj, mask) == b + Mi * r, (n, Mi, Mj, mask)


def main() -> None:
    for n, ts in ((8, (1, 2, 3)), (16, (1, 2, 3, 5))):
        for t in ts:
            for mask in range(1 << n):
                check_mask(n, t, mask)
            print(f"PASS base nodes: n={n} t={t} exhaustive ({1 << n} supports)")
    rng = random.Random(20260710)
    n = 32
    for t in (1, 3):
        for _ in range(20000):
            check_mask(n, t, rng.getrandbits(n))
        print(f"PASS base nodes: n={n} t={t} sampled (20000 supports)")
    print("ALL PASS: selector, tail criterion, partition, nested-fiber identity")


if __name__ == "__main__":
    main()
