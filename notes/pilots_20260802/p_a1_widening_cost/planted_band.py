#!/usr/bin/env python3
"""Planted band-core fixture: a globally generic received pair whose live
slopes share a core of size w in [k+1, A-2].

Purpose: the organic toy corpus (audit_p8p9_local_20260710.py rows, and the
t=4/t=5 extensions in band_measure.py) produces NO cross pair with core in
the band, so it cannot measure the incremental population the widening adds.
Here we construct one directly and test, on it:

  * the sunflower cap  mult(W) <= (n-k)/(t-d)  (d-adaptive, as coded at
    audit_p8p9_local_20260710.py:205-220)          -- expected to HOLD
  * the banked line/pencil cap floor(R/h) = floor((n-k)/(A-k)), which is what
    (CLB2), (PSP) and (FN3) print for kappa = k -- expected to FAIL
  * the widened cap floor((n-w)/(A-w))            -- expected to HOLD
  * H1  #high-core rays <= 2 * moment             -- expected to HOLD

Run: tools/ramguard local -- python3 <this>
"""
import itertools, random, json
from math import comb

q = 97
random.seed(20260802)


def inv(a): return pow(a, q - 2, q)


def polymul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % q
    return out


def interp_coeffs(xs, ys, k):
    coeff = [0] * k
    for i in range(k):
        num = [1]
        for j in range(k):
            if j == i:
                continue
            num = polymul(num, [(-xs[j]) % q, 1])
        den = 1
        for j in range(k):
            if j == i:
                continue
            den = den * ((xs[i] - xs[j]) % q) % q
        w = ys[i] * inv(den) % q
        for d_ in range(len(num)):
            coeff[d_] = (coeff[d_] + w * num[d_]) % q
    return tuple(coeff)


def evalp(c, x):
    r = 0
    for co in reversed(c):
        r = (r * x + co) % q
    return r


def build(n, k, t, J, nslope, seed):
    """plant a codeword pair (f,g) with joint agreement exactly the first J
    coordinates, and nslope live slopes each picking up A-J extra agreements
    on pairwise disjoint blocks."""
    random.seed(seed)
    A = k + t
    extra = A - J
    D = list(range(1, n + 1))
    assert J + nslope * extra <= n, "not enough coordinates"
    f = tuple(random.randrange(q) for _ in range(k))
    g = tuple(random.randrange(q) for _ in range(k))
    u = [None] * n
    v = [None] * n
    Z = list(range(J))
    for i in Z:                       # joint agreement block
        u[i] = evalp(f, D[i])
        v[i] = evalp(g, D[i])
    slopes = random.sample(range(1, q), nslope)
    pos = J
    blocks = []
    for z in slopes:
        blk = list(range(pos, pos + extra))
        blocks.append(blk)
        pos += extra
        for i in blk:
            vi = random.randrange(1, q)
            v[i] = vi
            # want u + z v = f + z g at i
            u[i] = (evalp(f, D[i]) + z * evalp(g, D[i]) - z * vi) % q
    for i in range(n):                # free coordinates
        if u[i] is None:
            u[i] = random.randrange(q)
            v[i] = random.randrange(1, q)
        if v[i] == 0:
            v[i] = 1
    return u, v, f, g, Z, slopes, blocks


