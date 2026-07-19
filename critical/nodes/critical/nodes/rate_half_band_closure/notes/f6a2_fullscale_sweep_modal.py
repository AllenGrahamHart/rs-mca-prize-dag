#!/usr/bin/env python3
"""F6-A2 (floor campaign, Modal): full-scale parametric-family sweep at the
razor rows — the exact-arithmetic attack on the F6 v2 floor.

FLOOR UNDER ATTACK: BAND-DETERMINATION (the band's true determination
equals the first-moment prediction). ATTACK: price EVERY known family
shape at EVERY parameter choice by exact/high-precision arithmetic at
n = 2^41, k = 2^40, log2 q swept through the razor slice (255.900, 256).
A family beating the trigger at a band radius refutes the first-moment
location of the crossing (and constructively covers band radii — a
death here is a discovery either way). CLASSIFY-BEFORE-DECLARING applies
to attack constructions too: any hit must have its construction validity
proven against the pinned lemma (cor:extension-pole-quotient-remainder-
floor) before the falsifier is declared fired.

CALIBRATION GATES (must PASS before the sweep informs anything):
  G1: the single-scale reach at lq = 255.95 reproduces the banked plateau
      (max covered depth d*c = 2^33) over the razor's original scale range
      e in [12, 40).
  G2: the first-moment crossing sigma*(lq) reproduces the banked constant
      8,592,912,738 at the appropriate razor point (matched within the
      published precision).

SWEEP (per razor lq, sharded):
  S1: single-scale quotient-remainder families at ALL scales c = 2^j,
      j = 1..40 (extends the original e in [12,40) — both smaller and the
      giant-M end), exact depth maximization: does ANY scale reach into
      the band (2^33, sigma*(lq)]?
  S2: nested two-scale stacks c2 | c1 (CANDIDATE constructions — validity
      unproven; any hit is flagged CANDIDATE, not a kill): price
      C(n/c1, k/c1 + d1) * C(n/c2 - (k/c2 + d1*c1/c2), d2) * q^-(d1+d2-1)
      vs trigger at sigma = d1*c1 + d2*c2.
Arithmetic: mpmath lgamma at dps = 40 on all decision paths (0.1-bit
margins over ~2^40-scale exponents need ~1e-12 absolute log2 precision).
"""
import json

import modal

app = modal.App("rs-mca-f6a2-sweep")
image = modal.Image.debian_slim().pip_install("mpmath")

