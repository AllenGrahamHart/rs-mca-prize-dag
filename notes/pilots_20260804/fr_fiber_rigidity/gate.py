#!/usr/bin/env python3
"""fr_fiber_rigidity -- verifier 3: the TANGENT GATE on explicit received
words, for a fiber-SPLITTING configuration and a fiber-RIGID one.

The scalar-free stack (toy.py) is blind to the received words themselves.
Everything that can still separate a splitting partition from a rigid one
lives here: the band-admissibility ("tangent") gate

    max { agr(F, alpha u + beta v) : deg F < k } = A = k+h,

i.e. no codeword beats the exact-A level.  This is the L-B over-agreement
mechanism and route (1)/(2) of the brief.

COMPLETENESS of the search.  |Core| = k+d and U_nu vanishes on Core.  A
NONZERO codeword F of degree < k has at most k-1 roots, so it can agree
with U_nu on at most k-1 points of Core; if agr(F,U_nu) >= A+1 then F
agrees with U_nu on at least A+1-(k-1) points of T = H\\Core.  For the
pinned shape that is >= 27 of the 35 points of T, so F is determined by
some 4-subset of T.  Enumerating every 4-subset of T is therefore an
EXHAUSTIVE search over nonzero competitors.  F == 0 gives agr = agr_0(nu)
which is checked separately.

Run: tools/ramguard local -- python3 \
       notes/pilots_20260804/fr_fiber_rigidity/gate.py
"""

import itertools
import json
import os
import random
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from toy import Shape, build, classify, deficiency_rank, ray_agreements  # noqa


def build_words(cfg, shape, B1, B2, rng):
    """Explicit (u,v) = (E, E') for the counted pair (f,g) = (0,0)."""
    q = shape.q
    H = cfg["H"]
    lam1, lam2 = cfg["lam1"], cfg["lam2"]
    E = {x: 0 for x in H}
    Ep = {x: 0 for x in H}
    for B, (al, be) in ((B1, lam1), (B2, lam2)):
        for x in B:
            c = rng.randrange(1, q)
            # (E,E') = c * (beta, -alpha)  =>  alpha E + beta E' = 0
            E[x] = (c * be) % q
            Ep[x] = (-c * al) % q
    for x in cfg["Out"]:
        m = rng.randrange(1, q)
        # (E,E') = m * (Q, -P) = m * (1, -x^3)
        E[x] = m % q
        Ep[x] = (-m * pow(x, 3, q)) % q
    # Core keeps E = E' = 0
    return E, Ep


def _modpow(a, e, q):
    """Elementwise a**e mod q for an int64 array (exact; q^2 < 2^63)."""
    r = np.ones_like(a)
    b = a % q
    while e:
        if e & 1:
            r = (r * b) % q
        b = (b * b) % q
        e >>= 1
    return r


def lagrange_tables(Hs, Ts, k, q):
    """Slope-INDEPENDENT precomputation: every k-subset of Ts, and the
    Lagrange basis of each subset evaluated on all of Hs."""
    Ha = np.array(Hs, dtype=np.int64)
    pos = {x: i for i, x in enumerate(Hs)}
    subs = np.array(list(itertools.combinations(
        [pos[x] for x in Ts], k)), dtype=np.int64)
    xs = Ha[subs]                                        # (m,k)
    diff = (Ha[None, None, :] - xs[:, :, None]) % q      # (m,k,n)
    dd = (xs[:, :, None] - xs[:, None, :]) % q           # (m,k,k)
    m = subs.shape[0]
    L = np.ones((m, k, len(Hs)), dtype=np.int64)
    den = np.ones((m, k), dtype=np.int64)
    for j in range(k):
        for i in range(k):
            if i == j:
                continue
            L[:, j, :] = (L[:, j, :] * diff[:, i, :]) % q
            den[:, j] = (den[:, j] * dd[:, j, i]) % q
    L = (L * _modpow(den, q - 2, q)[:, :, None]) % q
    return subs, L


def max_codeword_agreement(Hs, z, k, q, tables):
    """Exact max over ALL nonzero deg<k codewords of |{x: F(x)=z(x)}|."""
    subs, L = tables
    za = np.array([z[x] for x in Hs], dtype=np.int64)
    zs = za[subs]                                        # (m,k)
    F = np.zeros((subs.shape[0], len(Hs)), dtype=np.int64)
    for j in range(k):
        F = (F + zs[:, j, None] * L[:, j, :]) % q
    return int((F == za[None, :]).sum(axis=1).max())


