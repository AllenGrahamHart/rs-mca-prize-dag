#!/usr/bin/env python3
"""F2 campaign (Modal): B-RESOLVED RADEMACHER TEST (cycle 113) — the
falsifier watch extended to the axis where the consumer lives.

All prior alignment measurements used the FULL-WINDOW census
(N_total, z = 1). The consumer contract runs at mid-band sizes b:
    N_b = (1/q^j) sum_c [z^b] P_c(z),  P_c = prod_x (1 + z psi(c.xbar)).
Per row and per b:
    signed_b = q^j N_b - C(n,b) - struct_b (q^j - 1)
      struct_b = #{unions of mod-4 exponent classes of total size b}
               = C(n/4, b/4) if 4 | b else 0   (2-power n, j <= 3)
    scale_b  = sqrt( sum_{c != 0} |[z^b] P_c|^2 )   (positive sum;
               float-sound; = the b-resolved variance)
    ratio_b  = |signed_b| / scale_b;  orbit-normalized ratio_b/sqrt(n).

PRE-REGISTERED READS:
  (1) N_b integer-exact vs DP census at every (row, b) (identity);
  (2) mid-band orbit-normalized ratios in the O(1) band (~[0.05, 3],
      as at full window) => the per-orbit Rademacher model holds
      B-RESOLVED — the falsifier direction extends clean to the
      consumer's axis; any mid-band b with ratio/sqrt(n) > 10 at
      3+ rows => DANGER — bank loudly;
  (3) report the max over mid-band b (n/4 <= b <= 3n/4) per row.
"""
import math

import modal

app = modal.App("rs-mca-f2-bresolved")
image = modal.Image.debian_slim().pip_install("numpy")

JOBS = [(97, 32, 2), (113, 16, 2), (193, 64, 2), (257, 64, 2)]


@app.function(image=image, cpu=2, memory=8192, timeout=280)
def cell(job):
    q, n, j = job
    assert (q - 1) % n == 0 and n % 4 == 0
    import numpy as np
    from math import comb

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

    # exact b-resolved census: DP over states x sizes (int64-safe:
    # per-(state,b) counts <= C(n,b) <= 2^n <= 2^64/Q margin checked)
    counts = np.zeros((Q, n + 1), dtype=np.int64)
    counts[0, 0] = 1
    for xi in range(n):
        xb = xbar[xi]
        idx = sum(((cdig[i] + xb[i]) % q) * q ** i for i in range(j))
        shifted = np.zeros_like(counts)
        shifted[idx, 1:] = counts[:, :-1]
        counts = counts + shifted
    assert int(counts.max()) < (1 << 62)
    N_b = counts[0]  # exact integers, b = 0..n

    # frequency-side coefficient vectors (vectorized over c)
    psi = np.exp(2j * math.pi * np.arange(q) / q)
    coef = np.zeros((Q, n + 1), dtype=np.complex128)
    coef[:, 0] = 1.0
    for xi in range(n):
        xb = xbar[xi]
        sidx = sum(cdig[i] * xb[i] for i in range(j)) % q
        w = psi[sidx]
        coef[:, 1:xi + 2] += w[:, None] * coef[:, 0:xi + 1]
    # identity check + ratios
    rows = []
    worst_ident = 0.0
    for b in range(1, n):
        tot = coef[:, b].sum()
        got = tot.real / Q
        worst_ident = max(worst_ident,
                          float(abs(got - int(N_b[b]))) /
                          max(1.0, float(N_b[b])))
        struct_b = comb(n // 4, b // 4) if b % 4 == 0 else 0
        signed = Q * int(N_b[b]) - comb(n, b) - struct_b * (Q - 1)
        mags2 = np.abs(coef[:, b]) ** 2
        mags2[0] = 0.0
        scale = math.sqrt(float(mags2.sum()))
        if scale > 0:
            rows.append((int(b), float(abs(signed) / scale /
                                       math.sqrt(n))))
    mid = [r for (b, r) in rows if n // 4 <= b <= 3 * n // 4]
    return {"q": q, "n": n, "j": j, "ident": float(worst_ident),
            "mid_max": float(max(mid)), "mid_min": float(min(mid)),
            "argmax_b": int(max(((r, b) for (b, r) in rows
                                 if n // 4 <= b <= 3 * n // 4))[1])}


@app.local_entrypoint()
def main():
    res = list(cell.map(JOBS, return_exceptions=True))
    fails = 0
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:300])
            continue
        ok = r["ident"] < 1e-6 and r["mid_max"] <= 10
        print(f"(q={r['q']:>4}, n={r['n']:>3}, j={r['j']}): identity "
              f"{r['ident']:.0e}; mid-band orbit-normalized ratio in "
              f"[{r['mid_min']:.3f}, {r['mid_max']:.3f}] "
              f"(argmax b={r['argmax_b']})  {'OK' if ok else 'FLAG'}")
        if not ok:
            fails += 1
    if fails:
        raise SystemExit(f"F2_BRESOLVED_FAIL ({fails})")
    print("\nF2_BRESOLVED_RADEMACHER_PASS")
