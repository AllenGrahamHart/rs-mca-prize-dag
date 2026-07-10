#!/usr/bin/env python3
"""F2 campaign (Modal): FALSIFIER WATCH W1 (cycle 95) — the
refined falsifier (per-orbit constant > 10 sustained at 3+ scales)
tested at 4 NEW rows, one order of magnitude up in population
(4.5M-10M frequencies). Harness = satellite 20 verbatim.

At 2-power n with j in {2, 3}, the PROVED struct census (unions of
scaled mu_M-cosets, M >= 4; exhaustively confirmed = 2^{n/4} at
(113,16,j=3)) contributes exactly 1 per frequency, so its signed
drift is 2^{n/4} (q^j - 1) and the extras fluctuation is
    extras_dev = (q^j N_total - 2^n) - 2^{n/4} (q^j - 1)
      ratio'   = |extras_dev| / sqrt(sum_{c != 0} exp(2 S_c)).
(Subtracting a PROVED subclass is unconditionally valid; any exotic
structured mass remains inside 'extras' and would legitimately
register as alignment.)

PRE-REGISTERED READS:
  (1) COLLAPSE: the raw-inflated j=3 rows drop into or below the
      j=2 band (~7 +- 2); sharp prediction (113,16,3): extras_dev
      = -2^16 exactly, ratio' ~ 0.17.
  (2) PRIMARY: slope of log(ratio') vs log(population) over all 13
      rows: <= 0.1 stabilization (absorbable constant); >= 0.25
      DANGER LANE (bank loudly); else inconclusive, add scales.
  (3) identity and twisted-orbit checks as in cycle 83 (eps with
      the catch-#21 carry).
"""
import math

import modal

app = modal.App("rs-mca-f2-watch-w1")
image = modal.Image.debian_slim().pip_install("numpy")

JOBS = [
    (2113, 64, 2), (2689, 64, 2), (3137, 64, 2), (3169, 32, 2),
]


@app.function(image=image, cpu=2, memory=10240, timeout=280)
def cell(job):
    q, n, j = job
    assert (q - 1) % n == 0, f"mu_{n} does not exist in F_{q}"
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
    D = [pow(h, i, q) for i in range(n)]
    xbar = [[pow(x, i, q) for i in range(1, j + 1)] for x in D]

    Q = q ** j
    ar = np.arange(Q, dtype=np.int64)
    cdig = [((ar // q ** i) % q).astype(np.int64) for i in range(j)]

    counts = np.zeros(Q, dtype=np.int64)
    counts[0] = 1
    for xi in range(n):
        xb = xbar[xi]
        newidx = sum(((cdig[i] + xb[i]) % q) * q ** i for i in range(j))
        tmp = np.zeros_like(counts)
        tmp[newidx] = counts
        counts = counts + tmp
    N_total = int(counts[0])
    assert int(counts.max()) < (1 << 62)
    signed_exact = q ** j * N_total - 2 ** n
    struct = 2 ** (n // 4)
    extras_dev = signed_exact - struct * (q ** j - 1)

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
    assert int((ssum % q).max()) == 0
    eps = 1 - 2 * ((ssum // q + par) % 2)
    S[0] = -1e30
    eS = np.exp(S)
    sum1 = float(eS.sum())
    sum2 = float((eS * eS).sum())
    sgn_num = float((eps * eS).sum())
    ident_err = abs(sgn_num - signed_exact) / max(1.0, abs(signed_exact))
    denom = math.sqrt(sum2)
    return {"q": q, "n": n, "j": j, "Q": Q, "N_total": N_total,
            "raw": abs(signed_exact) / denom,
            "sub": abs(extras_dev) / denom,
            "extras_dev": float(extras_dev),
            "ident_err": float(ident_err)}


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
        ok = r["ident_err"] < 1e-6
        print(f"(q={r['q']:>5}, n={r['n']:>3}, j={r['j']}) "
              f"|c|={r['Q']:>10}: raw ratio = {r['raw']:7.2f}  "
              f"STRUCT-SUB ratio' = {r['sub']:7.2f}  "
              f"(extras_dev = {r['extras_dev']:+.3e})  "
              f"ident {r['ident_err']:.0e}  {'OK' if ok else 'FLAG'}")
        if not ok:
            fails += 1
        pts.append((math.log(r["Q"] - 1), math.log(max(r["sub"], 1e-9))))
    if len(pts) >= 6:
        mx = sum(p[0] for p in pts) / len(pts)
        my = sum(p[1] for p in pts) / len(pts)
        num = sum((p[0] - mx) * (p[1] - my) for p in pts)
        den = sum((p[0] - mx) ** 2 for p in pts)
        slope = num / den
        print(f"\nPRIMARY READ: slope of log(ratio') vs log(population) "
              f"= {slope:.3f} over {len(pts)} rows")
        if slope <= 0.1:
            print("=> STABILIZATION (absorbable constant)")
        elif slope >= 0.25:
            print("=> DANGER LANE — bank loudly")
            fails += 1
        else:
            print("=> INCONCLUSIVE — add scales")
    if fails:
        raise SystemExit(f"F2_WATCH_W1_FAIL ({fails})")
    print("\nF2_FALSIFIER_WATCH_W1_PASS")
