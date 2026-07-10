#!/usr/bin/env python3
"""g2f_powerset_check: SET-LEVEL test of the G2 closure trichotomy.

Question: does there EXIST any subset S of Z_n (n a 2-power) that is
PERIODIC (c(S) >= 2) yet NOT staircase at any dyadic scale M >= 2
(residual |B_M(S)| < M), i.e. a combinatorial third-class set at all?

Exhaustive over all 2^n subsets for n = 8, 16; 10^6 random subsets at n = 32.
Both LAX (tail-only scales allowed) and STRICT (>= 1 full fiber) readings.
Also: census of FIXED-M leak sets (periodic, non-staircase at that fixed M) -
the Finding-C hybrid shapes - per (n, M, |S|).
"""
from __future__ import annotations

import random
import sys
from collections import Counter

sys.path.insert(0, "/tmp/claude-1000/-home-u2470931-smooth-read-solomin/d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad")
from g2f_lib import dyadic_scales  # noqa: E402


def stab_size_bits(mask: int, n: int) -> int:
    full = (1 << n) - 1
    c = 0
    for a in range(n):
        rot = ((mask << a) | (mask >> (n - a))) & full
        if rot == mask:
            c += 1
    return c


def residual_bits(mask: int, n: int, M: int) -> tuple[int, int]:
    step = n // M
    fullc = 0
    covered = 0
    for r in range(step):
        fm = 0
        for i in range(M):
            fm |= 1 << (r + step * i)
        if mask & fm == fm:
            fullc += 1
            covered += M
    return bin(mask).count("1") - covered, fullc


def scan_n(n: int, masks) -> None:
    scales = dyadic_scales(n)
    third_lax = 0
    third_strict = 0
    aperiodic = 0
    periodic = 0
    leak = Counter()  # (M, |S|) -> count of periodic non-staircase-at-M sets
    checked = 0
    third_examples = []
    for mask in masks:
        if mask == 0:
            continue
        checked += 1
        c = stab_size_bits(mask, n)
        if c == 1:
            aperiodic += 1
            continue
        periodic += 1
        ok_lax = False
        ok_strict = False
        size = bin(mask).count("1")
        for M in scales:
            b, fullc = residual_bits(mask, n, M)
            if b < M:
                ok_lax = True
                if fullc >= 1:
                    ok_strict = True
            else:
                leak[(M, size)] += 1
        if not ok_lax:
            third_lax += 1
            if len(third_examples) < 5:
                third_examples.append(mask)
        if not ok_strict:
            third_strict += 1
    print(f"n={n}: checked={checked} aperiodic={aperiodic} periodic={periodic} "
          f"THIRD_LAX={third_lax} THIRD_STRICT={third_strict}")
    if third_examples:
        print("  THIRD-CLASS EXAMPLES (masks):", third_examples)
    # summarize leak counts by M (total over sizes)
    byM = Counter()
    for (M, size), v in leak.items():
        byM[M] += v
    print(f"  periodic-but-not-staircase-at-FIXED-M counts (leak shapes): "
          f"{dict(sorted(byM.items()))}")


if __name__ == "__main__":
    for n in (8, 16):
        scan_n(n, range(1, 1 << n))
    rng = random.Random(20260710)
    n = 32
    masks = (rng.getrandbits(32) for _ in range(1_000_000))
    scan_n(n, masks)
    # adversarial periodic sample at n=32: unions of 2-fibers (all 2^16),
    # the ONLY place third-class could live
    fibs = [(1 << j) | (1 << (j + 16)) for j in range(16)]
    def fiber_unions():
        for fm in range(1, 1 << 16):
            m = 0
            for j in range(16):
                if fm >> j & 1:
                    m |= fibs[j]
            yield m
    print("n=32 exhaustive over ALL periodic sets (unions of 2-fibers):")
    scan_n(32, fiber_unions())
