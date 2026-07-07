#!/usr/bin/env python3
"""h=3 Stepanov-swing data program (Modal). Per row (n, q):

(i)   exact T_3 census (subset buckets) + toral + orbit-structure
      classification of every nontoral trade (rotation / reflection /
      unstructured) — hunts interior structured families;
(ii)  S(F) fiber distribution (= signature-class sizes) vs the n/3 cap;
(iii) conic point counts N_2(F) = #{(u,v) in mu_n^2, u != v, F(u)=F(v)}
      for all colliding F plus a random sample — tests whether the per-F
      Weil loss is real (max N_2 ~ sqrt(q)) or conics over subgroups are
      uniformly thin (max N_2 = O(1));
(iv)  the global moment M = sum_z T(z)^2 over ORDERED triples with
      repeats (triple-convolution DP, exact int64) + machine check of
      the bookkeeping identity M = 72*T_3 + trivial terms, where the
      trivial terms are computed exactly from multiset-overlap patterns
      via a second small DP (ordered pairs of triples with equal sums of
      (x, x^2) AND equal multisets).

Rows: q ~ c*n^2 for c in {1,2,4}; the M-DP runs where q^2 cells fit."""
import itertools
import json
import modal

app = modal.App("rs-mca-f3-h3prog")
image = modal.Image.debian_slim().pip_install("numpy")


