#!/usr/bin/env python3
"""nf_stratum_census: S1 — EXHAUSTIVE flank census over whole degree strata.

Cell (n, k=n/2, q, t, delta):  a = k+t (agreement), d = a+delta (word degree).
A received word class W = its coefficient vector at degrees k..d, normalised
monic (scaling and adding codewords change nothing); there are exactly
K = q^(t+delta) classes.  delta = 0 IS the polynomial side (the banked fiber
reduction's exact hypothesis); delta >= 1 IS the flank.

F_LIST(W) = #{codewords f with agreement >= a} = #{P monic of degree d, top
part W, with >= a roots in D}.  Enumerated exactly as P = V_A * u over all
|A| = a subsets of D and all monic u of degree delta, deduplicated by P.

F_SUBSET(W) = #(A,u) pairs = the fiber-analogue SUBSET count (what the banked
instrument counts); F_SUBSET >= F_LIST with equality iff every member has
agreement exactly a.

Model of record (registered): total distinct P over the whole stratum must equal
   sum_{i=a}^{min(n,d)} (-1)^(i-a) C(i-1,a-1) C(n,i) q^(d-i)
and the per-class mean is that divided by q^(t+delta) -- registered to be
delta-independent up to the min(n,d) truncation.
"""
import json, sys
from itertools import combinations
from math import comb

def is_prime(m):
    if m < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if m % p == 0: return m == p
    dd, s = m-1, 0
    while dd % 2 == 0: dd //= 2; s += 1
    for A in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(A, dd, m)
        if x in (1, m-1): continue
        for _ in range(s-1):
            x = x*x % m
            if x == m-1: break
        else: return False
    return True

