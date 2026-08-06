#!/usr/bin/env python3
"""fr_fiber_rigidity -- verifier 2: exhaustive liveness at the smallest
tuple-incidence boundary shape that can pose (FR).

Shape (pinned by the boundary formulas, not chosen):
    h = 25,  ell = floor((h-4)/7) = 3,  r = 2ell+1 = 7,  d = h-r = 18,
    sigma = h-7ell-4 = 0,  e = 2r = 14,  t = e-4ell = 2,
    ell = 3 > sigma+2 = 2          <-- the load-bearing hypothesis HOLDS
    A = k+h,  |Core| = k+d,  n = 3d+k-c  with c = dim K_d = sigma+1 = 1.

Model: H = mu_n <= F_q^*, phi = [P:Q] = [X^3 : 1].  Since 3 | n, the
phi-fibers of H are exactly the n/3 cosets of mu_3, all of size ell = 3.

For every partition D = B_1 u B_2 into two r-sets we run the FULL
admissibility stack and record whether the partition is realised.
(FR) is decided by comparing the realised set against the
fiber-rigid set.

Run: tools/ramguard local -- python3 \
       notes/pilots_20260804/fr_fiber_rigidity/toy.py
"""

import itertools
import json
import os
import sys
from collections import Counter

# ------------------------------------------------------------------ F_q


def inv(a, q):
    return pow(a, q - 2, q)


