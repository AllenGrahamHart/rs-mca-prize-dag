#!/usr/bin/env python3
"""F2 campaign L1 (Modal): Fourier spectrum of the t-null moment map
at the calibration family. FALSIFICATION-FIRST per F2_FLIP_GOAL.md.

Objects (t = 2, D = mu_n in F_q, q prime, n | q-1):
  Phi(S) = (p1(S), p2(S)), weight-b slice; census N(s).
  For lambda = (l1, l2) in F_q^2: f_l(x) = l1 x + l2 x^2,
  E_b(lambda) = sum_{|S|=b} psi(sum_{x in S} f_l(x))
              = e_b( (psi(f_l(x)))_{x in D} )      [product-poly DP]
  Inversion: N(0) = q^{-2} sum_lambda E_b(lambda).

Arc classes (t=2): TRIVIAL (0,0); QUOTIENT (l1=0: f factors through
squaring, mu_n -> mu_{n/2} double cover); LINEAR (l2=0: value set a
rotated copy of mu_n — group-orbit arc); GENERIC (both nonzero) with
exact collision invariant kappa(c) = #{pairs {x,y} in mu_n : x+y = c},
c = -l1/l2 (the only collision chord; includes the Chebyshev locus
x + x^{-1} at inverse-symmetric pairs).

GATES (any failure refutes the packet):
  G1 exact inversion: |q^{-2} sum E_b - N0_DP| < max(0.5, 1e-6 N0_DP),
     N0_DP by exact integer DP over (p1, p2).
  G2 classification totals partition q^2.
  G3 GENERIC collision law: for sampled generic lambda, the number of
     distinct f_l values equals n - kappa(-l1/l2) exactly.

PRE-REGISTERED FALSIFIER (kill criterion, immutable): at the common
sub-balance cell b = 3, if max over GENERIC lambda of
r = |E_b|/sqrt(C(n,b)) exceeds R* = 32 at ALL THREE scales
q = 97, 193, 257 (n = 32), the L1 falsifier FIRES: branch (b) as posed
is refuted (persistent non-algebraic Fourier mass); bank and re-pose
per T-FLOOR logic. Otherwise the spectrum profile feeds L2.
"""
import cmath
import json
import math
from math import comb

import modal

app = modal.App("rs-mca-f2-l1-fourier")
image = modal.Image.debian_slim()

# (q, n, b) cells: three field scales at n = 32, window-spanning b;
# plus a domain-size contrast at n = 16.
JOBS = [(97, 32, 3), (97, 32, 4), (97, 32, 5), (97, 32, 6),
        (193, 32, 3), (193, 32, 4), (193, 32, 5), (193, 32, 6),
        (257, 32, 3), (257, 32, 4), (257, 32, 5), (257, 32, 6),
        (97, 16, 3), (97, 16, 4)]

R_STAR = 32.0   # pre-registered kill threshold (immutable)


