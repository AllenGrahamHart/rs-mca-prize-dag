"""D3: EXACT max list profile F_LMAX at scaled rate-1/2 RS rows, and its
per-step decay F_DECAY, by a q-INDEPENDENT algorithm.

F_LMAX(n_s,q,a) = max_U #{c in C : agreement(U,c) >= a}
                = max over cosets V of F[X]_{<K} in F[X]_{<n_s} of
                  #{f in V : f has >= a roots in D}.

Every such f factors uniquely as f = P_S * h with S = its exact root set in
D (|S| = j >= a) and h nonvanishing on D\S.  For fixed S the map h |-> key
(= the coefficients of f in degrees K..n_s-1) is LINEAR, so the reachable
keys from S form the column space Im(M_S).  The maximum is therefore
attained on some subspace in the intersection-closure of {Im(M_S)}, and can
be read off by evaluating one representative per closure element -- a cost
that does not grow with q.

Controls: lambda_FM = C(n_s,a) q^(K-a) (first-moment MEAN list size) and a
random-key sample.  BOTH ARE ZERO-POWER (F3) and never enter the verdict.
"""
import math
import random
from math import comb, isqrt
from itertools import combinations

import ffield as ff


def build(n_s, K, q, a):
    D = ff.subgroup(n_s, q)
    items = []                                  # (S, M_S rows, Im)
    R = n_s - K                                 # key length
    for j in range(a, n_s):
        for S in combinations(range(n_s), j):
            PS = ff.poly_from_roots([D[i] for i in S], q)
            nh = n_s - j                        # #coeffs of h
            rows = []
            for t in range(R):                  # degree K+t
                deg = K + t
                rows.append([PS[deg - i] if 0 <= deg - i <= j else 0
                             for i in range(nh)])
            Im = ff.colspace(rows, R, nh, q)
            out = [D[i] for i in range(n_s) if i not in S]
            items.append((S, rows, nh, Im, out))
    return D, items, R


def count_at(items, v, q, nunk_cap=4):
    """exact L(key=v): number of distinct root-rich f in that coset"""
    tot = 0
    for (S, rows, nh, Im, out) in items:
        sol = ff.solve(rows, v, nh, q)
        if sol is None:
            continue
        part, null = sol
        if not null:
            cands = [part]
        else:
            if len(null) > nunk_cap or q ** len(null) > 200000:
                return None                     # refuse to guess
            cands = []
            for k in range(q ** len(null)):
                x = part[:]
                kk = k
                for b in null:
                    c = kk % q
                    kk //= q
                    if c:
                        x = [(xi + c * bi) % q for xi, bi in zip(x, b)]
                cands.append(x)
        for h in cands:
            if not any(h):
                continue
            ok = True
            for x in out:
                if ff.poly_eval(h, x, q) == 0:
                    ok = False
                    break
            if ok:
                tot += 1
    return tot


def lmax_closure(n_s, K, q, a, cap=40000):
    D, items, R = build(n_s, K, q, a)
    seen = set()
    frontier = []
    for (_, _, _, Im, _) in items:
        if Im and Im not in seen:
            seen.add(Im)
            frontier.append(Im)
    closure = list(frontier)
    while frontier:
        nxt = []
        for i in range(len(closure)):
            for W in frontier:
                Z = ff.intersect(closure[i], W, R, q)
                if Z and Z not in seen:
                    seen.add(Z)
                    nxt.append(Z)
                    if len(seen) > cap:
                        return None, None, len(seen)
        closure += nxt
        frontier = nxt
    best, arg = 0, None
    for W in closure:
        v = list(W[0])
        c = count_at(items, v, q)
        if c is None:
            return None, None, len(closure)
        if c > best:
            best, arg = c, v
    return best, arg, len(closure)


def lmax_direct(n_s, K, q, a):
    """brute-force cross-check: enumerate every root-rich f once"""
    D = ff.subgroup(n_s, q)
    hist = {}
    for j in range(a, n_s):
        for S in combinations(range(n_s), j):
            PS = ff.poly_from_roots([D[i] for i in S], q)
            out = [D[i] for i in range(n_s) if i not in S]
            nh = n_s - j
            for code in range(q ** nh):
                h, kk = [], code
                for _ in range(nh):
                    h.append(kk % q)
                    kk //= q
                if not any(h):
                    continue
                if any(ff.poly_eval(h, x, q) == 0 for x in out):
                    continue
                f = [0] * (n_s + 1)
                for i, c1 in enumerate(PS):
                    if c1:
                        for t, c2 in enumerate(h):
                            if c2:
                                f[i + t] = (f[i + t] + c1 * c2) % q
                key = tuple(f[K:n_s])
                hist[key] = hist.get(key, 0) + 1
    hist.pop(tuple([0] * (n_s - K)), None)
    return (max(hist.values()) if hist else 0), hist


