#!/usr/bin/env python3
"""ms_strat: R3 -- stratified antipodal enumeration for the t=1, delta=1 maxscan.

Object (identical to the banked nf_maxscan complement form):
   F_SUBSET(n,q,alpha,beta) = #{B subset of mu_n, |B| = n/2-1 :
                                e2(B) + alpha*e1(B) + beta = 0}
   (banked coordinates: alpha = -W1, beta = W2)

Antipodal decomposition.  mu_n = disjoint union over j<M=n/2 of {z^j, -z^j}
with z = g a generator of order n and w = z^2 a primitive M-th root.
A subset B is (S, sigma, T):  S = pairs met once (with sign sigma_j = +-1),
T = pairs fully contained.  |S| + 2|T| = m = n/2 - 1.  With
   P = sum_{j in S} sigma_j z^j,  w_X = sum_{j in X} w^j
the exact identity is
   e1(B) = P,   e2(B) = (P^2 - w_S - 2 w_T)/2 .
Hence the scanned value  v := e2 + alpha*e1  satisfies
   v = (P^2 - w_S)/2 + alpha*P - w_T .
At alpha = 0 the value depends on sigma only through P^2, so sigma and
-sigma coincide: enumerate 2^(s-1) sign patterns and weight each by 2.

Cost: N = C(n, n/2-1) inner increments per alpha (N/2 at alpha=0).
RAM:  one dense counter array of length q (the whole point).

Modes:
  alpha0   n q            dense array over all beta at alpha=0
  strata   n q s1,s2,..   per-stratum exact fiber maxima (dict; small strata)
  fullscan n q            all alpha in F_q (dict per alpha) + heavy-alpha list
  alphas   n q a1,a2,..   dense array at each listed alpha
"""
import json, sys
from array import array
from itertools import combinations


