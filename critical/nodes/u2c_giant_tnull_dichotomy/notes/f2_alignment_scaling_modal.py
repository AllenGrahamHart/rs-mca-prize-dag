#!/usr/bin/env python3
"""F2 campaign (Modal): ALIGNMENT SCALING STUDY (cycle 83) — the
falsifier-adjacent number of satellite 19, measured across scales.

Per exact row (q, n, j) — full enumeration of the frequency space:
  R      = |q^j N_total - 2^n| / sum_{c != 0} exp(S_c)
  R_pred = sqrt(sum_{c != 0} exp(2 S_c)) / sum_{c != 0} exp(S_c)
  ratio  = R / R_pred   (random-sign alignment factor; cycle-82
           baseline: 6.5-8.0 at three rows)

PRE-REGISTERED READS:
  (1) PRIMARY: least-squares slope of log(ratio) vs log(q^j - 1)
      across all 12 rows.  slope <= 0.1  => stabilization-consistent
      (constant-factor alignment, absorbable in the 2^15/condition
      slack); slope >= 0.25 => DANGER LANE (sign-magnitude
      correlation grows with scale) — bank loudly and extend the
      falsifier; in between => inconclusive, add scales.
  (2) TWISTED-ORBIT INVARIANCE (new structure, one-line proof): the
      map c_i -> lambda^i c_i (lambda in mu_n) permutes the multiset
      {c.xbar(x) : x in mu_n} (it is x -> lambda x), so S and eps
      are constant on twisted orbits; effective frequency population
      is (q^j - 1)/n.  Verified exactly on sampled orbits per row.
  (3) sign imbalance |E eps| per row, with the orbit-corrected
      random scale sqrt(n/(q^j - 1)) for context (diagnostic).
"""
import math

import modal

app = modal.App("rs-mca-f2-align-scaling")
image = modal.Image.debian_slim().pip_install("numpy")

JOBS = [
    (97, 32, 2), (97, 32, 3), (113, 16, 2), (113, 16, 3),
    (193, 64, 2), (241, 48, 2), (241, 48, 3), (257, 64, 2),
    (257, 64, 3), (331, 30, 2), (331, 30, 3), (577, 64, 2),
]


