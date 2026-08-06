#!/usr/bin/env python3
"""fr_fiber_rigidity -- verifier 5: |Bset| for a FIXED received pair.

(FR) is refuted per-pair (witness.py).  But the quantity the (WTB) ledger
actually consumes is |Bset(Tau)| -- the number of DISTINCT selected blocks
realised across the family Tau of a FIXED (u,v).  This run measures it
directly, at a boundary shape where the family is genuinely
multi-dimensional (deg tau < k-ell = 4), using the LENS:

    B_nu(tau) = {x in D : tau(x) = W_nu(x)},   W_nu = C_nu / L_nu

which is tau-independent.  A block of size r pins tau at r > k-ell points,
so every candidate block is found by interpolating tau through some
(k-ell)-subset of D -- an EXHAUSTIVE enumeration of candidates.

Shape: h=25, ell=3, r=7, d=18, sigma=0, e=14, k=7, n=60, q=61.

Run: tools/ramguard local -- python3 \
       notes/pilots_20260804/fr_fiber_rigidity/census.py
"""

import itertools
import json
import os
import random
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from toy import Shape, build, classify, inv  # noqa
from gate import build_words  # noqa
from witness import kernel_basis  # noqa

CHECKS = []


def chk(cond, name, info=""):
    CHECKS.append({"name": name, "ok": bool(cond), "info": str(info)})


def interp(pts, q):
    """Lagrange interpolation through [(x,y)]; returns coefficient list."""
    n = len(pts)
    coeffs = [0] * n
    for j, (xj, yj) in enumerate(pts):
        num = [1]
        den = 1
        for i, (xi, _) in enumerate(pts):
            if i == j:
                continue
            new = [0] * (len(num) + 1)
            for a, c in enumerate(num):
                new[a + 1] = (new[a + 1] + c) % q
                new[a] = (new[a] - xi * c) % q
            num = new
            den = (den * (xj - xi)) % q
        s = (yj * inv(den % q, q)) % q
        for a, c in enumerate(num):
            coeffs[a] = (coeffs[a] + s * c) % q
    return coeffs


def pev(a, x, q):
    acc = 0
    for c in reversed(a):
        acc = (acc * x + c) % q
    return acc


def one_run(shape, cfg, want, seed):
    q, r = shape.q, shape.r
    H, D = cfg["H"], cfg["D"]
    fod = cfg["fibers_of_D"]
    rng = random.Random(seed)

    witness = None
    for B1t in itertools.combinations(D, r):
        B1 = list(B1t)
        if B1[0] != D[0]:
            continue
        B2 = [x for x in D if x not in set(B1)]
        prof1 = [len(set(F) & set(B1)) for F in fod]
        c1, c2 = classify(B1, fod), classify(B2, fod)
        kind = ("rigid" if c1 == c2 == "rigid"
                else ("strong" if "strong" in (c1, c2) else "weak"))
        if kind != want:
            continue
        if want == "strong" and 2 not in prof1:
            continue
        witness = (B1, B2)
        break
    if witness is None:
        return None
    B1, B2 = witness
    u, v = build_words(cfg, shape, B1, B2, rng)
    return _census(shape, cfg, u, v, B1, B2, want)


def main():
    shape = Shape(h=25, k=7, q=61)
    chk(shape.n == 60 and shape.k - shape.ell == 4,
        "family is 4-dimensional", repr(shape))
    cfg = build(shape)
    rows = []
    for want in ("strong", "rigid"):
        for seed in (20260806, 11, 12345, 777):
            res = one_run(shape, cfg, want, seed)
            if res:
                res["base_kind"] = want
                res["seed"] = seed
                rows.append(res)
    report = {"shape": repr(shape),
              "D_fiber_sizes": [len(F) for F in cfg["fibers_of_D"]],
              "sixt_bound": 6 * shape.t,
              "runs": rows,
              "max_Bset": max(x["Bset_size"] for x in rows),
              "max_members": max(x["maximal_selected_members"]
                                 for x in rows),
              "all_Bset_le_6t": all(x["Bset_size"] <= 6 * shape.t
                                    for x in rows),
              "checks": len(CHECKS),
              "failed": [c for c in CHECKS if not c["ok"]]}
    with open(os.path.join(HERE, "census.json"), "w") as fh:
        json.dump({"report": report, "all_checks": CHECKS}, fh, indent=1,
                  sort_keys=True, default=str)
    print(json.dumps(report, indent=1, sort_keys=True, default=str))
    return 1 if report["failed"] else 0


def _census(shape, cfg, u, v, B1, B2, want):
    q, r = shape.q, shape.r
    H, D = cfg["H"], cfg["D"]
    fod = cfg["fibers_of_D"]

    basis, rk = kernel_basis(cfg, shape, B1, B2)
    chk(len(basis) == shape.c, f"dim K_d = sigma+1 [{want}]", len(basis))
    rho = {x: (pow(x, 3, q) * u[x] + v[x]) % q for x in H}
    chk(sorted(x for x in H if rho[x]) == sorted(D),
        f"AD1 D = supp(rho) [{want}]")

    # --- exhaustive candidate enumeration via the LENS
    slopes = cfg["slopes"]
    bset = set()
    bset_by_kind = Counter()
    members = set()
    cand = 0
    for nu in slopes:
        al, be = nu
        # W_nu on D, where L_nu(x) = al - be*x^3 is nonzero
        W = {}
        for x in D:
            L = (al - be * pow(x, 3, q)) % q
            if L:
                W[x] = ((al * u[x] + be * v[x]) % q * inv(L, q)) % q
        if len(W) < shape.k - shape.ell:
            continue
        for sub in itertools.combinations(sorted(W), shape.k - shape.ell):
            cand += 1
            tau = interp([(x, W[x]) for x in sub], q)
            blk = tuple(sorted(x for x in W if pev(tau, x, q) == W[x]))
            if len(blk) != r:
                continue
            # the member: (f,g) = (tau, -X^3 * tau)
            E = {x: (u[x] - pev(tau, x, q)) % q for x in H}
            Ep = {x: (v[x] + pow(x, 3, q) * pev(tau, x, q)) % q for x in H}
            core = [x for x in H if E[x] == 0 and Ep[x] == 0]
            if len(core) != shape.k + shape.d:
                continue                       # not depth-d maximal
            agr = {}
            for mu in slopes:
                a0, b0 = mu
                agr[mu] = sum(1 for x in H
                              if (a0 * E[x] + b0 * Ep[x]) % q == 0)
            mx = max(agr.values())
            if mx != shape.A:
                continue                       # liveness fails
            liveslopes = [mu for mu, a in agr.items() if a == mx]
            if len(liveslopes) < 2:
                continue
            # all selected off-core points must lie in D
            ok = True
            for mu in liveslopes:
                a0, b0 = mu
                off = [x for x in H if (a0 * E[x] + b0 * Ep[x]) % q == 0
                       and x not in set(core)]
                if any(x not in set(D) for x in off) or len(off) != r:
                    ok = False
            if not ok:
                continue
            members.add(tuple(tau))
            for mu in liveslopes:
                a0, b0 = mu
                bb = tuple(sorted(x for x in D
                                  if (a0 * E[x] + b0 * Ep[x]) % q == 0))
                if len(bb) == r:
                    if bb not in bset:
                        bset_by_kind[classify(list(bb), fod)] += 1
                    bset.add(bb)

    return {
        "candidates_enumerated": cand,
        "maximal_selected_members": len(members),
        "Bset_size": len(bset),
        "Bset_by_fiber_class": dict(bset_by_kind),
    }


if __name__ == "__main__":
    sys.exit(main())
