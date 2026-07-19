#!/usr/bin/env python3
"""FALSIFICATION ROUND F2 (Modal): attack C2 (level-factorization) at the
D2 level — the exact cross-level kernel correlation on SHARED cells.

Setup (toy tower slice, n' = 32): cells x_i = zeta^i, i < 16 (half-section,
zeta of order 32 at the pinned embedding). Level 0 = odd moments {1, 3}
(L_0 = 2); level 1 = 2*odd moments {2, 6} (L_1 = 2). ONE shared ternary
d in {-1,0,1}^16 (the U-central measure). Exact counts via meet-in-middle
(3^8 half-enumerations joined on the 4-tuple of constraint residues).

  ratio(q) = Pr[d in ker A_0  AND  d in ker A_1] /
             (Pr[d in ker A_0] * Pr[d in ker A_1])

C2's equality form predicts ratio ~ 1. The known danger mechanism is the
round-6 LIFT identity (e -> 2e maps vanishers identically): lift-related
kernel elements are shared structure between the two moment windows and
should inflate the ratio at rows possessing them. Systematic inflation
refutes C2-as-equality; the Hoelder route then prices it.

~40 primes q ≡ 1 (mod 32) in [20000, 60000]; one Modal job per prime,
each a few seconds.
"""
import json

import modal

app = modal.App("dli-f2-levelcorr")
image = modal.Image.debian_slim().pip_install("numpy")

NP, NCELL = 32, 16
M0 = (1, 3)     # level-0 moments (odd)
M1 = (2, 6)     # level-1 moments (2*odd)


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def corr_at(q):
    import itertools
    import numpy as np

    # pinned embedding
    n = q - 1
    fs = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            fs.add(d)
            n //= d
        d += 1
    if n > 1:
        fs.add(n)
    g = 2
    while any(pow(g, (q - 1) // p, q) == 1 for p in fs):
        g += 1
    zeta = pow(g, (q - 1) // NP, q)
    cells = [pow(zeta, i, q) for i in range(NCELL)]
    momrows = {m: np.array([pow(x, m, q) for x in cells], dtype=np.int64)
               for m in M0 + M1}

    half = NCELL // 2
    terns = np.array(list(itertools.product((-1, 0, 1), repeat=half)),
                     dtype=np.int64)              # (6561, 8)

    def half_keys(idx):
        # residue 4-tuples of each half-assignment for all four constraints
        cols = np.stack([momrows[m][idx] for m in M0 + M1])   # (4, 8)
        return (terns @ cols.T) % q                            # (6561, 4)

    A = half_keys(slice(0, half))
    B = half_keys(slice(half, NCELL))

    def joint_count(constraint_ids):
        """#d with all named constraints zero, via hash join."""
        from collections import defaultdict
        table = defaultdict(int)
        for row in A[:, constraint_ids]:
            table[tuple(row.tolist())] += 1
        tot = 0
        for row in B[:, constraint_ids]:
            need = tuple((-x) % q for x in row.tolist())
            tot += table.get(need, 0)
        return tot

    n0 = joint_count([0, 1])          # ker A_0
    n1 = joint_count([2, 3])          # ker A_1
    nb = joint_count([0, 1, 2, 3])    # both
    tot = 3 ** NCELL
    p0, p1, pb = n0 / tot, n1 / tot, nb / tot
    ratio = pb / (p0 * p1) if p0 > 0 and p1 > 0 else None
    return {"q": q, "n0": n0, "n1": n1, "nboth": nb,
            "rand_model_n0": tot / q**2,
            "ratio": ratio}


@app.local_entrypoint()
def main():
    def is_prime(n):
        if n < 2 or n % 2 == 0:
            return n == 2
        d, s = n - 1, 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            if a % n == 0:
                continue
            x = pow(a, d, n)
            if x in (1, n - 1):
                continue
            for _ in range(s - 1):
                x = x * x % n
                if x == n - 1:
                    break
            else:
                return False
        return True

    primes = [q for q in range(20001, 60000, 32) if is_prime(q)][:40]
    results = [r for r in corr_at.map(primes, return_exceptions=True)
               if isinstance(r, dict)]
    ratios = [r["ratio"] for r in results if r["ratio"] is not None]
    inflated = [r for r in results if r["ratio"] and r["ratio"] > 2.0]
    print(f"{len(results)} primes; ratio: min={min(ratios):.3f} "
          f"median={sorted(ratios)[len(ratios)//2]:.3f} max={max(ratios):.3f}")
    print(f"primes with ratio > 2: {len(inflated)}")
    for r in sorted(results, key=lambda r: -(r['ratio'] or 0))[:8]:
        print(f"  q={r['q']}: n0={r['n0']} n1={r['n1']} both={r['nboth']} "
              f"(rand n0 ~ {r['rand_model_n0']:.1f}) ratio={r['ratio']:.3f}")
    with open("/tmp/f2_levelcorr.json", "w") as f:
        json.dump(results, f, indent=1)
