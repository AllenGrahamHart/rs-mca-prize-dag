#!/usr/bin/env python3
"""RowC window pilot -- part 3: exact toy-scale replicas of the window regime.

    tools/ramguard local -- python3 \
        notes/pilots_20260802/rowc_window/toy.py [--self-test] [--only NAME]

QUESTION MEASURED
-----------------
Inside the RowC 1/4 exposure band the first moment says a random received pair
has |Gamma_lo| ~ mu = C(n,A)/q^{h-1} >> 8n^3.  The only escape left for P-B is
that CONDITIONING ON ADMISSIBILITY (the T0-T4 strips + globally generic +
below cascade + v nowhere zero) suppresses Gamma_lo.  This file measures the
conditioning DIRECTLY, by exhaustive enumeration of every A-subset (and every
(A+1)- and (A-1)-subset, for the two gates), on a ladder of shapes whose
tangent-gate pressure runs from "free" (gate first moment 1e-4, as in the
window) to "harsh" (gate first moment ~2.5, only a few percent of pairs
admissible).

EXACT WITNESS CRITERION (proved, and self-tested against interpolation below):
for |S| = a, w in F_q^D,
    deg(interpolant of w|_S) < K  <=>  sum_{i in S} w_i x_i^s / Lambda'_S(x_i)
                                        = 0  for s = 0 .. a-K-1,
by expanding P_S/Lambda_S at infinity.  So each S carries (alpha(S), beta(S))
in F_q^H x F_q^H (H = a-K) built from (u,v), and

  * S is an exact witness support for the pencil at slope z  <=>  alpha + z
    beta = 0, i.e. the 2xH matrix [alpha;beta] has rank <= 1 (and beta != 0
    pins z uniquely; alpha = beta = 0 means every slope, a joint explanation).

Applying this at a = A gives the witnesses; at a = A+1 the T2 over-agreement
gate (agreement >= A+1 at some slope <=> some (A+1)-set is a witness set); at
a = A-1 the below-cascade gate (a joint codeword-pair explanation on an
(A-1)-support <=> alpha = beta = 0 there).

All arithmetic is exact in F_q (numpy int64 with explicit reduction).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from itertools import combinations
from math import comb

sys.dont_write_bytecode = True

import numpy as np  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def next_prime_1modn(x: int, n: int) -> int:
    from sympy import isprime
    q = x + ((1 - x) % n)
    while not isprime(q):
        q += n
    return q


def primitive_root(q: int) -> int:
    fac, m, d = [], q - 1, 2
    while d * d <= m:
        if m % d == 0:
            fac.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.append(m)
    for g in range(2, q):
        if all(pow(g, (q - 1) // p, q) != 1 for p in fac):
            return g
    raise RuntimeError


class Field:
    def __init__(self, q: int, n: int):
        assert (q - 1) % n == 0
        self.q, self.n = q, n
        self.g = primitive_root(q)
        self.pw = np.empty(q - 1, dtype=np.int64)
        v = 1
        for i in range(q - 1):
            self.pw[i] = v
            v = v * self.g % q
        self.dl = np.zeros(q, dtype=np.int64)
        self.dl[self.pw] = np.arange(q - 1)
        self.inv = np.zeros(q, dtype=np.int64)
        for i in range(1, q):
            self.inv[i] = pow(i, q - 2, q)
        w = pow(self.g, (q - 1) // n, q)
        self.x = np.array([pow(w, i, q) for i in range(n)], dtype=np.int64)
        assert len(set(self.x.tolist())) == n
        diff = (self.x[:, None] - self.x[None, :]) % q
        DL = np.zeros((n, n), dtype=np.int64)
        off = ~np.eye(n, dtype=bool)
        DL[off] = self.dl[diff[off]]
        self.DL = DL


class Level:
    """All a-subsets of D, with the H = a-K dual-weight vectors precomputed."""

    def __init__(self, F: Field, a: int, K: int):
        self.F, self.a, self.K = F, a, K
        self.H = a - K
        q = F.q
        self.idx = np.array(list(combinations(range(F.n), a)), dtype=np.int64)
        m = self.idx.shape[0]
        e = np.empty((m, a), dtype=np.int64)
        step = max(1, 3_000_000 // (a * a))
        for lo in range(0, m, step):
            ch = self.idx[lo:lo + step]
            e[lo:lo + step] = F.DL[ch[:, :, None],
                                   ch[:, None, :]].sum(axis=2) % (q - 1)
        W = F.pw[(-e) % (q - 1)]                       # 1/Lambda'_S(x_i)
        # WX[s] = W * x^s on the support, precomputed once
        self.WX = []
        xs = np.ones(F.n, dtype=np.int64)
        for s in range(self.H):
            self.WX.append(W * xs[self.idx] % q)
            xs = xs * F.x % q
        self.m = m

    def moments(self, u: np.ndarray) -> np.ndarray:
        q = self.F.q
        U = u[self.idx]
        out = np.empty((self.m, self.H), dtype=np.int64)
        for s in range(self.H):
            out[:, s] = (U * self.WX[s] % q).sum(axis=1) % q
        return out


def rank_le_1(a: np.ndarray, b: np.ndarray, q: int) -> np.ndarray:
    """rows where the 2xH matrix [a;b] has rank <= 1 (all 2x2 minors zero)."""
    H = a.shape[1]
    ok = np.ones(a.shape[0], dtype=bool)
    for s in range(H):
        for t in range(s + 1, H):
            ok &= ((a[:, s] * b[:, t] - a[:, t] * b[:, s]) % q == 0)
    return ok


def run_trial(F, cfg, LA, LP, LM, rng):
    q, n, A, K, h = F.q, F.n, cfg["A"], cfg["K"], cfg["h"]
    u = rng.integers(0, q, size=n)
    v = rng.integers(0, q, size=n)

    a = LA.moments(u)
    b = LA.moments(v)
    zero_a = (a == 0).all(axis=1)
    zero_b = (b == 0).all(axis=1)
    joint_A = int((zero_a & zero_b).sum())          # T0 / global genericity

    ok = rank_le_1(a, b, q) & (~zero_b)
    wit = np.nonzero(ok)[0]
    nz = np.argmax(b[wit] != 0, axis=1) if len(wit) else np.zeros(0, np.int64)
    z = ((-a[wit, nz]) * F.inv[b[wit, nz]]) % q if len(wit) else \
        np.zeros(0, np.int64)
    N = int(len(wit))

    uniq, counts = np.unique(z, return_counts=True) if N else \
        (np.zeros(0, np.int64), np.zeros(0, np.int64))
    n_live = int(len(uniq))
    max_mult = int(counts.max()) if n_live else 0

    masks = np.zeros(N, dtype=object)
    for i, j in enumerate(wit):
        masks[i] = int(np.bitwise_or.reduce(1 << LA.idx[j]))

    sel = {}
    for name in ("lex", "colex"):
        chosen = {}
        for i in range(N):
            key = tuple(LA.idx[wit[i]].tolist()) if name == "lex" else masks[i]
            zz = int(z[i])
            if zz not in chosen or key < chosen[zz][0]:
                chosen[zz] = (key, i)
        zs = sorted(chosen)
        mk = [masks[chosen[t][1]] for t in zs]
        hi = set()
        for i1 in range(len(zs)):
            for i2 in range(i1 + 1, len(zs)):
                if bin(int(mk[i1]) & int(mk[i2])).count("1") >= K:
                    hi.add(i1)
                    hi.add(i2)
        sel[name] = (len(zs), len(zs) - len(hi), len(hi))

    # T2 gate: any (A+1)-set that is a witness set at some slope
    ap = LP.moments(u)
    bp = LP.moments(v)
    t2 = int(rank_le_1(ap, bp, q).sum())

    # below cascade: joint explanation on an (A-1)-support
    am = LM.moments(u)
    cand = np.nonzero((am == 0).all(axis=1))[0]
    joint_Am1 = 0
    if len(cand):
        bmc = LM.moments(v)[cand]
        joint_Am1 = int((bmc == 0).all(axis=1).sum())

    vzero = int((v == 0).sum())
    degen = bool((u == 0).all() or (v == 0).all())
    if not degen and (u != 0).all():
        degen = bool(len(set(((v * F.inv[u]) % q).tolist())) == 1)
    fold = False
    M, gk = 2, int(np.gcd(n, K))
    while M <= gk:
        if gk % M == 0:
            st = n // M
            if (np.array_equal(u, np.roll(u, st)) and
                    np.array_equal(v, np.roll(v, st))):
                fold = True
        M *= 2

    adm = (joint_A == 0 and joint_Am1 == 0 and t2 == 0 and vzero == 0
           and not degen and not fold)
    return dict(N=N, n_live=n_live, max_mult=max_mult,
                gamma=sel["lex"][0], gamma_lo_lex=sel["lex"][1],
                gamma_hi_lex=sel["lex"][2], gamma_lo_colex=sel["colex"][1],
                joint_A=joint_A, joint_Am1=joint_Am1, t2=t2,
                vzero=vzero, degen=int(degen), fold=int(fold),
                admissible=int(adm))


def predict(cfg):
    n, A, K, h, q = cfg["n"], cfg["A"], cfg["K"], cfg["h"], cfg["q"]
    C = comb(n, A)
    mu = C / q ** (h - 1)
    pc = sum(comb(A, c) * comb(n - A, A - c) for c in range(K, A + 1)) / C
    return dict(C=C, mu=mu, mean_Wz=C / q ** h,
                gate_T2=comb(n, A + 1) / q ** (h + 1) * q,
                E_joint_A=C / q ** (2 * h),
                E_joint_Am1=comb(n, A - 1) / q ** (2 * (h - 1)),
                P_core_ge_K=pc,
                E_highcore_pairs=mu * mu * pc / 2,
                E_live=q * (1 - (1 - q ** -h) ** C) if h <= 3 else mu,
                var_pred=mu)


CONFIGS = [
    # ---- window-like: the tangent gate costs nothing, as at RowC 1/4 ----
    dict(name="W1", n=20, A=10, K=8, h=2, q=10061, trials=200),
    dict(name="W2", n=20, A=10, K=8, h=2, q=3001, trials=200),
    # ---- moderate gate pressure ----
    dict(name="M1", n=20, A=10, K=8, h=2, q=1021, trials=200),
    dict(name="M2", n=20, A=10, K=7, h=3, q=101, trials=200),
    # ---- harsh gate pressure: few pairs admissible ----
    dict(name="H1", n=20, A=10, K=8, h=2, q=241, trials=400),
    dict(name="H2", n=20, A=10, K=7, h=3, q=41, trials=400),
    dict(name="H3", n=20, A=10, K=6, h=4, q=41, trials=400),
    # ---- second domain size ----
    dict(name="D1", n=18, A=9, K=7, h=2, q=2431, trials=200),
    dict(name="D2", n=18, A=9, K=6, h=3, q=163, trials=200),
]


def self_test():
    q, n, A, K = 13, 12, 6, 4
    F = Field(q, n)
    L = Level(F, A, K)
    rng = np.random.default_rng(7)
    bad = checks = 0
    for _ in range(3):
        w = rng.integers(0, q, size=n)
        crit = (L.moments(w) == 0).all(axis=1)
        for j in range(L.m):
            S = L.idx[j]
            coef = np.zeros(A, dtype=np.int64)
            for t in range(A):
                poly = np.zeros(A, dtype=np.int64)
                poly[0] = 1
                deg, den = 0, 1
                for t2 in range(A):
                    if t2 == t:
                        continue
                    r = int(F.x[S[t2]])
                    new = np.zeros(A, dtype=np.int64)
                    new[1:deg + 2] = poly[0:deg + 1]
                    new[0:deg + 1] = (new[0:deg + 1] - r * poly[0:deg + 1]) % q
                    poly, deg = new % q, deg + 1
                    den = den * ((int(F.x[S[t]]) - r) % q) % q
                coef = (coef + int(w[S[t]]) * pow(den, q - 2, q) * poly) % q
            dgt = max([i for i in range(A) if coef[i]] or [-1])
            checks += 1
            bad += (dgt < K) != bool(crit[j])
    print("self-test: %d exhaustive interpolation checks, %d mismatches"
          % (checks, bad))
    return bad == 0


def _flush(path, results):
    old = []
    if os.path.exists(path):
        try:
            old = json.load(open(path))
        except Exception:
            old = []
    names = [x["cfg"]["name"] for x in results]
    keep = [r for r in old if r["cfg"]["name"] not in names]
    with open(path, "w") as fh:
        json.dump(keep + results, fh, indent=1, default=str)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--only", default=None)
    ap.add_argument("--out", default="TOY.json")
    args = ap.parse_args()
    if args.self_test:
        sys.exit(0 if self_test() else 1)

    results = []
    names = [c["name"] for c in CONFIGS]
    want = args.only.split(",") if args.only else names
    for cfg in CONFIGS:
        if cfg["name"] not in want:
            continue
        t0 = time.time()
        n, A, K, h, q = cfg["n"], cfg["A"], cfg["K"], cfg["h"], cfg["q"]
        assert A - K == h
        q = next_prime_1modn(q, n)
        cfg = dict(cfg, q=q)
        F = Field(q, n)
        LA = LP = LM = None
        LA = Level(F, A, K)
        LP = Level(F, A + 1, K)
        LM = Level(F, A - 1, K)
        pr = predict(cfg)
        rng = np.random.default_rng(20260802 + sum(map(ord, cfg["name"])))
        recs = [run_trial(F, cfg, LA, LP, LM, rng) for _ in range(cfg["trials"])]

        def agg(key, cond=False):
            xs = [r[key] for r in recs if (not cond or r["admissible"])]
            return sum(xs) / len(xs) if xs else float("nan")

        nadm = sum(r["admissible"] for r in recs)
        Ns = np.array([r["N"] for r in recs], dtype=float)
        out = dict(
            cfg=cfg, predicted=pr, n_admissible=nadm,
            frac_admissible=nadm / cfg["trials"],
            E_N=float(Ns.mean()), Var_N=float(Ns.var(ddof=1)),
            E_N_over_mu=float(Ns.mean() / pr["mu"]),
            Var_over_mu=float(Ns.var(ddof=1) / pr["mu"]),
            E_live=agg("n_live"), E_gamma_lo=agg("gamma_lo_lex"),
            E_gamma_hi=agg("gamma_hi_lex"),
            E_gamma_lo_colex=agg("gamma_lo_colex"),
            E_N_adm=agg("N", True), E_live_adm=agg("n_live", True),
            E_gamma_lo_adm=agg("gamma_lo_lex", True),
            E_gamma_lo_colex_adm=agg("gamma_lo_colex", True),
            fail_t2=sum(1 for r in recs if r["t2"]),
            fail_jointA=sum(1 for r in recs if r["joint_A"]),
            fail_jointAm1=sum(1 for r in recs if r["joint_Am1"]),
            fail_vzero=sum(1 for r in recs if r["vzero"]),
            fail_fold=sum(1 for r in recs if r["fold"]),
            max_mult=max(r["max_mult"] for r in recs),
            secs=time.time() - t0)
        for tag in ("N", "live", "gamma_lo"):
            un = out["E_" + tag] if tag != "N" else out["E_N"]
            cn = out["E_%s_adm" % tag]
            out["cond_ratio_" + tag] = (cn / un) if un else float("nan")
        results.append(out)
        _flush(os.path.join(HERE, args.out), results)
        print("%-3s n=%2d A=%2d K=%2d h=%d q=%7d | mu=%8.3f  gate=%8.5f  "
              "P[core>=K]=%9.2e | adm %5.3f | E[N]/mu %6.3f Var/mu %6.3f | "
              "E[live] %8.3f  E[Glo] %8.3f | cond ratios  N %6.4f  live %6.4f"
              "  Glo %6.4f  [%.0fs]" %
              (cfg["name"], n, A, K, h, q, pr["mu"], pr["gate_T2"],
               pr["P_core_ge_K"], out["frac_admissible"], out["E_N_over_mu"],
               out["Var_over_mu"], out["E_live"], out["E_gamma_lo"],
               out["cond_ratio_N"], out["cond_ratio_live"],
               out["cond_ratio_gamma_lo"], out["secs"]))
        sys.stdout.flush()

    path = os.path.join(HERE, args.out)
    old = []
    if os.path.exists(path):
        try:
            old = json.load(open(path))
        except Exception:
            old = []
    keep = [r for r in old if r["cfg"]["name"] not in
            [x["cfg"]["name"] for x in results]]
    with open(path, "w") as fh:
        json.dump(keep + results, fh, indent=1, default=str)
    print("\nwrote %s" % path)


if __name__ == "__main__":
    main()
