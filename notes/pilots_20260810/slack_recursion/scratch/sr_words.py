#!/usr/bin/env python3
"""sr_words: the arbitrary-word (all-delta) supply instrument.

Framework (re-derived, see PREREG R0):  n = 2^r, D = mu_n < F_q, k = n/2,
t = 1, a = k+1, m = n-a = n/2-1 = |B| with B = D\\A.  A received word of
slack delta has word class W(z) (normalized reversed truncation, W_0 = 1)
and A is admissible iff

    [z^{delta+1}]( W(z) * l_B(z) ) = 0,   l_B(z) = prod_{b in B}(1 - b z).

F_SUBSET = # admissible A;  F_LIST = # distinct codewords, obtained by
deduplicating P = L_A * u where u is monic of degree delta with
rev(u) = (W * l_B) mod z^{delta+1}.  P is fingerprinted at NFP points
outside D via  P(x) = [(x^n - 1)/L_B(x)] * u(x).

Modes
  n8all   q1,q2,...        exhaustive over ALL words / ALL delta at n=8
  nloc    n q dmin,dmax    orbit-exhaustive LOCATOR ladder W = l_S, |S|=delta+1
  word    n q delta S      one explicit locator word (cross-check vs nf_probe)
"""
import json, sys
from itertools import combinations
from math import comb

