#!/usr/bin/env python3
"""nf_probe: S2 — EXACT list counts for individual flank words at ANY q.

For a word class W (given as its reversed truncated series 1 + W_1 z + ... +
W_m z^m, m = t+delta) the exact list at agreement a = k+t is enumerated by
running over EVERY size-a subset A of D:

   A is admissible  <=>  W / L_A  mod z^(m+1)  is a polynomial of degree <= delta
   and then u := the monic degree-delta poly with rev(u) = that quotient,
   P := V_A * u,  f := Y - P  is the codeword.

F_LIST(W) = #distinct P ; F_SUBSET(W) = #admissible A. Works at any prime
q = 1 mod n (including q ~ 2^40), so this is the DEEPLY STARVED instrument.
Cost O(C(n,a) * (a*m + m^2)); usable at n = 8, 16.
"""
import json, random, sys
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
            if len({pow(g, i, q) for i in range(n)}) == n: return g
    raise RuntimeError

def smul(A, B, q, m):
    """truncated series product mod z^(m+1); A,B given as coeff lists 0..m."""
    out = [0]*(m+1)
    for i, x in enumerate(A):
        if x:
            for j, y in enumerate(B):
                if i+j > m: break
                out[i+j] = (out[i+j] + x*y) % q
    return out

def sinv(A, q, m):
    """inverse of a unit series (A[0] = 1) mod z^(m+1)."""
    r = [0]*(m+1); r[0] = 1
    for j in range(1, m+1):
        acc = 0
        for i in range(1, j+1):
            acc += A[i]*r[j-i]
        r[j] = (-acc) % q
    return r

def loc(pts, q, m):
    """L_S(z) = prod (1 - x z) mod z^(m+1)."""
    s = [0]*(m+1); s[0] = 1
    for x in pts:
        ns = s[:]
        for j in range(m, 0, -1):
            ns[j] = (s[j] - x*s[j-1]) % q
        s = ns
    return s

def polmul_lin(p, x, q):
    out = [0]*(len(p)+1)
    for i, c in enumerate(p):
        if c:
            out[i+1] = (out[i+1] + c) % q
            out[i] = (out[i] - c*x) % q
    return out

def plateau(n, k, s):
    M = 1
    while M <= k:
        if M > s and k % M == 0 and n % M == 0:
            N = n//M; h = k//M
            return M, (comb(N-1, h) if N-1 >= h else 0)
        M *= 2
    return 0, 0

def probe(n, q, t, delta, W, D, g, want_profile=True):
    """exact F_LIST / F_SUBSET for one word class W (series list len m+1)."""
    k = n//2; a = k+t; d = a+delta; m = t+delta
    Winv_ok = []
    seen = {}
    nA = 0
    coset_like = 0
    M, pl = plateau(n, k, m)
    Hset = None
    if M:
        step = n//M
        Hset = [frozenset((pow(g, j, q)*pow(g, step*i, q)) % q for i in range(M))
                for j in range(step)]
    for A in combinations(range(n), a):
        s = [0]*(m+1); s[0] = 1
        for i in A:
            x = D[i]
            for j in range(m, 0, -1):
                s[j] = (s[j] - x*s[j-1]) % q
        r = smul(W, sinv(s, q, m), q, m)
        ok = True
        for j in range(delta+1, m+1):
            if r[j]:
                ok = False; break
        if not ok: continue
        nA += 1
        # u: monic degree delta with rev(u) = r[0..delta]
        u = [r[delta-j] for j in range(delta+1)] if delta else [1]
        u[delta] = 1
        VA = [1]
        for i in A: VA = polmul_lin(VA, D[i], q)
        if delta == 0:
            P = VA
        else:
            P = [0]*(d+1)
            for i, c in enumerate(VA):
                if c:
                    for j, e in enumerate(u):
                        if e: P[i+j] = (P[i+j] + c*e) % q
        key = tuple(P)
        if key not in seen:
            nr = 0
            for x in D:
                acc = 0
                for c in reversed(P): acc = (acc*x + c) % q
                if acc == 0: nr += 1
            seen[key] = nr
        if Hset is not None:
            pts = {D[i] for i in A}
            used = [c for c in Hset if c <= pts]
            rest = set()
            for c in used: rest |= c
            if len(pts - rest) == t and len(used) == k//M:
                coset_like += 1
    prof = {}
    for v in seen.values(): prof[v] = prof.get(v, 0) + 1
    return dict(F_LIST=len(seen), F_SUBSET=nA,
                agreement_profile={str(x): y for x, y in sorted(prof.items())},
                coset_like_A=coset_like, plateau_M=M, plateau_pred=pl,
                subset_identity_ok=(sum(y*comb(x, a) for x, y in prof.items()) == nA))