@app.function(image=image, cpu=2, memory=2048, timeout=280)
def cell(job):
    q, n, b = job
    # domain mu_n
    def pf(x):
        out, d = [], 2
        while d * d <= x:
            while x % d == 0:
                out.append(d); x //= d
            d += 1
        if x > 1:
            out.append(x)
        return out
    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1 for r in set(pf(q - 1))))
    h = pow(g, (q - 1) // n, q)
    D = sorted(pow(h, i, q) for i in range(n))
    assert len(set(D)) == n

    # --- exact integer DP census N(0) over (p1, p2), weights 0..b ---
    dp = {(0, 0): [1] + [0] * b}
    for x in D:
        x2 = x * x % q
        new = {}
        for (a1, a2), vec in dp.items():
            tgt = new.setdefault((a1, a2), [0] * (b + 1))
            for w in range(b + 1):
                tgt[w] += vec[w]
            k1, k2 = (a1 + x) % q, (a2 + x2) % q
            tgt2 = new.setdefault((k1, k2), [0] * (b + 1))
            for w in range(b):
                if vec[w]:
                    tgt2[w + 1] += vec[w]
        dp = new
    N0 = dp.get((0, 0), [0] * (b + 1))[b]
    total = sum(vec[b] for vec in dp.values())
    assert total == comb(n, b)

    # --- coset-union context count: unions of pairwise-DISJOINT full
    #     mu_M cosets (M | n, 3 <= M <= b so p1 = p2 = 0), exact
    #     enumeration with real disjointness checks (cross-M cosets
    #     CAN intersect; do not assume) ---
    all_cosets = []
    for M in (M for M in range(3, b + 1) if n % M == 0):
        hM = pow(h, n // M, q)
        base = sorted(pow(hM, i, q) for i in range(M))
        seen = set()
        for c0 in D:
            cs = frozenset(c0 * x % q for x in base)
            if cs not in seen:
                seen.add(cs)
                all_cosets.append(cs)
    def enum(idx, used, rem):
        if rem == 0:
            return 1
        tot = 0
        for i in range(idx, len(all_cosets)):
            cs = all_cosets[i]
            if len(cs) <= rem and not (cs & used):
                tot += enum(i + 1, used | cs, rem - len(cs))
        return tot
    cu = enum(0, frozenset(), b)

    # --- Fourier spectrum ---
    two_pi_q = 2 * math.pi / q
    # precompute psi table
    psi = [cmath.exp(1j * two_pi_q * v) for v in range(q)]
    sqrt_flat = math.sqrt(comb(n, b))
    inv_sum = 0.0 + 0.0j
    prof = {"TRIVIAL": [], "QUOTIENT": [], "LINEAR": [], "GENERIC": []}
    top_generic = []
    # kappa table: for each c, #pairs {x,y} subset mu_n, x != y, x+y=c
    kappa = [0] * q
    Dset = set(D)
    for i, x in enumerate(D):
        for y in D[i + 1:]:
            kappa[(x + y) % q] += 1
    for l1 in range(q):
        for l2 in range(q):
            # e_b via truncated product poly
            coef = [0j] * (b + 1)
            coef[0] = 1.0 + 0j
            for x in D:
                w = psi[(l1 * x + l2 * x * x) % q]
                for d in range(b - 1, -1, -1):
                    if coef[d] != 0:
                        coef[d + 1] += coef[d] * w
            E = coef[b]
            inv_sum += E
            r = abs(E) / sqrt_flat
            if l1 == 0 and l2 == 0:
                prof["TRIVIAL"].append(r)
            elif l1 == 0:
                prof["QUOTIENT"].append(r)
            elif l2 == 0:
                prof["LINEAR"].append(r)
            else:
                prof["GENERIC"].append(r)
                c = (-l1 * pow(l2, q - 2, q)) % q
                top_generic.append((r, kappa[c]))
    # G1 inversion gate
    inv_N0 = inv_sum.real / (q * q)
    assert abs(inv_sum.imag) / (q * q) < 1e-4, ("imag leak", inv_sum.imag)
    assert abs(inv_N0 - N0) < max(0.5, 1e-6 * N0), \
        ("G1 inversion FAILED", inv_N0, N0)
    # G2 partition gate
    assert sum(len(v) for v in prof.values()) == q * q
    # G3 collision-law gate on 25 sampled generic lambdas
    import random as _r
    rng = _r.Random(1009)
    for _ in range(25):
        l1 = rng.randrange(1, q); l2 = rng.randrange(1, q)
        vals = {(l1 * x + l2 * x * x) % q for x in D}
        c = (-l1 * pow(l2, q - 2, q)) % q
        assert len(vals) == n - kappa[c], ("G3 collision law FAILED", l1, l2)

    top_generic.sort(reverse=True)
    gen = prof["GENERIC"]
    gen_sorted = sorted(gen, reverse=True)
    W = comb(n, b) / q ** 2
    return {"q": q, "n": n, "b": b, "W_log2": round(math.log2(W), 2),
            "N0": N0, "coset_union_ctx": cu,
            "max_r": {k: (round(max(v), 3) if v else None)
                      for k, v in prof.items()},
            "gen_max_r": round(gen_sorted[0], 3),
            "gen_p999_r": round(gen_sorted[len(gen) // 1000], 3),
            "gen_med_r": round(gen_sorted[len(gen) // 2], 3),
            "gen_mass": round(sum(gen) / len(gen), 4),
            "top_generic_kappa": [(round(r, 2), k)
                                  for r, k in top_generic[:8]],
            "kappa_max": max(kappa)}


@app.local_entrypoint()
def main():
    res = list(cell.map(JOBS, return_exceptions=True))
    fails = 0
    rows = []
    print(f"{'cell':>14} {'W(log2)':>8} {'N0':>7} {'cu':>4} "
          f"{'genMAX':>7} {'gen.999':>8} {'genMED':>7}  top-(r,kappa)")
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:200])
            continue
        rows.append(r)
        print(f"  ({r['q']},{r['n']},b={r['b']})".rjust(14) +
              f" {r['W_log2']:>8} {r['N0']:>7} {r['coset_union_ctx']:>4} "
              f"{r['gen_max_r']:>7} {r['gen_p999_r']:>8} "
              f"{r['gen_med_r']:>7}  {r['top_generic_kappa'][:4]}")
    with open("/tmp/f2_l1_fourier.json", "w") as f:
        json.dump(rows, f, indent=1)
    if fails:
        raise SystemExit(f"F2_L1_FOURIER_SPECTRUM_FAIL ({fails})")
    # pre-registered falsifier evaluation at b=3, n=32, three scales
    kill = all(r["gen_max_r"] > R_STAR for r in rows
               if r["b"] == 3 and r["n"] == 32)
    print(f"\nfalsifier (b=3, three scales, R*={R_STAR}): "
          f"{'FIRED' if kill else 'not fired'}")
    if kill:
        raise SystemExit("F2_L1_FALSIFIER_FIRED")
    print("F2_L1_FOURIER_SPECTRUM_PASS")
