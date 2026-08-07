#!/usr/bin/env python3
"""F2 campaign (Modal): CROSS-SUPPORT MEASUREMENT (cycle 89) — the
corrected E3 lane, decided by data.

Frame: w_c = e^{S_c} [c != 0]; W-hat = FFT(w); pairing identity
    (1/Q) sum_d eps-hat(d) conj(W-hat(d)) = sum_{c != 0} eps_c e^{S_c}
                                          = q^j N_total - 2^n
(verified per row).  E3-surgery viability: does there exist a SMALL
set H of frequencies with
    sum_{d not in H} |t_d| <= 10 * sqrt(sum_{c != 0} e^{2 S_c}),
    t_d = eps-hat(d) conj(W-hat(d)) / Q
(the absolute tail at alignment scale, so bounding |eps-hat| on H
alone would close the summit)?  H is taken as top-k by |W-hat|.

PRE-REGISTERED READS:
  (A) pairing identity per row (< 1e-9 rel);
  (B) k_surgery = smallest such k, reported as fraction of Q.
      Random-spectra prediction: tail mass ~ (1 - k/Q)(pi/4) sqrt(Q)
      * sqrt(sum e^{2S}) => k_surgery/Q -> 1 (E3 DEAD: bank NO-GO
      #11 — cross-support surgery cannot beat the sqrt(Q) barrier
      when both spectra are near-random, which satellite 23
      measured).  Surprise concentration (k_surgery/Q <= 0.1 at
      multiple rows) => E3 LIVE with named small support — bank the
      support's census structure instead.
  (C) capture: smallest k with |partial_k - signed_dev| <= 10 *
      sqrt(sum e^{2S}) — how many frequencies determine the answer.
"""
import math

import modal

app = modal.App("rs-mca-f2-cross-support")
image = modal.Image.debian_slim().pip_install("numpy")

JOBS = [
    (97, 32, 2), (113, 16, 2), (193, 64, 2), (257, 64, 2),
    (353, 32, 2), (449, 64, 2), (577, 64, 2),
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
    w = np.exp(S)
    w[0] = 0.0  # c != 0 weight
    signed_dev = float((eps * w).sum())
    scale = math.sqrt(float((w * w).sum()))

    ehat = np.fft.fftn(eps.reshape((q,) * j)).ravel()
    What = np.fft.fftn(w.reshape((q,) * j)).ravel()
    t = ehat * np.conj(What) / Q
    pair = float(t.sum().real)
    pair_err = abs(pair - signed_dev) / max(1.0, abs(signed_dev))

    order = np.argsort(np.abs(What))[::-1]
    tt = t[order]
    absr = np.abs(tt)
    # tail absolute mass after top-k, and partial signed sums
    tail = np.cumsum(absr[::-1])[::-1]  # tail[k] = sum_{i >= k} |t|
    partial = np.cumsum(tt.real)
    thr = 10 * scale
    ks = int(np.searchsorted(-tail, -thr))  # first k with tail <= thr
    # capture: first k with |partial_k - signed_dev| <= thr
    diff = np.abs(partial - signed_dev)
    kc = int(np.argmax(diff <= thr)) if bool((diff <= thr).any()) else Q
    Mabs = float(absr.sum())
    return {"q": q, "n": n, "j": j, "Q": Q,
            "pair_err": pair_err,
            "ks_frac": ks / Q, "kc_frac": (kc + 1) / Q,
            "bits_abs": math.log2(max(Mabs, 1e-300) / scale),
            "trivial_bits": 0.5 * j * math.log2(q),
            "ratio_meas": abs(signed_dev) / scale}


@app.local_entrypoint()
def main():
    res = list(cell.map(JOBS, return_exceptions=True))
    fails = 0
    dead = 0
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:300])
            continue
        ok = r["pair_err"] < 1e-9
        print(f"(q={r['q']:>4}, n={r['n']:>3}, j={r['j']}) "
              f"|c|={r['Q']:>7}: pairing {r['pair_err']:.0e}  "
              f"k_surgery/Q = {r['ks_frac']:.3f}  capture k/Q = "
              f"{r['kc_frac']:.4f}  abs-pairing cost = "
              f"{r['bits_abs']:.1f} bits (trivial sqrt(Q) = "
              f"{r['trivial_bits']:.1f})  meas ratio = "
              f"{r['ratio_meas']:.1f}  {'OK' if ok else 'FLAG'}")
        if not ok:
            fails += 1
        if r["ks_frac"] > 0.5:
            dead += 1
    print(f"\nVERDICT: k_surgery/Q > 0.5 at {dead}/{len(res)} rows")
    if dead >= max(1, len(res) - 1):
        print("=> E3 DEAD (no-go #11): the absolute tail never thins; "
              "cross-support surgery cannot beat sqrt(Q) with "
              "near-random spectra")
    elif dead == 0:
        print("=> E3 LIVE: concentration found — bank the support")
    else:
        print("=> MIXED — examine per-row structure")
    if fails:
        raise SystemExit(f"F2_CROSS_SUPPORT_FAIL ({fails})")
    print("\nF2_CROSS_SUPPORT_PASS")