def subgroup(q, n):
    def order(a):
        o, x = 1, a
        while x != 1:
            x = (x * a) % q
            o += 1
        return o
    for c in range(2, q):
        g = pow(c, (q - 1) // n, q)
        if order(g) == n:
            break
    else:
        raise RuntimeError("no element of order n")
    H, x = [], 1
    for _ in range(n):
        H.append(x)
        x = (x * g) % q
    assert len(set(H)) == n
    return sorted(H)


def rank_mod(rows, ncols, q):
    """Rank of a list of rows over F_q (destructive, exact)."""
    rows = [r[:] for r in rows]
    piv, rk = 0, 0
    for col in range(ncols):
        sel = None
        for i in range(rk, len(rows)):
            if rows[i][col] % q:
                sel = i
                break
        if sel is None:
            continue
        rows[rk], rows[sel] = rows[sel], rows[rk]
        iv = inv(rows[rk][col] % q, q)
        rows[rk] = [(v * iv) % q for v in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][col] % q:
                f = rows[i][col] % q
                rows[i] = [(rows[i][j] - f * rows[rk][j]) % q
                           for j in range(ncols)]
        rk += 1
        if rk == len(rows):
            break
    return rk


# ------------------------------------------------------- the configuration

class Shape:
    def __init__(self, h, k, q):
        self.h = h
        self.ell = (h - 4) // 7
        self.r = 2 * self.ell + 1
        self.d = h - self.r
        self.sigma = h - 7 * self.ell - 4
        self.e = 2 * self.r + 0            # sigma = 0 -> e = 2r exactly
        self.t = self.e - 4 * self.ell
        self.k = k
        self.c = self.sigma + 1
        self.n = 3 * self.d + k - self.c
        self.q = q
        self.A = k + h
        self.core = k + self.d
        assert self.sigma == self.d - self.ell - 1 - 2 * self.r
        assert (h + 1) // 2 <= self.d <= h - 2
        assert 2 <= self.t <= self.sigma + 2
        assert self.core + self.e <= self.n

    def __repr__(self):
        return (f"h={self.h} ell={self.ell} r={self.r} d={self.d} "
                f"sigma={self.sigma} e={self.e} t={self.t} k={self.k} "
                f"n={self.n} q={self.q} A={self.A} core={self.core}")


def fiber_profile(B, fibers_of_D):
    """(#full fibers used, #further points) of a block B."""
    Bs = set(B)
    full, extra, maxpartial = 0, 0, 0
    for F in fibers_of_D:
        m = len(Bs & set(F))
        if m == 0:
            continue
        if m == len(F):
            full += 1
        else:
            extra += m
            maxpartial = max(maxpartial, m)
    return full, extra, maxpartial


def classify(B, fibers_of_D):
    """'rigid' | 'weak' | 'strong' per the (FR) wording."""
    _, extra, maxpartial = fiber_profile(B, fibers_of_D)
    if extra <= 1:
        return "rigid"
    return "strong" if maxpartial >= 2 else "weak"


def build(shape, seed=0):
    q, n = shape.q, shape.n
    H = subgroup(q, n)
    idx = {x: i for i, x in enumerate(H)}
    P = [0, 0, 0, 1]                        # X^3
    Q = [1]                                 # 1

    def pev(a, x):
        acc = 0
        for cc in reversed(a):
            acc = (acc * cc if False else acc * x + cc) % q
        return acc

    # phi-fibers of H:  x ~ y  iff x^3 == y^3
    byval = {}
    for x in H:
        byval.setdefault(pow(x, 3, q), []).append(x)
    fibers = sorted((sorted(v) for v in byval.values()), key=lambda f: f[0])
    assert all(len(f) == shape.ell for f in fibers), \
        "phi=[X^3:1] must have all fibers of size ell"

    # D = four full ell-fibers + a t-point tail taken from a fifth fiber
    chosen = fibers[seed:seed + 5]
    D = sorted(chosen[0] + chosen[1] + chosen[2] + chosen[3]
               + chosen[4][:shape.t])
    assert len(D) == shape.e
    fibers_of_D = [chosen[0], chosen[1], chosen[2], chosen[3],
                   chosen[4][:shape.t]]

    rest = [x for x in H if x not in set(D)]
    Core = sorted(rest[:shape.core])
    Out = sorted(rest[shape.core:])          # H \ D \ Core
    assert len(Core) == shape.core and len(D) + len(Core) + len(Out) == n

    # selected slopes: must have EMPTY phi-fiber in H (so z_lambda = 0 and
    # LEMMA A is satisfiable), i.e. alpha/beta is not a cube in H.
    cubes = set(pow(x, 3, q) for x in H)
    slopes = [(1, b) for b in range(q)] + [(0, 1)]
    empty = [(a, b) for (a, b) in slopes
             if b == 0 or (a * inv(b, q)) % q not in cubes]
    assert len(empty) >= 2, "need two empty-fiber slopes"
    lam1, lam2 = empty[0], empty[1]
    assert (lam1[0] * lam2[1] - lam1[1] * lam2[0]) % q != 0

    return dict(H=H, idx=idx, P=P, Q=Q, fibers=fibers, D=D,
                fibers_of_D=fibers_of_D, Core=Core, Out=Out,
                lam1=lam1, lam2=lam2, slopes=slopes)


def deficiency_rank(cfg, shape, B1, B2):
    """dim of {(S_1,S_2): deg<d, S_1 E + S_2 E' = 0 on H}.

    Scalar-free: the pointwise conditions depend only on the projective
    direction of (E,E'), i.e. on the partition and on phi.
    """
    q, d = shape.q, shape.d
    lam1, lam2 = cfg["lam1"], cfg["lam2"]
    rows = []
    ncols = 2 * d

    def powers(x):
        out, v = [], 1
        for _ in range(d):
            out.append(v)
            v = (v * x) % q
        return out

    for B, (al, be) in ((B1, lam1), (B2, lam2)):
        for x in B:
            pw = powers(x)
            # beta*S_1(x) - alpha*S_2(x) = 0
            rows.append([(be * c) % q for c in pw]
                        + [(-al * c) % q for c in pw])
    for x in cfg["Out"]:
        pw = powers(x)
        Px, Qx = pow(x, 3, q), 1
        # Q(x) S_1(x) - P(x) S_2(x) = 0
        rows.append([(Qx * c) % q for c in pw]
                    + [(-Px * c) % q for c in pw])
    rk = rank_mod(rows, ncols, q)
    return ncols - rk, len(rows)


def ray_agreements(cfg, shape, B1, B2):
    """agr(nu) for every nu in P^1, from the scalar-free decomposition
    agr(nu) = |Core| + |psi^{-1}(nu) ^ D| + |phi^{-1}(nu) ^ Out|."""
    q = shape.q
    lam1, lam2 = cfg["lam1"], cfg["lam2"]
    agr = {}
    for nu in cfg["slopes"]:
        a = shape.core
        if nu == lam1:
            a += len(B1)
        if nu == lam2:
            a += len(B2)
        # phi(x) = [x^3 : 1]; phi(x) == nu=[al:be] iff be*x^3 == al
        al, be = nu
        for x in cfg["Out"]:
            if (be * pow(x, 3, q) - al) % q == 0:
                a += 1
        agr[nu] = a
    return agr


def main():
    shape = Shape(h=25, k=4, q=229)
    cfg = build(shape)
    q = shape.q

    report = {"shape": repr(shape), "checks": 0, "fails": []}

    def chk(cond, label, info=""):
        report["checks"] += 1
        if not cond:
            report["fails"].append([label, info])

    # ---- sanity on the shape (pinned, not chosen)
    chk(shape.ell == 3 and shape.r == 7 and shape.d == 18
        and shape.sigma == 0 and shape.e == 14 and shape.t == 2,
        "shape-pinned", repr(shape))
    chk(shape.ell > shape.sigma + 2, "ell>sigma+2-holds")
    chk(shape.n == 57 and shape.A == 29 and shape.core == 22, "shape-nums")

    # ---- exhaustive over ALL partitions of D into two r-blocks
    D = cfg["D"]
    fod = cfg["fibers_of_D"]
    tally = Counter()
    realised = Counter()
    examples = {}
    defect_dims = Counter()

    for B1t in itertools.combinations(D, shape.r):
        B1 = list(B1t)
        if B1[0] != D[0]:            # kill the B1<->B2 swap double count
            continue
        B2 = [x for x in D if x not in set(B1)]
        c1, c2 = classify(B1, fod), classify(B2, fod)
        kind = "rigid" if (c1 == "rigid" and c2 == "rigid") else (
            "strong" if "strong" in (c1, c2) else "weak")
        tally[kind] += 1

        # --- LEMMA A: block must avoid its own slope's fiber.
        # lam1, lam2 have EMPTY H-fibers, so this holds for every partition.
        okA = True

        # --- ray agreements: exactly two live slopes, both at exact A
        agr = ray_agreements(cfg, shape, B1, B2)
        mx = max(agr.values())
        live = [nu for nu, a in agr.items() if a == mx]
        okLive = (mx == shape.A and len(live) == 2
                  and set(live) == {cfg["lam1"], cfg["lam2"]})

        # --- deficiency: dim K_d must be exactly c = sigma+1 = 1
        dim, nrows = deficiency_rank(cfg, shape, B1, B2)
        defect_dims[(kind, dim)] += 1
        okDef = (dim == shape.c)

        if okA and okLive and okDef:
            realised[kind] += 1
            examples.setdefault(kind, {"B1": B1, "B2": B2,
                                       "c1": c1, "c2": c2, "dim": dim})

    report["partitions_by_kind"] = dict(tally)
    report["realised_by_kind"] = dict(realised)
    report["dim_histogram"] = {f"{k0}:{k1}": v
                               for (k0, k1), v in sorted(defect_dims.items())}
    report["examples"] = examples

    # ---- the (FR) verdict at this shape
    fr_holds = (realised["strong"] == 0 and realised["weak"] == 0)
    report["FR_F1_strong_violation_realised"] = realised["strong"]
    report["FR_F2_weak_violation_realised"] = realised["weak"]
    report["FR_compliant_realised"] = realised["rigid"]
    report["FR_verdict_at_shape"] = ("HOLDS (0-liveness)" if fr_holds
                                     else "REFUTED at this shape")
    chk(realised["rigid"] > 0, "FR-F8-shape-nonvacuous",
        "no (FR)-compliant realised partition -> toy vacuous")

    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "toy.json"), "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True, default=str)
    print(json.dumps({k: v for k, v in report.items()
                      if k != "examples"}, indent=1, sort_keys=True,
                     default=str))
    return 1 if report["fails"] else 0


if __name__ == "__main__":
    sys.exit(main())