def find_gen(q, n):
    co = (q-1)//n
    for g0 in range(2, 100000):
        g = pow(g0, co, q)
        if pow(g, n//2, q) != 1 and pow(g, n, q) == 1:
            pts = {pow(g, i, q) for i in range(n)}
            if len(pts) == n: return g
    raise RuntimeError("no order-n element")

def monic_polys(q, deg):
    """all monic polynomials of degree deg, as coefficient lists low->high."""
    if deg == 0:
        yield [1]; return
    idx = [0]*deg
    while True:
        yield idx[:] + [1]
        i = 0
        while i < deg:
            idx[i] += 1
            if idx[i] < q: break
            idx[i] = 0; i += 1
        if i == deg: return

def plateau(n, k, s):
    """C(n/M - 1, k/M) at the finest dyadic M | k with M > s (0 if none)."""
    M = 1
    best = 0
    while M <= k:
        if M > s and k % M == 0 and n % M == 0:
            N = n//M; h = k//M
            if N-1 >= h: best = comb(N-1, h)
            else: best = 0
            return M, best
        M *= 2
    return 0, 0

def structured_coset(n, k, q, t, delta, D, g):
    """coset key of the structured flank word X^(k+delta) L_T0, T0 in the
    order-M subgroup, M = finest dyadic > t+delta.  Returns (key, M, count)."""
    M, pl = plateau(n, k, t+delta)
    if M == 0 or pl == 0: return None, M, pl
    h = k//M
    step = n//M
    H = [pow(g, step*i, q) for i in range(M)]      # order-M subgroup
    if t > M: return None, M, pl
    T0 = H[:t]
    # A = T0 union h cosets of H other than H itself
    cosets = [[(pow(g, j, q)*x) % q for x in H] for j in range(step)]
    A = list(T0)
    for j in range(1, h+1):
        A += cosets[j]
    if len(A) != k+t: return None, M, pl
    VA = [1]
    for x in A:
        VA = polmul_lin(VA, x, q)
    P = [0]*delta + VA
    key = 0
    for j in range(t+delta-1, -1, -1):
        key = key*q + P[k+j]
    return key, M, pl

def polmul_lin(p, x, q):
    """p * (X - x)"""
    out = [0]*(len(p)+1)
    for i, c in enumerate(p):
        if c:
            out[i+1] = (out[i+1] + c) % q
            out[i] = (out[i] - c*x) % q
    return out

def bpois(K, mu, thresh=0.05):
    """least l with K*P(Poisson(mu) >= l) <= thresh (registered B_pois)."""
    from math import exp
    if mu <= 0: return 0
    # survival by direct summation with log-safe terms
    l = 0
    while l < 4000:
        # P(X >= l) = 1 - sum_{j<l} e^-mu mu^j/j!
        term = exp(-mu) if mu < 700 else 0.0
        cum = 0.0
        tj = term
        for j in range(l):
            cum += tj
            tj = tj*mu/(j+1)
        surv = max(0.0, 1.0-cum)
        if K*surv <= thresh: return l
        l += 1
    return -1

def run_cell(n, q, t, delta, pair_cap=3_000_000, want_argmax_detail=True):
    k = n//2; a = k+t; d = a+delta
    pairs = comb(n, a) * q**delta
    if pairs > 600_000: want_argmax_detail = False
    if pairs > pair_cap:
        return dict(n=n, q=q, t=t, delta=delta, skipped="pair_cap", pairs=pairs)
    g = find_gen(q, n)
    D = [pow(g, i, q) for i in range(n)]
    K = q**(t+delta)
    us = list(monic_polys(q, delta))
    qk = q**k
    seen = set()
    phi = {}
    Lc = {}
    for A in combinations(range(n), a):
        VA = [1]
        for i in A:
            VA = polmul_lin(VA, D[i], q)
        for u in us:
            if delta == 0:
                P = VA
            else:
                P = [0]*(d+1)
                for i, c in enumerate(VA):
                    if c:
                        for j, e in enumerate(u):
                            if e:
                                P[i+j] = (P[i+j] + c*e) % q
            ck = 0
            for j in range(t+delta-1, -1, -1):
                ck = ck*q + P[k+j]
            lw = 0
            for j in range(k-1, -1, -1):
                lw = lw*q + P[j]
            phi[ck] = phi.get(ck, 0) + 1
            full = ck*qk + lw
            if full not in seen:
                seen.add(full)
                Lc[ck] = Lc.get(ck, 0) + 1
    total_P = len(seen)
    model = 0
    for i in range(a, min(n, d)+1):
        model += (-1)**(i-a) * comb(i-1, a-1) * comb(n, i) * q**(d-i)
    hist = {}
    for v in Lc.values():
        hist[v] = hist.get(v, 0) + 1
    hist[0] = K - len(Lc)
    maxL = max(Lc.values()) if Lc else 0
    argmaxes = [c for c, v in Lc.items() if v == maxL]
    phimax = max(phi.values()) if phi else 0
    M, pl = plateau(n, k, t+delta)
    sk, _, _ = structured_coset(n, k, q, t, delta, D, g)
    out = dict(n=n, k=k, q=q, t=t, delta=delta, a=a, d=d, K=K,
               pairs=pairs, total_distinct_P=total_P, model_total=model,
               model_ok=(total_P == model),
               mean_measured=total_P/K, hist={str(x): y for x, y in sorted(hist.items())},
               F_MAX=maxL, n_argmax=len(argmaxes),
               F_SUBSET_MAX=phimax,
               plateau_M=M, plateau_pred=pl,
               structured_key_found=(sk is not None),
               structured_L=(Lc.get(sk, 0) if sk is not None else None),
               structured_PHI=(phi.get(sk, 0) if sk is not None else None),
               starved=(q**t > comb(n, a)),
               B_pois=bpois(K, total_P/K))
    if want_argmax_detail and argmaxes and maxL > 1:
        ck0 = argmaxes[0]
        prof = {}
        for A in combinations(range(n), a):
            VA = [1]
            for i in A:
                VA = polmul_lin(VA, D[i], q)
            for u in us:
                if delta == 0: P = VA
                else:
                    P = [0]*(d+1)
                    for i, c in enumerate(VA):
                        if c:
                            for j, e in enumerate(u):
                                if e: P[i+j] = (P[i+j] + c*e) % q
                ck = 0
                for j in range(t+delta-1, -1, -1): ck = ck*q + P[k+j]
                if ck != ck0: continue
                lw = 0
                for j in range(k-1, -1, -1): lw = lw*q + P[j]
                key = (ck, lw)
                if key in prof: continue
                nroots = 0
                for x in D:
                    acc = 0
                    for c in reversed(P): acc = (acc*x + c) % q
                    if acc == 0: nroots += 1
                prof[key] = nroots
        agr = {}
        for v in prof.values(): agr[v] = agr.get(v, 0) + 1
        out["argmax_agreement_profile"] = {str(x): y for x, y in sorted(agr.items())}
        out["argmax_is_structured"] = (ck0 == sk)
        out["argmax_subset_identity_ok"] = (
            sum(y*comb(x, a) for x, y in [(int(i), j) for i, j in out["argmax_agreement_profile"].items()])
            == phi[ck0])
    return out

def main():
    cells = json.loads(sys.argv[1]) if len(sys.argv) > 1 else []
    res = []
    for c in cells:
        r = run_cell(**c)
        res.append(r)
        print(json.dumps(r), flush=True)
    outp = sys.argv[2] if len(sys.argv) > 2 else None
    if outp:
        with open(outp, "w") as f: json.dump(res, f, indent=1)

if __name__ == "__main__":
    main()