NFP = 4
FPX = (2, 3, 5, 7)


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
    """IDENTICAL to the banked nf_probe/nf_maxscan find_gen (same D ordering)."""
    co = (q - 1) // n
    for g0 in range(2, 100000):
        g = pow(g0, co, q)
        if pow(g, n // 2, q) != 1 and pow(g, n, q) == 1:
            if len({pow(g, i, q) for i in range(n)}) == n:
                return g
    raise RuntimeError


def loc_coeffs(pts, q, top):
    """coefficients of prod (1 - x z) truncated to degree <= top."""
    s = [0] * (top + 1)
    s[0] = 1
    for x in pts:
        for j in range(min(top, len(pts)), 0, -1):
            s[j] = (s[j] - x * s[j - 1]) % q
    return s


# --------------------------------------------------------------- n=8, all words
def n8all(q, out=None):
    n, k = 8, 4
    a = k + 1                      # 5
    assert is_prime(q) and q % n == 1
    g = find_gen(q, n)
    D = [pow(g, i, q) for i in range(n)]
    dmax = n - 1 - a               # 2
    # all monic u of degree d <= dmax, as coefficient lists (low->high)
    us = []
    for d in range(dmax + 1):
        if d == 0:
            us.append((0, [1]))
            continue
        for co in range(q ** d):
            c = []
            x = co
            for _ in range(d):
                c.append(x % q)
                x //= q
            c.append(1)
            us.append((d, c))
    # all A, as monic L_A (low->high, degree a)
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
    # pass 1: F_SUBSET per coset key
    cnt = {}
    for A, LA in LAs:
        for d, u in us:
            P = [0] * (a + d + 1)
            for i, c in enumerate(LA):
                if c:
                    for j, e in enumerate(u):
                        if e:
                            P[i + j] = (P[i + j] + c * e) % q
            key = 0
            for j in range(n - 1, k - 1, -1):
                key = key * q + (P[j] if j < len(P) else 0)
            cnt[key] = cnt.get(key, 0) + 1
    maxsub = max(cnt.values())
    tau = 3
    hot = {key for key, c in cnt.items() if c >= tau}
    # pass 2: distinct P per hot key
    dist = {}
    for A, LA in LAs:
        for d, u in us:
            P = [0] * (a + d + 1)
            for i, c in enumerate(LA):
                if c:
                    for j, e in enumerate(u):
                        if e:
                            P[i + j] = (P[i + j] + c * e) % q
            key = 0
            for j in range(n - 1, k - 1, -1):
                key = key * q + (P[j] if j < len(P) else 0)
            if key in hot:
                dist.setdefault(key, {}).setdefault(tuple(P), 0)
                dist[key][tuple(P)] += 1
    best_list = 0
    best_key = None
    rows = []
    for key, dd in dist.items():
        fl = len(dd)
        fs = cnt[key]
        prof = {}
        for pp, mult in dd.items():
            j = None
            for jj in range(a, n):
                if comb(jj, a) == mult:
                    j = jj
                    break
            prof[str(j)] = prof.get(str(j), 0) + 1
        deg = max(i for i, c in enumerate(max(dd)) if c) if dd else 0
        delta = None
        for pp in dd:
            dg = max(i for i, c in enumerate(pp) if c)
            delta = dg - a
            break
        rows.append(dict(key=key, F_SUBSET=fs, F_LIST=fl, delta=delta,
                         profile=prof))
        if fl > best_list:
            best_list = fl
            best_key = key
    rows.sort(key=lambda r: (-r["F_LIST"], -r["F_SUBSET"]))
    submax_rows = sorted(rows, key=lambda r: -r["F_SUBSET"])[:6]
    per_delta = {}
    for r in rows:
        d = str(r["delta"])
        e = per_delta.setdefault(d, dict(maxlist=0, maxsub=0))
        e["maxlist"] = max(e["maxlist"], r["F_LIST"])
        e["maxsub"] = max(e["maxsub"], r["F_SUBSET"])
    res = dict(mode="n8all", n=n, q=q, g=g, a=a, dmax=dmax,
               n_cosets_hit=len(cnt), n_items=sum(cnt.values()),
               MAXWORD_SUB=maxsub, MAXWORD_LIST=best_list,
               PLATEAU=comb(n // 2 - 1, n // 4),
               C_nm1_a=comb(n - 1, a),
               tau=tau, top_by_list=rows[:8], top_by_subset=submax_rows,
               per_delta_over_hot=per_delta)
    print(json.dumps(res, indent=1))
    if out:
        with open(out, "w") as f:
            json.dump(res, f, indent=1)
    return res


# ------------------------------------------------------- n=16/32 locator ladder
def prep(n, q):
    a = n // 2 + 1
    m = n - a
    g = find_gen(q, n)
    D = [pow(g, i, q) for i in range(n)]
    Bs = list(combinations(range(n), m))
    cols = [[0] * len(Bs) for _ in range(m + 1)]
    fps = []
    xs = [x % q for x in FPX[:NFP]]
    xn = [(pow(x, n, q) - 1) % q for x in xs]
    for bi, B in enumerate(Bs):
        s = [0] * (m + 1)
        s[0] = 1
        ln = 0
        for i in B:
            x = D[i]
            ln += 1
            for j in range(min(ln, m), 0, -1):
                s[j] = (s[j] - x * s[j - 1]) % q
        for j in range(m + 1):
            cols[j][bi] = s[j]
        f = []
        for xi, x in enumerate(xs):
            lb = 1
            for i in B:
                lb = lb * (x - D[i]) % q
            f.append(xn[xi] * pow(lb, q - 2, q) % q)
        fps.append(f)
    return a, m, g, D, Bs, cols, fps, xs


def scan_word(W, delta, q, m, Bs, cols, fps, xs):
    """W: coeff list of the word class, len >= delta+2.  Returns (F_SUBSET,
    F_LIST, profile, mult histogram)."""
    NB = len(Bs)
    acc = [0] * NB
    for i in range(delta + 2):
        w = W[delta + 1 - i]
        if w:
            ci = cols[i]
            acc = [x + w * y for x, y in zip(acc, ci)]
    adm = [bi for bi in range(NB) if acc[bi] % q == 0]
    seen = {}
    for bi in adm:
        # u* = (W * l_B) mod z^{delta+1}
        us = []
        for j in range(delta + 1):
            s = 0
            for i in range(j + 1):
                s += W[j - i] * cols[i][bi]
            us.append(s % q)
        # u(X) = sum_i us[delta-i] X^i  -> Horner over reversed
        f = fps[bi]
        key = []
        for xi, x in enumerate(xs):
            v = 0
            for i in range(delta + 1):
                v = (v * x + us[i]) % q
            key.append(f[xi] * v % q)
        key = tuple(key)
        seen[key] = seen.get(key, 0) + 1
    prof = {}
    a = len(Bs[0]) and (len(cols) - 1)
    aa = None
    for mult in seen.values():
        prof[str(mult)] = prof.get(str(mult), 0) + 1
    return len(adm), len(seen), prof


def mult_to_agr(prof, a, n):
    out = {}
    for mult, cntv in prof.items():
        mm = int(mult)
        j = None
        for jj in range(a, n + 1):
            if comb(jj, a) == mm:
                j = jj
                break
        out[str(j) if j is not None else "mult%s" % mult] = cntv
    return out


def orbit_reps(n, j):
    reps = []
    for S in combinations(range(n), j):
        best = None
        for r in range(n):
            t = tuple(sorted((x + r) % n for x in S))
            if best is None or t < best:
                best = t
        if best == S:
            reps.append(S)
    return reps


def nloc(n, q, dmin, dmax, out=None):
    a, m, g, D, Bs, cols, fps, xs = prep(n, q)
    ladder = {}
    for delta in range(dmin, dmax + 1):
        j = delta + 1
        reps = orbit_reps(n, j)
        best = []
        for S in reps:
            W = loc_coeffs([D[i] for i in S], q, j)
            fs, fl, prof = scan_word(W, delta, q, m, Bs, cols, fps, xs)
            best.append((fl, fs, S, prof))
        best.sort(key=lambda r: (-r[0], -r[1]))
        bysub = sorted(best, key=lambda r: -r[1])
        ladder[str(delta)] = dict(
            delta=delta, n_orbits=len(reps),
            LOCLIST=best[0][0], LOCSUB=bysub[0][1],
            argmax_list=list(best[0][2]),
            prof_at_list_argmax=mult_to_agr(best[0][3], a, n),
            F_SUBSET_at_list_argmax=best[0][1],
            argmax_sub=list(bysub[0][2]),
            prof_at_sub_argmax=mult_to_agr(bysub[0][3], a, n),
            F_LIST_at_sub_argmax=bysub[0][0],
            top5_list=[[r[0], r[1], list(r[2])] for r in best[:5]])
        print(json.dumps(ladder[str(delta)]), flush=True)
        if out:
            with open(out, "w") as f:
                json.dump(dict(mode="nloc", n=n, q=q, g=g, a=a, m=m,
                               PLATEAU=comb(n // 2 - 1, n // 4),
                               ladder=ladder), f, indent=1)
    return ladder


def one_word(n, q, delta, S, out=None):
    a, m, g, D, Bs, cols, fps, xs = prep(n, q)
    W = loc_coeffs([D[i] for i in S], q, delta + 1)
    fs, fl, prof = scan_word(W, delta, q, m, Bs, cols, fps, xs)
    res = dict(mode="word", n=n, q=q, g=g, delta=delta, S=list(S),
               F_SUBSET=fs, F_LIST=fl, mult_hist=prof,
               agreement_profile=mult_to_agr(prof, a, n))
    print(json.dumps(res, indent=1))
    if out:
        with open(out, "w") as f:
            json.dump(res, f, indent=1)
    return res


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "n8all":
        qs = [int(x) for x in sys.argv[2].split(",")]
        res = []
        for q in qs:
            res.append(n8all(q, None))
            if len(sys.argv) > 3:
                with open(sys.argv[3], "w") as f:
                    json.dump(res, f, indent=1)
    elif mode == "nloc":
        nloc(int(sys.argv[2]), int(sys.argv[3]),
             int(sys.argv[4]), int(sys.argv[5]),
             sys.argv[6] if len(sys.argv) > 6 else None)
    elif mode == "word":
        one_word(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]),
                 tuple(int(x) for x in sys.argv[5].split(",")),
                 sys.argv[6] if len(sys.argv) > 6 else None)
    else:
        raise SystemExit("bad mode")
