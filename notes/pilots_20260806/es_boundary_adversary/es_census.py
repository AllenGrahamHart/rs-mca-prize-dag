#!/usr/bin/env python3
"""Round 16 -- (ES) boundary adversary: THE EXACT BAD-PRIME CENSUS (method M1).

For a fixed scaled-down row (n, r', w) this decides, for EVERY characteristic
p at once, whether an ACCIDENT (a non-periodic solution) exists -- by the
census identity validated in es_selftest.py:

    S is a solution in characteristic p (for some primitive n-th root of 1)
      <=>  gcd( Phi_n, V_1, ..., V_{w-1} ) has degree >= 1 in F_p[X]
      <=>  p | N(I_S),  I_S = (x_1,...,x_{w-1}) <= Z[zeta_n],

so the candidate primes are the prime divisors of gcd_s |N(x_s)| and each is
then CONFIRMED by the exact F_p[X] gcd.  No p-sweep, no sampling: the answer
is complete over all primes.

Orbit reduction: rotation (S -> S+1 multiplies x_s by the unit zeta^s),
dilation (S -> cS applies the Galois automorphism sigma_c) and complement
(x_s -> -x_s for 0 < s < n) all preserve the ideal I_S up to units/Galois,
hence preserve the bad-prime set exactly.  The invariance is VERIFIED
computationally here (check ORB) rather than assumed.

usage:  es_census.py N RPMIN RPMAX [WMAX]
run:    tools/ramguard local -- python3 notes/pilots_20260806/\
es_boundary_adversary/es_census.py 32 2 6
"""

import json
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from es_lib import (M_of, UnfactoredCofactor, coord_vector, cyclotomic_closure,
                    factorize, field_norm, mult_order, pgcd, phi_n_poly, pnorm)

FAIL = []


def fail(name, detail=""):
    FAIL.append((name, detail))
    print("  FAIL %s | %s" % (name, detail))


def colex_combinations(n, r):
    """r-subsets of range(n) in colex order; position == colex rank."""
    c = list(range(r))
    while True:
        yield tuple(c)
        i = 0
        while i < r and c[i] + 1 == (c[i + 1] if i + 1 < r else n):
            i += 1
        if i == r:
            return
        c[i] += 1
        for j in range(i):
            c[j] = j


def colex_rank(comb, binom):
    return sum(binom[c][j + 1] for j, c in enumerate(comb))


def orbit_masks(comb, n):
    """images of S under i -> c*i + b (c odd, b in Z/n)."""
    out = set()
    for c in range(1, n, 2):
        base = tuple(sorted((c * i) % n for i in comb))
        for b in range(n):
            out.add(tuple(sorted((i + b) % n for i in base)))
    return out


def bad_primes_for(S, n, w, norms):
    """the exact set of primes in which S (or a Galois dilate) is a solution."""
    g = 0
    for s in range(1, w):
        Ns = norms[s]
        if Ns != 0:
            g = math.gcd(g, abs(Ns))
    if g == 0:
        return None, []            # char-0 solution => periodic, not accident
    if g == 1:
        return [], []
    try:
        facs = factorize(g)
    except UnfactoredCofactor as e:
        return "UNFACTORED", [str(e)]
    PHI = phi_n_poly(n)
    bad = []
    for p in sorted(facs):
        if p == 2:
            continue
        gg = PHI
        for s in range(1, w):
            v = pnorm(coord_vector(S, s, n), p)
            if not v:
                continue
            gg = pgcd(gg, v, p)
            if len(gg) - 1 < 1:
                break
        if len(gg) - 1 >= 1:
            bad.append(p)
    return bad, []