def rword_control(n_s, K, q, a, items, trials=400, seed=11):
    rnd = random.Random(seed)
    R = n_s - K
    tot, mx = 0, 0
    for _ in range(trials):
        v = [rnd.randrange(q) for _ in range(R)]
        if not any(v):
            continue
        c = count_at(items, v, q)
        if c is None:
            return None, None
        tot += c
        mx = max(mx, c)
    return tot / trials, mx


if __name__ == "__main__":
    n_s, K = 8, 4
    print("=== VALIDATION: closure algorithm vs direct enumeration (n_s=8) ===", flush=True)
    for q in (17,):
        for a in (5, 6, 7):
            d, _ = lmax_direct(n_s, K, q, a)
            c, arg, ncl = lmax_closure(n_s, K, q, a)
            print(f"  q={q:<4} a={a}: direct={d:<5} closure={c:<5} "
                  f"agree={d == c}  (closure size {ncl})", flush=True)

    print()
    print("=== F_LMAX / F_DECAY ladder, n_s=8, K=4, rate 1/2 ===", flush=True)
    print(f"{'q':>12} {'log2q':>7} {'B_s':>8} {'a':>3} {'tau':>4} {'F_LMAX':>8} "
          f"{'lam_FM':>10} {'safe?':>6} {'F_DECAY':>8} {'/log2q':>8}")
    qs = [17, 41, 97, 257, 65537, 16777289, 1073741857]
    summary = {}
    for q in qs:
        if (q - 1) % n_s:
            continue
        Bs = isqrt(q)
        vals = {}
        for a in range(K + 1, n_s):
            v, arg, ncl = lmax_closure(n_s, K, q, a)
            vals[a] = v
        vals[n_s] = 1
        for a in range(K + 1, n_s + 1):
            v = vals[a]
            lam = comb(n_s, a) * (q ** (K - a)) if a <= K else comb(n_s, a) / q ** (a - K)
            dec = (math.log2(vals[a]) - math.log2(vals[a + 1])) if a + 1 in vals and vals[a + 1] else float('nan')
            print(f"{q:>12} {math.log2(q):>7.2f} {Bs:>8} {a:>3} {a-K:>4} {v:>8} "
                  f"{lam:>10.4g} {str(v <= Bs):>6} {dec:>8.3f} "
                  f"{dec/math.log2(q) if dec == dec else float('nan'):>8.3f}")
        sig = 0
        for a in range(K + 1, n_s + 1):
            if vals[a] > Bs:
                sig = a - K
        summary[q] = (Bs, dict(vals), sig)
        print()

    print("=== crossing ladder (n_s=8): sigma_L = max{sigma : F_LMAX(K+sigma) > B_s} ===")
    print(f"{'q':>12} {'log2q':>7} {'B_s':>8} {'sigma_L':>8} {'tau_FM=n/log2q':>15} "
          f"{'rho_S':>8} {'tau_lo=2n/log2q':>16} {'tau_hi=n/4':>11}")
    for q in qs:
        if (q - 1) % n_s:
            continue
        Bs, vals, sig = summary[q]
        tfm = n_s / math.log2(q)
        print(f"{q:>12} {math.log2(q):>7.2f} {Bs:>8} {sig:>8} {tfm:>15.4f} "
              f"{sig/tfm:>8.4f} {2*tfm:>16.4f} {n_s/4:>11.2f}")

    print()
    print("=== CONTROL (ZERO POWER, F3): random-key list sizes, n_s=8 ===")
    for q in (17, 257, 65537):
        D, items, R = build(n_s, K, q, 5)
        mean, mx = rword_control(n_s, K, q, 5, items)
        print(f"  q={q:<8} a=5: random-key mean L = {mean:.4f}, sampled max = {mx}, "
              f"exact max = {summary[q][1][5]}")
