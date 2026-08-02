#!/usr/bin/env python3
"""Covering-number scaling of the carry sumset up to p ~ 10^6.

Run:  tools/ramguard local -- python3 \
        notes/pilots_20260802/f2_carry_reachability/scaling.py

Uses the norm-one torus mu_{p+1} <= F_{p^2}^* (which needs only the
factorisation of p+1) and measures k_full = min{ k : S_k = Z/2p }.
All arithmetic exact.
"""

from __future__ import annotations

import json
import math
import os
import random
import statistics
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from f2model import Fp2, factorize, is_prime, rot  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results")


def torus_generator(F: Fp2, rng: random.Random) -> tuple[int, int]:
    """A generator of mu_{p+1} = ker(Norm) <= F_{p^2}^*."""
    p = F.p
    facs = list(factorize(p + 1))
    for _ in range(500):
        z = (rng.randrange(p), rng.randrange(p))
        if z == (0, 0):
            continue
        x = F.mul(F.frob(z), F.pow(z, p * p - 2))  # z^{p-1}
        if x == (1, 0):
            continue
        if all(F.pow(x, (p + 1) // q) != (1, 0) for q in facs):
            return x
    raise RuntimeError("no torus generator")


def pairs_from_torus(F: Fp2, g: tuple[int, int], want: int):
    p = F.p
    half = (p - 1) // 2
    out = []
    cur = (1, 0)
    seen = set()
    for _ in range(4 * want + 64):
        cur = F.mul(cur, g)
        if cur[1] == 0:
            continue
        rep = cur if 1 <= cur[1] <= half else F.frob(cur)
        if rep in seen:
            continue
        seen.add(rep)
        out.append(rep)
        if len(out) >= want:
            break
    return out


def k_full_for(F: Fp2, c, reps) -> tuple[int | None, list[int]]:
    p = F.p
    two_p = 2 * p
    full = (1 << two_p) - 1
    S = 1
    sizes = [1]
    for y in reps:
        ac, bc = c
        ay, by = y
        sp = (2 * (ac * ay + F.N * bc * by)) % p
        sm = (2 * (ac * ay - F.N * bc * by)) % p
        d = (sp - sm) % two_p
        S |= rot(S, d, two_p, full)
        sz = S.bit_count()
        sizes.append(sz)
        if sz == two_p:
            return len(sizes) - 1, sizes
    return None, sizes


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    ps = [251, 509, 1021, 2039, 4093, 8191, 16381, 32749, 65521,
          131071, 262139, 524287, 1048573]
    ps = [p for p in ps if is_prime(p)]
    rows = []
    print(f"{'p':>9} {'2p':>9} {'log2(2p)':>9} {'k_full med':>11}"
          f" {'excess':>8} {'ratio':>7}")
    for p in ps:
        F = Fp2.make(p)
        rng = random.Random(9000 + p)
        g = torus_generator(F, rng)
        want = 4 * int(math.log2(2 * p)) + 24
        reps = pairs_from_torus(F, g, want)
        ks = []
        for trial in range(8):
            if trial == 0:
                c = (0, 1)                       # trace-zero line
            elif trial == 1:
                c = (1, 1)
            else:
                c = (rng.randrange(1, p), rng.randrange(1, p))
            order = list(reps)
            random.Random(trial * 7 + p).shuffle(order)
            k, _ = k_full_for(F, c, order)
            if k is not None:
                ks.append(k)
        med = statistics.median(ks)
        lg = math.log2(2 * p)
        rows.append({"p": p, "two_p": 2 * p, "log2_2p": lg,
                     "k_full_all": ks, "k_full_median": med,
                     "excess": med - lg, "ratio": med / lg,
                     "pairs_available": len(reps)})
        print(f"{p:9d} {2*p:9d} {lg:9.3f} {med:11.1f} {med-lg:8.3f}"
              f" {med/lg:7.3f}")
    with open(os.path.join(OUT, "scaling.json"), "w") as f:
        json.dump({"rows": rows, "seconds": round(time.time() - t0, 1)},
                  f, indent=1)
    exc = [r["excess"] for r in rows]
    print(f"\nexcess k_full - log2(2p): min={min(exc):.2f} "
          f"median={statistics.median(exc):.2f} max={max(exc):.2f}")
    print(f"ratio k_full/log2(2p) at the largest p: {rows[-1]['ratio']:.3f}")
    print(f"F2A2_SCALING_DONE seconds={time.time()-t0:.1f}")


if __name__ == "__main__":
    main()