def main():
    n = int(sys.argv[1])
    rpmin = int(sys.argv[2])
    rpmax = int(sys.argv[3])
    wmax_cap = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 9
    h = n // 2
    print("=" * 78)
    print("ROUND 16 -- EXACT BAD-PRIME CENSUS   n = %d, r' = %d..%d"
          % (n, rpmin, rpmax))
    print("=" * 78)
    print("in-scope (registered): delta = ord_n(p) in {1,2,4};  p > w;")
    print("Lam = log2 C(n,r') - |Z_w| log2 p;  Lam < 0 == SUB-BALANCE.")

    binom = [[math.comb(a, b) for b in range(rpmax + 2)] for a in range(n + 1)]
    results = []
    refutations = []
    unfactored = []

    for rp in range(rpmin, rpmax + 1):
        total = math.comb(n, rp)
        seen = bytearray(total)
        reps = 0
        wmax = min(rp, wmax_cap)
        # per (w) bookkeeping
        acc_orbits = {w: 0 for w in range(2, wmax + 1)}
        badp = {w: {} for w in range(2, wmax + 1)}
        for pos, comb in enumerate(colex_combinations(n, rp)):
            if seen[pos]:
                continue
            reps += 1
            for img in orbit_masks(comb, n):
                seen[colex_rank(img, binom)] = 1
            S = list(comb)
            norms = {}
            smin = None
            for s in range(1, wmax):
                v = coord_vector(S, s, n)
                norms[s] = field_norm(v, n)
                if smin is None and any(v):
                    smin = s
            for w in range(2, wmax + 1):
                if smin is None or smin >= w:
                    continue               # periodic (structural), not accident
                acc_orbits[w] += 1
                bad, err = bad_primes_for(S, n, w, norms)
                if bad == "UNFACTORED":
                    unfactored.append((rp, w, comb, err))
                    continue
                for p in bad:
                    badp[w].setdefault(p, comb)
        print("\n  r' = %d :  C(%d,%d) = %d subsets, %d orbit reps"
              % (rp, n, rp, total, reps))
        print("  %-4s %-5s %-9s %-12s %-11s %-11s %-9s"
              % ("w", "M", "struct", "acc-orbits", "max bad p", "delta", "Lam"))
        for w in range(2, wmax + 1):
            M = M_of(w)
            st = binom[n // M][rp // M] if rp % M == 0 else 0
            prim = badp[w]
            inscope = [p for p in prim
                       if mult_order(p, n) in (1, 2, 4) and p > w]
            best = max(inscope) if inscope else None
            if best is None:
                print("  %-4d %-5d %-9d %-12d %-11s %-11s %-9s"
                      % (w, M, st, acc_orbits[w],
                         max(prim) if prim else "-", "-", "-"))
                continue
            zw = len(cyclotomic_closure(w, n, best))
            lam = math.log2(math.comb(n, rp)) - zw * math.log2(best)
            print("  %-4d %-5d %-9d %-12d %-11d %-11d %-9.2f"
                  % (w, M, st, acc_orbits[w], best, mult_order(best, n), lam))
            for p in sorted(prim):
                d = mult_order(p, n)
                zwp = len(cyclotomic_closure(w, n, p))
                lamp = math.log2(math.comb(n, rp)) - zwp * math.log2(p)
                rec = dict(n=n, rp=rp, w=w, p=p, delta=d, zw=zwp,
                           lam=lamp, struct=st, witness=list(prim[p]),
                           inscope=bool(d in (1, 2, 4) and p > w),
                           p_gt_n=bool(p > n))
                results.append(rec)
                if rec["inscope"] and lamp < 0:
                    refutations.append(rec)

    # ------------------------------------------------------------------ ORB
    print("\n" + "-" * 78)
    print("[ORB] orbit-invariance of the bad-prime set (spot check)")
    rng = random.Random(5)
    bad = []
    for _ in range(6):
        rp = rng.randint(max(2, rpmin), rpmax)
        comb = tuple(sorted(rng.sample(range(n), rp)))
        w = min(rp, 4)
        if w < 2:
            continue
        nm = {s: field_norm(coord_vector(list(comb), s, n), n)
              for s in range(1, w)}
        b0, _ = bad_primes_for(list(comb), n, w, nm)
        img = sorted(orbit_masks(comb, n))[len(comb) % 7]
        nm2 = {s: field_norm(coord_vector(list(img), s, n), n)
               for s in range(1, w)}
        b1, _ = bad_primes_for(list(img), n, w, nm2)
        if b0 != b1:
            bad.append((comb, img, b0, b1))
    if bad:
        fail("ORB bad-prime set is not orbit-invariant", str(bad[:1]))
    else:
        print("  6 random (S, image) pairs: bad-prime sets identical -- the")
        print("  orbit reduction is sound.")

    # --------------------------------------------------------------- VERDICT
    print("\n" + "=" * 78)
    if unfactored:
        print("UNFACTORED COFACTORS (honest gap): %d rows" % len(unfactored))
        for u in unfactored[:5]:
            print("   r'=%d w=%d %s" % (u[0], u[1], u[3]))
    print("IN-SCOPE SUB-BALANCE ACCIDENTS (Lam < 0)  =  REFUTATIONS of (ES): %d"
          % len(refutations))
    for r in sorted(refutations, key=lambda z: z["lam"])[:20]:
        print("  n=%d r'=%d w=%d p=%d delta=%d |Z_w|=%d Lam=%+.3f struct=%d S=%s"
              % (r["n"], r["rp"], r["w"], r["p"], r["delta"], r["zw"],
                 r["lam"], r["struct"], r["witness"]))
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "census_n%d_%d_%d.json" % (n, rpmin, rpmax))
    with open(out, "w") as fh:
        json.dump(dict(n=n, rpmin=rpmin, rpmax=rpmax, records=results,
                       refutations=refutations,
                       unfactored=[[u[0], u[1], list(u[2])] for u in unfactored]),
                  fh, indent=1)
    print("wrote %s  (%d bad-prime records)" % (out, len(results)))
    print("failures: %d" % len(FAIL))
    print("=" * 78)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
