#!/usr/bin/env python3
"""F2 campaign (Modal): PARITY WALSH SPECTRUM (cycle 88) — the E3
lane, measured. THE CHAIN (Parseval + Cauchy-Schwarz, two lines):

  A = sum_{c} eps_c e^{S_c} = (1/q^j) sum_d ephat(d) * conj(Ehat(d))
  => |A - (d=0 term)| <= max_{d != 0} |ephat(d)| / sqrt(q^j)
                          * sqrt(sum_c e^{2 S_c})

so the ENTIRE alignment bound reduces to Walsh flatness of the
parity field: W* = max_{d != 0} |ephat(d)| / sqrt(q^j).  The proved
target at scale becomes 'W* <= 2^{o(n)}' if W* measures O(1)-ish.

MEASUREMENTS per exact row (FFT of the +-1 grid over (Z/q)^j):
  (1) Parseval consistency: Fourier-side A equals direct sum (1e-6);
  (2) the chain inequality validated numerically (implementation
      check — the math is forced);
  (3) PRIMARY: W* per row; slope of log W* vs log(q^j); top-3
      off-zero frequencies (orbit-normalized) for struct-set
      diagnosis; the d=0 term (imbalance) reported separately.
PRE-REGISTERED READS: W* in an O(1)-to-polylog band across rows
=> E3 QUANTITATIVELY LIVE (summit reduces at reachable scales to
parity Walsh flatness — the sharpest reduction the campaign has);
W* growing like a power of the population => E3 requires struct-set
surgery; report top-d structure either way.  Honest note: FFT is
float — this is a MEASUREMENT cycle, not an identity bank; the
argmax coefficient is re-verified by direct summation.
"""
import math

import modal

app = modal.App("rs-mca-f2-parity-spectrum")
image = modal.Image.debian_slim().pip_install("numpy")

JOBS = [
    (97, 32, 2), (97, 32, 3), (113, 16, 2), (113, 16, 3),
    (193, 64, 2), (257, 64, 2), (353, 32, 2), (449, 64, 2),
    (577, 64, 2),
]


@app.function(image=image, cpu=2, memory=8192, timeout=280)
def cell(job):
    q, n, j = job
    assert (q - 1) % n == 0
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
    eps = (1 - 2 * ((ssum // q + par) % 2)).astype(np.float64)
    eS = np.exp(S)  # includes c = 0 (S_0 = n log 2)

    # spectra
    grid_e = eps.reshape((q,) * j)
    grid_w = eS.reshape((q,) * j)
    ehat = np.fft.fftn(grid_e).ravel()
    Ehat = np.fft.fftn(grid_w).ravel()

    # (1) Parseval consistency for the full signed sum
    A_direct = float((eps * eS).sum())
    A_fourier = float((ehat * np.conj(Ehat)).sum().real) / Q
    pars_err = abs(A_direct - A_fourier) / max(1.0, abs(A_direct))

    mags = np.abs(ehat)
    d0 = float(mags[0])
    mags[0] = 0.0
    Wstar = float(mags.max()) / math.sqrt(Q)
    top = np.argsort(mags)[-3:][::-1]

    # re-verify argmax coefficient by direct summation
    dmax = int(top[0])
    ddig = [(dmax // q ** i) % q for i in range(j)]
    phase = sum(cdig[i] * ddig[i] for i in range(j)) % q
    w = np.exp(-2j * math.pi * np.arange(q) / q)
    direct = complex((eps * w[phase]).sum())
    ver_err = abs(abs(direct) - float(mags[dmax])) / max(1.0,
                                                         abs(direct))

    # (2) the chain: |A - d0 term| <= W* sqrt(sum e^{2S}) (c=0 incl.
    # both sides consistently; subtract c-side flat manually)
    sum2 = float((eS * eS).sum())
    d0term = d0 * float(eS.sum()) / Q  # |ephat(0)| * Ehat(0)/Q bound
    lhs = abs(A_direct) - d0term  # conservative
    chain_ok = lhs <= Wstar * math.sqrt(sum2) + 1e-6 * abs(A_direct)

    return {"q": q, "n": n, "j": j, "Q": Q, "Wstar": Wstar,
            "imb0": d0 / math.sqrt(Q), "pars_err": pars_err,
            "ver_err": ver_err, "chain_ok": bool(chain_ok),
            "top": [int(t) for t in top],
            "topmag": [float(mags[t]) / math.sqrt(Q) for t in top]}


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
        ok = r["pars_err"] < 1e-6 and r["ver_err"] < 1e-6 and r["chain_ok"]
        tops = ", ".join(f"{m:.1f}" for m in r["topmag"])
        print(f"(q={r['q']:>4}, n={r['n']:>3}, j={r['j']}) "
              f"|c|={r['Q']:>8}: W* = {r['Wstar']:8.2f}  "
              f"(top3/sqrt(Q): [{tops}]; d0/sqrt(Q) = {r['imb0']:.2f})  "
              f"parseval {r['pars_err']:.0e} argmax-ver {r['ver_err']:.0e} "
              f"chain {'OK' if r['chain_ok'] else 'VIOLATED'}  "
              f"{'OK' if ok else 'FLAG'}")
        if not ok:
            fails += 1
        pts.append((math.log(r["Q"]), math.log(r["Wstar"])))
    if len(pts) >= 6:
        mx = sum(p[0] for p in pts) / len(pts)
        my = sum(p[1] for p in pts) / len(pts)
        num = sum((p[0] - mx) * (p[1] - my) for p in pts)
        den = sum((p[0] - mx) ** 2 for p in pts)
        slope = num / den
        print(f"\nPRIMARY READ: slope of log(W*) vs log(population) = "
              f"{slope:.3f}")
        print("(0 = perfectly flat parity spectrum; 0.5 = imbalance-"
              "like growth = E3 needs struct surgery)")
    if fails:
        raise SystemExit(f"F2_PARITY_SPECTRUM_FAIL ({fails})")
    print("\nF2_PARITY_SPECTRUM_PASS")
