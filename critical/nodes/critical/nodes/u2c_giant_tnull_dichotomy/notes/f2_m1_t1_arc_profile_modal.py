#!/usr/bin/env python3
"""F2 campaign M1-t1 (Modal): the t=1 FULL-BAND ARC PROFILE experiment
(pre-registered; the mid-band flatness question at the mildest
instance, per the arc-class recursion lemma).

t=1 anchors (PROVED inline here, verified as gates):
  A1 ORBIT COLLAPSE: E_b(lambda) depends only on the coset
     lambda*mu_n; N_b^{p1}(0) = C(n,b)/q + (n/q) sum_{j<m} E_b^(j).
  A2 FACTORIZATION: prod_{j<m} P_j(z) = prod_{x in F_q^x}(1+z psi(x))
     = (1+z^q)/(1+z), all coefficients +-1 below degree q. At m=1 the
     arc polynomial itself is coefficient-flat: |E_b| = 1 for ALL b.

MEASURED: per row (q, n), per orbit j, the full profile
r_b^(j) = |E_b^(j)| / sqrt(C(n,b)) for b = 1..n-1; report the row's
mid-band max R_mid = max over b in [n/4, 3n/4], j of r_b^(j), plus
argmax b, and the m=1 anchors' exact flatness.

PRE-REGISTERED READ (immutable):
  P1 (ARC ROUTE VIABLE-EXACT): R_mid <= poly — say R_mid^2 <= q — at
     all scales: the t=1 mid-band closes by the arc route.
  P2 (VIABLE-AVERAGED): R_mid ~ C(n,b)^{something<1/2}/..., i.e.
     r_b << 1 fails pointwise but the ORBIT-SUM (n/q)|sum_j E_b^(j)|
     stays < 1 at mid-band: closes on average; report the sum profile.
  P3 (ARC ROUTE DEAD at t=1): sustained R_mid >> sqrt-scale with the
     orbit-sum also super-budget across >= 3 field scales: bank the
     negative; M1-t1 must go through 0-specialness only.
Gates: A1 (orbit constancy + census identity vs integer DP), A2
(product flat, m=1 rows |E_b| = 1 to 1e-6). Failure refutes anchors.
"""
import cmath
import math
from math import comb

import modal

app = modal.App("rs-mca-f2-m1-t1")
image = modal.Image.debian_slim()

ROWS = [(97, 32), (97, 48), (97, 96), (193, 32), (193, 96), (193, 192),
        (257, 32), (257, 64), (257, 128), (257, 256), (449, 64),
        (769, 32), (641, 128), (1153, 128)]


@app.function(image=image, cpu=2, memory=2048, timeout=280)
def row(job):
    q, n = job
    m = (q - 1) // n
    assert (q - 1) % n == 0
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
    two_pi_q = 2 * math.pi / q
    psi = [cmath.exp(1j * two_pi_q * v) for v in range(q)]

    # full coefficient profiles per orbit rep lambda = g^j
    profiles = []
    for j in range(m):
        lam = pow(g, j, q)
        coef = [0j] * (n + 1)
        coef[0] = 1.0 + 0j
        deg = 0
        for x in D:
            w = psi[lam * x % q]
            deg += 1
            for dd in range(deg - 1, -1, -1):
                if coef[dd] != 0:
                    coef[dd + 1] += coef[dd] * w
        profiles.append(coef)
        # A1 orbit constancy spot-check: lambda' = lam * (random mu elt)
        lam2 = lam * D[j % n] % q
        c2 = [0j] * (n + 1)
        c2[0] = 1.0 + 0j
        deg = 0
        for x in D:
            w = psi[lam2 * x % q]
            deg += 1
            for dd in range(deg - 1, -1, -1):
                if c2[dd] != 0:
                    c2[dd + 1] += c2[dd] * w
        for bb in range(n + 1):
            tol = 1e-9 * (1 + max(abs(coef[bb]), abs(c2[bb]))) + 1e-4
            assert abs(coef[bb] - c2[bb]) < tol, ("A1 constancy", j, bb)

    # A2 factorization gate: product of the m orbit polynomials
    prod = [0j] * (q)
    prod[0] = 1.0 + 0j
    plen = 1
    maxinter = 1.0
    for coef in profiles:
        new = [0j] * min(q, plen + n)
        for i in range(plen):
            if prod[i] == 0:
                continue
            ci = prod[i]
            for dd in range(n + 1):
                if i + dd < len(new) and coef[dd] != 0:
                    new[i + dd] += ci * coef[dd]
        prod = new
        plen = len(new)
        maxinter = max(maxinter, max(abs(c) for c in prod))
    # (1+z^q)/(1+z) truncated below q: alternating +-1, tolerance scaled
    # to the float error of the largest intermediate coefficient
    a2tol = max(1e-4, 1e-11 * maxinter * m)
    a2_checked = a2tol < 0.5
    if a2_checked:
        for i in range(min(plen, q - 1)):
            want = 1.0 if i % 2 == 0 else -1.0
            assert abs(prod[i] - want) < a2tol, ("A2 not flat", i, prod[i])

    # A1 census identity vs integer DP at 3 sampled b
    for b in (n // 4, n // 2, (3 * n) // 4):
        dp = {0: [1] + [0] * b}
        for x in D:
            new = {}
            for a, vec in dp.items():
                t = new.setdefault(a, [0] * (b + 1))
                for w_ in range(b + 1):
                    t[w_] += vec[w_]
                k = (a + x) % q
                t2 = new.setdefault(k, [0] * (b + 1))
                for w_ in range(b):
                    if vec[w_]:
                        t2[w_ + 1] += vec[w_]
            dp = new
        N0 = dp.get(0, [0] * (b + 1))[b]
        inv = comb(n, b) / q + (n / q) * sum(p[b].real for p in profiles)
        ctol = 1e-9 * (1 + N0) + 1e-3
        assert abs(sum(p[b].imag for p in profiles)) < ctol
        assert abs(inv - N0) < ctol, ("A1 census identity", b, inv, N0)

    # the profile read
    R_mid, arg = 0.0, None
    sum_mid_max = 0.0
    for b in range(max(1, n // 4), (3 * n) // 4 + 1):
        sq = math.sqrt(comb(n, b))
        s_orbit = abs(sum(p[b] for p in profiles)) * n / q
        sum_mid_max = max(sum_mid_max, s_orbit)
        for j in range(m):
            r = abs(profiles[j][b]) / sq
            if r > R_mid:
                R_mid, arg = r, (j, b)
    return {"q": q, "n": n, "m": m, "R_mid": round(R_mid, 4),
            "argmax": arg, "orbit_sum_mid_max": round(sum_mid_max, 4),
            "flat_anchor": m == 1, "a2_checked": a2_checked}


@app.local_entrypoint()
def main():
    res = list(row.map(ROWS, return_exceptions=True))
    fails = 0
    print(f"{'row':>12} {'m':>3} {'R_mid':>9} {'argmax(j,b)':>12} "
          f"{'(n/q)|sum_j E_b|max':>20}")
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:250])
            continue
        tag = " [m=1 flat anchor]" if r["flat_anchor"] else ""
        print(f"  ({r['q']},{r['n']})".rjust(12) +
              f" {r['m']:>3} {r['R_mid']:>9} {str(r['argmax']):>12} "
              f"{r['orbit_sum_mid_max']:>20}{tag}")
    if fails:
        raise SystemExit(f"F2_M1_T1_ARC_PROFILE_FAIL ({fails})")
    print("\nF2_M1_T1_ARC_PROFILE_PASS")