def analyse(n, k, t, u, v, want_slopes, J):
    A, R, h, r = k + t, n - k, t, n - (k + t)
    D = list(range(1, n + 1))
    Wsets = list(itertools.combinations(range(n), k))
    rays = {}
    for z in range(q):
        Uz = [(u[i] + z * v[i]) % q for i in range(n)]
        seen = set()
        for W in Wsets:
            c = interp_coeffs([D[i] for i in W], [Uz[i] for i in W], k)
            if c in seen:
                continue
            seen.add(c)
            s = sum(1 for i in range(n) if evalp(c, D[i]) == Uz[i])
            if s >= A:
                rays[(z, c)] = frozenset(i for i in range(n)
                                         if evalp(c, D[i]) == Uz[i])
    raylist = list(rays.items())

    # global genericity: max joint agreement of ANY codeword pair.  Every
    # codeword pair with joint agreement >= k is (P_W,Q_W) for a k-set W in
    # it, so scanning all k-sets is exhaustive at that threshold.
    maxJA = 0
    for W in Wsets:
        P = interp_coeffs([D[i] for i in W], [u[i] for i in W], k)
        Q = interp_coeffs([D[i] for i in W], [v[i] for i in W], k)
        ja = sum(1 for i in range(n)
                 if evalp(P, D[i]) == u[i] and evalp(Q, D[i]) == v[i])
        maxJA = max(maxJA, ja)
    generic = maxJA <= A - 1
    cascade_free = maxJA <= A - 2

    mult = {}
    for (z, c), s in rays.items():
        for W in itertools.combinations(sorted(s), k):
            mult[W] = mult.get(W, 0) + 1
    moment = sum(comb(m, 2) for m in mult.values())

    cross = []
    for a in range(len(raylist)):
        for b in range(a + 1, len(raylist)):
            (z1, _), s1 = raylist[a]
            (z2, _), s2 = raylist[b]
            if z1 != z2:
                cross.append((a, b, len(s1 & s2), s1 & s2))
    hist = {}
    for _, _, Jc, _ in cross:
        if Jc >= k:
            hist[Jc] = hist.get(Jc, 0) + 1

    hc_eq, hc_wide = set(), set()
    for a, b, Jc, _ in cross:
        (z1, _), _ = raylist[a]
        (z2, _), _ = raylist[b]
        if Jc == k:
            hc_eq |= {z1, z2}
        if k <= Jc <= A - 2:
            hc_wide |= {z1, z2}

    # caps, evaluated on every distinct core of size >= k
    rows = []
    seen = set()
    for _, _, Jc, core in cross:
        if Jc < k or Jc > A - 2 or core in seen:
            continue
        seen.add(core)
        L = len({z for (z, c), s in rays.items() if core <= s})
        rows.append(dict(w=Jc, L=L,
                         cap_widened=(n - Jc) // (A - Jc),
                         cap_banked_Rh=R // h))

    # sunflower cap, d-adaptive, on every k-subset of a band core
    sun = []
    for _, _, Jc, core in cross:
        if Jc < k or Jc > A - 2:
            continue
        for W in itertools.combinations(sorted(core), k):
            P = interp_coeffs([D[i] for i in W], [u[i] for i in W], k)
            Q = interp_coeffs([D[i] for i in W], [v[i] for i in W], k)
            d_ = sum(1 for i in range(n) if i not in W
                     and evalp(Q, D[i]) == v[i] and evalp(P, D[i]) == u[i])
            if t - d_ <= 0:
                continue
            sun.append(dict(mult=mult.get(W, 0), d=d_,
                            cap=(n - k) // (t - d_),
                            cap_at_d0=(n - k) // t))
    max_supp = max((len(s) for s in rays.values()), default=0)
    return dict(max_ray_support=max_supp, tangent_free=(max_supp <= A),
                n=n, k=k, t=t, A=A, R=R, h=h, r=r, band=[k + 1, A - 2],
                planted_J=J, planted_slopes=sorted(want_slopes),
                rays=len(rays), live_slopes=len({z for (z, c) in rays}),
                maxJointAgreement=maxJA, globally_generic=generic,
                below_cascade_threshold=cascade_free,
                cross=len(cross), core_hist=hist, moment=moment,
                highcore_slopes_eq_k=len(hc_eq),
                highcore_slopes_widened=len(hc_wide),
                H1=(2 * len(hc_wide) <= 2 * moment or moment == 0),
                cores=rows, sunflower=sun)


OUT = []
# n=14, k=5, t=4 -> A=9, R=9, h=4, r=5, band [6,7]; floor(R/h)=2.
# plant J=7 (top of the band) with 3 slopes, 2 extra agreements each.
for seed in (1, 2, 3):
    u, v, f, g, Z, sl, blocks = build(14, 5, 4, J=7, nslope=3, seed=seed)
    res = analyse(14, 5, 4, u, v, sl, 7)
    OUT.append(res)
    print(f"\n### seed {seed}: n=14 k=5 t=4 A=9 R=9 h=4 r=5 band [6,7]  "
          f"banked floor(R/h)={9//4}")
    print(f"  planted slopes {res['planted_slopes']}, planted core |Z|=7")
    print(f"  rays {res['rays']}, live slopes {res['live_slopes']}, "
          f"cross pairs {res['cross']}, moment {res['moment']}")
    print(f"  max joint agreement over ALL codeword pairs = "
          f"{res['maxJointAgreement']}  (A={res['A']}); globally generic = "
          f"{res['globally_generic']}; below cascade threshold A-1 = "
          f"{res['below_cascade_threshold']}")
    print(f"  core histogram (>=k): {dict(sorted(res['core_hist'].items()))}")
    print(f"  high-core SLOPES: current(=k) {res['highcore_slopes_eq_k']}  "
          f"widened([k,A-2]) {res['highcore_slopes_widened']}")
    print(f"  H1 ok: {res['H1']}; max ray support {res['max_ray_support']} "
          f"(A={res['A']}) -> no single-slope over-agreement: {res['tangent_free']}")
    for c in res["cores"]:
        flag_b = "VIOLATED" if c["L"] > c["cap_banked_Rh"] else "ok"
        flag_w = "VIOLATED" if c["L"] > c["cap_widened"] else "ok"
        print(f"    core size w={c['w']}: slopes through core L={c['L']}; "
              f"banked floor(R/h)={c['cap_banked_Rh']} -> {flag_b}; "
              f"widened floor((n-w)/(A-w))={c['cap_widened']} -> {flag_w}")
    bad_sun = [s for s in res["sunflower"] if s["mult"] > s["cap"]]
    bad_d0 = [s for s in res["sunflower"] if s["mult"] > s["cap_at_d0"]]
    if res["sunflower"]:
        print(f"    sunflower over k-subsets of band cores: "
              f"{len(res['sunflower'])} tests, d-adaptive violations "
              f"{len(bad_sun)}, d=0-cap violations {len(bad_d0)}; "
              f"sample {res['sunflower'][0]}")

with open("notes/pilots_20260802/p_a1_widening_cost/planted_band.json", "w") as fh:
    json.dump(OUT, fh, indent=1)
print("\ncheckpoint written: planted_band.json")
