#!/usr/bin/env python3
"""Primitive-biased counterexample hunt for the imprimitivity conjecture.

Objective: exact-in-spirit log Norm(f) = sum_{j odd mod 2N} log|f(zeta^j)|,
evaluated in float64 by a dense DFT matmul (whole neighbourhoods at once).
Any candidate whose float score exceeds the law's prediction is re-evaluated
EXACTLY (python-int field-norm descent) and cross-checked by Bareiss.

Seeds are biased PRIMITIVE: the support is drawn so that it is not contained in
a coset of 2Z/N (many odd-index members).  Moves:
   M1  relocate one nonzero to a free slot, either sign
   M2  flip one sign
   M3  ROTATION FAMILY (new identity): f = p(x^2) + x^(2c+1) q(x^2), sweep c.
       prod_{c=0}^{M-1} Norm(f_c) = Norm_M(p^(2M) + q^(2M)), so this move class
       is exactly the family whose norms have a controlled product.
"""
from __future__ import annotations
import argparse, json, math, os, random, sys, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_norm_ladder/scripts")
from norm_core import norm_descent_py, norm_bareiss


def dft(N):
    j = np.arange(1, 2*N, 2)
    ang = np.pi * np.outer(np.arange(N), j) / N
    return np.cos(ang), np.sin(ang)


def scores(D, C, S):
    re = D @ C; im = D @ S
    P = re*re + im*im
    P = np.maximum(P, 1e-300)
    return 0.5*np.log(P).sum(axis=1), P.min(axis=1)


def is_primitive(f):
    sup = [i for i, c in enumerate(f) if c]
    return len({i % 2 for i in sup}) == 2 or len(sup) == 0


def neighbours(f, N):
    sup = [i for i, c in enumerate(f) if c]
    free = [i for i in range(N) if not f[i]]
    out = []
    for i in sup:                                   # M2 sign flips
        g = list(f); g[i] = -g[i]; out.append(g)
    for i in sup:                                   # M1 relocations
        for j in free:
            for s in (1, -1):
                g = list(f); g[i] = 0; g[j] = s; out.append(g)
    M = N // 2                                      # M3 rotation family
    p = f[0::2]; q = f[1::2]
    for c in range(1, M):
        qq = [0]*M
        for k in range(M):
            if q[k]:
                t = k + c
                qq[t % M] = q[k] * (1 if t < M else -1)
        g = [0]*N
        for k in range(M):
            g[2*k] = p[k]; g[2*k+1] = qq[k]
        out.append(g)
    return out


def climb(f, N, C, S, budget):
    cur = list(f)
    curs = scores(np.array([cur], float), C, S)[0][0]
    for _ in range(budget):
        nb = neighbours(cur, N)
        D = np.array(nb, dtype=np.float64)
        sc, _ = scores(D, C, S)
        i = int(np.argmax(sc))
        if sc[i] <= curs + 1e-12:
            break
        curs = float(sc[i]); cur = nb[i]
    return cur, curs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--w", type=int, required=True)
    ap.add_argument("--target", type=str, required=True)
    ap.add_argument("--restarts", type=int, default=60)
    ap.add_argument("--seconds", type=float, default=210.0)
    ap.add_argument("--seed", type=int, default=20260802)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    N, w = a.N, a.w
    target = int(a.target)
    logt = math.log(target)
    C, S = dft(N)
    rng = random.Random(a.seed)
    t0 = time.time()
    best = None; bestscore = -1e18
    beats = []; n_beats = [0]
    n_restarts = 0
    hist = []
    while n_restarts < a.restarts and time.time() - t0 < a.seconds:
        n_restarts += 1
        # primitive-biased seed: force >=1 odd and >=1 even index
        n_odd = rng.randint(max(1, w//3), max(1, w - 1))
        odd = rng.sample(range(1, N, 2), min(n_odd, N//2))
        even = rng.sample(range(0, N, 2), w - len(odd))
        f = [0]*N
        for i in odd + even: f[i] = rng.choice((1, -1))
        f, sc = climb(f, N, C, S, 400)
        hist.append({"restart": n_restarts, "log": round(sc, 6),
                     "primitive": is_primitive(f)})
        if sc > bestscore:
            bestscore, best = sc, f
        if sc > logt - 1e-6:
            v = norm_descent_py(f)
            if v > target:
                n_beats[0] += 1
                if len(beats) < 5:          # Bareiss re-check only on the first few
                    beats.append({"f": f, "norm": str(v),
                                  "bareiss": str(norm_bareiss(f)),
                                  "primitive": is_primitive(f),
                                  "ratio_to_target": v / target})
    exact_best = norm_descent_py(best) if best else None
    rec = {"N": N, "twoN": 2*N, "w": w, "target_law_prediction": str(target),
           "restarts_done": n_restarts, "seconds": round(time.time()-t0, 1),
           "best_found_f": best, "best_found_norm_exact": str(exact_best),
           "best_bareiss": str(norm_bareiss(best)) if best else None,
           "best_is_primitive": is_primitive(best) if best else None,
           "best_over_target_ratio": (float(exact_best) / target) if exact_best else None,
           "n_strict_beats": n_beats[0], "beats": beats[:5],
           "REFUTES_CONJECTURE": n_beats[0] > 0,
           "restart_log_scores": hist[:200]}
    json.dump(rec, open(a.out, "w"), indent=1)
    print(json.dumps({k: v for k, v in rec.items()
                      if k not in ("restart_log_scores", "best_found_f", "beats")}))


if __name__ == "__main__":
    main()