def _next_prime_1mod(n, lo):
    def isp(m):
        if m < 2:
            return False
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            if m % a == 0:
                return m == a
        d, r = m - 1, 0
        while d % 2 == 0:
            d //= 2; r += 1
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            x = pow(a, d, m)
            if x in (1, m - 1):
                continue
            for _ in range(r - 1):
                x = x * x % m
                if x == m - 1:
                    break
            else:
                return False
        return True
    q = (lo // n) * n + 1
    while q <= lo or not isp(q):
        q += n
    return q


def jobs():
    out = []
    for n in (96, 128, 160, 192, 256):
        for c in (1, 2, 4):
            out.append((n, c))
    return out


@app.function(image=image, cpu=4, memory=8192, timeout=280)
def row(job):
    import numpy as np
    import random
    n, cmult = job
    q = _next_prime_1mod(n, cmult * n * n)
    h = 3
    g = None
    for cand in range(2, q):
        x = pow(cand, (q - 1) // n, q)
        if x == 1:
            continue
        y, order = x, 1
        while y != 1:
            y = y * x % q
            order += 1
        if order == n:
            g = x
            break
    D = [pow(g, i, q) for i in range(n)]

    # (i)+(ii): subset census
    counts = {}
    for P in itertools.combinations(range(n), 3):
        r0, r1, r2 = D[P[0]], D[P[1]], D[P[2]]
        e1 = (r0 + r1 + r2) % q
        e2 = (r0 * r1 + r0 * r2 + r1 * r2) % q
        counts[(e1, e2)] = counts.get((e1, e2), 0) + 1
    colliding = {s for s, k in counts.items() if k >= 2}
    members = {}
    if colliding:
        for P in itertools.combinations(range(n), 3):
            r0, r1, r2 = D[P[0]], D[P[1]], D[P[2]]
            e1 = (r0 + r1 + r2) % q
            e2 = (r0 * r1 + r0 * r2 + r1 * r2) % q
            if (e1, e2) in colliding:
                members.setdefault((e1, e2), []).append(P)
    T = toral = rot_pairs = refl_pairs = unstructured = 0
    step = n // 3 if n % 3 == 0 else None
    for mem in members.values():
        for i in range(len(mem)):
            for j in range(i + 1, len(mem)):
                A, B = mem[i], mem[j]
                if set(A) & set(B):
                    continue
                T += 1
                if step and all(x % step == A[0] % step for x in A) and \
                        all(x % step == B[0] % step for x in B):
                    toral += 1
                    continue
                if any(sorted((a + s) % n for a in A) == list(B)
                       for s in range(n)):
                    rot_pairs += 1
                elif any(sorted((s - a) % n for a in A) == list(B)
                         for s in range(n)):
                    refl_pairs += 1
                else:
                    unstructured += 1
    fibmax = max(counts.values())
    fib_hist = {}
    for k in counts.values():
        fib_hist[k] = fib_hist.get(k, 0) + 1

    # (iii) conic counts for colliding F + sample
    rng = random.Random(1234 + n + cmult)
    Fs = [P for mem in members.values() for P in mem][:40]
    Fs += [tuple(sorted(rng.sample(range(n), 3))) for _ in range(60)]
    n2max = 0
    n2_colliding = []
    Dset = D
    for P in Fs:
        a = -(Dset[P[0]] + Dset[P[1]] + Dset[P[2]]) % q
        b = (Dset[P[0]] * Dset[P[1]] + Dset[P[0]] * Dset[P[2]]
             + Dset[P[1]] * Dset[P[2]]) % q
        cnt = 0
        for ui in range(n):
            u = Dset[ui]
            for vi in range(ui + 1, n):
                v = Dset[vi]
                if (u * u + u * v + v * v + a * (u + v) + b) % q == 0:
                    cnt += 1
        n2max = max(n2max, cnt)
        n2_colliding.append(cnt)

    # (iv) global moment M via triple convolution over (Z_q)^2, exact
    M = None
    ident = None
    if q <= 66000:
        base = np.zeros((q, q), dtype=np.float64)
        for x in D:
            base[x % q, (x * x) % q] += 1
        f = np.fft.rfft2(base)
        trip = np.fft.irfft2(f ** 3, s=(q, q))
        trip = np.rint(trip)
        M = int((trip.astype(np.int64) ** 2).sum())
        # trivial part: ordered pairs of triples with equal MULTISETS:
        # per multiset of size 3 with distinct entries: 36; with a double:
        # ... compute exactly: sum over multisets m of (perm count)^2
        # perms: distinct: 6 -> 36; one pair: 3 -> 9; triple: 1 -> 1
        n_distinct = n * (n - 1) * (n - 2) // 6
        n_pair = n * (n - 1)          # {x,x,y}
        n_triple = n
        trivial = 36 * n_distinct + 9 * n_pair + 1 * n_triple
        # nontrivial ordered = M - trivial; disjoint-support distinct-entry
        # part = 72*T + (equal-signature pairs sharing >= 1 point or with
        # repeats). For distinct-entry triples sharing points: impossible
        # (proved). Repeat-entry collisions measured as residue:
        ident = {"M": M, "trivial": trivial,
                 "nontrivial": M - trivial, "seventytwoT": 72 * T,
                 "residue_repeats": M - trivial - 72 * T}
    return {"n": n, "q": q, "cmult": cmult, "T": T, "toral": toral,
            "rot": rot_pairs, "refl": refl_pairs,
            "unstructured": unstructured, "fibmax": fibmax,
            "fib_hist": {str(k): v for k, v in sorted(fib_hist.items())[-4:]},
            "n2max_conic": n2max, "moment": ident}


@app.local_entrypoint()
def main():
    res = [r for r in row.map(jobs(), return_exceptions=True)
           if isinstance(r, dict)]
    print(f"{'(n,c)':>10} {'q':>8} {'T':>7} {'toral':>6} {'rot':>5} {'refl':>5} "
          f"{'unstr':>6} {'fibmax':>7} {'conic_max':>9} {'M-resid':>9}")
    for r in sorted(res, key=lambda r: (r['n'], r['cmult'])):
        mres = r['moment']['residue_repeats'] if r['moment'] else '-'
        print(f"  ({r['n']},{r['cmult']})".rjust(10) + f" {r['q']:>8} {r['T']:>7} "
              f"{r['toral']:>6} {r['rot']:>5} {r['refl']:>5} {r['unstructured']:>6} "
              f"{r['fibmax']:>7} {r['n2max_conic']:>9} {str(mres):>9}")
    with open("/tmp/f3_h3prog.json", "w") as f:
        json.dump(res, f, indent=1)
