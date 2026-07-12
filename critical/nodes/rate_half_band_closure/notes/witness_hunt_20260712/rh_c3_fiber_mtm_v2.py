#!/usr/bin/env python3
"""rh_c3_fiber_mtm_v2: TASK 3 — FULL-FIBER MTM census, two band-analogue cells.

Reduction (validated vs brute interpolation at n=16 in v1): for received word
Y = X^k * L_T0 (deg k+t), list members at agreement >= k+t on mu_n biject with
size-(k+t) subsets S whose locator matches Y's top t+1 coefficients. The fiber
count IS the exact full list count — every witness shape, known or unknown.

DEDUP FACT (catch, discovered in v1): the multi-scale qcore families are
NESTED — an order-2M coset (not containing C0) is a union of two order-M
cosets, so family(2M) is a strict subfamily of family(M). Deduped supply at a
band cell = C(n/M*-1, k/M*) at the finest admissible scale M* alone, NOT the
sum over scales. (v1 predicted 4 = 3+1 at n=32,t=5; the census's 3 is correct
and equals the deduped count.)

Cells (both fiber-starved for q >= 97 — the faithful razor regime):
  A: n=32, k=16, t=5, T0 in the order-8 subgroup;  deduped qcore = C(3,2) = 3
  B: n=32, k=16, t=3, T0 in the order-4 subgroup;  deduped qcore = C(7,4) = 35
Budget: 2 x 2^16 DP states per (cell, q) — under the 10^7-state law.
"""
from math import comb
import random

def is_prime(n):
    if n < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0: return n == p
    d, s = n-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a, d, n)
        if x in (1, n-1): continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

