#!/usr/bin/env python3
"""sr_product: INDEPENDENT instrument.  No W/lambda formalism at all — it works
directly with the received word as a VECTOR on D = mu_n and interpolates.

A subset A (|A| = a = k+t) is an agreement set iff the unique interpolant of
Y on A (degree < a) has degree < k.  The codeword is that interpolant.

  F_SUBSET = # such A ;  F_LIST = # distinct interpolants ;  AGRPROF from
  the multiplicities (a codeword of agreement j is hit C(j,a) times).

Modes:
  prod   n q t          the PRODUCT WORD  y(x) = x^{-1} + c x^{k+t-1-i} family
                        (c_i swept over structural values); exact counts
  allw   n q t          EXHAUSTIVE over ALL received words at this (n,t):
                        enumerate P = L_A * u (u monic, deg <= n-1-a), bucket
                        by the coset key = coefficients of degrees k..n-1.
"""
import json, sys
from itertools import combinations
from math import comb


def is_prime(mm):
    if mm < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if mm % p == 0:
            return mm == p
    dd, s = mm - 1, 0
    while dd % 2 == 0:
        dd //= 2
        s += 1
    for A in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(A, dd, mm)
        if x in (1, mm - 1):
            continue
        for _ in range(s - 1):
            x = x * x % mm
            if x == mm - 1:
                break
        else:
            return False
    return True


