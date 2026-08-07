#!/usr/bin/env python3
"""F2 campaign L2a (Modal): machine verification of the CHORD-ORBIT
LEMMA (see F2_L2A_CHORD_ORBIT_LEMMA.md).

Per row (q, n), m = (q-1)/n:
  G1: N(c) constant on mu_n-orbits — exact integer check over ALL c.
  G2: |J(chi1,chi2)| = sqrt(q) for every generic pair (chi1, chi2,
      chi1chi2 nontrivial in C_m) — < 1e-6.
  G3: the formula N(c) = (q+1-2m*1_{mu_n}(c)-m*delta+E(c))/m^2
      reproduces the direct count at EVERY orbit representative
      (including mu_n itself) — < 1e-6.
  G4: kappa(c) = (N(c)-1_{c/2 in mu_n})/2 matches direct pair counts;
      every kappa lies inside the corollary window.
Any failure refutes the lemma packet.
"""
import cmath
import math

import modal

app = modal.App("rs-mca-f2-l2a-chord")
image = modal.Image.debian_slim()

JOBS = [(97, 32), (97, 16), (193, 32), (193, 64), (257, 32), (257, 64),
        (257, 16), (769, 32), (449, 64)]


@app.function(image=image, cpu=1, memory=1024, timeout=280)
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
    # discrete log table
    dlog = {}
    v = 1
    for i in range(q - 1):
        dlog[v] = i
        v = v * g % q
    mu = {x for x in dlog if dlog[x] % m == 0}   # mu_n = (F_q^x)^m
    assert len(mu) == n

    # direct N(c) for all c != 0
    N = [0] * q
    for x in mu:
        for y in mu:
            N[(x + y) % q] += 1
    # G1: orbit constancy over all c (orbit of c = c * mu)
    for c in range(1, q):
        for u in mu:
            assert N[c * u % q] == N[c], ("G1 orbit constancy", c)

    # characters in C_m: chi_k(g^i) = exp(2pi i * (n k) * i / (q-1))
    zeta = 2 * math.pi / (q - 1)
    def chi(k, x):   # k in 0..m-1
        return cmath.exp(1j * zeta * n * k * dlog[x])

    # G2: Jacobi sums for all pairs in C_m
    sq = math.sqrt(q)
    J = {}
    for k1 in range(m):
        for k2 in range(m):
            s = 0j
            for t in range(2, q):    # s != 0, 1
                s += chi(k1, t) * chi(k2, (1 - t) % q)
            J[(k1, k2)] = s
            if k1 and k2 and (k1 + k2) % m:
                assert abs(abs(s) - sq) < 1e-6, ("G2 |J| != sqrt q", k1, k2)

    delta = 1 if (q - 1) in mu else 0   # q-1 represents -1 mod q

    # orbit representatives: g^j for j = 0..m-1 (cosets of mu_n)
    err_max = 0.0
    kappas = {}
    bound = (q + 1 + (m - 1) * (m - 2) * sq) / (2 * m * m) + 0.5
    inv2 = pow(2, q - 2, q)
    for j in range(m):
        c = pow(g, j, q)
        E = 0j
        for k1 in range(1, m):
            for k2 in range(1, m):
                if (k1 + k2) % m == 0:
                    continue
                E += chi(k1, c) * chi(k2, c) * J[(k1, k2)]
        in_mu = 1 if c in mu else 0
        formula = (q + 1 - 2 * m * in_mu - m * delta + E) / (m * m)
        assert abs(formula.imag) < 1e-6
        err = abs(formula.real - N[c])
        err_max = max(err_max, err)
        assert err < 1e-6, ("G3 formula mismatch", q, n, j, formula, N[c])
        # G4 kappa
        diag = 1 if (c * inv2 % q) in mu else 0
        assert (N[c] - diag) % 2 == 0
        kap = (N[c] - diag) // 2
        # direct kappa
        kd = 0
        mul = sorted(mu)
        for a_i, x in enumerate(mul):
            for y in mul[a_i + 1:]:
                if (x + y) % q == c:
                    kd += 1
        assert kd == kap, ("G4 kappa mismatch", c)
        if not in_mu:
            assert kap <= bound + 1e-9, ("G4 corollary violated", c, kap)
        kappas[j] = (kap, in_mu)
    return {"q": q, "n": n, "m": m, "delta": delta,
            "err_max": err_max, "bound": round(bound, 2),
            "orbit_kappas": {str(j): k for j, k in kappas.items()}}


@app.local_entrypoint()
def main():
    res = list(row.map(JOBS, return_exceptions=True))
    fails = 0
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:250])
            continue
        ks = {j: k for j, (k, im) in
              ((j, v) for j, v in r["orbit_kappas"].items())}
        print(f"(q={r['q']}, n={r['n']}, m={r['m']}, delta={r['delta']}) "
              f"err={r['err_max']:.2e} kappa-bound={r['bound']} "
              f"orbit kappas={ks}")
    if fails:
        raise SystemExit(f"F2_L2A_CHORD_ORBIT_FAIL ({fails})")
    print("\nF2_L2A_CHORD_ORBIT_PASS")