N_EXP, K_EXP = 41, 40
SIGMA_STAR_BANKED = 8_592_912_738
PLATEAU_BANKED = 1 << 33


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def sweep_at(payload):
    from mpmath import mp, loggamma as lgamma, log
    mp.dps = 40
    lq = payload["lq"]
    LOG2 = log(2)
    n, k = 1 << N_EXP, 1 << K_EXP

    def log2C(N, m):
        if m < 0 or m > N:
            return mp.mpf("-inf")
        return (lgamma(N + 1) - lgamma(m + 1) - lgamma(N - m + 1)) / LOG2

    trig = mp.mpf(lq) - 40

    # first-moment crossing: largest sigma with log2C(n, k+sigma) - sigma*lq > trig
    lo, hi = 1, n - k
    while lo <= hi:
        mid = (lo + hi) // 2
        if log2C(n, k + mid) - mp.mpf(lq) * mid > trig:
            lo = mid + 1
        else:
            hi = mid - 1
    sigma_star = hi  # largest passing

    # S1: single-scale reach, all scales j = 1..40
    best = {"reach": 0, "scale": None, "band_hits": []}
    for j in range(1, N_EXP):
        c = 1 << j
        if k % c:
            continue
        N, base = n // c, k // c
        lo, hi2, dmax = 1, N - base, 0
        while lo <= hi2:
            mid = (lo + hi2) // 2
            if log2C(N, base + mid) - mp.mpf(lq) * (mid - 1) > trig:
                dmax, lo = mid, mid + 1
            else:
                hi2 = mid - 1
        cov = dmax * c
        if cov > best["reach"]:
            best.update(reach=cov, scale=j)
        if cov > PLATEAU_BANKED and cov <= sigma_star:
            best["band_hits"].append({"j": j, "d": dmax, "covered": cov})

    # S2: nested two-scale stacks (c2 | c1), coarse grid (CANDIDATES only)
    s2_hits = []
    for j1 in range(20, N_EXP - 1):
        c1 = 1 << j1
        N1, b1 = n // c1, k // c1
        # d1 at the single-scale max for this scale
        lo, hi2, d1 = 1, N1 - b1, 0
        while lo <= hi2:
            mid = (lo + hi2) // 2
            if log2C(N1, b1 + mid) - mp.mpf(lq) * (mid - 1) > trig - 20:
                d1, lo = mid, mid + 1
            else:
                hi2 = mid - 1
        if d1 == 0:
            continue
        for j2 in range(max(1, j1 - 12), j1):
            c2 = 1 << j2
            N2 = n // c2
            used2 = (k // c2) + d1 * (c1 // c2)
            avail = N2 - used2
            if avail <= 0:
                continue
            for d2 in (1, 2, 4, 8, 16, 64, 256, 4096, 1 << 20):
                if d2 > avail:
                    break
                val = (log2C(N1, b1 + d1) + log2C(avail, d2)
                       - mp.mpf(lq) * (d1 + d2 - 1))
                sigma = d1 * c1 + d2 * c2
                if val > trig and PLATEAU_BANKED < sigma <= sigma_star:
                    s2_hits.append({"j1": j1, "d1": d1, "j2": j2, "d2": d2,
                                    "sigma": sigma,
                                    "margin_bits": float(val - trig)})
    return {"lq": lq, "sigma_star": int(sigma_star),
            "s1_best_reach": int(best["reach"]), "s1_best_scale": best["scale"],
            "s1_band_hits": best["band_hits"], "s2_candidate_hits": s2_hits[:20],
            "n_s2_hits": len(s2_hits)}


@app.local_entrypoint()
def main():
    # calibration + razor grid
    lqs = [255.90000002, 255.92, 255.95, 255.97, 255.99, 255.9999]
    results = [r for r in sweep_at.map([{"lq": x} for x in lqs],
                                       return_exceptions=True)
               if isinstance(r, dict)]
    g1 = next((r for r in results if abs(r["lq"] - 255.95) < 1e-9), None)
    print("== calibration ==")
    if g1:
        print(f"G1 plateau at lq=255.95: reach = {g1['s1_best_reach']} "
              f"(banked {PLATEAU_BANKED}) scale=2^{g1['s1_best_scale']} "
              f"-> {'PASS' if g1['s1_best_reach'] == PLATEAU_BANKED else 'CHECK'}")
    r0 = next((r for r in results if abs(r["lq"] - 255.90000002) < 1e-9), None)
    if r0:
        print(f"G2 sigma* at Q_crit: {r0['sigma_star']} "
              f"(banked {SIGMA_STAR_BANKED}) "
              f"-> {'PASS' if abs(r0['sigma_star'] - SIGMA_STAR_BANKED) <= 2 else 'CHECK'}")
    print("\n== sweep ==")
    for r in sorted(results, key=lambda r: r["lq"]):
        print(f"lq={r['lq']}: sigma*={r['sigma_star']} "
              f"reach={r['s1_best_reach']} (2^{r['s1_best_scale']}) "
              f"S1-band-hits={len(r['s1_band_hits'])} "
              f"S2-candidates={r['n_s2_hits']}")
        for h in r["s1_band_hits"][:3]:
            print("   S1 HIT:", h)
        for h in r["s2_candidate_hits"][:3]:
            print("   S2 CANDIDATE:", h)
    with open("/tmp/f6a2_results.json", "w") as f:
        json.dump(results, f, indent=1)
