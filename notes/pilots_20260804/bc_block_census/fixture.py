#!/usr/bin/env python3
"""bc_block_census -- verifier 2: MULTI-TARGET fixtures and the reuse law.

Round 14 measured |Bset| = 2 at |Tau| = 1 (eight runs, one shape).
Verifier 1 proved |Tau| = 1 was FORCED there by a pigeonhole that fails by
exactly t-1.  This file leaves the round-14 n-pinning and builds fixtures
with |Tau| = 2, then measures

    |Bset| (distinct blocks)   vs   2|Tau| (the (nu,tau) pair count)

EXHAUSTIVELY over the whole family q^K, under the full admissibility stack
including an EXHAUSTIVE tangent gate.

Gate devices (pre-registered, PREREG.md sec. 5):
  (a) BUCKETING.  A competitor F (deg < k) with agr(F,U_nu) >= thr+1 agrees
      with U_nu on >= thr+1-(k-1) =: need points of T = H\\Core_0 (U_nu
      vanishes on Core_0, and a nonzero F has <= k-1 roots).  If T is split
      into g buckets with g*(k-1) < need, some bucket holds k agreement
      points, so enumerating k-subsets INSIDE buckets is EXHAUSTIVE.
      g_max = (need-1)//(k-1).
  (b) SLOPE-FREENESS.  U_nu = alpha u + beta v is linear in (alpha,beta), so
      for a fixed interpolation set S the residuals R_u = u-F_u, R_v = v-F_v
      settle every slope at once: x agrees iff [alpha:beta]=[R_v(x):-R_u(x)].
      One per-row histogram replaces the loop over P^1.  F == 0 separately.

Both devices are validated by a POSITIVE CONTROL on the audited round-14
witness: run at threshold A-1 the search must FIND the over-agreement it is
designed to find; run at threshold A it must find none (reproducing the
round-14 verdict gate_max = A = 29).

Round-14 machinery is imported READ-ONLY.

Run: tools/ramguard local -- python3 \
       notes/pilots_20260804/bc_block_census/fixture.py
"""

import itertools
import json
import os
import random
import sys
from collections import Counter

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(os.path.dirname(HERE), "fr_fiber_rigidity")
sys.path.insert(0, FR)
from toy import inv, subgroup, rank_mod          # noqa: E402  (read-only)

CHECKS = []


def chk(cond, name, info=""):
    CHECKS.append({"name": name, "ok": bool(cond), "info": str(info)})
    return bool(cond)


def _modpow(a, e, q):
    r = np.ones_like(a)
    b = a % q
    while e:
        if e & 1:
            r = (r * b) % q
        b = (b * b) % q
        e >>= 1
    return r


# --------------------------------------------------------------- shapes

class BShape:
    """Boundary shape with n FREE (the round-14 pinning n=3d+k-c dropped)."""

    def __init__(self, h, k, q, n, tag=""):
        self.h, self.k, self.q, self.n, self.tag = h, k, q, n, tag
        self.ell = (h - 4) // 7
        self.r = 2 * self.ell + 1
        self.d = h - self.r
        self.sigma = self.d - self.ell - 1 - 2 * self.r
        self.e = 2 * self.r
        self.t = self.e - 4 * self.ell
        self.K = k - self.ell
        self.core = k + self.d
        self.A = k + h
        assert self.sigma == 0 and self.t == 2
        assert self.ell > self.sigma + 2, "load-bearing ell > sigma+2"
        assert (q - 1) % n == 0 and n % 3 == 0
        assert self.core + self.e <= n
        assert self.K >= 1

    def two_target_margin(self):
        return (self.n - self.e) - (2 * self.core - (self.K - 1))

    def above_johnson(self):
        return self.A * self.A > self.k * self.n

    def __repr__(self):
        return (f"{self.tag} h={self.h} ell={self.ell} r={self.r} d={self.d} "
                f"sigma={self.sigma} e={self.e} t={self.t} k={self.k} "
                f"K={self.K} n={self.n} q={self.q} A={self.A} "
                f"core={self.core} margin={self.two_target_margin()} "
                f"{'ABOVE' if self.above_johnson() else 'BELOW'}-Johnson")


