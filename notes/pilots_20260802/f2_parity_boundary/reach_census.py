#!/usr/bin/env python3
"""Is the total-death adjacent-pair window reachable at EVERY frequency?

Exhaustive over all c in F_{p^2}^* for small p (exact integers).  For each c
we report the largest parity-BALANCED window with Delta confined to two
adjacent residues, and check rho_b = 1 exactly on it.
"""
from __future__ import annotations
import collections, json, math, os, sys
sys.dont_write_bytecode = True
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _H)
import boundary as B  # noqa: E402
from slicecore import (Fp2, admissible_orders, pair_reps, residues,  # noqa: E402
                       Delta_of, sigma_of)

rows = []
for p in (11, 13, 19, 23, 31):
    F = Fp2.make(p)
    mu = admissible_orders(p)[-1]
    reps = pair_reps(F, F.subgroup(mu))
    two_p = 2 * p
    worst_n, tot_c, dead_c = 10 ** 9, 0, 0
    minbal = 1.0
    for a in range(p):
        for bq in range(p):
            if (a, bq) == (0, 0):
                continue
            loc = [residues(F, (a, bq), y) for y in reps]
            D = Delta_of(p, loc)
            S = [x[1] for x in sigma_of(p, loc)]
            ctr = collections.Counter(D)
            best, ba = -1, None
            for v in range(two_p):
                t = min(ctr.get(v, 0), ctr.get((v + 1) % two_p, 0))
                if t > best:
                    best, ba = t, v
            tot_c += 1
            if best < 4:
                continue
            n = 2 * best                       # perfectly balanced
            sel = ([i for i in range(len(D)) if D[i] == ba][:best] +
                   [i for i in range(len(D)) if D[i] == (ba + 1) % two_p][:best])
            dl = [D[i] for i in sel]
            base = sum(S[i] for i in sel) % two_p
            V = B.V_exact(p, dl, base)
            # the falsifier: does SOME slice in the central band have rho = 1?
            dead = any(abs(V[b]) == math.comb(n, b) for b in B.band(n))
            x, xb = B.worst_in_band(V, n)
            bm = B.beta_min(dl)
            minbal = min(minbal, bm)
            worst_n = min(worst_n, n)
            dead_c += 1 if dead else 0
            rows.append({"p": p, "c": [a, bq], "n": n, "beta_min": bm,
                         "some_central_slice_rho_one": dead,
                         "worst_neglog2": x, "worst_b": xb,
                         "eta_n": (x / n) if x is not None else None})
    es = [r["eta_n"] for r in rows if r["p"] == p and r["eta_n"] is not None]
    print(f"p={p:3d}: {tot_c} frequencies; {dead_c} carry a PERFECTLY "
          f"parity-balanced (beta_min={minbal:.3f}) adjacent-pair window "
          f"(n >= {worst_n}) with SOME central slice at rho_b = 1 exactly; "
          f"worst-slice eta_n over those frequencies: "
          f"max = {max(es):.6f}")

B.dump("reach_census.json", {"rows": rows})
n_all = len(rows)
n_dead = sum(1 for r in rows if r["some_central_slice_rho_one"])
print(f"\nTOTAL: {n_dead}/{n_all} tested frequencies give a parity-BALANCED "
      f"window with an EXACT rho_b = 1 central slice; beta_min is "
      f"{min(r['beta_min'] for r in rows):.4f} on every one of them; "
      f"max worst-slice eta_n over all = "
      f"{max(r['eta_n'] for r in rows if r['eta_n'] is not None):.6f}")