def run_case(cfg, shape, B1, B2, label, rng, slopes=None, tables=None):
    q = shape.q
    H, Core = cfg["H"], cfg["Core"]
    T = [x for x in H if x not in set(Core)]
    if tables is None:
        tables = lagrange_tables(H, T, shape.k, q)
    E, Ep = build_words(cfg, shape, B1, B2, rng)

    # --- re-derive the blocks from the words (no shortcuts)
    def block(nu):
        al, be = nu
        return sorted(x for x in cfg["D"]
                      if (al * E[x] + be * Ep[x]) % q == 0)

    out = {"label": label, "checks": 0, "fails": []}

    def chk(cond, name, info=""):
        out["checks"] += 1
        if not cond:
            out["fails"].append([name, info])

    chk(block(cfg["lam1"]) == sorted(B1), "block1-reconstructed")
    chk(block(cfg["lam2"]) == sorted(B2), "block2-reconstructed")
    chk(sorted(x for x in H if E[x] == 0 and Ep[x] == 0) == sorted(Core),
        "joint-core-exact")
    chk(len(Core) == shape.core, "core-size")

    # --- rho is nonzero exactly on D  (AD1)
    Dr = sorted(x for x in H
                if (pow(x, 3, q) * E[x] + Ep[x]) % q != 0)
    chk(Dr == sorted(cfg["D"]), "AD1-D-is-rho-support")

    # --- liveness over all of P^1 from the actual words
    agr0 = {}
    for nu in cfg["slopes"]:
        al, be = nu
        agr0[nu] = sum(1 for x in H if (al * E[x] + be * Ep[x]) % q == 0)
    mx = max(agr0.values())
    live = sorted(nu for nu, a in agr0.items() if a == mx)
    chk(mx == shape.A, "liveness-exact-A", f"max={mx} A={shape.A}")
    chk(live == sorted([cfg["lam1"], cfg["lam2"]]), "two-live-slopes",
        str(live))

    # --- the TANGENT GATE
    if slopes is None:
        slopes = cfg["slopes"]
    worst = 0
    worst_nu = None
    for nu in slopes:
        al, be = nu
        z = {x: (al * E[x] + be * Ep[x]) % q for x in H}
        mm = max_codeword_agreement(H, z, shape.k, q, tables)
        mm = max(mm, agr0[nu])          # include F == 0
        if mm > worst:
            worst, worst_nu = mm, nu
    chk(worst <= shape.A, "TANGENT-GATE",
        f"max codeword agreement {worst} at nu={worst_nu}, A={shape.A}")
    out["gate_max_agreement"] = worst
    out["gate_slopes_checked"] = len(slopes)
    out["A"] = shape.A
    out["admissible"] = not out["fails"]
    return out


def main():
    shape = Shape(h=25, k=4, q=229)
    cfg = build(shape)
    fod = cfg["fibers_of_D"]
    D = cfg["D"]
    rng = random.Random(20260806)

    # one fiber-RIGID partition and one STRONGLY fiber-splitting partition
    rigid = None
    split = None
    for B1t in itertools.combinations(D, shape.r):
        B1 = list(B1t)
        if B1[0] != D[0]:
            continue
        B2 = [x for x in D if x not in set(B1)]
        c1, c2 = classify(B1, fod), classify(B2, fod)
        if c1 == "rigid" and c2 == "rigid" and rigid is None:
            rigid = (B1, B2)
        if "strong" in (c1, c2) and split is None:
            # want the strongest witness: a fiber split 2-1
            ok = False
            for F in fod:
                if len(F) == 3 and len(set(F) & set(B1)) == 2:
                    ok = True
            if ok:
                split = (B1, B2)
        if rigid and split:
            break
    assert rigid and split

    report = {"shape": repr(shape), "cases": []}
    all_slopes = cfg["slopes"]
    Tset = [x for x in cfg["H"] if x not in set(cfg["Core"])]
    tables = lagrange_tables(cfg["H"], Tset, shape.k, shape.q)
    report["gate_search_size"] = int(tables[0].shape[0])
    for label, (B1, B2) in (("FR-rigid", rigid), ("FR-splitting", split)):
        res = run_case(cfg, shape, B1, B2, label, rng, slopes=all_slopes,
                       tables=tables)
        res["B1"] = B1
        res["B2"] = B2
        res["fiber_profile_B1"] = [len(set(F) & set(B1)) for F in fod]
        res["fiber_profile_B2"] = [len(set(F) & set(B2)) for F in fod]
        res["D_fiber_sizes"] = [len(F) for F in fod]
        report["cases"].append(res)

    report["verdict"] = (
        "FR-F1 FIRES: a fiber-splitting selected block is fully admissible"
        if all(c["admissible"] for c in report["cases"])
        else "at least one case failed a check -- see fails")
    with open(os.path.join(HERE, "gate.json"), "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=True, default=str)
    print(json.dumps(report, indent=1, sort_keys=True, default=str))
    return 0 if all(not c["fails"] for c in report["cases"]) else 1


if __name__ == "__main__":
    sys.exit(main())