def find_gen(q, n):
    co = (q-1)//n
    for g0 in range(2, 10000):
        g = pow(g0, co, q)
        if pow(g, n//2, q) != 1: return g
    raise RuntimeError

N_DOM, K = 32, 16

def mul_lin(ser, a, q):
    # series *= (1 - a z) mod z^(len+1); ser = (s1..sL), s0 = 1 implicit
    L = len(ser)
    out = []
    prev = 1
    for j in range(L):
        out.append((ser[j] - a*prev) % q)
        prev = ser[j]
    return tuple(out)

def ser_div(c, s, q):
    L = len(c)
    r = [0]*(L+1); r[0] = 1
    cc = (1,)+tuple(c); ss = (1,)+tuple(s)
    for j in range(1, L+1):
        acc = cc[j]
        for i in range(1, j+1):
            acc -= ss[i]*r[j-i]
        r[j] = acc % q
    return tuple(r[1:])

def series_of(pts, t, q):
    s = (0,)*t
    for a in pts: s = mul_lin(s, a, q)
    return s

def half_dp(points, t, q):
    d = {(0, (0,)*t): 1}
    for a in points:
        add = {}
        for (sz, ser), v in d.items():
            key = (sz+1, mul_lin(ser, a, q))
            add[key] = add.get(key, 0) + v
        for key, c in add.items():
            d[key] = d.get(key, 0) + c
    return d

def half_dp_masks(points, t, q):
    d = {(0, (0,)*t): [0]}
    for idx, a in enumerate(points):
        add = {}
        for (sz, ser), lst in list(d.items()):
            key = (sz+1, mul_lin(ser, a, q))
            add.setdefault(key, []).extend(m | (1 << idx) for m in lst)
        for key, lst in add.items():
            d.setdefault(key, []).extend(lst)
    return d

def probe(d1, d2, target, s_sz, q):
    tot = 0
    for (sz1, ser1), c1 in d1.items():
        sz2 = s_sz - sz1
        if sz2 < 0 or sz2 > 16: continue
        c2 = d2.get((sz2, ser_div(target, ser1, q)))
        if c2: tot += c1*c2
    return tot

def probe_sets(d1m, d2m, target, s_sz, q):
    hits = []
    for (sz1, ser1), lst1 in d1m.items():
        sz2 = s_sz - sz1
        if sz2 < 0 or sz2 > 16: continue
        lst2 = d2m.get((sz2, ser_div(target, ser1, q)))
        if lst2:
            hits.extend((m1, m2) for m1 in lst1 for m2 in lst2)
    return hits

def run_cell(q, t, msub, n_random=0, classify=True):
    """msub: order of the subgroup hosting T0 (t < msub required)."""
    s_sz = K + t
    g = find_gen(q, N_DOM)
    D = [pow(g, i, q) for i in range(N_DOM)]
    Hm = [pow(g, (N_DOM//msub)*i, q) for i in range(msub)]   # order-msub subgroup
    T0 = Hm[:t]
    target = series_of(T0, t, q)
    D1, D2 = D[:16], D[16:]
    d1 = half_dp(D1, t, q); d2 = half_dp(D2, t, q)
    fiber = probe(d1, d2, target, s_sz, q)
    zerof = probe(d1, d2, (0,)*t, s_sz, q)
    rng = random.Random(9999 + q + t)
    gen = [probe(d1, d2, series_of(rng.sample(D, t), t, q), s_sz, q)
           for _ in range(5)]
    rnd = [probe(d1, d2, tuple(rng.randrange(q) for _ in range(t)), s_sz, q)
           for _ in range(n_random)]
    out = dict(q=q, fiber=fiber, zero=zerof, generic=gen, rnd=rnd)
    if classify and fiber:
        d1m = half_dp_masks(D1, t, q); d2m = half_dp_masks(D2, t, q)
        hits = probe_sets(d1m, d2m, target, s_sz, q)
        assert len(hits) == fiber
        # classify rest = S - T0 by coset structure at scale msub
        cosN = N_DOM // msub
        cos_m = [frozenset((pow(g, j, q)*x) % q for x in Hm) for j in range(cosN)]
        n_coset, other = 0, []
        for m1, m2 in hits:
            S = {D1[i] for i in range(16) if m1 >> i & 1} | \
                {D2[i] for i in range(16) if m2 >> i & 1}
            rest = frozenset(S) - set(T0)
            # is rest a union of order-msub cosets (excluding C0 = cos_m[0])?
            used = [c for c in cos_m[1:] if c <= rest]
            if len(rest) == K and sum(len(c) for c in used) == K and \
               frozenset().union(*used) == rest:
                n_coset += 1
            else:
                other.append(sorted(S))
        out["coset_members"] = n_coset
        out["other"] = other
    return out

def main():
    cells = [("A: t=5, T0 in order-8 subgroup, deduped qcore = C(3,2) = 3",
              5, 8, comb(3, 2)),
             ("B: t=3, T0 in order-4 subgroup, deduped qcore = C(7,4) = 35",
              3, 4, comb(7, 4))]
    qs = [x for x in range(97, 4000, 32) if is_prime(x)][:10]
    big = []
    n0 = (1 << 40) | 1
    while len(big) < 1:
        if is_prime(n0): big.append(n0)
        n0 += 32
    for label, t, msub, dedup in cells:
        print("=" * 96)
        print(f"CELL {label}   [starved: C(32,{K+t}) = {comb(32,K+t):,} < 97^{t} = {97**t:,}: {comb(32,K+t) < 97**t}]")
        print("=" * 96)
        print(f"{'q':>13} {'fiber':>6} {'extras':>7} {'coset-cls':>9} {'other':>6} "
              f"{'zero-fiber':>10} {'generic5':>17} {'rnd(max/n)':>11}")
        for q in qs + big:
            nr = 60 if q in (97, 257, 3329) else 0
            r = run_cell(q, t, msub, n_random=nr)
            rmax = f"{max(r['rnd'])}/{len(r['rnd'])}" if r['rnd'] else "-"
            oth = len(r.get('other', []))
            print(f"{q:>13} {r['fiber']:>6} {r['fiber']-dedup:>7} "
                  f"{r.get('coset_members','-'):>9} {oth:>6} {r['zero']:>10} "
                  f"{str(r['generic']):>17} {rmax:>11}")
            if oth:
                for s in r['other'][:3]:
                    print(f"      OTHER-SHAPE member: {s}")
        print()
    print("READS: extras = fiber - deduped qcore. Razor-scaled win line = +4.83 bits (x28.4).")
    print("       'other' > 0 at large q would be a NEW mechanism; at small q, classify vs sporadic.")

if __name__ == "__main__":
    main()
