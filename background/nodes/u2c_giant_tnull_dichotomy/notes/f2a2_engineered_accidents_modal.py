#!/usr/bin/env python3
"""F2-A2 (floor campaign, Modal): ENGINEERED sub-balance accidents — the
adversarial second family against the u2c EXTRAS-BUDGET floor.

The F2-A1 sweep sampled natural primes (extras identically zero in
sub-balance). This attack SELECTS primes the way Pro's dli round-5 attack
selected them: for a candidate block S ⊆ Z/N (b exponents), the t
conditions p_r(S) = Σ_{i∈S} ω^{ir} ≡ 0 (r = 1..t) hold at a prime p iff
the corresponding prime ideals divide the P_r(z) = Σ_i z^{ir mod N}
(reduced in Z[z]/(z^{N/2}+1), power-of-two N — the dli norm-gate
machinery transports verbatim). ENGINEERING: compute per-r norms
|Res(x^{N/2}+1, P_r)|, take g = gcd over r (the multi-condition
coincidence filter — the E2 lesson: generically these are coprime, so
hits are rare and structural), extract admissible factors p ≡ 1 (mod N),
and for each verify directly whether a COMMON embedding makes S t-null;
classify hits (coset-union? sub-balance?).

PRE-REGISTERED: the floor is attacked only by NON-coset-union t-null
blocks at SUB-balance primes (C(N,b) < p^t) in counts beyond the
transported budget story. Window-regime hits and coset-union hits do not
fire. Zero engineered sub-balance accidents at ~3000 candidates = strong
survival evidence for the engineered family (the selection mechanism
itself comes up empty, mirroring E2's coprime-ideals finding).
"""
import json
import random
from pathlib import Path

import modal

app = modal.App("rs-mca-f2a2-engineered")
image = modal.Image.debian_slim()

CELLS = [(32, 2, 6), (64, 3, 8)]
TRIALS_PER_SHARD = 60
SHARDS_PER_CELL = 12


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def engineer_shard(payload):
    import itertools
    import math
    from fractions import Fraction
    N, t, b, seed = payload
    M = N // 2                     # work in Z[z]/(z^M + 1)
    rng = random.Random(seed)

    def reduce_poly(exps):
        co = [0] * M
        for e in exps:
            e %= N
            if e >= M:
                co[e - M] -= 1
            else:
                co[e] += 1
        return co

    def resultant(f, g):
        f = [Fraction(c) for c in f]
        g = [Fraction(c) for c in g]
        def deg(p):
            d = len(p) - 1
            while d >= 0 and p[d] == 0:
                d -= 1
            return d
        res = Fraction(1)
        F, G = f, g
        while True:
            dF, dG = deg(F), deg(G)
            if dG < 0:
                return 0
            if dG == 0:
                return res * G[0] ** dF
            R = F[:]
            while deg(R) >= dG:
                dR = deg(R)
                c = R[dR] / G[dG]
                for i in range(dG + 1):
                    R[dR - dG + i] -= c * G[i]
            dR = deg(R)
            res *= G[dG] ** (dF - max(dR, 0)) * (-1) ** (dF * dG)
            if dR < 0:
                return 0
            F, G = G, R[:dR + 1]

    xM1 = [1] + [0] * (M - 1) + [1]

    def is_prime(m):
        if m < 2:
            return False
        if m % 2 == 0:
            return m == 2
        d, s = m - 1, 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            if a % m == 0:
                continue
            x = pow(a, d, m)
            if x in (1, m - 1):
                continue
            for _ in range(s - 1):
                x = x * x % m
                if x == m - 1:
                    break
            else:
                return False
        return True

    def small_factors(g, cap=10**7):
        out = []
        d = 2
        gg = g
        while d * d <= gg and d < cap:
            while gg % d == 0:
                out.append(d)
                gg //= d
            d += 1
        if gg > 1 and gg < cap**2 and is_prime(gg):
            out.append(gg)
        return out

    hits = []
    n_cand_primes = 0
    for _ in range(TRIALS_PER_SHARD):
        S = tuple(sorted(rng.sample(range(N), b)))
        norms = []
        skip = False
        for r in range(1, t + 1):
            P = reduce_poly([i * r for i in S])
            if not any(P):
                skip = True   # identically zero in the ring (coset structure)
                break
            norms.append(abs(int(resultant(xM1, P))))
        if skip or any(nm == 0 for nm in norms):
            continue
        g = norms[0]
        for nm in norms[1:]:
            g = math.gcd(g, nm)
        if g <= 1:
            continue
        for p in set(small_factors(g)):
            if p % N != 1 or p < 2 * N:
                continue
            # sub-balance test
            if math.comb(N, b) >= p**t:
                continue
            n_cand_primes += 1
            # verify a COMMON embedding: some omega of order N kills all r
            # find generator of mu_N
            n0 = p - 1
            fs = set()
            dd = 2
            while dd * dd <= n0:
                while n0 % dd == 0:
                    fs.add(dd)
                    n0 //= dd
                dd += 1
            if n0 > 1:
                fs.add(n0)
            gen = 2
            while any(pow(gen, (p - 1) // f, p) == 1 for f in fs):
                gen += 1
            zN = pow(gen, (p - 1) // N, p)
            for a in range(1, N, 2):    # all order-N embeddings
                w = pow(zN, a, p)
                if all(sum(pow(w, (i * r) % N, p) for i in S) % p == 0
                       for r in range(1, t + 1)):
                    # coset-union check
                    rem = set(S)
                    ch = True
                    while ch and rem:
                        ch = False
                        for Mc in [m for m in range(2, N + 1) if N % m == 0]:
                            step = N // Mc
                            for j in range(step):
                                cos = set(range(j, N, step))
                                if cos <= rem and len(cos) == Mc:
                                    rem -= cos
                                    ch = True
                    hits.append({"S": list(S), "p": p, "embedding_exp": a,
                                 "is_coset_union": not rem,
                                 "log2W": round(math.log2(math.comb(N, b) / p**t), 2)})
                    break
    return {"N": N, "t": t, "b": b, "trials": TRIALS_PER_SHARD,
            "candidate_subbalance_primes": n_cand_primes, "hits": hits}


@app.local_entrypoint()
def main():
    payloads = []
    for i, (N, t, b) in enumerate(CELLS):
        for s in range(SHARDS_PER_CELL):
            payloads.append((N, t, b, 907 * (i + 1) + s))
    results = [r for r in engineer_shard.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    agg = {}
    for r in results:
        key = (r["N"], r["t"], r["b"])
        a = agg.setdefault(key, {"trials": 0, "cands": 0, "hits": []})
        a["trials"] += r["trials"]
        a["cands"] += r["candidate_subbalance_primes"]
        a["hits"] += r["hits"]
    for (N, t, b), a in sorted(agg.items()):
        noncoset = [h for h in a["hits"] if not h["is_coset_union"]]
        print(f"cell N={N} t={t} b={b}: trials={a['trials']} "
              f"cand-subbalance-primes={a['cands']} verified-hits={len(a['hits'])} "
              f"NON-COSET SUB-BALANCE ACCIDENTS={len(noncoset)}")
        for h in noncoset[:4]:
            print("   ENGINEERED ACCIDENT:", h)
    with open("/tmp/f2a2_results.json", "w") as f:
        json.dump({"cells": {str(k): v for k, v in agg.items()}}, f, indent=1)