def ground(shape, seed=0):
    q, n = shape.q, shape.n
    H = subgroup(q, n)
    byval = {}
    for x in H:
        byval.setdefault(pow(x, 3, q), []).append(x)
    fibers = sorted((sorted(v) for v in byval.values()), key=lambda f: f[0])
    assert all(len(f) == shape.ell for f in fibers)
    chosen = fibers[seed:seed + 5]
    D = sorted(chosen[0] + chosen[1] + chosen[2] + chosen[3]
               + chosen[4][:shape.t])
    assert len(D) == shape.e
    HD = [x for x in H if x not in set(D)]
    cubes = set(pow(x, 3, q) for x in H)
    slopes = [(1, b) for b in range(q)] + [(0, 1)]
    empty = [(a, b) for (a, b) in slopes
             if b == 0 or (a * inv(b, q)) % q not in cubes]
    assert len(empty) >= 4
    return dict(H=H, D=D, HD=HD, fibers_of_D=[chosen[0], chosen[1],
                chosen[2], chosen[3], chosen[4][:shape.t]],
                slopes=slopes, empty=empty[:6])


def Lval(nu, x, q):
    a, b = nu
    return (a - b * pow(x, 3, q)) % q


def canon_slope(E, Ep, q):
    """The unique nu = [alpha:beta] with alpha*E + beta*Ep = 0."""
    if Ep % q:
        return (1, (-E * inv(Ep, q)) % q)
    return (0, 1)


# ------------------------------------------------------- the construction

def build_fixture(shape, g, flavour, seed=1):
    """Received residual pair (u,v) carrying TWO prescribed targets.

    tau_1 = 0        with partition (B1 -> lam1, D\\B1 -> lam2)
    tau_2 = c  != 0  with partition (B2 -> mu1,  D\\B2 -> mu2)
    flavour 'reuse'   : B2 = B1       -> both targets share ONE partition
    flavour 'noreuse' : B2 not in {B1, D\\B1} -> four distinct blocks
    """
    q, r = shape.q, shape.r
    D, HD = g["D"], g["HD"]
    rng = random.Random(seed)
    lam1, lam2, mu1, mu2 = g["empty"][:4]
    c = rng.randrange(1, q)

    B1 = D[:r]
    B2 = list(B1) if flavour == "reuse" else D[:r - 2] + D[r:r + 2]
    assert len(B2) == r
    if flavour == "noreuse":
        assert set(B2) != set(B1) and set(B2) != set(D) - set(B1)

    assert 2 * shape.core <= len(HD) + (shape.K - 1)
    perm = list(HD)
    rng.shuffle(perm)
    C1 = sorted(perm[:shape.core])
    C2 = sorted(perm[shape.core:2 * shape.core])
    rest = sorted(perm[2 * shape.core:])

    m = {x: 0 for x in C1}
    m.update({x: c for x in C2})
    for x in rest:
        while True:
            val = rng.randrange(1, q)
            if val != c:
                m[x] = val
                break

    u, v = {}, {}
    for x in HD:
        u[x] = m[x] % q
        v[x] = (-m[x] * pow(x, 3, q)) % q

    sB1, sB2 = set(B1), set(B2)
    for x in D:
        nu1 = lam1 if x in sB1 else lam2
        nu2 = mu1 if x in sB2 else mu2
        a1, b1 = nu1
        a2, b2 = nu2
        delta = (a2 * b1 - b2 * a1) % q
        assert delta % q != 0
        s = (c * Lval(nu2, x, q) % q) * inv(delta, q) % q
        assert s % q != 0
        u[x] = (s * b1) % q
        v[x] = (-s * a1) % q

    return dict(u=u, v=v, m=m, C1=C1, C2=C2, rest=rest, c=c,
                B1=sorted(B1), B2=sorted(B2), lam1=lam1, lam2=lam2,
                mu1=mu1, mu2=mu2, flavour=flavour)


# ------------------------------------------------- exhaustive tangent gate