def is_prime(m):
    if m < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % p == 0:
            return m == p
    dd, s = m - 1, 0
    while dd % 2 == 0:
        dd //= 2
        s += 1
    for A in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(A, dd, m)
        if x in (1, m - 1):
            continue
        for _ in range(s - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def find_gen(q, n):
    """IDENTICAL to the banked nf_maxscan.find_gen -- same D ordering."""
    co = (q - 1) // n
    for g0 in range(2, 100000):
        g = pow(g0, co, q)
        if pow(g, n // 2, q) != 1 and pow(g, n, q) == 1:
            if len({pow(g, i, q) for i in range(n)}) == n:
                return g
    raise RuntimeError


def setup(n, q):
    assert is_prime(q) and q % n == 1, (q, n)
    M = n // 2
    m = M - 1
    g = find_gen(q, n)
    assert pow(g, M, q) == q - 1
    Z = [pow(g, j, q) for j in range(M)]          # z^j, j < M
    W = [pow(g, 2 * j, q) for j in range(M)]      # w^j = z^(2j)
    inv2 = pow(2, q - 2, q)
    return M, m, g, Z, W, inv2


def signed_sums(zs, q, half):
    """All P = sum +-zs[i] mod q.  half=True -> fix the first sign to +."""
    out = [zs[0] % q]
    if not half:
        out.append((-zs[0]) % q)
    for z in zs[1:]:
        nxt = []
        for p in out:
            a = p + z
            if a >= q:
                a -= q
            b = p - z
            if b < 0:
                b += q
            nxt.append(a)
            nxt.append(b)
        out = nxt
    return out


def stratum_iter(M, m, s):
    """yield (S tuple, avail tuple, h) for |S| = s."""
    h = (m - s) // 2
    allidx = range(M)
    for S in combinations(allidx, s):
        sset = set(S)
        avail = tuple(j for j in allidx if j not in sset)
        yield S, avail, h


def tsums(avail, h, W, q):
    """all (-w_T) mod q for T subset of avail, |T| = h."""
    if h == 0:
        return [0]
    ws = [W[j] for j in avail]
    out = []
    ap = out.append
    for T in combinations(ws, h):
        ap((-sum(T)) % q)
    return out


def run_alpha(n, q, alpha, counter=None, report_top=40, only=None):
    """Exact F_SUBSET(n,q,alpha,.) for all beta.  Returns (max, argmax vs, tail)."""
    M, m, g, Z, W, inv2 = setup(n, q)
    half = (alpha == 0)
    A = counter if counter is not None else array('i', [0]) * q
    total = 0
    for s in range(1 if m % 2 else 0, m + 1, 2):
        if (m - s) % 2:
            continue
        if only is not None and s not in only:
            continue
        h = (m - s) // 2
        if h < 0 or s > M or h > M - s:
            continue
        for S, avail, hh in stratum_iter(M, m, s):
            wS = 0
            for j in S:
                wS += W[j]
            wS %= q
            NT = tsums(avail, hh, W, q)
            zs = [Z[j] for j in S]
            for P in signed_sums(zs, q, half):
                base = ((P * P - wS) * inv2 + alpha * P) % q
                for nt in NT:
                    v = base + nt
                    if v >= q:
                        v -= q
                    A[v] += 1
                total += len(NT)
    if half:
        total *= 2
    w = 2 if half else 1
    mx = 0
    tail = {}
    for v in range(q):
        c = A[v]
        if c:
            tail[c] = tail.get(c, 0) + 1
            if c > mx:
                mx = c
    args = [v for v in range(q) if A[v] == mx]
    tail = {k * w: vv for k, vv in tail.items()}
    run_alpha.at1 = A[1] * w
    return mx * w, args, tail, total


def mode_alpha0(n, q, out, only=None):
    M, m, g, Z, W, inv2 = setup(n, q)
    mx, args, tail, tot = run_alpha(n, q, 0, only=only)
    tailtop = {str(k): v for k, v in sorted(tail.items())}
    res = dict(mode="alpha0", n=n, q=q, m=m, g=g, only=sorted(only) if only else None,
               N_subsets=tot, mean_per_class=tot / q,
               MAXSCAN_0=mx, count_at_v1=run_alpha.at1, n_argmax_fibers=len(args),
               argmax_v=args[:32], argmax_W2=[(-v) % q for v in args[:32]],
               count_tail_top=tailtop,
               distinct_nonzero_fibers=sum(tail.values()))
    print(json.dumps(res, indent=1))
    if out:
        with open(out, "w") as f:
            json.dump(res, f, indent=1)


def mode_strata(n, q, slist, out):
    """Per-stratum exact fiber maxima at alpha=0 (dict-based; small strata)."""
    M, m, g, Z, W, inv2 = setup(n, q)
    res = {}
    for s in slist:
        h = (m - s) // 2
        cnt = {}
        tot = 0
        for S, avail, hh in stratum_iter(M, m, s):
            wS = sum(W[j] for j in S) % q
            NT = tsums(avail, hh, W, q)
            zs = [Z[j] for j in S]
            for P in signed_sums(zs, q, True):
                base = ((P * P - wS) * inv2) % q
                for nt in NT:
                    v = base + nt
                    if v >= q:
                        v -= q
                    cnt[v] = cnt.get(v, 0) + 1
                tot += len(NT)
        mx = max(cnt.values()) if cnt else 0
        args = [v for v, c in cnt.items() if c == mx]
        res[str(s)] = dict(s=s, h=h, subsets=tot * 2, STRAT_max=mx * 2,
                           n_argmax=len(args), argmax_v=sorted(args)[:16],
                           distinct=len(cnt))
    out_d = dict(mode="strata", n=n, q=q, m=m, strata=res)
    print(json.dumps(out_d, indent=1))
    if out:
        with open(out, "w") as f:
            json.dump(out_d, f, indent=1)


def mode_fullscan(n, q, out, heavy_thresh):
    """All alpha in F_q -- reproduces the banked per-W1 max histogram."""
    M, m, g, Z, W, inv2 = setup(n, q)
    # precompute per-S data once
    blocks = []
    for s in range(1 if m % 2 else 0, m + 1, 2):
        if (m - s) % 2:
            continue
        h = (m - s) // 2
        if h < 0 or s > M or h > M - s:
            continue
        for S, avail, hh in stratum_iter(M, m, s):
            wS = sum(W[j] for j in S) % q
            NT = tsums(avail, hh, W, q)
            zs = [Z[j] for j in S]
            Ps = signed_sums(zs, q, False)
            blocks.append((wS, NT, Ps))
    hist = {}
    heavy = []
    for W1 in range(q):
        alpha = (-W1) % q
        cnt = {}
        for wS, NT, Ps in blocks:
            for P in Ps:
                base = ((P * P - wS) * inv2 + alpha * P) % q
                for nt in NT:
                    v = base + nt
                    if v >= q:
                        v -= q
                    cnt[v] = cnt.get(v, 0) + 1
        mx = 0
        arg = 0
        for v, c in cnt.items():
            if c > mx:
                mx = c
                arg = v
        hist[mx] = hist.get(mx, 0) + 1
        if mx >= heavy_thresh:
            heavy.append([W1, alpha, mx, (-arg) % q])
    res = dict(mode="fullscan", n=n, q=q, g=g,
               per_W1_max_histogram={str(a): b for a, b in sorted(hist.items())},
               heavy_thresh=heavy_thresh, n_heavy=len(heavy), heavy=heavy)
    print(json.dumps(res, indent=1)[:4000])
    if out:
        with open(out, "w") as f:
            json.dump(res, f, indent=1)


def mode_alphas(n, q, alist, out):
    M, m, g, Z, W, inv2 = setup(n, q)
    res = []
    for alpha in alist:
        A = array('i', [0]) * q
        mx, args, tail, tot = run_alpha(n, q, alpha, counter=A)
        del A
        res.append(dict(alpha=alpha, W1=(-alpha) % q, maxcount=mx,
                        n_argmax=len(args), argmax_W2=[(-v) % q for v in args[:8]],
                        tail_top={str(k): v for k, v in sorted(tail.items())[-8:]}))
        print(json.dumps(res[-1]))
        sys.stdout.flush()
        if out:
            with open(out, "w") as f:
                json.dump(dict(mode="alphas", n=n, q=q, g=g, results=res), f, indent=1)


if __name__ == "__main__":
    mode = sys.argv[1]
    n = int(sys.argv[2])
    q = int(sys.argv[3])
    if mode == "alpha0":
        mode_alpha0(n, q, sys.argv[4] if len(sys.argv) > 4 else None)
    elif mode == "alpha0s":
        only = set(int(x) for x in sys.argv[4].split(","))
        mode_alpha0(n, q, sys.argv[5] if len(sys.argv) > 5 else None, only=only)
    elif mode == "strata":
        sl = [int(x) for x in sys.argv[4].split(",")]
        mode_strata(n, q, sl, sys.argv[5] if len(sys.argv) > 5 else None)
    elif mode == "fullscan":
        th = int(sys.argv[4])
        mode_fullscan(n, q, sys.argv[5] if len(sys.argv) > 5 else None, th)
    elif mode == "alphas":
        al = [int(x) for x in sys.argv[4].split(",")]
        mode_alphas(n, q, al, sys.argv[5] if len(sys.argv) > 5 else None)
    else:
        raise SystemExit("bad mode")