def build_words(n, q, t, delta, D, g, seed=20260809, n_rand=6, n_plant=6, n_loc=6):
    k = n//2; a = k+t; m = t+delta
    rng = random.Random(seed)
    words = []
    # (a) structured at every dyadic scale M | k with t <= M
    M = 1
    while M <= k:
        if k % M == 0 and n % M == 0 and M > t:
            step = n//M
            H = [pow(g, step*i, q) for i in range(M)]
            T0 = H[:t]
            words.append(("struct_M%d" % M, loc(T0, q, m)))
            # prescribed quotient sum at scale M (the C1 flank freedom)
            if M <= m:
                for tag, v in (("e1=0", 0), ("e1=1", 1), ("e1=rand", rng.randrange(q))):
                    if v == 0: continue
                    fac = [0]*(m+1); fac[0] = 1; fac[M] = (-v) % q
                    words.append(("struct_M%d_%s" % (M, tag),
                                  smul(loc(T0, q, m), fac, q, m)))
        M *= 2
    # (b) locator words: W = L_S, |S| = j (words whose top part splits over D)
    for j in (1, min(m, 2), m):
        if j < 1 or j > m: continue
        for _ in range(n_loc):
            S = rng.sample(range(n), j)
            words.append(("locator_j%d" % j, loc([D[i] for i in S], q, m)))
    # (c) planted-hybrid: W = top part of V_B*u, |B| = a, u random monic deg delta
    for _ in range(n_plant):
        B = rng.sample(range(n), a)
        uh = [1] + [rng.randrange(q) for _ in range(delta)]
        words.append(("planted", smul(loc([D[i] for i in B], q, m), uh + [0]*(m-delta), q, m)))
    # (d) planted-hybrid at STRUCTURED B (giant-slack representative)
    M = 1
    while M <= k:
        if k % M == 0 and n % M == 0 and M > t:
            step = n//M
            H = [pow(g, step*i, q) for i in range(M)]
            T0 = H[:t]
            cos = [[(pow(g, j, q)*x) % q for x in H] for j in range(step)]
            B = list(T0)
            for j in range(1, k//M + 1): B += cos[j]
            if len(B) == a:
                for tag, uh in (("u=1", [1] + [0]*delta),
                                ("u=rand", [1] + [rng.randrange(q) for _ in range(delta)]),
                                ("u=loc", loc([D[i] for i in rng.sample(range(n), delta)], q, delta)
                                 if delta else [1])):
                    words.append(("planted_struct_M%d_%s" % (M, tag),
                                  smul(loc(B, q, m), list(uh) + [0]*(m-delta), q, m)))
        M *= 2
    # (e) two-structure hybrid: W = L_T0 * L_T0'
    if 2*t <= m:
        M = 1
        while M <= k:
            if k % M == 0 and n % M == 0 and M > t:
                step = n//M
                H = [pow(g, step*i, q) for i in range(M)]
                T0 = H[:t]
                Tp = [(pow(g, 1, q)*x) % q for x in H[:t]]
                words.append(("pair_struct_M%d" % M, smul(loc(T0, q, m), loc(Tp, q, m), q, m)))
            M *= 2
    # (f) random
    for _ in range(n_rand):
        words.append(("random", [1] + [rng.randrange(q) for _ in range(m)]))
    return words

def main():
    cfg = json.loads(sys.argv[1])
    out = []
    for c in cfg:
        n, q, t, delta = c["n"], c["q"], c["t"], c["delta"]
        g = find_gen(q, n); D = [pow(g, i, q) for i in range(n)]
        if c.get("locator_scan"):
            m = t+delta
            allS = list(combinations(range(n), m))
            lim = c["locator_scan"]
            if lim > 0 and len(allS) > lim:
                allS = random.Random(7).sample(allS, lim)
            words = [("locScan_%s" % ",".join(map(str, S)),
                      loc([D[i] for i in S], q, m)) for S in allS]
        elif "words" in c:
            words = [(w[0], [1] + list(w[1])) for w in c["words"]]
            if c.get("all_pair_locators"):
                for i in range(n):
                    for j in range(i+1, n):
                        words.append(("pairloc_%d_%d" % (i, j),
                                      loc([D[i], D[j]], q, t+delta)))
        else:
            words = build_words(n, q, t, delta, D, g, seed=c.get("seed", 20260809))
        for tag, W in words:
            r = probe(n, q, t, delta, W, D, g)
            r.update(n=n, q=q, t=t, delta=delta, word=tag,
                     starved=(q**t > comb(n, n//2+t)))
            out.append(r)
            print(json.dumps(r), flush=True)
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w") as f: json.dump(out, f, indent=1)

if __name__ == "__main__":
    main()
