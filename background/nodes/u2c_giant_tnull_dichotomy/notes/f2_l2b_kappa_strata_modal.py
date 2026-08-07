#!/usr/bin/env python3
"""F2 campaign L2b EXPERIMENT (Modal): per-kappa strata of the generic
Fourier arcs — measure the functional form of max |E_b| vs kappa
BEFORE proving the L2b arc bound (pre-registered in F2_CAMPAIGN_LOG #2).

Objects as L1. Each generic arc lambda = (l1, l2), l2 != 0, lives on
the chord c = -l1/l2; kappa(c) = #{pairs {x,y} in mu_n : x + y = c}.
Note c = 0 is the QUOTIENT class (pairs {x, -x}, kappa = n/2 when
-1 in mu_n) — excluded from GENERIC, reported separately.

Measured per cell, per kappa stratum over GENERIC arcs:
  #chords, #arcs, max r, mean r  (r = |E_b| / sqrt(C(n,b)))
plus per-chord flags: CHEB (c in {x + x^-1 : x in mu_n}) and the
identity of the argmax chord. Outputs feed the L2b bound's shape;
gates: stratum populations partition the generic arcs; kappa(0) = n/2
when -1 in mu_n (quotient-chord identity).
"""
import cmath
import json
import math
from math import comb

import modal

app = modal.App("rs-mca-f2-l2b-kappa")
image = modal.Image.debian_slim()

JOBS = [(97, 32, 3), (97, 32, 6), (193, 32, 3), (193, 32, 6),
        (257, 32, 3), (257, 32, 6), (97, 16, 4)]


@app.function(image=image, cpu=2, memory=2048, timeout=280)
def cell(job):
    q, n, b = job
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
    Dset = set(D)

    kappa = [0] * q
    for i, x in enumerate(D):
        for y in D[i + 1:]:
            kappa[(x + y) % q] += 1
    if (q - 1) % (2 * n) == 0 or (n % 2 == 0 and pow(h, n // 2, q) == q - 1):
        assert kappa[0] == n // 2, ("quotient-chord identity", kappa[0])
    cheb = {(x + pow(x, q - 2, q)) % q for x in D}

    two_pi_q = 2 * math.pi / q
    psi = [cmath.exp(1j * two_pi_q * v) for v in range(q)]
    sqrt_flat = math.sqrt(comb(n, b))

    # per-chord max over its q-1 arcs (l1, l2) = (-c*l2, l2)
    chord_max = {}
    n_generic = 0
    for c in range(q):
        if c == 0:
            continue    # quotient chord, not GENERIC
        mx = 0.0
        for l2 in range(1, q):
            l1 = (-c * l2) % q
            coef = [0j] * (b + 1)
            coef[0] = 1.0 + 0j
            for x in D:
                w = psi[(l1 * x + l2 * x * x) % q]
                for dd in range(b - 1, -1, -1):
                    if coef[dd] != 0:
                        coef[dd + 1] += coef[dd] * w
            r = abs(coef[b]) / sqrt_flat
            if r > mx:
                mx = r
            n_generic += 1
        chord_max[c] = mx
    assert n_generic == (q - 1) * (q - 1)

    # quotient chord for contrast (c = 0: l1 = 0, l2 != 0)
    qmax = 0.0
    for l2 in range(1, q):
        coef = [0j] * (b + 1)
        coef[0] = 1.0 + 0j
        for x in D:
            w = psi[(l2 * x * x) % q]
            for dd in range(b - 1, -1, -1):
                if coef[dd] != 0:
                    coef[dd + 1] += coef[dd] * w
        qmax = max(qmax, abs(coef[b]) / sqrt_flat)

    strata = {}
    for c, mx in chord_max.items():
        k = kappa[c]
        s = strata.setdefault(k, {"chords": 0, "max": 0.0, "sum": 0.0,
                                  "cheb": 0, "argmax_cheb": None})
        s["chords"] += 1
        s["sum"] += mx
        if c in cheb:
            s["cheb"] += 1
        if mx > s["max"]:
            s["max"] = mx
            s["argmax_cheb"] = (c in cheb)
    out = {str(k): {"chords": v["chords"],
                    "max_r": round(v["max"], 3),
                    "mean_r": round(v["sum"] / v["chords"], 3),
                    "cheb_frac": round(v["cheb"] / v["chords"], 3),
                    "argmax_is_cheb": v["argmax_cheb"]}
           for k, v in sorted(strata.items())}
    return {"q": q, "n": n, "b": b, "kappa0": kappa[0],
            "quotient_max_r": round(qmax, 3), "strata": out}


@app.local_entrypoint()
def main():
    res = list(cell.map(JOBS, return_exceptions=True))
    fails = 0
    rows = []
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:200])
            continue
        rows.append(r)
        print(f"({r['q']},{r['n']},b={r['b']}) kappa0={r['kappa0']} "
              f"quotient_max_r={r['quotient_max_r']}")
        for k, s in r["strata"].items():
            print(f"   kappa={k}: {s['chords']:>4} chords  "
                  f"max_r={s['max_r']:>8}  mean_r={s['mean_r']:>7}  "
                  f"cheb={s['cheb_frac']:>5}  argmax_cheb={s['argmax_is_cheb']}")
    with open("/tmp/f2_l2b_kappa.json", "w") as f:
        json.dump(rows, f, indent=1)
    if fails:
        raise SystemExit(f"F2_L2B_KAPPA_STRATA_FAIL ({fails})")
    print("\nF2_L2B_KAPPA_STRATA_PASS")