@app.function(image=image, cpu=2, memory=8192, timeout=280)
def cell(job):
    q, n, j = job
    import numpy as np

    def pf(x):
        out, d = [], 2
        while d * d <= x:
            while x % d == 0:
                out.append(d)
                x //= d
            d += 1
        if x > 1:
            out.append(x)
        return out

    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1 for r in set(pf(q - 1))))
    h = pow(g, (q - 1) // n, q)
    D = [pow(x, 1, q) for x in (pow(h, i, q) for i in range(n))]
    xbar = [[pow(x, i, q) for i in range(1, j + 1)] for x in D]

    Q = q ** j
    ar = np.arange(Q, dtype=np.int64)
    cdig = [((ar // q ** i) % q).astype(np.int64) for i in range(j)]

    # integer DP for N_total (state shift is a bijection)
    counts = np.zeros(Q, dtype=np.int64)
    counts[0] = 1
    for xi in range(n):
        xb = xbar[xi]
        newidx = sum(((cdig[i] + xb[i]) % q) * q ** i for i in range(j))
        tmp = np.zeros_like(counts)
        tmp[newidx] = counts
        counts = counts + tmp
    N_total = int(counts[0])
    # overflow sentinel: single-state counts stay ~2^n/q^j << 2^62;
    # (the total 2^n itself can exceed int64, so never .sum() it)
    assert int(counts.max()) < (1 << 62)
    signed_exact = q ** j * N_total - 2 ** n

    # (S, eps) enumeration
    theta = math.pi / q
    ltab = np.array([math.log(2.0)] +
                    [math.log(abs(2 * math.cos(theta * s)))
                     for s in range(1, q)])
    upper = np.array([0] + [1 if s > q // 2 else 0 for s in range(1, q)],
                     dtype=np.int64)
    S = np.zeros(Q)
    par = np.zeros(Q, dtype=np.int64)
    ssum = np.zeros(Q, dtype=np.int64)
    for xi in range(n):
        xb = xbar[xi]
        sidx = sum(cdig[i] * xb[i] for i in range(j)) % q
        S += ltab[sidx]
        par += upper[sidx]
        ssum += sidx
    # quantization theorem re-check: sum_x s_x == 0 mod q everywhere
    assert int((ssum % q).max()) == 0
    # CATCH #21: eps = (-1)^{K + U}, K = carry (sum s_x)/q, U = #upper
    eps = 1 - 2 * ((ssum // q + par) % 2)
    S[0] = -1e30
    eS = np.exp(S)
    sum1 = float(eS.sum())
    sum2 = float((eS * eS).sum())
    sgn_num = float((eps * eS).sum())
    imb = float(eps[1:].mean())
    R = abs(signed_exact) / sum1
    Rp = math.sqrt(sum2) / sum1
    ident_err = abs(sgn_num - signed_exact) / max(1.0, abs(signed_exact))

    # twisted-orbit invariance on 200 sampled orbits
    rng = np.random.RandomState(7)
    orb_err = 0.0
    lam = D[1] if n > 1 else 1
    for c0 in rng.randint(1, Q, 200):
        digs = [(int(c0) // q ** i) % q for i in range(j)]
        digs2 = [digs[i] * pow(lam, i + 1, q) % q for i in range(j)]
        c1 = sum(digs2[i] * q ** i for i in range(j))
        orb_err = max(orb_err,
                      float(abs(S[int(c0)] - S[c1])) if c0 != 0 else 0.0,
                      abs(float(eps[int(c0)]) - float(eps[c1])))
    return {"q": q, "n": n, "j": j, "Q": Q, "N_total": N_total,
            "R": R, "Rp": Rp, "ratio": R / Rp, "ident_err": ident_err,
            "imb": imb, "orb_err": orb_err,
            "rand_orbit": math.sqrt(n / (Q - 1))}


@app.local_entrypoint()
def main():
    res = list(cell.map(JOBS, return_exceptions=True))
    fails = 0
    pts = []
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:300])
            continue
        ok = r["ident_err"] < 1e-6 and r["orb_err"] < 1e-9
        print(f"(q={r['q']:>4}, n={r['n']:>3}, j={r['j']}) |c|={r['Q']:>9}: "
              f"ratio R/R_pred = {r['ratio']:7.2f}  (R = {r['R']:.3e}, "
              f"R_pred = {r['Rp']:.3e})  |E eps| = {abs(r['imb']):.4f} "
              f"(orbit-rand {r['rand_orbit']:.4f})  ident {r['ident_err']:.0e} "
              f"orbit-inv {r['orb_err']:.0e}  {'OK' if ok else 'FLAG'}")
        if not ok:
            fails += 1
        pts.append((math.log(r["Q"] - 1), math.log(r["ratio"])))
    if len(pts) >= 6:
        mx = sum(p[0] for p in pts) / len(pts)
        my = sum(p[1] for p in pts) / len(pts)
        num = sum((p[0] - mx) * (p[1] - my) for p in pts)
        den = sum((p[0] - mx) ** 2 for p in pts)
        slope = num / den
        print(f"\nPRIMARY READ: slope of log(ratio) vs log(population) "
              f"= {slope:.3f} over {len(pts)} rows")
        if slope <= 0.1:
            print("=> STABILIZATION-CONSISTENT (constant-factor "
                  "alignment; absorbable)")
        elif slope >= 0.25:
            print("=> DANGER LANE (alignment grows with scale) — bank "
                  "loudly")
            fails += 1
        else:
            print("=> INCONCLUSIVE — add scales")
    if fails:
        raise SystemExit(f"F2_ALIGN_SCALING_FAIL ({fails})")
    print("\nF2_ALIGNMENT_SCALING_PASS")