def find_gen(q, n):
    co = (q - 1) // n
    for g0 in range(2, 100000):
        g = pow(g0, co, q)
        if pow(g, n // 2, q) != 1 and pow(g, n, q) == 1:
            if len({pow(g, i, q) for i in range(n)}) == n:
                return g
    raise RuntimeError


def interp_deg_and_poly(A, Yv, D, q, a):
    """Lagrange interpolant of Y on A (|A| = a), returned as a coeff tuple."""
    # L_A
    L = [1]
    for i in A:
        x = D[i]
        nl = [0] * (len(L) + 1)
        for j, c in enumerate(L):
            if c:
                nl[j + 1] = (nl[j + 1] + c) % q
                nl[j] = (nl[j] - c * x) % q
        L = nl
    out = [0] * a
    for i in A:
        x = D[i]
        # Lp = L / (X - x) by synthetic division; Lpx = Lp(x) = L'(x)
        Lp = [0] * a
        r = 0
        for j in range(a, -1, -1):
            if j == a:
                r = L[j]
                continue
            Lp[j] = r
            r = (L[j] + r * x) % q
        Lpx = 0
        for c in reversed(Lp):
            Lpx = (Lpx * x + c) % q
        w = Yv[i] * pow(Lpx, q - 2, q) % q
        for j in range(a):
            if Lp[j]:
                out[j] = (out[j] + w * Lp[j]) % q
    return tuple(out)


def census(n, q, t, Yv, D, out_top=0):
    k = n // 2
    a = k + t
    seen = {}
    nA = 0
    for A in combinations(range(n), a):
        P = interp_deg_and_poly(A, Yv, D, q, a)
        if any(P[j] for j in range(k, a)):
            continue
        nA += 1
        seen[P] = seen.get(P, 0) + 1
    prof = {}
    for mult in seen.values():
        j = None
        for jj in range(a, n + 1):
            if comb(jj, a) == mult:
                j = jj
                break
        key = str(j) if j is not None else "mult%d" % mult
        prof[key] = prof.get(key, 0) + 1
    return dict(F_SUBSET=nA, F_LIST=len(seen), agreement_profile=prof,
                dedup_ok=(sum(comb(int(j), a) * c for j, c in prof.items()
                              if not j.startswith("mult")) == nA))


def mode_prod(n, q, t, out=None):
    k = n // 2
    a = k + t
    g = find_gen(q, n)
    D = [pow(g, i, q) for i in range(n)]
    res = []
    # y(x) = x^{-1} + sum_{i<t} c_i x^{a-1-i};  conditions: e_i(A) prescribed
    # sweep c_0 over mu_n-compatible values and c_{i>0} over a few structural ones
    for c0i in range(min(n, 4)):
        c0 = D[c0i]
        cs = [c0] + [0] * (t - 1)
        Yv = []
        for i in range(n):
            x = D[i]
            v = pow(x, q - 2, q)
            for ii in range(t):
                if cs[ii]:
                    v = (v + cs[ii] * pow(x, a - 1 - ii, q)) % q
            Yv.append(v % q)
        r = census(n, q, t, Yv, D)
        r.update(n=n, q=q, t=t, a=a, word="prod_c0=D[%d]" % c0i,
                 cs_index=c0i,
                 PLATEAU_t1=comb(n // 2 - 1, n // 4),
                 pred_t1=comb(n, a) // n if t == 1 else None)
        res.append(r)
        print(json.dumps(r), flush=True)
    if out:
        with open(out, "w") as f:
            json.dump(res, f, indent=1)
    return res


def mode_allw(n, q, t, out=None):
    """EXHAUSTIVE over all received words with a nonempty list, at this (n,t)."""
    k = n // 2
    a = k + t
    dmax = n - 1 - a
    assert dmax >= 0
    g = find_gen(q, n)
    D = [pow(g, i, q) for i in range(n)]
    us = []
    for d in range(dmax + 1):
        if d == 0:
            us.append([1])
            continue
        for co in range(q ** d):
            c = []
            x = co
            for _ in range(d):
                c.append(x % q)
                x //= q
            c.append(1)
            us.append(c)
    LAs = []
    for A in combinations(range(n), a):
        p = [1]
        for i in A:
            x = D[i]
            np_ = [0] * (len(p) + 1)
            for j, c in enumerate(p):
                if c:
                    np_[j + 1] = (np_[j + 1] + c) % q
                    np_[j] = (np_[j] - c * x) % q
            p = np_
        LAs.append((A, p))
    cnt = {}
    for A, LA in LAs:
        for u in us:
            P = [0] * (len(LA) + len(u) - 1)
            for i, c in enumerate(LA):
                if c:
                    for j, e in enumerate(u):
                        if e:
                            P[i + j] = (P[i + j] + c * e) % q
            key = tuple(P[j] if j < len(P) else 0 for j in range(k, n))
            cnt[key] = cnt.get(key, 0) + 1
    maxsub = max(cnt.values())
    tau = 2
    hot = {key for key, c in cnt.items() if c >= tau}
    dist = {}
    for A, LA in LAs:
        for u in us:
            P = [0] * (len(LA) + len(u) - 1)
            for i, c in enumerate(LA):
                if c:
                    for j, e in enumerate(u):
                        if e:
                            P[i + j] = (P[i + j] + c * e) % q
            key = tuple(P[j] if j < len(P) else 0 for j in range(k, n))
            if key in hot:
                d = dist.setdefault(key, {})
                pk = tuple(P)
                d[pk] = d.get(pk, 0) + 1
    rows = []
    for key, dd in dist.items():
        fl = len(dd)
        prof = {}
        for mult in dd.values():
            j = None
            for jj in range(a, n + 1):
                if comb(jj, a) == mult:
                    j = jj
                    break
            kk = str(j) if j is not None else "mult%d" % mult
            prof[kk] = prof.get(kk, 0) + 1
        deg = max(max(i for i, c in enumerate(p) if c) for p in dd)
        rows.append(dict(key=list(key), F_SUBSET=cnt[key], F_LIST=fl,
                         delta=deg - a, profile=prof))
    rows.sort(key=lambda r: (-r["F_LIST"], -r["F_SUBSET"]))
    per_delta = {}
    for r in rows:
        e = per_delta.setdefault(str(r["delta"]), dict(maxlist=0, maxsub=0))
        e["maxlist"] = max(e["maxlist"], r["F_LIST"])
        e["maxsub"] = max(e["maxsub"], r["F_SUBSET"])
    res = dict(mode="allw", n=n, q=q, t=t, a=a, dmax=dmax, g=g,
               MAXWORD_SUB=maxsub, MAXWORD_LIST=rows[0]["F_LIST"] if rows else 1,
               n_items=sum(cnt.values()), n_cosets=len(cnt),
               PRODUCT_PRED=comb(n, a) // n if comb(n, a) % n == 0 else comb(n, a) / n,
               per_delta=per_delta, top=rows[:6])
    print(json.dumps(res, indent=1)[:4000])
    if out:
        with open(out, "w") as f:
            json.dump(res, f, indent=1)
    return res


if __name__ == "__main__":
    m = sys.argv[1]
    n, q, t = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    out = sys.argv[5] if len(sys.argv) > 5 else None
    if m == "prod":
        mode_prod(n, q, t, out)
    elif m == "allw":
        mode_allw(n, q, t, out)
    else:
        raise SystemExit("bad mode")