def buckets_for(T, need, k):
    """Largest g with g*(k-1) < need; balanced buckets of size >= k."""
    g = (need - 1) // (k - 1) if k > 1 else len(T)
    g = max(1, min(g, len(T) // k))
    out = [[] for _ in range(g)]
    for i, x in enumerate(T):
        out[i % g].append(x)
    assert g * (k - 1) < need, "bucketing would not be exhaustive"
    assert all(len(b) >= k for b in out)
    return out


def gate_search(H, u, v, core0, k, q, threshold, chunk=2500):
    """Exhaustive over every deg<k codeword that could beat `threshold`."""
    Hs = np.array(H, dtype=np.int64)
    pos = {x: i for i, x in enumerate(H)}
    ua = np.array([u[x] for x in H], dtype=np.int64)
    va = np.array([v[x] for x in H], dtype=np.int64)
    T = [x for x in H if x not in set(core0)]
    need = threshold + 1 - (k - 1)
    bks = buckets_for(T, need, k)
    n = len(H)

    best, subsets = 0, 0
    for bk in bks:
        idxs = np.array([pos[x] for x in bk], dtype=np.int64)
        combos = np.array(list(itertools.combinations(range(len(bk)), k)),
                          dtype=np.int64)
        subs = idxs[combos]
        for st in range(0, subs.shape[0], chunk):
            sc = subs[st:st + chunk]
            m = sc.shape[0]
            subsets += m
            xs = Hs[sc]
            diff = (Hs[None, None, :] - xs[:, :, None]) % q
            dd = (xs[:, :, None] - xs[:, None, :]) % q
            L = np.ones((m, k, n), dtype=np.int64)
            den = np.ones((m, k), dtype=np.int64)
            for j in range(k):
                for i in range(k):
                    if i == j:
                        continue
                    L[:, j, :] = (L[:, j, :] * diff[:, i, :]) % q
                    den[:, j] = (den[:, j] * dd[:, j, i]) % q
            L = (L * _modpow(den, q - 2, q)[:, :, None]) % q
            Fu = np.zeros((m, n), dtype=np.int64)
            Fv = np.zeros((m, n), dtype=np.int64)
            for j in range(k):
                Fu = (Fu + ua[sc[:, j]][:, None] * L[:, j, :]) % q
                Fv = (Fv + va[sc[:, j]][:, None] * L[:, j, :]) % q
            Ru = (ua[None, :] - Fu) % q
            Rv = (va[None, :] - Fv) % q
            both0 = (Ru == 0) & (Rv == 0)
            zeros = both0.sum(axis=1)
            key = np.where(Rv != 0,
                           (-Ru * _modpow(Rv, q - 2, q)) % q, q)
            key = np.where(both0, q + 1, key)
            base = (np.arange(m) * (q + 2))[:, None]
            cnt = np.bincount((base + key).ravel(),
                              minlength=m * (q + 2)).reshape(m, q + 2)
            mx = cnt[:, :q + 1].max(axis=1) + zeros
            best = max(best, int(mx.max()))
    # the F == 0 competitor
    hist0, z0 = Counter(), 0
    for x in H:
        if u[x] % q == 0 and v[x] % q == 0:
            z0 += 1
        else:
            hist0[canon_slope(u[x], v[x], q)] += 1
    best = max(best, z0 + (max(hist0.values()) if hist0 else 0))
    return {"max_found": best, "threshold": threshold, "buckets": len(bks),
            "bucket_sizes": [len(b) for b in bks], "subsets": subsets,
            "need_in_T": need, "T": len(T)}


# ---------------------------------------------------- exhaustive census

def census(shape, g, fx):
    """EXHAUSTIVE over all q^K targets tau of degree < K."""
    q, K, r = shape.q, shape.K, shape.r
    H, D, HD = g["H"], g["D"], g["HD"]
    u, v = fx["u"], fx["v"]
    slopes = g["slopes"]
    cube = {x: pow(x, 3, q) for x in H}

    HDa = np.array(HD, dtype=np.int64)
    ma = np.array([fx["m"][x] for x in HD], dtype=np.int64)
    # all coefficient vectors of deg < K, chunked
    cand = []
    total = q ** K
    CH = 20000
    for st in range(0, total, CH):
        idxs = np.arange(st, min(st + CH, total), dtype=np.int64)
        coefs = []
        tmp = idxs.copy()
        for _ in range(K):
            coefs.append(tmp % q)
            tmp //= q
        TAU = np.zeros((len(idxs), len(HD)), dtype=np.int64)
        for j in range(K - 1, -1, -1):
            TAU = (TAU * HDa[None, :] + coefs[j][:, None]) % q
        hit = (TAU == ma[None, :]).sum(axis=1)
        for w in np.nonzero(hit == shape.core)[0]:
            cand.append(tuple(int(c[w]) for c in coefs))

    targets = []
    for coef in cand:
        def tv(x, coef=coef):
            acc = 0
            for cc in reversed(coef):
                acc = (acc * x + cc) % q
            return acc
        E = {x: (u[x] - tv(x)) % q for x in H}
        Ep = {x: (v[x] + cube[x] * tv(x)) % q for x in H}
        core = [x for x in H if E[x] == 0 and Ep[x] == 0]
        if len(core) != shape.core:
            continue
        if any(x in set(D) for x in core):
            continue
        hist, slope_at = Counter(), {}
        for x in D:
            nu = canon_slope(E[x], Ep[x], q)
            slope_at[x] = nu
            hist[nu] += 1
        big = sorted(nu for nu, cnt in hist.items() if cnt == r)
        if len(big) != 2 or hist[big[0]] + hist[big[1]] != shape.e:
            continue
        agr = {}
        for nu in slopes:
            a, b = nu
            agr[nu] = sum(1 for x in H if (a * E[x] + b * Ep[x]) % q == 0)
        mx = max(agr.values())
        live = sorted(nu for nu, aa in agr.items() if aa == mx)
        if mx != shape.A or len(live) != 2 or live != big:
            continue
        blocks = [tuple(sorted(x for x in D if slope_at[x] == nu))
                  for nu in big]
        targets.append({"coef": coef, "slopes": big, "blocks": blocks})

    bset = set()
    for tg in targets:
        bset.update(tg["blocks"])
    parts = set(frozenset(map(frozenset, tg["blocks"])) for tg in targets)
    return {"family_size_qK": total, "core_candidates": len(cand),
            "n_targets": len(targets), "pair_count_2Tau": 2 * len(targets),
            "Bset_distinct": len(bset), "partitions": len(parts),
            "reuse_ratio_2Tau_over_Bset": (
                round(2 * len(targets) / len(bset), 4) if bset else None),
            "targets": [{"coef": t["coef"], "slopes": t["slopes"],
                         "blocks": [list(b) for b in t["blocks"]]}
                        for t in targets]}


# ---------------------------------------------------- admissibility stack

def admissibility(shape, g, fx, cen):
    q, r = shape.q, shape.r
    H, D = g["H"], g["D"]
    u, v = fx["u"], fx["v"]
    tag = f"{shape.tag}/{fx['flavour']}"
    Dr = sorted(x for x in H if (pow(x, 3, q) * u[x] + v[x]) % q != 0)
    chk(Dr == sorted(D), f"[{tag}] AD1 D = supp(rho)")
    chk(cen["n_targets"] >= 2, f"[{tag}] fixture carries >= 2 targets",
        cen["n_targets"])
    shared = Counter()
    for tg in cen["targets"]:
        b0, b1 = tg["blocks"]
        chk(len(b0) == r and len(b1) == r, f"[{tag}] AD6 |B| = h-d = r")
        chk(not (set(b0) & set(b1)), f"[{tag}] AD6 blocks disjoint")
        chk(len(set(b0) | set(b1)) == shape.e,
            f"[{tag}] TKS2 leftover <= sigma = 0")
        for b in tg["blocks"]:
            shared[tuple(b)] += 1
    # BC-F2: the REUSE LAW -- sharing one block forces sharing both
    pairs = [frozenset(map(frozenset, tg["blocks"])) for tg in cen["targets"]]
    ok_law = True
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            inter = len(pairs[i] & pairs[j])
            if inter == 1:
                ok_law = False
    chk(ok_law, f"[{tag}] BC-F2 REUSE LAW: no two targets share exactly "
                f"one block")
    chk(cen["Bset_distinct"] == 2 * cen["partitions"],
        f"[{tag}] |Bset| = 2 * #partitions",
        f"{cen['Bset_distinct']} vs {2 * cen['partitions']}")
    rows, ncols = [], 2 * shape.d

    def powers(x):
        out, w = [], 1
        for _ in range(shape.d):
            out.append(w)
            w = (w * x) % q
        return out
    for x in H:
        pw = powers(x)
        rows.append([(u[x] * cc) % q for cc in pw]
                    + [(v[x] * cc) % q for cc in pw])
    dimKd = ncols - rank_mod(rows, ncols, q)
    chk(dimKd == shape.sigma + 1, f"[{tag}] dim K_d = sigma+1", dimKd)
    return {"dim_K_d": dimKd}


def run_shape(shape, seed=1):
    g = ground(shape)
    out = {"shape": repr(shape), "above_johnson": shape.above_johnson(),
           "cases": {}}
    for fl in ("reuse", "noreuse"):
        fx = build_fixture(shape, g, fl, seed=seed)
        cen = census(shape, g, fx)
        adm = admissibility(shape, g, fx, cen)
        gate = gate_search(g["H"], fx["u"], fx["v"], fx["C1"], shape.k,
                           shape.q, shape.A)
        holds = gate["max_found"] <= shape.A
        chk(holds, f"[{shape.tag}/{fl}] TANGENT GATE holds (exhaustive)",
            f"max={gate['max_found']} A={shape.A}")
        gate["gate_holds"] = holds
        out["cases"][fl] = {"census": cen, "admissibility": adm,
                            "gate": gate, "B1": fx["B1"], "B2": fx["B2"]}
    return out


# ------------------------------------------------------ positive control

def fr_control():
    """Validate the new gate machinery on the AUDITED round-14 witness."""
    from toy import Shape, build, classify            # noqa
    from gate import build_words                      # noqa
    shp = Shape(h=25, k=4, q=229)
    cfg = build(shp)
    fod, D = cfg["fibers_of_D"], cfg["D"]
    rng = random.Random(20260806)
    split = None
    for B1t in itertools.combinations(D, shp.r):
        B1 = list(B1t)
        if B1[0] != D[0]:
            continue
        B2 = [x for x in D if x not in set(B1)]
        c1, c2 = classify(B1, fod), classify(B2, fod)
        if "strong" in (c1, c2) and any(
                len(F) == 3 and len(set(F) & set(B1)) == 2 for F in fod):
            split = (B1, B2)
            break
    E, Ep = build_words(cfg, shp, split[0], split[1], rng)
    at_A = gate_search(cfg["H"], E, Ep, cfg["Core"], shp.k, shp.q, shp.A)
    at_Am1 = gate_search(cfg["H"], E, Ep, cfg["Core"], shp.k, shp.q,
                         shp.A - 1)
    chk(at_A["max_found"] <= shp.A,
        "[FR-CONTROL] bucketed gate reproduces round-14 verdict at A=29",
        f"max={at_A['max_found']} vs round-14 gate_max_agreement=29")
    chk(at_Am1["max_found"] >= shp.A,
        "[FR-CONTROL] positive control: at threshold A-1 the search FINDS "
        "the over-agreement",
        f"max={at_Am1['max_found']} >= A={shp.A}")
    return {"at_A": at_A, "at_A_minus_1": at_Am1,
            "round14_reported_gate_max": 29,
            "round14_search_size": 52360}


def main():
    report = {"fr_control": fr_control()}
    shapes = [
        BShape(h=25, k=5, q=61, n=60, tag="A2-above"),     # K=2, above Johnson
        BShape(h=25, k=4, q=61, n=60, tag="A1-above"),     # K=1, above Johnson
        BShape(h=25, k=4, q=853, n=213, tag="B1-below"),   # K=1, below Johnson
        BShape(h=25, k=5, q=367, n=183, tag="B2-below"),   # K=2, below Johnson
    ]
    for shp in shapes:
        chk(shp.two_target_margin() >= 0, f"[{shp.tag}] has 2-target room",
            shp.two_target_margin())
        report[shp.tag] = run_shape(shp)

    report["checks"] = len(CHECKS)
    report["failed"] = [c for c in CHECKS if not c["ok"]]
    with open(os.path.join(HERE, "fixture.json"), "w") as fh:
        json.dump({"report": report, "all_checks": CHECKS}, fh, indent=1,
                  sort_keys=True, default=str)
    slim = json.loads(json.dumps(report, default=str))
    for kk in list(slim):
        if isinstance(slim[kk], dict) and "cases" in slim[kk]:
            for fl in slim[kk]["cases"]:
                slim[kk]["cases"][fl]["census"].pop("targets", None)
    print(json.dumps(slim, indent=1, sort_keys=True, default=str))
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
