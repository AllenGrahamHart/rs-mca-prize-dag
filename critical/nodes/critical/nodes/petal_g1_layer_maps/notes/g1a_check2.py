#!/usr/bin/env python3
"""g1a_check2 — Monte Carlo cofactor-density check for GENUINE chart words u1
at the consumed shape n'=64, k'=32 (official n=128 layout), q in {257, 641}.

Measures: density of DD-consistent (k'+1)-supports containing y_nf (predict
~1/q), band-class density after the exactness sieve, and the weight (m'+1)
distribution. Confirms the first-moment law that powers F4/F5 at a shape far
beyond exhaustive reach (C(63,32) ~ 9.2e17)."""
import sys
import numpy as np

NPR, KPR = 64, 32
NF = KPR - 1                     # 31
T = NPR - KPR                    # 32

def find_subgroup_gen(q, order):
    for g in range(2, q):
        if pow(g, (q - 1) // order, q) != 1 or True:
            h = pow(g, (q - 1) // order, q)
            # h has order dividing `order`; check exact
            o, x = 1, h
            while x != 1:
                x = x * h % q; o += 1
            if o == order:
                return h
    raise RuntimeError

def modpow_vec(a, e, q):
    r = np.ones_like(a)
    b = a % q
    while e:
        if e & 1:
            r = r * b % q
        b = b * b % q
        e >>= 1
    return r

def run(q, nsamp, seed, label_mode):
    rng = np.random.default_rng(seed)
    h = find_subgroup_gen(q, NPR)            # generator of H^2, order 64
    Y = np.array([pow(h, j, q) for j in range(NPR)], dtype=np.int64)
    assert len(set(Y.tolist())) == NPR
    Zp = Y[:NF]                              # Z' = y_0..y_30
    # L_{Z'}(x) for all points
    LZp = np.ones(NPR, dtype=np.int64)
    for z in Zp:
        LZp = LZp * ((Y - z) % q) % q
    if label_mode == "geom5":
        c = np.array([pow(5, i + 1, q) for i in range(T)], dtype=np.int64)
        if np.any(c % q == 0): raise RuntimeError
    else:
        c = rng.integers(1, q, T).astype(np.int64)
    u1 = np.zeros(NPR, dtype=np.int64)
    u1[KPR:] = c * LZp[KPR:] % q
    assert np.all(u1[:KPR] == 0) and np.all(u1[KPR:] != 0)

    others = np.array([j for j in range(NPR) if j != NF])
    a = KPR + 1                              # 33
    hits_supports = []
    nhit = 0
    B = 0
    band_m = []
    batch = 20000
    done = 0
    while done < nsamp:
        b = min(batch, nsamp - done)
        # sample b supports: y_nf + 32 distinct others
        keys = rng.random((b, NPR - 1))
        sel = np.argsort(keys, axis=1)[:, :a - 1]
        idx = np.concatenate([np.full((b, 1), NF), others[sel]], axis=1)  # (b,33)
        pts = Y[idx]
        vals = u1[idx]
        # L'_i = prod_{j != i} (pts_i - pts_j) mod q
        Lp = np.ones((b, a), dtype=np.int64)
        for j in range(a):
            d = (pts - pts[:, j:j + 1]) % q
            d[:, j] = 1
            Lp = Lp * d % q
        inv = modpow_vec(Lp, q - 2, q)
        DD = (vals * inv % q).sum(axis=1) % q
        hit = np.nonzero(DD == 0)[0]
        nhit += len(hit)
        # exactness sieve per hit
        for r in hit:
            S = idx[r]
            p = Y[S].astype(object)
            v = u1[S].astype(object)
            # Lagrange evaluation of the interpolant at all 64 points
            agree = []
            wts = []
            for i in range(a):
                den = 1
                for j in range(a):
                    if j != i:
                        den = den * (int(p[i]) - int(p[j])) % q
                wts.append(int(v[i]) * pow(den, q - 2, q) % q)
            Sset = set(S.tolist())
            full = list(Sset)
            for x in range(NPR):
                if x in Sset:
                    agree.append(x); continue
                xx = int(Y[x])
                tot = 0
                prod_all = 1
                for j in range(a):
                    prod_all = prod_all * ((xx - int(p[j])) % q) % q
                for i in range(a):
                    tot = (tot + wts[i] * pow((xx - int(p[i])) % q, q - 2, q)) % q
                gx = tot * prod_all % q
                if gx == int(u1[x]) % q:
                    agree.append(x)
            agree = sorted(set(agree))
            if len(agree) <= KPR + 2 and NF in agree:
                # band class; only count each class once (distinct supports of
                # the same class both consistent only if |A|=34: dedupe by A)
                Akey = tuple(agree)
                hits_supports.append(Akey)
                z = sum(1 for i in agree if i < KPR)
                band_m.append(len(agree) - z)
        done += b
    classes = set(hits_supports)
    Bc = len(classes)
    dens = nhit / nsamp
    print(f"q={q} labels={label_mode}: samples={nsamp} DD-hits={nhit} "
          f"density*q={dens*q:.3f} (predict ~1)")
    print(f"   band classes among hits: {Bc} "
          f"(band fraction of hits {Bc/max(nhit,1):.3f})")
    if band_m:
        bm = np.array(band_m)
        print(f"   m' stats: mean={bm.mean():.1f} min={bm.min()} max={bm.max()}"
              f"  (weight m'+1 mean {bm.mean()+1:.1f}; NOT O(1) — catch)")
    # implied class-count estimate: C(63,32)/q * band_fraction
    from math import comb
    est = comb(NPR - 1, KPR) / q * (Bc / max(nhit, 1))
    print(f"   implied #band-classes(size 33) ~ {est:.3e}   "
          f"[budgets: own-row (121/128)*128^6={121/128*128**6:.3e}, "
          f"C(63,32)={comb(63,32):.3e}]")
    return dens * q, Bc / max(nhit, 1)

ok = True
for (q, ns) in [(257, 300000), (641, 600000)]:
    for lm in ("geom5", "random"):
        d, bf = run(q, ns, seed=q * 7 + len(lm), label_mode=lm)
        if not (0.7 < d < 1.4):
            print(f"FAIL: density*q={d} far from 1"); ok = False
        if bf < 0.8:
            print(f"NOTE: band fraction {bf} (oversized attrition)");
print("ALL PASS" if ok else "DENSITY ANOMALY")
sys.exit(0 if ok else 1)
