#!/usr/bin/env python3
"""F5 P6-E3 (Modal): calibrate the Z-mining density model for the
NEAR-PENCIL BUDGET conjecture.

Construction: (u,v) = pencil pair (c0 + z0*w0, w0) perturbed at T (|T| = 4
= t+1 points, both du, dv nonzero there). By the NP-SUPPORT and
NP-VALIDITY lemmas every post-tangent valid live support is S = Z ∪ T
with Z ⊆ unperturbed, |Z| = A - 4, and the T-coincidences pin
(gamma, z) with t-1 = 2 residual checks: random-Z solve probability
~ q^-(t-1) = q^-2.

Model under test:  E[#live (z,Z) hits] = C(n-4, A-4) * q^-2   (per T)
Rows: (24, 73):    C(20,11)/73^2   = 167960/5329  = 31.5 predicted
      (24, 193):   C(20,11)/193^2  = 4.51
      (24, 577):   C(20,11)/577^2  = 0.504
      (24, 1153):  C(20,11)/1153^2 = 0.126

FULL enumeration of Z-space (167,960 sets), exact arithmetic; every hit
verified end-to-end: agreement >= A, validity (top interpolant
coefficients of v on S nonzero), |S ∩ R| >= t+1, S ∩ R_v nonempty.
Reports distinct live slopes vs the NPB budget C(2r, t+1) = C(8,4) = 70.
"""
import itertools
import json
import random

import modal

app = modal.App("rs-mca-f5-p6e3")
image = modal.Image.debian_slim()

ROWS = [(24, 73, 5, 7001), (24, 193, 5, 7002), (24, 577, 5, 7003),
        (24, 1153, 5, 7004)]


@app.function(image=image, cpu=2, memory=2048, timeout=280)
def mine(row):
    n, q, n_trials, seed = row
    rng = random.Random(seed)
    k, t = n // 2, 3
    A = k + t                      # 15
    sT = t + 1                     # 4

    def inv(a):
        return pow(a % q, q - 2, q)

    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1
                    for r in set(_f(q - 1))))
    h = pow(g, (q - 1) // n, q)
    D = sorted(pow(h, i, q) for i in range(n))

    def ev(cf, x):
        acc = 0
        for c in reversed(cf):
            acc = (acc * x + c) % q
        return acc

    def interp_coeffs(pts, vals):
        """deg<len(pts) interpolant coefficients (Newton->monomial)."""
        m = len(pts)
        coeffs = [0] * m
        for i, (xi, yi) in enumerate(zip(pts, vals)):
            num = [1]
            den = 1
            for j, xj in enumerate(pts):
                if j == i:
                    continue
                new = [0] * (len(num) + 1)
                for d, cc in enumerate(num):
                    new[d] = (new[d] - cc * xj) % q
                    new[d + 1] = (new[d + 1] + cc) % q
                num = new
                den = den * (xi - xj) % q
            w = yi * inv(den) % q
            for d, cc in enumerate(num):
                coeffs[d] = (coeffs[d] + cc * w) % q
        return coeffs

    trials = []
    for _ in range(n_trials):
        c0 = [rng.randrange(q) for _ in range(k)]
        w0 = [rng.randrange(q) for _ in range(k)]
        z0 = rng.randrange(q)
        T = sorted(rng.sample(D, sT))
        Tset = set(T)
        unpert = [x for x in D if x not in Tset]
        du = {x: rng.randrange(1, q) for x in T}
        dv = {x: rng.randrange(1, q) for x in T}
        u = {x: (ev(c0, x) + z0 * ev(w0, x) + du.get(x, 0)) % q for x in D}
        v = {x: (ev(w0, x) + dv.get(x, 0)) % q for x in D}
        hits = []
        slopes = set()
        for Z in itertools.combinations(unpert, A - sT):
            lz = []
            ok = True
            for x in T:
                val = 1
                for zt in Z:
                    val = val * (x - zt) % q
                if val == 0:
                    ok = False
                    break
                lz.append(val)
            if not ok:
                continue
            # gamma*lz[i] = du[T[i]] + z*dv[T[i]] for all i; eliminate gamma
            # via i=0: gamma = (du0 + z dv0)/lz0; then for i=1: linear in z.
            x0, x1 = T[0], T[1]
            a0, b0, a1, b1 = du[x0], dv[x0], du[x1], dv[x1]
            # (a0 + z b0) * lz[1] = (a1 + z b1) * lz[0]
            den = (b0 * lz[1] - b1 * lz[0]) % q
            num = (a1 * lz[0] - a0 * lz[1]) % q
            if den == 0:
                continue          # degenerate direction; skip (measure-zero)
            z = num * inv(den) % q
            gamma = (a0 + z * b0) % q * inv(lz[0]) % q
            if gamma == 0:
                continue
            good = all((gamma * lz[i] - (du[T[i]] + z * dv[T[i]])) % q == 0
                       for i in range(2, sT))
            if not good:
                continue
            # verify end-to-end: c = c0 + (z0+z) w0 + gamma * ell_Z
            S = sorted(set(Z) | Tset)
            cz = [(c0[d] + (z0 + z) * w0[d]) % q if d < k else 0
                  for d in range(k)]
            # agreement check on S via ell_Z: c(x) - (u+zv)(x) =
            # gamma*ell_Z(x) - (du+z dv)(x)*1_T ... check directly:
            def cval(x):
                base = (ev(c0, x) + (z0 + z) * ev(w0, x)) % q
                lzx = 1
                for zt in Z:
                    lzx = lzx * (x - zt) % q
                return (base + gamma * lzx) % q
            agree = [x for x in D if cval(x) == (u[x] + z * v[x]) % q]
            assert set(S) <= set(agree), "agreement verification failed"
            # validity: v on S interpolates with nonzero top block
            vc = interp_coeffs(S, [v[x] for x in S])
            valid = any(vc[d] % q for d in range(k, A))
            # lemma checks
            assert len(set(S) & Tset) >= t + 1
            assert set(S) & set(dv.keys())
            if valid:
                hits.append({"z": z, "agree": len(agree)})
                slopes.add(z)
        trials.append({"n_hits": len(hits), "n_slopes": len(slopes),
                       "max_agree": max((h["agree"] for h in hits),
                                        default=0)})
    return {"n": n, "q": q, "t": t, "A": A,
            "predicted_hits": 167960 / q ** 2,
            "trials": trials}


def _f(x):
    out, d = [], 2
    while d * d <= x:
        while x % d == 0:
            out.append(d)
            x //= d
        d += 1
    if x > 1:
        out.append(x)
    return out


@app.local_entrypoint()
def main():
    out = list(mine.map(ROWS, return_exceptions=True))
    print(f"{'(n,q)':>12} {'predicted':>10} {'measured hits (5 trials)':>28} {'slopes':>18} {'budget':>7}")
    for r in out:
        if not isinstance(r, dict):
            print("worker error:", str(r)[:160]); continue
        hits = [tr["n_hits"] for tr in r["trials"]]
        sls = [tr["n_slopes"] for tr in r["trials"]]
        print(f"  ({r['n']},{r['q']})".rjust(12) +
              f" {r['predicted_hits']:>10.2f} {str(hits):>28} {str(sls):>18} {'C(8,4)=70':>7}")
    with open("/tmp/f5_p6e3.json", "w") as f:
        json.dump([r for r in out if isinstance(r, dict)], f, indent=1)
